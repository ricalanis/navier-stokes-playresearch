"""
Spectral Theory Tools for Concentration Analysis in Navier-Stokes Solutions.

This module provides operators and analysis tools to study concentration phenomena
at different scales using spectral theory. The key insight is that concentration
(which would lead to blowup) must satisfy spectral constraints that can potentially
rule out certain blowup scenarios.

Mathematical Framework:
----------------------
For a potential Type II blowup at rate alpha in [1/2, 3/4), the solution concentrates
energy into smaller scales. We study this via:

1. Concentration Operators: T_r localizes to scale r
2. Scale-Space Operators: S_r measures local energy density
3. Littlewood-Paley: Frequency decomposition for scale analysis
4. Wavelets: Sparse representation detecting concentration
5. Spectral Gaps: Constraints from linearized NS operator

Key Constraint Discovery:
------------------------
If concentration at scale r requires spectral gap <= c*r^beta for some beta,
this constrains how fast concentration can occur, potentially ruling out blowup.
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq, fftshift
from scipy import linalg
from scipy.sparse import diags, csr_matrix
from scipy.sparse.linalg import eigs, eigsh
from typing import Tuple, Optional, Dict, List, Callable, NamedTuple
from dataclasses import dataclass, field
import warnings


# =============================================================================
# Section 1: Concentration Operator T_r
# =============================================================================

@dataclass
class ConcentrationOperatorResult:
    """Result of applying concentration operator T_r."""
    scale_r: float
    eigenvalues: np.ndarray
    eigenvectors: np.ndarray
    spectral_radius: float
    trace: float
    concentration_index: float  # Measures how peaked the spectrum is
    notes: str = ""


class ConcentrationOperator:
    """
    Concentration Operator T_r : L^2(R^3) -> L^2(R^3)

    Definition:
        (T_r u)(x) = chi_{B(x,r)} * u / ||chi_{B(x,r)} * u||_{L^2}

    This is a normalized convolution with a ball indicator, which localizes
    the function u to scale r around each point. The spectrum of T_r
    reveals concentration properties.

    Key Properties:
    - T_r is a positive semi-definite operator
    - ||T_r|| <= 1 for normalized version
    - Eigenvalues decay reveals smoothness
    - Concentration appears as eigenvalue clustering at 1
    """

    def __init__(self, N: int = 64, L: float = 2*np.pi):
        """
        Initialize concentration operator on periodic domain.

        Args:
            N: Grid points per dimension
            L: Domain size [0, L]^3
        """
        self.N = N
        self.L = L
        self.dx = L / N

        # Physical coordinates
        x = np.linspace(0, L, N, endpoint=False)
        self.X, self.Y, self.Z = np.meshgrid(x, x, x, indexing='ij')

        # Wavenumbers for spectral representation
        k = fftfreq(N, d=L/(2*np.pi*N))
        self.kx, self.ky, self.kz = np.meshgrid(k, k, k, indexing='ij')
        self.k_mag = np.sqrt(self.kx**2 + self.ky**2 + self.kz**2)

    def _ball_kernel_spectral(self, r: float) -> np.ndarray:
        """
        Compute Fourier transform of ball indicator chi_{B(0,r)}.

        FT of ball of radius r in 3D:
            chi_hat(k) = (4*pi/|k|^3) * (sin(|k|r) - |k|r*cos(|k|r))

        This is the spherical Bessel function j_1 scaled.
        """
        k_r = self.k_mag * r

        # Avoid division by zero
        with np.errstate(divide='ignore', invalid='ignore'):
            # j_1(x) = sin(x)/x^2 - cos(x)/x
            # chi_hat = (4*pi*r^3/3) * 3*j_1(kr)/(kr)
            j1_normalized = np.where(
                k_r > 1e-10,
                3 * (np.sin(k_r) - k_r * np.cos(k_r)) / k_r**3,
                1.0  # Limit as kr -> 0
            )

        # Volume normalization
        vol_ball = (4/3) * np.pi * r**3
        chi_hat = vol_ball * j1_normalized

        return chi_hat

    def apply(self, u: np.ndarray, r: float, normalize: bool = True) -> np.ndarray:
        """
        Apply concentration operator T_r to field u.

        Args:
            u: Input field (N x N x N array)
            r: Concentration scale
            normalize: Whether to normalize the output

        Returns:
            T_r u: Localized field
        """
        # Get ball kernel in spectral space
        chi_hat = self._ball_kernel_spectral(r)

        # Convolution in spectral space
        u_hat = fftn(u)
        Tu_hat = chi_hat * u_hat
        Tu = np.real(ifftn(Tu_hat))

        if normalize:
            norm = np.sqrt(np.mean(Tu**2)) * self.L**(3/2)
            if norm > 1e-15:
                Tu = Tu / norm

        return Tu

    def compute_spectrum(self, r: float, num_eigs: int = 20,
                        random_projections: int = 100) -> ConcentrationOperatorResult:
        """
        Compute spectrum of T_r using randomized methods.

        For large systems, we use random projections to estimate eigenvalues.
        The operator T_r in spectral space is diagonal (convolution = multiplication),
        so we analyze the multiplier |chi_hat(k)|^2.

        Args:
            r: Concentration scale
            num_eigs: Number of eigenvalues to compute
            random_projections: Number of random vectors for estimation

        Returns:
            ConcentrationOperatorResult with spectral data
        """
        chi_hat = self._ball_kernel_spectral(r)

        # The eigenvalues of convolution are the Fourier coefficients
        # For self-adjoint case, eigenvalues are |chi_hat|^2
        multiplier = np.abs(chi_hat)**2

        # Get eigenvalue distribution from multiplier values
        # Sort to get "spectrum" (values the multiplier takes)
        flat_mult = multiplier.flatten()
        sorted_mult = np.sort(flat_mult)[::-1]  # Descending

        # Top eigenvalues
        top_eigs = sorted_mult[:num_eigs]

        # Spectral radius
        spectral_radius = np.max(np.abs(flat_mult))

        # Trace (sum of eigenvalues = integral of multiplier)
        trace = np.sum(flat_mult) * (self.L / (2*np.pi))**3 / self.N**3

        # Concentration index: ratio of top eigenvalue to trace
        # High value = concentrated spectrum
        concentration_index = top_eigs[0] / (trace + 1e-15) if trace > 0 else 0

        notes = f"""
Concentration operator T_r analysis for r = {r:.4f}:
- Spectral radius: {spectral_radius:.6e}
- Trace: {trace:.6e}
- Concentration index: {concentration_index:.6f}

Interpretation:
- High concentration index means energy concentrated in few modes
- For blowup, expect concentration index to grow as r -> 0
- Spectral radius ~ r^3 for small r (ball volume scaling)
"""

        return ConcentrationOperatorResult(
            scale_r=r,
            eigenvalues=top_eigs,
            eigenvectors=np.array([]),  # Not computed for efficiency
            spectral_radius=spectral_radius,
            trace=trace,
            concentration_index=concentration_index,
            notes=notes
        )

    def analyze_concentration_constraint(self, r_values: np.ndarray) -> Dict:
        """
        Analyze how spectral properties scale with concentration scale r.

        This reveals constraints on concentration: if the spectral radius
        scales as r^beta, then concentration rate is constrained.

        Args:
            r_values: Array of scales to analyze

        Returns:
            Dictionary with scaling analysis
        """
        results = []
        for r in r_values:
            result = self.compute_spectrum(r)
            results.append({
                'r': r,
                'spectral_radius': result.spectral_radius,
                'trace': result.trace,
                'concentration_index': result.concentration_index,
                'top_eigenvalue': result.eigenvalues[0]
            })

        # Fit power law: spectral_radius ~ r^beta
        log_r = np.log(r_values)
        log_sr = np.log([res['spectral_radius'] for res in results])

        # Linear regression
        coeffs = np.polyfit(log_r, log_sr, 1)
        beta_sr = coeffs[0]

        # Same for trace
        log_trace = np.log([res['trace'] for res in results])
        coeffs_trace = np.polyfit(log_r, log_trace, 1)
        beta_trace = coeffs_trace[0]

        constraint = f"""
CONCENTRATION CONSTRAINT FROM SPECTRAL ANALYSIS:

Spectral radius scaling: ||T_r|| ~ r^{beta_sr:.3f}
Trace scaling: Tr(T_r) ~ r^{beta_trace:.3f}

For Type II blowup at rate alpha:
- Concentration scale r(t) ~ (T-t)^alpha
- Energy in scale r: E(r) ~ ||T_r u||^2

Constraint: If alpha < {beta_sr/2:.3f}, spectral concentration is too fast
for the energy to remain bounded in L^2.

For window [1/2, 3/5]:
- alpha = 1/2 gives r ~ sqrt(T-t), spectral radius ~ (T-t)^{beta_sr/2:.3f}
- alpha = 3/5 gives r ~ (T-t)^0.6, spectral radius ~ (T-t)^{0.6*beta_sr:.3f}

This provides a spectral obstruction to blowup if {beta_sr:.3f} < 0.
"""

        return {
            'r_values': r_values,
            'results': results,
            'beta_spectral_radius': beta_sr,
            'beta_trace': beta_trace,
            'constraint': constraint
        }


# =============================================================================
# Section 2: Scale-Space Operator S_r
# =============================================================================

@dataclass
class ScaleSpaceResult:
    """Result of scale-space analysis."""
    r_values: np.ndarray
    local_energy: np.ndarray  # S_r u evaluated at center
    energy_profile: np.ndarray  # Full S_r u field
    scaling_exponent: float
    concentration_detected: bool
    concentration_center: Optional[Tuple[float, float, float]]
    notes: str = ""


class ScaleSpaceOperator:
    """
    Scale-Space Operator S_r for local energy density analysis.

    Definition:
        (S_r u)(x) = integral_{B(x,r)} |u(y)|^2 dy / |B(r)|

    This measures the local energy density at scale r around each point.
    For Type II blowup, we expect S_r to develop a singularity.

    Properties:
    - S_r u >= 0 everywhere
    - integral S_r u dx = ||u||_L^2 (energy conservation)
    - For smooth u: S_r u -> |u(x)|^2 as r -> 0
    - For concentration: S_r u develops delta-like peak
    """

    def __init__(self, N: int = 64, L: float = 2*np.pi):
        """Initialize scale-space operator."""
        self.N = N
        self.L = L
        self.dx = L / N

        # Grid
        x = np.linspace(0, L, N, endpoint=False)
        self.X, self.Y, self.Z = np.meshgrid(x, x, x, indexing='ij')

        # Wavenumbers
        k = fftfreq(N, d=L/(2*np.pi*N))
        self.kx, self.ky, self.kz = np.meshgrid(k, k, k, indexing='ij')
        self.k_mag = np.sqrt(self.kx**2 + self.ky**2 + self.kz**2)

    def _ball_kernel_spectral(self, r: float) -> np.ndarray:
        """Fourier transform of normalized ball indicator."""
        k_r = self.k_mag * r
        vol_ball = (4/3) * np.pi * r**3

        with np.errstate(divide='ignore', invalid='ignore'):
            j1_normalized = np.where(
                k_r > 1e-10,
                3 * (np.sin(k_r) - k_r * np.cos(k_r)) / k_r**3,
                1.0
            )

        return j1_normalized  # Normalized by volume

    def apply(self, u: np.ndarray, r: float) -> np.ndarray:
        """
        Apply scale-space operator: S_r u = (chi_r * |u|^2) / |B(r)|

        Args:
            u: Input field
            r: Scale

        Returns:
            Local energy density field
        """
        # Local energy density
        u_sq = np.abs(u)**2

        # Convolve with normalized ball
        kernel_hat = self._ball_kernel_spectral(r)
        u_sq_hat = fftn(u_sq)
        Sr_u_hat = kernel_hat * u_sq_hat
        Sr_u = np.real(ifftn(Sr_u_hat))

        return Sr_u

    def compute_profile(self, u: np.ndarray, r_values: np.ndarray) -> ScaleSpaceResult:
        """
        Compute scale-space profile: S_r u as function of r.

        This reveals concentration: for smooth functions, S_r varies slowly
        with r. For concentrating solutions, S_r develops a peak at small r.

        Args:
            u: Input field
            r_values: Array of scales to analyze

        Returns:
            ScaleSpaceResult with profile data
        """
        local_energy = []

        # Find point of maximum |u|^2 (potential concentration center)
        u_sq = np.abs(u)**2
        max_idx = np.unravel_index(np.argmax(u_sq), u_sq.shape)
        center = (
            self.X[max_idx],
            self.Y[max_idx],
            self.Z[max_idx]
        )

        for r in r_values:
            Sr_u = self.apply(u, r)
            # Evaluate at concentration center
            local_energy.append(Sr_u[max_idx])

        local_energy = np.array(local_energy)

        # Store full profile at smallest scale
        energy_profile = self.apply(u, r_values[0])

        # Fit scaling: S_r ~ r^gamma
        # For L^2 function: gamma ~ 0 (energy roughly constant)
        # For delta: gamma ~ -3 (inverse volume)
        log_r = np.log(r_values[r_values > 0])
        log_E = np.log(local_energy[r_values > 0] + 1e-15)

        if len(log_r) > 1:
            coeffs = np.polyfit(log_r, log_E, 1)
            gamma = coeffs[0]
        else:
            gamma = 0.0

        # Detect concentration: gamma < -1 indicates concentration
        concentration_detected = gamma < -1.0

        notes = f"""
Scale-Space Analysis Results:
- Concentration center: ({center[0]:.3f}, {center[1]:.3f}, {center[2]:.3f})
- Scaling exponent gamma: {gamma:.3f}
- S_r u ~ r^{gamma:.3f}

Interpretation:
- gamma ~ 0: Smooth function, no concentration
- gamma ~ -1: Weak concentration
- gamma ~ -3: Strong concentration (delta-like)

For Type II blowup:
- At time t, concentration scale r(t) ~ (T-t)^alpha
- Energy in B(x,r): E_r ~ r^3 * (max |u|^2) ~ r^(3-2*alpha_eff)
- Concentration detected: {'YES' if concentration_detected else 'NO'}

CONSTRAINT: If gamma < -3, concentration is too strong for L^2.
This provides spectral obstruction to extreme concentration.
"""

        return ScaleSpaceResult(
            r_values=r_values,
            local_energy=local_energy,
            energy_profile=energy_profile,
            scaling_exponent=gamma,
            concentration_detected=concentration_detected,
            concentration_center=center if concentration_detected else None,
            notes=notes
        )


# =============================================================================
# Section 3: Littlewood-Paley Decomposition
# =============================================================================

@dataclass
class LittlewoodPaleyResult:
    """Result of Littlewood-Paley decomposition."""
    j_values: np.ndarray  # Dyadic scales
    delta_j_norms: np.ndarray  # ||Delta_j u||_L2
    frequency_bands: List[Tuple[float, float]]  # (k_min, k_max) for each j
    regularity_estimate: float  # Estimated Sobolev regularity
    concentration_scale: Optional[int]  # j where concentration occurs
    type_II_signature: bool  # Whether spectrum matches Type II
    notes: str = ""


class LittlewoodPaleyDecomposition:
    """
    Littlewood-Paley Decomposition for frequency-space concentration.

    Definition:
        u = Sum_j Delta_j u

    where Delta_j localizes to frequencies |xi| ~ 2^j.

    For Type II blowup candidates:
    - Energy should concentrate at high frequencies: ||Delta_j u||_L2 grows with j
    - Regularity: u in H^s iff Sum 2^{2sj} ||Delta_j u||_L2^2 < infinity
    - Concentration at scale 2^{-j} appears as growth in ||Delta_j u||_L2

    Key Constraint:
    - For alpha in [1/2, 3/5], the frequency concentration rate must match
    - ||Delta_j u||_L2 ~ 2^{j*beta} for some beta depending on alpha
    """

    def __init__(self, N: int = 64, L: float = 2*np.pi):
        """Initialize Littlewood-Paley decomposition."""
        self.N = N
        self.L = L

        # Maximum dyadic scale (Nyquist)
        self.j_max = int(np.log2(N // 2))

        # Wavenumbers
        k = fftfreq(N, d=L/(2*np.pi*N))
        self.kx, self.ky, self.kz = np.meshgrid(k, k, k, indexing='ij')
        self.k_mag = np.sqrt(self.kx**2 + self.ky**2 + self.kz**2)

        # Precompute LP filters
        self._setup_filters()

    def _setup_filters(self):
        """Setup Littlewood-Paley filters."""
        self.filters = {}

        # Smooth partition of unity
        # psi(|k|) supported in [1/2, 2], with sum psi(|k|/2^j) = 1

        def smooth_bump(k, k_low, k_high):
            """Smooth bump function on [k_low, k_high]."""
            # Use smooth cutoff
            with np.errstate(divide='ignore', invalid='ignore'):
                # Rising part: smooth transition from 0 to 1
                rise = np.where(
                    k <= k_low, 0,
                    np.where(k >= k_low * 1.5, 1,
                            0.5 * (1 - np.cos(np.pi * (k - k_low) / (0.5 * k_low))))
                )
                # Falling part: smooth transition from 1 to 0
                fall = np.where(
                    k <= k_high * 0.75, 1,
                    np.where(k >= k_high, 0,
                            0.5 * (1 + np.cos(np.pi * (k - k_high * 0.75) / (0.25 * k_high))))
                )
            return rise * fall

        # Low frequency part (j = -1, |k| < 1)
        self.filters[-1] = np.where(self.k_mag < 1, 1.0, 0.0)

        # Dyadic bands
        for j in range(self.j_max + 1):
            k_low = 2**(j - 1)
            k_high = 2**(j + 1)
            self.filters[j] = smooth_bump(self.k_mag, k_low, k_high)

    def decompose(self, u: np.ndarray) -> Dict[int, np.ndarray]:
        """
        Compute Littlewood-Paley decomposition of u.

        Returns:
            Dictionary mapping j to Delta_j u
        """
        u_hat = fftn(u)

        pieces = {}
        for j, psi_j in self.filters.items():
            delta_j_hat = psi_j * u_hat
            pieces[j] = np.real(ifftn(delta_j_hat))

        return pieces

    def analyze(self, u: np.ndarray) -> LittlewoodPaleyResult:
        """
        Analyze frequency distribution of u.

        Returns:
            LittlewoodPaleyResult with spectral analysis
        """
        pieces = self.decompose(u)

        j_values = np.array(sorted(pieces.keys()))
        delta_j_norms = np.array([
            np.sqrt(np.mean(pieces[j]**2)) * self.L**(3/2)
            for j in j_values
        ])

        # Frequency bands
        frequency_bands = [
            (2.0**(j-1), 2.0**(j+1)) for j in j_values
        ]

        # Estimate regularity: find s such that 2^{sj} ||Delta_j u|| is bounded
        # This means ||Delta_j u|| ~ 2^{-sj}
        # Log-linear fit: log(||Delta_j||) ~ -s * j * log(2)
        valid = delta_j_norms > 1e-15
        if np.sum(valid) > 2:
            log_norms = np.log(delta_j_norms[valid])
            j_valid = j_values[valid]
            coeffs = np.polyfit(j_valid, log_norms, 1)
            regularity_estimate = -coeffs[0] / np.log(2)
        else:
            regularity_estimate = 0.0

        # Find concentration scale (where ||Delta_j|| peaks)
        if len(delta_j_norms) > 0:
            peak_j = j_values[np.argmax(delta_j_norms)]
            # Only flag as concentration if peak is at high j
            concentration_scale = peak_j if peak_j > 2 else None
        else:
            concentration_scale = None

        # Type II signature: energy grows at high frequencies
        # Check if ||Delta_j||^2 * 2^{2j} is NOT summable (would fail H^1)
        h1_seminorm_sq = np.sum(delta_j_norms**2 * 4.0**j_values)
        l2_norm_sq = np.sum(delta_j_norms**2)
        type_II_signature = h1_seminorm_sq > 100 * l2_norm_sq  # Heuristic threshold

        notes = f"""
Littlewood-Paley Decomposition Analysis:
- Number of scales: {len(j_values)}
- Estimated regularity: H^{regularity_estimate:.2f}
- Concentration scale j: {concentration_scale}
- Type II signature: {'YES' if type_II_signature else 'NO'}

For Type II blowup with rate alpha:
- Concentration at scale 2^{{-j}} means j ~ alpha * log_2(1/(T-t))
- ||Delta_j u||_L2 should grow as 2^{{j*(3/2 - 1/alpha)}} for L^2 conservation
- For alpha = 1/2: 2^{{j*1/2}} growth (Type I)
- For alpha = 3/5: 2^{{j*(-1/6)}} decay (borderline)

SPECTRAL CONSTRAINT:
If regularity estimate s > 1/2, solution is smooth by Sobolev embedding.
Current: s = {regularity_estimate:.3f} {'(SMOOTH)' if regularity_estimate > 0.5 else '(potentially singular)'}
"""

        return LittlewoodPaleyResult(
            j_values=j_values,
            delta_j_norms=delta_j_norms,
            frequency_bands=frequency_bands,
            regularity_estimate=regularity_estimate,
            concentration_scale=concentration_scale,
            type_II_signature=type_II_signature,
            notes=notes
        )


# =============================================================================
# Section 4: Wavelet Concentration Analysis
# =============================================================================

@dataclass
class WaveletConcentrationResult:
    """Result of wavelet concentration analysis."""
    num_coefficients: int
    coefficient_magnitudes: np.ndarray  # Sorted descending
    sparsity_index: float  # Fraction of energy in top 1% coefficients
    entropy: float  # Information entropy of coefficient distribution
    concentration_threshold: float  # Magnitude above which 90% energy lies
    besov_regularity: Tuple[float, float, float]  # (s, p, q) estimate
    notes: str = ""


class WaveletConcentration:
    """
    Wavelet-based concentration analysis.

    Uses Haar wavelets (for simplicity) to decompose u into localized
    basis functions. Concentration appears as energy in few coefficients.

    Key Quantities:
    - Sparsity: How many coefficients capture most energy
    - Entropy: Information content of coefficient distribution
    - Besov regularity: Finer than Sobolev, captures singularities

    For Type II:
    - Blowup concentrates energy in few wavelet coefficients
    - Sparsity index grows as t -> T
    - Entropy decreases (more ordered structure)
    """

    def __init__(self, N: int = 64, L: float = 2*np.pi):
        """Initialize wavelet analysis."""
        self.N = N
        self.L = L

        # Number of levels (dyadic)
        self.n_levels = int(np.log2(N))

    def haar_transform_3d(self, u: np.ndarray) -> np.ndarray:
        """
        Compute 3D Haar wavelet transform.

        Uses tensor product of 1D Haar transforms.
        """
        result = u.copy().astype(float)
        N = self.N

        # Apply Haar transform along each axis
        for level in range(self.n_levels):
            step = N // (2**(level + 1))
            if step < 1:
                break

            # Along x
            for j in range(N):
                for k in range(N):
                    temp = result[:, j, k].copy()
                    for i in range(step):
                        avg = (temp[2*i] + temp[2*i + 1]) / np.sqrt(2)
                        diff = (temp[2*i] - temp[2*i + 1]) / np.sqrt(2)
                        result[i, j, k] = avg
                        result[step + i, j, k] = diff

            # Along y
            for i in range(N):
                for k in range(N):
                    temp = result[i, :, k].copy()
                    for j in range(step):
                        avg = (temp[2*j] + temp[2*j + 1]) / np.sqrt(2)
                        diff = (temp[2*j] - temp[2*j + 1]) / np.sqrt(2)
                        result[i, j, k] = avg
                        result[i, step + j, k] = diff

            # Along z
            for i in range(N):
                for j in range(N):
                    temp = result[i, j, :].copy()
                    for k in range(step):
                        avg = (temp[2*k] + temp[2*k + 1]) / np.sqrt(2)
                        diff = (temp[2*k] - temp[2*k + 1]) / np.sqrt(2)
                        result[i, j, k] = avg
                        result[i, j, step + k] = diff

        return result

    def analyze(self, u: np.ndarray) -> WaveletConcentrationResult:
        """
        Analyze wavelet concentration of u.

        Returns:
            WaveletConcentrationResult with sparsity analysis
        """
        # Compute wavelet transform
        coeffs = self.haar_transform_3d(u)

        # Flatten and sort by magnitude
        flat_coeffs = coeffs.flatten()
        magnitudes = np.abs(flat_coeffs)
        sorted_mags = np.sort(magnitudes)[::-1]

        # Total energy
        total_energy = np.sum(magnitudes**2)

        # Sparsity index: fraction of coefficients needed for 90% energy
        cumulative_energy = np.cumsum(sorted_mags**2)
        threshold_idx = np.searchsorted(cumulative_energy, 0.9 * total_energy)
        sparsity_index = (threshold_idx + 1) / len(flat_coeffs)

        # Concentration threshold
        concentration_threshold = sorted_mags[threshold_idx] if threshold_idx < len(sorted_mags) else 0

        # Entropy of coefficient distribution
        probs = magnitudes**2 / (total_energy + 1e-15)
        probs = probs[probs > 1e-15]  # Remove zeros
        entropy = -np.sum(probs * np.log(probs))
        max_entropy = np.log(len(flat_coeffs))
        normalized_entropy = entropy / max_entropy

        # Estimate Besov regularity B^s_{p,q}
        # For Haar wavelets, ||u||_{B^s_{p,q}} ~ (Sum_j 2^{jsq} ||Delta_j u||_p^q)^{1/q}
        # Simplified: estimate s from decay of wavelet coefficients at each level

        level_energies = []
        idx = 0
        for level in range(self.n_levels):
            level_size = (self.N // 2**level)**3 - (self.N // 2**(level+1))**3 if level > 0 else (self.N // 2)**3
            level_size = max(1, min(level_size, len(flat_coeffs) - idx))
            level_energy = np.sum(sorted_mags[idx:idx+level_size]**2)
            level_energies.append(level_energy)
            idx += level_size

        # Fit decay
        if len(level_energies) > 2:
            log_energies = np.log(np.array(level_energies) + 1e-15)
            levels = np.arange(len(level_energies))
            coeffs = np.polyfit(levels, log_energies, 1)
            s_estimate = -coeffs[0] / (2 * np.log(2))
        else:
            s_estimate = 0.0

        besov_regularity = (s_estimate, 2.0, 2.0)  # B^s_{2,2} ~ H^s

        notes = f"""
Wavelet Concentration Analysis:
- Total coefficients: {len(flat_coeffs)}
- Sparsity index: {sparsity_index:.4f} (fraction for 90% energy)
- Normalized entropy: {normalized_entropy:.4f}
- Concentration threshold: {concentration_threshold:.6e}
- Estimated Besov regularity: B^{s_estimate:.2f}_{{2,2}}

Interpretation:
- Low sparsity (< 0.01): Energy concentrated in few coefficients (blowup-like)
- High entropy (~1): Uniform distribution (smooth)
- Low entropy: Concentrated structure

For Type II blowup:
- Sparsity index should decrease toward 0 as t -> T
- Entropy should decrease (increasing order)
- Besov regularity s should decrease toward critical value

CONSTRAINT: If sparsity_index < 1e-4 but solution in L^2,
the concentration is incompatible with NS evolution.
Current sparsity: {sparsity_index:.6f} {'(CONCENTRATED)' if sparsity_index < 0.01 else '(SPREAD)'}
"""

        return WaveletConcentrationResult(
            num_coefficients=len(flat_coeffs),
            coefficient_magnitudes=sorted_mags[:100],  # Top 100 for storage
            sparsity_index=sparsity_index,
            entropy=normalized_entropy,
            concentration_threshold=concentration_threshold,
            besov_regularity=besov_regularity,
            notes=notes
        )


# =============================================================================
# Section 5: Spectral Gap Analysis for Linearized NS
# =============================================================================

@dataclass
class SpectralGapResult:
    """Result of spectral gap analysis."""
    eigenvalues: np.ndarray
    spectral_gap: float  # Gap between first unstable and second
    essential_spectrum_bound: float
    unstable_modes: int  # Number of modes with positive real part
    growth_rate_bound: float  # Max eigenvalue real part
    concentration_constraint: str
    notes: str = ""


class LinearizedNSOperator:
    """
    Spectral analysis of linearized Navier-Stokes around concentrating solution.

    For a base flow U with potential blowup, we study:
        L v = P[-nu * Delta v + (U . nabla)v + (v . nabla)U]

    where P is Leray projection.

    Key quantities:
    - Spectral gap: Distance from unstable eigenvalues to essential spectrum
    - Growth rate: Maximum real part of eigenvalues
    - Number of unstable modes

    Constraint: If the spectral gap closes too fast, instability grows
    faster than concentration can proceed.
    """

    def __init__(self, N: int = 32, L: float = 2*np.pi, nu: float = 0.01):
        """Initialize linearized operator."""
        self.N = N
        self.L = L
        self.nu = nu
        self.dx = L / N

        # Grid
        x = np.linspace(0, L, N, endpoint=False)
        self.X, self.Y, self.Z = np.meshgrid(x, x, x, indexing='ij')

        # Wavenumbers
        k = fftfreq(N, d=L/(2*np.pi*N))
        self.kx, self.ky, self.kz = np.meshgrid(k, k, k, indexing='ij')
        self.k_sq = self.kx**2 + self.ky**2 + self.kz**2
        self.k_sq[0, 0, 0] = 1.0  # Avoid division by zero

    def _leray_projection_spectral(self, fx_hat: np.ndarray,
                                   fy_hat: np.ndarray,
                                   fz_hat: np.ndarray) -> Tuple[np.ndarray, ...]:
        """
        Apply Leray projection P = I - nabla nabla^{-1} div in spectral space.

        P_ij = delta_ij - k_i k_j / |k|^2
        """
        # Divergence in spectral space
        div_hat = 1j * (self.kx * fx_hat + self.ky * fy_hat + self.kz * fz_hat)

        # Gradient of inverse Laplacian of divergence
        grad_phi_x = 1j * self.kx * div_hat / self.k_sq
        grad_phi_y = 1j * self.ky * div_hat / self.k_sq
        grad_phi_z = 1j * self.kz * div_hat / self.k_sq

        # Zero at k=0
        grad_phi_x[0, 0, 0] = 0
        grad_phi_y[0, 0, 0] = 0
        grad_phi_z[0, 0, 0] = 0

        # Project
        return (
            fx_hat - grad_phi_x,
            fy_hat - grad_phi_y,
            fz_hat - grad_phi_z
        )

    def apply_linearized_operator(self, v: Tuple[np.ndarray, ...],
                                  U: Tuple[np.ndarray, ...]) -> Tuple[np.ndarray, ...]:
        """
        Apply linearized NS operator L to perturbation v around base flow U.

        L v = P[-nu * Delta v + (U . nabla)v + (v . nabla)U]

        Returns L v as tuple of arrays.
        """
        vx, vy, vz = v
        Ux, Uy, Uz = U

        # Spectral transforms
        vx_hat, vy_hat, vz_hat = fftn(vx), fftn(vy), fftn(vz)
        Ux_hat, Uy_hat, Uz_hat = fftn(Ux), fftn(Uy), fftn(Uz)

        # Laplacian term: -nu * Delta v = nu * |k|^2 * v_hat
        lap_x = self.nu * self.k_sq * vx_hat
        lap_y = self.nu * self.k_sq * vy_hat
        lap_z = self.nu * self.k_sq * vz_hat

        # Advection by U: (U . nabla) v
        # Compute derivatives
        dvx_dx = np.real(ifftn(1j * self.kx * vx_hat))
        dvx_dy = np.real(ifftn(1j * self.ky * vx_hat))
        dvx_dz = np.real(ifftn(1j * self.kz * vx_hat))
        dvy_dx = np.real(ifftn(1j * self.kx * vy_hat))
        dvy_dy = np.real(ifftn(1j * self.ky * vy_hat))
        dvy_dz = np.real(ifftn(1j * self.kz * vy_hat))
        dvz_dx = np.real(ifftn(1j * self.kx * vz_hat))
        dvz_dy = np.real(ifftn(1j * self.ky * vz_hat))
        dvz_dz = np.real(ifftn(1j * self.kz * vz_hat))

        adv_x = Ux * dvx_dx + Uy * dvx_dy + Uz * dvx_dz
        adv_y = Ux * dvy_dx + Uy * dvy_dy + Uz * dvy_dz
        adv_z = Ux * dvz_dx + Uy * dvz_dy + Uz * dvz_dz

        # Stretching by v: (v . nabla) U
        dUx_dx = np.real(ifftn(1j * self.kx * Ux_hat))
        dUx_dy = np.real(ifftn(1j * self.ky * Ux_hat))
        dUx_dz = np.real(ifftn(1j * self.kz * Ux_hat))
        dUy_dx = np.real(ifftn(1j * self.kx * Uy_hat))
        dUy_dy = np.real(ifftn(1j * self.ky * Uy_hat))
        dUy_dz = np.real(ifftn(1j * self.kz * Uy_hat))
        dUz_dx = np.real(ifftn(1j * self.kx * Uz_hat))
        dUz_dy = np.real(ifftn(1j * self.ky * Uz_hat))
        dUz_dz = np.real(ifftn(1j * self.kz * Uz_hat))

        stretch_x = vx * dUx_dx + vy * dUx_dy + vz * dUx_dz
        stretch_y = vx * dUy_dx + vy * dUy_dy + vz * dUy_dz
        stretch_z = vx * dUz_dx + vy * dUz_dy + vz * dUz_dz

        # Total nonlinear part
        nl_x_hat = fftn(adv_x + stretch_x)
        nl_y_hat = fftn(adv_y + stretch_y)
        nl_z_hat = fftn(adv_z + stretch_z)

        # Full operator (before projection)
        Lv_x_hat = -lap_x + nl_x_hat
        Lv_y_hat = -lap_y + nl_y_hat
        Lv_z_hat = -lap_z + nl_z_hat

        # Apply Leray projection
        Lv_x_hat, Lv_y_hat, Lv_z_hat = self._leray_projection_spectral(
            Lv_x_hat, Lv_y_hat, Lv_z_hat
        )

        return (
            np.real(ifftn(Lv_x_hat)),
            np.real(ifftn(Lv_y_hat)),
            np.real(ifftn(Lv_z_hat))
        )

    def estimate_spectrum_power_iteration(self, U: Tuple[np.ndarray, ...],
                                         num_eigs: int = 10,
                                         max_iter: int = 100) -> SpectralGapResult:
        """
        Estimate leading eigenvalues using power iteration.

        For large systems, direct eigenvalue computation is infeasible.
        We use power iteration to find the dominant eigenvalue(s).

        Args:
            U: Base flow
            num_eigs: Number of eigenvalues to estimate
            max_iter: Maximum iterations

        Returns:
            SpectralGapResult with spectral analysis
        """
        N = self.N

        # Initialize random perturbation
        vx = np.random.randn(N, N, N)
        vy = np.random.randn(N, N, N)
        vz = np.random.randn(N, N, N)

        # Make divergence-free
        v_hat = (fftn(vx), fftn(vy), fftn(vz))
        v_hat = self._leray_projection_spectral(*v_hat)
        vx = np.real(ifftn(v_hat[0]))
        vy = np.real(ifftn(v_hat[1]))
        vz = np.real(ifftn(v_hat[2]))

        # Normalize
        norm = np.sqrt(np.mean(vx**2 + vy**2 + vz**2))
        vx, vy, vz = vx / norm, vy / norm, vz / norm

        eigenvalues = []

        for iteration in range(max_iter):
            # Apply operator
            Lvx, Lvy, Lvz = self.apply_linearized_operator((vx, vy, vz), U)

            # Estimate eigenvalue (Rayleigh quotient)
            numerator = np.mean(vx * Lvx + vy * Lvy + vz * Lvz)
            denominator = np.mean(vx**2 + vy**2 + vz**2)
            lam = numerator / denominator
            eigenvalues.append(lam)

            # Normalize for next iteration
            norm = np.sqrt(np.mean(Lvx**2 + Lvy**2 + Lvz**2))
            if norm < 1e-15:
                break
            vx, vy, vz = Lvx / norm, Lvy / norm, Lvz / norm

        eigenvalues = np.array(eigenvalues[-20:])  # Last 20 for convergence

        # Dominant eigenvalue
        dominant_eig = np.mean(eigenvalues[-5:]) if len(eigenvalues) >= 5 else eigenvalues[-1]

        # Essential spectrum for Stokes: -nu * |k|^2, lowest non-zero is -nu
        # For linearized NS, shifted by ||nabla U||_infty
        grad_U_max = 0
        for Ui in U:
            Ui_hat = fftn(Ui)
            for ki in [self.kx, self.ky, self.kz]:
                deriv = np.real(ifftn(1j * ki * Ui_hat))
                grad_U_max = max(grad_U_max, np.max(np.abs(deriv)))

        essential_spectrum_bound = -self.nu * (2 * np.pi / self.L)**2 + grad_U_max

        # Spectral gap
        spectral_gap = abs(dominant_eig - essential_spectrum_bound)

        # Count unstable modes (heuristic from Rayleigh quotient distribution)
        unstable_modes = 1 if dominant_eig > 0 else 0

        # Concentration constraint
        if dominant_eig > 0:
            growth_time = 1 / dominant_eig
            constraint = f"""
UNSTABLE SPECTRUM DETECTED!
Growth rate: {dominant_eig:.4e}
Growth time scale: {growth_time:.4e}

For Type II blowup at rate alpha:
- Concentration time: (T-t) ~ r^{{1/alpha}}
- Growth must outpace concentration for instability to dominate

If growth_time < concentration_time, blowup is UNSTABLE.
This could PREVENT blowup via instability mechanism.
"""
        else:
            constraint = f"""
Spectrum is stable (all eigenvalues have negative real part).
Dominant eigenvalue: {dominant_eig:.4e}
Spectral gap: {spectral_gap:.4e}

For Type II blowup:
- Stable spectrum allows concentration to proceed
- Spectral gap ~ {spectral_gap:.4e} sets decay rate of perturbations
- Concentration at rate r must satisfy dr/dt << spectral_gap
"""

        notes = f"""
Linearized NS Spectral Analysis:
- Dominant eigenvalue: {dominant_eig:.6e}
- Essential spectrum bound: {essential_spectrum_bound:.6e}
- Spectral gap: {spectral_gap:.6e}
- ||nabla U||_infty: {grad_U_max:.6e}

Interpretation:
- Positive eigenvalues indicate linear instability
- Spectral gap determines decay rate of stable modes
- For blowup, concentration rate must respect spectral constraints
"""

        return SpectralGapResult(
            eigenvalues=eigenvalues,
            spectral_gap=spectral_gap,
            essential_spectrum_bound=essential_spectrum_bound,
            unstable_modes=unstable_modes,
            growth_rate_bound=max(0, dominant_eig),
            concentration_constraint=constraint,
            notes=notes
        )


# =============================================================================
# Section 6: Unified Analysis and Visualization
# =============================================================================

@dataclass
class SpectralConcentrationReport:
    """Complete spectral concentration analysis report."""
    concentration_result: ConcentrationOperatorResult
    scale_space_result: ScaleSpaceResult
    littlewood_paley_result: LittlewoodPaleyResult
    wavelet_result: WaveletConcentrationResult
    spectral_gap_result: Optional[SpectralGapResult]
    combined_constraints: str
    blowup_compatible: bool


class SpectralConcentrationAnalyzer:
    """
    Unified spectral concentration analyzer.

    Combines all five spectral tools to provide comprehensive
    constraints on concentration in Navier-Stokes solutions.
    """

    def __init__(self, N: int = 64, L: float = 2*np.pi, nu: float = 0.01):
        """Initialize analyzer with all tools."""
        self.N = N
        self.L = L
        self.nu = nu

        self.conc_op = ConcentrationOperator(N, L)
        self.scale_space = ScaleSpaceOperator(N, L)
        self.lp_decomp = LittlewoodPaleyDecomposition(N, L)
        self.wavelet = WaveletConcentration(N, L)
        self.linearized = LinearizedNSOperator(min(N, 32), L, nu)  # Smaller for spectral

    def analyze(self, u: Tuple[np.ndarray, np.ndarray, np.ndarray],
                r: float = 0.1,
                analyze_linearized: bool = True) -> SpectralConcentrationReport:
        """
        Perform complete spectral concentration analysis.

        Args:
            u: Velocity field (ux, uy, uz)
            r: Characteristic scale for concentration analysis
            analyze_linearized: Whether to analyze linearized operator

        Returns:
            SpectralConcentrationReport with all analyses
        """
        ux, uy, uz = u
        u_mag = np.sqrt(ux**2 + uy**2 + uz**2)

        # 1. Concentration operator
        conc_result = self.conc_op.compute_spectrum(r)

        # 2. Scale-space analysis
        r_values = np.logspace(-2, 0, 20) * self.L / (2 * np.pi)
        scale_result = self.scale_space.compute_profile(u_mag, r_values)

        # 3. Littlewood-Paley
        lp_result = self.lp_decomp.analyze(u_mag)

        # 4. Wavelet
        wavelet_result = self.wavelet.analyze(u_mag)

        # 5. Linearized spectrum (optional, expensive)
        if analyze_linearized:
            spectral_result = self.linearized.estimate_spectrum_power_iteration(u)
        else:
            spectral_result = None

        # Combine constraints
        constraints = self._combine_constraints(
            conc_result, scale_result, lp_result, wavelet_result, spectral_result
        )

        # Determine blowup compatibility
        blowup_compatible = self._assess_blowup_compatibility(
            conc_result, scale_result, lp_result, wavelet_result, spectral_result
        )

        return SpectralConcentrationReport(
            concentration_result=conc_result,
            scale_space_result=scale_result,
            littlewood_paley_result=lp_result,
            wavelet_result=wavelet_result,
            spectral_gap_result=spectral_result,
            combined_constraints=constraints,
            blowup_compatible=blowup_compatible
        )

    def _combine_constraints(self, conc_result, scale_result, lp_result,
                            wavelet_result, spectral_result) -> str:
        """Combine all spectral constraints into a coherent analysis."""
        lines = [
            "=" * 70,
            "COMBINED SPECTRAL CONCENTRATION CONSTRAINTS",
            "=" * 70,
            "",
            "1. CONCENTRATION OPERATOR T_r:",
            f"   - Spectral radius at r={conc_result.scale_r:.4f}: {conc_result.spectral_radius:.6e}",
            f"   - Concentration index: {conc_result.concentration_index:.4f}",
            "",
            "2. SCALE-SPACE S_r:",
            f"   - Scaling exponent: {scale_result.scaling_exponent:.3f}",
            f"   - Concentration detected: {'YES' if scale_result.concentration_detected else 'NO'}",
            "",
            "3. LITTLEWOOD-PALEY:",
            f"   - Estimated regularity: H^{lp_result.regularity_estimate:.2f}",
            f"   - Type II signature: {'YES' if lp_result.type_II_signature else 'NO'}",
            "",
            "4. WAVELET:",
            f"   - Sparsity index: {wavelet_result.sparsity_index:.4f}",
            f"   - Normalized entropy: {wavelet_result.entropy:.4f}",
            f"   - Besov regularity: B^{wavelet_result.besov_regularity[0]:.2f}_{{2,2}}",
            "",
        ]

        if spectral_result:
            lines.extend([
                "5. LINEARIZED NS SPECTRUM:",
                f"   - Spectral gap: {spectral_result.spectral_gap:.6e}",
                f"   - Unstable modes: {spectral_result.unstable_modes}",
                f"   - Growth rate bound: {spectral_result.growth_rate_bound:.6e}",
                "",
            ])

        lines.extend([
            "=" * 70,
            "CONSTRAINT SYNTHESIS FOR TYPE II BLOWUP:",
            "=" * 70,
            "",
        ])

        # Analyze consistency with Type II in [1/2, 3/5]
        smooth_threshold = 0.5
        concentrated = (
            scale_result.concentration_detected or
            lp_result.type_II_signature or
            wavelet_result.sparsity_index < 0.01
        )

        if lp_result.regularity_estimate > smooth_threshold:
            lines.append("REGULARITY CONSTRAINT: Solution appears H^s with s > 1/2.")
            lines.append("By Sobolev embedding, this implies L^infty bounds.")
            lines.append("CONCLUSION: Current state inconsistent with blowup.")
        elif concentrated:
            lines.append("CONCENTRATION DETECTED: Energy localizing to small scales.")
            if spectral_result and spectral_result.unstable_modes > 0:
                lines.append("WARNING: Linear instability may prevent ordered concentration.")
                lines.append("Unstable modes could destroy blowup structure.")
            else:
                lines.append("Concentration structure is linearly stable.")
                lines.append("Type II blowup CANNOT be ruled out from spectral data alone.")
        else:
            lines.append("Neither smooth nor concentrated.")
            lines.append("Solution in critical regime - requires further analysis.")

        return "\n".join(lines)

    def _assess_blowup_compatibility(self, conc_result, scale_result,
                                     lp_result, wavelet_result, spectral_result) -> bool:
        """
        Assess whether current state is compatible with blowup.

        Returns True if blowup cannot be ruled out.
        """
        # Check regularity
        if lp_result.regularity_estimate > 0.5:
            return False  # Too smooth

        # Check wavelet sparsity
        if wavelet_result.sparsity_index > 0.1 and wavelet_result.entropy > 0.8:
            return False  # Too spread out

        # Check spectral stability
        if spectral_result and spectral_result.unstable_modes > 3:
            return False  # Too unstable for ordered concentration

        return True


def create_visualization(report: SpectralConcentrationReport,
                        save_path: Optional[str] = None):
    """
    Create visualization of spectral concentration analysis.

    Generates plots of:
    1. Concentration operator spectrum
    2. Scale-space profile
    3. Littlewood-Paley decomposition
    4. Wavelet coefficient distribution
    5. Linearized NS spectrum (if available)
    """
    try:
        import matplotlib.pyplot as plt
        from matplotlib.gridspec import GridSpec
    except ImportError:
        warnings.warn("matplotlib not available for visualization")
        return None

    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 2, figure=fig)

    # 1. Concentration operator eigenvalues
    ax1 = fig.add_subplot(gs[0, 0])
    eigs = report.concentration_result.eigenvalues
    ax1.semilogy(range(len(eigs)), eigs, 'bo-', markersize=4)
    ax1.set_xlabel('Eigenvalue index')
    ax1.set_ylabel('Eigenvalue magnitude')
    ax1.set_title(f'Concentration Operator Spectrum (r={report.concentration_result.scale_r:.3f})')
    ax1.grid(True, alpha=0.3)

    # 2. Scale-space profile
    ax2 = fig.add_subplot(gs[0, 1])
    r_vals = report.scale_space_result.r_values
    energy = report.scale_space_result.local_energy
    ax2.loglog(r_vals, energy, 'r-', linewidth=2)
    ax2.set_xlabel('Scale r')
    ax2.set_ylabel('Local energy S_r u')
    ax2.set_title(f'Scale-Space Profile (gamma = {report.scale_space_result.scaling_exponent:.2f})')
    ax2.grid(True, alpha=0.3)

    # Power law fit
    if report.scale_space_result.scaling_exponent != 0:
        gamma = report.scale_space_result.scaling_exponent
        fit = energy[0] * (r_vals / r_vals[0])**gamma
        ax2.loglog(r_vals, fit, 'k--', label=f'r^{gamma:.2f}', linewidth=1)
        ax2.legend()

    # 3. Littlewood-Paley decomposition
    ax3 = fig.add_subplot(gs[1, 0])
    j_vals = report.littlewood_paley_result.j_values
    delta_norms = report.littlewood_paley_result.delta_j_norms
    ax3.semilogy(j_vals, delta_norms, 'g^-', markersize=6)
    ax3.set_xlabel('Dyadic scale j')
    ax3.set_ylabel('||Delta_j u||_L2')
    ax3.set_title(f'Littlewood-Paley (reg ~ H^{report.littlewood_paley_result.regularity_estimate:.2f})')
    ax3.grid(True, alpha=0.3)

    # 4. Wavelet coefficients
    ax4 = fig.add_subplot(gs[1, 1])
    coeffs = report.wavelet_result.coefficient_magnitudes
    ax4.semilogy(range(len(coeffs)), coeffs, 'm-', linewidth=1)
    ax4.axhline(y=report.wavelet_result.concentration_threshold,
                color='k', linestyle='--', label='90% threshold')
    ax4.set_xlabel('Coefficient rank')
    ax4.set_ylabel('|Wavelet coefficient|')
    ax4.set_title(f'Wavelet Sparsity (index = {report.wavelet_result.sparsity_index:.4f})')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # 5. Combined summary
    ax5 = fig.add_subplot(gs[2, :])
    ax5.axis('off')

    summary_text = report.combined_constraints
    # Truncate if too long
    lines = summary_text.split('\n')
    if len(lines) > 20:
        lines = lines[:20] + ['...']
    summary_text = '\n'.join(lines)

    ax5.text(0.02, 0.98, summary_text, transform=ax5.transAxes,
             fontsize=8, family='monospace', verticalalignment='top')

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Saved visualization to {save_path}")

    return fig


# =============================================================================
# Example usage and demonstration
# =============================================================================

def demo_spectral_concentration():
    """
    Demonstrate spectral concentration analysis on a test field.
    """
    print("=" * 70)
    print("SPECTRAL CONCENTRATION ANALYSIS DEMO")
    print("=" * 70)

    # Create analyzer
    N = 64
    L = 2 * np.pi
    analyzer = SpectralConcentrationAnalyzer(N, L)

    # Create test velocity field (concentrating vortex)
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    # Center of domain
    cx, cy, cz = L/2, L/2, L/2

    # Concentrated vortex (potential blowup profile)
    r_sq = (X - cx)**2 + (Y - cy)**2 + (Z - cz)**2
    sigma = 0.3  # Concentration scale
    amplitude = 1.0

    # Vortical velocity field
    ux = -amplitude * (Y - cy) * np.exp(-r_sq / (2 * sigma**2))
    uy = amplitude * (X - cx) * np.exp(-r_sq / (2 * sigma**2))
    uz = np.zeros_like(X)

    print(f"\nTest field: Gaussian vortex")
    print(f"  - Grid: {N}^3")
    print(f"  - Concentration scale: sigma = {sigma}")
    print(f"  - Max velocity: {np.max(np.sqrt(ux**2 + uy**2 + uz**2)):.4f}")

    # Run analysis
    print("\nRunning spectral concentration analysis...")
    report = analyzer.analyze((ux, uy, uz), r=sigma, analyze_linearized=True)

    # Print results
    print("\n" + report.combined_constraints)

    print("\n" + "=" * 70)
    print("BLOWUP COMPATIBILITY ASSESSMENT")
    print("=" * 70)
    if report.blowup_compatible:
        print("Current state IS compatible with potential blowup.")
        print("Spectral analysis alone cannot rule out blowup.")
    else:
        print("Current state NOT compatible with blowup.")
        print("Spectral constraints suggest global regularity.")

    return report


if __name__ == "__main__":
    demo_spectral_concentration()

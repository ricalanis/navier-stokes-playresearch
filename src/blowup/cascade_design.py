"""
Cascade Structure Design for Type II Blowup in Navier-Stokes.

This module implements the analysis of variable cascade factors f_k that could
potentially lead to Type II blowup while satisfying the necessary constraints:
- Dissipation integral must converge: integral ||nabla u||^2 dt < infinity
- But A_{m_1} must diverge: r^{-(2m-1)} ||u||^2_{L^2(B(r))} -> infinity

Mathematical Framework:
----------------------
Consider a cascade where energy is transferred between scales r_k = r_0 * lambda^{-k}
with variable transfer factor f_k = ||u||^2_{L^2(B(r_k))} / ||u||^2_{L^2(B(r_{k-1}))}.

Key Insight:
- Coherent cascade with constant f requires f >> 1 (impossible)
- Incoherent cascade terminates at dissipation scale
- But VARIABLE f(k) cascade might work!

For the cascade to produce blowup, we need:
- sum_k (4*f_k)^k < infinity (dissipation finite)
- sum_k (2^{2m-1}*f_k)^k = infinity (A_{m_1} diverges)

Since 4 > 2^{2m-1} for m in (1/2, 3/5), a decreasing f_k sequence might work.

References:
- Seregin (2024): Type II blowup analysis (arXiv:2507.08733)
- Hou-Luo (2014): Potentially singular solutions of 3D axisymmetric Euler
- Caffarelli-Kohn-Nirenberg (1982): Partial regularity
"""

import numpy as np
from typing import Tuple, Dict, List, Optional, NamedTuple, Callable
from dataclasses import dataclass, field
from scipy.optimize import minimize, minimize_scalar, brentq
from scipy.special import gamma as gamma_fn
import warnings


# =============================================================================
# Section 1: Cascade Configuration and Core Definitions
# =============================================================================

@dataclass
class CascadeConfig:
    """Configuration for cascade analysis."""
    # Scale ratio between successive shells
    lambda_scale: float = 2.0  # r_{k+1} = r_k / lambda

    # Initial scale
    r_0: float = 1.0

    # Number of cascade levels to analyze
    K_max: int = 100

    # Exponent m for A_m (Type II range: m in (1/2, 3/5))
    m: float = 0.55

    # Viscosity
    nu: float = 0.01

    # Time scale for cascade
    T_cascade: float = 1.0

    def __post_init__(self):
        """Validate configuration."""
        if not 0.5 < self.m < 0.6:
            warnings.warn(f"m={self.m} outside Type II window (1/2, 3/5)")
        if self.lambda_scale <= 1:
            raise ValueError("lambda_scale must be > 1")


class CascadeProfile(NamedTuple):
    """Profile of cascade factor sequence."""
    name: str
    f_k: Callable[[int], float]  # k -> f_k
    parameters: Dict[str, float]
    description: str


# =============================================================================
# Section 2: Variable Cascade Factor Analysis
# =============================================================================

@dataclass
class CascadeAnalysis:
    """
    Analyze variable cascade factor f_k for Type II blowup potential.

    For a cascade with f_k = ||u||^2_{L^2(B(r_k))} / ||u||^2_{L^2(B(r_{k-1}))}
    varying with scale k, we need:

    1. Dissipation Convergence: sum_k (4*f_k)^k < infinity
       - This requires (4*f_k)^k -> 0 fast enough
       - For f_k = c/k^gamma: need k * log(4c/k^gamma) -> -infinity

    2. A_{m_1} Divergence: sum_k (lambda^{2m-1} * f_k)^k = infinity
       - For m in (1/2, 3/5), lambda=2: 2^{2m-1} in (1, 2^{0.2}) ~ (1, 1.15)
       - Need (lambda^{2m-1} * f_k)^k to not decay too fast
    """

    config: CascadeConfig = field(default_factory=CascadeConfig)

    def _compute_critical_factors(self) -> Dict[str, float]:
        """
        Compute critical factors for cascade analysis.

        Returns:
            Dict with dissipation_factor (4 for lambda=2) and
            am_factor (2^{2m-1} for lambda=2)
        """
        lam = self.config.lambda_scale
        m = self.config.m

        # Dissipation factor: lambda^2 = 4 (for lambda=2)
        # This comes from ||nabla u||^2 ~ r^{-2} ||u||^2
        dissipation_factor = lam**2

        # A_m factor: lambda^{2m-1} for the quantity r^{-(2m-1)} ||u||^2
        am_factor = lam**(2 * m - 1)

        return {
            'dissipation_factor': dissipation_factor,
            'am_factor': am_factor,
            'ratio': dissipation_factor / am_factor,
            'm': m,
            'lambda': lam,
        }

    def analyze_power_law_cascade(self, c: float, gamma: float,
                                  verbose: bool = False) -> Dict[str, any]:
        """
        Analyze cascade with f_k = c / k^gamma.

        Key Observation:
        For f_k = c / k^gamma:
        - (a * f_k)^k = (a * c / k^gamma)^k = exp(k * log(a*c) - k*gamma*log(k))

        For large k:
        - If gamma > 0: k*gamma*log(k) dominates, so (a*f_k)^k -> 0
        - The rate depends on gamma

        Args:
            c: Coefficient in f_k = c/k^gamma
            gamma: Exponent in f_k = c/k^gamma
            verbose: Print detailed analysis

        Returns:
            Dict with convergence analysis
        """
        factors = self._compute_critical_factors()
        diss_factor = factors['dissipation_factor']
        am_factor = factors['am_factor']
        K = self.config.K_max

        # Compute series terms
        k_vals = np.arange(1, K + 1)
        f_k = c / k_vals**gamma

        # Dissipation series: sum_k (diss_factor * f_k)^k
        # = sum_k (4 * c / k^gamma)^k
        diss_terms = np.zeros(K)
        for i, k in enumerate(k_vals):
            log_term = k * np.log(diss_factor * c) - k * gamma * np.log(k)
            if log_term < 700:  # Avoid overflow
                diss_terms[i] = np.exp(log_term)
            else:
                diss_terms[i] = np.inf

        # A_m series: sum_k (am_factor * f_k)^k
        am_terms = np.zeros(K)
        for i, k in enumerate(k_vals):
            log_term = k * np.log(am_factor * c) - k * gamma * np.log(k)
            if log_term < 700:
                am_terms[i] = np.exp(log_term)
            else:
                am_terms[i] = np.inf

        # Partial sums
        diss_partial = np.cumsum(diss_terms)
        am_partial = np.cumsum(am_terms)

        # Check convergence
        # Series converges if terms decay to zero
        diss_converges = np.all(np.isfinite(diss_terms[-10:])) and \
                        diss_terms[-1] < diss_terms[-2] * 0.5

        # For A_m to diverge, we need terms to not decay too fast
        # or to have enough non-decaying terms
        am_diverges = np.sum(am_terms) > 1e6 or not np.all(np.isfinite(am_partial))

        # Asymptotic analysis
        # For (a*c/k^gamma)^k, the maximum occurs at k* where d/dk = 0
        # k * log(a*c) - k*gamma*log(k) max at k* = (a*c)^{1/gamma} / e^{1/gamma}
        k_star_diss = (diss_factor * c)**(1/gamma) / np.e**(1/gamma) if gamma > 0 else 1
        k_star_am = (am_factor * c)**(1/gamma) / np.e**(1/gamma) if gamma > 0 else 1

        if verbose:
            print(f"Power-law cascade analysis: f_k = {c:.4f} / k^{gamma:.4f}")
            print(f"  Dissipation factor: {diss_factor:.4f}")
            print(f"  A_m factor: {am_factor:.4f}")
            print(f"  Dissipation series sum: {diss_partial[-1]:.6e}")
            print(f"  A_m series sum: {am_partial[-1]:.6e}")
            print(f"  Dissipation converges: {diss_converges}")
            print(f"  A_m diverges: {am_diverges}")
            print(f"  Critical k for diss: {k_star_diss:.2f}")
            print(f"  Critical k for A_m: {k_star_am:.2f}")

        return {
            'c': c,
            'gamma': gamma,
            'f_k': f_k,
            'k_vals': k_vals,
            'diss_terms': diss_terms,
            'am_terms': am_terms,
            'diss_partial_sum': diss_partial,
            'am_partial_sum': am_partial,
            'diss_converges': diss_converges,
            'am_diverges': am_diverges,
            'blowup_possible': diss_converges and am_diverges,
            'k_star_diss': k_star_diss,
            'k_star_am': k_star_am,
            'factors': factors,
        }

    def find_blowup_regime(self, gamma_range: Tuple[float, float] = (0.1, 2.0),
                           c_range: Tuple[float, float] = (0.01, 1.0),
                           n_grid: int = 50) -> Dict:
        """
        Search for (c, gamma) pairs where Type II blowup might occur.

        A blowup regime requires:
        1. Dissipation converges: sum_k (4*f_k)^k < infinity
        2. A_m diverges: sum_k (2^{2m-1}*f_k)^k = infinity

        Args:
            gamma_range: Range of gamma values to search
            c_range: Range of c values to search
            n_grid: Grid resolution

        Returns:
            Dict with blowup regime map
        """
        factors = self._compute_critical_factors()
        diss_factor = factors['dissipation_factor']
        am_factor = factors['am_factor']

        gamma_vals = np.linspace(gamma_range[0], gamma_range[1], n_grid)
        c_vals = np.linspace(c_range[0], c_range[1], n_grid)

        # Store results
        diss_converges_map = np.zeros((n_grid, n_grid), dtype=bool)
        am_diverges_map = np.zeros((n_grid, n_grid), dtype=bool)
        blowup_map = np.zeros((n_grid, n_grid), dtype=bool)

        K = min(self.config.K_max, 200)  # Limit for efficiency
        k_vals = np.arange(1, K + 1)

        for i, gamma in enumerate(gamma_vals):
            for j, c in enumerate(c_vals):
                # Quick convergence test using asymptotic behavior
                # (a*c/k^gamma)^k ~ exp(k*log(a*c) - k*gamma*log(k))
                # For large k, this behaves like exp(-k*gamma*log(k)/c') for some c'

                f_k = c / k_vals**gamma

                # Dissipation convergence test
                diss_product = diss_factor * c
                # Check if series converges
                # Uses: sum_k a^k k^{-k*gamma} converges if a < 1 or gamma > 0
                if diss_product < 1:
                    diss_converges_map[i, j] = True
                elif gamma > 0:
                    # More careful test: compute partial sum
                    log_terms = k_vals * np.log(diss_product) - gamma * k_vals * np.log(k_vals)
                    finite_terms = log_terms[log_terms < 50]
                    if len(finite_terms) > 10:
                        diss_converges_map[i, j] = log_terms[-1] < -10

                # A_m divergence test
                am_product = am_factor * c
                if am_product >= 1:
                    am_diverges_map[i, j] = True
                elif gamma > 0:
                    # Check if sum diverges despite decay
                    log_terms = k_vals * np.log(am_product) - gamma * k_vals * np.log(k_vals)
                    # Diverges if maximum term is large enough
                    if np.max(log_terms) > 10:
                        am_diverges_map[i, j] = True

                blowup_map[i, j] = diss_converges_map[i, j] and am_diverges_map[i, j]

        # Find boundary curves
        blowup_region = np.where(blowup_map)

        return {
            'gamma_vals': gamma_vals,
            'c_vals': c_vals,
            'diss_converges': diss_converges_map,
            'am_diverges': am_diverges_map,
            'blowup_possible': blowup_map,
            'blowup_points': list(zip(gamma_vals[blowup_region[0]],
                                      c_vals[blowup_region[1]])),
            'factors': factors,
        }

    def design_optimal_cascade(self) -> Dict:
        """
        Design an optimal f_k profile for potential Type II blowup.

        Strategy:
        1. We need f_k -> 0 slowly so that:
           - (4*f_k)^k -> 0 (dissipation converges)
           - (2^{2m-1}*f_k)^k stays large enough (A_m diverges)

        2. Since 4 > 2^{2m-1} for m < 3/5, there's a window where this is possible.

        3. Try f_k = c / k^gamma with gamma tuned to hit the sweet spot.

        Returns:
            Dict with optimal cascade design
        """
        factors = self._compute_critical_factors()
        diss_factor = factors['dissipation_factor']
        am_factor = factors['am_factor']

        # The key constraint is:
        # 4 * f_k < 1 at some point (for diss convergence)
        # 2^{2m-1} * f_k > epsilon for longer (for A_m growth)

        # Critical observation:
        # If f_k = c/k^gamma, then (a*f_k)^k = (ac)^k / k^{gamma*k}
        # This goes to 0 for any gamma > 0, but the rate depends on a*c

        # For blowup, we want:
        # - diss_factor * c / k^gamma < 1 eventually -> 4c < k^gamma for large k
        # - am_factor * c / k^gamma * (number of terms) large

        # Optimal c satisfies: am_factor * c close to 1
        c_optimal = 1.0 / am_factor  # This makes am_factor * c = 1

        # Then choose gamma small but positive
        gamma_optimal = 0.5  # Start with square root decay

        # Verify this choice
        result = self.analyze_power_law_cascade(c_optimal, gamma_optimal,
                                                 verbose=True)

        # If not in blowup regime, adjust parameters
        if not result['blowup_possible']:
            # Try to find better parameters
            best_params = self._optimize_cascade_parameters()
            if best_params is not None:
                c_optimal, gamma_optimal = best_params
                result = self.analyze_power_law_cascade(c_optimal, gamma_optimal,
                                                         verbose=True)

        result['optimal_c'] = c_optimal
        result['optimal_gamma'] = gamma_optimal
        result['design_notes'] = f"""
Cascade Design for Type II Blowup (m = {self.config.m}):
---------------------------------------------------------
Dissipation factor: {diss_factor:.4f} (= lambda^2)
A_m factor: {am_factor:.4f} (= lambda^{{2m-1}})
Ratio: {factors['ratio']:.4f}

Chosen profile: f_k = {c_optimal:.4f} / k^{gamma_optimal:.4f}

Physical interpretation:
- Energy ratio between shells decreases with scale
- This allows dissipation to converge (less energy at small scales)
- But A_m can still diverge if the decrease is slow enough

Key insight: Since {diss_factor:.4f} > {am_factor:.4f}, there's a window
where dissipation converges but A_m diverges. The profile f_k ~ 1/k^0.5
attempts to exploit this gap.
"""

        return result

    def _optimize_cascade_parameters(self) -> Optional[Tuple[float, float]]:
        """
        Numerically optimize (c, gamma) for blowup regime.

        Returns:
            Optimal (c, gamma) if found, None otherwise
        """
        factors = self._compute_critical_factors()
        diss_factor = factors['dissipation_factor']
        am_factor = factors['am_factor']

        K = 100
        k_vals = np.arange(1, K + 1)

        def objective(params):
            c, gamma = params
            if c <= 0 or gamma <= 0:
                return 1e10

            f_k = c / k_vals**gamma

            # Compute series sums (log-scale for stability)
            diss_log = k_vals * np.log(diss_factor * c) - gamma * k_vals * np.log(k_vals)
            am_log = k_vals * np.log(am_factor * c) - gamma * k_vals * np.log(k_vals)

            # Want: diss sum finite, am sum large
            # Penalize: large diss sum, small am sum
            diss_max = np.max(diss_log)
            am_max = np.max(am_log)

            # Objective: minimize diss_max, maximize am_max
            # (want diss to converge fast, am to diverge or converge slowly)
            return diss_max - am_max

        from scipy.optimize import minimize

        # Try multiple starting points
        best_result = None
        best_score = np.inf

        for c0 in [0.1, 0.3, 0.5, 0.7, 1.0]:
            for gamma0 in [0.3, 0.5, 0.7, 1.0]:
                result = minimize(objective, [c0, gamma0],
                                method='Nelder-Mead',
                                options={'maxiter': 500})
                if result.fun < best_score:
                    best_score = result.fun
                    best_result = result.x

        if best_result is not None and all(p > 0 for p in best_result):
            return tuple(best_result)
        return None


# =============================================================================
# Section 3: Hou-Luo Style Cascade
# =============================================================================

@dataclass
class HouLuoCascade:
    """
    Cascade design compatible with Hou-Luo geometry.

    The Hou-Luo scenario features:
    - Axisymmetric flow
    - Boundary-driven concentration
    - Corner singularity structure at z-axis
    - Vorticity concentrating near axis

    Key Geometry:
    - Cylindrical coordinates (r, theta, z)
    - Vorticity omega_theta dominates near axis
    - Flow pushed toward corner by boundary conditions
    """

    config: CascadeConfig = field(default_factory=CascadeConfig)

    def axisymmetric_cascade_profile(self, n_scales: int = 50) -> Dict:
        """
        Design cascade profile for axisymmetric flow geometry.

        In Hou-Luo geometry:
        - r_k = r_0 * lambda^{-k} (radial scale toward axis)
        - z_k = z_0 * lambda^{-beta*k} for some beta ~ 1
        - Aspect ratio varies: d_k/r_k ~ lambda^{(1-beta)*k}

        The cascade factor f_k depends on the geometry:
        - For self-similar: f_k = const
        - For Type II: f_k must decrease to bound dissipation

        Returns:
            Dict with cascade profile and geometry
        """
        lam = self.config.lambda_scale
        m = self.config.m
        r_0 = self.config.r_0

        # Radial scales
        k_vals = np.arange(n_scales)
        r_k = r_0 * lam**(-k_vals)

        # For Hou-Luo, the aspect ratio (z-extent / r) grows
        # Use beta slightly less than 1 for focusing
        beta = 0.9

        z_k = r_0 * lam**(-beta * k_vals)
        aspect = z_k / r_k  # = lambda^{(1-beta)*k}, grows

        # Volume of concentration region
        vol_k = np.pi * r_k**2 * z_k

        # For Type II compatible cascade:
        # Energy in shell k: E_k ~ f_k * E_{k-1}
        # Dissipation in shell: D_k ~ nu * E_k / r_k^2

        # Design f_k to match Hou-Luo observations
        # The numerical data suggests omega_max ~ (T-t)^{-alpha} with alpha ~ 3/4
        # This implies specific energy concentration

        # For alpha ~ 3/4 (boundary of Type II):
        # f_k should scale to maintain omega ~ r^{-3/2}
        # With omega ~ E^{1/2} / r, we get E ~ omega^2 * r^2 ~ r^{-1}
        # So f_k ~ r_{k-1} / r_k = lambda

        # But this gives constant f_k = lambda, which doesn't work for Type II!
        # Need modification for true Type II (alpha < 3/4)

        # For Type II with alpha in (1/2, 3/4):
        # Want ||u||_infty ~ (T-t)^{-alpha}
        # Time to cascade to level k: t_k ~ sum_{j<k} r_j^2 / nu
        # So (T - t_k) ~ nu / r_k^2

        # Therefore ||u||_infty ~ (nu/r_k^2)^{-alpha} = (r_k^2/nu)^alpha

        # Energy at scale k: E_k ~ ||u||_infty^2 * r_k^3 ~ r_k^{3+4*alpha}
        # f_k = E_k / E_{k-1} ~ (r_k/r_{k-1})^{3+4*alpha} = lambda^{-(3+4*alpha)}

        alpha_hl = 0.65  # Typical Type II exponent
        f_hl = lam**(-(3 + 4 * alpha_hl))

        # This is a CONSTANT cascade factor, which cannot satisfy both constraints
        # Need VARIABLE f_k for true Type II

        # Modification: let alpha vary slightly with scale
        # alpha_k = alpha_0 + epsilon * k for small epsilon
        epsilon_alpha = 0.01  # Small drift

        alpha_k = alpha_hl + epsilon_alpha * k_vals
        f_k_variable = lam**(-(3 + 4 * alpha_k))

        return {
            'k_vals': k_vals,
            'r_k': r_k,
            'z_k': z_k,
            'aspect_ratio': aspect,
            'volume': vol_k,
            'f_k_constant': f_hl,
            'f_k_variable': f_k_variable,
            'alpha_k': alpha_k,
            'geometry_params': {
                'beta': beta,
                'r_0': r_0,
                'lambda': lam,
            },
            'notes': f"""
Hou-Luo Compatible Cascade Analysis:
------------------------------------
Base alpha: {alpha_hl:.3f}
Lambda: {lam:.2f}
Constant f: {f_hl:.6f}

For constant f = {f_hl:.6f}:
- Dissipation series: sum_k ({lam**2 * f_hl:.4f})^k
- A_m series: sum_k ({lam**(2*m-1) * f_hl:.4f})^k

Key observation: Constant f_k = lambda^{{-(3+4*alpha)}} gives
- Diss factor * f = {lam**2 * f_hl:.6f}
- A_m factor * f = {lam**(2*m-1) * f_hl:.6f}

For Type II, we need variable alpha_k that increases slowly,
making f_k decrease and allowing dissipation to converge while
A_m can still grow.
"""
        }

    def strain_vorticity_alignment(self, omega: np.ndarray,
                                    strain: np.ndarray) -> Dict:
        """
        Analyze strain-vorticity alignment at each scale.

        For blowup, the vorticity should align with the stretching
        direction of strain. In Hou-Luo geometry, this happens naturally
        near the axis where omega_theta aligns with S_rtheta.

        Args:
            omega: Vorticity field (N, N, N, 3)
            strain: Strain tensor (N, N, N, 3, 3)

        Returns:
            Dict with alignment analysis
        """
        # Compute vorticity-strain alignment: omega . S . omega / |omega|^2 / |S|
        omega_mag = np.sqrt(np.sum(omega**2, axis=-1))
        strain_mag = np.sqrt(np.sum(strain**2, axis=(-1, -2)))

        # omega . S . omega (stretching term coefficient)
        omega_S_omega = np.einsum('...i,...ij,...j->...', omega, strain, omega)

        # Alignment parameter
        alignment = np.zeros_like(omega_mag)
        mask = (omega_mag > 1e-10) & (strain_mag > 1e-10)
        alignment[mask] = omega_S_omega[mask] / (omega_mag[mask]**2 * strain_mag[mask])

        return {
            'alignment': alignment,
            'max_alignment': np.max(alignment),
            'mean_alignment': np.mean(alignment[mask]) if np.any(mask) else 0,
            'alignment_distribution': np.histogram(alignment[mask], bins=50)[0],
        }


# =============================================================================
# Section 4: NS Compatibility Checker
# =============================================================================

class NSCompatibilityChecker:
    """
    Check if a proposed cascade profile is compatible with NS dynamics.

    The cascade f_k must be realizable by NS evolution, which imposes:
    1. Energy transfer must obey NS nonlinearity structure
    2. Vortex stretching must provide required amplification
    3. Time scales must be consistent

    Key Constraints:
    - Energy cascade rate: dE_k/dt ~ -nu*|k|^2*E_k + transfer terms
    - Vorticity stretching: d|omega|/dt ~ |omega| * |S|
    - Time scale: delta_t_k ~ r_k^2 / nu (viscous) or r_k / u_k (advective)
    """

    def __init__(self, config: CascadeConfig):
        self.config = config
        self.analyzer = CascadeAnalysis(config)

    def check_energy_transfer_rate(self, f_k: np.ndarray) -> Dict:
        """
        Check if energy transfer rate is NS-compatible.

        For NS, the energy flux Pi_k at wavenumber k satisfies:
        - Pi_k bounded by ||u||^3 ||nabla u|| (Kolmogorov-like)
        - For 3D: Pi ~ epsilon^{1/4} * nu^{3/4} * k^{5/4} (Kolmogorov)

        Args:
            f_k: Cascade factors at each scale

        Returns:
            Dict with compatibility analysis
        """
        lam = self.config.lambda_scale
        nu = self.config.nu
        r_0 = self.config.r_0

        K = len(f_k)
        k_vals = np.arange(K)

        # Scales
        r_k = r_0 * lam**(-k_vals)
        wavenumber_k = 2 * np.pi / r_k

        # Energy at each scale (assuming initial E_0 = 1)
        E_k = np.zeros(K)
        E_k[0] = 1.0
        for k in range(1, K):
            E_k[k] = f_k[k] * E_k[k-1]

        # Velocity estimate: |u_k| ~ sqrt(E_k / r_k^3)
        u_k = np.sqrt(E_k / r_k**3)

        # Time scale for cascade to level k
        # Advective: t_adv ~ r_k / u_k
        t_adv_k = r_k / (u_k + 1e-15)

        # Viscous: t_visc ~ r_k^2 / nu
        t_visc_k = r_k**2 / nu

        # The cascade time is limited by the slower of these
        t_cascade_k = np.minimum(t_adv_k, t_visc_k)

        # Energy transfer rate: dE_k/dt ~ E_k / t_cascade_k
        dE_dt = E_k / (t_cascade_k + 1e-15)

        # NS compatibility: transfer rate should not exceed u_k^3 / r_k
        # (from dimensional analysis of NS nonlinearity)
        max_transfer = u_k**3 / r_k
        is_compatible = dE_dt <= max_transfer * 10  # Allow factor of 10 margin

        # Kolmogorov cascade prediction
        # In inertial range: Pi ~ epsilon = const
        # epsilon ~ u_k^3 / r_k ~ E_k^{3/2} / r_k^{5.5}
        epsilon_k = u_k**3 / r_k

        return {
            'k_vals': k_vals,
            'r_k': r_k,
            'E_k': E_k,
            'u_k': u_k,
            't_advective': t_adv_k,
            't_viscous': t_visc_k,
            't_cascade': t_cascade_k,
            'energy_transfer_rate': dE_dt,
            'max_allowed_rate': max_transfer,
            'is_compatible': is_compatible,
            'epsilon_k': epsilon_k,
            'kolmogorov_compatible': np.all(is_compatible),
        }

    def check_vortex_stretching(self, f_k: np.ndarray) -> Dict:
        """
        Check if vortex stretching can sustain the cascade.

        Vorticity equation: d|omega|/dt = (omega . S . omega_hat) ~ |omega| * |S|
        For blowup, stretching must dominate diffusion.

        Args:
            f_k: Cascade factors

        Returns:
            Dict with vortex stretching analysis
        """
        lam = self.config.lambda_scale
        nu = self.config.nu
        r_0 = self.config.r_0

        K = len(f_k)
        k_vals = np.arange(K)
        r_k = r_0 * lam**(-k_vals)

        # Energy at each scale
        E_k = np.zeros(K)
        E_k[0] = 1.0
        for k in range(1, K):
            E_k[k] = f_k[k] * E_k[k-1]

        # Velocity and vorticity estimates
        u_k = np.sqrt(E_k / r_k**3)
        # Vorticity: omega ~ u / r
        omega_k = u_k / r_k

        # Strain magnitude: S ~ omega (rough estimate)
        S_k = omega_k

        # Stretching rate: gamma_stretch ~ omega * S
        stretch_rate = omega_k * S_k

        # Diffusion rate: gamma_diff ~ nu * omega / r^2 = nu * |nabla omega|
        diffusion_rate = nu * omega_k / r_k**2

        # For blowup, need stretch > diffusion
        stretching_dominates = stretch_rate > diffusion_rate

        # Ratio indicates strength of nonlinearity
        stretch_diff_ratio = stretch_rate / (diffusion_rate + 1e-15)

        return {
            'k_vals': k_vals,
            'r_k': r_k,
            'omega_k': omega_k,
            'strain_k': S_k,
            'stretching_rate': stretch_rate,
            'diffusion_rate': diffusion_rate,
            'ratio': stretch_diff_ratio,
            'stretching_dominates': stretching_dominates,
            'blowup_favorable': np.any(stretch_diff_ratio > 1),
        }

    def full_compatibility_check(self, c: float, gamma: float) -> Dict:
        """
        Perform full NS compatibility check for f_k = c/k^gamma cascade.

        Args:
            c: Coefficient
            gamma: Exponent

        Returns:
            Comprehensive compatibility analysis
        """
        K = self.config.K_max
        k_vals = np.arange(1, K + 1)
        f_k = c / k_vals**gamma

        # Get cascade analysis
        cascade_result = self.analyzer.analyze_power_law_cascade(c, gamma)

        # Check energy transfer
        energy_check = self.check_energy_transfer_rate(f_k)

        # Check vortex stretching
        stretch_check = self.check_vortex_stretching(f_k)

        # Overall compatibility
        is_ns_compatible = energy_check['kolmogorov_compatible'] and \
                          stretch_check['blowup_favorable']

        is_type_ii_possible = cascade_result['blowup_possible'] and is_ns_compatible

        return {
            'cascade_analysis': cascade_result,
            'energy_transfer': energy_check,
            'vortex_stretching': stretch_check,
            'ns_compatible': is_ns_compatible,
            'type_ii_possible': is_type_ii_possible,
            'summary': f"""
NS Compatibility Check for f_k = {c:.4f}/k^{gamma:.4f}
======================================================
Cascade Analysis:
  - Dissipation converges: {cascade_result['diss_converges']}
  - A_m diverges: {cascade_result['am_diverges']}
  - Blowup regime: {cascade_result['blowup_possible']}

Energy Transfer:
  - Kolmogorov compatible: {energy_check['kolmogorov_compatible']}

Vortex Stretching:
  - Stretching can dominate: {stretch_check['blowup_favorable']}
  - Max stretch/diff ratio: {np.max(stretch_check['ratio']):.4f}

Overall Assessment:
  - NS Compatible: {is_ns_compatible}
  - Type II Blowup Possible: {is_type_ii_possible}
"""
        }


# =============================================================================
# Section 5: Cascade Evolution Simulator
# =============================================================================

@dataclass
class CascadeDesigner:
    """
    High-level interface for cascade design and analysis.

    Combines all tools to design, analyze, and verify cascade structures
    that could potentially lead to Type II blowup.
    """

    config: CascadeConfig = field(default_factory=CascadeConfig)

    def __post_init__(self):
        self.analyzer = CascadeAnalysis(self.config)
        self.hou_luo = HouLuoCascade(self.config)
        self.checker = NSCompatibilityChecker(self.config)

    def design_blowup_cascade(self, strategy: str = 'power_law') -> Dict:
        """
        Design a cascade that could lead to Type II blowup.

        Args:
            strategy: 'power_law', 'hou_luo', or 'optimal'

        Returns:
            Complete cascade design with analysis
        """
        if strategy == 'power_law':
            # Find optimal power law parameters
            result = self.analyzer.design_optimal_cascade()
            c, gamma = result['optimal_c'], result['optimal_gamma']

        elif strategy == 'hou_luo':
            # Use Hou-Luo compatible cascade
            hl_result = self.hou_luo.axisymmetric_cascade_profile()
            # Extract variable f_k and fit to power law
            f_k = hl_result['f_k_variable']
            k_vals = hl_result['k_vals'][1:]  # Skip k=0
            # Fit: log(f_k) = log(c) - gamma * log(k)
            log_f = np.log(f_k[1:] + 1e-15)
            log_k = np.log(k_vals)
            # Linear regression
            slope, intercept = np.polyfit(log_k, log_f, 1)
            gamma = -slope
            c = np.exp(intercept)
            result = self.analyzer.analyze_power_law_cascade(c, gamma)

        elif strategy == 'optimal':
            # Search over parameter space
            regime = self.analyzer.find_blowup_regime()
            if len(regime['blowup_points']) > 0:
                # Take first blowup point
                gamma, c = regime['blowup_points'][0]
            else:
                # Default to power law
                result = self.analyzer.design_optimal_cascade()
                c, gamma = result['optimal_c'], result['optimal_gamma']
            result = self.analyzer.analyze_power_law_cascade(c, gamma)

        else:
            raise ValueError(f"Unknown strategy: {strategy}")

        # Check NS compatibility
        compatibility = self.checker.full_compatibility_check(c, gamma)

        return {
            'strategy': strategy,
            'c': c,
            'gamma': gamma,
            'cascade_analysis': result,
            'ns_compatibility': compatibility,
            'final_verdict': compatibility['type_ii_possible'],
        }

    def evolve_cascade(self, f_k: np.ndarray, T_final: float = 1.0,
                       n_steps: int = 1000) -> Dict:
        """
        Evolve the cascade in time and track key quantities.

        Simplified model: E_k(t) evolves according to
        dE_k/dt = -gamma_k * E_k + f_k * gamma_{k-1} * E_{k-1}

        where gamma_k is the transfer rate at scale k.

        Args:
            f_k: Cascade factors
            T_final: Final time
            n_steps: Number of time steps

        Returns:
            Evolution history
        """
        lam = self.config.lambda_scale
        nu = self.config.nu
        m = self.config.m
        r_0 = self.config.r_0

        K = len(f_k)
        k_vals = np.arange(K)
        r_k = r_0 * lam**(-k_vals)

        # Limit scales to avoid numerical overflow
        # For k > ~30 with lambda=2, r_k < 1e-9 which causes overflow
        K_effective = min(K, 30)
        r_k_eff = r_k[:K_effective]
        f_k_eff = f_k[:K_effective]

        # Time stepping
        dt = T_final / n_steps
        times = np.linspace(0, T_final, n_steps + 1)

        # Initialize energy
        E = np.zeros((n_steps + 1, K_effective))
        E[0, 0] = 1.0  # All energy at largest scale initially

        # Dissipation history
        dissipation = np.zeros(n_steps + 1)

        # A_m history
        A_m = np.zeros(n_steps + 1)

        for n in range(n_steps):
            # Transfer rates (viscous timescale)
            gamma_k = nu / r_k_eff**2

            # Clamp gamma to avoid overflow
            gamma_k = np.minimum(gamma_k, 1e10)

            # Energy transfer (simplified cascade model)
            dE = np.zeros(K_effective)

            # Outflow from each scale
            dE -= gamma_k * E[n]

            # Inflow from previous scale
            for k in range(1, K_effective):
                dE[k] += f_k_eff[k] * gamma_k[k-1] * E[n, k-1]

            # Update energy with stability check
            E[n+1] = E[n] + dt * dE
            E[n+1] = np.maximum(E[n+1], 0)  # Ensure non-negative
            E[n+1] = np.minimum(E[n+1], 1e10)  # Cap to avoid overflow

            # Compute dissipation: nu * sum_k E_k / r_k^2
            diss_terms = E[n+1] / r_k_eff**2
            diss_terms = np.minimum(diss_terms, 1e10)  # Cap to avoid overflow
            dissipation[n+1] = nu * np.sum(diss_terms)

            # Compute A_m: sum_k r_k^{-(2m-1)} * E_k
            am_terms = r_k_eff**(-(2*m - 1)) * E[n+1]
            am_terms = np.minimum(am_terms, 1e10)  # Cap to avoid overflow
            A_m[n+1] = np.sum(am_terms)

        # Integrated dissipation using trapezoidal rule
        total_dissipation = np.trapezoid(dissipation, times)

        # Check for numerical validity
        valid = np.all(np.isfinite(dissipation)) and np.all(np.isfinite(A_m))

        return {
            'times': times,
            'energy': E,
            'dissipation': dissipation,
            'A_m': A_m,
            'total_dissipation': total_dissipation,
            'final_A_m': A_m[-1],
            'r_k': r_k_eff,
            'f_k': f_k_eff,
            'blowup_indicator': A_m[-1] > 1e6 and total_dissipation < 1e6,
            'numerical_valid': valid,
        }

    def comprehensive_analysis(self, verbose: bool = True) -> Dict:
        """
        Perform comprehensive cascade analysis for Type II blowup.

        Returns:
            Complete analysis with all results
        """
        results = {}

        # 1. Find optimal power law cascade
        if verbose:
            print("=" * 60)
            print("COMPREHENSIVE TYPE II BLOWUP CASCADE ANALYSIS")
            print("=" * 60)
            print(f"\nConfiguration: m = {self.config.m}, lambda = {self.config.lambda_scale}")

        optimal = self.analyzer.design_optimal_cascade()
        results['optimal_cascade'] = optimal

        if verbose:
            print(f"\nOptimal cascade: f_k = {optimal['optimal_c']:.4f} / k^{optimal['optimal_gamma']:.4f}")
            print(f"  Dissipation converges: {optimal['diss_converges']}")
            print(f"  A_m diverges: {optimal['am_diverges']}")
            print(f"  Blowup possible: {optimal['blowup_possible']}")

        # 2. Search for blowup regime
        regime = self.analyzer.find_blowup_regime()
        results['blowup_regime'] = regime

        if verbose:
            n_blowup = len(regime['blowup_points'])
            print(f"\nBlowup regime search: Found {n_blowup} parameter combinations")

        # 3. Hou-Luo analysis
        hou_luo = self.hou_luo.axisymmetric_cascade_profile()
        results['hou_luo_cascade'] = hou_luo

        if verbose:
            print(f"\nHou-Luo compatible cascade:")
            print(f"  Constant f (Type I-like): {hou_luo['f_k_constant']:.6f}")

        # 4. NS compatibility check for optimal cascade
        c, gamma = optimal['optimal_c'], optimal['optimal_gamma']
        compatibility = self.checker.full_compatibility_check(c, gamma)
        results['ns_compatibility'] = compatibility

        if verbose:
            print(f"\nNS Compatibility:")
            print(f"  Energy transfer OK: {compatibility['energy_transfer']['kolmogorov_compatible']}")
            print(f"  Stretching favorable: {compatibility['vortex_stretching']['blowup_favorable']}")
            print(f"  Overall NS compatible: {compatibility['ns_compatible']}")

        # 5. Evolution simulation
        K = 50
        k_vals = np.arange(1, K + 1)
        f_k = c / k_vals**gamma
        evolution = self.evolve_cascade(f_k, T_final=10.0, n_steps=1000)
        results['cascade_evolution'] = evolution

        if verbose:
            print(f"\nCascade evolution:")
            print(f"  Total dissipation: {evolution['total_dissipation']:.6e}")
            print(f"  Final A_m: {evolution['final_A_m']:.6e}")
            print(f"  Blowup indicator: {evolution['blowup_indicator']}")

        # 6. Final assessment
        final_verdict = optimal['blowup_possible'] and compatibility['ns_compatible']
        results['final_verdict'] = final_verdict

        if verbose:
            print("\n" + "=" * 60)
            print("FINAL VERDICT")
            print("=" * 60)
            if final_verdict:
                print("Type II blowup MAY BE POSSIBLE with this cascade structure.")
                print("The cascade satisfies both mathematical constraints and NS compatibility.")
            else:
                print("Type II blowup UNLIKELY with simple power-law cascade.")
                reasons = []
                if not optimal['diss_converges']:
                    reasons.append("- Dissipation series diverges")
                if not optimal['am_diverges']:
                    reasons.append("- A_m series converges (no blowup)")
                if not compatibility['ns_compatible']:
                    reasons.append("- Cascade not NS-compatible")
                print("Reasons:")
                print("\n".join(reasons))

        return results


# =============================================================================
# Section 6: Utility Functions
# =============================================================================

def demonstrate_cascade_analysis():
    """
    Demonstrate the cascade analysis tools.

    This function shows how the various components work together
    to analyze potential Type II blowup scenarios.
    """
    print("=" * 70)
    print("CASCADE DESIGN FOR TYPE II BLOWUP - DEMONSTRATION")
    print("=" * 70)

    # Create configuration
    config = CascadeConfig(
        lambda_scale=2.0,
        m=0.55,  # In Type II range (1/2, 3/5)
        nu=0.01,
        K_max=100,
    )

    print(f"\nConfiguration:")
    print(f"  Scale ratio lambda = {config.lambda_scale}")
    print(f"  Type II exponent m = {config.m}")
    print(f"  Viscosity nu = {config.nu}")

    # Create designer
    designer = CascadeDesigner(config)

    # Run comprehensive analysis
    results = designer.comprehensive_analysis(verbose=True)

    return results


if __name__ == "__main__":
    results = demonstrate_cascade_analysis()

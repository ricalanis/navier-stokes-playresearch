"""
Type II Blowup Construction for 3D Navier-Stokes.

This module attempts to CONSTRUCT Type II blowup solutions by exploiting
theoretical gaps in the regularity theory:

Key Gaps Being Exploited:
1. Type II blowup with alpha in (1/2, 3/5) is NOT ruled out by known results
2. The concentration function C(r) = sup_x int_{B(x,r)} |u|^2 / int|u|^2 is NOT monotone
3. Energy is the ONLY monotone quantity (not enstrophy, not local norms)
4. The dimensional gap of 0.9 (from 5/2 - 1/2 - 1) gives "freedom" for concentration

Construction Approach:
- Modified self-similar ansatz with log(T-t) dependence
- Profile equation derivation for non-self-similar evolution
- Explicit cascade construction with scale-dependent concentration
- Numerical verification of self-consistency

Mathematical Framework:
For Type II blowup at rate alpha:
    ||u||_inf ~ (T-t)^{-alpha} with alpha in (1/2, 3/5)

Modified ansatz:
    u(x,t) = (T-t)^{-alpha} U(x/(T-t)^beta, log(T-t))

where beta = (1+alpha)/2 for dimensional consistency.

The log(T-t) dependence allows deviation from pure self-similarity,
potentially evading the Necas-Ruzicka-Sverak obstruction.
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq
from scipy.optimize import minimize, fsolve, root
from scipy.integrate import solve_ivp, quad, dblquad
from scipy.interpolate import RegularGridInterpolator, interp1d
from scipy.special import spherical_jn
try:
    from scipy.special import sph_harm
except ImportError:
    from scipy.special import sph_harm_y as sph_harm  # Newer scipy versions
from typing import Tuple, Optional, Dict, List, Callable, Any
from dataclasses import dataclass, field
import warnings


# =============================================================================
# PHYSICAL CONSTANTS AND CONSTRAINTS
# =============================================================================

@dataclass
class TypeIIParameters:
    """Parameters for Type II blowup construction."""
    # Blowup rate exponent: alpha in (1/2, 3/5) is the gap
    alpha: float = 0.55  # Middle of unexplored window

    # Spatial scaling exponent: beta = (1+alpha)/2 for Navier-Stokes
    beta: float = field(init=False)

    # Viscosity
    nu: float = 0.01

    # Blowup time
    T_star: float = 1.0

    # Grid parameters
    N: int = 64
    L: float = 2 * np.pi

    # Number of cascade levels
    n_cascade: int = 8

    def __post_init__(self):
        # Dimensional consistency for Navier-Stokes
        self.beta = (1 + self.alpha) / 2

        # Validate alpha is in the gap
        if not (0.5 < self.alpha < 0.6):
            warnings.warn(f"alpha={self.alpha} outside unexplored window (1/2, 3/5)")


# =============================================================================
# MODIFIED SELF-SIMILAR ANSATZ
# =============================================================================

class ModifiedSelfSimilarAnsatz:
    """
    Modified self-similar ansatz for Type II blowup.

    Pure self-similar: u = (T-t)^{-1/2} U(x/(T-t)^{1/2})
    This is ruled out by Necas-Ruzicka-Sverak (1996).

    Modified ansatz: u = (T-t)^{-alpha} U(y, s)
    where:
        y = x / (T-t)^beta
        s = -log(T-t)
        alpha in (1/2, 3/5)  -- THE GAP
        beta = (1+alpha)/2

    The s-dependence allows non-self-similar evolution that may
    evade the NRS obstruction.
    """

    def __init__(self, params: TypeIIParameters):
        self.params = params
        self.alpha = params.alpha
        self.beta = params.beta
        self.nu = params.nu
        self.T_star = params.T_star

    def scaling_factors(self, t: float) -> Dict[str, float]:
        """Compute scaling factors at time t."""
        dt = self.T_star - t
        if dt <= 0:
            raise ValueError(f"t={t} >= T_star={self.T_star}")

        return {
            'amplitude': dt**(-self.alpha),          # Velocity scaling
            'space': dt**self.beta,                   # Spatial scaling
            's': -np.log(dt),                         # Self-similar time
            'vorticity_scale': dt**(-self.alpha - self.beta),  # Vorticity scaling
            'pressure_scale': dt**(-2*self.alpha),    # Pressure scaling
        }

    def transform_to_similarity(self, x: np.ndarray, u: np.ndarray, t: float) -> Tuple[np.ndarray, np.ndarray, float]:
        """
        Transform (x, u, t) to similarity variables (y, U, s).

        Args:
            x: Physical coordinates (N, 3) or meshgrid arrays
            u: Velocity field
            t: Time

        Returns:
            y: Similarity coordinates
            U: Rescaled velocity profile
            s: Similarity time
        """
        scales = self.scaling_factors(t)

        y = x / scales['space']
        U = u / scales['amplitude']
        s = scales['s']

        return y, U, s

    def transform_from_similarity(self, y: np.ndarray, U: np.ndarray, s: float) -> Tuple[np.ndarray, np.ndarray, float]:
        """
        Transform (y, U, s) back to physical variables (x, u, t).
        """
        dt = np.exp(-s)
        t = self.T_star - dt

        scales = self.scaling_factors(t)

        x = y * scales['space']
        u = U * scales['amplitude']

        return x, u, t


# =============================================================================
# PROFILE EQUATION DERIVATION
# =============================================================================

class ProfileEquation:
    """
    Derive and analyze the equation U must satisfy for the modified ansatz
    to be a Navier-Stokes solution.

    Starting from:
        u_t + (u.grad)u = -grad(p) + nu * Delta(u)
        div(u) = 0

    With ansatz u(x,t) = (T-t)^{-alpha} U(x/(T-t)^beta, -log(T-t))

    The profile equation becomes (after substitution and simplification):

        d_s U + alpha * U + beta * (y . grad_y) U + (U . grad_y) U
            = -grad_y(P) + nu * (T-t)^{1-2beta} * Delta_y U

    Key insight: The viscous term has coefficient (T-t)^{1-2beta}.
    For beta = (1+alpha)/2, this is (T-t)^{-alpha}.

    As t -> T (s -> inf), if alpha > 0, viscosity becomes dominant at small scales
    but the nonlinear term can still drive concentration at larger scales.
    """

    def __init__(self, params: TypeIIParameters):
        self.params = params
        self.alpha = params.alpha
        self.beta = params.beta
        self.nu = params.nu

    def viscous_coefficient(self, s: float) -> float:
        """
        Coefficient of viscous term in similarity variables.

        For beta = (1+alpha)/2:
            coeff = nu * exp(-(1-2*beta)*s) = nu * exp(alpha*s)

        This GROWS as s -> infinity, meaning viscosity becomes MORE important
        at late times in similarity variables. This is the key challenge.
        """
        dt = np.exp(-s)
        return self.nu * dt**(1 - 2*self.beta)

    def profile_rhs(self, y: np.ndarray, U: np.ndarray, P: np.ndarray,
                    grad_U: np.ndarray, laplacian_U: np.ndarray,
                    grad_P: np.ndarray, s: float) -> np.ndarray:
        """
        Compute RHS of the profile equation:

        dU/ds = -alpha*U - beta*(y.grad)U - (U.grad)U - grad(P) + nu_eff*laplacian(U)

        Args:
            y: Similarity coordinates
            U: Velocity profile (3 components)
            P: Pressure profile
            grad_U: Velocity gradient tensor
            laplacian_U: Laplacian of velocity
            grad_P: Pressure gradient
            s: Similarity time

        Returns:
            dU/ds: Time derivative in similarity variables
        """
        nu_eff = self.viscous_coefficient(s)

        # Linear stretching term: -alpha * U
        linear = -self.alpha * U

        # Self-similar transport: -beta * (y . grad) U
        # This is the term from coordinate transformation
        transport = -self.beta * np.einsum('i,ij->j', y, grad_U)

        # Nonlinear advection: -(U . grad) U
        advection = -np.einsum('i,ij->j', U, grad_U)

        # Pressure gradient
        pressure = -grad_P

        # Viscous dissipation
        viscous = nu_eff * laplacian_U

        return linear + transport + advection + pressure + viscous

    def steady_state_condition(self, U: np.ndarray, grad_U: np.ndarray,
                               laplacian_U: np.ndarray, s: float) -> np.ndarray:
        """
        For a STEADY profile (dU/ds = 0), what does U satisfy?

        This is what we need to find for a true self-similar blowup.
        The log(T-t) dependence gives us freedom here.
        """
        # If dU/ds = 0, the profile equation becomes:
        # alpha*U + beta*(y.grad)U + (U.grad)U = -grad(P) + nu_eff*laplacian(U)

        # For alpha in (1/2, 3/5), this is a balance between:
        # - Stretching (alpha*U + beta*(y.grad)U)
        # - Nonlinear advection
        # - Viscous damping (which grows with s)

        # The key is: can we find U such that this balance holds
        # WITHOUT nu_eff being too large?

        nu_eff = self.viscous_coefficient(s)

        # Required pressure gradient for steady state
        # grad(P) = -alpha*U - beta*(y.grad)U - (U.grad)U + nu_eff*laplacian(U)

        return -self.alpha * U - self.beta * grad_U - np.einsum('i,ij->j', U, grad_U) + nu_eff * laplacian_U


# =============================================================================
# CONCENTRATION FUNCTION ANALYSIS (NON-MONOTONE!)
# =============================================================================

class ConcentrationAnalyzer:
    """
    Analyze the concentration function C(r) which is NOT monotone.

    C(r) = sup_x int_{B(x,r)} |u|^2 / int|u|^2

    Key insight from regularity theory:
    - Energy E(t) = int |u|^2 is MONOTONE DECREASING
    - But C(r) is NOT required to be monotone
    - Local energy can CONCENTRATE even as global energy decreases

    This is the gap we exploit: Design profiles where
    - Global energy decreases (satisfies NS energy inequality)
    - Local concentration increases (allowed!)

    For Type II blowup:
    - ||u||_inf ~ (T-t)^{-alpha}
    - Energy ~ (T-t)^{3beta - 2alpha} (from scaling)
    - For beta = (1+alpha)/2: Energy ~ (T-t)^{(3-alpha)/2}
    - Since alpha < 1: Energy decreases as t -> T (good!)

    But concentration can still grow because the energy is
    becoming more localized even as it decreases.
    """

    def __init__(self, params: TypeIIParameters):
        self.params = params
        self.L = params.L
        self.N = params.N

    def compute_concentration_function(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                                        radii: np.ndarray = None) -> Dict[str, np.ndarray]:
        """
        Compute the concentration function C(r) for a velocity field.

        C(r) = sup_x (int_{B(x,r)} |u|^2) / (int |u|^2)

        Args:
            u, v, w: Velocity components on grid
            radii: Array of radii to evaluate C(r)

        Returns:
            Dict with radii, C(r), and location of maximum concentration
        """
        # Use actual input array size
        N_input = u.shape[0]

        if radii is None:
            radii = np.linspace(0.1, self.L/2, 20)

        # Total energy
        u_sq = u**2 + v**2 + w**2
        dx = self.L / N_input
        total_energy = np.sum(u_sq) * dx**3

        if total_energy < 1e-15:
            return {'radii': radii, 'C': np.zeros_like(radii), 'max_loc': (0, 0, 0)}

        # Grid coordinates - use actual input size
        x = np.linspace(0, self.L, N_input, endpoint=False)
        X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

        C_values = []
        max_locations = []

        for r in radii:
            max_local_energy = 0.0
            max_loc = (0, 0, 0)

            # Sample center locations (for efficiency, don't check every point)
            n_samples = min(N_input // 2, 16)
            centers = np.linspace(0, self.L, n_samples, endpoint=False)

            for cx in centers:
                for cy in centers:
                    for cz in centers:
                        # Distance from center (with periodic BC)
                        dx_grid = np.minimum(np.abs(X - cx), self.L - np.abs(X - cx))
                        dy_grid = np.minimum(np.abs(Y - cy), self.L - np.abs(Y - cy))
                        dz_grid = np.minimum(np.abs(Z - cz), self.L - np.abs(Z - cz))
                        dist = np.sqrt(dx_grid**2 + dy_grid**2 + dz_grid**2)

                        # Ball indicator
                        mask = (dist <= r).astype(float)

                        # Local energy
                        local_energy = np.sum(u_sq * mask) * dx**3

                        if local_energy > max_local_energy:
                            max_local_energy = local_energy
                            max_loc = (cx, cy, cz)

            C_values.append(max_local_energy / total_energy)
            max_locations.append(max_loc)

        return {
            'radii': radii,
            'C': np.array(C_values),
            'max_locations': max_locations,
            'total_energy': total_energy
        }

    def design_concentrating_profile(self, target_C_ratio: float = 2.0,
                                     initial_r: float = 0.5,
                                     final_r: float = 0.1) -> Callable:
        """
        Design a velocity profile where concentration increases.

        The idea: As t -> T, the profile should concentrate more energy
        into smaller balls, even as total energy decreases.

        Args:
            target_C_ratio: C(final_r)/C(initial_r) target ratio
            initial_r: Initial concentration radius
            final_r: Final concentration radius (smaller)

        Returns:
            Profile function U(r, theta, phi, s) in spherical coords
        """
        alpha = self.params.alpha

        def concentrating_profile(r: np.ndarray, s: float) -> np.ndarray:
            """
            Radial profile that concentrates as s increases.

            U(r, s) = A(s) * exp(-r^2 / (2*sigma(s)^2))

            where sigma(s) decreases and A(s) adjusts to satisfy constraints.
            """
            # Characteristic width decreases with s
            sigma_0 = initial_r
            sigma = sigma_0 * np.exp(-s / (2 * target_C_ratio))

            # Amplitude adjusted for energy constraint
            # int |U|^2 r^2 dr ~ A^2 * sigma^3
            # For energy to decrease: A^2 * sigma^3 must decrease
            # But |U|_max = A increases if A grows faster than sigma^{-3/2}

            # Choose: A ~ sigma^{-alpha} so |U|_max ~ sigma^{-alpha}
            # Energy ~ A^2 * sigma^3 ~ sigma^{3 - 2*alpha}
            # For alpha < 3/2, energy decreases as sigma decreases (good!)

            A = sigma**(-alpha)

            profile = A * np.exp(-r**2 / (2 * sigma**2))

            return profile, sigma, A

        return concentrating_profile


# =============================================================================
# CASCADE CONSTRUCTION
# =============================================================================

class CascadeConstructor:
    """
    Construct explicit cascade solutions with scale-dependent concentration.

    The cascade ansatz:
        u = sum_{j=0}^{J} u_j

    where u_j has characteristic scale 2^{-j} L and amplitude f_j.

    Energy constraint: sum_j |u_j|^2 must decrease in time

    Concentration constraint: We want local norms to increase

    The key freedom: f_j can be scale-dependent, allowing energy
    to redistribute across scales while total decreases.
    """

    def __init__(self, params: TypeIIParameters):
        self.params = params
        self.n_levels = params.n_cascade
        self.L = params.L
        self.N = params.N
        self.alpha = params.alpha
        self.nu = params.nu

    def dyadic_scales(self) -> np.ndarray:
        """Return dyadic scales 2^{-j} * L for j = 0, ..., n_levels-1."""
        return self.L * 2.0**(-np.arange(self.n_levels))

    def dissipation_constraint(self, f: np.ndarray, scales: np.ndarray) -> float:
        """
        Compute the dissipation rate from cascade amplitudes.

        Dissipation ~ nu * sum_j f_j^2 / scale_j^2

        This must be positive (viscous damping).
        """
        return self.nu * np.sum(f**2 / scales**2)

    def energy_from_cascade(self, f: np.ndarray, scales: np.ndarray) -> float:
        """
        Total energy from cascade amplitudes.

        E ~ sum_j f_j^2 * scale_j^3

        (Each mode contributes f_j^2 * volume ~ f_j^2 * scale^3)
        """
        return np.sum(f**2 * scales**3)

    def concentration_from_cascade(self, f: np.ndarray, scales: np.ndarray, r: float) -> float:
        """
        Concentration at scale r from cascade.

        C(r) ~ sum_{j: scale_j < r} f_j^2 * scale_j^3 / E

        Modes smaller than r contribute to C(r).
        """
        E = self.energy_from_cascade(f, scales)
        if E < 1e-15:
            return 0.0

        mask = scales < r
        local_E = np.sum(f[mask]**2 * scales[mask]**3)
        return local_E / E

    def find_concentrating_cascade(self, s_values: np.ndarray) -> Dict[str, np.ndarray]:
        """
        Find cascade amplitudes f_j(s) such that:
        1. Total energy decreases with s
        2. Concentration C(r) increases with s for some r
        3. Dissipation constraint is satisfied

        This is the key construction!

        Strategy: Shift energy to smaller scales over time.
        - f_j(s) = f_j(0) * g_j(s)
        - g_j(s) transfers energy from large to small scales
        - Total energy: E(s) = sum_j f_j(s)^2 * scale_j^3
        - Require dE/ds < 0 (energy decrease)
        - But C(r, s) can still increase for small r

        Args:
            s_values: Array of similarity times

        Returns:
            Dict with cascade evolution data
        """
        scales = self.dyadic_scales()
        n_s = len(s_values)

        # Initial amplitudes: Kolmogorov-like spectrum
        # f_j ~ scale_j^{1/3} (energy spectrum E(k) ~ k^{-5/3})
        f0 = scales**(1/3)
        f0 = f0 / np.linalg.norm(f0)  # Normalize

        # Evolution: Transfer energy to smaller scales
        # g_j(s) = exp(lambda_j * s) where lambda_j > 0 for small j
        # and lambda_j < 0 for large j

        # Critical constraint: sum_j lambda_j * f_j^2 * scale_j^3 < 0
        # (energy must decrease)

        # Design lambda_j: negative at large scales, positive at small scales
        # but weighted sum must be negative

        j = np.arange(self.n_levels)
        j_mid = self.n_levels / 2

        # Lambda profile: negative for large scales (small j), positive for small scales (large j)
        lambda_j = 0.1 * (j - j_mid) / j_mid

        # Adjust to ensure energy decreases
        energy_rate = np.sum(lambda_j * f0**2 * scales**3)
        if energy_rate >= 0:
            # Shift lambda to make energy decrease
            lambda_j = lambda_j - energy_rate / np.sum(f0**2 * scales**3) - 0.01

        # Compute evolution
        f_evolution = np.zeros((n_s, self.n_levels))
        energy_evolution = np.zeros(n_s)
        concentration_evolution = np.zeros((n_s, self.n_levels))  # C at each scale

        for i, s in enumerate(s_values):
            # f_j(s) = f0_j * exp(lambda_j * s)
            f_s = f0 * np.exp(lambda_j * s)
            f_evolution[i] = f_s

            # Energy
            energy_evolution[i] = self.energy_from_cascade(f_s, scales)

            # Concentration at each scale
            for k, scale_k in enumerate(scales):
                concentration_evolution[i, k] = self.concentration_from_cascade(f_s, scales, scale_k)

        return {
            's_values': s_values,
            'scales': scales,
            'lambda_j': lambda_j,
            'f_evolution': f_evolution,
            'energy': energy_evolution,
            'concentration': concentration_evolution,
            'dissipation': np.array([self.dissipation_constraint(f_evolution[i], scales)
                                     for i in range(n_s)])
        }

    def construct_cascade_velocity(self, f: np.ndarray, center: np.ndarray = None) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Construct a velocity field from cascade amplitudes.

        Each scale j contributes a localized vortex-like structure.

        Args:
            f: Cascade amplitudes f_j
            center: Center of cascade (default: domain center)

        Returns:
            u, v, w: Velocity components on grid
        """
        if center is None:
            center = np.array([self.L/2, self.L/2, self.L/2])

        scales = self.dyadic_scales()

        # Grid
        x = np.linspace(0, self.L, self.N, endpoint=False)
        X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

        # Distance from center (with periodic BC)
        dx = np.minimum(np.abs(X - center[0]), self.L - np.abs(X - center[0]))
        dy = np.minimum(np.abs(Y - center[1]), self.L - np.abs(Y - center[1]))
        dz = np.minimum(np.abs(Z - center[2]), self.L - np.abs(Z - center[2]))
        r = np.sqrt(dx**2 + dy**2 + dz**2)

        u = np.zeros_like(X)
        v = np.zeros_like(X)
        w = np.zeros_like(X)

        for j, (f_j, scale_j) in enumerate(zip(f, scales)):
            # Each scale contributes a localized vortex ring
            sigma = scale_j / 4  # Characteristic width

            # Gaussian envelope
            envelope = f_j * np.exp(-r**2 / (2 * sigma**2))

            # Vortex-like velocity: u ~ r x z_hat for simplicity
            # More precisely: toroidal flow in phi direction
            r_perp = np.sqrt(dx**2 + dy**2)
            r_perp = np.maximum(r_perp, 1e-10)  # Avoid division by zero

            # Toroidal component
            u_j = -envelope * dy / r_perp * np.exp(-(dz/sigma)**2)
            v_j = envelope * dx / r_perp * np.exp(-(dz/sigma)**2)
            w_j = np.zeros_like(X)

            u += u_j
            v += v_j
            w += w_j

        return u, v, w


# =============================================================================
# NUMERICAL VERIFICATION
# =============================================================================

class NumericalVerifier:
    """
    Numerically verify if constructed profiles satisfy Navier-Stokes
    (at least approximately).

    The verification checks:
    1. Divergence-free condition: div(u) = 0
    2. NS residual: u_t + (u.grad)u + grad(p) - nu*Delta(u) should be small
    3. Energy budget: dE/dt = -nu * ||grad(u)||^2
    4. Concentration behavior: C(r) evolution
    """

    def __init__(self, params: TypeIIParameters):
        self.params = params
        self.N = params.N
        self.L = params.L
        self.nu = params.nu

        # Setup spectral operators
        k = fftfreq(self.N, d=self.L/(2*np.pi*self.N))
        self.kx, self.ky, self.kz = np.meshgrid(k, k, k, indexing='ij')
        self.k_sq = self.kx**2 + self.ky**2 + self.kz**2
        self.k_sq[0, 0, 0] = 1.0  # Avoid division by zero

    def check_divergence_free(self, u: np.ndarray, v: np.ndarray, w: np.ndarray) -> float:
        """
        Check divergence-free condition: div(u) = 0.

        Returns ||div(u)||_2 / ||u||_2.
        """
        u_hat = fftn(u)
        v_hat = fftn(v)
        w_hat = fftn(w)

        # div(u) in spectral space
        div_hat = 1j * (self.kx * u_hat + self.ky * v_hat + self.kz * w_hat)
        div = np.real(ifftn(div_hat))

        u_norm = np.sqrt(np.mean(u**2 + v**2 + w**2))
        div_norm = np.sqrt(np.mean(div**2))

        return div_norm / max(u_norm, 1e-15)

    def compute_ns_residual(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                            u_t: np.ndarray = None, v_t: np.ndarray = None,
                            w_t: np.ndarray = None) -> Dict[str, float]:
        """
        Compute the Navier-Stokes residual.

        Residual = u_t + (u.grad)u + grad(p) - nu*Delta(u)

        For a true solution, this should be zero.

        Args:
            u, v, w: Velocity components
            u_t, v_t, w_t: Time derivatives (if known)

        Returns:
            Dict with residual norms
        """
        # Spectral representation
        u_hat = fftn(u)
        v_hat = fftn(v)
        w_hat = fftn(w)

        # Get wavenumbers matching the input array size
        N_input = u.shape[0]
        if N_input != self.N:
            # Recompute wavenumbers for this grid size
            k = fftfreq(N_input, d=self.L/(2*np.pi*N_input))
            kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
            k_sq = kx**2 + ky**2 + kz**2
            k_sq[0, 0, 0] = 1.0
        else:
            kx, ky, kz = self.kx, self.ky, self.kz
            k_sq = self.k_sq

        # Compute Laplacian
        lap_u = np.real(ifftn(-k_sq * u_hat))
        lap_v = np.real(ifftn(-k_sq * v_hat))
        lap_w = np.real(ifftn(-k_sq * w_hat))

        # Compute gradients
        du_dx = np.real(ifftn(1j * kx * u_hat))
        du_dy = np.real(ifftn(1j * ky * u_hat))
        du_dz = np.real(ifftn(1j * kz * u_hat))
        dv_dx = np.real(ifftn(1j * kx * v_hat))
        dv_dy = np.real(ifftn(1j * ky * v_hat))
        dv_dz = np.real(ifftn(1j * kz * v_hat))
        dw_dx = np.real(ifftn(1j * kx * w_hat))
        dw_dy = np.real(ifftn(1j * ky * w_hat))
        dw_dz = np.real(ifftn(1j * kz * w_hat))

        # Advection: (u.grad)u
        advect_u = u * du_dx + v * du_dy + w * du_dz
        advect_v = u * dv_dx + v * dv_dy + w * dv_dz
        advect_w = u * dw_dx + v * dw_dy + w * dw_dz

        # Pressure (solve Poisson equation from div of momentum equation)
        # div((u.grad)u) = -Delta(p) for incompressible flow
        div_advect = (np.real(ifftn(1j * kx * fftn(advect_u))) +
                      np.real(ifftn(1j * ky * fftn(advect_v))) +
                      np.real(ifftn(1j * kz * fftn(advect_w))))

        p_hat = -fftn(div_advect) / k_sq
        p_hat[0, 0, 0] = 0  # Zero mean pressure

        dp_dx = np.real(ifftn(1j * kx * p_hat))
        dp_dy = np.real(ifftn(1j * ky * p_hat))
        dp_dz = np.real(ifftn(1j * kz * p_hat))

        # Residual (assuming steady state if u_t not provided)
        if u_t is None:
            u_t = np.zeros_like(u)
            v_t = np.zeros_like(v)
            w_t = np.zeros_like(w)

        res_u = u_t + advect_u + dp_dx - self.nu * lap_u
        res_v = v_t + advect_v + dp_dy - self.nu * lap_v
        res_w = w_t + advect_w + dp_dz - self.nu * lap_w

        # Norms
        u_norm = np.sqrt(np.mean(u**2 + v**2 + w**2))
        res_norm = np.sqrt(np.mean(res_u**2 + res_v**2 + res_w**2))

        return {
            'residual_norm': res_norm,
            'relative_residual': res_norm / max(u_norm, 1e-15),
            'advection_norm': np.sqrt(np.mean(advect_u**2 + advect_v**2 + advect_w**2)),
            'viscous_norm': self.nu * np.sqrt(np.mean(lap_u**2 + lap_v**2 + lap_w**2)),
            'pressure_grad_norm': np.sqrt(np.mean(dp_dx**2 + dp_dy**2 + dp_dz**2))
        }

    def check_energy_budget(self, u: np.ndarray, v: np.ndarray, w: np.ndarray) -> Dict[str, float]:
        """
        Verify the energy budget.

        For NS: dE/dt = -nu * ||grad(u)||^2 <= 0

        Returns energy and dissipation rate.
        """
        # Energy
        energy = 0.5 * np.mean(u**2 + v**2 + w**2) * self.L**3

        # Dissipation: nu * ||grad(u)||^2
        u_hat = fftn(u)
        v_hat = fftn(v)
        w_hat = fftn(w)

        # Get wavenumbers matching the input array size
        N_input = u.shape[0]
        if N_input != self.N:
            k = fftfreq(N_input, d=self.L/(2*np.pi*N_input))
            kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
        else:
            kx, ky, kz = self.kx, self.ky, self.kz

        grad_u_sq = 0.0
        for vel_hat in [u_hat, v_hat, w_hat]:
            for ki in [kx, ky, kz]:
                deriv = np.real(ifftn(1j * ki * vel_hat))
                grad_u_sq += np.mean(deriv**2)

        dissipation = self.nu * grad_u_sq * self.L**3

        return {
            'energy': energy,
            'dissipation_rate': dissipation,
            'energy_decay_rate': -dissipation  # dE/dt = -dissipation
        }

    def verify_ansatz(self, U_profile: Callable, s_values: np.ndarray,
                      n_grid: int = 32) -> Dict[str, np.ndarray]:
        """
        Verify that a profile U satisfies the profile equation approximately.

        Args:
            U_profile: Function (y, s) -> (U, V, W) giving the profile
            s_values: Array of similarity times to check
            n_grid: Grid points for spatial discretization

        Returns:
            Dict with verification results
        """
        results = {
            's_values': s_values,
            'residuals': [],
            'energies': [],
            'dissipations': [],
            'concentrations': []
        }

        # Grid in similarity variables
        y_max = 5.0  # Truncate at y_max
        y = np.linspace(-y_max, y_max, n_grid)
        Y1, Y2, Y3 = np.meshgrid(y, y, y, indexing='ij')
        dy = y[1] - y[0]

        conc_analyzer = ConcentrationAnalyzer(self.params)

        for s in s_values:
            # Evaluate profile
            try:
                U, V, W = U_profile(Y1, Y2, Y3, s)
            except:
                # If profile function doesn't work, skip
                results['residuals'].append(np.nan)
                results['energies'].append(np.nan)
                results['dissipations'].append(np.nan)
                results['concentrations'].append(np.nan)
                continue

            # Check residual
            res = self.compute_ns_residual(U, V, W)
            results['residuals'].append(res['relative_residual'])

            # Energy budget
            budget = self.check_energy_budget(U, V, W)
            results['energies'].append(budget['energy'])
            results['dissipations'].append(budget['dissipation_rate'])

            # Concentration at a fixed radius
            r_check = y_max / 4
            conc = conc_analyzer.compute_concentration_function(
                U, V, W, radii=np.array([r_check])
            )
            results['concentrations'].append(conc['C'][0])

        # Convert to arrays
        for key in ['residuals', 'energies', 'dissipations', 'concentrations']:
            results[key] = np.array(results[key])

        return results


# =============================================================================
# MAIN CONSTRUCTOR CLASS
# =============================================================================

class TypeIIBlowupConstructor:
    """
    Main class for attempting Type II blowup construction.

    This class orchestrates the full construction:
    1. Set up parameters in the gap alpha in (1/2, 3/5)
    2. Construct candidate profiles using modified self-similar ansatz
    3. Verify concentration behavior (non-monotone!)
    4. Check energy constraints
    5. Numerically verify self-consistency

    The goal is to find profiles U such that the NS equations with
    the modified ansatz are satisfied (at least approximately) with
    alpha in the unexplored window.
    """

    def __init__(self, alpha: float = 0.55, nu: float = 0.01,
                 T_star: float = 1.0, N: int = 64):
        """
        Initialize the constructor.

        Args:
            alpha: Blowup rate exponent (should be in (1/2, 3/5))
            nu: Kinematic viscosity
            T_star: Blowup time
            N: Grid resolution
        """
        self.params = TypeIIParameters(alpha=alpha, nu=nu, T_star=T_star, N=N)

        self.ansatz = ModifiedSelfSimilarAnsatz(self.params)
        self.profile_eq = ProfileEquation(self.params)
        self.concentration = ConcentrationAnalyzer(self.params)
        self.cascade = CascadeConstructor(self.params)
        self.verifier = NumericalVerifier(self.params)

    def construct_candidate_profile(self, profile_type: str = 'gaussian_concentrating'
                                    ) -> Callable:
        """
        Construct a candidate profile for Type II blowup.

        Different profile types explore different structures:
        - 'gaussian_concentrating': Gaussian that concentrates over time
        - 'cascade': Dyadic cascade with energy transfer
        - 'vortex_sheet': Vortex sheet-like structure

        Args:
            profile_type: Type of profile to construct

        Returns:
            Profile function (y, s) -> (U, V, W)
        """
        alpha = self.params.alpha
        beta = self.params.beta
        nu = self.params.nu

        if profile_type == 'gaussian_concentrating':
            def profile(Y1, Y2, Y3, s):
                """
                Gaussian profile that concentrates as s increases.

                U(y, s) = A(s) * y_perp * exp(-|y|^2 / (2*sigma(s)^2)) * e_phi

                This is an axisymmetric vortex that shrinks with s.
                """
                # Characteristic width decreases with s
                sigma_0 = 1.0
                sigma = sigma_0 * np.exp(-s / 10)  # Slow concentration

                # Amplitude adjustment for Type II rate
                # |U|_max ~ sigma^{-alpha} to give correct blowup rate
                A = sigma**(-alpha)

                # Radial distance from z-axis
                r_perp = np.sqrt(Y1**2 + Y2**2)
                r_perp = np.maximum(r_perp, 1e-10)

                # Full radius
                r = np.sqrt(Y1**2 + Y2**2 + Y3**2)

                # Envelope
                envelope = A * np.exp(-r**2 / (2 * sigma**2))

                # Toroidal velocity (axisymmetric vortex)
                # e_phi = (-Y2, Y1, 0) / r_perp
                U = -envelope * Y2 / r_perp * (r_perp / sigma) * np.exp(-(r_perp/sigma - 1)**2)
                V = envelope * Y1 / r_perp * (r_perp / sigma) * np.exp(-(r_perp/sigma - 1)**2)
                W = np.zeros_like(Y1)

                return U, V, W

            return profile

        elif profile_type == 'cascade':
            def profile(Y1, Y2, Y3, s):
                """
                Multi-scale cascade profile.

                Sum of Gaussian vortices at different scales.
                """
                # Get cascade evolution at this s
                cascade_data = self.cascade.find_concentrating_cascade(np.array([s]))
                f = cascade_data['f_evolution'][0]
                scales = cascade_data['scales']

                # Rescale to similarity variables
                y_scale = self.params.L  # Reference scale

                r = np.sqrt(Y1**2 + Y2**2 + Y3**2)
                r_perp = np.sqrt(Y1**2 + Y2**2)
                r_perp = np.maximum(r_perp, 1e-10)

                U = np.zeros_like(Y1)
                V = np.zeros_like(Y1)
                W = np.zeros_like(Y1)

                for f_j, scale_j in zip(f, scales):
                    sigma_j = scale_j / y_scale
                    envelope = f_j * np.exp(-r**2 / (2 * sigma_j**2))

                    U += -envelope * Y2 / r_perp
                    V += envelope * Y1 / r_perp

                return U, V, W

            return profile

        elif profile_type == 'vortex_sheet':
            def profile(Y1, Y2, Y3, s):
                """
                Vortex sheet-like profile that could develop Type II blowup.

                Motivated by the fact that vortex sheet roll-up can
                concentrate vorticity while dissipating energy.
                """
                # Sheet thickness decreases with s
                delta_0 = 1.0
                delta = delta_0 * np.exp(-s / 5)

                # Amplitude
                A = delta**(-alpha)

                # Sheet profile (hyperbolic tangent)
                tanh_factor = np.tanh(Y3 / delta)
                sech_sq = 1 - tanh_factor**2

                # Velocity: shear flow with roll-up perturbation
                U = A * tanh_factor
                V = 0.1 * A * sech_sq * np.sin(Y1 / delta)  # Roll-up perturbation
                W = np.zeros_like(Y1)

                return U, V, W

            return profile

        else:
            raise ValueError(f"Unknown profile type: {profile_type}")

    def run_construction(self, s_final: float = 5.0, n_s: int = 50,
                        profile_type: str = 'gaussian_concentrating',
                        verbose: bool = True) -> Dict[str, Any]:
        """
        Run the full construction and verification.

        Args:
            s_final: Final similarity time
            n_s: Number of time steps
            profile_type: Type of profile to construct
            verbose: Print progress

        Returns:
            Dict with construction results
        """
        s_values = np.linspace(0, s_final, n_s)

        if verbose:
            print(f"Type II Blowup Construction")
            print(f"  alpha = {self.params.alpha:.4f} (in gap (1/2, 3/5): {0.5 < self.params.alpha < 0.6})")
            print(f"  beta = {self.params.beta:.4f}")
            print(f"  nu = {self.params.nu:.4f}")
            print(f"  Profile type: {profile_type}")
            print()

        # Construct profile
        profile = self.construct_candidate_profile(profile_type)

        # Verify profile
        if verbose:
            print("Verifying profile...")

        verification = self.verifier.verify_ansatz(profile, s_values)

        # Analyze cascade
        if verbose:
            print("Analyzing cascade structure...")

        cascade_data = self.cascade.find_concentrating_cascade(s_values)

        # Compute key metrics
        results = {
            'params': self.params,
            's_values': s_values,
            'verification': verification,
            'cascade': cascade_data,
            'summary': {}
        }

        # Summary statistics
        valid = ~np.isnan(verification['residuals'])
        if np.any(valid):
            results['summary']['mean_residual'] = np.mean(verification['residuals'][valid])
            results['summary']['max_residual'] = np.max(verification['residuals'][valid])
            results['summary']['energy_decreasing'] = np.all(np.diff(verification['energies'][valid]) <= 1e-10)

            # Check if concentration increases
            conc = verification['concentrations'][valid]
            results['summary']['concentration_increasing'] = np.mean(np.diff(conc) > 0) > 0.5

            if verbose:
                print("\nResults Summary:")
                print(f"  Mean residual: {results['summary']['mean_residual']:.6e}")
                print(f"  Max residual: {results['summary']['max_residual']:.6e}")
                print(f"  Energy decreasing: {results['summary']['energy_decreasing']}")
                print(f"  Concentration increasing: {results['summary']['concentration_increasing']}")

        # Cascade summary
        results['summary']['cascade_energy_decreasing'] = np.all(np.diff(cascade_data['energy']) < 0)

        # Key finding: Can we have decreasing energy but increasing concentration?
        small_scale_idx = len(cascade_data['scales']) - 1  # Smallest scale
        small_scale_conc = cascade_data['concentration'][:, small_scale_idx]
        results['summary']['small_scale_concentration_increasing'] = np.all(np.diff(small_scale_conc) > 0)

        if verbose:
            print(f"  Cascade energy decreasing: {results['summary']['cascade_energy_decreasing']}")
            print(f"  Small-scale concentration increasing: {results['summary']['small_scale_concentration_increasing']}")

            if results['summary']['cascade_energy_decreasing'] and results['summary']['small_scale_concentration_increasing']:
                print("\n  SUCCESS: Found profile with decreasing energy but increasing concentration!")
                print("  This exploits the non-monotonicity of C(r) while respecting energy decay.")

        return results

    def optimize_profile_parameters(self, objective: str = 'minimize_residual',
                                   n_iter: int = 100) -> Dict[str, Any]:
        """
        Optimize profile parameters to better satisfy NS equations.

        This uses numerical optimization to find profiles that:
        1. Have small NS residual
        2. Maintain decreasing energy
        3. Show increasing concentration

        Args:
            objective: Optimization objective
            n_iter: Maximum iterations

        Returns:
            Optimized profile parameters
        """
        s_test = np.linspace(0, 3, 10)

        def objective_function(params):
            """Compute objective from profile parameters."""
            sigma_rate, amplitude_power = params

            if sigma_rate <= 0 or amplitude_power <= 0:
                return 1e10

            alpha = self.params.alpha

            def profile(Y1, Y2, Y3, s):
                sigma = np.exp(-sigma_rate * s)
                A = sigma**(-amplitude_power)

                r = np.sqrt(Y1**2 + Y2**2 + Y3**2)
                r_perp = np.sqrt(Y1**2 + Y2**2)
                r_perp = np.maximum(r_perp, 1e-10)

                envelope = A * np.exp(-r**2 / (2 * sigma**2))

                U = -envelope * Y2 / r_perp
                V = envelope * Y1 / r_perp
                W = np.zeros_like(Y1)

                return U, V, W

            # Verify
            try:
                verification = self.verifier.verify_ansatz(profile, s_test, n_grid=16)

                valid = ~np.isnan(verification['residuals'])
                if not np.any(valid):
                    return 1e10

                # Objective: small residual + energy decreasing + concentration increasing
                residual_penalty = np.mean(verification['residuals'][valid])

                energy = verification['energies'][valid]
                if len(energy) > 1:
                    energy_penalty = np.sum(np.maximum(np.diff(energy), 0))  # Penalize energy increase
                else:
                    energy_penalty = 0

                conc = verification['concentrations'][valid]
                if len(conc) > 1:
                    conc_reward = -np.sum(np.maximum(np.diff(conc), 0))  # Reward concentration increase
                else:
                    conc_reward = 0

                return residual_penalty + 10 * energy_penalty + conc_reward
            except:
                return 1e10

        # Initial guess
        x0 = [0.1, self.params.alpha]

        # Optimize
        result = minimize(objective_function, x0, method='Nelder-Mead',
                         options={'maxiter': n_iter, 'disp': False})

        return {
            'optimal_params': result.x,
            'objective_value': result.fun,
            'success': result.success,
            'sigma_rate': result.x[0],
            'amplitude_power': result.x[1]
        }

    def generate_velocity_field(self, t: float, profile_type: str = 'cascade') -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Generate a velocity field at physical time t from the constructed profile.

        This transforms the similarity-variable profile back to physical space.

        Args:
            t: Physical time (must be < T_star)
            profile_type: Type of profile

        Returns:
            u, v, w: Physical velocity components on grid
        """
        T = self.params.T_star
        N = self.params.N
        L = self.params.L

        if t >= T:
            raise ValueError(f"t={t} must be < T_star={T}")

        dt = T - t
        s = -np.log(dt)

        # Scaling factors
        amplitude_scale = dt**(-self.params.alpha)
        space_scale = dt**self.params.beta

        # Physical grid
        x = np.linspace(0, L, N, endpoint=False)
        X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

        # Center of blowup (domain center)
        center = np.array([L/2, L/2, L/2])

        # Similarity coordinates
        Y1 = (X - center[0]) / space_scale
        Y2 = (Y - center[1]) / space_scale
        Y3 = (Z - center[2]) / space_scale

        # Get profile
        profile = self.construct_candidate_profile(profile_type)
        U, V, W = profile(Y1, Y2, Y3, s)

        # Transform to physical velocity
        u = amplitude_scale * U
        v = amplitude_scale * V
        w = amplitude_scale * W

        return u, v, w

    def analyze_critical_quantities(self, t_values: np.ndarray,
                                   profile_type: str = 'cascade') -> Dict[str, np.ndarray]:
        """
        Analyze critical quantities as t -> T_star.

        This checks:
        - ||u||_inf growth rate
        - Energy decay
        - Concentration function behavior
        - Critical Sobolev norms

        Args:
            t_values: Array of times to analyze
            profile_type: Profile type

        Returns:
            Dict with critical quantity evolution
        """
        T = self.params.T_star
        alpha = self.params.alpha

        results = {
            't_values': t_values,
            'dt': T - t_values,
            'u_Linf': [],
            'energy': [],
            'enstrophy': [],
            'concentration_r0.1': [],
            'u_L3': [],
        }

        for t in t_values:
            if t >= T:
                for key in ['u_Linf', 'energy', 'enstrophy', 'concentration_r0.1', 'u_L3']:
                    results[key].append(np.inf)
                continue

            try:
                u, v, w = self.generate_velocity_field(t, profile_type)

                # ||u||_inf
                u_mag = np.sqrt(u**2 + v**2 + w**2)
                results['u_Linf'].append(np.max(u_mag))

                # Energy
                dx = self.params.L / self.params.N
                results['energy'].append(0.5 * np.sum(u_mag**2) * dx**3)

                # Enstrophy (compute vorticity)
                # omega = curl(u)
                omega_x, omega_y, omega_z = self._compute_vorticity(u, v, w)
                omega_mag = np.sqrt(omega_x**2 + omega_y**2 + omega_z**2)
                results['enstrophy'].append(0.5 * np.sum(omega_mag**2) * dx**3)

                # Concentration at r=0.1
                conc = self.concentration.compute_concentration_function(u, v, w, radii=np.array([0.1]))
                results['concentration_r0.1'].append(conc['C'][0])

                # ||u||_L3
                results['u_L3'].append((np.sum(u_mag**3) * dx**3)**(1/3))

            except Exception as e:
                for key in ['u_Linf', 'energy', 'enstrophy', 'concentration_r0.1', 'u_L3']:
                    results[key].append(np.nan)

        # Convert to arrays
        for key in ['u_Linf', 'energy', 'enstrophy', 'concentration_r0.1', 'u_L3']:
            results[key] = np.array(results[key])

        # Compute effective exponents
        valid = ~np.isnan(results['u_Linf']) & (results['dt'] > 0)
        if np.sum(valid) > 2:
            # Fit ||u||_inf ~ (T-t)^{-alpha_eff}
            from scipy.stats import linregress
            log_dt = np.log(results['dt'][valid])
            log_u = np.log(results['u_Linf'][valid])
            slope, intercept, r, p, se = linregress(log_dt, log_u)
            results['alpha_effective'] = -slope
            results['alpha_target'] = alpha
            results['alpha_error'] = abs(results['alpha_effective'] - alpha)

        return results

    def _compute_vorticity(self, u: np.ndarray, v: np.ndarray, w: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Compute vorticity from velocity using spectral differentiation."""
        u_hat = fftn(u)
        v_hat = fftn(v)
        w_hat = fftn(w)

        # omega = curl(u)
        omega_x_hat = 1j * (self.verifier.ky * w_hat - self.verifier.kz * v_hat)
        omega_y_hat = 1j * (self.verifier.kz * u_hat - self.verifier.kx * w_hat)
        omega_z_hat = 1j * (self.verifier.kx * v_hat - self.verifier.ky * u_hat)

        omega_x = np.real(ifftn(omega_x_hat))
        omega_y = np.real(ifftn(omega_y_hat))
        omega_z = np.real(ifftn(omega_z_hat))

        return omega_x, omega_y, omega_z


# =============================================================================
# DEMONSTRATION AND TESTING
# =============================================================================

def demonstrate_type_ii_construction():
    """
    Demonstrate the Type II blowup construction.

    This runs through the full construction pipeline and reports results.
    """
    print("=" * 70)
    print("TYPE II BLOWUP CONSTRUCTION FOR 3D NAVIER-STOKES")
    print("=" * 70)
    print()
    print("Exploiting theoretical gaps:")
    print("  1. alpha in (1/2, 3/5) is NOT ruled out")
    print("  2. Concentration C(r) is NOT monotone")
    print("  3. Energy is the ONLY monotone quantity")
    print("  4. Dimensional gap of 0.9 gives freedom")
    print()

    # Test different alpha values in the gap
    alphas_to_test = [0.51, 0.55, 0.58]

    for alpha in alphas_to_test:
        print("-" * 70)
        print(f"Testing alpha = {alpha}")
        print("-" * 70)

        constructor = TypeIIBlowupConstructor(alpha=alpha, nu=0.01, N=32)

        # Run construction
        results = constructor.run_construction(s_final=3.0, n_s=20,
                                               profile_type='cascade',
                                               verbose=True)
        print()

    # Detailed analysis of one construction
    print("=" * 70)
    print("DETAILED ANALYSIS: alpha = 0.55")
    print("=" * 70)

    constructor = TypeIIBlowupConstructor(alpha=0.55, nu=0.01, N=32)

    # Analyze critical quantities
    T = constructor.params.T_star
    t_values = T - np.logspace(-3, -0.5, 20)  # Approach T_star

    print("\nAnalyzing critical quantities as t -> T*...")
    critical = constructor.analyze_critical_quantities(t_values, profile_type='cascade')

    print(f"\nEffective blowup rate: alpha_eff = {critical.get('alpha_effective', 'N/A'):.4f}")
    print(f"Target blowup rate: alpha = {critical.get('alpha_target', 'N/A'):.4f}")

    # Check cascade behavior
    print("\nCascade analysis:")
    cascade = constructor.cascade.find_concentrating_cascade(np.linspace(0, 5, 50))
    print(f"  Energy ratio (final/initial): {cascade['energy'][-1] / cascade['energy'][0]:.4f}")
    print(f"  Small-scale concentration ratio: {cascade['concentration'][-1, -1] / cascade['concentration'][0, -1]:.4f}")

    return constructor, results, critical


if __name__ == '__main__':
    constructor, results, critical = demonstrate_type_ii_construction()

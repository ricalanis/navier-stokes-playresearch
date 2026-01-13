"""
Initial Condition Search for Type II Blowup.

Searches for initial conditions that might lead to sustained Type II blowup
with rate alpha in the open window (1/2, 3/5) or possibly (3/5, 3/4).

Key insight from analysis:
- Hou-Luo IC gives transient alpha in (0.6, 0.7) but regularizes
- We need IC that SUSTAINS Type II rate
- The gap (1/2, 3/5) is not ruled out mathematically

This module implements:
1. Parameterized IC families designed for blowup potential
2. Blowup indicators (concentration, stretching, effective rate)
3. Genetic algorithm search for optimal IC parameters
4. Specific blowup candidate configurations

Theory background:
- Type I blowup (self-similar, alpha = 1/2): RULED OUT
- Type II blowup alpha >= 3/4: RULED OUT (dissipation)
- Type II blowup alpha < 1/2: Not blowup (subcritical)
- Type II blowup alpha in [1/2, 3/5) or [3/5, 3/4): OPEN

For blowup IC, we want:
- High local enstrophy / global enstrophy ratio
- Vorticity alignment favorable for stretching
- Topology allowing sustained stretching without reconnection
- Energy distribution enabling efficient cascade
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq
from typing import Tuple, Optional, Dict, List, Callable
from dataclasses import dataclass, field
import json
from pathlib import Path


# ============================================================================
# Type II Window Constants
# ============================================================================

ALPHA_TYPE_I = 0.5          # Self-similar rate (ruled out)
ALPHA_LOWER = 3/5           # 0.6 - Lower bound from BKM
ALPHA_UPPER = 3/4           # 0.75 - Upper bound from dissipation
ALPHA_CRITICAL = 3/5        # The critical rate where energy is constant


# ============================================================================
# Blowup Indicators
# ============================================================================

@dataclass
class BlowupIndicators:
    """
    Indicators that predict blowup potential of initial conditions.

    These are computed from short-time evolution and signal whether
    an IC is likely to develop Type II behavior.
    """
    # I_1: Concentration indicator
    # ||omega||_{L^infty} / ||omega||_{L^2}
    # Higher values indicate more concentrated vorticity
    concentration: float

    # I_2: Stretching rate indicator
    # int omega . S omega / ||omega||^2 where S is strain tensor
    # Higher values indicate more vortex stretching
    stretching_rate: float

    # I_3: Effective blowup rate from short-time evolution
    # Fitted alpha from ||u||_infty ~ (T* - t)^{-alpha}
    alpha_effective: float

    # I_4: Enstrophy growth rate
    # d/dt ||omega||^2 / ||omega||^2
    enstrophy_growth: float

    # I_5: Local enstrophy ratio
    # max(local enstrophy) / mean(enstrophy)
    local_enstrophy_ratio: float

    # I_6: Helicity content
    # |int u . omega| / (||u|| ||omega||)
    helicity_normalized: float

    # I_7: Alignment factor
    # Average alignment between omega and strain eigenvector
    alignment_factor: float

    # Fitness score (weighted combination)
    fitness: float = 0.0

    # Time spent in Type II window
    time_in_window: float = 0.0

    # Maximum sustained alpha
    max_sustained_alpha: float = 0.0


def compute_blowup_indicators(
    omega_x: np.ndarray, omega_y: np.ndarray, omega_z: np.ndarray,
    u: np.ndarray, v: np.ndarray, w: np.ndarray,
    L: float = 2*np.pi
) -> BlowupIndicators:
    """
    Compute all blowup indicators from vorticity and velocity fields.

    Args:
        omega_x, omega_y, omega_z: Vorticity components
        u, v, w: Velocity components
        L: Domain size

    Returns:
        BlowupIndicators with all computed values
    """
    N = omega_x.shape[0]

    # Compute norms
    omega_mag = np.sqrt(omega_x**2 + omega_y**2 + omega_z**2)
    u_mag = np.sqrt(u**2 + v**2 + w**2)

    omega_Linf = np.max(omega_mag)
    omega_L2 = np.sqrt(np.mean(omega_mag**2) * L**3)

    u_Linf = np.max(u_mag)
    u_L2 = np.sqrt(np.mean(u_mag**2) * L**3)

    # I_1: Concentration
    concentration = omega_Linf / (omega_L2 + 1e-10)

    # Compute strain tensor S_ij = (du_i/dx_j + du_j/dx_i) / 2
    k = fftfreq(N, d=L/(2*np.pi*N))
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')

    u_hat = fftn(u)
    v_hat = fftn(v)
    w_hat = fftn(w)

    # Velocity gradients
    du_dx = np.real(ifftn(1j * kx * u_hat))
    du_dy = np.real(ifftn(1j * ky * u_hat))
    du_dz = np.real(ifftn(1j * kz * u_hat))
    dv_dx = np.real(ifftn(1j * kx * v_hat))
    dv_dy = np.real(ifftn(1j * ky * v_hat))
    dv_dz = np.real(ifftn(1j * kz * v_hat))
    dw_dx = np.real(ifftn(1j * kx * w_hat))
    dw_dy = np.real(ifftn(1j * ky * w_hat))
    dw_dz = np.real(ifftn(1j * kz * w_hat))

    # Strain tensor components (symmetric)
    S_xx = du_dx
    S_yy = dv_dy
    S_zz = dw_dz
    S_xy = 0.5 * (du_dy + dv_dx)
    S_xz = 0.5 * (du_dz + dw_dx)
    S_yz = 0.5 * (dv_dz + dw_dy)

    # I_2: Stretching rate = omega . S . omega / ||omega||^2
    # (S.omega)_x = S_xx*omega_x + S_xy*omega_y + S_xz*omega_z
    S_omega_x = S_xx * omega_x + S_xy * omega_y + S_xz * omega_z
    S_omega_y = S_xy * omega_x + S_yy * omega_y + S_yz * omega_z
    S_omega_z = S_xz * omega_x + S_yz * omega_y + S_zz * omega_z

    omega_S_omega = omega_x * S_omega_x + omega_y * S_omega_y + omega_z * S_omega_z
    stretching_rate = np.mean(omega_S_omega) * L**3 / (omega_L2**2 + 1e-10)

    # I_3: Alpha effective (placeholder - needs time evolution)
    alpha_effective = 0.5  # Will be updated from simulation

    # I_4: Enstrophy growth rate (instantaneous estimate)
    # d||omega||^2/dt ~ 2 * omega . S . omega (stretching contribution)
    enstrophy = 0.5 * np.mean(omega_mag**2) * L**3
    enstrophy_growth = 2 * np.mean(omega_S_omega) * L**3 / (enstrophy + 1e-10)

    # I_5: Local enstrophy ratio
    local_enstrophy = omega_mag**2
    local_enstrophy_ratio = np.max(local_enstrophy) / (np.mean(local_enstrophy) + 1e-10)

    # I_6: Helicity content
    helicity = np.mean(u * omega_x + v * omega_y + w * omega_z) * L**3
    helicity_normalized = np.abs(helicity) / (u_L2 * omega_L2 + 1e-10)

    # I_7: Alignment factor
    # Compute eigenvalues of strain at each point (expensive, use sampling)
    alignment_factor = _compute_alignment_factor(
        omega_x, omega_y, omega_z,
        S_xx, S_yy, S_zz, S_xy, S_xz, S_yz
    )

    return BlowupIndicators(
        concentration=concentration,
        stretching_rate=stretching_rate,
        alpha_effective=alpha_effective,
        enstrophy_growth=enstrophy_growth,
        local_enstrophy_ratio=local_enstrophy_ratio,
        helicity_normalized=helicity_normalized,
        alignment_factor=alignment_factor
    )


def _compute_alignment_factor(
    omega_x: np.ndarray, omega_y: np.ndarray, omega_z: np.ndarray,
    S_xx: np.ndarray, S_yy: np.ndarray, S_zz: np.ndarray,
    S_xy: np.ndarray, S_xz: np.ndarray, S_yz: np.ndarray,
    n_samples: int = 1000
) -> float:
    """
    Compute average alignment between vorticity and strain eigenvector.

    For blowup, vorticity should align with the stretching direction
    (positive eigenvalue) of the strain tensor.
    """
    N = omega_x.shape[0]

    # Sample random points
    np.random.seed(42)  # Reproducible
    idx = np.random.choice(N**3, size=min(n_samples, N**3), replace=False)

    alignments = []

    for flat_idx in idx:
        i, j, k = np.unravel_index(flat_idx, (N, N, N))

        # Local strain tensor
        S = np.array([
            [S_xx[i,j,k], S_xy[i,j,k], S_xz[i,j,k]],
            [S_xy[i,j,k], S_yy[i,j,k], S_yz[i,j,k]],
            [S_xz[i,j,k], S_yz[i,j,k], S_zz[i,j,k]]
        ])

        # Local vorticity
        omega = np.array([omega_x[i,j,k], omega_y[i,j,k], omega_z[i,j,k]])
        omega_norm = np.linalg.norm(omega)

        if omega_norm < 1e-10:
            continue

        omega_hat = omega / omega_norm

        # Eigenvalues and eigenvectors of S
        try:
            eigvals, eigvecs = np.linalg.eigh(S)
            # Most stretching direction (largest eigenvalue)
            stretch_dir = eigvecs[:, np.argmax(eigvals)]

            # Alignment = |cos(angle)|
            alignment = np.abs(np.dot(omega_hat, stretch_dir))
            alignments.append(alignment)
        except:
            continue

    if len(alignments) == 0:
        return 0.0

    return np.mean(alignments)


# ============================================================================
# Parameterized Initial Condition Families
# ============================================================================

@dataclass
class ICParameters:
    """
    Parameters defining an initial condition from our blowup-candidate family.

    The family is designed to explore configurations that might sustain
    Type II blowup behavior.
    """
    # Concentration scale (fraction of domain)
    concentration_scale: float = 0.1

    # Vorticity alignment angle (radians)
    alignment_angle: float = 0.0

    # Helicity content (can be positive, negative, or zero)
    helicity: float = 0.0

    # Symmetry type
    symmetry: str = 'axisymmetric'  # 'axisymmetric', 'helical', 'triaxial', 'none'

    # Amplitude
    amplitude: float = 1.0

    # Radial profile parameters
    radial_peak: float = 0.5  # Location of peak (fraction of domain)
    radial_width: float = 0.1  # Width of profile

    # Axial structure parameters
    axial_modes: int = 2  # Number of axial modes
    axial_phase: float = 0.0  # Phase offset

    # Anti-parallel tube parameters (if applicable)
    tube_separation: float = 0.3  # For anti-parallel tubes
    tube_radius: float = 0.1

    # Knot parameters (if applicable)
    knot_type: str = 'none'  # 'none', 'trefoil', 'torus', 'figure8'
    knot_aspect: float = 1.0

    # Random perturbation
    perturbation_amplitude: float = 0.0
    perturbation_seed: int = 42

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            'concentration_scale': self.concentration_scale,
            'alignment_angle': self.alignment_angle,
            'helicity': self.helicity,
            'symmetry': self.symmetry,
            'amplitude': self.amplitude,
            'radial_peak': self.radial_peak,
            'radial_width': self.radial_width,
            'axial_modes': self.axial_modes,
            'axial_phase': self.axial_phase,
            'tube_separation': self.tube_separation,
            'tube_radius': self.tube_radius,
            'knot_type': self.knot_type,
            'knot_aspect': self.knot_aspect,
            'perturbation_amplitude': self.perturbation_amplitude,
            'perturbation_seed': self.perturbation_seed,
        }

    @classmethod
    def from_dict(cls, d: dict) -> 'ICParameters':
        """Create from dictionary."""
        return cls(**d)


def generate_ic_from_params(
    params: ICParameters,
    N: int = 64,
    L: float = 2*np.pi
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate initial condition from parameters.

    Returns vorticity in spectral space.
    """
    if params.symmetry == 'axisymmetric':
        return _generate_axisymmetric_ic(params, N, L)
    elif params.symmetry == 'helical':
        return _generate_helical_ic(params, N, L)
    elif params.symmetry == 'triaxial':
        return _generate_triaxial_ic(params, N, L)
    elif params.knot_type != 'none':
        return _generate_knot_ic(params, N, L)
    else:
        return _generate_general_ic(params, N, L)


def _generate_axisymmetric_ic(
    params: ICParameters,
    N: int,
    L: float
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate axisymmetric initial condition (Hou-Luo style).

    Key features for blowup potential:
    - Concentrated angular vorticity near outer boundary
    - Convergent axial flow to enhance stretching
    - Specific z-structure to promote localized concentration
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    # Center coordinates
    X_c = X - L/2
    Y_c = Y - L/2
    Z_c = Z - L/2

    # Cylindrical coordinates
    r = np.sqrt(X_c**2 + Y_c**2)
    r_safe = np.maximum(r, 1e-10)
    theta = np.arctan2(Y_c, X_c)

    # Radial profile
    r_peak = params.radial_peak * L / 2
    sigma_r = params.radial_width * L / 2
    r_max = 0.95 * L / 2

    # Hou-Luo style radial profile
    f_r = (r / (r_peak + 1e-10)) * np.maximum(1 - r / r_max, 0)**2 * \
          np.exp(-((r - r_peak)**2) / (2 * sigma_r**2 + 1e-10))

    # Axial structure
    g_z = np.sin(params.axial_modes * np.pi * Z_c / L + params.axial_phase)**2
    h_z = np.sin(np.pi * Z_c / L)  # Odd component

    # Angular velocity
    u_theta = params.amplitude * f_r * g_z

    # Add helicity through z-dependent twist
    if np.abs(params.helicity) > 1e-10:
        u_theta += params.helicity * f_r * np.cos(2 * np.pi * Z / L)

    # Axial velocity for stretching
    u_z_profile = 0.2 * params.amplitude * (1 - (r / (L/2))**2)
    u_z = u_z_profile * h_z * np.exp(-r**2 / (r_peak**2 + 1e-10))

    # No radial velocity (enforced by projection)
    u_r = np.zeros_like(X)

    # Convert to Cartesian
    u = u_r * np.cos(theta) - u_theta * np.sin(theta)
    v = u_r * np.sin(theta) + u_theta * np.cos(theta)
    w = u_z

    # Add perturbation if requested
    if params.perturbation_amplitude > 0:
        u, v, w = _add_perturbation(u, v, w, params)

    return _velocity_to_vorticity_projected(u, v, w, L)


def _generate_helical_ic(
    params: ICParameters,
    N: int,
    L: float
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate helical initial condition.

    Helical flows have specific properties:
    - Velocity aligned with vorticity (Beltrami type)
    - Can have sustained stretching without reconnection
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    X_c = X - L/2
    Y_c = Y - L/2
    Z_c = Z - L/2

    r = np.sqrt(X_c**2 + Y_c**2)
    theta = np.arctan2(Y_c, X_c)

    # Helical wavenumber
    k_h = params.axial_modes * 2 * np.pi / L

    # Radial envelope
    sigma = params.concentration_scale * L / 2
    envelope = np.exp(-r**2 / (2 * sigma**2))

    # Helical structure: u parallel to omega (Beltrami)
    # ABC flow type
    phase = k_h * Z + params.helicity * theta

    u = params.amplitude * envelope * (
        np.cos(phase) * np.cos(theta) - np.sin(phase) * np.sin(theta)
    )
    v = params.amplitude * envelope * (
        np.cos(phase) * np.sin(theta) + np.sin(phase) * np.cos(theta)
    )
    w = params.amplitude * envelope * np.sin(phase)

    if params.perturbation_amplitude > 0:
        u, v, w = _add_perturbation(u, v, w, params)

    return _velocity_to_vorticity_projected(u, v, w, L)


def _generate_triaxial_ic(
    params: ICParameters,
    N: int,
    L: float
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate triaxially symmetric initial condition.

    Similar to Kida vortex - can develop strong stretching.
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    k = params.axial_modes
    A = params.amplitude

    # Kida-type velocity field
    u = A * np.sin(k * Z) + 0.5 * A * np.cos(k * Y)
    v = A * np.sin(k * X) + 0.5 * A * np.cos(k * Z)
    w = A * np.sin(k * Y) + 0.5 * A * np.cos(k * X)

    # Modulate by concentration envelope
    X_c = X - L/2
    Y_c = Y - L/2
    Z_c = Z - L/2

    sigma = params.concentration_scale * L / 2
    envelope = np.exp(-(X_c**2 + Y_c**2 + Z_c**2) / (2 * sigma**2))

    u *= envelope
    v *= envelope
    w *= envelope

    if params.perturbation_amplitude > 0:
        u, v, w = _add_perturbation(u, v, w, params)

    return _velocity_to_vorticity_projected(u, v, w, L)


def _generate_knot_ic(
    params: ICParameters,
    N: int,
    L: float
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate vortex knot initial condition.

    Knotted vortex tubes can have sustained stretching due to
    topological constraints preventing reconnection.
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    X_c = X - L/2
    Y_c = Y - L/2
    Z_c = Z - L/2

    # Knot parameters
    R_major = params.radial_peak * L / 4  # Major radius
    R_minor = params.tube_radius * L / 4  # Tube radius
    aspect = params.knot_aspect

    if params.knot_type == 'trefoil':
        # Trefoil knot: (p, q) = (2, 3)
        p, q = 2, 3
    elif params.knot_type == 'torus':
        # Torus knot with adjustable aspect
        p, q = 3, 2
    elif params.knot_type == 'figure8':
        # Figure-8 knot (simple knot)
        p, q = 2, 3
    else:
        p, q = 2, 3

    # Distance to knot centerline (approximation using parametric form)
    # For trefoil: r(t) = ((2 + cos(3t))cos(2t), (2 + cos(3t))sin(2t), sin(3t))

    # We create a vorticity distribution concentrated near the knot
    omega_x = np.zeros_like(X)
    omega_y = np.zeros_like(X)
    omega_z = np.zeros_like(X)

    # Sample points along knot
    n_points = 100
    t_vals = np.linspace(0, 2*np.pi, n_points, endpoint=False)

    for t in t_vals:
        # Knot centerline
        if params.knot_type == 'trefoil':
            x_k = R_major * (2 + np.cos(q*t)) * np.cos(p*t)
            y_k = R_major * (2 + np.cos(q*t)) * np.sin(p*t)
            z_k = R_major * aspect * np.sin(q*t)
        else:
            x_k = R_major * np.cos(p*t) * (2 + np.cos(q*t))
            y_k = R_major * np.sin(p*t) * (2 + np.cos(q*t))
            z_k = R_major * aspect * np.sin(q*t)

        # Tangent vector (unnormalized)
        dt = 0.01
        if params.knot_type == 'trefoil':
            x_k_dt = R_major * (2 + np.cos(q*(t+dt))) * np.cos(p*(t+dt))
            y_k_dt = R_major * (2 + np.cos(q*(t+dt))) * np.sin(p*(t+dt))
            z_k_dt = R_major * aspect * np.sin(q*(t+dt))
        else:
            x_k_dt = R_major * np.cos(p*(t+dt)) * (2 + np.cos(q*(t+dt)))
            y_k_dt = R_major * np.sin(p*(t+dt)) * (2 + np.cos(q*(t+dt)))
            z_k_dt = R_major * aspect * np.sin(q*(t+dt))

        tangent = np.array([x_k_dt - x_k, y_k_dt - y_k, z_k_dt - z_k])
        tangent = tangent / (np.linalg.norm(tangent) + 1e-10)

        # Distance from each grid point to knot centerline
        dist_sq = (X_c - x_k)**2 + (Y_c - y_k)**2 + (Z_c - z_k)**2

        # Gaussian tube profile
        profile = np.exp(-dist_sq / (2 * R_minor**2))

        # Add vorticity along tangent direction
        omega_x += params.amplitude * tangent[0] * profile
        omega_y += params.amplitude * tangent[1] * profile
        omega_z += params.amplitude * tangent[2] * profile

    # Normalize by number of points
    omega_x /= n_points
    omega_y /= n_points
    omega_z /= n_points

    # Convert vorticity to velocity using Biot-Savart
    omega_x_hat = fftn(omega_x)
    omega_y_hat = fftn(omega_y)
    omega_z_hat = fftn(omega_z)

    k = fftfreq(N, d=L/(2*np.pi*N))
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
    k_sq = kx**2 + ky**2 + kz**2
    k_sq[0, 0, 0] = 1.0

    # u = curl^{-1}(omega) via Biot-Savart
    # In spectral: u_hat = (ik x omega_hat) / |k|^2
    cross_x = 1j * (ky * omega_z_hat - kz * omega_y_hat)
    cross_y = 1j * (kz * omega_x_hat - kx * omega_z_hat)
    cross_z = 1j * (kx * omega_y_hat - ky * omega_x_hat)

    u_hat = cross_x / k_sq
    v_hat = cross_y / k_sq
    w_hat = cross_z / k_sq

    u_hat[0, 0, 0] = 0
    v_hat[0, 0, 0] = 0
    w_hat[0, 0, 0] = 0

    u = np.real(ifftn(u_hat))
    v = np.real(ifftn(v_hat))
    w = np.real(ifftn(w_hat))

    if params.perturbation_amplitude > 0:
        u, v, w = _add_perturbation(u, v, w, params)

    return _velocity_to_vorticity_projected(u, v, w, L)


def _generate_general_ic(
    params: ICParameters,
    N: int,
    L: float
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate general (no special symmetry) initial condition.

    Anti-parallel vortex tubes style.
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    cx, cy = L/2, L/2

    # Two vortex cores
    sep = params.tube_separation * L
    y1 = cy + sep/2
    y2 = cy - sep/2

    sigma = params.tube_radius * L

    # Distance from each core
    r1_sq = (X - cx)**2 + (Y - y1)**2
    r2_sq = (X - cx)**2 + (Y - y2)**2

    # Vorticity cores (opposite signs)
    omega_z = params.amplitude * (
        np.exp(-r1_sq / (2*sigma**2)) - np.exp(-r2_sq / (2*sigma**2))
    )

    # Add z-variation
    omega_z *= (1 + 0.3 * np.sin(params.axial_modes * 2 * np.pi * Z / L))

    # Axial vorticity for 3D structure
    omega_x = 0.1 * params.amplitude * np.sin(2 * np.pi * Z / L) * (
        np.exp(-r1_sq / (2*sigma**2)) + np.exp(-r2_sq / (2*sigma**2))
    )
    omega_y = np.zeros_like(X)

    # Convert to velocity via Biot-Savart
    omega_x_hat = fftn(omega_x)
    omega_y_hat = fftn(omega_y)
    omega_z_hat = fftn(omega_z)

    k = fftfreq(N, d=L/(2*np.pi*N))
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
    k_sq = kx**2 + ky**2 + kz**2
    k_sq[0, 0, 0] = 1.0

    cross_x = 1j * (ky * omega_z_hat - kz * omega_y_hat)
    cross_y = 1j * (kz * omega_x_hat - kx * omega_z_hat)
    cross_z = 1j * (kx * omega_y_hat - ky * omega_x_hat)

    u_hat = cross_x / k_sq
    v_hat = cross_y / k_sq
    w_hat = cross_z / k_sq

    u_hat[0, 0, 0] = 0
    v_hat[0, 0, 0] = 0
    w_hat[0, 0, 0] = 0

    u = np.real(ifftn(u_hat))
    v = np.real(ifftn(v_hat))
    w = np.real(ifftn(w_hat))

    if params.perturbation_amplitude > 0:
        u, v, w = _add_perturbation(u, v, w, params)

    return _velocity_to_vorticity_projected(u, v, w, L)


def _add_perturbation(
    u: np.ndarray, v: np.ndarray, w: np.ndarray,
    params: ICParameters
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Add random divergence-free perturbation."""
    N = u.shape[0]
    np.random.seed(params.perturbation_seed)

    perturb_u = params.perturbation_amplitude * np.random.randn(N, N, N)
    perturb_v = params.perturbation_amplitude * np.random.randn(N, N, N)
    perturb_w = params.perturbation_amplitude * np.random.randn(N, N, N)

    return u + perturb_u, v + perturb_v, w + perturb_w


def _velocity_to_vorticity_projected(
    u: np.ndarray, v: np.ndarray, w: np.ndarray,
    L: float
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Convert velocity to vorticity with Leray projection."""
    N = u.shape[0]
    k = fftfreq(N, d=L/(2*np.pi*N))
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
    k_sq = kx**2 + ky**2 + kz**2
    k_sq[0, 0, 0] = 1.0

    u_hat = fftn(u)
    v_hat = fftn(v)
    w_hat = fftn(w)

    # Leray projection
    div = (kx * u_hat + ky * v_hat + kz * w_hat) / k_sq
    u_hat -= kx * div
    v_hat -= ky * div
    w_hat -= kz * div

    u_hat[0, 0, 0] = 0
    v_hat[0, 0, 0] = 0
    w_hat[0, 0, 0] = 0

    # Vorticity
    omega_x_hat = 1j * (ky * w_hat - kz * v_hat)
    omega_y_hat = 1j * (kz * u_hat - kx * w_hat)
    omega_z_hat = 1j * (kx * v_hat - ky * u_hat)

    return omega_x_hat, omega_y_hat, omega_z_hat


# ============================================================================
# Fitness Function for Genetic Search
# ============================================================================

def compute_fitness(
    indicators: BlowupIndicators,
    weights: Optional[Dict[str, float]] = None
) -> float:
    """
    Compute fitness score from blowup indicators.

    Higher fitness indicates higher blowup potential.

    Args:
        indicators: BlowupIndicators from simulation
        weights: Optional custom weights for each indicator

    Returns:
        Fitness score (higher = more likely to blowup)
    """
    if weights is None:
        weights = {
            'concentration': 1.0,
            'stretching_rate': 2.0,
            'alpha_effective': 5.0,  # Most important
            'enstrophy_growth': 1.5,
            'local_enstrophy_ratio': 0.5,
            'alignment_factor': 1.0,
            'time_in_window': 10.0,  # Reward sustained Type II
        }

    fitness = 0.0

    # Concentration contribution (log scale)
    if indicators.concentration > 1:
        fitness += weights['concentration'] * np.log(indicators.concentration)

    # Stretching rate (positive is good for blowup)
    if indicators.stretching_rate > 0:
        fitness += weights['stretching_rate'] * indicators.stretching_rate

    # Alpha effective - reward being in Type II window
    alpha = indicators.alpha_effective
    if ALPHA_TYPE_I < alpha < ALPHA_UPPER:
        # Peak fitness at alpha ~ 0.65 (middle of window)
        distance_from_optimal = abs(alpha - 0.65)
        fitness += weights['alpha_effective'] * (0.15 - distance_from_optimal)
    elif alpha >= ALPHA_UPPER:
        # Penalize being outside window
        fitness -= weights['alpha_effective'] * (alpha - ALPHA_UPPER)

    # Enstrophy growth (positive is good)
    fitness += weights['enstrophy_growth'] * max(0, indicators.enstrophy_growth)

    # Local concentration
    if indicators.local_enstrophy_ratio > 10:
        fitness += weights['local_enstrophy_ratio'] * np.log10(indicators.local_enstrophy_ratio)

    # Alignment factor (higher = better for stretching)
    fitness += weights['alignment_factor'] * indicators.alignment_factor

    # Time in window (most important for sustained blowup)
    fitness += weights['time_in_window'] * indicators.time_in_window

    return fitness


# ============================================================================
# Genetic Algorithm for IC Search
# ============================================================================

@dataclass
class GeneticSearchConfig:
    """Configuration for genetic algorithm IC search."""
    population_size: int = 50
    n_generations: int = 100
    mutation_rate: float = 0.1
    crossover_rate: float = 0.7
    elite_fraction: float = 0.1

    # Simulation parameters for fitness evaluation
    N: int = 64
    L: float = 2*np.pi
    nu: float = 0.0005
    T_eval: float = 1.0  # Simulation time for evaluation

    # Output
    save_best: bool = True
    output_dir: str = 'results/ic_search'


class GeneticICSearch:
    """
    Genetic algorithm search for Type II blowup initial conditions.

    Uses evolutionary optimization to find IC parameters that
    maximize blowup potential (fitness based on indicators).
    """

    def __init__(self, config: Optional[GeneticSearchConfig] = None):
        self.config = config or GeneticSearchConfig()
        self.population: List[ICParameters] = []
        self.fitness_history: List[float] = []
        self.best_individual: Optional[ICParameters] = None
        self.best_fitness: float = -np.inf

    def initialize_population(self) -> None:
        """Initialize random population of IC parameters."""
        self.population = []

        for _ in range(self.config.population_size):
            params = ICParameters(
                concentration_scale=np.random.uniform(0.05, 0.3),
                alignment_angle=np.random.uniform(0, 2*np.pi),
                helicity=np.random.uniform(-1, 1),
                symmetry=np.random.choice(['axisymmetric', 'helical', 'triaxial', 'none']),
                amplitude=np.random.uniform(1, 10),
                radial_peak=np.random.uniform(0.3, 0.9),
                radial_width=np.random.uniform(0.05, 0.2),
                axial_modes=np.random.randint(1, 5),
                axial_phase=np.random.uniform(0, 2*np.pi),
                tube_separation=np.random.uniform(0.1, 0.5),
                tube_radius=np.random.uniform(0.05, 0.2),
                knot_type=np.random.choice(['none', 'trefoil', 'torus', 'figure8']),
                knot_aspect=np.random.uniform(0.5, 2.0),
                perturbation_amplitude=np.random.uniform(0, 0.1),
                perturbation_seed=np.random.randint(0, 10000),
            )
            self.population.append(params)

    def evaluate_fitness(self, params: ICParameters) -> float:
        """
        Evaluate fitness of an IC by running short simulation.

        Returns fitness score based on blowup indicators.
        """
        from ..simulator.spectral_ns import SpectralNSSolver, SolverConfig
        from ..analysis.rate_tracker import RateTracker

        # Generate IC
        omega_hat = generate_ic_from_params(params, self.config.N, self.config.L)

        # Setup solver
        solver_config = SolverConfig(
            N=self.config.N,
            L=self.config.L,
            nu=self.config.nu,
            dealias=True,
            cfl=0.5,
            integrator='rk4'
        )
        solver = SpectralNSSolver(solver_config)

        # Run simulation
        try:
            history = solver.run(omega_hat, self.config.T_eval)
        except Exception as e:
            print(f"Simulation failed: {e}")
            return -1e10

        # Compute indicators from final state
        times = np.array(history['times'])
        u_Linf = np.array(history['u_Linf'])
        omega_Linf = np.array(history['omega_Linf'])

        # Fit blowup rate
        rate_tracker = RateTracker()
        alpha, T_star = rate_tracker.fit_blowup_rate(times, u_Linf)

        # Get final velocity and vorticity fields
        u, v, w = solver.get_velocity(omega_hat)
        omega_x = np.real(ifftn(omega_hat[0]))
        omega_y = np.real(ifftn(omega_hat[1]))
        omega_z = np.real(ifftn(omega_hat[2]))

        # Compute indicators
        indicators = compute_blowup_indicators(
            omega_x, omega_y, omega_z, u, v, w, self.config.L
        )
        indicators.alpha_effective = alpha

        # Compute time in Type II window
        time_in_window = 0.0
        for i in range(len(times) - 1):
            if len(u_Linf) > i:
                # Compute local alpha from consecutive points
                if i > 0 and T_star < np.inf and T_star > times[i]:
                    local_alpha = self._local_alpha(times[i:i+2], u_Linf[i:i+2], T_star)
                    if ALPHA_LOWER <= local_alpha < ALPHA_UPPER:
                        time_in_window += times[i+1] - times[i]

        indicators.time_in_window = time_in_window
        indicators.max_sustained_alpha = alpha

        # Compute fitness
        fitness = compute_fitness(indicators)
        indicators.fitness = fitness

        return fitness

    def _local_alpha(self, times: np.ndarray, u_Linf: np.ndarray, T_star: float) -> float:
        """Compute local alpha from two points."""
        if len(times) < 2 or len(u_Linf) < 2:
            return 0.5

        dt1 = T_star - times[0]
        dt2 = T_star - times[1]

        if dt1 <= 0 or dt2 <= 0 or u_Linf[0] <= 0 or u_Linf[1] <= 0:
            return 0.5

        log_ratio = np.log(u_Linf[1] / u_Linf[0])
        log_time_ratio = np.log(dt1 / dt2)

        if abs(log_time_ratio) < 1e-10:
            return 0.5

        return log_ratio / log_time_ratio

    def crossover(self, parent1: ICParameters, parent2: ICParameters) -> ICParameters:
        """Crossover two parents to create offspring."""
        child_dict = {}

        for key in parent1.to_dict().keys():
            if np.random.random() < 0.5:
                child_dict[key] = getattr(parent1, key)
            else:
                child_dict[key] = getattr(parent2, key)

        return ICParameters.from_dict(child_dict)

    def mutate(self, params: ICParameters) -> ICParameters:
        """Mutate an individual's parameters."""
        d = params.to_dict()

        # Mutate each continuous parameter with probability mutation_rate
        continuous_params = [
            ('concentration_scale', 0.05, 0.3),
            ('alignment_angle', 0, 2*np.pi),
            ('helicity', -1, 1),
            ('amplitude', 1, 10),
            ('radial_peak', 0.3, 0.9),
            ('radial_width', 0.05, 0.2),
            ('axial_phase', 0, 2*np.pi),
            ('tube_separation', 0.1, 0.5),
            ('tube_radius', 0.05, 0.2),
            ('knot_aspect', 0.5, 2.0),
            ('perturbation_amplitude', 0, 0.1),
        ]

        for key, low, high in continuous_params:
            if np.random.random() < self.config.mutation_rate:
                # Gaussian mutation
                current = d[key]
                mutation = np.random.normal(0, (high - low) * 0.1)
                d[key] = np.clip(current + mutation, low, high)

        # Mutate discrete parameters
        if np.random.random() < self.config.mutation_rate:
            d['symmetry'] = np.random.choice(['axisymmetric', 'helical', 'triaxial', 'none'])

        if np.random.random() < self.config.mutation_rate:
            d['axial_modes'] = np.random.randint(1, 5)

        if np.random.random() < self.config.mutation_rate:
            d['knot_type'] = np.random.choice(['none', 'trefoil', 'torus', 'figure8'])

        if np.random.random() < self.config.mutation_rate:
            d['perturbation_seed'] = np.random.randint(0, 10000)

        return ICParameters.from_dict(d)

    def select_parents(self, fitnesses: List[float]) -> Tuple[int, int]:
        """Tournament selection of parents."""
        tournament_size = 3

        def tournament():
            candidates = np.random.choice(len(fitnesses), tournament_size, replace=False)
            best = max(candidates, key=lambda i: fitnesses[i])
            return best

        return tournament(), tournament()

    def run(self, verbose: bool = True) -> ICParameters:
        """
        Run genetic algorithm search.

        Returns best IC parameters found.
        """
        self.initialize_population()

        for gen in range(self.config.n_generations):
            # Evaluate fitness for all individuals
            fitnesses = []
            for i, params in enumerate(self.population):
                fitness = self.evaluate_fitness(params)
                fitnesses.append(fitness)

                if fitness > self.best_fitness:
                    self.best_fitness = fitness
                    self.best_individual = params

            self.fitness_history.append(max(fitnesses))

            if verbose:
                print(f"Generation {gen+1}/{self.config.n_generations}: "
                      f"Best fitness = {max(fitnesses):.4f}, "
                      f"Mean fitness = {np.mean(fitnesses):.4f}")

            # Selection and reproduction
            new_population = []

            # Elitism: keep best individuals
            n_elite = int(self.config.elite_fraction * self.config.population_size)
            elite_indices = np.argsort(fitnesses)[-n_elite:]
            for idx in elite_indices:
                new_population.append(self.population[idx])

            # Fill rest with offspring
            while len(new_population) < self.config.population_size:
                # Select parents
                idx1, idx2 = self.select_parents(fitnesses)
                parent1 = self.population[idx1]
                parent2 = self.population[idx2]

                # Crossover
                if np.random.random() < self.config.crossover_rate:
                    child = self.crossover(parent1, parent2)
                else:
                    child = parent1 if fitnesses[idx1] > fitnesses[idx2] else parent2

                # Mutation
                child = self.mutate(child)

                new_population.append(child)

            self.population = new_population

        # Save best
        if self.config.save_best and self.best_individual is not None:
            self._save_best()

        return self.best_individual

    def _save_best(self) -> None:
        """Save best individual to file."""
        output_dir = Path(self.config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        result = {
            'best_params': self.best_individual.to_dict(),
            'best_fitness': self.best_fitness,
            'fitness_history': self.fitness_history,
            'config': {
                'population_size': self.config.population_size,
                'n_generations': self.config.n_generations,
                'mutation_rate': self.config.mutation_rate,
                'crossover_rate': self.config.crossover_rate,
                'N': self.config.N,
                'nu': self.config.nu,
                'T_eval': self.config.T_eval,
            }
        }

        with open(output_dir / 'best_ic_params.json', 'w') as f:
            json.dump(result, f, indent=2)


# ============================================================================
# Specific Blowup Candidate Generators
# ============================================================================

def anti_parallel_tubes_sweep(
    N: int = 64,
    L: float = 2*np.pi,
    separations: Optional[List[float]] = None,
    amplitudes: Optional[List[float]] = None
) -> List[Tuple[ICParameters, np.ndarray]]:
    """
    Generate anti-parallel vortex tube ICs with varying parameters.

    Returns list of (params, omega_hat) tuples.
    """
    if separations is None:
        separations = [0.1, 0.2, 0.3, 0.4, 0.5]
    if amplitudes is None:
        amplitudes = [2, 5, 10]

    results = []

    for sep in separations:
        for amp in amplitudes:
            params = ICParameters(
                symmetry='none',
                tube_separation=sep,
                amplitude=amp,
                tube_radius=0.1,
                axial_modes=2,
            )
            omega_hat = generate_ic_from_params(params, N, L)
            results.append((params, omega_hat))

    return results


def vortex_knot_sweep(
    N: int = 64,
    L: float = 2*np.pi,
    knot_types: Optional[List[str]] = None,
    aspects: Optional[List[float]] = None
) -> List[Tuple[ICParameters, np.ndarray]]:
    """
    Generate vortex knot ICs with varying topology.

    Returns list of (params, omega_hat) tuples.
    """
    if knot_types is None:
        knot_types = ['trefoil', 'torus', 'figure8']
    if aspects is None:
        aspects = [0.5, 1.0, 1.5, 2.0]

    results = []

    for knot in knot_types:
        for aspect in aspects:
            params = ICParameters(
                symmetry='none',
                knot_type=knot,
                knot_aspect=aspect,
                amplitude=5.0,
                radial_peak=0.5,
                tube_radius=0.1,
            )
            omega_hat = generate_ic_from_params(params, N, L)
            results.append((params, omega_hat))

    return results


def hou_luo_parameter_sweep(
    N: int = 64,
    L: float = 2*np.pi,
    amplitudes: Optional[List[float]] = None,
    radial_peaks: Optional[List[float]] = None,
    axial_modes_list: Optional[List[int]] = None
) -> List[Tuple[ICParameters, np.ndarray]]:
    """
    Generate Hou-Luo style axisymmetric ICs with parameter variations.

    Returns list of (params, omega_hat) tuples.
    """
    if amplitudes is None:
        amplitudes = [3, 5, 8, 10]
    if radial_peaks is None:
        radial_peaks = [0.7, 0.8, 0.9]
    if axial_modes_list is None:
        axial_modes_list = [1, 2, 3]

    results = []

    for amp in amplitudes:
        for r_peak in radial_peaks:
            for modes in axial_modes_list:
                params = ICParameters(
                    symmetry='axisymmetric',
                    amplitude=amp,
                    radial_peak=r_peak,
                    radial_width=0.1,
                    axial_modes=modes,
                    axial_phase=0,
                )
                omega_hat = generate_ic_from_params(params, N, L)
                results.append((params, omega_hat))

    return results


def helical_flow_sweep(
    N: int = 64,
    L: float = 2*np.pi,
    helicities: Optional[List[float]] = None,
    concentrations: Optional[List[float]] = None
) -> List[Tuple[ICParameters, np.ndarray]]:
    """
    Generate helical flow ICs.

    Returns list of (params, omega_hat) tuples.
    """
    if helicities is None:
        helicities = [-1.0, -0.5, 0, 0.5, 1.0]
    if concentrations is None:
        concentrations = [0.05, 0.1, 0.2]

    results = []

    for h in helicities:
        for conc in concentrations:
            params = ICParameters(
                symmetry='helical',
                helicity=h,
                concentration_scale=conc,
                amplitude=5.0,
                axial_modes=2,
            )
            omega_hat = generate_ic_from_params(params, N, L)
            results.append((params, omega_hat))

    return results


# ============================================================================
# Numerical Protocol for Candidate Evaluation
# ============================================================================

@dataclass
class CandidateEvaluation:
    """Results from evaluating a blowup candidate IC."""
    params: ICParameters
    indicators: BlowupIndicators
    time_series: Dict[str, np.ndarray]
    max_u_Linf: float
    max_omega_Linf: float
    sustained_alpha: float
    time_in_type_ii_window: float
    final_classification: str


def evaluate_candidate(
    params: ICParameters,
    N: int = 64,
    L: float = 2*np.pi,
    nu: float = 0.0005,
    T_final: float = 2.0,
    verbose: bool = True
) -> CandidateEvaluation:
    """
    Full numerical evaluation of a blowup candidate IC.

    Runs spectral NS solver and computes comprehensive diagnostics.

    Args:
        params: IC parameters
        N: Grid resolution
        L: Domain size
        nu: Viscosity
        T_final: Final simulation time
        verbose: Print progress

    Returns:
        CandidateEvaluation with full analysis
    """
    from ..simulator.spectral_ns import SpectralNSSolver, SolverConfig
    from ..analysis.rate_tracker import RateTracker

    # Generate IC
    omega_hat = generate_ic_from_params(params, N, L)

    # Setup solver
    solver_config = SolverConfig(
        N=N, L=L, nu=nu, dealias=True, cfl=0.5, integrator='rk4'
    )
    solver = SpectralNSSolver(solver_config)

    # Storage for detailed tracking
    alpha_history = []

    def callback(t, omega_hat_current, u_tuple, diagnostics):
        if verbose and len(alpha_history) % 50 == 0:
            print(f"t = {t:.4f}, ||u||_inf = {diagnostics['u_Linf']:.4e}, "
                  f"||omega||_inf = {diagnostics['omega_Linf']:.4e}")

    # Run simulation
    if verbose:
        print(f"Running simulation with params: {params.symmetry}, amp={params.amplitude}")

    history = solver.run(omega_hat, T_final, callback=callback)

    # Extract time series
    times = np.array(history['times'])
    u_Linf = np.array(history['u_Linf'])
    omega_Linf = np.array(history['omega_Linf'])
    energy = np.array(history['energy'])
    enstrophy = np.array(history['enstrophy'])

    # Fit blowup rate
    rate_tracker = RateTracker()
    alpha, T_star = rate_tracker.fit_blowup_rate(times, u_Linf)

    # Track time-varying alpha
    _, alpha_evolution = rate_tracker.track_rate_evolution(times, u_Linf, window_size=20)

    # Compute time in Type II window
    time_in_window = 0.0
    if len(alpha_evolution) > 0:
        for i in range(len(alpha_evolution) - 1):
            if ALPHA_LOWER <= alpha_evolution[i] < ALPHA_UPPER:
                if i + 20 < len(times):
                    time_in_window += times[i + 21] - times[i + 20]

    # Get final state indicators
    u, v, w = solver.get_velocity(omega_hat)
    omega_x = np.real(ifftn(omega_hat[0]))
    omega_y = np.real(ifftn(omega_hat[1]))
    omega_z = np.real(ifftn(omega_hat[2]))

    indicators = compute_blowup_indicators(omega_x, omega_y, omega_z, u, v, w, L)
    indicators.alpha_effective = alpha
    indicators.time_in_window = time_in_window
    indicators.fitness = compute_fitness(indicators)

    # Classification
    classification = rate_tracker.classify_blowup(alpha)

    if verbose:
        print(f"\nResults:")
        print(f"  Final alpha: {alpha:.4f}")
        print(f"  T*: {T_star:.4f}")
        print(f"  Time in Type II window: {time_in_window:.4f}")
        print(f"  Classification: {classification}")
        print(f"  Fitness: {indicators.fitness:.4f}")

    return CandidateEvaluation(
        params=params,
        indicators=indicators,
        time_series={
            'times': times,
            'u_Linf': u_Linf,
            'omega_Linf': omega_Linf,
            'energy': energy,
            'enstrophy': enstrophy,
            'alpha_evolution': alpha_evolution,
        },
        max_u_Linf=np.max(u_Linf),
        max_omega_Linf=np.max(omega_Linf),
        sustained_alpha=alpha,
        time_in_type_ii_window=time_in_window,
        final_classification=classification,
    )


def run_systematic_search(
    viscosities: Optional[List[float]] = None,
    N: int = 64,
    L: float = 2*np.pi,
    T_final: float = 2.0,
    output_dir: str = 'results/ic_search',
    verbose: bool = True
) -> List[CandidateEvaluation]:
    """
    Run systematic search over multiple IC families and viscosities.

    Tests:
    - Anti-parallel tubes
    - Vortex knots
    - Hou-Luo style
    - Helical flows

    Returns list of all evaluations sorted by fitness.
    """
    if viscosities is None:
        viscosities = [0.001, 0.0005, 0.0002, 0.0001]

    all_evaluations = []

    # Generate all candidate ICs
    if verbose:
        print("Generating candidate ICs...")

    all_candidates = []
    all_candidates.extend(anti_parallel_tubes_sweep(N, L))
    all_candidates.extend(vortex_knot_sweep(N, L))
    all_candidates.extend(hou_luo_parameter_sweep(N, L))
    all_candidates.extend(helical_flow_sweep(N, L))

    if verbose:
        print(f"Total candidates: {len(all_candidates)}")

    # Evaluate each candidate at each viscosity
    for nu in viscosities:
        if verbose:
            print(f"\n{'='*60}")
            print(f"Testing viscosity nu = {nu}")
            print('='*60)

        for i, (params, _) in enumerate(all_candidates):
            if verbose:
                print(f"\nCandidate {i+1}/{len(all_candidates)}")

            try:
                evaluation = evaluate_candidate(
                    params, N=N, L=L, nu=nu, T_final=T_final, verbose=verbose
                )
                all_evaluations.append(evaluation)
            except Exception as e:
                if verbose:
                    print(f"Failed: {e}")

    # Sort by fitness
    all_evaluations.sort(key=lambda e: e.indicators.fitness, reverse=True)

    # Save results
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    summary = []
    for i, eval in enumerate(all_evaluations[:20]):  # Top 20
        summary.append({
            'rank': i + 1,
            'fitness': eval.indicators.fitness,
            'alpha': eval.sustained_alpha,
            'time_in_window': eval.time_in_type_ii_window,
            'classification': eval.final_classification,
            'params': eval.params.to_dict(),
        })

    with open(output_path / 'search_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    if verbose:
        print(f"\n{'='*60}")
        print("TOP 10 CANDIDATES")
        print('='*60)
        for i, eval in enumerate(all_evaluations[:10]):
            print(f"\n{i+1}. {eval.params.symmetry} (alpha={eval.sustained_alpha:.3f})")
            print(f"   Fitness: {eval.indicators.fitness:.4f}")
            print(f"   Time in window: {eval.time_in_type_ii_window:.4f}")
            print(f"   Classification: {eval.final_classification}")

    return all_evaluations


# ============================================================================
# Main Entry Point
# ============================================================================

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Search for Type II blowup ICs')
    parser.add_argument('--mode', choices=['genetic', 'systematic', 'single'],
                        default='systematic', help='Search mode')
    parser.add_argument('--N', type=int, default=64, help='Grid resolution')
    parser.add_argument('--nu', type=float, default=0.0005, help='Viscosity')
    parser.add_argument('--T', type=float, default=2.0, help='Final time')
    parser.add_argument('--output', type=str, default='results/ic_search',
                        help='Output directory')

    args = parser.parse_args()

    if args.mode == 'genetic':
        config = GeneticSearchConfig(
            N=args.N, nu=args.nu, T_eval=args.T,
            output_dir=args.output
        )
        searcher = GeneticICSearch(config)
        best = searcher.run(verbose=True)
        print(f"\nBest IC parameters: {best.to_dict()}")

    elif args.mode == 'systematic':
        results = run_systematic_search(
            N=args.N, T_final=args.T,
            output_dir=args.output,
            verbose=True
        )

    elif args.mode == 'single':
        # Test single Hou-Luo style IC
        params = ICParameters(
            symmetry='axisymmetric',
            amplitude=5.0,
            radial_peak=0.9,
            radial_width=0.1,
            axial_modes=2,
        )
        evaluation = evaluate_candidate(
            params, N=args.N, nu=args.nu, T_final=args.T, verbose=True
        )

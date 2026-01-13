"""
Initial conditions for Navier-Stokes simulations.

Provides several canonical initial conditions known to develop
strong gradients or potentially approach singularity.
"""

import numpy as np
from numpy.fft import fftn, fftfreq
from typing import Tuple


def taylor_green(N: int = 64, L: float = 2*np.pi, amplitude: float = 1.0) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Taylor-Green vortex initial condition.

    Classic test case with known analytical solution for short times.
    Develops complex 3D structure and strong gradients.

    u = A cos(x) sin(y) cos(z)
    v = -A sin(x) cos(y) cos(z)
    w = 0

    Returns vorticity in spectral space.
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    # Velocity field
    u = amplitude * np.cos(X) * np.sin(Y) * np.cos(Z)
    v = -amplitude * np.sin(X) * np.cos(Y) * np.cos(Z)
    w = np.zeros_like(X)

    # Convert to vorticity
    return velocity_to_vorticity_spectral(u, v, w, L)


def kida_vortex(N: int = 64, L: float = 2*np.pi, amplitude: float = 1.0,
                wavenumber: int = 2) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Kida vortex - elliptical vortex that develops strong gradients.

    A perturbed vortex configuration known to exhibit
    intense vortex stretching.

    Returns vorticity in spectral space.
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    k = wavenumber

    # Velocity field (perturbed shear flow with vortical structure)
    u = amplitude * np.sin(k * Z) + 0.5 * amplitude * np.cos(k * Y)
    v = amplitude * np.sin(k * X) + 0.5 * amplitude * np.cos(k * Z)
    w = amplitude * np.sin(k * Y) + 0.5 * amplitude * np.cos(k * X)

    return velocity_to_vorticity_spectral(u, v, w, L)


def perturbed_burgers(N: int = 64, L: float = 2*np.pi, amplitude: float = 1.0,
                      strain_rate: float = 1.0) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Perturbed Burgers vortex.

    The Burgers vortex is a steady solution with balance between
    stretching and diffusion. Perturbations can potentially
    trigger instability.

    Returns vorticity in spectral space.
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    # Center the domain
    X_c = X - L/2
    Y_c = Y - L/2
    Z_c = Z - L/2

    r_sq = X_c**2 + Y_c**2

    # Burgers vortex circulation parameter
    Gamma = amplitude

    # Azimuthal velocity: u_theta = Gamma/(2*pi*r) * (1 - exp(-r²/4))
    # Converted to Cartesian
    r = np.sqrt(r_sq + 1e-10)
    u_theta = Gamma / (2 * np.pi * r) * (1 - np.exp(-r_sq / 4))

    u = -u_theta * Y_c / r
    v = u_theta * X_c / r

    # Axial strain flow
    w = strain_rate * Z_c

    # Add perturbation to potentially trigger instability
    perturbation = 0.1 * amplitude * np.sin(2 * np.pi * Z / L)
    u += perturbation * np.exp(-r_sq / 2)
    v += perturbation * np.exp(-r_sq / 2) * np.cos(2 * np.pi * X / L)

    return velocity_to_vorticity_spectral(u, v, w, L)


def random_field(N: int = 64, L: float = 2*np.pi, amplitude: float = 1.0,
                 k_peak: int = 4, seed: int = None) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Random divergence-free velocity field.

    Energy spectrum peaks at wavenumber k_peak.
    Useful for exploring parameter space.

    Returns vorticity in spectral space.
    """
    if seed is not None:
        np.random.seed(seed)

    # Wavenumbers
    k = fftfreq(N, d=L/(2*np.pi*N))
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
    k_mag = np.sqrt(kx**2 + ky**2 + kz**2)
    k_mag[0, 0, 0] = 1.0  # Avoid division by zero

    # Random phases
    phase_x = np.random.uniform(0, 2*np.pi, (N, N, N))
    phase_y = np.random.uniform(0, 2*np.pi, (N, N, N))
    phase_z = np.random.uniform(0, 2*np.pi, (N, N, N))

    # Energy spectrum: E(k) ~ k^4 exp(-(k/k_peak)^2)
    energy_spectrum = k_mag**4 * np.exp(-(k_mag / k_peak)**2)

    # Generate random spectral coefficients
    amp = amplitude * np.sqrt(energy_spectrum)
    u_hat = amp * np.exp(1j * phase_x)
    v_hat = amp * np.exp(1j * phase_y)
    w_hat = amp * np.exp(1j * phase_z)

    # Project to divergence-free (Leray projection)
    # P = I - k⊗k/|k|²
    k_sq = k_mag**2
    div = (kx * u_hat + ky * v_hat + kz * w_hat) / k_sq
    u_hat -= kx * div
    v_hat -= ky * div
    w_hat -= kz * div

    # Zero mean
    u_hat[0, 0, 0] = 0
    v_hat[0, 0, 0] = 0
    w_hat[0, 0, 0] = 0

    # Make Hermitian for real output
    from numpy.fft import ifftn
    u = np.real(ifftn(u_hat))
    v = np.real(ifftn(v_hat))
    w = np.real(ifftn(w_hat))

    return velocity_to_vorticity_spectral(u, v, w, L)


def anti_parallel_vortex_tubes(N: int = 64, L: float = 2*np.pi, amplitude: float = 1.0,
                               separation: float = 0.3) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Anti-parallel vortex tubes - configuration studied by Hou-Luo.

    Two vortex tubes of opposite sign approaching each other.
    This configuration is believed to potentially develop singularities.

    Returns vorticity in spectral space.
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    # Center
    cx, cy = L/2, L/2

    # Two vortex cores at y = cy ± separation*L
    y1 = cy + separation * L
    y2 = cy - separation * L

    # Gaussian vortex cores
    sigma = L / 10  # Core radius

    # Distance from each core
    r1_sq = (X - cx)**2 + (Y - y1)**2
    r2_sq = (X - cx)**2 + (Y - y2)**2

    # Vorticity (in z-direction) - opposite signs
    omega_z = amplitude * (np.exp(-r1_sq / (2*sigma**2)) - np.exp(-r2_sq / (2*sigma**2)))

    # Velocity from stream function (2D for simplicity, extended to 3D)
    # ψ = amplitude * sigma² * (exp(-r1²/2σ²) - exp(-r2²/2σ²))
    # u = -∂ψ/∂y, v = ∂ψ/∂x

    u = amplitude * sigma**2 * (
        (Y - y1) / sigma**2 * np.exp(-r1_sq / (2*sigma**2)) -
        (Y - y2) / sigma**2 * np.exp(-r2_sq / (2*sigma**2))
    )
    v = -amplitude * sigma**2 * (
        (X - cx) / sigma**2 * np.exp(-r1_sq / (2*sigma**2)) -
        (X - cx) / sigma**2 * np.exp(-r2_sq / (2*sigma**2))
    )

    # Add z-variation for 3D
    w = 0.1 * amplitude * np.sin(2 * np.pi * Z / L) * (
        np.exp(-r1_sq / (2*sigma**2)) + np.exp(-r2_sq / (2*sigma**2))
    )

    return velocity_to_vorticity_spectral(u, v, w, L)


def hou_luo_candidate(N: int = 64, L: float = 2*np.pi, amplitude: float = 1.0,
                      r0: float = 0.9, delta: float = 0.1,
                      mode: str = 'full') -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Hou-Luo blowup candidate initial condition.

    Based on Luo & Hou (2014) "Potentially singular solutions of the 3D
    axisymmetric Euler equations" (PNAS). This axisymmetric initial condition
    was shown numerically to develop a potential singularity for 3D Euler
    at a point on the symmetry axis.

    Key features of the Hou-Luo scenario:
    - Axisymmetric flow with swirl (angular velocity u_theta)
    - Angular vorticity omega_theta concentrated near outer boundary
    - Odd symmetry in z: omega_1 = omega_theta/r ~ sin^2(z) at r = r0
    - Vortex stretching amplification mechanism near the axis

    For Navier-Stokes with small viscosity, this is a candidate for
    approaching blowup behavior before viscous regularization.

    In cylindrical coordinates (r, theta, z), the Hou-Luo IC has:
    - u_theta(r,z) = A * f(r) * sin^2(pi*z/L)
    - f(r) peaks near r = r0 (outer region) and vanishes at r = 0
    - omega_theta = d(r*u_theta)/dr / r has specific radial structure

    Args:
        N: Grid resolution per dimension
        L: Domain size [0, L]^3 (periodic cube approximating cylinder)
        amplitude: Amplitude of the initial velocity
        r0: Radial location of peak angular velocity (fraction of L/2)
        delta: Width of the radial profile
        mode: 'full' for complete 3D, 'simplified' for faster testing

    Returns:
        Vorticity in spectral space (omega_x_hat, omega_y_hat, omega_z_hat)

    References:
        - Luo, G., Hou, T.Y. "Potentially singular solutions of the 3D
          axisymmetric Euler equations" PNAS 111(36), 2014
        - Luo, G., Hou, T.Y. "Toward the finite-time blowup of the 3D
          axisymmetric Euler equations" SIAM Multiscale Model. Simul. 2014
    """
    x = np.linspace(0, L, N, endpoint=False)
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')

    # Center domain for cylindrical coordinates
    X_c = X - L/2
    Y_c = Y - L/2
    Z_c = Z - L/2  # Center z as well

    # Cylindrical r (distance from z-axis)
    r = np.sqrt(X_c**2 + Y_c**2)
    r_safe = np.maximum(r, 1e-10)  # Avoid division by zero

    # Azimuthal angle theta
    theta = np.arctan2(Y_c, X_c)

    # Radial profile f(r) - peaks at r0*L/2, vanishes at r=0 and large r
    # Using a smooth bump function: r^2 * exp(-(r - r0*L/2)^2 / (2*delta^2*L^2/4))
    r_peak = r0 * L / 2
    sigma_r = delta * L / 2

    # f(r) = r^2 * exp(-((r - r_peak)^2)/(2*sigma_r^2)) for smooth approach to axis
    # This ensures u_theta ~ r near r=0 (solid body rotation), peaks at r_peak
    f_r = (r**2 / (r_peak**2 + 1e-10)) * np.exp(-((r - r_peak)**2) / (2 * sigma_r**2))

    # z-profile: sin^2(pi*z/L) with odd symmetry centered at z=L/2
    # Map to centered coordinate: use sin^2(pi*(Z - L/2)/L) = sin^2(pi*Z_c/L)
    # For odd symmetry we use sin(2*pi*Z_c/L) component
    g_z = np.sin(2 * np.pi * Z_c / L)**2

    # Hou-Luo also has specific z-monotonicity. Add asymmetric perturbation
    # to break reflection symmetry and promote one-sided concentration
    h_z = np.sin(np.pi * Z_c / L)  # Odd in z

    if mode == 'simplified':
        # Simplified version: basic axisymmetric swirl flow
        # u_theta = A * f(r) * g(z)
        u_theta = amplitude * f_r * g_z

        # Axial velocity: small perturbation to trigger dynamics
        u_z = 0.1 * amplitude * f_r * h_z

    else:  # 'full' mode
        # Full Hou-Luo inspired IC with stronger angular vorticity concentration
        #
        # The key mechanism in Hou-Luo is that omega_1 = omega_theta/r
        # at the boundary drives u_1 = u_theta/r through the Biot-Savart law
        #
        # omega_theta = (1/r) * d(r*u_theta)/dr - du_z/dz
        #
        # We design u_theta to have strong gradient near the axis

        # Radial profile that creates intense omega_theta/r near axis
        # Use r * (1 - r/r_max)^2 * exp(...) type profile
        r_max = 0.95 * L / 2
        f_r_hou = (r / r_peak) * np.maximum(1 - r / r_max, 0)**2 * \
                  np.exp(-((r - r_peak)**2) / (2 * sigma_r**2))

        # Angular velocity with Hou-Luo type z-dependence
        # The sin^2 creates nodes at z = 0, L/2, L
        u_theta = amplitude * f_r_hou * g_z

        # Add swirl perturbation to break azimuthal symmetry slightly
        # (In pure axisymmetric, this would be zero, but we're on a Cartesian grid)
        swirl_perturb = 0.05 * amplitude * np.sin(2 * theta) * f_r_hou * g_z
        u_theta += swirl_perturb

        # Axial velocity - computed to enhance vortex stretching
        # Near the axis, u_z > 0 for z > 0 and u_z < 0 for z < 0
        # This creates convergent flow that amplifies omega_theta/r

        # Stream function approach: psi(r,z) such that
        # u_r = -(1/r) * dpsi/dz, u_z = (1/r) * dpsi/dr
        # For our purpose, a simpler direct specification:
        u_z_profile = 0.2 * amplitude * (1 - (r / (L/2))**2) * h_z
        u_z = u_z_profile * np.exp(-r**2 / (r_peak**2))

        # Radial velocity for incompressibility (approximate)
        # div(u) = 0 in cylindrical: (1/r)*d(r*u_r)/dr + du_z/dz = 0
        # For axisymmetric: du_r/dr + u_r/r + du_z/dz = 0
        # We'll let the spectral solver handle projection to div-free
        u_r = np.zeros_like(X)

    # Convert from cylindrical (u_r, u_theta, u_z) to Cartesian (u, v, w)
    # u = u_r * cos(theta) - u_theta * sin(theta)
    # v = u_r * sin(theta) + u_theta * cos(theta)
    # w = u_z

    if mode == 'simplified':
        u_r = np.zeros_like(X)
        u = u_r * np.cos(theta) - u_theta * np.sin(theta)
        v = u_r * np.sin(theta) + u_theta * np.cos(theta)
        w = u_z
    else:
        u = u_r * np.cos(theta) - u_theta * np.sin(theta)
        v = u_r * np.sin(theta) + u_theta * np.cos(theta)
        w = u_z

    # Project to divergence-free and return vorticity
    return velocity_to_vorticity_spectral_projected(u, v, w, L)


def velocity_to_vorticity_spectral_projected(u: np.ndarray, v: np.ndarray, w: np.ndarray,
                                              L: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Convert velocity to vorticity in spectral space with Leray projection.

    First projects velocity to divergence-free, then computes vorticity.
    This ensures exact incompressibility for initial conditions constructed
    in physical space (like Hou-Luo).
    """
    N = u.shape[0]
    k = fftfreq(N, d=L/(2*np.pi*N))
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
    k_sq = kx**2 + ky**2 + kz**2
    k_sq[0, 0, 0] = 1.0  # Avoid division by zero

    u_hat = fftn(u)
    v_hat = fftn(v)
    w_hat = fftn(w)

    # Leray projection: P = I - k⊗k/|k|²
    # Remove divergent part
    div = (kx * u_hat + ky * v_hat + kz * w_hat) / k_sq
    u_hat_proj = u_hat - kx * div
    v_hat_proj = v_hat - ky * div
    w_hat_proj = w_hat - kz * div

    # Zero mean
    u_hat_proj[0, 0, 0] = 0
    v_hat_proj[0, 0, 0] = 0
    w_hat_proj[0, 0, 0] = 0

    # Compute vorticity: omega = curl(u)
    omega_x_hat = 1j * (ky * w_hat_proj - kz * v_hat_proj)
    omega_y_hat = 1j * (kz * u_hat_proj - kx * w_hat_proj)
    omega_z_hat = 1j * (kx * v_hat_proj - ky * u_hat_proj)

    return omega_x_hat, omega_y_hat, omega_z_hat


def velocity_to_vorticity_spectral(u: np.ndarray, v: np.ndarray, w: np.ndarray,
                                   L: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Convert velocity to vorticity in spectral space."""
    N = u.shape[0]
    k = fftfreq(N, d=L/(2*np.pi*N))
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')

    u_hat = fftn(u)
    v_hat = fftn(v)
    w_hat = fftn(w)

    # ω = ∇ × u
    omega_x_hat = 1j * (ky * w_hat - kz * v_hat)
    omega_y_hat = 1j * (kz * u_hat - kx * w_hat)
    omega_z_hat = 1j * (kx * v_hat - ky * u_hat)

    return omega_x_hat, omega_y_hat, omega_z_hat

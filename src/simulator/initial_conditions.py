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

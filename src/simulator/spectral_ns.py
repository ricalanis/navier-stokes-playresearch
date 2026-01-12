"""
Pseudo-spectral Navier-Stokes solver for 3D incompressible flow.

Solves the vorticity formulation:
    ∂ω/∂t + (u·∇)ω = (ω·∇)u + ν∆ω

with divergence-free velocity recovered via Biot-Savart.
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq
from typing import Tuple, Optional, Dict, List
from dataclasses import dataclass


@dataclass
class SolverConfig:
    """Configuration for the spectral solver."""
    N: int = 64                    # Grid points per dimension
    L: float = 2 * np.pi           # Domain size [0, L]^3
    nu: float = 0.01               # Kinematic viscosity
    dealias: bool = True           # Apply 2/3 dealiasing
    cfl: float = 0.5               # CFL number for adaptive dt
    integrator: str = 'rk4'        # Time integrator: 'rk4' or 'euler'


class SpectralNSSolver:
    """
    Pseudo-spectral solver for 3D incompressible Navier-Stokes.

    Uses vorticity formulation to avoid pressure computation.
    FFT-based spectral derivatives with 2/3 dealiasing rule.
    """

    def __init__(self, config: Optional[SolverConfig] = None):
        self.config = config or SolverConfig()
        self._setup_grid()
        self._setup_spectral()

    def _setup_grid(self):
        """Initialize physical space grid."""
        N, L = self.config.N, self.config.L
        self.dx = L / N

        # Physical coordinates
        x = np.linspace(0, L, N, endpoint=False)
        self.X, self.Y, self.Z = np.meshgrid(x, x, x, indexing='ij')

    def _setup_spectral(self):
        """Initialize spectral space quantities."""
        N, L = self.config.N, self.config.L

        # Wavenumbers
        k = fftfreq(N, d=L/(2*np.pi*N))
        self.kx, self.ky, self.kz = np.meshgrid(k, k, k, indexing='ij')

        # |k|² for Laplacian and Biot-Savart
        self.k_sq = self.kx**2 + self.ky**2 + self.kz**2
        self.k_sq[0, 0, 0] = 1.0  # Avoid division by zero

        # Dealiasing mask (2/3 rule)
        if self.config.dealias:
            k_max = N // 3
            self.dealias_mask = (
                (np.abs(self.kx) < k_max) &
                (np.abs(self.ky) < k_max) &
                (np.abs(self.kz) < k_max)
            ).astype(float)
        else:
            self.dealias_mask = np.ones_like(self.k_sq)

    def _spectral_derivative(self, f_hat: np.ndarray, direction: int) -> np.ndarray:
        """Compute spectral derivative in given direction (0=x, 1=y, 2=z)."""
        k = [self.kx, self.ky, self.kz][direction]
        return 1j * k * f_hat

    def _curl_spectral(self, vx_hat: np.ndarray, vy_hat: np.ndarray,
                       vz_hat: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Compute curl in spectral space: ω = ∇ × v."""
        omega_x = 1j * (self.ky * vz_hat - self.kz * vy_hat)
        omega_y = 1j * (self.kz * vx_hat - self.kx * vz_hat)
        omega_z = 1j * (self.kx * vy_hat - self.ky * vx_hat)
        return omega_x, omega_y, omega_z

    def _biot_savart(self, omega_x_hat: np.ndarray, omega_y_hat: np.ndarray,
                     omega_z_hat: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Recover velocity from vorticity via Biot-Savart.

        In spectral space: û = (ik × ω̂) / |k|²
        """
        # Cross product in spectral space: k × ω
        cross_x = 1j * (self.ky * omega_z_hat - self.kz * omega_y_hat)
        cross_y = 1j * (self.kz * omega_x_hat - self.kx * omega_z_hat)
        cross_z = 1j * (self.kx * omega_y_hat - self.ky * omega_x_hat)

        # Divide by |k|²
        u_hat = cross_x / self.k_sq
        v_hat = cross_y / self.k_sq
        w_hat = cross_z / self.k_sq

        # Zero mean (k=0 mode)
        u_hat[0, 0, 0] = 0
        v_hat[0, 0, 0] = 0
        w_hat[0, 0, 0] = 0

        return u_hat, v_hat, w_hat

    def _compute_rhs(self, omega: Tuple[np.ndarray, np.ndarray, np.ndarray],
                     omega_hat: Tuple[np.ndarray, np.ndarray, np.ndarray]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Compute RHS of vorticity equation.

        ∂ω/∂t = -(u·∇)ω + (ω·∇)u + ν∆ω
               = stretching + advection + viscous
        """
        omega_x, omega_y, omega_z = omega
        omega_x_hat, omega_y_hat, omega_z_hat = omega_hat

        # Recover velocity
        u_hat, v_hat, w_hat = self._biot_savart(omega_x_hat, omega_y_hat, omega_z_hat)

        # Transform to physical space
        u = np.real(ifftn(u_hat))
        v = np.real(ifftn(v_hat))
        w = np.real(ifftn(w_hat))

        # Compute velocity gradients in spectral space
        du_dx = np.real(ifftn(self._spectral_derivative(u_hat, 0)))
        du_dy = np.real(ifftn(self._spectral_derivative(u_hat, 1)))
        du_dz = np.real(ifftn(self._spectral_derivative(u_hat, 2)))
        dv_dx = np.real(ifftn(self._spectral_derivative(v_hat, 0)))
        dv_dy = np.real(ifftn(self._spectral_derivative(v_hat, 1)))
        dv_dz = np.real(ifftn(self._spectral_derivative(v_hat, 2)))
        dw_dx = np.real(ifftn(self._spectral_derivative(w_hat, 0)))
        dw_dy = np.real(ifftn(self._spectral_derivative(w_hat, 1)))
        dw_dz = np.real(ifftn(self._spectral_derivative(w_hat, 2)))

        # Compute vorticity gradients
        domega_x_dx = np.real(ifftn(self._spectral_derivative(omega_x_hat, 0)))
        domega_x_dy = np.real(ifftn(self._spectral_derivative(omega_x_hat, 1)))
        domega_x_dz = np.real(ifftn(self._spectral_derivative(omega_x_hat, 2)))
        domega_y_dx = np.real(ifftn(self._spectral_derivative(omega_y_hat, 0)))
        domega_y_dy = np.real(ifftn(self._spectral_derivative(omega_y_hat, 1)))
        domega_y_dz = np.real(ifftn(self._spectral_derivative(omega_y_hat, 2)))
        domega_z_dx = np.real(ifftn(self._spectral_derivative(omega_z_hat, 0)))
        domega_z_dy = np.real(ifftn(self._spectral_derivative(omega_z_hat, 1)))
        domega_z_dz = np.real(ifftn(self._spectral_derivative(omega_z_hat, 2)))

        # Advection: -(u·∇)ω
        advect_x = -(u * domega_x_dx + v * domega_x_dy + w * domega_x_dz)
        advect_y = -(u * domega_y_dx + v * domega_y_dy + w * domega_y_dz)
        advect_z = -(u * domega_z_dx + v * domega_z_dy + w * domega_z_dz)

        # Stretching: (ω·∇)u
        stretch_x = omega_x * du_dx + omega_y * du_dy + omega_z * du_dz
        stretch_y = omega_x * dv_dx + omega_y * dv_dy + omega_z * dv_dz
        stretch_z = omega_x * dw_dx + omega_y * dw_dy + omega_z * dw_dz

        # Nonlinear terms in physical space
        nl_x = advect_x + stretch_x
        nl_y = advect_y + stretch_y
        nl_z = advect_z + stretch_z

        # Transform to spectral and apply dealiasing
        nl_x_hat = fftn(nl_x) * self.dealias_mask
        nl_y_hat = fftn(nl_y) * self.dealias_mask
        nl_z_hat = fftn(nl_z) * self.dealias_mask

        # Viscous term: ν∆ω = -ν|k|²ω̂
        nu = self.config.nu
        visc_x = -nu * self.k_sq * omega_x_hat
        visc_y = -nu * self.k_sq * omega_y_hat
        visc_z = -nu * self.k_sq * omega_z_hat

        # Total RHS
        rhs_x = nl_x_hat + visc_x
        rhs_y = nl_y_hat + visc_y
        rhs_z = nl_z_hat + visc_z

        return rhs_x, rhs_y, rhs_z

    def _compute_dt(self, u: np.ndarray, v: np.ndarray, w: np.ndarray) -> float:
        """Compute adaptive timestep based on CFL condition."""
        u_max = max(np.max(np.abs(u)), np.max(np.abs(v)), np.max(np.abs(w)), 1e-10)

        # Advective CFL
        dt_adv = self.config.cfl * self.dx / u_max

        # Viscous stability (more restrictive at high resolution)
        dt_visc = 0.5 * self.dx**2 / self.config.nu

        return min(dt_adv, dt_visc)

    def step(self, omega_hat: Tuple[np.ndarray, np.ndarray, np.ndarray],
             dt: Optional[float] = None) -> Tuple[Tuple[np.ndarray, np.ndarray, np.ndarray], float]:
        """
        Advance vorticity by one timestep.

        Returns updated omega_hat and the dt used.
        """
        omega_x_hat, omega_y_hat, omega_z_hat = omega_hat

        # Get physical space vorticity
        omega_x = np.real(ifftn(omega_x_hat))
        omega_y = np.real(ifftn(omega_y_hat))
        omega_z = np.real(ifftn(omega_z_hat))
        omega = (omega_x, omega_y, omega_z)

        # Compute dt if not provided
        if dt is None:
            u_hat, v_hat, w_hat = self._biot_savart(omega_x_hat, omega_y_hat, omega_z_hat)
            u = np.real(ifftn(u_hat))
            v = np.real(ifftn(v_hat))
            w = np.real(ifftn(w_hat))
            dt = self._compute_dt(u, v, w)

        if self.config.integrator == 'euler':
            # Simple forward Euler
            rhs = self._compute_rhs(omega, omega_hat)
            omega_x_hat_new = omega_x_hat + dt * rhs[0]
            omega_y_hat_new = omega_y_hat + dt * rhs[1]
            omega_z_hat_new = omega_z_hat + dt * rhs[2]

        elif self.config.integrator == 'rk4':
            # Classical RK4
            k1 = self._compute_rhs(omega, omega_hat)

            # k2
            omega_hat_2 = (
                omega_x_hat + 0.5 * dt * k1[0],
                omega_y_hat + 0.5 * dt * k1[1],
                omega_z_hat + 0.5 * dt * k1[2]
            )
            omega_2 = tuple(np.real(ifftn(o)) for o in omega_hat_2)
            k2 = self._compute_rhs(omega_2, omega_hat_2)

            # k3
            omega_hat_3 = (
                omega_x_hat + 0.5 * dt * k2[0],
                omega_y_hat + 0.5 * dt * k2[1],
                omega_z_hat + 0.5 * dt * k2[2]
            )
            omega_3 = tuple(np.real(ifftn(o)) for o in omega_hat_3)
            k3 = self._compute_rhs(omega_3, omega_hat_3)

            # k4
            omega_hat_4 = (
                omega_x_hat + dt * k3[0],
                omega_y_hat + dt * k3[1],
                omega_z_hat + dt * k3[2]
            )
            omega_4 = tuple(np.real(ifftn(o)) for o in omega_hat_4)
            k4 = self._compute_rhs(omega_4, omega_hat_4)

            # Combine
            omega_x_hat_new = omega_x_hat + (dt / 6) * (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
            omega_y_hat_new = omega_y_hat + (dt / 6) * (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
            omega_z_hat_new = omega_z_hat + (dt / 6) * (k1[2] + 2*k2[2] + 2*k3[2] + k4[2])
        else:
            raise ValueError(f"Unknown integrator: {self.config.integrator}")

        return (omega_x_hat_new, omega_y_hat_new, omega_z_hat_new), dt

    def run(self, omega_hat_0: Tuple[np.ndarray, np.ndarray, np.ndarray],
            T_final: float,
            callback: Optional[callable] = None,
            save_interval: int = 10) -> Dict:
        """
        Run simulation from initial vorticity to final time.

        Args:
            omega_hat_0: Initial vorticity in spectral space
            T_final: Final simulation time
            callback: Optional function called each step with (t, omega_hat, u, diagnostics)
            save_interval: Save full state every N steps

        Returns:
            Dictionary with simulation results
        """
        omega_hat = omega_hat_0
        t = 0.0
        step_count = 0

        history = {
            'times': [0.0],
            'u_Linf': [],
            'omega_Linf': [],
            'energy': [],
            'enstrophy': [],
        }

        while t < T_final:
            # Compute velocity for diagnostics
            u_hat, v_hat, w_hat = self._biot_savart(*omega_hat)
            u = np.real(ifftn(u_hat))
            v = np.real(ifftn(v_hat))
            w = np.real(ifftn(w_hat))

            omega_x = np.real(ifftn(omega_hat[0]))
            omega_y = np.real(ifftn(omega_hat[1]))
            omega_z = np.real(ifftn(omega_hat[2]))

            # Compute diagnostics
            u_Linf = np.sqrt(np.max(u**2 + v**2 + w**2))
            omega_Linf = np.sqrt(np.max(omega_x**2 + omega_y**2 + omega_z**2))
            energy = 0.5 * np.mean(u**2 + v**2 + w**2) * self.config.L**3
            enstrophy = 0.5 * np.mean(omega_x**2 + omega_y**2 + omega_z**2) * self.config.L**3

            history['u_Linf'].append(u_Linf)
            history['omega_Linf'].append(omega_Linf)
            history['energy'].append(energy)
            history['enstrophy'].append(enstrophy)

            if callback is not None:
                callback(t, omega_hat, (u, v, w), {
                    'u_Linf': u_Linf,
                    'omega_Linf': omega_Linf,
                    'energy': energy,
                    'enstrophy': enstrophy
                })

            # Step forward
            omega_hat, dt = self.step(omega_hat)
            t += dt
            step_count += 1

            history['times'].append(t)

            # Check for blowup
            if u_Linf > 1e6 or np.isnan(u_Linf):
                print(f"Potential blowup detected at t = {t:.6f}")
                break

        return history

    def get_velocity(self, omega_hat: Tuple[np.ndarray, np.ndarray, np.ndarray]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Get velocity field from vorticity."""
        u_hat, v_hat, w_hat = self._biot_savart(*omega_hat)
        u = np.real(ifftn(u_hat))
        v = np.real(ifftn(v_hat))
        w = np.real(ifftn(w_hat))
        return u, v, w


def velocity_to_vorticity(u: np.ndarray, v: np.ndarray, w: np.ndarray,
                          L: float = 2*np.pi) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Convert velocity field to vorticity in spectral space."""
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

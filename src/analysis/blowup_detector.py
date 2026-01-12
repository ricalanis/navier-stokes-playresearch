"""
Blowup detection and monitoring for Navier-Stokes simulations.

Tracks key quantities that signal potential singularity formation:
- ||u||_∞, ||ω||_∞ (L^∞ norms)
- Energy, enstrophy
- Dissipation rate
- BKM integral
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class BlowupDiagnostics:
    """Container for blowup diagnostic quantities."""
    time: float
    u_Linf: float           # ||u||_∞
    omega_Linf: float       # ||ω||_∞
    u_L3: float             # ||u||_{L³}
    energy: float           # ||u||²_{L²} / 2
    enstrophy: float        # ||ω||²_{L²} / 2
    dissipation: float      # ν||∇u||²_{L²}
    palinstrophy: float     # ||∇ω||²_{L²}

    # Location of maximum vorticity
    omega_max_loc: Tuple[int, int, int] = (0, 0, 0)


class BlowupDetector:
    """
    Monitor Navier-Stokes solutions for potential blowup.

    Computes and tracks diagnostic quantities that indicate
    singularity formation according to known criteria:
    - BKM: ∫||ω||_∞ dt = ∞ ⟺ blowup
    - ESS: ||u||_{L³} → ∞ ⟺ blowup
    """

    def __init__(self, nu: float = 0.01, L: float = 2*np.pi):
        """
        Args:
            nu: Kinematic viscosity
            L: Domain size
        """
        self.nu = nu
        self.L = L
        self.history: List[BlowupDiagnostics] = []

        # BKM integral tracking
        self.bkm_integral = 0.0
        self.last_time = 0.0

    def compute_diagnostics(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                            omega_x: np.ndarray, omega_y: np.ndarray, omega_z: np.ndarray,
                            t: float) -> BlowupDiagnostics:
        """
        Compute all diagnostic quantities from velocity and vorticity fields.

        Args:
            u, v, w: Velocity components
            omega_x, omega_y, omega_z: Vorticity components
            t: Current time

        Returns:
            BlowupDiagnostics object with all computed quantities
        """
        N = u.shape[0]
        dx = self.L / N

        # Compute norms
        u_mag = np.sqrt(u**2 + v**2 + w**2)
        omega_mag = np.sqrt(omega_x**2 + omega_y**2 + omega_z**2)

        u_Linf = np.max(u_mag)
        omega_Linf = np.max(omega_mag)

        # L³ norm (critical for ESS)
        u_L3 = (np.mean(u_mag**3) * self.L**3)**(1/3)

        # Energy and enstrophy
        energy = 0.5 * np.mean(u_mag**2) * self.L**3
        enstrophy = 0.5 * np.mean(omega_mag**2) * self.L**3

        # Compute gradients for dissipation
        k = fftfreq(N, d=self.L/(2*np.pi*N))
        kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')

        # Velocity gradients via spectral differentiation
        u_hat = fftn(u)
        v_hat = fftn(v)
        w_hat = fftn(w)

        grad_u_sq = 0.0
        for vel_hat in [u_hat, v_hat, w_hat]:
            for ki in [kx, ky, kz]:
                deriv = np.real(ifftn(1j * ki * vel_hat))
                grad_u_sq += np.mean(deriv**2)

        dissipation = self.nu * grad_u_sq * self.L**3

        # Vorticity gradients for palinstrophy
        omega_x_hat = fftn(omega_x)
        omega_y_hat = fftn(omega_y)
        omega_z_hat = fftn(omega_z)

        grad_omega_sq = 0.0
        for omega_hat in [omega_x_hat, omega_y_hat, omega_z_hat]:
            for ki in [kx, ky, kz]:
                deriv = np.real(ifftn(1j * ki * omega_hat))
                grad_omega_sq += np.mean(deriv**2)

        palinstrophy = grad_omega_sq * self.L**3

        # Location of maximum vorticity
        idx = np.unravel_index(np.argmax(omega_mag), omega_mag.shape)

        return BlowupDiagnostics(
            time=t,
            u_Linf=u_Linf,
            omega_Linf=omega_Linf,
            u_L3=u_L3,
            energy=energy,
            enstrophy=enstrophy,
            dissipation=dissipation,
            palinstrophy=palinstrophy,
            omega_max_loc=idx
        )

    def update(self, diagnostics: BlowupDiagnostics):
        """Update history and BKM integral with new diagnostics."""
        # Update BKM integral: ∫||ω||_∞ dt
        if len(self.history) > 0:
            dt = diagnostics.time - self.last_time
            # Trapezoidal rule
            self.bkm_integral += 0.5 * (diagnostics.omega_Linf + self.history[-1].omega_Linf) * dt

        self.last_time = diagnostics.time
        self.history.append(diagnostics)

    def check_blowup_criteria(self) -> Dict[str, bool]:
        """
        Check various blowup criteria against current state.

        Returns dict indicating which criteria suggest blowup.
        """
        if len(self.history) < 2:
            return {'bkm_warning': False, 'ess_warning': False, 'numerical_blowup': False}

        current = self.history[-1]
        prev = self.history[-2]

        # Check for rapid growth (numerical blowup indicator)
        if prev.u_Linf > 0:
            growth_rate = current.u_Linf / prev.u_Linf
        else:
            growth_rate = 1.0

        return {
            'bkm_warning': self.bkm_integral > 100,  # Large BKM integral
            'ess_warning': current.u_L3 > 1000,      # Large L³ norm
            'numerical_blowup': growth_rate > 10 or np.isnan(current.u_Linf),
            'omega_explosive': current.omega_Linf > 1e6
        }

    def get_history_arrays(self) -> Dict[str, np.ndarray]:
        """Return history as numpy arrays for analysis."""
        if len(self.history) == 0:
            return {}

        return {
            'times': np.array([d.time for d in self.history]),
            'u_Linf': np.array([d.u_Linf for d in self.history]),
            'omega_Linf': np.array([d.omega_Linf for d in self.history]),
            'u_L3': np.array([d.u_L3 for d in self.history]),
            'energy': np.array([d.energy for d in self.history]),
            'enstrophy': np.array([d.enstrophy for d in self.history]),
            'dissipation': np.array([d.dissipation for d in self.history]),
            'palinstrophy': np.array([d.palinstrophy for d in self.history]),
        }

    def estimate_blowup_rate(self, T_star: Optional[float] = None) -> Tuple[float, float]:
        """
        Estimate the blowup rate α from ||u||_∞ ~ (T-t)^{-α}.

        Returns (alpha, T_star) where T_star is estimated if not provided.
        """
        history = self.get_history_arrays()
        if len(history) == 0:
            return (0.5, np.inf)

        times = history['times']
        u_Linf = history['u_Linf']

        from .rate_tracker import RateTracker
        tracker = RateTracker()
        return tracker.fit_blowup_rate(times, u_Linf, T_star)

    def summary(self) -> str:
        """Return a summary string of the current state."""
        if len(self.history) == 0:
            return "No data recorded yet."

        current = self.history[-1]
        criteria = self.check_blowup_criteria()

        lines = [
            f"Time: {current.time:.6f}",
            f"||u||_∞ = {current.u_Linf:.6e}",
            f"||ω||_∞ = {current.omega_Linf:.6e}",
            f"||u||_L³ = {current.u_L3:.6e}",
            f"Energy = {current.energy:.6e}",
            f"Enstrophy = {current.enstrophy:.6e}",
            f"BKM integral = {self.bkm_integral:.6e}",
            f"Blowup warnings: {criteria}",
        ]
        return "\n".join(lines)

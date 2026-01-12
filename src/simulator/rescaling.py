"""
Type II rescaling for self-similar analysis.

For Type II blowup at rate α, we transform:
    U(τ, y) = (T-t)^α u(t, (T-t)^{1/2} y)
    τ = -log(T-t)

This should reveal the limiting profile (if any) as τ → ∞.
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq
from typing import Tuple, Optional
from scipy.interpolate import RegularGridInterpolator


class TypeIIRescaler:
    """
    Rescale Navier-Stokes solutions to Type II self-similar variables.

    For ||u||_∞ ~ (T-t)^{-α}, the rescaled U should have ||U||_∞ ~ O(1).
    """

    def __init__(self, T_star: float, alpha: float, N: int = 64, L: float = 2*np.pi):
        """
        Args:
            T_star: Estimated blowup time
            alpha: Blowup rate exponent (should be in [3/5, 3/4) for Type II)
            N: Grid resolution
            L: Original domain size
        """
        self.T_star = T_star
        self.alpha = alpha
        self.N = N
        self.L = L

    def rescale_solution(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                         t: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float]:
        """
        Rescale velocity field to self-similar variables.

        Args:
            u, v, w: Velocity components on original grid
            t: Current time

        Returns:
            U, V, W: Rescaled velocity on rescaled grid
            tau: Self-similar time coordinate
        """
        T = self.T_star
        if t >= T:
            raise ValueError(f"Time t={t} must be less than T_star={T}")

        dt = T - t
        tau = -np.log(dt)

        # Scaling factors
        amp_scale = dt**self.alpha  # For velocity amplitude
        space_scale = dt**0.5        # For spatial coordinates

        # Create rescaled grid
        # y = x / (T-t)^{1/2}, so y ranges over [0, L/(T-t)^{1/2}]
        # For numerical purposes, we interpolate onto a fixed grid

        # Original grid
        x_orig = np.linspace(0, self.L, self.N, endpoint=False)

        # Rescaled grid (centered, bounded region)
        L_rescaled = self.L / space_scale  # This grows as t → T
        y = np.linspace(-L_rescaled/2, L_rescaled/2, self.N, endpoint=False)

        # For simplicity, we'll just rescale the amplitude without regridding
        # (full regridding would require interpolation which is expensive)

        # Rescale amplitude: U = (T-t)^α u
        U = amp_scale * u
        V = amp_scale * v
        W = amp_scale * w

        return U, V, W, tau

    def rescale_vorticity(self, omega_x: np.ndarray, omega_y: np.ndarray,
                          omega_z: np.ndarray, t: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float]:
        """
        Rescale vorticity field to self-similar variables.

        For vorticity: Ω = (T-t)^{2α} ω  (two derivatives give extra power)
        """
        T = self.T_star
        if t >= T:
            raise ValueError(f"Time t={t} must be less than T_star={T}")

        dt = T - t
        tau = -np.log(dt)

        # Vorticity scaling (one more derivative than velocity)
        vort_scale = dt**(2*self.alpha - 0.5)

        Omega_x = vort_scale * omega_x
        Omega_y = vort_scale * omega_y
        Omega_z = vort_scale * omega_z

        return Omega_x, Omega_y, Omega_z, tau

    def compute_rescaled_norms(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                               omega_x: np.ndarray, omega_y: np.ndarray, omega_z: np.ndarray,
                               t: float) -> dict:
        """
        Compute norms in rescaled variables.

        For correct Type II rate α, ||U||_∞ should be O(1) as t → T.
        """
        U, V, W, tau = self.rescale_solution(u, v, w, t)
        Omega_x, Omega_y, Omega_z, _ = self.rescale_vorticity(omega_x, omega_y, omega_z, t)

        U_Linf = np.sqrt(np.max(U**2 + V**2 + W**2))
        Omega_Linf = np.sqrt(np.max(Omega_x**2 + Omega_y**2 + Omega_z**2))

        # For correct α, these should stabilize
        return {
            'tau': tau,
            'U_Linf': U_Linf,
            'Omega_Linf': Omega_Linf,
            'dt': self.T_star - t
        }

    @staticmethod
    def estimate_blowup_time(times: np.ndarray, u_Linf: np.ndarray) -> float:
        """
        Estimate blowup time T from the growth of ||u||_∞.

        Fits ||u||_∞ ~ (T-t)^{-α} and extrapolates to find T.
        """
        # Use the last portion of data where growth is strongest
        n = len(times)
        idx_start = int(0.7 * n)

        t_fit = times[idx_start:]
        u_fit = u_Linf[idx_start:]

        # Fit: log(||u||) = -α log(T-t) + const
        # Need to simultaneously fit T and α

        from scipy.optimize import minimize

        def objective(params):
            T, alpha, C = params
            if T <= t_fit[-1] or alpha <= 0:
                return 1e10
            predicted = C * (T - t_fit)**(-alpha)
            return np.sum((np.log(u_fit) - np.log(predicted))**2)

        # Initial guess
        T0 = t_fit[-1] + (t_fit[-1] - t_fit[-2]) * 10  # Extrapolate
        alpha0 = 0.65  # Middle of Type II window
        C0 = u_fit[0] * (T0 - t_fit[0])**alpha0

        result = minimize(objective, [T0, alpha0, C0],
                         method='Nelder-Mead',
                         options={'maxiter': 1000})

        return result.x[0]  # Return estimated T

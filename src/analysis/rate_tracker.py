"""
Rate tracker for Type II blowup analysis.

Fits the blowup rate α from ||u||_∞ ~ (T-t)^{-α} and tracks
whether α falls within the open window [3/5, 3/4).
"""

import numpy as np
from scipy.optimize import minimize, curve_fit
from typing import Tuple, Optional, List
from dataclasses import dataclass


# Type II window bounds
ALPHA_LOWER = 3/5   # 0.6
ALPHA_UPPER = 3/4   # 0.75


@dataclass
class RateFitResult:
    """Results from blowup rate fitting."""
    T_star: float           # Estimated blowup time
    alpha: float            # Fitted rate exponent
    C: float                # Amplitude constant
    residual: float         # Fit residual
    in_type_ii_window: bool # α ∈ [3/5, 3/4)?
    confidence: float       # Confidence in the fit (0-1)


class RateTracker:
    """
    Track and fit the blowup rate parameter α.

    For Type II blowup: ||u||_∞ ~ (T-t)^{-α} with α ∈ [3/5, 3/4).
    """

    def __init__(self):
        self.fit_history: List[RateFitResult] = []

    def fit_blowup_rate(self, times: np.ndarray, u_Linf: np.ndarray,
                        T_star: Optional[float] = None,
                        fit_fraction: float = 0.3) -> Tuple[float, float]:
        """
        Fit the blowup rate α from time series of ||u||_∞.

        Args:
            times: Array of time values
            u_Linf: Array of ||u||_∞ values
            T_star: Known or estimated blowup time (if None, will be fitted)
            fit_fraction: Fraction of later data to use for fitting

        Returns:
            (alpha, T_star) tuple
        """
        n = len(times)
        n_u = len(u_Linf)

        # Ensure arrays have same length
        min_len = min(n, n_u)
        times = times[:min_len]
        u_Linf = u_Linf[:min_len]
        n = min_len

        if n < 5:
            return (0.5, np.inf)

        # Use later portion where blowup behavior is clearer
        idx_start = max(0, int((1 - fit_fraction) * n))
        t_fit = times[idx_start:]
        u_fit = u_Linf[idx_start:]

        # Filter out any NaN or inf values
        valid = np.isfinite(u_fit) & (u_fit > 0)
        t_fit = t_fit[valid]
        u_fit = u_fit[valid]

        if len(t_fit) < 3:
            return (0.5, np.inf)

        if T_star is None:
            # Fit T_star, alpha, and C simultaneously
            result = self._fit_full(t_fit, u_fit)
        else:
            # Fit only alpha and C with known T_star
            result = self._fit_with_known_T(t_fit, u_fit, T_star)

        self.fit_history.append(result)
        return (result.alpha, result.T_star)

    def _fit_full(self, times: np.ndarray, u_Linf: np.ndarray) -> RateFitResult:
        """Fit T_star, alpha, and C simultaneously."""

        def model(t, T, alpha, C):
            dt = np.maximum(T - t, 1e-10)
            return C * dt**(-alpha)

        def objective(params):
            T, alpha, C = params
            if T <= times[-1] or alpha <= 0 or alpha > 2 or C <= 0:
                return 1e20

            try:
                pred = model(times, T, alpha, C)
                # Log-space residual for better scaling
                residual = np.sum((np.log(u_Linf) - np.log(pred))**2)
                return residual
            except:
                return 1e20

        # Initial guesses
        # Extrapolate T from the last few points
        dt_last = times[-1] - times[-2]
        T0 = times[-1] + dt_last * 5

        # Estimate alpha from log-log slope
        if len(times) >= 3:
            log_t_to_end = np.log(T0 - times[-3:])
            log_u = np.log(u_Linf[-3:])
            alpha0 = -np.polyfit(log_t_to_end, log_u, 1)[0]
            alpha0 = np.clip(alpha0, 0.4, 1.0)
        else:
            alpha0 = 0.65

        C0 = u_Linf[0] * (T0 - times[0])**alpha0

        # Optimize
        result = minimize(objective, [T0, alpha0, C0],
                         method='Nelder-Mead',
                         options={'maxiter': 2000, 'xatol': 1e-8})

        T_star, alpha, C = result.x

        # Compute confidence based on residual
        pred = model(times, T_star, alpha, C)
        residual = np.sqrt(np.mean((np.log(u_Linf) - np.log(pred))**2))
        confidence = np.exp(-residual)  # Rough measure

        return RateFitResult(
            T_star=T_star,
            alpha=alpha,
            C=C,
            residual=residual,
            in_type_ii_window=(ALPHA_LOWER <= alpha < ALPHA_UPPER),
            confidence=confidence
        )

    def _fit_with_known_T(self, times: np.ndarray, u_Linf: np.ndarray,
                          T_star: float) -> RateFitResult:
        """Fit alpha and C with known T_star."""

        # Transform to linear regression in log-log space
        # log(||u||) = -α log(T-t) + log(C)
        dt = T_star - times
        valid = dt > 0
        if not np.any(valid):
            return RateFitResult(T_star, 0.5, 1.0, np.inf, False, 0.0)

        log_dt = np.log(dt[valid])
        log_u = np.log(u_Linf[valid])

        # Linear regression
        coeffs = np.polyfit(log_dt, log_u, 1)
        alpha = -coeffs[0]
        C = np.exp(coeffs[1])

        # Residual
        pred = C * dt[valid]**(-alpha)
        residual = np.sqrt(np.mean((np.log(u_Linf[valid]) - np.log(pred))**2))
        confidence = np.exp(-residual)

        return RateFitResult(
            T_star=T_star,
            alpha=alpha,
            C=C,
            residual=residual,
            in_type_ii_window=(ALPHA_LOWER <= alpha < ALPHA_UPPER),
            confidence=confidence
        )

    def is_in_type_ii_window(self, alpha: float) -> bool:
        """Check if rate α is in the Type II window [3/5, 3/4)."""
        return ALPHA_LOWER <= alpha < ALPHA_UPPER

    def classify_blowup(self, alpha: float) -> str:
        """
        Classify the type of blowup based on rate α.

        Returns:
            'Type I' if α = 1/2 (self-similar)
            'Type II low' if 1/2 < α < 3/5 (ruled out by BKM)
            'Type II window' if 3/5 ≤ α < 3/4 (the open window)
            'Type II high' if α ≥ 3/4 (ruled out by dissipation)
            'subcritical' if α < 1/2 (not blowup)
        """
        if alpha < 0.5:
            return 'subcritical'
        elif abs(alpha - 0.5) < 0.01:
            return 'Type I'
        elif 0.5 < alpha < ALPHA_LOWER:
            return 'Type II low (BKM ruled out)'
        elif ALPHA_LOWER <= alpha < ALPHA_UPPER:
            return 'Type II window [3/5, 3/4)'
        else:
            return 'Type II high (dissipation ruled out)'

    def track_rate_evolution(self, times: np.ndarray, u_Linf: np.ndarray,
                             window_size: int = 20) -> Tuple[np.ndarray, np.ndarray]:
        """
        Track how the fitted rate α evolves as we get more data.

        Returns arrays of times and corresponding fitted α values.
        """
        n = len(times)
        if n < window_size:
            return np.array([]), np.array([])

        alpha_values = []
        fit_times = []

        for i in range(window_size, n):
            t_window = times[:i]
            u_window = u_Linf[:i]

            alpha, T = self.fit_blowup_rate(t_window, u_window)
            alpha_values.append(alpha)
            fit_times.append(times[i-1])

        return np.array(fit_times), np.array(alpha_values)

    def summary(self) -> str:
        """Return summary of latest fit."""
        if len(self.fit_history) == 0:
            return "No fits performed yet."

        latest = self.fit_history[-1]
        classification = self.classify_blowup(latest.alpha)

        lines = [
            f"Latest fit results:",
            f"  T* = {latest.T_star:.6f}",
            f"  α = {latest.alpha:.4f}",
            f"  C = {latest.C:.4e}",
            f"  Residual = {latest.residual:.4e}",
            f"  Confidence = {latest.confidence:.2%}",
            f"  Classification: {classification}",
            f"  In Type II window: {latest.in_type_ii_window}",
        ]
        return "\n".join(lines)

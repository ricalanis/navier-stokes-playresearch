"""
Visualization tools for Type II blowup analysis.

Provides plotting functions for:
- Rate evolution α(t) with Type II window highlighted
- Diagnostic time series
- Phase portraits
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from typing import Optional, Dict, List, Tuple
import warnings


# Type II window bounds
ALPHA_LOWER = 3/5   # 0.6
ALPHA_UPPER = 3/4   # 0.75


class TypeIIVisualizer:
    """
    Visualization tools for Type II blowup analysis.
    """

    def __init__(self, figsize: Tuple[int, int] = (10, 6)):
        self.figsize = figsize
        plt.style.use('seaborn-v0_8-whitegrid')

    def plot_rate_evolution(self, times: np.ndarray, alphas: np.ndarray,
                            T_star: Optional[float] = None,
                            ax: Optional[plt.Axes] = None,
                            title: str = "Blowup Rate Evolution") -> plt.Figure:
        """
        Plot the evolution of fitted rate α(t) with Type II window highlighted.

        Args:
            times: Time values
            alphas: Fitted α values at each time
            T_star: Estimated blowup time (optional, shown as vertical line)
            ax: Existing axes (creates new figure if None)
            title: Plot title

        Returns:
            matplotlib Figure
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=self.figsize)
        else:
            fig = ax.figure

        # Highlight Type II window
        ax.axhspan(ALPHA_LOWER, ALPHA_UPPER, alpha=0.2, color='red',
                  label=f'Type II window [{ALPHA_LOWER:.2f}, {ALPHA_UPPER:.2f})')

        # Reference lines
        ax.axhline(y=0.5, color='blue', linestyle='--', alpha=0.5,
                  label='Self-similar (α = 1/2)')
        ax.axhline(y=ALPHA_LOWER, color='orange', linestyle=':', alpha=0.7,
                  label=f'BKM bound (α = {ALPHA_LOWER})')
        ax.axhline(y=ALPHA_UPPER, color='purple', linestyle=':', alpha=0.7,
                  label=f'Dissipation bound (α = {ALPHA_UPPER})')

        # Plot rate evolution
        ax.plot(times, alphas, 'b-', linewidth=2, label='Fitted α(t)')

        # Mark if in window
        in_window = (alphas >= ALPHA_LOWER) & (alphas < ALPHA_UPPER)
        if np.any(in_window):
            ax.scatter(times[in_window], alphas[in_window], c='red', s=50,
                      zorder=5, label='In Type II window')

        if T_star is not None:
            ax.axvline(x=T_star, color='red', linestyle='--', alpha=0.7,
                      label=f'T* = {T_star:.4f}')

        ax.set_xlabel('Time t', fontsize=12)
        ax.set_ylabel('Blowup rate α', fontsize=12)
        ax.set_title(title, fontsize=14)
        ax.legend(loc='best', fontsize=10)
        ax.set_ylim(0.3, 1.0)

        plt.tight_layout()
        return fig

    def plot_diagnostics(self, history: Dict[str, np.ndarray],
                         figsize: Optional[Tuple[int, int]] = None) -> plt.Figure:
        """
        Plot diagnostic time series on multiple subplots.

        Args:
            history: Dictionary with keys 'times', 'u_Linf', 'omega_Linf',
                     'energy', 'enstrophy', 'dissipation'
        """
        if figsize is None:
            figsize = (12, 10)

        fig, axes = plt.subplots(2, 3, figsize=figsize)
        axes = axes.flatten()

        times = history.get('times', np.array([]))

        # ||u||_∞
        ax = axes[0]
        if 'u_Linf' in history:
            ax.semilogy(times, history['u_Linf'], 'b-', linewidth=1.5)
        ax.set_xlabel('Time')
        ax.set_ylabel('||u||_∞')
        ax.set_title('Velocity L∞ norm')

        # ||ω||_∞
        ax = axes[1]
        if 'omega_Linf' in history:
            ax.semilogy(times, history['omega_Linf'], 'r-', linewidth=1.5)
        ax.set_xlabel('Time')
        ax.set_ylabel('||ω||_∞')
        ax.set_title('Vorticity L∞ norm')

        # ||u||_{L³}
        ax = axes[2]
        if 'u_L3' in history:
            ax.semilogy(times, history['u_L3'], 'g-', linewidth=1.5)
        ax.set_xlabel('Time')
        ax.set_ylabel('||u||_L³')
        ax.set_title('Velocity L³ norm (ESS criterion)')

        # Energy
        ax = axes[3]
        if 'energy' in history:
            ax.plot(times, history['energy'], 'b-', linewidth=1.5)
        ax.set_xlabel('Time')
        ax.set_ylabel('Energy')
        ax.set_title('Kinetic Energy')

        # Enstrophy
        ax = axes[4]
        if 'enstrophy' in history:
            ax.semilogy(times, history['enstrophy'], 'r-', linewidth=1.5)
        ax.set_xlabel('Time')
        ax.set_ylabel('Enstrophy')
        ax.set_title('Enstrophy ||ω||²_L²')

        # Dissipation
        ax = axes[5]
        if 'dissipation' in history:
            ax.semilogy(times, history['dissipation'], 'm-', linewidth=1.5)
        ax.set_xlabel('Time')
        ax.set_ylabel('Dissipation')
        ax.set_title('Energy Dissipation')

        plt.tight_layout()
        return fig

    def plot_phase_portrait(self, u_Linf: np.ndarray, omega_Linf: np.ndarray,
                            times: Optional[np.ndarray] = None,
                            ax: Optional[plt.Axes] = None) -> plt.Figure:
        """
        Plot phase portrait (||u||_∞, ||ω||_∞) with time coloring.

        This shows the trajectory in the space of critical norms.
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=self.figsize)
        else:
            fig = ax.figure

        if times is not None:
            # Color by time
            scatter = ax.scatter(u_Linf, omega_Linf, c=times, cmap='viridis',
                               s=10, alpha=0.7)
            plt.colorbar(scatter, ax=ax, label='Time')
        else:
            ax.plot(u_Linf, omega_Linf, 'b-', linewidth=1, alpha=0.7)
            ax.scatter(u_Linf[0], omega_Linf[0], c='green', s=100,
                      marker='o', label='Start', zorder=5)
            ax.scatter(u_Linf[-1], omega_Linf[-1], c='red', s=100,
                      marker='x', label='End', zorder=5)

        ax.set_xlabel('||u||_∞', fontsize=12)
        ax.set_ylabel('||ω||_∞', fontsize=12)
        ax.set_title('Phase Portrait: Velocity vs Vorticity', fontsize=14)
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.legend()

        plt.tight_layout()
        return fig

    def plot_blowup_fit(self, times: np.ndarray, u_Linf: np.ndarray,
                        T_star: float, alpha: float, C: float,
                        ax: Optional[plt.Axes] = None) -> plt.Figure:
        """
        Plot ||u||_∞ data with fitted blowup curve.

        Shows how well the fit ||u||_∞ ~ C(T*-t)^{-α} matches the data.
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=self.figsize)
        else:
            fig = ax.figure

        # Data
        ax.semilogy(times, u_Linf, 'b.', markersize=3, alpha=0.5, label='Data')

        # Fit
        t_fit = np.linspace(times[0], min(times[-1], T_star - 0.001), 200)
        u_fit = C * (T_star - t_fit)**(-alpha)
        ax.semilogy(t_fit, u_fit, 'r-', linewidth=2,
                   label=f'Fit: C(T*-t)^{{-α}}, α={alpha:.3f}')

        # Blowup time
        ax.axvline(x=T_star, color='red', linestyle='--', alpha=0.7,
                  label=f'T* = {T_star:.4f}')

        # Classification
        if ALPHA_LOWER <= alpha < ALPHA_UPPER:
            status = "IN TYPE II WINDOW"
            status_color = 'red'
        else:
            status = "outside Type II window"
            status_color = 'gray'

        ax.text(0.05, 0.95, status, transform=ax.transAxes,
               fontsize=12, verticalalignment='top',
               color=status_color, fontweight='bold')

        ax.set_xlabel('Time t', fontsize=12)
        ax.set_ylabel('||u||_∞', fontsize=12)
        ax.set_title('Blowup Rate Fitting', fontsize=14)
        ax.legend(loc='lower right')

        plt.tight_layout()
        return fig

    def plot_rescaled_norms(self, taus: np.ndarray, U_Linf: np.ndarray,
                            Omega_Linf: np.ndarray,
                            ax: Optional[plt.Axes] = None) -> plt.Figure:
        """
        Plot rescaled norms ||U||_∞ and ||Ω||_∞ vs τ.

        For correct Type II rate α, these should stabilize as τ → ∞.
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=self.figsize)
        else:
            fig = ax.figure

        ax.plot(taus, U_Linf, 'b-', linewidth=2, label='||U||_∞ (rescaled velocity)')
        ax.plot(taus, Omega_Linf, 'r-', linewidth=2, label='||Ω||_∞ (rescaled vorticity)')

        ax.set_xlabel('τ = -log(T*-t)', fontsize=12)
        ax.set_ylabel('Rescaled norm', fontsize=12)
        ax.set_title('Rescaled Norms (should stabilize for correct α)', fontsize=14)
        ax.legend()

        # Add reference for O(1) behavior
        ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5)

        plt.tight_layout()
        return fig

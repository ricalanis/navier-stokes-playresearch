#!/usr/bin/env python3
"""
Track Seregin's condition (1.4) during Navier-Stokes evolution.

This script runs the spectral NS solver and monitors the weighted norms
A_{m₁}, E_m, D_m for multiple values of m ∈ (1/2, 3/5).

Usage:
    python scripts/track_seregin_condition.py --ic taylor_green --nu 0.001 --T 5.0
"""

import argparse
import numpy as np
import json
from pathlib import Path
from datetime import datetime
from numpy.fft import ifftn

# Add parent directory to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.simulator.spectral_ns import SpectralNSSolver, SolverConfig
from src.simulator.initial_conditions import (
    taylor_green, anti_parallel_vortex_tubes, hou_luo_candidate
)
from src.analysis.seregin_condition import SereginConditionChecker, Condition14Result


def create_initial_condition(ic_name: str, N: int, L: float) -> tuple:
    """Create initial condition by name. Returns spectral vorticity tuple."""
    if ic_name == 'taylor_green':
        return taylor_green(N, L, amplitude=1.0)
    elif ic_name == 'anti_parallel':
        return anti_parallel_vortex_tubes(N, L, amplitude=5.0)
    elif ic_name == 'hou_luo':
        return hou_luo_candidate(N, L)
    else:
        raise ValueError(f"Unknown initial condition: {ic_name}")


class SereginTracker:
    """Track Seregin condition (1.4) during simulation."""

    def __init__(self, L: float, nu: float, m_values: np.ndarray = None,
                 output_dir: str = None):
        """
        Args:
            L: Domain size
            nu: Viscosity
            m_values: Array of m values to track
            output_dir: Directory for output files
        """
        self.L = L
        self.nu = nu
        self.m_values = m_values if m_values is not None else np.linspace(0.51, 0.59, 5)

        self.checker = SereginConditionChecker(L=L, nu=nu)

        # Results storage
        self.times = []
        self.results_by_m = {m: [] for m in self.m_values}
        self.diagnostics = []  # Standard diagnostics (energy, enstrophy, etc)

        # Output directory
        if output_dir is None:
            output_dir = Path(__file__).parent.parent / 'results' / 'seregin_tracking'
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def record(self, t: float, omega_hat: tuple, u: np.ndarray, v: np.ndarray,
               w: np.ndarray, diag: dict):
        """
        Record diagnostics at current time.

        Args:
            t: Current time
            omega_hat: Vorticity in spectral space (tuple)
            u, v, w: Velocity components in physical space
            diag: Standard diagnostics dict from solver
        """
        self.times.append(t)
        self.diagnostics.append(diag.copy())

        # Seregin condition for each m
        for m in self.m_values:
            result = self.checker.check_condition_14(u, v, w, m)
            self.results_by_m[m].append(result)

        # Print progress
        if len(self.times) % 10 == 0 or len(self.times) == 1:
            print(f"t = {t:.4f}, ||u||_∞ = {diag['u_Linf']:.4e}, "
                  f"E = {diag['energy']:.4e}")
            for m in self.m_values[:2]:  # Print first two m values
                r = self.results_by_m[m][-1]
                print(f"  m={m:.2f}: sup = {r.sup_total:.4e}")

    def get_summary(self) -> dict:
        """Get summary of tracking results."""
        summary = {
            'times': np.array(self.times).tolist(),
            'n_steps': len(self.times),
            'm_values': list(self.m_values),
            'results_by_m': {},
            'diagnostics': {
                'u_Linf': [d['u_Linf'] for d in self.diagnostics],
                'omega_Linf': [d['omega_Linf'] for d in self.diagnostics],
                'energy': [d['energy'] for d in self.diagnostics],
                'enstrophy': [d['enstrophy'] for d in self.diagnostics]
            }
        }

        for m in self.m_values:
            results = self.results_by_m[m]
            if results:
                summary['results_by_m'][str(m)] = {
                    'sup_total': [float(r.sup_total) for r in results],
                    'sup_A_m1': [float(r.sup_A_m1) for r in results],
                    'sup_E_m': [float(r.sup_E_m) for r in results],
                    'sup_D_m': [float(r.sup_D_m) for r in results],
                    'r_max': [float(r.r_max) for r in results],
                    'is_bounded': [bool(r.is_bounded) for r in results]
                }

        return summary

    def save_results(self, filename: str = None):
        """Save results to JSON file."""
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'seregin_tracking_{timestamp}.json'

        filepath = self.output_dir / filename

        summary = self.get_summary()

        with open(filepath, 'w') as f:
            json.dump(summary, f, indent=2)

        print(f"Results saved to {filepath}")
        return filepath

    def print_final_summary(self):
        """Print final summary of condition (1.4) status."""
        print("\n" + "=" * 60)
        print("SEREGIN CONDITION (1.4) FINAL ANALYSIS")
        print("=" * 60)

        for m in self.m_values:
            results = self.results_by_m[m]
            if not results:
                continue

            final = results[-1]
            max_sup = max(r.sup_total for r in results)
            min_sup = min(r.sup_total for r in results)

            print(f"\nm = {m:.3f} (m₁ = {2*m-1:.3f}):")
            print(f"  Final sup_total: {final.sup_total:.4e}")
            print(f"  Max sup_total:   {max_sup:.4e}")
            print(f"  Min sup_total:   {min_sup:.4e}")
            print(f"  Final breakdown:")
            print(f"    A_m1: {final.sup_A_m1:.4e}")
            print(f"    E_m:  {final.sup_E_m:.4e}")
            print(f"    D_m:  {final.sup_D_m:.4e}")

            # Trend analysis
            if len(results) > 5:
                early_avg = np.mean([r.sup_total for r in results[:5]])
                late_avg = np.mean([r.sup_total for r in results[-5:]])
                if late_avg > 2 * early_avg:
                    print(f"  Trend: GROWING (factor {late_avg/early_avg:.2f}x)")
                elif late_avg < 0.5 * early_avg:
                    print(f"  Trend: DECAYING (factor {late_avg/early_avg:.2f}x)")
                else:
                    print(f"  Trend: STABLE")

        # Overall conclusion
        print("\n" + "-" * 60)
        all_bounded = all(
            all(r.is_bounded for r in results)
            for results in self.results_by_m.values()
            if results
        )

        if all_bounded:
            print("CONCLUSION: Condition (1.4) appears SATISFIED throughout")
            print("→ Evidence supports Type II exclusion for tested m range")
        else:
            print("CONCLUSION: Condition (1.4) shows potential VIOLATION")
            print("→ Further investigation needed")


def main():
    parser = argparse.ArgumentParser(description='Track Seregin condition (1.4)')
    parser.add_argument('--ic', type=str, default='taylor_green',
                        choices=['taylor_green', 'anti_parallel', 'hou_luo'],
                        help='Initial condition type')
    parser.add_argument('--N', type=int, default=64, help='Grid resolution')
    parser.add_argument('--nu', type=float, default=0.001, help='Viscosity')
    parser.add_argument('--T', type=float, default=5.0, help='Final time')
    parser.add_argument('--dt', type=float, default=0.1, help='Output time interval')
    parser.add_argument('--L', type=float, default=2*np.pi, help='Domain size')
    parser.add_argument('--output', type=str, default=None, help='Output filename')

    args = parser.parse_args()

    print(f"Seregin Condition (1.4) Tracker")
    print(f"=" * 40)
    print(f"IC: {args.ic}, N: {args.N}, ν: {args.nu}, T: {args.T}")
    print()

    # Create solver and initial condition
    config = SolverConfig(N=args.N, L=args.L, nu=args.nu)
    solver = SpectralNSSolver(config)

    print("Creating initial condition...")
    omega_hat = create_initial_condition(args.ic, args.N, args.L)

    # Create tracker
    m_values = np.array([0.51, 0.53, 0.55, 0.57, 0.59])
    tracker = SereginTracker(L=args.L, nu=args.nu, m_values=m_values)

    # Callback function for the solver
    def callback(t, omega_hat_current, velocity, diag):
        """Callback to record Seregin diagnostics."""
        u, v, w = velocity
        tracker.record(t, omega_hat_current, u, v, w, diag)

    # Run simulation with tracking
    print("\nStarting simulation...")
    results = solver.run(omega_hat, args.T, callback=callback)

    # Save and summarize
    tracker.save_results(args.output)
    tracker.print_final_summary()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Analyze r-scaling of Seregin condition components.

Mines simulation data to extract A_{m₁}(r), E_m(r), D_m(r) as functions of r
and fits power-law scaling.
"""

import numpy as np
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.simulator.spectral_ns import SpectralNSSolver, SolverConfig
from src.simulator.initial_conditions import taylor_green, anti_parallel_vortex_tubes
from src.analysis.seregin_condition import SereginConditionChecker


def analyze_r_scaling(u, v, w, L, nu, m_values, n_r_points=50):
    """
    Analyze how A_{m₁}, E_m, D_m scale with r for various m.

    Returns dict with scaling data for each m.
    """
    checker = SereginConditionChecker(L=L, nu=nu)

    # Logarithmically spaced r values from small to moderate
    r_min = L / 100  # Small scale
    r_max = L / 4    # Moderate scale
    r_values = np.logspace(np.log10(r_min), np.log10(r_max), n_r_points)

    # Compute pressure once
    p = checker.compute_pressure_from_velocity(u, v, w)

    results = {}

    for m in m_values:
        A_m1_data = []
        E_m_data = []
        D_m_data = []

        for r in r_values:
            A = checker.compute_A_m1(u, v, w, r, m)
            E = checker.compute_E_m(u, v, w, r, m)
            D = checker.compute_D_m(p, r, m)

            A_m1_data.append(A)
            E_m_data.append(E)
            D_m_data.append(D)

        results[m] = {
            'r_values': r_values,
            'A_m1': np.array(A_m1_data),
            'E_m': np.array(E_m_data),
            'D_m': np.array(D_m_data),
            'total': np.array(A_m1_data) + np.array(E_m_data) + np.array(D_m_data)
        }

    return results


def fit_power_law(r, y, r_range=None):
    """
    Fit y = C * r^β to data.
    Returns (β, C, r_squared).
    """
    if r_range is not None:
        mask = (r >= r_range[0]) & (r <= r_range[1])
        r = r[mask]
        y = y[mask]

    # Remove zeros/negatives
    valid = y > 0
    r = r[valid]
    y = y[valid]

    if len(r) < 3:
        return None, None, 0

    # Log-log fit
    log_r = np.log(r)
    log_y = np.log(y)

    # Linear regression
    A = np.vstack([log_r, np.ones(len(log_r))]).T
    result = np.linalg.lstsq(A, log_y, rcond=None)
    beta, log_C = result[0]
    C = np.exp(log_C)

    # R-squared
    y_pred = C * r**beta
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    return beta, C, r_squared


def main():
    print("=" * 60)
    print("R-SCALING ANALYSIS FOR SEREGIN CONDITION")
    print("=" * 60)

    # Parameters
    N = 64
    L = 2 * np.pi
    nu = 0.001
    m_values = [0.51, 0.53, 0.55, 0.57, 0.59]

    # Test ICs
    ics = {
        'taylor_green': lambda: taylor_green(N, L, amplitude=1.0),
        'anti_parallel': lambda: anti_parallel_vortex_tubes(N, L, amplitude=5.0),
    }

    # Create solver
    config = SolverConfig(N=N, L=L, nu=nu)
    solver = SpectralNSSolver(config)

    all_results = {}

    for ic_name, ic_func in ics.items():
        print(f"\n--- Analyzing {ic_name} ---")

        # Get initial condition
        omega_hat = ic_func()

        # Get velocity
        u, v, w = solver.get_velocity(omega_hat)

        # Analyze r-scaling
        results = analyze_r_scaling(u, v, w, L, nu, m_values)
        all_results[ic_name] = results

        # Fit power laws
        print(f"\nPower-law fits: A_m1 ~ r^β")
        print("-" * 40)

        for m in m_values:
            r = results[m]['r_values']
            A = results[m]['A_m1']
            E = results[m]['E_m']
            D = results[m]['D_m']
            total = results[m]['total']

            # Fit for A_m1 (dominant component)
            beta_A, C_A, rsq_A = fit_power_law(r, A)
            beta_E, C_E, rsq_E = fit_power_law(r, E)
            beta_total, C_total, rsq_total = fit_power_law(r, total)

            print(f"\nm = {m:.2f} (m₁ = {2*m-1:.2f}):")
            print(f"  A_m1: β = {beta_A:.3f}, R² = {rsq_A:.3f}")
            print(f"  E_m:  β = {beta_E:.3f}, R² = {rsq_E:.3f}")
            print(f"  Total: β = {beta_total:.3f}, R² = {rsq_total:.3f}")

            # Theoretical prediction
            # K41 predicts: ||u||²_{L²(B(r))} ~ r^{11/3}
            # So A_m1 ~ r^{11/3 - (2m-1)} = r^{14/3 - 2m}
            beta_theory = 14/3 - 2*m
            print(f"  K41 prediction: β = {beta_theory:.3f}")

            # Check if β > 0 (decay)
            if beta_A is not None and beta_A > 0:
                print(f"  → A_m1 DECAYS as r → 0 (bounded)")
            elif beta_A is not None:
                print(f"  → A_m1 GROWS as r → 0 (unbounded!)")

        # Summary statistics
        print("\n" + "=" * 40)
        print("SUMMARY for", ic_name)
        print("=" * 40)

        # Check if all m values show decay
        all_decay = True
        for m in m_values:
            r = results[m]['r_values']
            total = results[m]['total']
            beta, _, rsq = fit_power_law(r, total)
            if beta is None or beta <= 0:
                all_decay = False
                print(f"  m = {m:.2f}: WARNING - may not decay (β = {beta})")

        if all_decay:
            print("All m values show DECAY of condition (1.4) as r → 0")
            print("→ NUMERICAL EVIDENCE supports Seregin's condition")

    # Cross-IC comparison
    print("\n" + "=" * 60)
    print("CROSS-IC COMPARISON")
    print("=" * 60)

    print("\nScaling exponent β for A_m1:")
    print("(Positive β means A_m1 → 0 as r → 0)")
    print("-" * 50)
    header = "m     | " + " | ".join(ics.keys())
    print(header)
    print("-" * len(header))

    for m in m_values:
        row = f"{m:.2f}  | "
        for ic_name in ics.keys():
            r = all_results[ic_name][m]['r_values']
            A = all_results[ic_name][m]['A_m1']
            beta, _, _ = fit_power_law(r, A)
            row += f"{beta:6.3f}        | "
        print(row)

    print("\nTheoretical predictions:")
    print("  K41: β = 14/3 - 2m (isotropic turbulence)")
    print("  Topology: β = 3 - 2m (frozen vortex lines)")
    print("  Worst-case 1D: β = 4 - 2m (filament)")


if __name__ == '__main__':
    main()

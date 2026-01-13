#!/usr/bin/env python3
"""
High-resolution Navier-Stokes simulations for Type II window analysis.

Runs anti-parallel vortex tubes at N=96 and N=128 with varying viscosity
to study the blowup rate evolution in the Type II window [3/5, 3/4).
"""

import sys
sys.path.insert(0, '/Users/ricalanis/Documents/dev/navier-stokes-research')

import numpy as np
from scipy.optimize import minimize
import json
from datetime import datetime
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

from src.simulator.spectral_ns import SpectralNSSolver, SolverConfig
from src.simulator.initial_conditions import anti_parallel_vortex_tubes
from src.analysis.blowup_detector import BlowupDetector


# Type II window bounds
ALPHA_LOWER = 3/5   # 0.6
ALPHA_UPPER = 3/4   # 0.75


def fit_blowup_rate(times: np.ndarray, u_Linf: np.ndarray,
                    window_fraction: float = 0.3) -> Dict:
    """
    Fit ||u||_inf ~ C * (T* - t)^{-alpha} to estimate blowup parameters.

    Uses the latter portion of the data where blowup behavior is most apparent.
    """
    n = len(times)
    if n < 10:
        return {'T_star': np.inf, 'alpha': 0.5, 'C': 1.0, 'fit_quality': 0.0}

    # Use the last window_fraction of data
    idx_start = max(0, int((1 - window_fraction) * n))
    t_fit = times[idx_start:]
    u_fit = u_Linf[idx_start:]

    # Filter out any invalid values
    valid = (u_fit > 0) & np.isfinite(u_fit) & np.isfinite(t_fit)
    if np.sum(valid) < 5:
        return {'T_star': np.inf, 'alpha': 0.5, 'C': 1.0, 'fit_quality': 0.0}

    t_fit = t_fit[valid]
    u_fit = u_fit[valid]

    def objective(params):
        T, alpha, logC = params
        if T <= t_fit[-1] * 1.001 or alpha <= 0.1 or alpha > 1.5:
            return 1e10
        C = np.exp(logC)
        predicted = C * (T - t_fit)**(-alpha)
        if np.any(predicted <= 0) or np.any(~np.isfinite(predicted)):
            return 1e10
        residual = np.sum((np.log(u_fit) - np.log(predicted))**2)
        return residual

    # Initial guesses based on growth rate
    growth_rate = (u_fit[-1] / u_fit[0]) ** (1 / max(t_fit[-1] - t_fit[0], 0.001))
    T0 = t_fit[-1] + 0.5  # Modest extrapolation
    alpha0 = 0.65  # Middle of Type II window
    C0 = u_fit[0] * (T0 - t_fit[0])**alpha0

    try:
        result = minimize(objective, [T0, alpha0, np.log(max(C0, 1e-10))],
                         method='Nelder-Mead',
                         options={'maxiter': 2000, 'xatol': 1e-6, 'fatol': 1e-6})

        if result.success or result.fun < 1e8:
            T_star, alpha, logC = result.x
            C = np.exp(logC)

            # Compute fit quality (R^2)
            predicted = C * (T_star - t_fit)**(-alpha)
            ss_res = np.sum((np.log(u_fit) - np.log(predicted))**2)
            ss_tot = np.sum((np.log(u_fit) - np.mean(np.log(u_fit)))**2)
            r_squared = 1 - ss_res / max(ss_tot, 1e-10)

            return {
                'T_star': T_star,
                'alpha': alpha,
                'C': C,
                'fit_quality': max(0, r_squared)
            }
    except Exception as e:
        pass

    return {'T_star': np.inf, 'alpha': 0.5, 'C': 1.0, 'fit_quality': 0.0}


def compute_rate_evolution(times: np.ndarray, u_Linf: np.ndarray,
                          window_size: int = 50) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute the evolution of the fitted rate alpha(t) using sliding window.
    """
    n = len(times)
    if n < window_size + 10:
        return np.array([]), np.array([])

    alphas = []
    t_alphas = []

    step = max(1, window_size // 4)
    for i in range(window_size, n - 5, step):
        t_window = times[max(0, i-window_size):i]
        u_window = u_Linf[max(0, i-window_size):i]

        fit = fit_blowup_rate(t_window, u_window, window_fraction=0.5)
        if fit['fit_quality'] > 0.5 and 0.1 < fit['alpha'] < 1.5:
            alphas.append(fit['alpha'])
            t_alphas.append(times[i])

    return np.array(t_alphas), np.array(alphas)


def run_simulation(N: int, nu: float, T_final: float = 3.0,
                   amplitude: float = 2.0) -> Dict:
    """
    Run a single anti-parallel vortex tube simulation.

    Args:
        N: Grid resolution
        nu: Kinematic viscosity
        T_final: Maximum simulation time
        amplitude: Initial condition amplitude

    Returns:
        Dictionary with simulation results and analysis
    """
    print(f"\n{'='*60}")
    print(f"Running N={N}, nu={nu:.4f}, T_final={T_final}")
    print(f"{'='*60}")

    config = SolverConfig(
        N=N,
        nu=nu,
        cfl=0.4,  # Conservative CFL for stability
        integrator='rk4',
        dealias=True
    )

    solver = SpectralNSSolver(config)
    detector = BlowupDetector(nu=nu, L=config.L)

    # Initial condition
    omega_hat_0 = anti_parallel_vortex_tubes(N=N, L=config.L, amplitude=amplitude)

    # Storage for time series
    times = []
    u_Linf_series = []
    omega_Linf_series = []
    energy_series = []
    enstrophy_series = []

    omega_hat = omega_hat_0
    t = 0.0
    step_count = 0

    # Track time in Type II window
    time_in_window = 0.0
    last_t = 0.0
    max_alpha_achieved = 0.0
    window_entry_exit = []

    print(f"Starting simulation...")

    while t < T_final:
        # Get physical fields
        from numpy.fft import ifftn
        u_hat, v_hat, w_hat = solver._biot_savart(*omega_hat)
        u = np.real(ifftn(u_hat))
        v = np.real(ifftn(v_hat))
        w = np.real(ifftn(w_hat))
        omega_x = np.real(ifftn(omega_hat[0]))
        omega_y = np.real(ifftn(omega_hat[1]))
        omega_z = np.real(ifftn(omega_hat[2]))

        # Compute norms
        u_mag = np.sqrt(u**2 + v**2 + w**2)
        omega_mag = np.sqrt(omega_x**2 + omega_y**2 + omega_z**2)
        u_Linf = np.max(u_mag)
        omega_Linf = np.max(omega_mag)
        energy = 0.5 * np.mean(u_mag**2) * config.L**3
        enstrophy = 0.5 * np.mean(omega_mag**2) * config.L**3

        # Store
        times.append(t)
        u_Linf_series.append(u_Linf)
        omega_Linf_series.append(omega_Linf)
        energy_series.append(energy)
        enstrophy_series.append(enstrophy)

        # Progress reporting
        if step_count % 500 == 0:
            print(f"  t = {t:.4f}, ||u||_inf = {u_Linf:.4e}, ||omega||_inf = {omega_Linf:.4e}")

            # Fit rate on the fly if we have enough data
            if len(times) > 100:
                fit = fit_blowup_rate(np.array(times), np.array(u_Linf_series))
                if fit['fit_quality'] > 0.6:
                    alpha_curr = fit['alpha']
                    print(f"       Current fitted alpha = {alpha_curr:.4f}, T* ~ {fit['T_star']:.4f}")

        # Check for numerical blowup
        if u_Linf > 1e6 or np.isnan(u_Linf) or np.isnan(omega_Linf):
            print(f"  Numerical blowup at t = {t:.6f}")
            break

        # Step forward
        try:
            omega_hat, dt = solver.step(omega_hat)
            t += dt
            step_count += 1
        except Exception as e:
            print(f"  Solver error at t = {t:.6f}: {e}")
            break

    # Convert to arrays
    times = np.array(times)
    u_Linf_series = np.array(u_Linf_series)
    omega_Linf_series = np.array(omega_Linf_series)
    energy_series = np.array(energy_series)
    enstrophy_series = np.array(enstrophy_series)

    # Final fit
    final_fit = fit_blowup_rate(times, u_Linf_series)

    # Compute rate evolution
    t_alphas, alphas = compute_rate_evolution(times, u_Linf_series)

    if len(alphas) > 0:
        max_alpha_achieved = np.max(alphas)

        # Time in Type II window [0.6, 0.75)
        in_window = (alphas >= ALPHA_LOWER) & (alphas < ALPHA_UPPER)
        if len(t_alphas) > 1 and np.any(in_window):
            dt_alpha = np.diff(t_alphas)
            dt_alpha = np.append(dt_alpha, dt_alpha[-1])
            time_in_window = np.sum(dt_alpha[in_window])

            # Find window entry/exit times
            window_changes = np.diff(in_window.astype(int))
            entries = np.where(window_changes == 1)[0]
            exits = np.where(window_changes == -1)[0]
            for idx in entries:
                window_entry_exit.append(('enter', t_alphas[idx+1], alphas[idx+1]))
            for idx in exits:
                window_entry_exit.append(('exit', t_alphas[idx+1], alphas[idx+1]))

    # Determine final behavior
    if len(alphas) > 5:
        final_alpha_trend = alphas[-5:]
        if np.mean(final_alpha_trend) < ALPHA_LOWER:
            final_behavior = "regularizing (alpha < 0.6)"
        elif np.all(final_alpha_trend >= ALPHA_LOWER) and np.all(final_alpha_trend < ALPHA_UPPER):
            final_behavior = "in Type II window"
        elif np.mean(final_alpha_trend) >= ALPHA_UPPER:
            final_behavior = "potential Type I (alpha >= 0.75)"
        else:
            final_behavior = "transitional"
    else:
        final_behavior = "insufficient data"

    if u_Linf_series[-1] > 1e5:
        final_behavior += " + numerical blowup"

    results = {
        'N': N,
        'nu': nu,
        'T_final_achieved': times[-1] if len(times) > 0 else 0,
        'num_steps': step_count,
        'final_u_Linf': u_Linf_series[-1] if len(u_Linf_series) > 0 else 0,
        'final_omega_Linf': omega_Linf_series[-1] if len(omega_Linf_series) > 0 else 0,
        'max_u_Linf': np.max(u_Linf_series) if len(u_Linf_series) > 0 else 0,
        'max_omega_Linf': np.max(omega_Linf_series) if len(omega_Linf_series) > 0 else 0,
        'T_star_estimate': final_fit['T_star'],
        'final_alpha': final_fit['alpha'],
        'final_fit_quality': final_fit['fit_quality'],
        'max_alpha_achieved': max_alpha_achieved,
        'time_in_type_II_window': time_in_window,
        'final_behavior': final_behavior,
        'window_entry_exit': window_entry_exit,
        'time_series': {
            'times': times.tolist(),
            'u_Linf': u_Linf_series.tolist(),
            'omega_Linf': omega_Linf_series.tolist(),
            'energy': energy_series.tolist(),
            'enstrophy': enstrophy_series.tolist()
        },
        'alpha_evolution': {
            'times': t_alphas.tolist() if len(t_alphas) > 0 else [],
            'alphas': alphas.tolist() if len(alphas) > 0 else []
        }
    }

    print(f"\n  Simulation complete:")
    print(f"    Final time: {times[-1]:.4f}")
    print(f"    Final ||u||_inf: {u_Linf_series[-1]:.4e}")
    print(f"    T* estimate: {final_fit['T_star']:.4f}")
    print(f"    Final alpha: {final_fit['alpha']:.4f}")
    print(f"    Max alpha achieved: {max_alpha_achieved:.4f}")
    print(f"    Time in Type II window: {time_in_window:.4f}")
    print(f"    Final behavior: {final_behavior}")

    return results


def main():
    """Run all high-resolution simulations."""
    print("="*70)
    print("HIGH-RESOLUTION NAVIER-STOKES SIMULATIONS FOR TYPE II ANALYSIS")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    print(f"\nType II window: [{ALPHA_LOWER:.4f}, {ALPHA_UPPER:.4f})")
    print("Running anti-parallel vortex tubes configuration")

    # Parameters
    resolutions = [96, 128]
    viscosities = [0.0005, 0.0002, 0.0001]
    T_final = 3.0

    all_results = []

    for N in resolutions:
        for nu in viscosities:
            try:
                result = run_simulation(N=N, nu=nu, T_final=T_final)
                all_results.append(result)
            except Exception as e:
                print(f"\nERROR in N={N}, nu={nu}: {e}")
                all_results.append({
                    'N': N,
                    'nu': nu,
                    'error': str(e)
                })

    # Summary
    print("\n" + "="*70)
    print("SUMMARY OF ALL SIMULATIONS")
    print("="*70)
    print(f"\n{'N':<6} {'nu':<10} {'T_achieved':<12} {'T*':<10} {'alpha':<8} {'max_alpha':<10} {'t_in_window':<12} {'behavior'}")
    print("-"*100)

    for r in all_results:
        if 'error' in r:
            print(f"{r['N']:<6} {r['nu']:<10.4f} ERROR: {r['error'][:40]}")
        else:
            print(f"{r['N']:<6} {r['nu']:<10.4f} {r['T_final_achieved']:<12.4f} {r['T_star_estimate']:<10.4f} "
                  f"{r['final_alpha']:<8.4f} {r['max_alpha_achieved']:<10.4f} {r['time_in_type_II_window']:<12.4f} "
                  f"{r['final_behavior'][:30]}")

    # Return for external use
    return all_results


if __name__ == "__main__":
    results = main()

    # Save results to JSON for later processing
    output_file = "/Users/ricalanis/Documents/dev/navier-stokes-research/docs/computations/high_res_results.json"

    # Prepare serializable results (without large time series for JSON)
    summary_results = []
    for r in results:
        summary = {k: v for k, v in r.items() if k not in ['time_series', 'alpha_evolution']}
        if 'alpha_evolution' in r:
            summary['alpha_evolution_length'] = len(r['alpha_evolution'].get('times', []))
        summary_results.append(summary)

    with open(output_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'description': 'High-resolution Type II blowup analysis',
            'type_II_window': [ALPHA_LOWER, ALPHA_UPPER],
            'results': summary_results
        }, f, indent=2)

    print(f"\nResults saved to: {output_file}")

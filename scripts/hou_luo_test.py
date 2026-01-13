#!/usr/bin/env python3
"""
Hou-Luo Blowup Candidate Test Simulations.

This script tests the Hou-Luo initial condition (axisymmetric blowup candidate)
at various viscosities to analyze potential Type II blowup behavior.

The Hou-Luo scenario (2014) is based on numerical evidence that 3D axisymmetric
Euler equations can develop finite-time singularity. For Navier-Stokes with
small viscosity, this serves as a candidate for approaching blowup.

Key question: Can the blowup rate alpha sustain values in [3/5, 3/4)?

References:
- Luo, G., Hou, T.Y. "Potentially singular solutions of the 3D axisymmetric
  Euler equations" PNAS 111(36), 2014
- Luo, G., Hou, T.Y. "Toward the finite-time blowup of the 3D axisymmetric
  Euler equations" SIAM Multiscale Model. Simul. 2014
"""

import sys
sys.path.insert(0, '/Users/ricalanis/Documents/dev/navier-stokes-research')

import numpy as np
from numpy.fft import ifftn
from scipy.optimize import minimize
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

from src.simulator.spectral_ns import SpectralNSSolver, SolverConfig
from src.simulator.initial_conditions import hou_luo_candidate
from src.analysis.blowup_detector import BlowupDetector


# Type II window bounds (from theory)
ALPHA_LOWER = 3/5   # 0.6 - BKM lower bound
ALPHA_UPPER = 3/4   # 0.75 - Dissipation upper bound


def fit_blowup_rate(times: np.ndarray, u_Linf: np.ndarray,
                    window_fraction: float = 0.3) -> Dict:
    """
    Fit ||u||_inf ~ C * (T* - t)^{-alpha} to estimate blowup parameters.

    Uses nonlinear least squares on log-transformed data.
    """
    n = len(times)
    if n < 10:
        return {'T_star': np.inf, 'alpha': 0.5, 'C': 1.0, 'fit_quality': 0.0}

    # Use the last window_fraction of data
    idx_start = max(0, int((1 - window_fraction) * n))
    t_fit = times[idx_start:]
    u_fit = u_Linf[idx_start:]

    # Filter invalid values
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

    # Initial guesses
    T0 = t_fit[-1] + 0.5
    alpha0 = 0.65  # Middle of Type II window
    C0 = u_fit[0] * (T0 - t_fit[0])**alpha0

    try:
        result = minimize(objective, [T0, alpha0, np.log(max(C0, 1e-10))],
                         method='Nelder-Mead',
                         options={'maxiter': 2000, 'xatol': 1e-6, 'fatol': 1e-6})

        if result.success or result.fun < 1e8:
            T_star, alpha, logC = result.x
            C = np.exp(logC)

            # Compute R^2
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
    except Exception:
        pass

    return {'T_star': np.inf, 'alpha': 0.5, 'C': 1.0, 'fit_quality': 0.0}


def compute_rate_evolution(times: np.ndarray, u_Linf: np.ndarray,
                          window_size: int = 50) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute evolution of fitted rate alpha(t) using sliding window.

    Returns (t_alphas, alphas, fit_qualities)
    """
    n = len(times)
    if n < window_size + 10:
        return np.array([]), np.array([]), np.array([])

    alphas = []
    t_alphas = []
    qualities = []

    step = max(1, window_size // 4)
    for i in range(window_size, n - 5, step):
        t_window = times[max(0, i-window_size):i]
        u_window = u_Linf[max(0, i-window_size):i]

        fit = fit_blowup_rate(t_window, u_window, window_fraction=0.5)
        if fit['fit_quality'] > 0.5 and 0.1 < fit['alpha'] < 1.5:
            alphas.append(fit['alpha'])
            t_alphas.append(times[i])
            qualities.append(fit['fit_quality'])

    return np.array(t_alphas), np.array(alphas), np.array(qualities)


def analyze_type_II_behavior(times: np.ndarray, alphas: np.ndarray) -> Dict:
    """
    Analyze whether the solution exhibits sustained Type II behavior.

    Checks if alpha stays in [3/5, 3/4) for extended periods.
    """
    if len(alphas) < 5:
        return {
            'in_window': False,
            'time_in_window': 0.0,
            'fraction_in_window': 0.0,
            'max_consecutive_in_window': 0.0,
            'trend': 'insufficient data'
        }

    in_window = (alphas >= ALPHA_LOWER) & (alphas < ALPHA_UPPER)

    # Time in window
    if len(times) > 1:
        dt = np.diff(times)
        dt = np.append(dt, dt[-1] if len(dt) > 0 else 0.01)
        time_in_window = np.sum(dt[in_window])
        total_time = times[-1] - times[0]
        fraction = time_in_window / max(total_time, 1e-10)
    else:
        time_in_window = 0.0
        fraction = 0.0

    # Maximum consecutive time in window
    max_consecutive = 0.0
    current_consecutive = 0.0
    last_t = times[0] if len(times) > 0 else 0

    for i, (t, iw) in enumerate(zip(times, in_window)):
        if iw:
            current_consecutive += t - last_t
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 0.0
        last_t = t

    # Trend analysis
    if len(alphas) >= 10:
        early = np.mean(alphas[:len(alphas)//4])
        late = np.mean(alphas[-len(alphas)//4:])

        if late > early + 0.05:
            trend = 'increasing (toward blowup)'
        elif late < early - 0.05:
            trend = 'decreasing (regularizing)'
        else:
            trend = 'stable'
    else:
        trend = 'insufficient data'

    return {
        'in_window': np.any(in_window),
        'time_in_window': time_in_window,
        'fraction_in_window': fraction,
        'max_consecutive_in_window': max_consecutive,
        'mean_alpha': np.mean(alphas),
        'std_alpha': np.std(alphas),
        'min_alpha': np.min(alphas),
        'max_alpha': np.max(alphas),
        'trend': trend,
        'final_5_mean': np.mean(alphas[-5:]) if len(alphas) >= 5 else np.nan
    }


def run_hou_luo_simulation(N: int, nu: float, T_final: float = 2.0,
                           amplitude: float = 5.0, mode: str = 'full') -> Dict:
    """
    Run a Hou-Luo initial condition simulation.

    Args:
        N: Grid resolution
        nu: Kinematic viscosity
        T_final: Maximum simulation time
        amplitude: Initial condition amplitude (larger = more intense)
        mode: 'full' or 'simplified' for IC generation

    Returns:
        Dictionary with comprehensive simulation results
    """
    print(f"\n{'='*60}")
    print(f"HOU-LUO SIMULATION: N={N}, nu={nu:.6f}, amp={amplitude}")
    print(f"{'='*60}")

    config = SolverConfig(
        N=N,
        nu=nu,
        cfl=0.35,  # Conservative for potentially singular solutions
        integrator='rk4',
        dealias=True
    )

    solver = SpectralNSSolver(config)

    # Generate Hou-Luo initial condition
    print(f"Generating Hou-Luo IC (mode={mode})...")
    omega_hat_0 = hou_luo_candidate(N=N, L=config.L, amplitude=amplitude, mode=mode)

    # Verify IC is valid
    omega_x = np.real(ifftn(omega_hat_0[0]))
    omega_mag_0 = np.sqrt(
        np.real(ifftn(omega_hat_0[0]))**2 +
        np.real(ifftn(omega_hat_0[1]))**2 +
        np.real(ifftn(omega_hat_0[2]))**2
    )
    print(f"Initial ||omega||_inf = {np.max(omega_mag_0):.4e}")

    # Storage
    times = []
    u_Linf_series = []
    omega_Linf_series = []
    energy_series = []
    enstrophy_series = []
    omega_max_locs = []  # Track location of max vorticity

    omega_hat = omega_hat_0
    t = 0.0
    step_count = 0

    print(f"Running simulation to T={T_final}...")

    while t < T_final:
        # Get physical fields
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

        # Location of max vorticity (for Hou-Luo, should concentrate on axis)
        max_idx = np.unravel_index(np.argmax(omega_mag), omega_mag.shape)

        # Store
        times.append(t)
        u_Linf_series.append(u_Linf)
        omega_Linf_series.append(omega_Linf)
        energy_series.append(energy)
        enstrophy_series.append(enstrophy)
        omega_max_locs.append(max_idx)

        # Progress
        if step_count % 300 == 0:
            print(f"  t = {t:.4f}, ||u||_inf = {u_Linf:.4e}, ||omega||_inf = {omega_Linf:.4e}")

            if len(times) > 80:
                fit = fit_blowup_rate(np.array(times), np.array(u_Linf_series))
                if fit['fit_quality'] > 0.5:
                    alpha_window = 'IN' if ALPHA_LOWER <= fit['alpha'] < ALPHA_UPPER else 'OUT'
                    print(f"       alpha = {fit['alpha']:.4f} ({alpha_window}), "
                          f"T* ~ {fit['T_star']:.4f}, R^2 = {fit['fit_quality']:.3f}")

        # Check for numerical blowup
        if u_Linf > 1e6 or np.isnan(u_Linf):
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

    # Analysis
    print(f"\nAnalyzing results...")

    # Global fit
    global_fit = fit_blowup_rate(times, u_Linf_series)

    # Rate evolution
    t_alphas, alphas, qualities = compute_rate_evolution(times, u_Linf_series)

    # Type II behavior analysis
    type_II_analysis = analyze_type_II_behavior(t_alphas, alphas)

    # BKM integral: int ||omega||_inf dt
    if len(times) > 1:
        # Use scipy.integrate.trapezoid or manual trapz for numpy 2.x compatibility
        try:
            from scipy.integrate import trapezoid
            bkm_integral = trapezoid(omega_Linf_series, times)
        except ImportError:
            # Manual trapezoidal integration
            dt = np.diff(times)
            avg_omega = (omega_Linf_series[:-1] + omega_Linf_series[1:]) / 2
            bkm_integral = np.sum(dt * avg_omega)
    else:
        bkm_integral = 0.0

    # Check if max vorticity migrated toward axis (key Hou-Luo feature)
    axis_concentration = False
    if len(omega_max_locs) > 10:
        # Check if max location stayed near center (axis)
        center = N // 2
        late_locs = omega_max_locs[-10:]
        distances = [np.sqrt((loc[0] - center)**2 + (loc[1] - center)**2)
                    for loc in late_locs]
        axis_concentration = np.mean(distances) < N / 4

    results = {
        'config': {
            'N': N,
            'nu': nu,
            'amplitude': amplitude,
            'mode': mode,
            'T_final_requested': T_final
        },
        'simulation': {
            'T_final_achieved': times[-1] if len(times) > 0 else 0,
            'num_steps': step_count,
            'final_u_Linf': float(u_Linf_series[-1]) if len(u_Linf_series) > 0 else 0,
            'final_omega_Linf': float(omega_Linf_series[-1]) if len(omega_Linf_series) > 0 else 0,
            'max_u_Linf': float(np.max(u_Linf_series)) if len(u_Linf_series) > 0 else 0,
            'max_omega_Linf': float(np.max(omega_Linf_series)) if len(omega_Linf_series) > 0 else 0,
            'energy_change': float((energy_series[-1] - energy_series[0]) / max(energy_series[0], 1e-10))
                            if len(energy_series) > 1 else 0,
            'bkm_integral': float(bkm_integral)
        },
        'global_fit': {
            'T_star': float(global_fit['T_star']),
            'alpha': float(global_fit['alpha']),
            'C': float(global_fit['C']),
            'fit_quality': float(global_fit['fit_quality'])
        },
        'type_II_analysis': {k: (float(v) if isinstance(v, (np.floating, np.integer)) else
                                 (None if isinstance(v, float) and np.isnan(v) else v))
                            for k, v in type_II_analysis.items()},
        'hou_luo_features': {
            'axis_concentration': axis_concentration,
            'vorticity_amplification': float(omega_Linf_series[-1] / max(omega_Linf_series[0], 1e-10))
                                      if len(omega_Linf_series) > 1 else 1.0
        },
        'time_series': {
            'times': times.tolist(),
            'u_Linf': u_Linf_series.tolist(),
            'omega_Linf': omega_Linf_series.tolist(),
            'energy': energy_series.tolist(),
            'enstrophy': enstrophy_series.tolist()
        },
        'alpha_evolution': {
            'times': t_alphas.tolist() if len(t_alphas) > 0 else [],
            'alphas': alphas.tolist() if len(alphas) > 0 else [],
            'fit_qualities': qualities.tolist() if len(qualities) > 0 else []
        }
    }

    # Summary
    print(f"\n{'='*40}")
    print(f"SIMULATION SUMMARY:")
    print(f"  Final time: {times[-1]:.4f}")
    print(f"  ||u||_inf: {u_Linf_series[0]:.4e} -> {u_Linf_series[-1]:.4e}")
    print(f"  ||omega||_inf: {omega_Linf_series[0]:.4e} -> {omega_Linf_series[-1]:.4e}")
    print(f"  BKM integral: {bkm_integral:.4e}")
    print(f"\n  BLOWUP FIT:")
    print(f"    T* estimate: {global_fit['T_star']:.4f}")
    print(f"    alpha: {global_fit['alpha']:.4f}")
    print(f"    fit quality (R^2): {global_fit['fit_quality']:.4f}")
    print(f"\n  TYPE II ANALYSIS:")
    print(f"    In [3/5, 3/4) window: {type_II_analysis['in_window']}")
    print(f"    Time in window: {type_II_analysis['time_in_window']:.4f}")
    print(f"    Fraction in window: {type_II_analysis['fraction_in_window']:.2%}")
    print(f"    Max consecutive in window: {type_II_analysis['max_consecutive_in_window']:.4f}")
    if 'mean_alpha' in type_II_analysis:
        print(f"    Mean alpha: {type_II_analysis['mean_alpha']:.4f}")
        print(f"    Alpha range: [{type_II_analysis['min_alpha']:.4f}, {type_II_analysis['max_alpha']:.4f}]")
    print(f"    Trend: {type_II_analysis['trend']}")
    print(f"\n  HOU-LUO FEATURES:")
    print(f"    Axis concentration: {axis_concentration}")
    print(f"    Vorticity amplification: {results['hou_luo_features']['vorticity_amplification']:.2f}x")
    print(f"{'='*40}")

    return results


def main():
    """Run comprehensive Hou-Luo test suite."""
    print("="*70)
    print("HOU-LUO BLOWUP CANDIDATE TEST SIMULATIONS")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    print(f"\nType II window: [{ALPHA_LOWER:.4f}, {ALPHA_UPPER:.4f})")
    print("Testing if Hou-Luo IC can sustain alpha in this range")
    print("\nReferences:")
    print("  Luo & Hou, PNAS 111(36), 2014")
    print("  Luo & Hou, SIAM MMS, 2014")

    # Test parameters
    # Vary viscosity from moderate to very small
    viscosities = [0.001, 0.0005, 0.0002, 0.0001]
    N = 64  # Base resolution (increase for more accurate results)
    T_final = 2.0
    amplitudes = [3.0, 5.0]  # Test different amplitudes

    all_results = []

    print(f"\nTest matrix:")
    print(f"  Resolutions: N={N}")
    print(f"  Viscosities: {viscosities}")
    print(f"  Amplitudes: {amplitudes}")
    print(f"  T_final: {T_final}")

    for amp in amplitudes:
        for nu in viscosities:
            try:
                result = run_hou_luo_simulation(
                    N=N, nu=nu, T_final=T_final,
                    amplitude=amp, mode='full'
                )
                all_results.append(result)
            except Exception as e:
                print(f"\nERROR in N={N}, nu={nu}, amp={amp}: {e}")
                import traceback
                traceback.print_exc()
                all_results.append({
                    'config': {'N': N, 'nu': nu, 'amplitude': amp},
                    'error': str(e)
                })

    # Final summary table
    print("\n" + "="*70)
    print("FINAL SUMMARY TABLE")
    print("="*70)
    print(f"\n{'amp':<6} {'nu':<10} {'T*':<10} {'alpha':<8} {'in_window':<10} "
          f"{'t_in_win':<10} {'trend':<20}")
    print("-"*90)

    for r in all_results:
        if 'error' in r:
            print(f"{r['config']['amplitude']:<6} {r['config']['nu']:<10.4f} ERROR: {r['error'][:30]}")
        else:
            cfg = r['config']
            gf = r['global_fit']
            t2 = r['type_II_analysis']
            print(f"{cfg['amplitude']:<6.1f} {cfg['nu']:<10.4f} "
                  f"{gf['T_star']:<10.4f} {gf['alpha']:<8.4f} "
                  f"{'YES' if t2['in_window'] else 'NO':<10} "
                  f"{t2['time_in_window']:<10.4f} {t2['trend'][:20]}")

    # Key findings
    print("\n" + "="*70)
    print("KEY FINDINGS")
    print("="*70)

    successful = [r for r in all_results if 'error' not in r]
    if successful:
        # Any sustained Type II?
        sustained_type_II = [r for r in successful
                           if r['type_II_analysis']['fraction_in_window'] > 0.5]

        if sustained_type_II:
            print("\nSUSTAINED TYPE II BEHAVIOR DETECTED!")
            print("These cases show alpha in [3/5, 3/4) for >50% of simulation:")
            for r in sustained_type_II:
                cfg = r['config']
                t2 = r['type_II_analysis']
                print(f"  nu={cfg['nu']:.4f}, amp={cfg['amplitude']}: "
                      f"mean alpha={t2['mean_alpha']:.4f}, "
                      f"fraction={t2['fraction_in_window']:.2%}")
        else:
            print("\nNo sustained Type II behavior detected.")
            print("All simulations either regularized (alpha < 0.6) or")
            print("approached Type I (alpha >= 0.75) before being cut off.")

        # Best candidate
        best = max(successful, key=lambda r: r['type_II_analysis']['time_in_window'])
        print(f"\nBest candidate for Type II (longest time in window):")
        print(f"  nu={best['config']['nu']:.4f}, amp={best['config']['amplitude']}")
        print(f"  Time in window: {best['type_II_analysis']['time_in_window']:.4f}")
        print(f"  Final alpha: {best['global_fit']['alpha']:.4f}")

    return all_results


if __name__ == "__main__":
    results = main()

    # Save results
    output_file = "/Users/ricalanis/Documents/dev/navier-stokes-research/docs/computations/hou_luo_results.json"

    # Prepare serializable summary (without large time series)
    summary_results = []
    for r in results:
        if 'error' in r:
            summary_results.append(r)
        else:
            summary = {
                'config': r['config'],
                'simulation': r['simulation'],
                'global_fit': r['global_fit'],
                'type_II_analysis': r['type_II_analysis'],
                'hou_luo_features': r['hou_luo_features']
            }
            summary_results.append(summary)

    with open(output_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'description': 'Hou-Luo blowup candidate test simulations',
            'type_II_window': [ALPHA_LOWER, ALPHA_UPPER],
            'results': summary_results
        }, f, indent=2)

    print(f"\nResults saved to: {output_file}")

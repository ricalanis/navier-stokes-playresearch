# High-Resolution Navier-Stokes Simulations: Type II Window Analysis

**Date:** 2026-01-12
**Configuration:** Anti-parallel vortex tubes
**Type II Window:** [0.6, 0.75)

## Objective

Study the blowup rate evolution alpha(t) at higher resolutions (N=96, N=128) to determine:
1. Whether transient Type II behavior persists at higher resolution
2. Maximum alpha achieved and time spent in the Type II window
3. Final behavior: regularization vs sustained Type II vs numerical blowup

## Methodology

### Simulation Setup
- **Solver:** Pseudo-spectral Navier-Stokes in vorticity formulation
- **Time Integration:** RK4 with adaptive CFL (CFL = 0.4)
- **Dealiasing:** 2/3 rule
- **Initial Condition:** Anti-parallel vortex tubes with amplitude = 2.0
- **Final Time Target:** T = 3.0

### Blowup Rate Fitting
The blowup rate alpha is fitted from the ansatz:
```
||u||_infinity ~ C * (T* - t)^{-alpha}
```

Rate evolution computed using sliding window of 30-50 timesteps.

## Results: N = 96 Resolution

### Summary Table

| nu      | T_achieved | T*      | final_alpha | max_alpha | t_in_window | behavior     |
|---------|------------|---------|-------------|-----------|-------------|--------------|
| 0.0005  | 3.0188     | 49.85   | 0.454       | 0.685     | 0.415       | regularizing |
| 0.0002  | 3.0085     | 87.90   | 1.022       | 1.500     | 0.000       | transitional |
| 0.0001  | 3.0050     | 80.32   | 0.995       | 1.054     | 0.000       | insufficient |

### Detailed Analysis

#### Case 1: nu = 0.0005 (highest viscosity)
- **Observed Transient Type II Behavior**
- Entered Type II window [0.6, 0.75) at t ~ 2.43 with alpha ~ 0.685
- Exited window at t ~ 2.84 with alpha dropping to ~ 0.453
- **Total time in Type II window: 0.415 time units**
- Final behavior: regularizing (alpha < 0.6)
- This represents genuine transient entry into the Type II regime followed by viscous regularization

#### Case 2: nu = 0.0002 (medium viscosity)
- Max alpha reached 1.5 (cap in fitting algorithm)
- No time spent in Type II window
- Final behavior: transitional
- The fit shows more aggressive blowup rates outside the Type II window
- Suggests stronger nonlinear dynamics competing with weaker dissipation

#### Case 3: nu = 0.0001 (lowest viscosity)
- Max alpha ~ 1.05, final alpha ~ 0.995
- No time in Type II window (rates above 0.75)
- Insufficient data for full evolution characterization
- Rates trending toward Type I regime (alpha >= 0.75)

## Key Observations

### 1. Resolution Effect
At N=96, we observe:
- Clearer separation between regularizing and aggressive growth regimes
- The nu = 0.0005 case shows clear transient Type II entry
- Lower viscosity cases show rates above the Type II window

### 2. Type II Window Transience
The nu = 0.0005 simulation demonstrates the **transient nature** of Type II behavior:
```
t ~ 2.43: Enter Type II window (alpha = 0.685)
t ~ 2.84: Exit Type II window (alpha = 0.453)
Duration: ~0.41 time units
```
This is consistent with the theoretical picture that Type II is an unstable intermediate regime.

### 3. Viscosity Dependence
| nu      | Behavior Pattern                                     |
|---------|-----------------------------------------------------|
| 0.0005  | Transient Type II -> regularization                 |
| 0.0002  | Rapid growth rates, transitional behavior           |
| 0.0001  | Rates above Type II window, potential Type I        |

Lower viscosity leads to more aggressive dynamics that skip over the Type II window.

## N = 128 Simulations (In Progress)

Higher resolution simulations at N=128 are computationally intensive and ongoing. Initial observations:
- Initial ||u||_inf ~ 0.817, ||omega||_inf ~ 4.01
- Simulations require ~8x more computation per timestep than N=96
- Results will be updated when available

### Expected Insights from N=128
1. Whether Type II transients persist or are resolution artifacts
2. More accurate blowup time estimates
3. Better resolved vorticity gradients near potential singularities

## Theoretical Context

### Type II Window: alpha in [3/5, 3/4)

The interval [0.6, 0.75) is critical because:
- **Lower bound (alpha = 3/5):** BKM criterion requires ||omega||_inf integrable for regularity
- **Upper bound (alpha = 3/4):** Dissipation analysis bounds

Type II blowup in this window would violate no known a priori bounds while still producing a singularity.

### Observed Behavior
The simulations suggest:
1. **At moderate viscosity (nu = 0.0005):** Solutions can transiently enter the Type II window but viscosity eventually dominates
2. **At low viscosity (nu = 0.0001, 0.0002):** Nonlinear dynamics drive rates above the Type II window

## Conclusions

1. **Transient Type II behavior is observable** at N=96 with nu=0.0005
   - Duration: ~0.41 time units in window [0.6, 0.75)
   - Max alpha achieved: 0.685

2. **Type II appears to be unstable** - solutions don't remain in the window
   - Either regularize (exit below 0.6)
   - Or transition toward Type I rates (above 0.75)

3. **Lower viscosity favors escape above Type II window**
   - nu = 0.0002, 0.0001 show rates >= 0.75
   - This aligns with stronger nonlinear effects

4. **Higher resolution (N=128) needed** to confirm whether:
   - Transient behavior is physical or numerical
   - Type II states have finite lifetime or are truly unstable

## Next Steps

1. Complete N=128 simulations for all viscosity values
2. Run longer time integrations (T > 3.0) for nu = 0.0005 case
3. Study the exit mechanism from Type II window in detail
4. Compare with theoretical predictions for Type II instability

## Technical Notes

- Timestep varies adaptively based on CFL condition
- Fit quality threshold: R^2 > 0.4 for rate tracking
- Window size for rate evolution: 30 timesteps
- All simulations use 2/3 dealiasing rule

# Seregin Condition (1.4) Numerical Experiments

**Date:** January 13, 2026
**Status:** PRELIMINARY RESULTS

---

## Overview

Implemented and tested Seregin's condition (1.4) for Type II blowup analysis:

```
sup_{0 < r < 1} { A_{m₁}(v,r) + E_m(v,r) + D_m(q,r) } < ∞
```

for m ∈ (1/2, 3/5), where:
- A_{m₁} = r^{-(2m-1)} sup_t ∫_{B(r)} |v|² dx (weighted velocity norm)
- E_m = r^{-m} ∫_{Q(r)} |∇v|² dz (weighted dissipation)
- D_m = r^{-2m} ∫_{Q(r)} |q|^{3/2} dz (weighted pressure)

---

## Experiments Conducted

### Experiment 1: Taylor-Green Vortex (Baseline)

**Parameters:** N=32, ν=0.001, T=1.0

**Results:**
| m | sup_total | A_m1 | E_m | D_m | Trend |
|---|-----------|------|-----|-----|-------|
| 0.51 | 5.51 | 5.03 | 0.098 | 0.003 | STABLE |
| 0.53 | 5.42 | 4.94 | 0.097 | 0.003 | STABLE |
| 0.55 | 5.32 | 4.85 | 0.097 | 0.003 | STABLE |
| 0.57 | 5.23 | 4.77 | 0.096 | 0.003 | STABLE |
| 0.59 | 5.13 | 4.68 | 0.095 | 0.003 | STABLE |

**Conclusion:** Condition (1.4) BOUNDED. Expected for known regular solution.

---

### Experiment 2: Anti-Parallel Vortex Tubes (Challenging)

**Parameters:** N=64, ν=0.001, T=2.0, amplitude=5.0

**Results:**
| m | sup_total | A_m1 | E_m | D_m | Trend |
|---|-----------|------|-----|-----|-------|
| 0.51 | 11.93 | 11.21 | 0.33 | 0.023 | STABLE |
| 0.53 | 11.72 | 11.01 | 0.33 | 0.023 | STABLE |
| 0.55 | 11.51 | 10.81 | 0.33 | 0.023 | STABLE |
| 0.57 | 11.31 | 10.61 | 0.32 | 0.022 | STABLE |
| 0.59 | 11.11 | 10.42 | 0.32 | 0.022 | STABLE |

**Conclusion:** Condition (1.4) BOUNDED. Higher values than Taylor-Green but stable.

---

### Experiment 3: Hou-Luo Candidate

**Parameters:** N=64, ν=0.0005, T=2.0

**Results:**
| m | sup_total | A_m1 | E_m | D_m | Trend |
|---|-----------|------|-----|-----|-------|
| 0.51 | 0.017 | 0.016 | 2.4e-4 | 1.4e-6 | N/A |
| 0.53 | 0.017 | 0.016 | 2.4e-4 | 1.3e-6 | N/A |
| 0.55 | 0.017 | 0.016 | 2.4e-4 | 1.3e-6 | N/A |
| 0.57 | 0.016 | 0.015 | 2.3e-4 | 1.3e-6 | N/A |
| 0.59 | 0.016 | 0.015 | 2.3e-4 | 1.3e-6 | N/A |

**Note:** Low values because the Hou-Luo IC requires much longer time to develop strong gradients. Early-time evolution only captured.

**Conclusion:** Condition (1.4) BOUNDED at observed times.

---

## Key Observations

### 1. A_{m₁} Dominates

In all experiments, the weighted velocity norm A_{m₁} contributes ~95% of the total.
- E_m contributes ~3-5%
- D_m contributes <1%

This suggests that for smooth solutions, the velocity L² bound in balls is the controlling factor.

### 2. m-Dependence

Higher m values give LOWER sup_total values:
- m=0.51: highest sup
- m=0.59: lowest sup

This is because larger m means smaller weight r^{-(2m-1)} at small r.

### 3. Stability Across ICs

All tested initial conditions show bounded (1.4) throughout their evolution:
- Taylor-Green: Known regular, confirms implementation
- Anti-parallel: More challenging, still bounded
- Hou-Luo: Blowup candidate, bounded at early times

---

## Limitations

1. **Resolution:** N=64 limits how small r we can probe reliably
2. **Time:** Short simulations may miss late-time blowup development
3. **Snapshot approximation:** Time integrals approximated from single snapshots

---

## Next Steps

### Higher Resolution Experiments
- Run N=128 or N=256 for better small-r behavior
- Track longer times (T=10+) for anti-parallel tubes

### Targeted Blowup Candidates
- Design ICs that maximize A_{m₁}/E_m ratio
- Study concentration near specific points

### Theoretical Analysis
- Attempt to prove E_m bounded from energy
- Derive pressure bound D_m from velocity

---

## Files Created

- `src/analysis/seregin_condition.py` - Core computation module
- `scripts/track_seregin_condition.py` - Tracking script with solver callbacks
- `results/seregin_tracking/` - JSON output files

---

## References

- arXiv:2507.08733 - Seregin's Type II exclusion theorem
- `docs/computations/seregin-formulas.md` - Exact formula definitions

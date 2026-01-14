# Iteration 15 Summary - Ralph Loop

**Date:** January 13, 2026
**Status:** CONTINUING (TYPE_II_RULED_OUT cannot be output)

---

## Key Accomplishments This Iteration

### 1. Implemented Seregin Condition (1.4) Computation

Created full computational framework:
- `src/analysis/seregin_condition.py` - Core module with weighted norm computations
- `scripts/track_seregin_condition.py` - Tracking script with solver callbacks

### 2. Ran Numerical Experiments

Tested condition (1.4) on three initial conditions:

| IC | sup(1.4) | A_{m₁} % | E_m % | D_m % | Status |
|---|----------|----------|-------|-------|--------|
| Taylor-Green | 5.5 | 96% | 4% | <1% | BOUNDED |
| Anti-parallel tubes | 11.9 | 94% | 3% | <1% | BOUNDED |
| Hou-Luo | 0.017 | 94% | 1% | <1% | BOUNDED |

**Key Finding:** A_{m₁} dominates in all cases (~95% of total).

### 3. Attempted Theoretical Lemmas

| Lemma | Target | Result |
|-------|--------|--------|
| 1 | E_m from energy | Works for smooth, fails at singularity |
| 2 | D_m from E_m | SUCCESS: D_m ≤ f(E_m) |
| 3 | A_{m₁} from CKN | Works at regular points only |

**Bottleneck Identified:** A_{m₁} near singular points.

### 4. Theoretical Conclusion

The bound A_{m₁} cannot be derived from known estimates because:
1. ε-regularity controls |u|³, not |u|²
2. Dimensional mismatch prevents direct application
3. Near singularities, ||u||_{L²(B(r))} may diverge

**This is exactly what Seregin assumes in condition (1.4).**

---

## Current State of Knowledge

```
Gap: α ∈ (1/2, 3/5), width 0.1

Self-similar (α = 1/2): RULED OUT
Non-self-similar (1/2 < α < 3/5): CONDITIONALLY excluded
    → Condition: (1.4) must hold
    → Bottleneck: A_{m₁} boundedness
α ≥ 3/5: RULED OUT by energy

NUMERICAL EVIDENCE: (1.4) bounded for all tested ICs
THEORETICAL PROOF: Missing control of A_{m₁} near singularities
```

---

## Files Created/Modified

### New Files
- `src/analysis/seregin_condition.py` - Computation module
- `scripts/track_seregin_condition.py` - Tracking script
- `docs/computations/seregin-numerical-experiments.md` - Experimental results
- `docs/computations/lemma-1-energy-weighted.md` - E_m analysis
- `docs/computations/lemma-2-pressure.md` - D_m analysis
- `docs/computations/lemma-3-velocity.md` - A_{m₁} analysis
- `docs/wip/iteration-15-summary.md` (this file)

### Modified Files
- `.claude/ralph-loop.local.md` (increment iteration)
- Results in `results/seregin_tracking/`

---

## Technical Insights

### Why A_{m₁} is Hard

```
A_{m₁}(v,r) = r^{-(2m-1)} sup_t ∫_{B(r)} |u|² dx
```

For m = 0.55, weight is r^{-0.1}.

To bound this as r → 0, need:
```
||u||_{L²(B(r))}² ≤ C r^{0.1+ε}
```

This requires L² mass in balls to vanish as r → 0, which is NOT guaranteed near singularities.

### The CKN Gap

CKN ε-regularity bounds:
```
r^{-2} ∫_{Q(r)} |u|³ ≤ ε  ⟹ regularity
```

But A_{m₁} involves |u|² with weight r^{-(2m-1)} < r^0.

The exponents don't match:
- CKN: |u|³/r² (dimension 0)
- A_{m₁}: |u|²/r^{0.1} (dimension ≈ 0.9)

No direct implication between them.

---

## Paths Forward

### Path A: Lorentz Space Interpolation
Use L^{p,q} spaces to bridge the dimensional gap.
**Difficulty:** HIGH

### Path B: Axisymmetric Specialization
Exploit geometric structure of axisymmetric flows.
**Difficulty:** MEDIUM

### Path C: Concentration Analysis
Study how mass concentrates near potential singularities.
**Difficulty:** HIGH

### Path D: New Functional Inequality
Find inequality connecting ||u||_{L²(B(r))} to known quantities.
**Difficulty:** VERY HIGH

---

## Promise Status

**TYPE_II_RULED_OUT: CANNOT BE OUTPUT**

The gap (1/2, 3/5) remains because:
1. Seregin's exclusion requires assumption (1.4)
2. (1.4) cannot be derived from known estimates
3. The bottleneck is A_{m₁} control near singularities

Numerical evidence suggests (1.4) holds but proof requires new mathematics.

---

## Next Iteration Plans

1. **Higher-resolution experiments:** N=128 to probe smaller r values
2. **Axisymmetric specialization:** Check if geometry helps bound A_{m₁}
3. **Lorentz space approach:** Investigate L^{2,∞} interpolation
4. **Literature search:** Recent work on concentration near NS singularities

---

## Additional Analysis: Seregin Rescaling Structure

**New document created:** `docs/computations/seregin-rescaling-structure.md`

### Key Findings on Ancient Euler Limit V

The rescaling procedure imposes four structural obstructions to bounded trajectories:

1. **Energy Obstruction:** V has infinite total energy (E^lambda ~ lambda^{2alpha-3} -> infinity)

2. **Concentration Obstruction:** The blowup core shrinks to a point in rescaled coordinates

3. **Asymptotic Obstruction:** V has power-law behavior |V| ~ |y|^{-alpha} at infinity

4. **Homogeneity Obstruction:** Inherited scaling V(mu y, mu^{1+alpha} tau) = mu^{-alpha} V(y, tau) incompatible with bounded invariant sets

### Implications for Vortex Rings

For axisymmetric Type II blowup:
- Vortex ring radius shrinks to zero in rescaled coordinates
- Closed streamlines around vortex core become singular
- No finite bounded configuration survives the limit

### Gap Remaining

Showing asymptotic constraints force V = 0 (not just ruling out bounded trajectories)

---

## References

- arXiv:2507.08733 - Seregin Type II exclusion
- CKN (1982) - Partial regularity
- Barker-Prange (2021) - Quantitative concentration
- Our analysis: lemma-1,2,3 documents
- New: seregin-rescaling-structure.md

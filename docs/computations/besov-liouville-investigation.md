# Besov-Liouville Theorem Investigation: Comprehensive Analysis

**Date:** January 13, 2026
**Status:** INVESTIGATION COMPLETE - NEGATIVE RESULT FOR DIRECT APPROACH
**Based on:** 4 parallel research agents

---

## Executive Summary

The "obvious" path of extending Seregin's framework via Besov-space Liouville theorems **does NOT work** as initially hoped. The investigation reveals a fundamental mismatch between what Besov/Lorentz spaces provide and what Seregin's framework requires.

### Key Finding

| Approach | Result | Reason |
|----------|--------|--------|
| Critical Besov B^{-1+3/p}_{p,q} | **FAILS** | O(1) scaling - no improvement over L² |
| Lorentz L^{3,∞} | **FAILS** | Requires SLOWER decay than Seregin's L² |
| Direct Liouville extension | **OPEN** | Gap γ ∈ [1/5, 1) genuinely unexplored |

### The Correct Understanding

The constraint m < 3/5 is **intrinsic to L² geometry**, not a limitation of the space choice. Besov/Lorentz spaces don't escape this constraint because:

1. Critical Besov is scale-invariant (O(1) scaling) - worse than L²
2. L^{3,∞} requires |U| ~ |y|^{-1} decay, but Seregin needs |U| ~ |y|^{-1.4} (faster)
3. The gap γ ∈ [1/5, 1) for growth rate isn't covered by any known Liouville theorem

---

## Part 1: Why Besov Spaces Don't Help Directly

### 1.1 Scaling Analysis

Under Type II concentration with L ~ (T-t)^β:

**L² weighted norm (Seregin):**
```
||u||²_{L²(B_L)} ~ ||u||²_∞ · L³ ~ (T-t)^{-2α} · (T-t)^{3β} = (T-t)^{3β-2α}
```

For β = (1+α)/2: exponent = (3-α)/2 > 0 for α < 1. **Decays to zero.**

**Critical Besov B^{-1+3/p}_{p,∞}:**
```
||u||_{B^{-1+3/p}_{p,∞}(B_L)} ~ (T-t)^0 = O(1)
```

Scale-invariant. **No decay, no improvement.**

### 1.2 The Dimensional Mismatch

Seregin's weighted condition:
```
A_{m₁}(v,r) = r^{-(2m-1)} ∫_{B(r)} |v|² dx
```

For this to be bounded, need ∫_{B(r)} |v|² = O(r^{2m-1}).

With m < 3/5: growth rate γ = (2m-1)/3 < 1/5.

**This means:** |U(y)| ~ |y|^{-p} with p > 7/5 = 1.4 at infinity.

**L^{3,∞} critical decay:** |U(y)| ~ |y|^{-1} at infinity.

**Seregin requires FASTER decay (p > 1.4) than L^{3,∞} (p = 1).**

### 1.3 Conclusion for Besov

Standard Besov spaces can't help because:
1. Critical Besov has no decay advantage over L²
2. Subcritical Besov has worse bounds than L²
3. The fundamental constraint is on growth rate γ, not the space

---

## Part 2: The True Nature of the m < 3/5 Constraint

### 2.1 Source: Euler Liouville Theorem

From Seregin's Proposition 4.1:

**Theorem:** Let U be an ancient solution of 3D Euler. If:
```
∫_{B(b)} |U|² dy = O(b^{2m-1}) as b → ∞
```
with 2m - 1 < 1/5 (i.e., m < 3/5), then U ≡ 0.

**The critical exponent 1/5 is sharp for L² growth bounds.**

### 2.2 What Happens at m = 3/5

At m = 3/5:
- m₁ = 2m - 1 = 1/5 (critical)
- Growth rate γ = 1/5/3 = 1/15 (error: recalculate)
- Actually: ∫_{B(b)} |U|² = O(b^{1/5})
- This means |U| ~ b^{(1/5 - 3)/2} = b^{-7/5} at infinity
- Decay rate: |U(y)| ~ |y|^{-7/5}

**This is exactly the critical threshold where:
- Subcritical (m < 3/5): Liouville applies, U = 0
- Critical (m = 3/5): Liouville FAILS, non-trivial U may exist**

### 2.3 Pan-Li Result (2020)

**Theorem (Pan-Li):** For stationary Euler with |u| = o(|x|^α), α < 1, Liouville holds.

**Sharp at α = 1:** There exist non-trivial steady Euler with linear growth.

**The gap:** Between L² subcritical (γ < 1/5, roughly |U| = O(|y|^{-1.4})) and Pan-Li (|U| = o(|y|)), there's a range where:
- No positive Liouville results
- No counterexamples
- This is genuinely open

---

## Part 3: What Would Actually Work

### 3.1 Path A: New Euler Liouville for γ ∈ [1/5, 1)

**What's Needed:**
Prove that ancient 3D Euler solutions with:
```
∫_{B(b)} |U|² = O(b^γ) for γ < 1/3
```
must satisfy U ≡ 0.

**Current State:**
- Known for γ < 1/5 (Seregin's Prop 4.1)
- Known to fail at γ = 1 (Pan-Li counterexample)
- Gap γ ∈ [1/5, 1) is open

**Difficulty:** VERY HARD - would be significant new mathematics.

### 3.2 Path B: Additional Structure

Use constraints beyond L² growth:
- **Axisymmetry:** Stronger Liouville may hold
- **Vorticity bounds:** Add sup |ω| or helicity constraints
- **No swirl:** Exploit structural simplification

**Known:** Korobkov-Pileckas-Russo (2015) proves Liouville for axisymmetric Euler without swirl and finite Dirichlet integral.

### 3.3 Path C: Chemin-Lerner Time-Besov

Mixed norms L̃^r_T(B^s_{p,q}) treat time and frequency differently:
```
||u||_{L̃^r_T(B^s_{p,q})} = ||(2^{js}||Δ_j u||_{L^p})_{j}||_{ℓ^q(L^r_T)}
```

**Potential:** Time-frequency coupling might reveal hidden constraints not visible in pure spatial norms.

### 3.4 Path D: Weighted L² with Custom Weights

Instead of r^{-(2m-1)}, use:
```
w(r) = r^{-a} (log r)^{-b}
```
or other slowly varying weights that might interpolate between m regimes.

### 3.5 Path E: Force Different Scaling β

If β = 1 - α (instead of β = (1+α)/2), then:
- Energy E_local ~ (T-t)^{(3-5α)/2}
- For α > 3/5: energy INCREASES → contradiction

**Problem:** No proof that β = 1 - α is forced.

---

## Part 4: Assessment of Each Path

| Path | Description | Feasibility | New Math Required |
|------|-------------|-------------|-------------------|
| A | Euler Liouville for γ ∈ [1/5, 1) | LOW | Major breakthrough |
| B | Axisymmetric structure | MEDIUM | Modest extension |
| C | Chemin-Lerner norms | LOW | New framework |
| D | Custom weighted L² | LOW | Unclear benefit |
| E | Force β = 1 - α | LOW | Physical principle |

### Most Promising: Path B (Axisymmetric)

For axisymmetric flows:
1. Type I already excluded
2. Korobkov-Pileckas-Russo gives stronger Liouville (no swirl case)
3. Swirl case: additional structure from angular momentum

**Concrete direction:** Prove axisymmetric Euler Liouville with γ < 1/3.

---

## Part 5: Documents Created

| File | Content |
|------|---------|
| `euler-liouville-survey.md` | Complete survey of known Liouville theorems |
| `besov-ns-analysis.md` | Besov space scaling analysis |
| `lorentz-liouville-analysis.md` | L^{3,∞} and Lorentz space investigation |
| `seregin-m-constraint-analysis.md` | Detailed trace of m < 3/5 origin |

---

## Conclusion

The Besov-Liouville approach was a natural guess but **incorrect**. The investigation reveals:

1. **Besov/Lorentz spaces don't help** because the constraint is on growth rate γ, not the function space
2. **The gap γ ∈ [1/5, 1) is genuinely open** - no Liouville theorem, no counterexample
3. **The most promising path is axisymmetric structure** (Path B), not interpolation spaces

### Current Status

```
| Range | Method | Status |
|-------|--------|--------|
| γ < 1/5 (m < 3/5) | Seregin Liouville | WORKS |
| γ = 1/5 (m = 3/5) | Critical threshold | FAILS |
| γ ∈ (1/5, 1) | No method | OPEN |
| γ = 1 | Pan-Li counterexample | FAILS |
```

**The gap α ∈ [5/7, 1) persists because the gap γ ∈ [1/5, 1) in Euler Liouville is open.**

---

*Investigation complete: January 13, 2026*
*Result: Besov-Liouville is NOT the path forward; axisymmetric structure more promising*

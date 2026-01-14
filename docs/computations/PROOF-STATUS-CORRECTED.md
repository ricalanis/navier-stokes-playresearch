# Proof Status: Axisymmetric Navier-Stokes Global Regularity

**Date:** January 13, 2026
**Status:** CONDITIONAL - Critical Gaps Identified

---

## Executive Summary

After rigorous review by six independent analysis agents, the claimed "unconditional proof" of axisymmetric Navier-Stokes global regularity has been found to contain **several critical errors and gaps**.

### Verdict: The paper's main claims are NOT VALID as stated.

---

## Gap Summary

| Gap | Issue | Severity | Status |
|-----|-------|----------|--------|
| **Gap 1** | Sign control (Prop 4.4) is FALSE | HIGH | Alternative formulation available |
| **Gap 2** | Liouville boundary η → 0 not justified | CRITICAL | No current fix |
| **Gap 3** | α_c = 0.5, NOT 0.82 | CRITICAL | Backward dispersion fails |
| **Gap 4** | Energy formula E ~ (T-t)^{3-5α} is WRONG | MEDIUM | Corrected to (3-α)/2 |

---

## Detailed Analysis

### Gap 1: Sign Control (Proposition 4.4)

**Original Claim:** "For vorticity to concentrate toward the axis (r → 0), the radial velocity must satisfy u^r < 0 in the concentration region."

**Finding:** This claim is **FALSE**.

The vorticity equation reveals a fundamental contradiction:
- Transport toward axis requires u^r < 0
- Stretching amplification requires u^r > 0
- Both cannot hold at the same point

**Resolution:** The self-defeating mechanism works through η = ω^θ/r geometry, NOT through sign control of u^r. The maximum principle ||η||_∞ bounded + geometric constraint ω^θ = r·η prevents blowup at r = 0.

**Impact:** Low - proof can be reformulated using η geometry.

---

### Gap 2: Liouville Boundary Condition (Theorem 6.5)

**Original Claim:** The Enhanced Liouville theorem assumes η → 0 at infinity for the ancient Euler solution arising from Type II rescaling.

**Finding:** This boundary condition is **NOT JUSTIFIED**.

Under Type II rescaling V^λ(y,τ) = λ^α u(λy, T + λ^{1+α}τ):
- The limit extracts behavior near the singularity
- Spatial infinity in original coordinates is NOT mapped to infinity in rescaled coordinates
- The ancient Euler limit's behavior at |y| → ∞ is NOT determined by original solution's decay

**Resolution Attempts:**
1. Direct decay estimates through rescaling - HARD, unproven
2. Strengthen Liouville without pointwise decay - Requires new theory
3. Exploit diverging ν_eff → ∞ - MOST PROMISING but unproven

**Impact:** CRITICAL - The Liouville chain breaks without this condition.

---

### Gap 3: Critical Exponent α_c (Backward Dispersion)

**Original Claim:** α_c ≈ 0.82 ensures backward dispersion for Type II range (1/2, 3/5).

**Finding:** The correct value is **α_c = 0.5**, not 0.82.

The energy evolution for ancient self-similar Euler:
```
dE/dτ = γE where γ = (3β/2 - 2α)
```

With β = 1/(1+α):
```
γ = 0 ⟺ 4α² + 4α - 3 = 0 ⟺ α = 0.5
```

For α > 0.5: γ < 0, meaning energy DECREASES forward (INCREASES backward).

**Problem:** The backward energy growth argument FAILS for α = 0.5 exactly, and provides no coverage for Type II rates α > 0.5.

**Impact:** CRITICAL - The backward dispersion argument does NOT cover the Type II range.

---

### Gap 4: Energy Scaling Formula

**Original Claim:** E(t) ~ (T-t)^{3-5α}

**Finding:** This formula is **INCORRECT**.

Correct derivation:
```
E ~ |u|² · L³ ~ (T-t)^{-2α} · (T-t)^{3β}
With β = (1+α)/2:
E ~ (T-t)^{-2α + 3(1+α)/2} = (T-t)^{(3-α)/2}
```

| α | Incorrect (3-5α) | Correct (3-α)/2 |
|---|------------------|-----------------|
| 0.5 | 0.5 | 1.25 |
| 0.55 | 0.25 | 1.225 |
| 0.6 | 0.0 | 1.2 |

**Impact:** Medium - Some arguments need recalculation but structure may survive.

---

## What IS Valid

Despite the gaps, several parts of the analysis remain valid:

### 1. Type I Exclusion (VALID)
- Theorems 3.1, 3.2: No forward/backward self-similar profiles in L^{3,∞}
- Corollary 3.3: Type I blowup excluded
- Based on NRŠ, KNSS, Chae-Wolf - well-established

### 2. η Conservation (VALID)
- Proposition 4.1: D_t η = ν L[η] is correct
- Corollary 4.2: Maximum principle ||η||_∞ ≤ ||η_0||_∞ is correct
- Proposition 4.3: ω^θ ≤ r·M is correct

### 3. Energy Constraint α ≥ 3/5 (VALID with correction)
- Theorem 5.2: Energy inequality excludes α ≥ 3/5
- Uses corrected formula E ~ (T-t)^{(3-α)/2}
- Dissipation divergence at α = 3/5 is still contradictory

### 4. Effective Viscosity for Swirl (VALID)
- Proposition 6.1: ν_eff → ∞ for α > 1/2 is correct
- Theorem 6.2: Swirl decay under diverging viscosity likely correct
- Corollary 6.3: Blowup limit is asymptotically swirl-free

### 5. Concentration Scale (VALID)
- β = (1+α)/2 is correct and now properly derived

---

## Current Status by Blowup Type

| Blowup Type | Rate | Mechanism | Status |
|-------------|------|-----------|--------|
| Type I | α = 1/2 | Profile non-existence | **EXCLUDED** ✓ |
| Type II no-swirl | α ∈ (1/2, 3/5) | η conservation | **CONDITIONAL** (needs Liouville) |
| Type II with-swirl | α ∈ (1/2, 3/5) | Effective viscosity | **CONDITIONAL** (same gaps) |
| Type II | α ≥ 3/5 | Energy inequality | **EXCLUDED** ✓ |

---

## What Would Close the Gaps

### To Fix Gap 2 (Liouville Boundary):
1. Prove decay estimates propagate through rescaling
2. Develop Liouville theorem for L^p growth (not pointwise decay)
3. Work directly with viscous equation using diverging ν_eff

### To Fix Gap 3 (α_c):
1. Find alternative backward dispersion mechanism
2. Use different rescaling convention (β = 1 gives α_c = 0.75)
3. Develop direct Liouville for ancient Euler without dispersion argument

### Alternative Approaches:
1. Seregin's condition (1.4) - prove it's automatic (current plan file)
2. Vorticity direction constraints (Constantin-Fefferman)
3. Topological obstruction methods
4. Computer-assisted bounds

---

## Honest Assessment

**The axisymmetric Navier-Stokes global regularity problem is NOT SOLVED.**

What we have achieved:
1. Complete Type I exclusion (valid)
2. Partial Type II understanding with identified gaps
3. Clear identification of what new mathematics is needed
4. Multiple potential paths forward

What remains:
1. Closing the Liouville boundary gap
2. Finding alternative to backward dispersion
3. Rigorous Euler Liouville for ancient solutions

**The gap (1/2, 3/5) for axisymmetric NS remains at the mathematical frontier.**

---

## Files Created by Review Agents

| File | Content |
|------|---------|
| `concentration-scale-derivation.md` | Rigorous β = (1+α)/2 derivation |
| `energy-scaling-correction.md` | Correct formula E ~ (T-t)^{(3-α)/2} |
| `critical-alpha-resolution.md` | α_c = 0.5 not 0.82 |
| `liouville-boundary-analysis.md` | Gap 2 analysis and potential fixes |
| `sign-control-proof.md` | Prop 4.4 is false, η geometry works |
| `backward-dispersion-review.md` | Gap 3 detailed analysis |

---

*Document created: January 13, 2026*
*Status: Critical review complete, proof conditional*

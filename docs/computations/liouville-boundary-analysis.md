# Liouville Theorem Boundary Condition Analysis

## Critical Issue Investigation

**Date:** January 13, 2026
**Status:** CRITICAL GAP IDENTIFIED
**Problem:** The Enhanced Liouville Theorem (Theorem 6.5) requires eta -> 0 at infinity, but this boundary condition is NOT established from the Type II rescaling limit.

---

## Executive Summary

This document analyzes whether the boundary condition `eta -> 0 at infinity` is justified in the proof of the Enhanced Liouville theorem for axisymmetric Navier-Stokes.

**CONCLUSION:** The boundary condition is **NOT automatically justified** from the rescaling procedure. This represents a **genuine gap** in the current proof that requires additional work to close.

| Component | Status |
|-----------|--------|
| Type II rescaling preserves eta | VERIFIED |
| Decay of eta at infinity from initial data | NOT ESTABLISHED |
| Decay preserved by NS evolution | CONDITIONAL |
| Decay preserved by rescaling limit | **GAP - NOT PROVEN** |
| Alternative Liouville theorems available | PARTIAL |

---

## 1. Analysis of the Rescaling

### 1.1 Type II Rescaling Setup

For Type II blowup at time T with rate alpha in (1/2, 3/5), define the rescaled solution:

```
V^lambda(y, tau) = lambda^alpha u(lambda y, T + lambda^{1+alpha} tau)
```

where:
- lambda -> 0 extracts the blowup limit
- tau in (-infinity, 0] is the rescaled backward time
- y = x/lambda is the spatial rescaling

### 1.2 Behavior of eta Under Rescaling

The reduced vorticity is defined as:
```
eta = omega^theta / r
```

Under the rescaling, the vorticity transforms as:
```
Omega^lambda(y, tau) = lambda^{alpha+1} omega(lambda y, T + lambda^{1+alpha} tau)
```

In cylindrical coordinates with y = (rho, z) where rho = r/lambda:
```
eta_rescaled(rho, z, tau) = Omega^theta_lambda(y, tau) / rho
                          = lambda^{alpha+1} omega^theta(lambda rho, lambda z, ...) / rho
                          = lambda^{alpha+1} * (r/lambda) * eta(r, z, t) / rho
                          = lambda^{alpha+1} * eta(r, z, t)
```

**Critical Observation:** The rescaled eta is:
```
eta_rescaled = lambda^{alpha+1} * eta_original
```

Since lambda -> 0 and alpha > 1/2, we have lambda^{alpha+1} -> 0.

### 1.3 What This Implies

**Case A: Pointwise Decay**
If eta_original is bounded at each point, then eta_rescaled -> 0 pointwise as lambda -> 0.

**BUT:** The limit is taken at y = x/lambda, so as lambda -> 0:
- Fixed y corresponds to x = lambda * y -> 0
- We're zooming into the blowup point
- Information about eta at infinity (large |x|) is NOT captured by small lambda limits

**Case B: Decay at Spatial Infinity**
The rescaling sends:
- Small |x| (near blowup point) -> finite |y|
- Large |x| (spatial infinity) -> |y| = infinity as lambda -> 0... but this limit is singular

### 1.4 The Fundamental Problem

**The Type II rescaling does NOT automatically produce a limit with eta -> 0 at infinity because:**

1. The rescaling zooms into the singularity point
2. Spatial infinity in original coordinates is NOT mapped to spatial infinity in rescaled coordinates in any well-defined way
3. The limit U(y, tau) is an ancient solution on R^3 x (-infinity, 0], but its behavior at |y| -> infinity is determined by the STRUCTURE of the limit, not directly from the original solution's decay

**Key Question:** Does the blowup limit U automatically satisfy eta_U -> 0 as |y| -> infinity?

**Answer:** This is NOT proven by the rescaling procedure alone.

---

## 2. Decay from Initial Data

### 2.1 Initial Data Class

The standard assumption is u_0 in L^2(R^3) with:
```
||u_0||_{L^2} < infinity (finite energy)
```

For axisymmetric initial data with additional regularity (e.g., Schwartz class or compact support):
```
omega_0(x) -> 0 as |x| -> infinity (pointwise or in L^p)
eta_0(x) = omega^theta_0(x) / r -> 0 as |x| -> infinity
```

### 2.2 Is Decay Preserved by NS Evolution?

**For Euler (inviscid):**
- eta is materially conserved: D_t eta = 0
- If eta_0 -> 0 at infinity, this is preserved along particle trajectories
- **But:** Particles can move, so decay at infinity depends on particle dispersion

**For Navier-Stokes (viscous):**
- eta satisfies: D_t eta = nu * L[eta] where L is a parabolic operator
- Viscous diffusion spreads the vorticity
- Maximum principle: ||eta(t)||_{L^infty} <= ||eta_0||_{L^infty}
- Decay at infinity is generally preserved by parabolic regularization

**Conclusion:** For NS, if eta_0 has good decay, eta(t) maintains decay for t < T.

### 2.3 Is Decay Preserved by the Rescaling Limit?

**This is the crux of the problem.**

Even if eta(x, t) -> 0 as |x| -> infinity for each t < T, the rescaled limit:
```
U = lim_{lambda -> 0} V^lambda
```
is constructed by zooming into the singularity. The decay properties at spatial infinity are NOT directly inherited.

**Technical Issue:**
- The limit U is extracted via compactness arguments (e.g., Arzela-Ascoli on compact sets)
- Compactness on R^3 requires uniform estimates including at infinity
- Standard compactness gives limits on compact subsets, with no control at infinity

**What's Needed:**
- Uniform decay estimates: eta_rescaled(y, tau) <= C / (1 + |y|^gamma) uniformly in lambda
- Such estimates would require specific structure of the blowup

---

## 3. What KNSS (2009) and Related Works Assume

### 3.1 Koch-Nadirashvili-Seregin-Sverak (2009)

**Reference:** "Liouville theorems for the Navier-Stokes equations and applications," Acta Math. 203 (2009), 83-105.

**Their Setting:**
- Ancient mild solutions of NS: u exists for t in (-infinity, 0]
- **Assumption:** Bounded solutions: ||u||_{L^infty(R^3 x (-infinity, 0])} < infinity

**Key Point:** KNSS does NOT assume eta -> 0 at infinity separately. Instead:
- Boundedness implies decay at infinity for each time slice (by elliptic regularity)
- The viscous smoothing provides additional decay estimates

**Their Liouville Theorem:**
For bounded ancient axisymmetric NS without swirl, u = constant (hence = 0 with finite energy).

### 3.2 Seregin (2025) - Type II Framework

**Reference:** arXiv:2507.08733, "A note on certain scenarios of Type II blowups..."

**Seregin's Approach:**
- Rescales to produce ancient EULER limit (viscosity vanishes in the limit)
- Requires condition (1.4): weighted L^2 bounds at all scales
- Under (1.4), applies Liouville for ancient Euler

**Seregin's Euler Liouville (Proposition 4.1):**
For m in (1/2, 3/5), ancient Euler solutions U with:
```
sup_{b > 0} b^{-(2m-1)} integral_{B(b)} |U|^2 dy < infinity
```
must satisfy U = 0.

**What's Assumed:**
Seregin's Liouville uses L^2 growth bounds, NOT pointwise eta decay at infinity.

### 3.3 Pan-Li (2020) - Sublinear Growth

**Reference:** "Liouville theorem of axially symmetric Navier-Stokes equations with growing velocity at infinity"

**Their Extension:**
- For NS (not Euler)
- Allow |u(x)| = o(|x|^alpha) with alpha < 1 (sublinear growth)
- Conclude u = constant

**Limitation:** This is for Navier-Stokes, not for the inviscid Euler limit arising from Type II rescaling.

---

## 4. Alternative Approaches Without Pointwise Decay

### 4.1 Approach A: Use L^2 Growth Bounds Instead

**Modification:** Replace "eta -> 0 at infinity" with:
```
integral_{B(R)} eta^2 r^3 dr dz = O(R^gamma) with gamma < 1
```

**Advantage:** L^2 bounds are more directly related to energy estimates and may be provable from the rescaling.

**Status:** This is essentially what Seregin's condition (1.4) captures.

**Gap:** Need to verify (1.4) is automatic for Type II blowup limits.

### 4.2 Approach B: Trajectory-Based Liouville

**Alternative Theorem Statement:**
For ancient axisymmetric Euler without swirl, if:
1. eta is materially conserved (always true)
2. All backward trajectories disperse: |X(tau)| -> infinity as tau -> -infinity
3. eta satisfies integral bounds (not pointwise decay)

Then U = 0.

**Status of Condition 2:** NOT PROVEN

This is the "dispersion hypothesis" identified in the enhanced Liouville final analysis. The exact same gap appears here.

### 4.3 Approach C: Energy-Based Liouville

**Energy Liouville Attempt:**
Use:
- Energy conservation for Euler: integral |U|^2 = constant
- Enstrophy control: integral |omega|^2 <= C (for axisymmetric no swirl)
- Material conservation of eta

**Gap:** Energy and enstrophy bounds don't force U = 0 without decay at infinity or dispersion.

### 4.4 Approach D: Return to NS (Keep Viscosity)

**Alternative Path:**
Instead of taking the Euler limit (nu -> 0), keep the NS structure with rescaled viscosity:
```
nu_eff = nu * lambda^{1-2alpha} -> infinity (since alpha > 1/2)
```

**Observation:** The effective viscosity DIVERGES in the Type II rescaling for alpha > 1/2.

**Implication:** The rescaled NS becomes:
```
partial_tau U + (U . nabla) U = -nabla P + nu_eff Delta U
```
with nu_eff -> infinity.

**Potential:** Strong viscosity should force U -> 0 (extreme dissipation).

**Gap:** Need rigorous analysis of the singular limit nu_eff -> infinity.

---

## 5. Proposed Fixes

### 5.1 Fix Option 1: Prove Uniform Decay Estimates

**Claim to Prove:**
For Type II blowup with rate alpha in (1/2, 3/5), the rescaled vorticity satisfies:
```
|eta_lambda(y, tau)| <= C / (1 + |y|)^{1+epsilon} uniformly in lambda, tau
```

**Approach:**
1. Use energy bounds on the original solution: E(t) <= E_0
2. Derive vorticity decay from energy concentration structure
3. Track decay through rescaling

**Difficulty:** HIGH - requires detailed understanding of blowup structure

### 5.2 Fix Option 2: Strengthen the Liouville Theorem

**Modified Liouville:**
Prove that for ancient axisymmetric Euler without swirl with:
- Sublinear L^2 growth: integral_{B(R)} |U|^2 = O(R^gamma), gamma < 1
- NO assumption on eta at infinity

Then U = 0.

**Approach:** Combine material conservation of eta with:
- Birkhoff ergodic theorem for bounded trajectories
- Energy-vorticity identities
- Structural constraints from axisymmetry

**Difficulty:** MEDIUM-HIGH - requires new mathematical techniques

### 5.3 Fix Option 3: Use Diverging Effective Viscosity

**Modified Argument:**
For alpha > 1/2, the rescaled NS has nu_eff = nu * lambda^{1-2alpha} -> infinity.

**Key Steps:**
1. At large nu_eff, solutions are controlled by heat-kernel decay
2. Heat kernel forces exponential spatial decay
3. This decay provides the missing boundary condition

**Advantage:** Uses the NS structure rather than going to Euler limit

**Status:** Promising but needs rigorous development

### 5.4 Fix Option 4: Exclude Bounded Trajectories Directly

**Direct Proof:**
Show that for ancient Euler arising from Type II rescaling:
- No bounded backward trajectories exist
- All particles disperse as tau -> -infinity

**Approach:**
1. Use specific structure of blowup limits (concentration at the axis)
2. Analyze flow geometry near concentration regions
3. Show incompatibility with bounded recirculating flow

**Difficulty:** MEDIUM - most geometrically natural approach

---

## 6. Literature Gaps Identified

### 6.1 Missing Result: Euler Liouville Without Pointwise Decay

**Current State:**
- KNSS handles bounded ancient NS (not Euler)
- Pan-Li handles sublinear NS (not Euler)
- Seregin handles ancient Euler with L^2 bounds (Proposition 4.1)

**Gap:** No unconditional Liouville for ancient axisymmetric Euler without swirl with only energy/enstrophy bounds

### 6.2 Missing Result: Decay Inheritance from Rescaling

**Current State:**
- Type II rescaling produces ancient solutions
- Compactness gives limits on compact sets
- No result on decay at infinity for rescaling limits

**Gap:** No theorem stating that if u(x, t) decays at infinity, then rescaling limit U(y, tau) also decays at infinity

### 6.3 Missing Result: Trajectory Dispersion

**Current State:**
- Material conservation of eta is well-established
- Dispersion implies triviality (proven)
- No proof that dispersion occurs

**Gap:** Backward dispersion is a HYPOTHESIS, not a theorem

---

## 7. Summary of the Gap

### 7.1 The Exact Obstruction

**Theorem 6.5 (Enhanced Liouville) as stated requires:**
1. Ancient axisymmetric Euler without swirl
2. Sublinear L^2 growth (gamma < 1)
3. **eta -> 0 at spatial infinity**

**The gap is in condition 3:**
- This is assumed, not derived
- The Type II rescaling procedure does NOT establish this
- Current proof is CONDITIONAL on this assumption

### 7.2 Impact on the Full Proof

If the boundary condition cannot be established:
- The Liouville chain breaks at Theorem 6.5
- Type II exclusion for alpha in (1/2, 3/5) is NOT completed
- Global regularity claim is NOT proven

### 7.3 Assessment of Severity

**Severity: HIGH**

This is not a minor technical point. The boundary condition eta -> 0 at infinity is essential because:
1. Material conservation (D_t eta = 0) only forces eta = 0 IF we can trace backward to infinity
2. Without decay at infinity, bounded invariant regions could carry nonzero eta
3. Hill's spherical vortex is a counterexample (bounded, eta != 0 inside)

---

## 8. Recommendations

### 8.1 Immediate Actions

1. **Acknowledge the gap** in any paper claiming the full result
2. **State the conditional theorem clearly:** "Under the assumption that eta -> 0 at infinity..."
3. **Pursue Fix Options** in parallel

### 8.2 Most Promising Resolution

**Fix Option 3 (Diverging Viscosity)** appears most promising because:
- It uses NS structure directly (doesn't require Euler limit)
- Infinite effective viscosity provides strong decay
- Heat kernel estimates are well-established

### 8.3 Backup Approach

**Fix Option 4 (Exclude Bounded Trajectories)** as backup:
- More geometric and intuitive
- Specific to axisymmetric structure
- Could provide stronger insight into blowup geometry

---

## 9. Conclusion

**The boundary condition eta -> 0 at infinity is NOT justified from the Type II rescaling limit.**

This represents a genuine gap in the current proof of global regularity for axisymmetric Navier-Stokes. The gap is at the level of the Enhanced Liouville theorem, which is used to conclude that the ancient Euler limit must be trivial.

**Possible Resolutions:**
1. Prove uniform decay estimates for eta through rescaling (Hard)
2. Strengthen Liouville theorem to not require pointwise decay (Medium-Hard)
3. Use diverging effective viscosity to provide decay (Promising)
4. Directly exclude bounded trajectories (Geometric approach)

**Current Status:** CONDITIONAL PROOF
The full result depends on either:
- Assuming eta -> 0 at infinity (unjustified)
- Completing one of the proposed fixes

---

## References

1. Koch, Nadirashvili, Seregin, Sverak. "Liouville theorems for the Navier-Stokes equations and applications." Acta Math. 203 (2009), 83-105.

2. Seregin, G. "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations." arXiv:2507.08733 (July 2025).

3. Pan, X., Li, Z. "Liouville theorem of axially symmetric Navier-Stokes equations with growing velocity at infinity." NL Analysis RWA 52 (2020).

4. Korobkov, Pileckas, Russo. "The Liouville Theorem for the Steady-State Navier-Stokes Problem for Axially Symmetric 3D Solutions in Absence of Swirl." J. Math. Fluid Mech. 17 (2015), 287-293.

---

*Document created: January 13, 2026*
*Analysis Status: Gap identified, resolution paths proposed*
*Proof Status: CONDITIONAL pending boundary condition justification*

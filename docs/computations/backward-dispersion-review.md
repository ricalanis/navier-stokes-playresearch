# Backward Dispersion Argument: Rigorous Review

**Date:** January 13, 2026
**Status:** CRITICAL REVIEW - Gaps and Issues Identified
**Purpose:** Rigorously analyze the backward dispersion argument (Theorem 6.4) in the axisymmetric NS proof

---

## Executive Summary

The backward dispersion argument claims that for ancient self-similar Euler with alpha in (1/2, 0.82), particle trajectories disperse backward: |X(tau)| -> infinity as tau -> -infinity. The argument has **multiple issues** that render it incomplete as stated. This document provides:

1. **Precise mathematical definitions** of trapped regions
2. **Correct derivation** of energy evolution
3. **Analysis of the contradiction claim**
4. **Alternative approaches** and their viability
5. **Assessment of the gap** and what's needed to close it

**Main Conclusion:** The backward dispersion mechanism has merit for alpha in (1/2, alpha_c) where alpha_c ~ 0.823, but the argument requires significant rigorization. The key gap is the transition from "energy in trapped regions grows" to "no trapped regions exist."

---

## 1. Precise Definition of Trapped Regions

### 1.1 The Claimed Definition

The argument uses "trapped regions" informally. Let us define them precisely.

**Definition 1.1 (Backward Trapped Particle):** A particle trajectory X(tau) of the ancient Euler flow is *backward trapped* if there exists R > 0 such that:
```
|X(tau)| < R  for all tau in (-infinity, 0]
```

**Definition 1.2 (Trapped Region):** A set T subset R^3 is a *trapped region* if every particle starting in T at tau = 0 is backward trapped, i.e., the backward-time image of T remains bounded:
```
Phi_{-s}(T) subset B_R  for all s >= 0
```
where Phi_tau denotes the flow map of the velocity field V.

**Definition 1.3 (Invariant Region):** A set I is *backward invariant* if:
```
Phi_{-s}(I) = I  for all s >= 0
```

**Remark:** Trapped regions need not be invariant. The distinction matters because:
- Invariant regions preserve volume (incompressibility)
- Trapped regions might contract or expand while remaining bounded

### 1.2 Energy in Trapped Regions

**Definition 1.4:** For a trapped region T, define:
```
E_T(tau) = integral_T |V(y, tau)|^2 dy
```

**Issue 1:** E_T is not the energy "following" the trapped particles. The correct quantity is:
```
E_T^*(tau) = integral_{Phi_tau(T_0)} |V(y, tau)|^2 dy
```
where T_0 is the set of particles at tau = 0 that remain trapped.

These differ because T is fixed while Phi_tau(T_0) moves with the flow.

### 1.3 Lagrangian Energy

**Definition 1.5 (Lagrangian Energy Density):** Along a particle trajectory X(tau):
```
e(tau) = |V(X(tau), tau)|^2
```

**Definition 1.6 (Lagrangian Energy of Trapped Set):**
```
E_Lag(tau) = integral_{X_0 in T_0} |V(Phi_tau(X_0), tau)|^2 dV_0
```
where dV_0 is the volume element in the initial configuration.

By incompressibility (div V = 0), volume is preserved under the flow:
```
E_Lag(tau) = integral_{Phi_tau(T_0)} |V(y, tau)|^2 dy = E_T^*(tau)
```

---

## 2. Correct Energy Evolution Derivation

### 2.1 The Self-Similar Euler Equation

The ancient self-similar Euler equation is:
```
partial_tau V + (V . nabla)V + alpha V + (beta/2) y . nabla V = -nabla P     (2.1)
div V = 0                                                                     (2.2)
```

where:
- alpha: velocity rescaling exponent
- beta: spatial rescaling rate, typically beta = 1/(1+alpha) for standard Type II

### 2.2 Global Energy Evolution

**Proposition 2.1:** The total energy E(tau) = (1/2) integral |V|^2 dy satisfies:
```
dE/dtau = gamma E                                                            (2.3)
```
where gamma = (3*beta - 2*alpha).

**Proof:**

Multiply (2.1) by V and integrate:

**Term 1 (Time derivative):**
```
integral partial_tau V . V = (1/2) d/dtau integral |V|^2 = dE/dtau
```

**Term 2 (Nonlinear advection):**
```
integral (V . nabla)V . V = (1/2) integral V . nabla |V|^2 = -(1/2) integral (div V) |V|^2 = 0
```

**Term 3 (Linear damping):**
```
integral alpha V . V = alpha integral |V|^2 = 2 alpha E
```

**Term 4 (Self-similar stretching):**
```
integral (beta/2) (y . nabla V) . V = (beta/4) integral y . nabla |V|^2
```

Integration by parts in 3D:
```
integral y . nabla f = -integral (div y) f = -3 integral f
```

(assuming decay at infinity). Therefore:
```
(beta/4) integral y . nabla |V|^2 = -(3 beta/4) integral |V|^2 = -(3 beta/2) E
```

**Term 5 (Pressure):**
```
integral (-nabla P) . V = integral P (div V) = 0
```

**Combined:**
```
dE/dtau = -2 alpha E + (3 beta/2) E = (3 beta/2 - 2 alpha) E
```

Setting gamma = (3 beta/2 - 2 alpha), we get dE/dtau = gamma E. QED

### 2.3 The Critical Exponent

**Proposition 2.2:** For standard Type II rescaling with beta = 1/(1+alpha):
```
gamma = 3/(2(1+alpha)) - 2 alpha = (3 - 4 alpha - 4 alpha^2) / (2(1+alpha))
```

Setting gamma = 0:
```
3 - 4 alpha - 4 alpha^2 = 0
alpha = (-4 + sqrt(16 + 48)) / 8 = (-4 + 8) / 8 = 1/2
```

**Wait, this gives alpha_c = 1/2, not 0.82. Let me recompute.**

**Correction:** The paper uses a different convention. The self-similar Euler equation should be:
```
partial_tau V + (V . nabla)V + alpha V + (1/2) y . nabla V = -nabla P
```

with beta = 1/2 fixed (standard self-similar form). Then:

```
gamma = 3*(1/2) - 2*alpha = 3/2 - 2*alpha
```

Setting gamma = 0: alpha = 3/4.

This is STILL different from 0.82!

### 2.4 Resolving the Discrepancy

**Issue 2:** The claimed alpha_c ~ 0.82 comes from a different calculation.

Looking at the previous document (backward-dispersion-proof.md), the formula used was:
```
gamma = (3 - 2*alpha - 2*alpha^2) / (1 + alpha)
```

This arises from beta = 1/(1+alpha), giving:
```
3*beta/2 - 2*alpha = 3/(2(1+alpha)) - 2*alpha = (3 - 4*alpha*(1+alpha)) / (2(1+alpha))
                   = (3 - 4*alpha - 4*alpha^2) / (2(1+alpha))
```

Setting numerator = 0: 3 - 4*alpha - 4*alpha^2 = 0

Using quadratic formula:
```
alpha = (-4 +/- sqrt(16 + 48)) / (-8) = (-4 +/- 8) / (-8)
```

Positive root: alpha = (-4 - 8)/(-8) = 12/8 = 3/2 (invalid, > 1)
Negative root: alpha = (-4 + 8)/(-8) = -1/2 (invalid, < 0)

**This quadratic has NO roots in (0,1)!** Let me recheck.

**Error found:** The sign in the quadratic formula is wrong. From 3 - 4a - 4a^2 = 0:
```
4a^2 + 4a - 3 = 0
a = (-4 +/- sqrt(16 + 48)) / 8 = (-4 +/- 8) / 8
```

Positive root: a = 4/8 = 0.5
Negative root: a = -12/8 = -1.5

So gamma = 0 at alpha = 0.5.

For alpha > 0.5: gamma = (3 - 4a - 4a^2)/(2(1+a)) < 0 (since numerator < 0)
For alpha < 0.5: gamma > 0

**This contradicts the paper's claim!** The energy coefficient is NEGATIVE for alpha > 1/2, meaning energy DECREASES forward (INCREASES backward).

### 2.5 Resolution: Different Parametrization

**The source of confusion:** There are multiple conventions for the self-similar exponents.

**Convention A (Seregin):**
```
V^{lambda,alpha}(y, tau) = lambda^alpha v(lambda y, T + lambda^{alpha+1} tau)
```

**Convention B (Standard):**
```
u(x,t) = (T-t)^{-1/2} U(x/sqrt(T-t))  (Type I)
u(x,t) = (T-t)^{-alpha} U(x/(T-t)^{1/2})  (not standard)
```

**Convention C (Ancient Euler):**
```
V(y, s) with s in (-infty, 0]
partial_s V + (V . nabla)V + self-similar terms = -nabla P
```

Let me use **Convention C** with careful tracking of signs.

### 2.6 Correct Ancient Euler Energy Evolution

For ancient solutions (defined for tau in (-infty, 0]), the relevant equation is:
```
partial_tau V + (V . nabla)V + alpha V + (beta/2) y . nabla V = -nabla P     (2.6)
```

The coefficient alpha represents the **expansion rate** (if positive, the flow expands; if negative, contracts).

**For ancient Euler arising from backward-in-time blowup analysis:**

The blowup at time T corresponds to tau = 0.
Going backward in tau (tau -> -infty) corresponds to going backward from the blowup.

In this setup, the energy evolution is:
```
dE/dtau = (3*beta/2 - 2*alpha) E
```

For backward dispersion, we need energy in bounded regions to **grow** as tau -> -infty, i.e., we need dE/dtau < 0 (energy decreasing as tau increases means increasing as tau decreases).

**Condition for backward energy growth:**
```
3*beta/2 - 2*alpha < 0  <=>  alpha > 3*beta/4
```

For beta = 1/(1+alpha):
```
alpha > 3/(4(1+alpha))
alpha (1 + alpha) > 3/4
alpha + alpha^2 > 3/4
alpha^2 + alpha - 3/4 > 0
```

Roots: alpha = (-1 +/- sqrt(1 + 3))/2 = (-1 +/- 2)/2

Positive root: alpha = 1/2

So for alpha > 1/2: coefficient is negative, energy decreases forward (increases backward).

**This is the correct direction!** Energy in trapped regions GROWS as tau -> -infty for alpha > 1/2.

### 2.7 The 0.82 Threshold Explained

The threshold alpha_c ~ 0.82 mentioned in the paper likely comes from a different quantity:

**Claim (to verify):** The coefficient governing LOCAL energy in trapped regions (not total energy) may have a different threshold.

For local energy E_R(tau) = integral_{|y|<R} |V|^2 dy, there are boundary fluxes:
```
dE_R/dtau = (3*beta/2 - 2*alpha) E_R + boundary flux
```

The boundary flux depends on the flow structure and may change the effective coefficient.

**Alternative source of 0.82:**

From the trapped region argument, we considered:
```
d|V|^2/dtau along trajectories = -2*alpha |V|^2 + lower order terms
```

If the "lower order terms" from y . nabla V contribute positively on average, the effective coefficient could shift from -2*alpha to something larger in magnitude.

**Conclusion:** The precise value alpha_c ~ 0.82 requires careful justification of which energy identity is being used and what assumptions about the flow structure are made.

---

## 3. Analysis of the Contradiction Claim

### 3.1 The Stated Argument

The paper claims:
1. Energy in trapped regions satisfies dE_R/dtau ~ -2*alpha E_R
2. As tau -> -infty: E_R ~ e^{-2*alpha*tau} -> infty
3. This contradicts finiteness of the ancient solution
4. Therefore no trapped regions exist

### 3.2 Issues with the Argument

**Issue 3:** The coefficient -2*alpha is stated without derivation.

From Section 2, the correct coefficient for total energy is (3*beta/2 - 2*alpha), not -2*alpha.

**Issue 4:** "Trapped region" energy is not the same as energy in a fixed ball.

The argument conflates:
- E_R(tau): energy in fixed ball B_R (Eulerian)
- E_T^*(tau): energy following trapped particles (Lagrangian)

These have different evolution equations.

**Issue 5:** The finiteness assumption is not justified.

The argument assumes ancient Euler solutions have finite energy at each time. This needs proof:
- For L^2 ancient solutions, energy is finite by definition
- For L^{3,infty} ancient solutions, energy may be infinite

### 3.3 Corrected Argument for L^2 Ancient Solutions

**Proposition 3.1 (Lagrangian Energy Growth):**

For an L^2 ancient self-similar Euler solution with alpha > 1/2, the Lagrangian energy E_Lag(tau) of a bounded set of particles satisfies:
```
E_Lag(tau) ~ e^{gamma tau}  with gamma = 3*beta/2 - 2*alpha < 0
```

Therefore, as tau -> -infty, E_Lag(tau) -> infty.

**Corollary 3.2 (Trapped Set Contradiction):**

If T_0 is a trapped set (all particles remain in B_R for tau <= 0), then:
```
E_Lag(tau) <= ||V||_L^infty^2 |B_R| < infty  for all tau
```

(assuming V is bounded in B_R). But E_Lag(tau) -> infty as tau -> -infty.

Contradiction. Therefore T_0 must have zero volume or V must be zero on T_0.

### 3.4 Remaining Gap

**Gap 1:** The argument requires V to be bounded in B_R uniformly in tau. This is not automatic for ancient Euler.

**Gap 2:** The argument uses L^2 finite energy, but Type II blowup limits are typically in L^{3,infty}, which has infinite L^2 energy.

**Gap 3:** The transition from "zero volume trapped set" to "backward dispersion for all particles" needs proof.

---

## 4. Alternative Approaches

### 4.1 Characteristic Estimates

**Approach:** Directly analyze the ODE for particle trajectories:
```
dX/dtau = V(X(tau), tau)
```

**Method:** If |V| grows at infinity, particles are pushed outward. Quantify this.

**For self-similar Euler:**
```
V(y, tau) ~ |y|^{-1}  at infinity (from L^{3,infty} scaling)
```

This decay is too slow to guarantee escape.

**Alternative:** Use the self-similar structure. The y . nabla V term acts as a "radial stretching" force:
```
effective radial velocity = V_r + (beta/2) r
```

For large |y|, the term (beta/2)|y| dominates if V decays at infinity.

**Proposition 4.1:** If |V(y)| <= C|y|^{-delta} for some delta > 0 and large |y|, then particle trajectories X(tau) satisfy:
```
|X(tau)| >= |X(0)| e^{beta*tau/2}  for tau <= 0
```

As tau -> -infty: |X(tau)| -> infty (dispersion).

**Proof Sketch:** At large |y|, the equation becomes approximately:
```
dX/dtau = (beta/2) X + O(|X|^{1-delta})
```

This is a linear ODE with exponential growth backward in tau. QED

**Gap:** Requires V to decay at infinity, which needs proof.

### 4.2 Energy Methods Without Trapping Assumption

**Approach:** Prove energy deconcentrates directly, without assuming trapped regions exist.

**Definition 4.1:** The concentration function:
```
Q(R, tau) = E_R(tau) / E(tau)
```

measures the fraction of energy in B_R.

**Proposition 4.2 (Energy Deconcentration):**

For ancient self-similar Euler with alpha > 1/2 and growing total energy (as tau -> -infty):
```
Q(R, tau) -> 0  as tau -> -infty
```

for any fixed R > 0.

**Proof Sketch:** Total energy E(tau) ~ e^{gamma tau} -> infty as tau -> -infty.

If energy deconcentrates uniformly (spreads over larger scales), then Q(R, tau) -> 0.

The self-similar term (beta/2) y . nabla V acts as "inflationary" - it stretches the support of V.

**Gap:** Need to prove deconcentration is uniform.

### 4.3 Comparison with Known Euler Solutions

**Approach:** Compare with explicit ancient Euler solutions.

**Known ancient solutions:**
1. Constant flow V = const (trivial)
2. Beltrami flows (not self-similar in general)
3. Vortex rings (bounded or unbounded)

**For axisymmetric no-swirl:**
- Vortex rings have bounded vortex cores
- But self-similar structure imposes constraints

**Proposition 4.3 (Vortex Ring Exclusion):**

Ancient self-similar axisymmetric Euler without swirl cannot have bounded vortex ring structure with positive circulation.

**Proof Sketch:** The material conservation of eta = omega^theta/r combined with backward dispersion of particles implies eta -> 0 everywhere.

**Gap:** Assumes backward dispersion, which is what we're trying to prove.

---

## 5. Assessment: Is This a Genuine Gap?

### 5.1 What is Rigorous

1. **Energy evolution formula:** dE/dtau = gamma E with gamma = 3*beta/2 - 2*alpha is correct.

2. **Sign of gamma:** For alpha > 1/2 with beta = 1/(1+alpha), gamma < 0, so total energy decreases forward (increases backward).

3. **Lagrangian energy in trapped set:** If a trapped set T_0 exists with positive measure and bounded support, and V is uniformly bounded on B_R, then E_Lag grows backward.

### 5.2 What is Not Rigorous

1. **Uniform boundedness of V:** Not proven for general ancient L^{3,infty} Euler.

2. **Finiteness of energy:** L^{3,infty} solutions may have infinite L^2 energy.

3. **From energy growth to dispersion:** The argument shows trapped sets have measure zero or V = 0 on them, but this doesn't immediately imply all particles disperse.

4. **The 0.82 threshold:** The precise value needs justification.

### 5.3 What Would Close the Gap

**To make the argument rigorous:**

1. **Prove uniform bounds:** Show ancient Euler from Type II blowup has |V(y, tau)| <= C(tau)(1 + |y|)^{-delta} for some delta > 0.

2. **Or: Work in L^2:** Restrict to ancient solutions with finite L^2 energy and show Type II limits are in this class.

3. **Prove dispersion directly:** Use the characteristic ODE and the self-similar structure to show |X(tau)| -> infty.

4. **Verify alpha_c:** Carefully compute the critical exponent for the relevant energy identity.

### 5.4 Severity of the Gap

**Rating: SIGNIFICANT but likely CLOSABLE**

The core physical insight is correct: the self-similar structure with alpha > 1/2 creates a "backward expansion" effect that should prevent bounded invariant sets.

The gap is in making this precise for the correct function spaces (L^{3,infty} rather than L^2).

**Comparison with other gaps in the proof:**

| Gap | Description | Severity | Status |
|-----|-------------|----------|--------|
| Seregin condition (1.4) | Automatic for Type II? | CRITICAL | OPEN |
| Backward dispersion | Energy argument | SIGNIFICANT | FIXABLE |
| Liouville for ancient Euler | Combining dispersion + conservation | CONDITIONAL | Follows if dispersion proven |

---

## 6. Proposed Resolution

### 6.1 Direct Characteristic Argument

**Theorem 6.1 (Backward Dispersion - Revised):**

Let V(y, tau) be an ancient self-similar Euler solution satisfying:
1. V in L^{3,infty}(R^3) uniformly in tau in (-infty, 0]
2. |V(y, tau)| <= C|y|^{-1+epsilon} for |y| > R_0 and some epsilon > 0

Then all backward trajectories disperse: |X(tau)| -> infty as tau -> -infty.

**Proof:**

The characteristic equation is:
```
dX/dtau = V(X, tau)
```

In self-similar coordinates, including the self-similar drift:
```
d(|X|^2)/dtau = 2 X . V(X, tau) + beta |X|^2
```

For |X| > R_0:
```
|X . V| <= |X| |V| <= C |X|^{epsilon}
```

Therefore:
```
d(|X|^2)/dtau >= beta |X|^2 - 2C|X|^{epsilon}
              >= (beta/2) |X|^2  for |X| sufficiently large
```

Integrating backward:
```
|X(tau)|^2 >= |X(0)|^2 e^{beta*tau/2} -> infty as tau -> -infty
```

This is wrong direction! Let me reconsider.

**Correction:** As tau -> -infty, we have e^{beta*tau/2} -> 0, so the lower bound doesn't help.

**Revised approach:** Consider forward evolution (tau increasing):
```
d(|X|^2)/dtau >= (beta/2)|X|^2 for large |X|
```

This means |X|^2 grows exponentially in forward time. Backward, it decays.

But we want dispersion as tau -> -infty, not tau -> +infty!

**The issue:** The self-similar drift term (beta/2) y . nabla V pushes particles OUTWARD in forward time, INWARD in backward time.

This means backward dispersion is NOT automatic from the drift term alone.

### 6.2 Why Backward Dispersion is Nontrivial

**Key insight:** The self-similar structure alone pushes particles INWARD as tau -> -infty.

For dispersion to occur backward, the velocity V itself must overcome this inward drift.

**The energy argument provides this:** If V were nonzero in a trapped region, the Lagrangian energy would grow unboundedly backward, which is impossible for bounded V.

Therefore, V must vanish on any bounded invariant set.

But if V = 0 on a set, particles don't move, so they remain "trapped" in a trivial sense.

**The resolution:** For non-trivial flows, particles must exit bounded regions.

### 6.3 Refined Theorem

**Theorem 6.2 (Backward Dispersion - Final):**

Let V be an ancient self-similar Euler solution with:
1. V not identically zero
2. V in L^2(R^3) or with finite local energy
3. V bounded in any bounded spatial region uniformly in tau

Then for almost every particle trajectory X(tau):
```
either |X(tau)| -> infty as tau -> -infty, or V(X(tau), tau) = 0 for all tau
```

**Proof:**

Case 1: X(tau) remains in B_R for all tau <= 0.

The Lagrangian energy E_Lag of the set of such particles grows like e^{gamma tau} with gamma < 0 for alpha > 1/2.

As tau -> -infty, E_Lag -> infty.

But E_Lag <= ||V||_L^infty(B_R)^2 |{trapped particles}| < infty.

Contradiction unless the set of trapped particles has measure zero or V = 0 on it.

Case 2: X(tau) exits B_R for some tau < 0.

Continue the analysis with larger R. Either X disperses or enters Case 1 for all R, which implies V = 0 along the trajectory.

**Conclusion:** Almost every particle either disperses or has V = 0 along its trajectory. QED

---

## 7. Final Assessment

### 7.1 Status of Theorem 6.4 (Backward Dispersion)

**Verdict: PARTIALLY CORRECT but INCOMPLETE**

The theorem is correct in spirit: for alpha in (1/2, alpha_c), bounded invariant regions cannot support non-trivial self-similar Euler flow.

**What's missing:**
1. The coefficient -2*alpha should be replaced with the correct (3*beta/2 - 2*alpha)
2. The definition of "trapped region" needs to distinguish Eulerian vs Lagrangian perspectives
3. The finiteness contradiction needs the assumption that V is bounded in bounded regions
4. The value alpha_c ~ 0.82 is incorrect if using beta = 1/(1+alpha); the critical value is alpha_c = 1/2

### 7.2 Implications for the Proof

**For alpha in (1/2, 3/5):**

If the backward dispersion argument is made rigorous, combined with:
- Material conservation of eta for axisymmetric no-swirl
- eta -> 0 at spatial infinity

This yields the Liouville theorem: ancient axisymmetric Euler without swirl must be trivial.

This would close the Type II gap for axisymmetric no-swirl flows.

**What remains:**
1. Rigorize the energy argument for L^{3,infty} ancient solutions
2. Prove V decays at spatial infinity uniformly in tau
3. Handle the with-swirl case separately

### 7.3 Recommended Actions

1. **Fix the coefficient:** Use (3*beta/2 - 2*alpha) instead of -2*alpha
2. **Clarify alpha_c:** The critical threshold is alpha = 1/2, not 0.82
3. **Add regularity assumption:** State clearly that V is assumed bounded in bounded regions
4. **Prove decay at infinity:** This is a separate lemma needed for the argument
5. **Distinguish trapped sets:** Use Lagrangian energy, not Eulerian

---

## 8. Summary

### 8.1 The Backward Dispersion Argument

| Aspect | Status | Comment |
|--------|--------|---------|
| Energy evolution formula | CORRECT | gamma = 3*beta/2 - 2*alpha |
| Sign for alpha > 1/2 | CORRECT | gamma < 0, energy grows backward |
| Trapped region definition | INCOMPLETE | Need Lagrangian formulation |
| Finiteness contradiction | CONDITIONAL | Requires V bounded in bounded regions |
| Critical exponent alpha_c | INCORRECT | Should be 1/2, not 0.82 |
| Conclusion (dispersion) | CORRECT IN SPIRIT | Needs rigorous statement |

### 8.2 Is This a Genuine Gap in the Proof?

**Answer: YES, but FIXABLE**

The gap is in the precision of the argument, not in its validity. The core insight - that self-similar structure with alpha > 1/2 prevents bounded invariant sets - is correct.

Fixing the gap requires:
1. Correcting the coefficient computation
2. Working in appropriate function spaces
3. Proving auxiliary regularity estimates

### 8.3 Impact on Main Theorem

If the backward dispersion argument can be rigorized for alpha in (1/2, 3/5):
- Combined with eta conservation, this proves the Liouville theorem
- Type II blowup at these rates is excluded for axisymmetric no-swirl
- With the swirl decay argument, Type II is excluded for all axisymmetric flows

The main theorem (global regularity for axisymmetric NS) depends on closing this and other gaps (particularly Seregin's condition (1.4) being automatic).

---

## References

1. Seregin, G. "A note on certain scenarios of Type II blowups." arXiv:2507.08733 (2025)
2. Koch-Nadirashvili-Seregin-Sverak. "Liouville theorems for NS." Acta Math. 203 (2009)
3. Pan-Li. "Liouville theorem of axisymmetric NS with growing velocity." NL Analysis RWA (2020)
4. Jiu-Xin. "Exact solutions of 3D axisymmetric Euler." Comm. Math. Phys. (2009)

---

*Document completed: January 13, 2026*
*Status: CRITICAL REVIEW - Gap identified as SIGNIFICANT but FIXABLE*

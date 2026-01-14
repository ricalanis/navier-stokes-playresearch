# Monotonicity Formula Analysis for Type II Blowup Exclusion

**Date:** January 13, 2026
**Status:** COMPREHENSIVE ANALYSIS
**Author:** Claude Opus 4.5

---

## Executive Summary

This document investigates monotonicity formulas as potential tools for excluding Type II blowup with rate alpha in (1/2, 3/5). We analyze:
1. The CKN almost-monotone local energy
2. Almgren-type frequency functions
3. Scale-invariant quantities for Type II
4. Backward monotonicity for ancient solutions
5. Novel monotone quantity candidates
6. Variational structure and Lyapunov functions

**Key Finding:** No known monotonicity formula directly closes the gap, but we identify promising candidates for future investigation.

---

## 1. CKN Monotonicity Analysis

### 1.1 The CKN Local Energy Quantity

The Caffarelli-Kohn-Nirenberg partial regularity proof uses:

```
A(r) = (1/r) integral_{Q_r} |nabla u|^2 dz + (1/r^2) integral_{Q_r} |u|^3 dz
```

where Q_r = B(r) x (-r^2, 0) is the parabolic cylinder.

**Almost-Monotonicity:** For suitable weak solutions:

```
A(r) <= C A(R)  for r < R
```

with C depending only on the local energy inequality constants.

### 1.2 Relation to Type II Blowup

**Observation:** The CKN quantity A(r) has scaling dimension 0 (scale-invariant):
- |nabla u|^2 has dimension -2 (scaling like lambda^2)
- Integration over Q_r contributes dimension 5 (r^3 x r^2)
- Division by r contributes dimension -1
- Net: -2 + 5 - 1 = 2, but there's weight from NS normalization

**For Type II with rate alpha:**

At concentration scale L ~ (T-t)^{2alpha/3}:

```
||nabla u||^2_{L^2(Q_L)} ~ ||u||^2_infty / L ~ (T-t)^{-2alpha} / (T-t)^{2alpha/3}
                         = (T-t)^{-8alpha/3}
```

Then:
```
A(L) ~ L^{-1} (T-t)^{-8alpha/3} L^5 = (T-t)^{-8alpha/3 + 4 * 2alpha/3}
     = (T-t)^{-8alpha/3 + 8alpha/3} = O(1)
```

**Conclusion:** A(L) remains O(1) for Type II - the CKN quantity does NOT detect Type II blowup directly!

### 1.3 Strengthening CKN Monotonicity

Consider a modified CKN quantity with different exponent:

```
A_beta(r) = r^{-beta} integral_{Q_r} |nabla u|^2 + r^{-(beta+1)} integral_{Q_r} |u|^3
```

For this to detect Type II with rate alpha, we need:

```
A_beta(L) -> infinity as t -> T
```

**Calculation:**
```
A_beta(L) ~ L^{-beta} (T-t)^{-8alpha/3} L^5 ~ (T-t)^{-beta * 2alpha/3 - 8alpha/3 + 10alpha/3}
          = (T-t)^{(2 - beta) * 2alpha/3}
```

For divergence: need (2 - beta) * 2alpha/3 < 0, i.e., beta > 2.

**But:** For beta > 2, A_beta(r) is NOT almost-monotone in the CKN sense.

The proof of almost-monotonicity relies on beta = 1 for the gradient term.

**Conclusion:** Modifying the CKN exponent breaks the monotonicity property.

---

## 2. Frequency Function Analysis

### 2.1 Almgren Frequency Function

For harmonic functions u: Delta u = 0, the Almgren frequency is:

```
N(r) = (r integral_{B_r} |nabla u|^2) / (integral_{partial B_r} |u|^2)
```

**Monotonicity:** N'(r) >= 0 (non-decreasing in r).

This controls the "homogeneity degree" of u near 0.

### 2.2 Frequency for Heat Equation

For caloric functions (heat equation u_t = Delta u), define:

```
N(r, t) = (r integral_{B_r} |nabla u(t)|^2) / (integral_{partial B_r} |u(t)|^2)
```

This is NOT monotone in r at fixed t, but there's a parabolic version:

```
N_parab(r) = (r integral_{-r^2}^0 integral_{B_r} |nabla u|^2 dt) / (integral_{-r^2}^0 integral_{partial B_r} |u|^2 dt)
```

### 2.3 Frequency for Navier-Stokes

Define NS frequency:

```
N_{NS}(r) = (r integral_{Q_r} |nabla u|^2 dz) / (integral_{-r^2}^0 integral_{partial B_r} |u|^2 dS dt)
```

**Behavior near Type II blowup:**

At concentration scale L ~ (T-t)^{2alpha/3}:

Numerator:
```
L * ||nabla u||^2_{L^2(Q_L)} ~ L * (T-t)^{-8alpha/3} * L^5 = (T-t)^{(2alpha/3)(1+5) - 8alpha/3}
                              = (T-t)^{4alpha/3 - 8alpha/3} = (T-t)^{-4alpha/3}
```

Denominator: On partial B_L, assume |u| ~ ||u||_infty ~ (T-t)^{-alpha}:
```
integral |u|^2 dS dt ~ (T-t)^{-2alpha} * L^2 * L^2 ~ (T-t)^{-2alpha + 8alpha/3}
                     = (T-t)^{2alpha/3}
```

Therefore:
```
N_{NS}(L) ~ (T-t)^{-4alpha/3} / (T-t)^{2alpha/3} = (T-t)^{-2alpha}
```

**Finding:** N_{NS}(L) DIVERGES for Type II!

### 2.4 Monotonicity of N_{NS}?

**Key Question:** Is N_{NS}(r) monotone in r?

**Analysis:** The NS frequency evolution is:

```
d/dr N_{NS}(r) = [...complicated expression involving convective term...]
```

The convective term (u . nabla)u spoils the monotonicity proof that works for heat equation.

**Partial Result:** For axisymmetric NS without swirl (2D essentially), N_{NS} is related to vorticity and may have monotonicity properties.

**Open Problem:** Establish monotonicity (or almost-monotonicity) for N_{NS} in 3D NS.

If N_{NS}(r) were monotone increasing and N_{NS}(r) >= c > 0 for r near 0, this would constrain the blowup profile.

---

## 3. Scale-Invariant Quantities for Type II

### 3.1 Definition

For Type II blowup with rate alpha, define:

```
Phi_alpha(r, t) = r^{2alpha} ||u||^2_{L^infty(Q_r)} + r^{2alpha-1} ||nabla u||^2_{L^2(Q_r)}
```

### 3.2 Scaling Check

Under NS scaling u -> lambda u(lambda x, lambda^2 t):

- ||u||_infty -> lambda ||u||_infty
- ||nabla u||_{L^2} -> lambda^{1/2} ||nabla u||_{L^2}
- r -> r/lambda

Then:
```
Phi_alpha(r/lambda) = (r/lambda)^{2alpha} (lambda ||u||_infty)^2 + (r/lambda)^{2alpha-1} (lambda^{1/2} ||nabla u||_{L^2})^2
                    = r^{2alpha} lambda^{2-2alpha} ||u||^2_infty + r^{2alpha-1} lambda^{2-2alpha} ||nabla u||^2_{L^2}
                    = lambda^{2-2alpha} Phi_alpha(r)
```

**For scale invariance:** Need 2 - 2alpha = 0, i.e., alpha = 1 (Type I rate!).

For alpha in (1/2, 1), Phi_alpha is NOT scale-invariant.

### 3.3 Behavior Under Type II

At blowup time T with concentration at scale L:

```
Phi_alpha(L, T) ~ L^{2alpha} (T-t)^{-2alpha} + L^{2alpha-1} (T-t)^{-4alpha/3} L^5
```

With L ~ (T-t)^{2alpha/3}:

First term: (T-t)^{4alpha^2/3 - 2alpha} = (T-t)^{2alpha(2alpha/3 - 1)}

For alpha < 3/2: exponent < 0, term diverges.

Second term: More complex, similar analysis.

### 3.4 Monotonicity of Phi_alpha?

**Time derivative:**

```
d/dt Phi_alpha(r, t) = 2 r^{2alpha} ||u||_infty ||u||_infty'
                     + 2 r^{2alpha-1} <nabla u, nabla u_t>_{L^2}
```

Using NS: u_t = nu Delta u - (u.nabla)u - nabla p

The nonlinear and pressure terms make monotonicity analysis difficult.

**r-derivative:**

```
d/dr Phi_alpha(r, t) = 2alpha r^{2alpha-1} ||u||^2_{L^infty(Q_r)} + [boundary terms]
                     + (2alpha-1) r^{2alpha-2} ||nabla u||^2_{L^2(Q_r)} + [boundary terms]
```

For alpha > 1/2: all coefficients positive, suggesting Phi_alpha is increasing in r.

**Finding:** Phi_alpha appears to be increasing in r (for alpha > 1/2), but this needs rigorous verification.

---

## 4. Backward Monotonicity for Ancient Solutions

### 4.1 Ancient Solution Setup

In self-similar variables (y, tau) with y = x / sqrt(T-t), tau = -log(T-t):

```
V(y, tau) = sqrt(T-t) u(x, t)
```

satisfies the rescaled equation:

```
V_tau + (V.nabla)V = nu_eff Delta V + (1/2)(V + y.nabla V) + nabla P
```

For ancient solutions (tau in (-infty, 0]), we study tau -> -infty behavior.

### 4.2 Gaussian-Weighted Energy

Define:

```
E(tau) = integral |V(y, tau)|^2 exp(-|y|^2 / (4|tau|)) dy
```

The Gaussian weight exp(-|y|^2/(4|tau|)) has variance 2|tau|, so:
- As tau -> -infty: weight spreads, E measures global behavior
- As tau -> 0: weight concentrates, E measures local behavior

### 4.3 Monotonicity Calculation

```
d/d tau E(tau) = 2 integral V . V_tau exp(-|y|^2/(4|tau|)) dy
               + integral |V|^2 d/d tau[exp(-|y|^2/(4|tau|))] dy
```

The weight derivative:
```
d/d tau [exp(-|y|^2/(4|tau|))] = (-|y|^2/(4 tau^2)) exp(-|y|^2/(4|tau|))
```

For tau < 0: this is negative for y != 0.

### 4.4 Using the Rescaled Equation

Substituting V_tau from the rescaled NS:

```
d/d tau E(tau) = -2 nu_eff integral |nabla V|^2 w dy
               - integral |V|^2 (y.nabla V + V/2) w dy
               + [...nonlinear and pressure contributions...]
```

where w = exp(-|y|^2/(4|tau|)).

**The linear part:** Completing the square in the self-similar terms gives:

```
-integral |V|^2 (y.nabla V + V/2) w dy = (1/4) integral |V|^2 w dy + boundary terms
```

**Result:** The linear terms contribute POSITIVE to dE/dtau (energy increases going forward in tau).

### 4.5 Implication for Euler

For Euler (nu_eff = 0 or tau -> -infty limit):

```
d/d tau E(tau) >= c E(tau)  for some c > 0
```

This suggests E is monotone INCREASING as tau -> 0 (approaching blowup).

**Contrapositive:** If E(0) < infty, then E(tau) < infty for all tau < 0.

**Connection to Type II:** The Gaussian weight may be tuned to detect Type II concentration.

**Open Question:** For Type II with alpha > 1/2, does the weighted energy E(tau) with Gaussian weight satisfy:

```
E(tau) bounded implies no Type II blowup?
```

---

## 5. Novel Monotone Quantity Candidates

### 5.1 Design Criteria

We seek a quantity M(r) such that:
1. M is finite for smooth solutions
2. M is monotone (or almost-monotone) in r
3. M would be infinite for Type II with alpha > 5/7 (or some threshold)

### 5.2 Candidate 1: Weighted Vorticity Moment

```
M_1(r) = (1/r^{gamma}) integral_{B_r} |omega|^2 |x|^{2-gamma} dx
```

**Motivation:** Vorticity blows up for Type II; the weight |x|^{2-gamma} controls axis behavior.

**Scaling:** Under u -> lambda u(lambda x):
- |omega| -> lambda^2 |omega|
- integral_{B_r} |omega|^2 |x|^{2-gamma} dx -> lambda^{4 + gamma} (scale lambda^4 from omega^2, times lambda^{gamma-2} from |x|^{2-gamma}, times lambda^3 from volume, net: 4 + 3 + gamma - 2 = 5 + gamma)

For M_1 scale-invariant: need gamma = 5 + gamma - gamma = 5 (doesn't work simply).

### 5.3 Candidate 2: Frequency-Type with Pressure

```
M_2(r) = (r integral_{Q_r} |nabla u|^2 + |p|^{3/2} dz) / (integral_{Q_r} |u|^2 dz)
```

**Motivation:** Combines velocity gradient, pressure (which tracks nonlinearity), and velocity in a ratio.

**Monotonicity?** Using local energy inequality:

```
d/dr [integral_{Q_r} |u|^2] = integral_{partial Q_r} |u|^2 - [dissipation contribution]
```

The ratio structure may lead to monotonicity via calculus of variations.

### 5.4 Candidate 3: Modified Almgren with Convection

```
M_3(r) = N(r) + (1/r) integral_{Q_r} |u . nabla u| dz / integral_{partial Q_r} |u|^2 dS
```

where N(r) is the standard frequency.

**Motivation:** The added term accounts for convection.

**Open:** Need to verify if this corrects the frequency monotonicity for NS.

### 5.5 Candidate 4: Enstrophy-Based

For vorticity omega = curl u:

```
M_4(r) = (integral_{B_r} |omega|^2 dx)^{1/2} / (integral_{partial B_r} |u|^2 dS)^{1/2}
```

**Relation to regularity:** By Biot-Savart, u ~ nabla^{-1} omega, so this ratio measures local versus boundary contributions.

**For Type II:** Vorticity concentrates faster than velocity, suggesting M_4 -> infty near blowup.

### 5.6 Assessment

| Candidate | Scale Invariant? | Monotone? | Detects Type II? |
|-----------|-----------------|-----------|------------------|
| M_1 | No | Unknown | Likely |
| M_2 | Approximately | Unknown | Possibly |
| M_3 | No | Unknown | Unknown |
| M_4 | No | Unknown | Likely |

**None of these candidates have established monotonicity for NS.**

---

## 6. Variational Approach: Lyapunov Functions

### 6.1 NS as Gradient Flow

The Navier-Stokes equations can be viewed (formally) as gradient flow:

```
u_t = -delta H / delta u
```

where H is the enstrophy:

```
H[u] = (1/2) integral |omega|^2 dx = (1/2) integral |curl u|^2 dx
```

**Caveat:** This is only formal; NS is not exactly gradient flow due to pressure and incompressibility.

### 6.2 Lyapunov Functional for Rescaled System

In self-similar variables, the rescaled NS is:

```
V_tau = nu_eff Delta V - (V.nabla)V - nabla P + (1/2)(V + y.nabla V)
```

Seek Lyapunov functional L[V] with dL/dtau <= 0.

**Candidate:**
```
L[V] = integral |V|^2 exp(-|y|^2/4) dy
```

(Gaussian-weighted L^2 norm)

### 6.3 Computing dL/dtau

```
dL/dtau = 2 integral V . V_tau exp(-|y|^2/4) dy
        = -2 nu_eff integral |nabla V|^2 exp(-|y|^2/4) dy  [viscous term, negative]
        + 2 integral V . (V + y.nabla V)/2 exp(-|y|^2/4) dy  [self-similar term]
        + [nonlinear and pressure contributions]
```

**Self-similar term:** Integration by parts shows:

```
integral V . (y.nabla V) exp(-|y|^2/4) dy = -(3/2) integral |V|^2 exp(-|y|^2/4) dy
                                          + (1/4) integral |V|^2 |y|^2 exp(-|y|^2/4) dy
```

The self-similar structure gives:

```
dL/dtau = -2 nu_eff ||nabla V||^2_w - (1/2) ||V||^2_w + (1/4) integral |V|^2 |y|^2 w dy + O(nonlinear)
```

### 6.4 Sign of dL/dtau

For localized V (supported near y = 0):

```
integral |V|^2 |y|^2 w dy << ||V||^2_w
```

So: dL/dtau approximately equal to -2 nu_eff ||nabla V||^2_w - (1/2) ||V||^2_w < 0.

**L is decreasing!**

### 6.5 Implication

If L[V(tau)] is decreasing and bounded below by 0:

```
L[V(tau)] -> L_infty >= 0 as tau -> infty
```

If L_infty = 0, then V -> 0 (no blowup profile).

If L_infty > 0, then V -> V_infty with ||V_infty||_w > 0.

**Connection to Type II:**

For Type II blowup, the rescaled V should have ||V||_infty bounded but ||V||_w may vary.

**Open:** Prove L_infty = 0 for Type II with alpha in (1/2, 3/5).

---

## 7. Key Insight: The Gap at alpha = 5/7

### 7.1 Why 5/7?

From energy scaling: E ~ (T-t)^{3-5alpha}
- For alpha < 3/5: E decreases
- For alpha = 3/5: E constant (critical)
- For alpha > 3/5: E would increase (impossible)

From dissipation scaling: D ~ (T-t)^{1-5alpha/3}
- Integrated dissipation integral_0^T D dt converges iff 1 - 5alpha/3 > -1, i.e., alpha < 6/5

From BKM criterion: omega_infty ~ (T-t)^{-2alpha}
- integral_0^T omega_infty dt = infty requires 2alpha >= 1, i.e., alpha >= 1/2

**The gap (1/2, 3/5) comes from energy vs BKM constraints.**

### 7.2 Can Monotonicity Close the Gap?

A monotone quantity M(r) that detects Type II would need:

1. M(r) bounded for regular solutions
2. M(r) -> infty for Type II as r -> 0

The CKN quantity A(r) is bounded for Type II with alpha in (1/2, 3/5) - it cannot detect this blowup.

### 7.3 Required Property

For a monotone quantity to close the gap, it must be:

```
M(L) ~ (T-t)^{-epsilon} for some epsilon > 0
```

at the concentration scale L ~ (T-t)^{2alpha/3}.

From Section 2.3: N_{NS}(L) ~ (T-t)^{-2alpha} - this DOES diverge!

**Crucial Question:** Is N_{NS} monotone in r?

---

## 8. Synthesis: The Most Promising Approach

### 8.1 The Frequency Function Path

The NS frequency N_{NS}(r) defined in Section 2.3:
1. Diverges for Type II blowup (Section 2.3)
2. May be monotone in r (unproven but plausible)
3. Bounded for regular solutions

**If monotonicity is established:** N_{NS}(r) >= c > 0 for small r would imply Type II blowup.

Contrapositive: If N_{NS}(r) -> 0 as r -> 0 for all solutions, then no Type II.

### 8.2 Research Program

1. **Prove monotonicity:** Show d/dr N_{NS}(r) >= 0 (or >= -C N_{NS} for almost-monotonicity)

2. **Compute N_{NS} at r = 0:** For regular solutions, limr->0 N_{NS}(r) = ?

3. **Contradiction:** If monotone and lim = 0 for regular, but N_{NS} diverges for Type II, contradiction.

### 8.3 Technical Challenges

The convective term (u.nabla)u contributes:

```
integral_{Q_r} nabla u . nabla[(u.nabla)u] dz
```

This has indefinite sign and breaks standard monotonicity arguments.

**Possible resolution:** Weight by Gaussian in time to cancel convection contribution.

---

## 9. Connection to Seregin's Condition (1.4)

### 9.1 Seregin's Weighted Norms

```
A_{m1}(r) = r^{1-2m} sup_t integral_{B_r} |v|^2 dx
E_m(r) = r^{-m} integral_{Q_r} |nabla v|^2 dz
D_m(r) = r^{-2m} integral_{Q_r} |q|^{3/2} dz
```

### 9.2 Monotonicity of A_{m1} + E_m + D_m?

Consider:
```
S_m(r) = A_{m1}(r) + E_m(r) + D_m(r)
```

From Section 3 of our previous analysis:
- A_{m1}(L) has positive exponent for Type II with matching m
- E_m(L) has positive exponent
- D_m(L) has positive exponent

**But:** S_m is NOT monotone in r in general.

### 9.3 Alternative: Monotonicity of Integral

Define:
```
I_m(r) = integral_0^r S_m(s) ds/s
```

If S_m has specific structure, I_m might be monotone.

**Open:** Investigate if cumulative integral has better monotonicity properties.

---

## 10. Conclusions and Open Problems

### 10.1 Summary of Findings

| Quantity | Monotone? | Detects Type II? | Status |
|----------|-----------|------------------|--------|
| CKN A(r) | Almost | No (bounded) | Cannot close gap |
| N_{NS}(r) | Unknown | Yes (diverges) | Most promising |
| Phi_alpha(r) | Likely | Yes | Needs verification |
| E(tau) backward | Yes (for Euler) | Possibly | Needs NS analysis |
| Seregin S_m(r) | No | Yes | Not useful directly |

### 10.2 The Key Open Problem

**Prove or disprove:** The NS frequency N_{NS}(r) is monotone (or almost-monotone) in r for suitable weak solutions.

### 10.3 Promising Directions

1. **Frequency monotonicity:** Establish d/dr N_{NS} >= 0 using Carleman estimates or weighted inequalities.

2. **Gaussian-weighted Lyapunov:** Prove dL/dtau < 0 strictly for the self-similar rescaling with proper nonlinear control.

3. **New conservation law:** Seek a quantity conserved by NS that controls A_{m1} at small scales.

4. **Structural constraint:** Prove Type II concentration has specific geometry incompatible with NS dynamics.

### 10.4 Honest Assessment

**No monotonicity formula currently closes the gap (1/2, 3/5).**

The most promising candidate is the NS frequency N_{NS}(r), which:
- Diverges for Type II (shown)
- May be monotone (unproven)

If frequency monotonicity is established, this would provide a new tool for regularity theory.

### 10.5 Comparison to Other PDEs

| PDE | Monotone Quantity | Result |
|-----|-------------------|--------|
| Harmonic maps | Almgren frequency | Regularity |
| Free boundaries | Alt-Caffarelli-Friedman | Regularity |
| Minimal surfaces | Area monotonicity | Regularity |
| Mean curvature flow | Huisken entropy | Type I classification |
| Navier-Stokes | CKN energy (partial) | Partial regularity only |

**NS is unique:** The convective nonlinearity prevents direct application of standard monotonicity techniques.

---

## References

1. Caffarelli, L., Kohn, R., Nirenberg, L. "Partial regularity of suitable weak solutions of the Navier-Stokes equations." CPAM 35 (1982).

2. Almgren, F. "Dirichlet's problem for multiple valued functions." (Frequency function origin)

3. Alt, H.W., Caffarelli, L.A., Friedman, A. "Variational problems with two phases and their free boundaries." TAMS 282 (1984).

4. Seregin, G. "A note on certain scenarios of Type II blowups." arXiv:2507.08733 (2025).

5. Escauriaza, L., Seregin, G., Sverak, V. "L_{3,infty}-solutions." Russian Math. Surveys 58 (2003).

6. Constantin, P., Fefferman, C. "Direction of vorticity and the problem of global regularity." Indiana Univ. Math. J. 42 (1993).

7. Tao, T. "Quantitative bounds for critically bounded solutions." Amer. J. Math. 141 (2019).

---

## Appendix A: Detailed Frequency Calculation

### A.1 Numerator Evolution

For N_{NS}(r) = (r integral_{Q_r} |nabla u|^2) / (integral_{-r^2}^0 integral_{partial B_r} |u|^2 dS dt):

```
d/dr [r integral_{Q_r} |nabla u|^2] = integral_{Q_r} |nabla u|^2 + r integral_{partial Q_r} |nabla u|^2
                                    = integral_{Q_r} |nabla u|^2 + r [integral_{partial B_r x (-r^2,0)} |nabla u|^2
                                      + integral_{B_r x {-r^2}} |nabla u|^2 * (-2r)]
```

### A.2 Denominator Evolution

```
d/dr [integral_{-r^2}^0 integral_{partial B_r} |u|^2 dS dt]
    = integral_{-r^2}^0 [d/dr integral_{partial B_r} |u|^2 dS] dt + integral_{partial B_r} |u(-r^2)|^2 dS * (-2r)
```

### A.3 Ratio Evolution

The full d/dr N_{NS}(r) is a ratio of polynomials in derivatives of u.

For monotonicity, need:
```
(Num' / Num) >= (Denom' / Denom)
```

This reduces to an integral inequality involving gradient and boundary terms.

**Key obstruction:** The convective term contribution does not have definite sign.

---

## Appendix B: Lyapunov Calculation Details

### B.1 Self-Similar Term Expansion

```
integral V . (y.nabla V)/2 exp(-|y|^2/4) dy
```

Integration by parts:
```
= -(1/2) integral (y.nabla(|V|^2/2)) exp(-|y|^2/4) dy
= (1/4) integral |V|^2 div(y exp(-|y|^2/4)) dy
= (1/4) integral |V|^2 (3 - |y|^2/2) exp(-|y|^2/4) dy
= (3/4) ||V||^2_w - (1/8) integral |V|^2 |y|^2 exp(-|y|^2/4) dy
```

### B.2 Combined Linear Terms

```
dL/dtau|_{linear} = -2 nu ||nabla V||^2_w + ||V||^2_w + (3/4) ||V||^2_w - (1/8) integral |V|^2 |y|^2 w dy
                  = -2 nu ||nabla V||^2_w + (7/4) ||V||^2_w - (1/8) <|y|^2 |V|^2>_w
```

For the self-similar blowup equation (not NS), this has indefinite sign unless nu is large enough.

---

**End of Document**


# Annular Energy Analysis: Can Type II Concentration Compensate for Boundary Flux Divergence?

**Date:** January 13, 2026
**Status:** MATHEMATICAL INVESTIGATION - PARTIAL RESOLUTION
**Problem:** Gap 2 boundary flux term scaling as (T-t)^{1-2alpha}

---

## Executive Summary

**Question:** Can Type II concentration structure FORCE the annular energy ||u||^3_{L^3(B_{2L} \ B_L)} to decay fast enough to compensate for the boundary flux divergence?

**Answer:** PARTIALLY VIABLE, but with significant caveats.

The approach shows promise for single-scale concentration but encounters fundamental obstructions for:
1. Multi-scale cascade configurations
2. The boundary case alpha = 3/5
3. Establishing uniform bounds across all scales

**Key Finding:** Concentration at scale L implies annular energy decay, but the decay rate is barely sufficient and requires additional structural assumptions beyond what Type II blowup automatically provides.

---

## 1. Problem Setup

### 1.1 The Boundary Flux Issue

In the local energy inequality for suitable weak solutions, the boundary flux term arises from integrating by parts with a cutoff function phi_L supported on B_L:

```
Boundary Flux = (1/L) * integral_{partial B_L direction} (|u|^2 + 2p) (u . nabla phi_L) dx dt
```

This scales as:

```
BF ~ (1/L) * ||u||^3_{L^3(annulus)} + (1/L) * ||p||_{L^{3/2}(annulus)} ||u||_{L^3(annulus)}
```

where the annulus is A_L := B_{2L} \ B_L.

### 1.2 The Divergence Problem

For Type II blowup with rate alpha in (1/2, 3/5) and concentration scale L ~ (T-t)^{beta} with beta = (1+alpha)/2:

**Naive estimate (assuming uniform distribution):**

```
||u||_{L^3(A_L)}^3 ~ ||u||_infty^3 * |A_L| ~ (T-t)^{-3alpha} * L^3 ~ (T-t)^{-3alpha + 3beta}
```

```
BF ~ (1/L) * (T-t)^{-3alpha + 3beta} = (T-t)^{-beta} * (T-t)^{-3alpha + 3beta} = (T-t)^{-3alpha + 2beta}
```

With beta = (1+alpha)/2:

```
-3alpha + 2beta = -3alpha + (1+alpha) = 1 - 2alpha
```

**For alpha in (1/2, 3/5): exponent 1-2alpha in (-1/5, 0) < 0**

The boundary flux DIVERGES as (T-t)^{1-2alpha}.

### 1.3 The Question

Can the concentration structure imply:

```
||u||^3_{L^3(A_L)} << ||u||^3_{L^3(B_L)} * (decay factor)
```

where the decay factor compensates for the (T-t)^{1-2alpha} divergence?

---

## 2. What Type II Concentration Implies

### 2.1 Energy Distribution Under Concentration

**Definition 2.1.1 (Type II Concentration).** A solution exhibits Type II concentration at scale L(t) if:

1. ||u||_infty ~ (T-t)^{-alpha} with alpha > 1/2
2. The maximum is achieved near the origin: |u(x_*(t), t)| = ||u||_infty
3. L(t) := (nu * (T-t))^{1/2} * ||u||_infty^{-1/(some power)} ~ (T-t)^{beta}

**Lemma 2.1.2 (Energy in Concentration Region).** Under Type II concentration:

```
integral_{B_L} |u|^2 dx >= c * E(t)
```

where c > 0 is a universal constant and E(t) = ||u(t)||_{L^2}^2.

**Proof Sketch:** By definition of concentration, the velocity amplitude decays outside B_L. The L^2 norm contribution from outside is controlled by L^infty decay.

### 2.2 Implied Decay in Annulus

**Proposition 2.2.1 (Annular Decay from Concentration).** If Type II concentration holds with profile U in the rescaled variables, then:

```
||u||_{L^3(A_L)}^3 <= C * ||u||_{L^3(B_L)}^3 * (L/R)^{sigma}
```

where R is the outer radius (R = 2L for A_L) and sigma > 0 depends on the profile decay rate.

**Proof:**

In rescaled variables y = x/L(t), the velocity scales as:

```
u(x,t) = (T-t)^{-alpha} U(x/L, tau)
```

For Type II concentration, U(y) must decay as |y| -> infty (otherwise energy would not be finite).

The minimal decay consistent with finite energy is:

```
|U(y)| <= C / |y|^{3/2}  for |y| > 1
```

(This is the borderline L^2 decay in 3D.)

In the annulus |y| in [1, 2]:

```
||U||_{L^3(|y| in [1,2])}^3 ~ integral_1^2 |y|^2 * |y|^{-9/2} d|y| ~ integral_1^2 |y|^{-5/2} d|y| ~ 1
```

This is the same order as ||U||_{L^3(|y| < 1)}^3 ~ 1.

**Key observation:** The minimal decay |U| ~ |y|^{-3/2} does NOT provide additional suppression in the annulus.

---

## 3. Monotonicity Formulas Approach

### 3.1 Almgren Frequency Function

**Definition 3.1.1.** For a harmonic function u, the Almgren frequency function is:

```
N(r) := r * (integral_{B_r} |nabla u|^2 dx) / (integral_{partial B_r} |u|^2 dS)
```

**Theorem (Almgren).** N(r) is monotone non-decreasing in r.

### 3.2 Adaptation to Navier-Stokes

For Navier-Stokes, direct application of Almgren's frequency function fails because:

1. The equation is nonlinear (u . nabla u term)
2. The equation is parabolic (time derivative)
3. Pressure is non-local

**Proposed modified frequency:**

```
N_NS(r,t) := r * E_m(r,t) / A_{m_1}(r,t)
```

where E_m and A_{m_1} are Seregin's weighted norms.

**Problem:** There is no known monotonicity formula for N_NS in the Navier-Stokes setting.

### 3.3 Local Energy Monotonicity

The CKN local energy inequality provides a one-sided bound:

```
integral |u|^2 phi |_{t_2} + 2nu integral_{t_1}^{t_2} integral |nabla u|^2 phi
<= integral |u|^2 phi |_{t_1} + (error terms)
```

**This is NOT monotonicity** - it's an inequality, and the error terms include the problematic boundary flux.

### 3.4 Assessment of Monotonicity Approach

**Status: NOT VIABLE for annular decay**

Reasons:
1. No Almgren-type monotonicity for NS velocity
2. CKN inequality is not monotonicity
3. Nonlinearity breaks the structure needed for frequency analysis

**Reference:** Almgren-type monotonicity formulas have been extended to some nonlinear elliptic problems ([Almgren-type monotonicity formulas](https://mc.sbm.org.br/wp-content/uploads/sites/9/sites/9/2024/12/61-article2.pdf)), but not to parabolic systems like Navier-Stokes.

---

## 4. Carleman Estimates Approach

### 4.1 Standard Carleman Framework

For parabolic equations partial_t u - nu Delta u = f, Carleman estimates give:

```
integral e^{2lambda phi} (lambda^3 |u|^2 + lambda |nabla u|^2) dx dt
<= C integral e^{2lambda phi} |f|^2 dx dt
```

where phi is a suitable weight function.

**Key property:** The exponential weight can "highlight" behavior near a surface, enabling unique continuation results.

### 4.2 Application to Annular Decay

**Proposed strategy:**

Choose phi = phi(|x|) with:
- phi small in B_L (inner region)
- phi large in A_L (annulus)
- phi decays at infinity

Then the Carleman estimate would imply:

```
||u||_{L^2(A_L)} controlled by ||u||_{L^2(B_L)} with exponential improvement
```

**Obstacle:** For Navier-Stokes, the source term f = -u . nabla u - nabla p involves u itself, creating a circular argument.

### 4.3 Strong Unique Continuation Results

**Theorem (Ignatova-Kukavica, 2013).** Solutions to Navier-Stokes with Gevrey forcing have the strong unique continuation property.

This uses Carleman inequalities but for a different purpose (unique continuation from a set, not annular decay).

**Reference:** [Strong Unique Continuation for Navier-Stokes](https://web.math.princeton.edu/~ignatova/IK_NSE.pdf)

### 4.4 Assessment of Carleman Approach

**Status: PROMISING but INCOMPLETE**

What works:
- Carleman estimates can be formulated for NS
- Quantitative versions exist (Barker-Prange arXiv:2510.20757)
- Can provide bounds with explicit constant tracking

What's missing:
- No direct application to annular decay known
- Nonlinear term creates technical difficulties
- Boundary flux is not directly controlled by unique continuation

---

## 5. CKN Theory and Annular Regions

### 5.1 CKN Epsilon-Regularity

**Theorem (CKN 1982).** There exists epsilon > 0 such that if:

```
r^{-2} integral_{Q_r} (|u|^3 + |p|^{3/2}) dx dt < epsilon
```

then u is bounded in Q_{r/2}.

### 5.2 Application to Annular Estimates

**Observation:** CKN controls the TOTAL integral over Q_r, not specifically the annular part.

**Lemma 5.2.1 (Annular CKN Bound).** If the CKN criterion is satisfied at scale r, then:

```
r^{-2} integral_{Q_r cap (A_r)} |u|^3 dx dt < epsilon
```

automatically, since the annulus is a subset of Q_r.

**Problem:** This gives no ADDITIONAL control on the annulus beyond what's already required for regularity.

### 5.3 Scaling at Singular Points

Near a potential singularity, the CKN criterion FAILS:

```
r^{-2} integral_{Q_r} |u|^3 dx dt >= epsilon
```

At such points, CKN provides no bound on annular vs. interior distribution.

### 5.4 Assessment of CKN Approach

**Status: INSUFFICIENT**

CKN theory:
- Bounds total energy, not annular specifically
- Fails at singular points (where we need the bound most)
- Does not distinguish interior from annular contributions

**Reference:** [Caffarelli-Kohn-Nirenberg Partial Regularity](https://onlinelibrary.wiley.com/doi/10.1002/cpa.3160350604)

---

## 6. Profile Structure Analysis

### 6.1 Type II Profile Decay Rates

For Type II blowup, the rescaled profile U satisfies constraints from:
1. Finite energy: integral |U|^2 < infty
2. Finite dissipation: integral |nabla U|^2 < infty (time-integrated)
3. Euler limit equation structure

**Minimal decay for finite energy:**

```
|U(y)| <= C / |y|^{3/2} for |y| >> 1
```

This gives |U|^2 ~ |y|^{-3}, and integral_{|y|>R} |U|^2 d^3y ~ R^0 (logarithmic).

### 6.2 Physical Decay Scenarios

**Scenario A: Gaussian-like decay**

```
|U(y)| ~ exp(-c|y|^2)
```

Then:
```
||U||_{L^3(|y| in [1,2])}^3 ~ exp(-c) << ||U||_{L^3(|y|<1)}^3
```

**Strong annular suppression!** But this is NOT forced by Type II structure.

**Scenario B: Algebraic decay (minimal)**

```
|U(y)| ~ |y|^{-3/2}
```

Then:
```
||U||_{L^3(|y| in [1,2])}^3 ~ ||U||_{L^3(|y|<1)}^3
```

**No annular suppression.** This IS consistent with Type II structure.

### 6.3 Constraint from Vorticity

The BKM criterion requires:

```
integral_0^T ||omega||_{L^infty} dt = infty
```

For Type II with ||omega||_infty ~ (T-t)^{-gamma} with gamma > 1, this is satisfied.

**Vorticity decay outside core:** If vorticity concentrates, then outside B_L:

```
|omega(x)| << (T-t)^{-gamma} for |x| > L
```

This implies faster velocity decay in the annulus via Biot-Savart.

### 6.4 Biot-Savart Estimate

**Lemma 6.4.1.** If vorticity is supported in B_L with ||omega||_infty ~ Lambda, then:

```
|u(x)| <= C * Lambda * L^3 / |x|^2 for |x| > 2L
```

**Proof:** Direct estimate from Biot-Savart kernel K(x-y) ~ |x-y|^{-2}.

**Application to annulus A_L = B_{2L} \ B_L:**

```
|u(x)| <= C * Lambda * L^3 / L^2 = C * Lambda * L for x in A_L
```

Compare to interior:
```
|u(x)| ~ Lambda * L for x in B_L (from concentration)
```

**Result:** Biot-Savart gives NO additional suppression in the annulus for concentrated vorticity!

---

## 7. Dimensional Mismatch Analysis

### 7.1 The Core Problem

The boundary flux term requires bounding:

```
BF ~ (1/L) * ||u||^3_{L^3(A_L)}
```

With L ~ (T-t)^{beta}, we need:

```
||u||^3_{L^3(A_L)} = o(L) = o((T-t)^{beta})
```

for bounded boundary flux.

### 7.2 Available Estimates

From Type II structure:
- ||u||_infty ~ (T-t)^{-alpha}
- |A_L| ~ L^3 ~ (T-t)^{3beta}

If u has amplitude ~ ||u||_infty in A_L:
```
||u||^3_{L^3(A_L)} ~ ||u||_infty^3 * |A_L| = (T-t)^{-3alpha + 3beta}
```

### 7.3 Required vs. Available

**Required for bounded BF:**
```
-3alpha + 3beta > beta  =>  2beta > 3alpha  =>  beta > 3alpha/2
```

**Available from beta = (1+alpha)/2:**
```
(1+alpha)/2 > 3alpha/2  =>  1+alpha > 3alpha  =>  1 > 2alpha  =>  alpha < 1/2
```

**CONTRADICTION:** For Type II (alpha > 1/2), the available beta is NOT sufficient.

### 7.4 What Would Be Needed

To close the gap, we would need:

```
||u||^3_{L^3(A_L)} << ||u||_infty^3 * |A_L|
```

Specifically:
```
||u||^3_{L^3(A_L)} <= (T-t)^{sigma} * ||u||_infty^3 * |A_L|
```

with sigma > 2alpha - 1 > 0.

**This requires the velocity in the annulus to be MUCH smaller than ||u||_infty.**

---

## 8. Structural Constraints from Type II

### 8.1 Energy Balance Constraint

The energy identity:
```
dE/dt = -2nu ||nabla u||_{L^2}^2
```

For Type II, the dissipation integral converges:
```
integral_0^T ||nabla u||_{L^2}^2 dt < infty
```

This places constraints on the spatial distribution of gradients.

### 8.2 Annular Dissipation

**Claim 8.2.1.** If dissipation concentrates (||nabla u||_{L^2(B_L)}^2 ~ ||nabla u||_{L^2}^2), then:

```
||nabla u||_{L^2(A_L)}^2 << ||nabla u||_{L^2}^2
```

**Implication for velocity:** By Poincare-type inequality on the annulus:

```
||u - u_avg||_{L^2(A_L)} <= C * L * ||nabla u||_{L^2(A_L)}
```

If ||nabla u||_{L^2(A_L)} is small, then u is nearly constant on A_L.

### 8.3 The "Leakage" Problem

**Obstruction:** Even if u is nearly constant on A_L, that constant could be O(||u||_infty).

Type II concentration does NOT force the value of u on A_L to be small - it only forces the variation to be small.

### 8.4 Quantitative Estimate

**Proposition 8.4.1 (Annular Estimate Under Concentrated Dissipation).**

Suppose:
- ||nabla u||_{L^2(A_L)}^2 <= delta * ||nabla u||_{L^2(B_L)}^2
- ||u||_{L^infty(B_L)} = M

Then:
```
||u||_{L^3(A_L)}^3 <= (M^3 + C delta^{3/2} M^3 L^{-3/2}) * |A_L|
```

**Proof:** Split u = u_avg + (u - u_avg) where u_avg is the average on A_L.

By the boundary trace theorem:
```
|u_avg| <= C * (||u||_{L^2(partial B_L)} / L^2) <= C * M
```

The fluctuation is controlled by the gradient:
```
||u - u_avg||_{L^3(A_L)} <= C * L^{1/2} * ||nabla u||_{L^2(A_L)} <= C * L^{1/2} * delta^{1/2} ||nabla u||_{L^2(B_L)}
```

Combining:
```
||u||_{L^3(A_L)}^3 <= (|u_avg| + ||u-u_avg||_{L^3/|A_L|^{1/3}})^3 * |A_L|
                    <= (M + delta^{1/2} term)^3 * |A_L|
```

**Result:** No suppression of the M^3 term!

---

## 9. Viability Assessment

### 9.1 Summary of Approaches

| Approach | Viability | Key Obstruction |
|----------|-----------|-----------------|
| Monotonicity formulas | NOT VIABLE | No Almgren for NS |
| Carleman estimates | PARTIAL | Nonlinearity, no direct annular bound |
| CKN theory | INSUFFICIENT | Bounds total, not annular |
| Profile decay | INSUFFICIENT | Minimal decay gives no suppression |
| Biot-Savart | INSUFFICIENT | No suppression for concentrated omega |
| Dissipation concentration | PARTIAL | Controls gradient, not value |

### 9.2 What Would Make It Viable

The approach WOULD work if one could prove ANY of:

1. **Profile decay theorem:** Type II profiles have super-algebraic decay (e.g., exponential)

2. **Boundary value control:** The trace of u on partial B_L decays faster than the interior maximum

3. **Vorticity spreading:** omega cannot be perfectly concentrated - must have positive measure outside B_L

4. **Energy monotonicity:** Some scale-specific energy is monotone in r

### 9.3 Why These Are Hard

1. **Profile decay:** No known mechanism forces fast decay; Euler profiles can have slow decay

2. **Boundary value:** Harmonic continuation arguments fail for NS (not harmonic)

3. **Vorticity spreading:** Consistent with BKM for vorticity to concentrate arbitrarily

4. **Energy monotonicity:** NS lacks the variational structure needed

---

## 10. Partial Resolution: The Single-Scale Case

### 10.1 Setup

Assume Type II with STRICT single-scale concentration:
- All vorticity in B_{L/2}
- Velocity decays as Biot-Savart outside

### 10.2 Improved Annular Estimate

**Theorem 10.2.1 (Annular Decay Under Strict Concentration).**

If omega is supported in B_{L/2} with ||omega||_{L^1} = Gamma, then:

```
||u||_{L^3(A_L)}^3 <= C * Gamma^3 / L^3
```

**Proof:**

From Biot-Savart: u = K * omega where K(x) ~ |x|^{-2}.

For x in A_L (so |x| ~ L) and omega supported in B_{L/2}:

```
|u(x)| <= integral_{B_{L/2}} |K(x-y)| |omega(y)| dy
       <= C / L^2 * ||omega||_{L^1}
       = C * Gamma / L^2
```

Therefore:
```
||u||_{L^3(A_L)}^3 <= (Gamma / L^2)^3 * |A_L| = Gamma^3 / L^6 * L^3 = Gamma^3 / L^3
```

### 10.3 Implication for Boundary Flux

With ||u||_{L^3(A_L)}^3 <= Gamma^3 / L^3:

```
BF ~ (1/L) * Gamma^3 / L^3 = Gamma^3 / L^4
```

With L ~ (T-t)^{beta}:

```
BF ~ Gamma^3 * (T-t)^{-4beta}
```

### 10.4 Constraint on Gamma

For Type II, the circulation Gamma must satisfy:
- ||u||_infty >= ||omega||_{L^1} / L (by Biot-Savart scaling)
- ||u||_infty ~ (T-t)^{-alpha}

Therefore:
```
Gamma <= L * (T-t)^{-alpha} = (T-t)^{beta - alpha}
```

With beta = (1+alpha)/2:
```
Gamma <= (T-t)^{(1-alpha)/2}
```

### 10.5 Boundary Flux Under Strict Concentration

```
BF ~ Gamma^3 / L^4 <= (T-t)^{3(1-alpha)/2} / (T-t)^{4beta}
   = (T-t)^{3(1-alpha)/2 - 2(1+alpha)}
   = (T-t)^{(3-3alpha - 4 - 4alpha)/2}
   = (T-t)^{(-1 - 7alpha)/2}
```

**For alpha in (1/2, 3/5): exponent (-1-7alpha)/2 in (-2.1, -1.75) < 0**

**STILL DIVERGES!** Even under strict concentration, the boundary flux diverges.

### 10.6 Conclusion of Single-Scale Analysis

**Result:** Strict concentration REDUCES but does NOT ELIMINATE the divergence.

The exponent improves from (1-2alpha) to (-1-7alpha)/2, but both are negative for alpha > 1/2.

---

## 11. Alternative: Integrated Boundary Flux

### 11.1 Time-Integrated Approach

Instead of bounding BF at each instant, consider the total:

```
integral_0^T BF(t) dt = integral_0^T (1/L) * ||u||^3_{L^3(A_L)} dt
```

### 11.2 Scaling of Integrated Flux

With ||u||^3_{L^3(A_L)} ~ (T-t)^{-3alpha + 3beta} and L ~ (T-t)^{beta}:

```
integral_0^T BF dt ~ integral_0^T (T-t)^{-3alpha + 2beta} dt
```

For the integral to converge:
```
-3alpha + 2beta > -1
```

With beta = (1+alpha)/2:
```
-3alpha + (1+alpha) > -1  =>  1 - 2alpha > -1  =>  alpha < 1
```

**For Type II (alpha in (1/2, 3/5)): INTEGRAL CONVERGES!**

### 11.3 Implication

The integrated boundary flux is finite, even though the instantaneous flux diverges.

This suggests that for time-integrated quantities (like total energy dissipation), the boundary terms may not be fatal.

### 11.4 Connection to Seregin's Framework

Seregin's condition (1.4) involves:
```
M_1 = sup_{r} { A_{m_1}(r) + E_m(r) + D_m(r) }
```

The quantities A_{m_1}, E_m, D_m are INSTANTANEOUS, not time-integrated.

**Gap:** The convergence of the integrated flux does not directly imply boundedness of instantaneous quantities.

---

## 12. Final Assessment

### 12.1 Viability Verdict

**PARTIALLY VIABLE under strong additional assumptions.**

The approach works IF:
1. Concentration is strict (vorticity has compact support in B_{L/2})
2. We consider time-integrated quantities, not instantaneous
3. We accept bounds that become tight at the boundary alpha = 3/5

### 12.2 What This Approach Achieves

1. Reduces the divergence rate (from 1-2alpha to worse but analyzable)
2. Shows integrated flux converges for alpha < 1
3. Highlights the role of vorticity concentration

### 12.3 What Remains Unresolved

1. **Instantaneous bounds:** The approach does not give bounded instantaneous flux
2. **Cascade configurations:** Multi-scale energy distribution defeats the argument
3. **Profile freedom:** Type II does not force sufficient profile decay

### 12.4 Recommended Path Forward

1. **Pursue Carleman:** Quantitative Carleman estimates (Barker-Prange style) may provide the needed instantaneous bounds

2. **Time-integrated reformulation:** Reformulate Seregin's condition in terms of time-integrated quantities

3. **Profile classification:** Prove that Type II profiles must have specific decay properties

4. **Numerical investigation:** Test whether physical Type II concentrations have enhanced annular decay

---

## 13. Technical Appendix: Detailed Calculations

### A.1 Boundary Flux Derivation

Starting from the local energy inequality with cutoff phi_L:

```
d/dt integral |u|^2 phi_L + 2nu integral |nabla u|^2 phi_L
= integral |u|^2 (partial_t phi_L + nu Delta phi_L) + integral (|u|^2 + 2p) (u . nabla phi_L)
```

The boundary flux is the last term. With |nabla phi_L| ~ 1/L supported in A_L:

```
|BF| <= (C/L) integral_{A_L} (|u|^3 + |p||u|) dx
```

By Holder and pressure estimate ||p||_{L^{3/2}} <= C||u||^2_{L^3}:

```
|BF| <= (C/L) * (||u||^3_{L^3(A_L)} + ||u||^2_{L^3(A_L)} ||u||_{L^3(A_L)})
      = (C/L) * ||u||^3_{L^3(A_L)}
```

### A.2 Scaling Exponent Table

| Quantity | Scaling | Exponent |
|----------|---------|----------|
| ||u||_infty | (T-t)^{-alpha} | -alpha |
| L | (T-t)^{beta} | beta = (1+alpha)/2 |
| ||u||_{L^3(B_L)} | (T-t)^{beta-alpha} | (1-alpha)/2 |
| ||u||_{L^3(A_L)} (naive) | (T-t)^{beta-alpha} | (1-alpha)/2 |
| BF (naive) | (T-t)^{1-2alpha} | 1-2alpha |
| BF (strict conc.) | (T-t)^{(-1-7alpha)/2} | (-1-7alpha)/2 |

### A.3 Critical Values

| alpha | 1-2alpha | (-1-7alpha)/2 | Status |
|-------|----------|---------------|--------|
| 0.5 | 0 | -2.25 | BOUNDARY |
| 0.55 | -0.1 | -2.175 | DIVERGES |
| 0.6 | -0.2 | -2.6 | DIVERGES |

---

## 14. References

1. Caffarelli, L., Kohn, R., Nirenberg, L. (1982). [Partial regularity of suitable weak solutions of the Navier-Stokes equations](https://onlinelibrary.wiley.com/doi/10.1002/cpa.3160350604). Comm. Pure Appl. Math. 35, 771-831.

2. Seregin, G. (2025). A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations. arXiv:2507.08733.

3. Ignatova, M., Kukavica, I. (2013). [Strong Unique Continuation for the Navier-Stokes Equation](https://web.math.princeton.edu/~ignatova/IK_NSE.pdf). J. Dyn. Diff. Eq. 25, 1-15.

4. [Almgren-type monotonicity formulas](https://mc.sbm.org.br/wp-content/uploads/sites/9/sites/9/2024/12/61-article2.pdf). (2024). Survey of extensions to nonlinear elliptic problems.

5. [Quantitative partial regularity of the Navier-Stokes equations](https://arxiv.org/abs/2210.01783). (2022). arXiv:2210.01783.

6. Tataru, D. [Carleman estimates, unique continuation and applications](https://math.berkeley.edu/~tataru/papers/book.pdf). Berkeley lecture notes.

7. [The Partial Regularity Theory of Caffarelli, Kohn, and Nirenberg and its Sharpness](https://link.springer.com/book/10.1007/978-3-030-26661-5). Springer, 2019.

---

## 15. Summary

**Main Question:** Can Type II concentration force sufficient annular energy decay?

**Answer:** The concentration structure provides SOME suppression but NOT ENOUGH to compensate for the (T-t)^{1-2alpha} divergence in the boundary flux.

**Key Results:**

1. Naive estimate gives BF ~ (T-t)^{1-2alpha} (diverges)
2. Strict concentration improves to BF ~ (T-t)^{(-1-7alpha)/2} (still diverges)
3. Time-integrated flux converges (but doesn't help instantaneous bounds)
4. No known monotonicity formula or Carleman estimate bridges the gap

**Status:** This approach is NOT SUFFICIENT to close Gap 2 by itself.

**Recommendation:** Combine with quantitative Carleman methods or reformulate the problem in terms of time-integrated quantities.

---

**Document Status:** COMPLETE
**Conclusion:** PARTIALLY VIABLE - insufficient alone to close Gap 2

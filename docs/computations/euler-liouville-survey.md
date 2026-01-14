# Survey: Liouville Theorems for the Euler Equations

## Purpose

This document surveys known Liouville-type theorems for the Euler equations, with an eye toward understanding what is needed for extending results to Besov spaces and critical exponent regimes.

**Critical Question from Seregin's Framework:**
The ancient solution approach requires growth bounds:
```
integral_{B(b)} |U|^2 = O(b^{2m-1})  with m < 3/5
```
This translates to growth exponent gamma = (2m-1)/3 < 1/5.

**Goal:** Understand what Liouville results exist for gamma >= 1/5 (the "gap" region).

---

## 1. Foundational Results: Navier-Stokes Ancient Solutions

### 1.1 Koch-Nadirashvili-Seregin-Sverak (2009)

**Reference:** G. Koch, N. Nadirashvili, G.A. Seregin, V. Sverak, "Liouville theorems for the Navier-Stokes equations and applications," Acta Mathematica 203 (2009), 83-105.
- [arXiv:0709.3599](https://arxiv.org/abs/0709.3599)
- [Published version](https://projecteuclid.org/journals/acta-mathematica/volume-203/issue-1/Liouville-theorems-for-the-NavierStokes-equations-and-applications/10.1007/s11511-009-0039-6.full)

**Setting:** Bounded ancient solutions of Navier-Stokes in R^n x (-infinity, 0).

**Main Results:**

**Theorem (2D Navier-Stokes):** Any bounded ancient mild solution of the 2D Navier-Stokes equations is either constant or of the form u(x,t) = b(t).

**Theorem (3D Axisymmetric, No Swirl):** Any bounded ancient mild solution of the 3D axisymmetric Navier-Stokes equations without swirl is constant.

**Conjecture (KNSS):** Any bounded ancient mild solution of the 3D axisymmetric Navier-Stokes equations (with or without swirl) is constant.

**Proof Technique:**
- Backward uniqueness arguments
- Scaling analysis
- Energy estimates on rescaled domains

**Growth Assumption:** L^infinity bound (gamma = 0 in the growth exponent framework).

**Connection to Singularity:** A finite-time singularity arising from a mild solution generates a bounded ancient mild solution which is not identically zero. Therefore Liouville theorems preclude singularity formation.

---

### 1.2 Escauriaza-Seregin-Sverak (2003) - L^{3,infinity} Regularity

**Reference:** L. Escauriaza, G. Seregin, V. Sverak, "L_{3,infinity}-solutions of Navier-Stokes equations and backward uniqueness," Russian Math. Surveys 58 (2003), no. 2, 211-250.
- [University of Minnesota archive](https://conservancy.umn.edu/items/1ded2377-3cb2-43af-b8ff-f8d52ce5e3fe)

**Main Theorem (ESS Regularity):**
L^{3,infinity}-solutions (weak-L^3) of the Cauchy problem for the 3D Navier-Stokes equations are smooth.

**Statement:** Let u be a suitable weak solution of the Navier-Stokes equations on R^3 x (0,T). If
```
u in L^infinity_t L^3_x([0,T] x R^3)
```
then u is smooth on (0,T] x R^3.

**Proof Technique:**
1. Reduction to backward uniqueness for the heat operator with lower-order terms
2. Carleman estimates to establish backward uniqueness
3. Bootstrap regularity

**Critical Space:** L^3(R^3) is scale-invariant for Navier-Stokes:
```
||lambda u(lambda x)||_3 = ||u||_3
```

**Significance for Liouville:** The ESS result shows the critical L^{3,infinity} norm cannot blow up, constraining possible ancient solution profiles.

---

### 1.3 Pan-Li Growing Velocity Liouville (2020)

**Reference:** X. Pan, Z. Li, "Liouville theorem of axially symmetric Navier-Stokes equations with growing velocity at infinity," Nonlinear Analysis: Real World Applications 52 (2020), 103778.
- [arXiv:1908.11591](https://arxiv.org/abs/1908.11591)
- [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1468121820300778)

**Improvement over KNSS:** Allows solutions that grow sublinearly at infinity.

**Main Result:**
For 3D axisymmetric Navier-Stokes, the Liouville theorem holds if the solution grows with power strictly less than 1 with respect to distance to the origin:
```
|u(x)| = o(|x|^alpha) as |x| -> infinity, for any alpha < 1
```

**Optimality:**
The exponent alpha = 1 is **sharp**. Counterexamples exist showing the Liouville theorem fails if the solution can grow linearly (alpha = 1).

**Proof Technique:**
- Energy methods adapted to growing solutions
- Weighted function spaces
- Exploitation of axisymmetric structure

**Critical Threshold:** The sublinear growth condition corresponds to the maximally allowed growing condition for the Liouville theorem for the heat equation.

---

## 2. Euler-Specific Liouville Theorems

### 2.1 Hamel-Nadirashvili 2D Steady Euler (2019)

**Reference:** F. Hamel, N. Nadirashvili, "A Liouville theorem for the Euler equations in the plane," Archive for Rational Mechanics and Analysis 233 (2019), 599-642.
- [arXiv:1703.07293](https://arxiv.org/abs/1703.07293)

**Setting:** Bounded steady flows of ideal incompressible fluid in R^2 with no stagnation points.

**Main Theorem:**
Any bounded steady flow of an ideal incompressible fluid with no stagnation point in R^2 is a **shear flow** (parallel to some constant vector).

**Hypotheses:**
1. Steady (time-independent)
2. Bounded velocity: |u(x)| <= M for all x in R^2
3. No stagnation points: u(x) != 0 for all x in R^2
4. Divergence-free: div u = 0
5. Ideal (inviscid): satisfies Euler equations

**Proof Technique:**
1. Geometric analysis of level curves of the stream function
2. Derive estimates on the at-most-logarithmic growth of the argument of the velocity field
3. Conclude all streamlines are parallel

**Key Estimate:** The argument of the flow (angle of velocity vector) grows at most logarithmically, forcing parallel streamlines.

**Limitation:** 2D only, requires no stagnation points.

---

### 2.2 Nadirashvili Beltrami Flow Liouville (2014)

**Reference:** N. Nadirashvili, "Liouville theorem for Beltrami flow," Geometric and Functional Analysis 24 (2014), 916-921.
- [arXiv:1403.1414](https://arxiv.org/abs/1403.1414)

**Setting:** Beltrami flows (curl u = lambda u) in R^3, which are special solutions to stationary Euler.

**Main Theorem:**
If v in C^1(R^3) is a Beltrami solution of the stationary Euler equations with either:
- v in L^p(R^3) for p in [2,3], OR
- |v(x)| = o(1/|x|) as |x| -> infinity

Then v = 0 identically.

**Equivalent Statement:** The Beltrami flow of ideal fluid in R^3 with finite energy is zero.

**Proof Technique:**
- Energy-based arguments
- Sobolev inequalities
- Special structure of Beltrami condition

**Extensions (Chae-Constantin 2015):** Simplified elementary proof covering the finite energy case.

---

### 2.3 Chae Forced Euler/Navier-Stokes (2014)

**Reference:** D. Chae, "Liouville-type theorems for the forced Euler equations and the Navier-Stokes equations," Communications in Mathematical Physics 326 (2014), 37-48.
- [arXiv:1306.5839](https://arxiv.org/abs/1306.5839)

**Setting:** Steady incompressible Euler equations with external force in R^N.

**Main Result (Forced Euler):**
Under a "single signedness condition" on the force, if (v,p) is a C^1(R^N) solution with
```
|v|^2 + |p| in L^{q/2}(R^N) for q in (3N/(N-1), infinity)
```
then v = 0.

**For Navier-Stokes:**
If v solves steady Navier-Stokes with v(x) -> 0 as |x| -> infinity and
```
integral_{R^3} |Delta v|^{6/5} dx < infinity
```
(stronger than finite Dirichlet integral but same scaling), then v = 0.

**Key Insight:** The condition has the same scaling property as the Dirichlet integral:
```
integral |nabla v|^2 dx
```

---

### 2.4 Korobkov-Pileckas-Russo Axisymmetric (2015)

**Reference:** M. Korobkov, K. Pileckas, R. Russo, "The Liouville theorem for the steady-state Navier-Stokes problem for axially symmetric 3D solutions in absence of swirl," J. Math. Fluid Mech. 17 (2015), 287-293.

**Main Results:**

**Navier-Stokes (Unconditional):**
There are no nontrivial D-solutions (finite Dirichlet integral) of the steady Navier-Stokes equations in R^3 for the axially symmetric case without swirl.

**Euler (Conditional):**
A conditional Liouville-type theorem holds for axially symmetric solutions to the Euler system (requires additional decay assumptions).

**D-Solution Definition:**
```
integral_{R^3} |nabla v|^2 dx < infinity
```

**Proof Technique:**
- Stream function analysis
- Asymptotic decay estimates
- Vorticity bounds

---

## 3. Rigidity Results for 3D Steady Euler

### 3.1 Isolated Steady States (2025)

**Reference:** Recent work on "Isolated steady solutions of the 3D Euler equations" (PNAS).
- [arXiv:2407.12938](https://arxiv.org/html/2407.12938)

**Main Result:**
On certain 3D compact Riemannian manifolds, the incompressible Euler equations admit **isolated** steady states in the C^1 topology.

**Relevance:** This is a rigidity result showing certain steady solutions are isolated (no nearby distinct solutions), rather than a vanishing result.

**Proof Technique:**
- Dynamical systems (Anosov flows)
- Spectral geometry
- Contact topology

**Key Mechanism:** Ergodicity of Anosov flows forces continuous first integrals to be constant, severely constraining perturbations.

---

### 3.2 Compactly Supported Steady Euler (Gavrilov)

**Reference:** A.V. Gavrilov, "A steady Euler flow with compact support," Geometric and Functional Analysis 29 (2019), 190-197.

**Key Finding:**
There exist smooth, compactly supported solutions of 3D incompressible Euler equations that are at rest outside a compact region.

**Construction:** Based on localizable Grad-Shafranov equations.

**Constraint:**
Smooth compactly supported velocities solving stationary axisymmetric 3D Euler equations must vanish identically **if the swirl F vanishes**.

**Implication:** Non-trivial compactly supported 3D Euler steady states require swirl.

---

## 4. Growth Rate Analysis and Critical Exponents

### 4.1 The Critical Exponent Problem

In Seregin's framework for ancient solutions, the key growth condition is:
```
integral_{B(R)} |U|^2 dy = O(R^{2m-1}) as R -> infinity
```

**Dimensionless form:** If |U| ~ R^gamma, then:
```
integral_{B(R)} |U|^2 ~ R^{2gamma} * R^3 = R^{2gamma+3}
```

Matching: 2gamma + 3 = 2m - 1 gives gamma = m - 2.

For m < 3/5: gamma < 3/5 - 2 = -7/5 < 0 (decaying solutions).

**The Gap:** What happens for gamma in [-7/5, 0]? This is the sublinear growth regime.

### 4.2 Comparison of Growth Thresholds

| Result | Growth Condition | Exponent | Applies To |
|--------|-----------------|----------|------------|
| KNSS (2009) | Bounded | gamma = 0 | NS ancient |
| ESS (2003) | L^3,infinity | gamma = -1 (critical) | NS Cauchy |
| Pan-Li (2020) | o(|x|^alpha) for alpha < 1 | gamma < 1 | NS axisym |
| NRS (1996) | L^3 | gamma < -1 | NS profiles |
| Nadirashvili Beltrami | L^p, p in [2,3] | gamma < -1 | Euler Beltrami |
| Hamel-Nadirashvili | Bounded | gamma = 0 | 2D Euler |

### 4.3 The Critical Gap

**For gamma in [-1, 0) (sublinear decay/bounded):**
- 2D Euler: Covered by Hamel-Nadirashvili (no stagnation points)
- 3D NS axisymmetric: Partially covered by Pan-Li (alpha < 1)
- 3D Euler general: **OPEN**

**For gamma in [0, 1) (sublinear growth):**
- NS: Pan-Li shows Liouville fails at gamma = 1
- Euler: Largely **OPEN**

---

## 5. Proof Techniques Summary

### 5.1 Energy Methods

**Structure:** Multiply equation by test function (u, |u|u, weighted u), integrate, exploit cancellations.

**Applies to:**
- NRS (1996): Multiplier |U|U gives integral |U|^3 = 0
- KNSS (2009): Energy estimates on bounded ancient solutions
- Our L^2 results: Vorticity energy identity

**Limitation:** Requires sufficient integrability (L^2 or L^3 type conditions).

### 5.2 Backward Uniqueness / Carleman Estimates

**Structure:** Use unique continuation principles to propagate information backward in time.

**Applies to:**
- ESS (2003): Key ingredient for L^{3,infinity} regularity
- Type I blowup exclusion

**Key Tool:** Carleman estimates of the form:
```
integral e^{2phi} |u|^2 <= C integral e^{2phi} |L u|^2
```
where L is a parabolic operator and phi is a carefully chosen weight.

### 5.3 Geometric/Stream Function Methods

**Structure:** Analyze level curves of stream function, use geometry of flow.

**Applies to:**
- Hamel-Nadirashvili: Level curve analysis in 2D
- Korobkov-Pileckas-Russo: Stream function in axisymmetric case

**Limitation:** Requires special geometry (2D or axisymmetric).

### 5.4 Scaling and Dimensional Analysis

**Structure:** Exploit scale invariance to derive constraints.

**Key Observation:** L^3 norm is critical for NS:
```
||lambda u(lambda x)||_3 = ||u||_3
```

**Applies to:** All profile non-existence results.

---

## 6. Implications for Besov Space Extension

### 6.1 Current State for NS Profiles

From our project files, the status is:

| Direction | Space | Result | Method |
|-----------|-------|--------|--------|
| Forward | L^2 | U = 0 | Vorticity energy |
| Forward | L^{3,infinity} | U = 0 | Gradient decay + vorticity |
| Backward | L^2 | U = 0 | Velocity energy |
| Backward | L^3 | U = 0 | NRS 1996 |
| Backward | L^{3,infinity} | U = 0 | Localized NRS |

### 6.2 The Besov Space Question

**Critical Besov spaces for NS:**
```
B^{-1+3/p}_{p,q}(R^3)
```
with p >= 3 is:
- Subcritical if s > -1 + 3/p
- Critical if s = -1 + 3/p
- Supercritical if s < -1 + 3/p

**Question:** Do Liouville theorems extend to critical Besov spaces?

### 6.3 Required Ingredients for Extension

Based on the survey, extending to Besov/Lorentz spaces requires:

1. **Product estimates in Lorentz/Besov spaces:**
   - Weak-type Holder inequalities
   - Bilinear estimates for nonlinear terms

2. **Elliptic regularity in Lorentz spaces:**
   - Mapping properties of Laplacian
   - Bootstrap from profile equation

3. **Appropriate Liouville theorem:**
   - Growth rate must be sublinear for Navier-Stokes (Pan-Li threshold)
   - Euler case requires additional geometric assumptions

---

## 7. Open Problems and Gaps

### 7.1 For the Euler Equations

1. **3D Liouville without symmetry:** No general Liouville theorem for bounded 3D steady Euler (without axisymmetry or Beltrami condition).

2. **Ancient solutions:** No systematic theory of ancient Euler solutions analogous to KNSS for NS.

3. **Sublinear growth:** Unknown whether Liouville holds for Euler with |u| = O(|x|^alpha), 0 < alpha < 1.

### 7.2 For Navier-Stokes Extensions

1. **Weak-L^3 ancient solutions:** The localized NRS argument (backward-L3weak-attack.md) needs rigorous verification.

2. **Besov spaces:** No Liouville theorems known specifically for Besov-type spaces.

3. **Type II blowup:** Liouville methods don't directly apply to Type II (non-self-similar) scenarios.

### 7.3 The Gamma = 1/5 Threshold

**Seregin's condition:** m < 3/5, i.e., gamma = (2m-1)/3 < 1/5.

**What is special about gamma = 1/5?**

This appears related to the scaling of mixed derivative estimates. For a profile with |U| ~ R^gamma:
- |nabla U| ~ R^{gamma-1}
- Dirichlet integral: R^{2(gamma-1)+3} = R^{2gamma+1}

The condition 2gamma + 1 < 0 gives gamma < -1/2, which is **more restrictive** than gamma < 1/5.

**Conclusion:** The gamma = 1/5 threshold likely arises from more subtle considerations in the Carleman estimate or backward uniqueness argument, not directly from energy scaling.

---

## 8. Summary Table of Liouville Results

| Equation | Dimension | Setting | Growth | Result | Reference |
|----------|-----------|---------|--------|--------|-----------|
| NS | 2D | Ancient bounded | gamma = 0 | Trivial | KNSS 2009 |
| NS | 3D | Ancient bounded, axisym no swirl | gamma = 0 | Trivial | KNSS 2009 |
| NS | 3D | Ancient axisym | gamma < 1 | Trivial | Pan-Li 2020 |
| NS | 3D | L^{3,infinity} Cauchy | gamma = -1 | Regular | ESS 2003 |
| NS | 3D | Steady D-solution, axisym no swirl | L^2 grad | Trivial | KPR 2015 |
| Euler | 2D | Steady bounded, no stag | gamma = 0 | Shear flow | H-N 2019 |
| Euler | 3D | Beltrami, L^p p in [2,3] | gamma < -1 | Trivial | Nadirashvili 2014 |
| Euler | 3D | Axisym no swirl, compact supp | - | Must vanish | Gavrilov 2019 |
| Euler | 3D | General steady bounded | gamma = 0 | **OPEN** | - |

---

## 9. Conclusions for the Research Project

### 9.1 Main Takeaways

1. **NS is better understood than Euler:** The viscous term enables energy dissipation arguments not available for Euler.

2. **Axisymmetric case is tractable:** Most positive results assume axisymmetry, which reduces the problem dimension.

3. **Growth rate matters critically:** The Liouville theorem **fails** at linear growth (gamma = 1). The Pan-Li result is optimal.

4. **2D Euler has Liouville:** Hamel-Nadirashvili establishes this under no-stagnation hypothesis.

5. **3D Euler Liouville is open:** No general result for bounded steady 3D Euler without additional structure.

### 9.2 Relevance to Besov Extension

For extending our results to Besov spaces:
- The growth rate must stay in the sublinear regime (gamma < 1)
- Need Lorentz-space versions of the NRS identity
- Carleman estimates may need reformulation for Besov regularity

### 9.3 What's Needed for gamma >= 1/5

To handle the gap region gamma in [1/5, 1):
1. **New multipliers:** The standard |U|U multiplier may not suffice
2. **Finer backward uniqueness:** Need Carleman estimates allowing moderate growth
3. **Geometric constraints:** May require additional assumptions (axisymmetry, Beltrami, etc.)

---

## Sources

- [Koch-Nadirashvili-Seregin-Sverak 2009](https://arxiv.org/abs/0709.3599)
- [Escauriaza-Seregin-Sverak 2003](https://conservancy.umn.edu/items/1ded2377-3cb2-43af-b8ff-f8d52ce5e3fe)
- [Pan-Li 2020](https://arxiv.org/abs/1908.11591)
- [Hamel-Nadirashvili 2019](https://arxiv.org/abs/1703.07293)
- [Nadirashvili Beltrami 2014](https://arxiv.org/abs/1403.1414)
- [Chae 2014](https://arxiv.org/abs/1306.5839)
- [Korobkov-Pileckas-Russo 2015](https://link.springer.com/content/pdf/10.1007/s00021-015-0202-0.pdf)
- [Isolated Steady Euler 2025](https://arxiv.org/html/2407.12938)
- [Gavrilov Compact Support 2019](https://link.springer.com/article/10.1007/s00039-019-00476-6)

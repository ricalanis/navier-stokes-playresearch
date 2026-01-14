# Korobkov-Pileckas-Russo Liouville Theorem: Analysis and Extensions

## Overview

This document analyzes the Korobkov-Pileckas-Russo (KPR) Liouville theorem for axisymmetric Navier-Stokes/Euler equations and explores its potential extensions, particularly in connection with Seregin's framework for Type II blowup exclusion.

**Primary Reference:**
M. Korobkov, K. Pileckas, R. Russo, "The Liouville Theorem for the Steady-State Navier-Stokes Problem for Axially Symmetric 3D Solutions in Absence of Swirl," J. Math. Fluid Mech. 17 (2015), 287-293.
- [Springer PDF](https://link.springer.com/content/pdf/10.1007/s00021-015-0202-0.pdf)

---

## 1. The KPR Result (2015)

### 1.1 Theorem Statement

**Theorem (KPR Navier-Stokes Liouville):**
Let v be an axially symmetric D-solution of the steady Navier-Stokes equations in R^3 without swirl. Then v = 0.

**D-Solution Definition:**
A solution with finite Dirichlet integral:
```
integral_{R^3} |nabla v|^2 dx < infinity
```

**Axially Symmetric Without Swirl:**
In cylindrical coordinates (r, theta, z), the velocity field has the form:
```
v = v_r(r,z) e_r + v_z(r,z) e_z
```
with v_theta = 0 (no swirl component).

### 1.2 Theorem for Euler (Conditional)

**Theorem (KPR Euler, Conditional):**
A conditional Liouville-type theorem holds for axially symmetric solutions to the Euler system, requiring additional decay assumptions on the solution.

The Euler case is weaker because:
1. No viscous dissipation to aid decay estimates
2. Requires explicit assumptions on asymptotic behavior
3. The stream function analysis is more delicate

### 1.3 Hypotheses Summary

| Hypothesis | NS Case | Euler Case |
|------------|---------|------------|
| Axisymmetric | Required | Required |
| No swirl (v_theta = 0) | Required | Required |
| Finite Dirichlet integral | Required | Required + extra decay |
| Smoothness | Smooth | Smooth |
| Domain | R^3 | R^3 |

---

## 2. Proof Technique

### 2.1 Stream Function Approach

For axisymmetric flows without swirl, introduce the Stokes stream function psi:
```
v_r = -(1/r) partial_z psi
v_z = (1/r) partial_r psi
```

The vorticity is purely azimuthal:
```
omega = omega_theta e_theta = -(1/r)[partial_rr psi - (1/r)partial_r psi + partial_zz psi] e_theta
```

### 2.2 Key Steps in KPR Proof

**Step 1: Asymptotic Decay Estimates**

Using the finite Dirichlet integral assumption, establish decay rates:
```
|v(x)| = O(|x|^{-1}) as |x| -> infinity
```

This is achieved through:
- Sobolev embedding in exterior domains
- Weighted energy estimates
- Specific structure of axisymmetric flows

**Step 2: Vorticity Analysis**

For axisymmetric NS without swirl, the vorticity equation becomes:
```
(v . nabla)(omega/r) = nu Delta (omega/r) + nu (2/r^2) partial_r (omega/r)
```

The quantity Gamma = r * omega satisfies a maximum principle-type argument.

**Step 3: Bernoulli-Type Identity**

The KPR approach uses a generalization of Bernoulli's law for weak solutions:
```
H = (1/2)|v|^2 + p = const along streamlines
```

Combined with Morse-Sard type theorems for Sobolev functions, this constrains the level sets of the stream function.

**Step 4: Contradiction via Flux Estimates**

Show that non-trivial D-solutions would violate flux conservation or the finite Dirichlet integral condition.

### 2.3 Role of the Dirichlet Integral

The finite Dirichlet integral condition:
```
integral_{R^3} |nabla v|^2 dx < infinity
```

provides:
1. **Decay control:** Forces v -> 0 at infinity
2. **Energy finiteness:** Total viscous dissipation is finite
3. **Sobolev regularity:** Enables embedding theorems

**Scaling:**
The Dirichlet integral is scale-invariant:
```
integral |nabla v_lambda|^2 dx = integral |nabla v|^2 dx
```
where v_lambda(x) = lambda v(lambda x).

---

## 3. Extensions of KPR

### 3.1 Chae-Weng Alternative Conditions (2016)

**Reference:** D. Chae, S. Weng, "Liouville type theorems for the steady axially symmetric Navier-Stokes and magnetohydrodynamic equations," DCDS 36 (2016), 5267-5285.
- [AIMSciences](https://www.aimsciences.org/article/doi/10.3934/dcds.2016031)

**Main Contribution:**
Replace the Dirichlet integral condition with mild decay conditions.

**Alternative Conditions:**
1. If Gamma = r * u_theta -> 0 as |x| -> infinity, then u = 0
2. If Gamma in L^q(R^3) for some q in [2, infinity), then u = 0

**Significance:** These conditions are easier to verify in some scenarios and don't require explicit Dirichlet integral bounds.

### 3.2 Kozono-Terasawa-Wakasugi Decay Properties (2022)

**Reference:** "Asymptotic properties of steady solutions to the 3D axisymmetric Navier-Stokes equations with no swirl," J. Funct. Anal. 282 (2022).
- [arXiv:2004.13471](https://arxiv.org/abs/2004.13471)

**Main Result:**
A priori decay estimates for vorticity under the assumption that velocity has a generalized finite Dirichlet integral.

**Application:**
Provides a Liouville-type theorem as a corollary of the decay estimates.

### 3.3 Pan-Li Sublinear Growth (2020)

**Reference:** X. Pan, Z. Li, "Liouville theorem of axially symmetric Navier-Stokes equations with growing velocity at infinity," NL Analysis RWA 52 (2020).
- [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1468121820300778)

**Extension:**
Allow solutions with sublinear growth at infinity.

**Theorem:**
For 3D axisymmetric NS, the Liouville theorem holds if:
```
|u(x)| = o(|x|^alpha) as |x| -> infinity, for any alpha < 1
```

**Optimality:**
The exponent alpha = 1 is **sharp** - counterexamples exist for linear growth.

---

## 4. Extension Possibilities

### 4.1 Ancient Solutions (Not Just Steady)

**Current Status:** KPR is for **steady** solutions. Extension to **ancient** solutions is:

**Challenge:**
Ancient solutions satisfy:
```
partial_t v + (v . nabla)v = nu Delta v - nabla p
partial_t v != 0
```

**KNSS Conjecture (Koch-Nadirashvili-Seregin-Sverak 2009):**
- [arXiv:0709.3599](https://arxiv.org/abs/0709.3599)
- [Acta Mathematica](https://projecteuclid.org/journals/acta-mathematica/volume-203/issue-1/Liouville-theorems-for-the-NavierStokes-equations-and-applications/10.1007/s11511-009-0039-6.full)

**KNSS Result:**
Bounded ancient mild solutions of 3D axisymmetric NS **without swirl** are constant.

**KNSS Conjecture:**
Bounded ancient mild solutions of 3D axisymmetric NS **with swirl** are constant.

**Gap:** Can we extend to ancient solutions with growth bounds instead of boundedness?

**Pan-Li-type extension:** For ancient solutions with |u| = o(|x|^alpha), alpha < 1, might expect Liouville.

### 4.2 Small Swirl

**Current Status:** KPR requires v_theta = 0 exactly.

**Question:** What if |v_theta| is "small" in some sense?

**Relevant Results:**

1. **Chae-Weng condition:**
   Gamma = r * v_theta -> 0 at infinity suffices for Liouville

2. **L^q swirl condition:**
   Gamma in L^q for q in [2, infinity) gives Liouville

3. **No small swirl perturbation:**
   As of now, no result handles "small but nonzero" swirl uniformly

**Difficulty:**
Swirl introduces additional nonlinear terms in vorticity transport that break the structure used in KPR.

### 4.3 Growth Bounds Instead of Dirichlet Integral

**Question:** Replace integral_{R^3} |nabla v|^2 < infinity with:
```
integral_{B(R)} |v|^2 dx = O(R^gamma) as R -> infinity
```

**Analysis:**

For Dirichlet integral to be finite:
```
integral |nabla v|^2 ~ integral_{R}^{2R} |v|^2/r^2 * r^2 dr ~ |v|^2_{typical} * R
```

If |v| ~ R^{-1} (standard decay for D-solutions):
```
integral_{B(R)} |v|^2 ~ R^{-2} * R^3 = R^1
```

So finite Dirichlet integral corresponds to gamma = 1 in the L^2 growth bound.

**Hierarchy:**
| Condition | Growth Exponent gamma |
|-----------|----------------------|
| Bounded | 0 (automatic gamma = 3 for L^2) |
| L^3 | gamma = 0 |
| Dirichlet finite | gamma = 1 |
| Sublinear (Pan-Li) | gamma < 5 |

**For Seregin's framework (m < 3/5):**
```
integral_{B(b)} |U|^2 = O(b^{2m-1}) with m < 3/5
```
gives gamma = 2m - 1 < 1/5.

This is MORE RESTRICTIVE than Dirichlet integral (gamma = 1).

---

## 5. Connection to Seregin's Gap

### 5.1 Seregin's Framework

**Reference:** G. Seregin, "A note on certain scenarios of Type II blowups..." arXiv:2507.08733 (July 2025).

**Key Result (Proposition 4.1):**
For m in (1/2, 3/5), ancient Euler solutions U with:
```
sup_{b > 0} { (1/b^{gamma m_1}) integral_{B(b)} |U|^2 dy } < infinity
```
must satisfy U = 0.

Here gamma = 3, m_1 = 2m - 1, so the condition is:
```
integral_{B(b)} |U|^2 = O(b^{3(2m-1)}) = O(b^{6m-3})
```

For m = 1/2: exponent = 0 (bounded L^2 mass)
For m = 3/5: exponent = 0.6 (mild growth allowed)

### 5.2 Comparing Conditions

| Framework | Condition Type | Exponent | Range |
|-----------|---------------|----------|-------|
| KPR | Dirichlet integral | implicit | finite |
| Pan-Li | Pointwise decay | alpha < 1 | sublinear |
| Seregin | L^2 growth | gamma < 0.6 | m < 3/5 |
| KNSS | Boundedness | alpha = 0 | bounded |

### 5.3 Can These Be Related for Axisymmetric Flows?

**Key Observation:**
For axisymmetric flows without swirl, KPR's Dirichlet condition implies Seregin's L^2 growth condition.

**Proof sketch:**
1. Dirichlet integral finite => |v| = O(|x|^{-1}) at infinity (by Sobolev embedding)
2. Therefore integral_{B(R)} |v|^2 ~ R^{-2} * R^3 = R (at most)
3. This is gamma = 1, which is larger than Seregin's gamma < 0.6

**Problem:** The implication goes the wrong way!

KPR's condition is WEAKER than Seregin's growth bound.

**Interpretation:**
- Seregin needs faster-decaying solutions (gamma < 0.6)
- KPR handles slower-decaying solutions (gamma ~ 1)
- But KPR is only for STEADY, not ANCIENT

### 5.4 The Real Question

**For axisymmetric ancient Euler WITHOUT swirl:**

Does:
```
integral_{B(b)} |U|^2 = O(b^gamma) with gamma < 1/3
```
imply U = 0?

**Note:** gamma < 1/3 is equivalent to m < 2/3 in Seregin's parametrization (since gamma = 6m - 3 gives m = (gamma + 3)/6, and gamma < 1/3 gives m < 19/18... this needs rechecking).

**Corrected relationship:**
From integral_{B(b)} |U|^2 = O(b^{2m-1}), we have:
- m = 1/2 => exponent = 0 (bounded)
- m = 3/5 => exponent = 1/5

So gamma < 1/3 corresponds to m < (1/3 + 1)/2 = 2/3, which is OUTSIDE Seregin's range.

**The actual Seregin gap:**
m in (1/2, 3/5) gives gamma = 2m - 1 in (0, 1/5).

### 5.5 Extending Seregin's m < 3/5 Constraint

To extend beyond m < 3/5, we need:

1. **Improved Liouville for Ancient Euler:**
   Currently works for m < 3/5 via energy/Carleman methods.
   Need: Liouville for m in [3/5, 1)?

2. **Connection to Axisymmetric Structure:**
   KPR handles steady axisymmetric with Dirichlet (gamma ~ 1).
   Can this be adapted to ancient axisymmetric?

3. **Viscous vs Inviscid:**
   KPR is for Navier-Stokes (viscous).
   Seregin's limit is Euler (inviscid).
   The inviscid limit is singular - estimates may not transfer.

---

## 6. Key Question: Axisymmetric Ancient Euler Without Swirl

### 6.1 Precise Statement

**Conjecture:**
Let U be an ancient solution of the 3D Euler equations:
```
partial_tau U + (U . nabla)U = -nabla P, div U = 0
```
on R^3 x (-infinity, 0), which is:
1. Axially symmetric
2. Without swirl (U_theta = 0)
3. Satisfies integral_{B(b)} |U|^2 = O(b^gamma) with gamma < 1/3

Then U = 0.

### 6.2 Why gamma < 1/3 Matters

If this conjecture holds, it would:

1. **Extend Seregin's exclusion:**
   Currently m < 3/5 (gamma < 1/5).
   With gamma < 1/3, we get m < 2/3.

2. **New Type II exclusion:**
   Would rule out Type II blowup scenarios in a larger parameter range.

3. **Bridge to KPR:**
   KPR handles gamma ~ 1 for steady solutions.
   Gap between gamma = 1/3 and gamma = 1 remains.

### 6.3 Potential Approaches

**Approach 1: Stream Function for Ancient Solutions**

Extend KPR's stream function analysis to time-dependent case:
- Introduce time-dependent stream function psi(r, z, tau)
- Analyze level sets as tau -> -infinity
- Use asymptotic self-similarity arguments

**Approach 2: Vorticity Formulation**

For axisymmetric Euler without swirl:
```
D/Dt (omega_theta/r) = 0
```

The quantity omega_theta/r is materially conserved!

**Implication:**
If omega_theta/r -> 0 at infinity, then omega_theta/r = 0 everywhere along particle paths traced backward.

**Challenge:** Control behavior as tau -> -infinity.

**Approach 3: Energy-Vorticity Identity**

For Euler:
```
d/dt integral |u|^2 = 0 (energy conservation)
```

But also:
```
d/dt integral |omega|^2 = ? (need enstrophy analysis)
```

For axisymmetric without swirl, enstrophy satisfies:
```
integral |omega_theta|^2 (1/r^2) dV = integral |omega_theta/r|^2 r^2 dV
```

**Approach 4: Backward Characteristics**

Along backward particle trajectories:
```
dX/dtau = U(X, tau)
```

For U with growth O(|x|^{gamma/3}), particles move at most O(|tau|^{???}) backward.

If particles stay bounded as tau -> -infinity, use KNSS-type arguments.

---

## 7. Summary and Open Problems

### 7.1 What KPR Establishes

1. **Steady NS, axisymmetric, no swirl:**
   Dirichlet integral finite => v = 0 (unconditional)

2. **Steady Euler, axisymmetric, no swirl:**
   Dirichlet integral + extra decay => v = 0 (conditional)

3. **Proof technique:**
   Stream function geometry + Bernoulli law + Morse-Sard

### 7.2 What Extensions Exist

1. **Chae-Weng (2016):** Alternative decay conditions instead of Dirichlet
2. **Pan-Li (2020):** Sublinear growth allowed, alpha < 1 is sharp
3. **Kozono et al (2022):** Vorticity decay from Dirichlet assumption

### 7.3 What Remains Open

| Question | Status | Difficulty |
|----------|--------|------------|
| Ancient NS axisymmetric no swirl, bounded | Solved (KNSS) | - |
| Ancient NS axisymmetric no swirl, sublinear | Likely true (Pan-Li type) | Medium |
| Ancient Euler axisymmetric no swirl, bounded | Open | Hard |
| Ancient Euler axisymmetric no swirl, O(b^gamma) | Open | Hard |
| Steady NS with small swirl | Open | Hard |
| Ancient NS with small swirl | Open (KNSS conjecture) | Very Hard |

### 7.4 Connection to Seregin's Gap

**Current state:**
Seregin's Proposition 4.1 gives Liouville for ancient Euler with growth bound, but only for m in (1/2, 3/5).

**The gap m in [3/5, 1):**
- Requires new Liouville theorem for ancient Euler
- Axisymmetric no swirl is most tractable special case
- KPR techniques might adapt but face inviscid obstacle

**Strategy:**
1. Prove Liouville for ancient axisymmetric Euler without swirl with O(b^gamma), gamma < 1
2. This would close the gap for the special axisymmetric case
3. Might provide insight for general case

---

## 8. Technical Details for Potential Extension

### 8.1 KPR Proof Adaptation for Ancient Case

**Step 1: Time-Dependent Stream Function**

For axisymmetric incompressible flow, define:
```
v_r = -(1/r) partial_z psi(r, z, tau)
v_z = (1/r) partial_r psi(r, z, tau)
```

**Step 2: Evolution Equation for psi**

From Euler equations:
```
partial_tau (Delta* psi) + {psi, Delta* psi}/(r^2) = 0
```
where Delta* = partial_rr - (1/r)partial_r + partial_zz and {,} is a Poisson bracket.

**Step 3: Material Conservation**

The quantity omega_theta/r = -Delta* psi / r^2 is materially conserved:
```
D/Dtau (omega_theta/r) = 0
```

**Step 4: Liouville-Type Argument**

If |omega_theta/r| -> 0 at spatial infinity uniformly in tau, and particles trace back to spatial infinity as tau -> -infinity, then omega_theta/r = 0 everywhere.

**Main Challenge:**
Controlling particle trajectories for ancient solutions with only growth bounds.

### 8.2 Required Estimates

**Estimate 1: Particle Path Bounds**

For |U| ~ |x|^{gamma/3} growth:
```
|dX/dtau| ~ |X|^{gamma/3}
```

Solving: |X(tau)| ~ |tau|^{3/(3-gamma)} for gamma < 3.

For gamma < 1/3: |X(tau)| ~ |tau|^{9/8}, slow enough for bounded enstrophy arguments?

**Estimate 2: Enstrophy Decay**

Need:
```
integral |omega_theta/r|^2 r drdz -> 0 as tau -> -infinity
```
or remains bounded.

**Estimate 3: Energy-Enstrophy Relation**

For axisymmetric Euler without swirl:
```
E = (1/2) integral |v|^2 = const
Omega = (1/2) integral |omega_theta/r|^2 r^2 dV = ???
```

### 8.3 Obstruction to Extension

**The Inviscid Limit Problem:**

KPR works for Navier-Stokes because:
1. Viscous dissipation provides decay estimates
2. Parabolic regularity enables bootstrap
3. Maximum principles apply to vorticity

For Euler:
1. No dissipation - energy conserved, not dissipated
2. Hyperbolic regularity is weaker
3. Vorticity is transported, not diffused

**Key difference:**
In NS, Dirichlet integral bounds dissipation over ALL TIME.
In Euler, energy is conserved but doesn't constrain local behavior.

---

## 9. Conclusions

### 9.1 For Seregin's Framework

The KPR Liouville theorem provides a template for axisymmetric analysis, but:
1. It's for steady (not ancient) solutions
2. It requires viscosity (Navier-Stokes, not Euler)
3. The Dirichlet condition is weaker than Seregin's growth bound

### 9.2 Potential Path Forward

To extend Seregin's m < 3/5 to larger m using axisymmetric structure:

1. **Prove:** Ancient axisymmetric Euler without swirl with L^2 growth O(b^gamma), gamma < 1, implies U = 0

2. **Method:** Adapt KPR stream function + material conservation of omega_theta/r

3. **Main obstacle:** Controlling backward particle trajectories without viscous decay

### 9.3 Assessment

**Likelihood of success:** Medium

**Justification:**
- The axisymmetric no-swirl case has special structure (material conservation)
- This structure hasn't been fully exploited for ancient Euler
- The gap between steady (KPR) and ancient (needed) is significant but possibly bridgeable

**Recommended next step:**
Develop detailed particle trajectory estimates for ancient axisymmetric Euler with growth bounds, following the approach in Section 8.

---

## Sources

### Primary References
- [Korobkov-Pileckas-Russo 2015](https://link.springer.com/content/pdf/10.1007/s00021-015-0202-0.pdf)
- [Koch-Nadirashvili-Seregin-Sverak 2009](https://arxiv.org/abs/0709.3599)
- [Chae-Weng 2016](https://www.aimsciences.org/article/doi/10.3934/dcds.2016031)

### Extension Results
- [Pan-Li 2020 Growing Velocity](https://www.sciencedirect.com/science/article/abs/pii/S1468121820300778)
- [Kozono-Terasawa-Wakasugi 2022](https://arxiv.org/abs/2004.13471)
- [Lei-Zhang 2011](https://arxiv.org/abs/1011.5066)

### 2D Euler and Beltrami
- [Hamel-Nadirashvili 2019 Plane Euler](https://arxiv.org/abs/1703.07293)
- [Nadirashvili 2014 Beltrami](https://arxiv.org/abs/1403.1414)

### Seregin Framework
- Seregin, G. "A note on certain scenarios of Type II blowups..." arXiv:2507.08733 (July 2025)

### Additional Context
- [Escauriaza-Seregin-Sverak L^{3,infinity} 2003](https://conservancy.umn.edu/items/1ded2377-3cb2-43af-b8ff-f8d52ce5e3fe)
- [Liouville theorems for NS and applications, Acta Math](https://projecteuclid.org/journals/acta-mathematica/volume-203/issue-1/Liouville-theorems-for-the-NavierStokes-equations-and-applications/10.1007/s11511-009-0039-6.full)

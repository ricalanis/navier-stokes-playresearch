# Axisymmetric Navier-Stokes Equations: Regularity Theory Survey

## Date: January 13, 2026

This document provides a comprehensive survey of regularity results for axisymmetric solutions to the incompressible Navier-Stokes equations, with particular emphasis on the exclusion of Type I singularities and recent developments on Type II blowup analysis.

---

## 1. Axisymmetric Formulation in Cylindrical Coordinates

### 1.1 Coordinate System and Velocity Decomposition

In cylindrical coordinates (r, theta, z) with the z-axis as the symmetry axis:

**Velocity field:**
```
u = u^r(r,z,t) e_r + u^theta(r,z,t) e_theta + u^z(r,z,t) e_z
```

where:
- `r` = radial distance from the z-axis
- `theta` = azimuthal angle (solution independent of theta)
- `z` = axial coordinate
- `e_r, e_theta, e_z` = orthonormal basis vectors

### 1.2 The Swirl Component

**Definition.** The *swirl* (or angular momentum) is defined as:
```
Gamma = r * u^theta
```

This quantity plays a crucial role in regularity theory because it satisfies a *transport equation* without pressure:

**Transport Equation for Gamma:**
```
partial_t Gamma + u^r partial_r Gamma + u^z partial_z Gamma = nu * (Delta Gamma - (2/r) partial_r Gamma)
```

where `Delta` is the Laplacian and `nu` is the kinematic viscosity.

**Key Property:** The equation for Gamma is *pressureless*, enabling the application of De Giorgi-Nash-Moser techniques.

### 1.3 Stream Function-Vorticity Formulation

For axisymmetric flows, the Stokes stream function psi defines velocity:
```
u^z = (1/r) partial_r psi
u^r = -(1/r) partial_z psi
```

This automatically satisfies incompressibility: `div(u) = 0`.

**Vorticity:** The azimuthal vorticity is:
```
omega = omega^theta = partial_z u^r - partial_r u^z
```

**Stream Function Equation:**
```
partial_zz psi + partial_rr psi - (1/r) partial_r psi = -omega * r
```

**Vorticity Transport Equation:**
```
partial_t omega + u^r partial_r omega + u^z partial_z omega - (u^r/r) omega
    = nu * (partial_zz omega + partial_rr omega + (1/r) partial_r omega - omega/r^2)
```

The term `-(u^r/r) omega` represents **vortex stretching** in the axisymmetric geometry.

---

## 2. Classical Regularity Results (1968)

### 2.1 Ladyzhenskaya Theorem (No Swirl)

**Theorem (Ladyzhenskaya, 1968).** *Let u_0 be smooth, axisymmetric initial data with `u^theta = 0` (no swirl) and finite energy. Then the corresponding solution to the 3D incompressible Navier-Stokes equations exists globally in time and remains smooth.*

**Reference:** O.A. Ladyzhenskaya, "Unique global solvability of the three-dimensional Cauchy problem for the Navier-Stokes equations in the presence of axial symmetry," Zap. Nauchn. Sem. Leningrad. Otdel. Math. Inst. Steklov. (LOMI) 7, 155-177 (1968).

**Key Insight:** Without swirl, the problem reduces to an essentially 2D structure. The vorticity omega^theta/r satisfies a maximum principle, preventing unbounded growth.

### 2.2 Ukhovskii-Yudovich Theorem

**Theorem (Ukhovskii-Yudovich, 1968).** *For axisymmetric flows in R^3 without swirl, weak solutions are regular for all time.*

**Reference:** M.R. Ukhovskii and V.I. Yudovich, "Axially symmetric flows of ideal and viscous fluids filling the whole space," J. Appl. Math. Mech. 32, 52-61 (1968).

**Interpretation:** The case u^theta = 0 (no swirl) is completely resolved. **The open problem concerns axisymmetric flows WITH nonzero swirl.**

---

## 3. Modern Regularity Results: Type I Exclusion

### 3.1 Definition of Type I and Type II Singularities

**Definition.** Let z = (x,t) be a singular point of a solution v to the Navier-Stokes equations. Define the scale-invariant quantities:

```
A(v,r) = (1/r) integral_{Q_r(z)} |v|^3 dx dt
E(v,r) = sup_{t in I_r} (1/r) integral_{B_r(x_0)} |v|^2 dx
C(v,r) = (1/r^2) integral_{Q_r(z)} |nabla v|^2 dx dt
```

where Q_r(z) is a parabolic cylinder.

**Type I Singularity:** The point z is a *Type I singularity* if:
```
g := inf{lim sup_{r->0} A(v,r), lim sup_{r->0} E(v,r), lim sup_{r->0} C(v,r)} < infinity
```

Equivalently, Type I means the blowup rate is bounded by:
```
|v(x,t)| <= C / sqrt(T - t)
```

**Type II Singularity:** The point z is a *Type II singularity* if it is singular and g = infinity.

Type II singularities would have faster-than-scale-invariant blowup rates.

### 3.2 Chen-Strain-Yau-Tsai Theorem (2008-2009)

**Theorem (Chen-Strain-Tsai-Yau, 2008-2009).** *Axisymmetric suitable weak solutions to the Navier-Stokes equations do not have Type I blowups.*

More precisely:

**Theorem.** *Let v be an axisymmetric strong solution to the incompressible Navier-Stokes equations in R^3 with nontrivial swirl. Suppose for some 0 <= epsilon <= 1:*
```
|v(x,t)| <= C_* * r^(-1+epsilon) * |t|^(-epsilon/2)
```
*Then the solution is smooth (no singularity forms).*

**References:**
1. C.-C. Chen, R.M. Strain, T.-P. Tsai, H.-T. Yau, "Lower bound on the blow-up rate of the axisymmetric Navier-Stokes equations," Int. Math. Res. Not. IMRN (2008), no. 9, Art. ID rnn016, 31 pages.
2. C.-C. Chen, R.M. Strain, T.-P. Tsai, H.-T. Yau, "Lower bounds on the blow-up rate of the axisymmetric Navier-Stokes equations II," Comm. Partial Differential Equations 34 (2009), 203-232.

**Method of Proof:**
1. Apply De Giorgi-Nash-Moser iteration to the equation for Gamma = r * u^theta
2. Exploit the *pressureless* structure of the swirl equation
3. Obtain Holder continuity of Gamma near the symmetry axis
4. Use blow-up scaling to derive contradictions

**Key Lemma (De Giorgi-Nash-Moser for Swirl).** *The swirl Gamma = r u^theta satisfies:*
```
|Gamma|_{C^alpha(Q_{r/2})} <= C * (||Gamma||_{L^infinity(Q_r)} + ||f||_{L^p(Q_r)})
```
*for appropriate forcing terms f, giving Holder continuity at r = 0.*

### 3.3 Koch-Nadirashvili-Seregin-Sverak Liouville Theorem (2009)

**Theorem (Koch-Nadirashvili-Seregin-Sverak, 2009).** *Let (v, p) be a bounded ancient mild solution to the 3D Navier-Stokes equations in R^3 x (-infinity, 0). If v is axisymmetric and swirl-free (u^theta = 0), then v is constant.*

**Reference:** G. Koch, N. Nadirashvili, G.A. Seregin, V. Sverak, "Liouville theorems for the Navier-Stokes equations and applications," Acta Math. 203 (2009), 83-105. [arXiv:0709.3599](https://arxiv.org/abs/0709.3599)

**Conjecture (KNSS).** *Any bounded ancient mild solution of the 3D axially symmetric Navier-Stokes equations is constant* (including solutions with swirl).

**Application:** These Liouville theorems are used in blow-up analysis. If a singularity exists, rescaling produces an ancient solution. Proving such solutions are trivial excludes the singularity.

### 3.4 Seregin-Sverak Type I Exclusion (2009)

**Theorem (Seregin-Sverak, 2009).** *Let v be an axisymmetric solution to the 3D Navier-Stokes equations. If v satisfies a bounded scale-invariant energy quantity (Type I condition), then v is smooth. That is, axially symmetric energy solutions have no Type I blowups.*

**Reference:** G. Seregin and V. Sverak, "On Type I singularities of the local axi-symmetric solutions of the Navier-Stokes equations," Comm. Partial Differential Equations 34 (2009), 171-201.

**Key Technical Point:** The proof combines:
1. Caffarelli-Kohn-Nirenberg partial regularity (reduces problem to the axis r = 0)
2. De Giorgi-Nash-Moser bounds for the swirl equation
3. Scaling and compactness arguments

---

## 4. Lei-Zhang Regularity Criteria (2011)

### 4.1 Liouville Theorem for Axisymmetric NS

**Theorem (Lei-Zhang, 2011).** *Let v be a bounded ancient solution to the axisymmetric Navier-Stokes equations. Suppose the radial-axial velocity components satisfy certain scaling-invariant conditions and:*
```
r * v^theta(x, 0) in L^infinity
```
*Then the solution is regular (smooth).*

**Reference:** Z. Lei and Q.S. Zhang, "A Liouville theorem for the axially-symmetric Navier-Stokes equations," J. Funct. Anal. 261 (2011), 2323-2345.

**Key Result:** Under suitable conditions on the radial-axial flow, the swirl Gamma = r v^theta is Holder continuous at r = 0, t = 0.

### 4.2 Criticality Result (2017)

**Theorem (Lei-Zhang, 2017).** *Smooth solutions to the axisymmetric Navier-Stokes equations obey a maximum principle. All solutions with initial data in H^{1/2} are smooth globally in time if r v^theta satisfies a Form Boundedness Condition (FBC) that is invariant under the natural scaling of the Navier-Stokes equations.*

**Reference:** Z. Lei and Q.S. Zhang, "Criticality of the axially symmetric Navier-Stokes equations," Pacific J. Math. 289 (2017), 169-187. [arXiv:1505.02628](https://arxiv.org/abs/1505.02628)

### 4.3 A Priori Velocity Bounds (2016)

**Theorem (Lei-Navas-Zhang, 2016).** *For axisymmetric solutions, a priori bounds on velocity can be established under suitable conditions on the swirl component.*

**Reference:** Z. Lei, E.A. Navas, Q.S. Zhang, "A priori bound on the velocity in axially symmetric Navier-Stokes equations," Comm. Math. Phys. 341 (2016), 289-307.

---

## 5. Seregin's Type II Analysis (2024)

### 5.1 Main Paper

**Reference:** G. Seregin, "On Type II blowups of axisymmetric solutions to the Navier-Stokes equations," arXiv:2402.13229 (2024). Published in Comm. Pure Appl. Anal. 2024.

**Context:** Since Type I blowups are excluded for axisymmetric solutions, to complete the regularity theory one must study **potential Type II blowups**.

### 5.2 Main Results

**Proposition 5.1 (Seregin 2024).** *Under specific Type II blowup conditions (inequalities 1.2, 1.3, 1.5 in the paper), there exists a nontrivial solution (u, p) to the Euler equations satisfying bounded scaled quantities and an energy inequality on the half-space.*

**Proposition 5.2 (Seregin 2024).** *If the integrated vorticity component remains finite at some time t_0, it stays constant for all t <= 0 under restriction (2.10).*

**Proposition 5.3 (Seregin 2024).** *Potential Type II singularities cannot occur for axisymmetric solutions under condition (2.13) unless fundamental assumptions fail.*

### 5.3 The Euler Scaling Method

**Key Tool:** The Euler scaling transformation:
```
lambda^alpha * v(lambda x, lambda^{alpha+1} t), lambda^{2alpha} * q(lambda x, lambda^{alpha+1} t)
```
where alpha = 2 - m for some parameter m.

**Critical Observation:** Under Euler scaling, the limiting profile has:
- u^theta = 0 (swirl vanishes in the limit)
- The flow is irrotational unless trivial

This geometric constraint, combined with axial symmetry, **severely restricts possible singularities**.

### 5.4 Further Developments (2025)

**Reference:** G. Seregin, "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations," arXiv:2507.08733 (2025).

**Result:** Studies various scenarios of potential Type II blowups. Shows that under certain assumptions, such blowups cannot happen. The method uses Euler scaling and Liouville-type theorems for ancient solutions to the Euler system.

---

## 6. Why Axisymmetric is Special

### 6.1 Reduced Dimensionality (2.5D Structure)

- Solutions depend on (r, z, t), not (x, y, z, t)
- The azimuthal component u^theta decouples from pressure
- Stream function formulation reduces to 2 scalar equations

### 6.2 Vortex Stretching Has Specific Structure

In general 3D:
```
(omega . nabla) u  [arbitrary vortex stretching term]
```

In axisymmetric:
```
-(u^r / r) omega  [constrained to radial direction]
```

The vorticity can only be stretched/compressed radially, limiting amplification mechanisms.

### 6.3 Angular Momentum Conservation

The transport equation for Gamma = r u^theta:
```
D_t Gamma = nu * (Delta - 2/r partial_r) Gamma
```

- No pressure term
- Maximum principle applies
- De Giorgi-Nash-Moser regularity theory is available

### 6.4 Summary of What's Proven

| Configuration | Type I | Type II | Global Regularity |
|--------------|--------|---------|-------------------|
| No swirl (u^theta = 0) | Excluded | Excluded | **PROVEN** (1968) |
| With swirl | **Excluded** (2008-2009) | Partially excluded | **OPEN** |

---

## 7. The Remaining Gap

### 7.1 Current State

**Proven:**
- Type I singularities are impossible for axisymmetric NS (Chen-Strain-Yau-Tsai, Seregin-Sverak)
- Various scenarios of Type II are excluded (Seregin 2024, 2025)
- Swirl-free case is completely regular (Ladyzhenskaya, Ukhovskii-Yudovich)

**Open:**
- Complete exclusion of Type II blowups for axisymmetric flows with swirl
- Global regularity for axisymmetric NS with arbitrary swirl

### 7.2 What Would Close the Gap

To prove global regularity for axisymmetric NS with swirl, one needs:

1. **Complete Liouville theorem:** Prove that ALL bounded ancient solutions (with swirl) are constant (KNSS conjecture)

2. **Type II exclusion:** Show that no Type II blowup scenario is compatible with:
   - Energy inequality
   - Axisymmetric structure
   - Properties of the swirl equation

3. **Direct a priori estimates:** Establish global bounds on:
   - ||v||_{L^infinity}
   - ||omega||_{L^infinity}
   - ||Gamma||_{L^infinity}

### 7.3 Obstructions

- Type II blowups are more elusive (no natural scaling)
- The swirl u^theta couples the system in complex ways
- Standard energy methods give weaker control than in 2D

---

## 8. Related Results and Context

### 8.1 Caffarelli-Kohn-Nirenberg Theorem (1982)

**Theorem (CKN, 1982).** *For any suitable weak solution to the 3D Navier-Stokes equations, the 1-dimensional parabolic Hausdorff measure of the singular set is zero.*

**Reference:** L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," Comm. Pure Appl. Math. 35 (1982), 771-831.

**Implication for Axisymmetric:** If a singularity exists, it must be concentrated on the axis r = 0. The CKN theorem combined with axisymmetric structure makes regularity proofs more tractable.

### 8.2 Connection to Euler Equations

The Euler scaling used by Seregin produces ancient Euler solutions in the limit. Liouville theorems for Euler become relevant:

**Theorem.** *Smooth, bounded, stationary solutions to the 3D Euler equations in R^3 with finite energy are constant.*

This connects NS regularity to Euler rigidity.

---

## 9. Key References

### Foundational Papers
1. O.A. Ladyzhenskaya (1968) - Global regularity without swirl
2. M.R. Ukhovskii, V.I. Yudovich (1968) - Regularity without swirl
3. L. Caffarelli, R. Kohn, L. Nirenberg (1982) - Partial regularity

### Type I Exclusion
4. C.-C. Chen, R.M. Strain, T.-P. Tsai, H.-T. Yau (2008, 2009) - Lower bounds on blowup rate
5. G. Seregin, V. Sverak (2009) - Type I singularities excluded
6. G. Koch, N. Nadirashvili, G. Seregin, V. Sverak (2009) - Liouville theorems

### Modern Developments
7. Z. Lei, Q.S. Zhang (2011) - Liouville theorem for axisymmetric
8. Z. Lei, Q.S. Zhang (2017) - Criticality of axisymmetric NS
9. G. Seregin (2024) - [Type II blowups for axisymmetric](https://arxiv.org/abs/2402.13229)
10. G. Seregin (2025) - [Type II scenarios](https://arxiv.org/html/2507.08733v2)

### Review Articles
11. Q.S. Zhang, X. Pan (2021) - [Review of axially symmetric NS](https://arxiv.org/html/2101.04905v2)

---

## 10. Conclusion

The axisymmetric Navier-Stokes equations represent the most tractable non-trivial case of the 3D regularity problem. The exclusion of Type I singularities (proven by 2009) represents major progress. The remaining challenge is to completely exclude Type II blowups, which would establish global regularity for this important class of solutions.

Seregin's 2024 work provides new tools (Euler scaling + Liouville theorems) that exclude specific Type II scenarios. A complete resolution likely requires either:

1. A general Liouville theorem for ancient axisymmetric solutions with swirl, or
2. Direct a priori estimates exploiting the special structure of the swirl equation.

The axisymmetric case, while not solving the general Millennium Problem, would demonstrate that the fundamental mechanisms preventing blowup in Navier-Stokes can be rigorously established in geometrically constrained settings.

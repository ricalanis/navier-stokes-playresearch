# Ancient Solutions to Axisymmetric Euler Equations and Liouville-Type Results

**Research Summary:** Investigation of ancient solutions, Liouville theorems, and their role in Navier-Stokes regularity theory.

---

## 1. Definitions and Context

### 1.1 Ancient Solutions

An **ancient solution** to the Euler (or Navier-Stokes) equations is a solution defined for all t in (-infty, 0]. These arise naturally as:

1. **Blowup limits under Seregin's rescaling:** If u(x,t) blows up at (0,T), define
   ```
   v^{lambda,alpha}(y,tau) = lambda^alpha v(lambda y, T + lambda^{alpha+1} tau)
   ```
   Taking lambda -> 0 produces an ancient solution (if limits exist).

2. **Backward-in-time analysis:** Understanding asymptotic behavior.

3. **Classification problems:** What ancient solutions exist?

### 1.2 Axisymmetric Setting

In cylindrical coordinates (r, theta, z):
```
u = u^r(r,z,t) e_r + u^theta(r,z,t) e_theta + u^z(r,z,t) e_z
```

**Key quantities:**
- **Swirl velocity:** u^theta (azimuthal component)
- **Swirl-free:** u^theta = 0 (velocity in meridional plane only)
- **Circulation:** Gamma = r u^theta (conserved along particle paths in Euler)
- **Azimuthal vorticity:** omega_theta = partial_z u^r - partial_r u^z

### 1.3 Why Axisymmetry Helps

Axisymmetric flow WITHOUT swirl reduces effectively to 2D:
- The vorticity is scalar (omega_theta only)
- Vortex stretching is controlled
- Global wellposedness is known for Euler

Axisymmetric flow WITH swirl retains 3D complexity:
- Vortex stretching can amplify vorticity
- Global regularity is OPEN
- Provides a "controlled" setting to study 3D phenomena

---

## 2. Known Ancient Solutions

### 2.1 Hill's Spherical Vortex (Euler, No Swirl)

**Discovery:** M.J.M. Hill (1894)

**Properties:**
- Steady solution (trivially ancient)
- Axisymmetric, no swirl
- Vorticity confined to a ball: omega_theta/r = const inside, zero outside
- Propagates at constant velocity
- Finite energy (compact support)

**Mathematical form:**
Inside the sphere of radius a:
```
omega_theta = (15U/2a^2) r
```
where U is the propagation speed.

**Significance:** The only known non-trivial axisymmetric Euler solution with compact support in the no-swirl case.

**Stability:** Proven by Cao-Wan-Wang-Zhan (CPAM, 2023) using variational methods from Friedman-Turkington (1981).

**References:**
- [Hill's spherical vortex - Wikipedia](https://en.wikipedia.org/wiki/Hill's_spherical_vortex)
- [Stability of Hill's spherical vortex](https://arxiv.org/abs/2011.06808)

### 2.2 Burgers Vortex (Navier-Stokes, With Swirl)

**Note:** This is a Navier-Stokes solution, NOT Euler.

A steady balance between:
- Viscous diffusion (spreading the vortex)
- Strain field (compressing the vortex)

Not directly relevant to inviscid Euler ancient solutions.

### 2.3 Classification Status

**Known steady axisymmetric Euler solutions:**
1. Uniform flows (trivial)
2. Hill's spherical vortex (no swirl)
3. Prendergast vortex (with swirl, discovered 1956 in plasma context)
4. Moffatt's class (1986): propagating vortices without shape change

**Known non-trivial ancient solutions:**
- Hill vortex family (traveling frames make it time-dependent)
- Time-dependent perturbations remain largely unexplored

---

## 3. Liouville Theorems: Navier-Stokes Results

### 3.1 The KNSS Theorem (2009)

**Authors:** Koch, Nadirashvili, Seregin, Sverak

**Paper:** "Liouville theorems for the Navier-Stokes equations and applications," Acta Mathematica 203 (2009), 83-105.

**Main Results:**

**2D Case:**
> Bounded ancient solutions of the 2D Navier-Stokes equations are either constant or of the form u(x,t) = b(t).

**3D Axisymmetric, No Swirl:**
> Any bounded ancient mild solution of the 3D axisymmetric Navier-Stokes equations WITHOUT swirl is constant.

**3D Axisymmetric, With Swirl:**
> Conjecture: Any bounded ancient mild solution is constant. PROVED when solution is swirl-free.

**Significance:** If bounded ancient NS solutions are trivial, then Type I blowup rescaling leads to contradiction -> no Type I blowup in axisymmetric case.

**References:**
- [arXiv:0709.3599](https://arxiv.org/abs/0709.3599)
- [Acta Mathematica (Springer)](https://link.springer.com/article/10.1007/s11511-009-0039-6)

### 3.2 Extensions: Growing Velocity at Infinity

**Authors:** Pan, Li

**Paper:** "Liouville theorem of axially symmetric Navier-Stokes equations with growing velocity at infinity" (arXiv:1908.11591, 2019)

**Key Result:**
The bounded condition can be relaxed to SUBLINEAR growth:
```
|u(x)| = O(|x|^gamma) with gamma < 1
```

**Optimality:**
> Linear growth (gamma = 1) allows counterexamples. Thus gamma < 1 is SHARP.

**Implication:** For ancient axisymmetric NS:
- Bounded -> constant (KNSS)
- Sublinear growth -> constant (Pan-Li)
- Linear growth -> possibly non-trivial

**References:**
- [arXiv:1908.11591](https://arxiv.org/abs/1908.11591)
- [Review by Pan-Zhang](https://arxiv.org/abs/2101.04905)

### 3.3 Lei-Zhang Result (2011)

**Paper:** "A Liouville theorem for the axially-symmetric Navier-Stokes equations"

**Result:** Under scaling-invariant conditions on the radial-axial velocity, Holder continuity of Gamma = r u^theta at the axis is proved.

This gives a partial proof of the KNSS conjecture.

**Reference:** [arXiv:1011.5066](https://arxiv.org/abs/1011.5066)

---

## 4. Liouville Theorems: Euler Results

### 4.1 Jiu-Xin Theorem for Steady Euler (2009)

**Paper:** "Smooth Approximations and Exact Solutions of the 3D Steady Axisymmetric Euler Equations," Comm. Math. Phys. 287 (2009), 323-349.

**Main Result:**
> There are NO non-trivial C^1-smooth exact solutions to the 3D steady axisymmetric Euler equations with:
> 1. Finite energy (integral of |u|^2 finite)
> 2. Uniform constant state at far fields

**Significance:** Liouville-type result for EULER (not NS).

**Implication:** Hill's vortex is NOT in this class (it has uniform far-field, but is a special explicit solution). The theorem rules out more general smooth solutions.

**Reference:** [Springer](https://link.springer.com/article/10.1007/s00220-008-0687-y)

### 4.2 2D Euler: Hamel-Nadirashvili-Shvydkoy (2017)

**Paper:** "A Liouville theorem for the Euler equations in the plane"

**Result:** Bounded steady flows with no stagnation points in R^2 must be SHEAR FLOWS (parallel to a constant vector).

**Proof technique:**
1. Analyze level curves of stream function
2. Derive at most logarithmic growth of flow argument
3. Conclude streamlines are parallel

**Reference:** [arXiv:1703.07293](https://arxiv.org/abs/1703.07293)

### 4.3 Axisymmetric Euler Liouville (Constantin-Drivas-Ginsberg)

**Paper:** "Flexibility and Rigidity in Steady Fluid Motion," Comm. Math. Phys. 2021

**Results:** Liouville-type theorems for steady Euler/Boussinesq/MHD in specific geometries (channels, cylinders).

Axisymmetric solutions in hollowed cylinders must have specific structural symmetries.

**Reference:** [Springer](https://link.springer.com/article/10.1007/s00220-021-04048-4)

---

## 5. Connection to Blowup Theory

### 5.1 Seregin's Type II Framework (2024-2025)

**Key insight:** Type II blowups, if they exist, produce ancient EULER solutions via rescaling.

**The Euler Scaling:**
```
v(x,t) -> lambda^alpha v(lambda x, lambda^{alpha+1} t)
```
with alpha = 2 - m.

**Proposition (Seregin, arXiv:2402.13229):**
Under appropriate integrability conditions, the rescaling limit (U, P) satisfies:
- Euler equations in Q_- = R^3 x (-infty, 0)
- Bounded scaled quantities
- Axisymmetric with NO SWIRL (swirl vanishes in limit!)

### 5.2 The Liouville Implication

**Seregin's Proposition 4.1:** For m in (1/2, 3/5), ancient Euler solutions U satisfying:
```
sup_{b > 0} { (1/b^{gamma m_1}) integral_{B(b)} |U|^2 dy } < infty
```
must be TRIVIAL: U = 0.

**Consequence:** If the growth bound is satisfied, Type II blowup in the range m in (1/2, 3/5) is IMPOSSIBLE.

### 5.3 The Gap Question

**Current state:**
- BKM criterion: beta >= 1/2 for any blowup
- Energy scaling: beta <= 3/5 for Type II
- Gap (1/2, 3/5) corresponds to m in (1/2, 3/5) in Seregin's notation

**The key question from your research task:**

> For ancient axisymmetric Euler U:
> If integral_{B(b)} |U|^2 = O(b^gamma) with gamma < 1/3, must U = 0?
> Can axisymmetry push the threshold from gamma < 1/5 to gamma < 1/3?

**Analysis:**

1. **Without axisymmetry (general 3D):** Liouville for bounded ancient NS is OPEN.

2. **With axisymmetry, no swirl:** KNSS (2009) proves bounded -> constant for NS. For Euler, Jiu-Xin (2009) proves finite energy steady -> trivial.

3. **Growth conditions:** Pan-Li show gamma < 1 suffices for NS. The specific threshold gamma < 1/3 vs gamma < 1/5 relates to:
   - 1/5 = (3 - 2)/5 from scaling in general 3D
   - 1/3 = potential axisymmetric improvement via reduced dimensionality

4. **Why axisymmetry might help:**
   - Vorticity structure is simpler (omega_theta/r plays role of 2D vorticity)
   - No swirl limit eliminates azimuthal complexity
   - Better a priori estimates available

5. **Closing the gap requires proving:**
   - Either: The growth bound gamma < 1/3 forces U = 0
   - Or: Verify that Type II solutions automatically satisfy the growth bound

---

## 6. With Swirl vs Without Swirl

### 6.1 No Swirl Case (More Tractable)

**Equations reduce to:**
```
D_t (omega_theta/r) = 0  (Euler)
D_t (omega_theta/r) = nu [Delta - 1/r^2] (omega_theta/r)  (NS)
```

**Key properties:**
- omega_theta/r is conserved along particle paths (Euler)
- Dissipation acts on omega_theta/r like 2D vorticity
- Global wellposedness: KNOWN for Euler, open for NS but better control

**Liouville results:** COMPLETE for bounded ancient solutions.

### 6.2 With Swirl Case (Full 3D Complexity)

**Additional equation for swirl:**
```
D_t (Gamma/r^2) = 0  (Euler)  where Gamma = r u^theta
```

**Key properties:**
- Gamma^2/r^4 acts as effective pressure creating radial flow
- Vortex stretching from swirl can amplify omega_theta
- Full 3D dynamics, though in axisymmetric geometry

**Liouville results:** CONJECTURED by KNSS, partial results by Lei-Zhang.

### 6.3 Comparison

| Property | No Swirl | With Swirl |
|----------|----------|------------|
| Effective dimension | 2D | 3D in 2D geometry |
| Vortex stretching | Absent | Present |
| Euler wellposedness | Global | Open |
| NS Liouville (bounded) | Complete | Conjectured |
| Tractability | High | Low |

**Recommendation:** Focus on the no-swirl case for closing the gap, as:
1. Seregin's limiting procedure eliminates swirl
2. Stronger results available
3. Still captures essential Type II structure

---

## 7. Summary: The Key Question Revisited

### 7.1 What We Know

1. **Bounded ancient NS (axisymmetric, no swirl):** Must be constant (KNSS 2009)

2. **Sublinear growth ancient NS (axisymmetric):** Must be constant (Pan-Li 2019)

3. **Finite energy steady Euler (axisymmetric):** Must be trivial (Jiu-Xin 2009)

4. **Type II blowup limits:** Produce ancient Euler solutions with specific growth (Seregin)

5. **Seregin's Liouville (m in (1/2, 3/5)):** Under growth bound, ancient Euler trivial

### 7.2 What Remains Open

1. **Verify automatic growth bounds:** Do Type II solutions automatically satisfy condition (1.4)?

2. **Extend Liouville to Euler:** Can NS results (Pan-Li) be adapted to Euler?

3. **Improve growth threshold:** Can axisymmetry push gamma from 1/5 to 1/3?

### 7.3 Path to Closing the Gap

**Option A:** Prove boundedness condition (1.4) is automatic for suitable weak solutions with Type II rate in (1/2, 3/5).

**Option B:** Strengthen Liouville to handle weaker growth conditions.

**Option C:** Find direct obstruction to Type II structure via axisymmetric geometry.

**Current assessment:** The gap (1/2, 3/5) remains OPEN because:
- Seregin's Liouville applies but requires verification of (1.4)
- Direct Euler Liouville with right growth conditions is not yet proven
- The connection between NS regularity and Euler ancient solutions is conditional

---

## 8. Key References

### Primary Sources

1. Koch, Nadirashvili, Seregin, Sverak. "Liouville theorems for the Navier-Stokes equations and applications." Acta Math. 203 (2009), 83-105.
   - [arXiv:0709.3599](https://arxiv.org/abs/0709.3599)
   - [Springer](https://link.springer.com/article/10.1007/s11511-009-0039-6)

2. Jiu, Q. and Xin, Z. "Smooth Approximations and Exact Solutions of the 3D Steady Axisymmetric Euler Equations." Comm. Math. Phys. 287 (2009), 323-349.
   - [Springer](https://link.springer.com/article/10.1007/s00220-008-0687-y)

3. Pan, X. and Li, Z. "Liouville theorem of axially symmetric Navier-Stokes equations with growing velocity at infinity." Nonlinear Analysis: RWA (2020).
   - [arXiv:1908.11591](https://arxiv.org/abs/1908.11591)

4. Lei, Z. and Zhang, Q.S. "A Liouville theorem for the axially-symmetric Navier-Stokes equations." J. Func. Anal. 261 (2011), 2323-2345.
   - [arXiv:1011.5066](https://arxiv.org/abs/1011.5066)

5. Seregin, G. "A note on potential Type II blowups of axisymmetric solutions to the Navier-Stokes equations."
   - [arXiv:2402.13229](https://arxiv.org/html/2402.13229)

### Related Work

6. Hamel, Nadirashvili, Shvydkoy. "A Liouville theorem for the Euler equations in the plane." (2017)
   - [arXiv:1703.07293](https://arxiv.org/abs/1703.07293)

7. Constantin, Drivas, Ginsberg. "Flexibility and Rigidity in Steady Fluid Motion." Comm. Math. Phys. (2021)
   - [Springer](https://link.springer.com/article/10.1007/s00220-021-04048-4)

8. Pan, X. and Zhang, Q.S. "A Review of results on axially symmetric Navier-Stokes equations." (2021)
   - [arXiv:2101.04905](https://arxiv.org/abs/2101.04905)

### Hill Vortex

9. Cao, Wan, Wang, Zhan. "Stability of Hill's spherical vortex." CPAM (2023)
   - [arXiv:2011.06808](https://arxiv.org/abs/2011.06808)

10. Wikipedia: [Hill's spherical vortex](https://en.wikipedia.org/wiki/Hill's_spherical_vortex)

---

## 9. Conclusions

### 9.1 Answer to Research Questions

**Q1: Classification of ancient axisymmetric Euler?**
- No swirl: Bounded -> shear flows (2D result extends)
- Finite energy steady: Only trivial solutions (Jiu-Xin)
- Hill vortex is special explicit solution, not in general class

**Q2: With vs without swirl tractability?**
- No swirl is MORE tractable (2D reduction, complete Liouville)
- With swirl retains 3D complexity, partial results only

**Q3: Known ancient solutions?**
- Hill vortex (steady, no swirl) - main non-trivial example
- Burgers vortex is NS, not Euler
- General ancient axisymmetric Euler: poorly understood

**Q4: KNSS extension to Euler?**
- Partial: Jiu-Xin for steady finite energy
- No complete extension for time-dependent ancient Euler
- This is a GAP in the literature

**Q5: Energy growth condition O(b^gamma)?**
- For NS: gamma < 1 suffices (Pan-Li)
- For Euler: unknown if gamma < 1/3 forces triviality
- Axisymmetry likely improves threshold but not yet proven

### 9.2 Impact on Type II Gap

The gap (1/2, 3/5) for Type II blowup rates relates to:
1. Seregin's m in (1/2, 3/5) range
2. Liouville for ancient Euler under growth bounds
3. Whether bounds are automatic for Type II solutions

**Status:** CONDITIONALLY closed by Seregin's framework. Unconditional closure requires:
- Proving growth bounds automatic, OR
- Stronger Liouville theorems for Euler with weaker hypotheses

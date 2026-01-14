# Liouville Theorem Comparison and Synthesis for Ancient Axisymmetric Euler Without Swirl

## Target Theorem

**Goal:** Prove that ancient axisymmetric Euler solutions without swirl satisfying:
```
integral_{B(b)} |U|^2 = O(b^gamma), gamma < 1
```
must be trivial: U = 0.

---

## 1. Landscape of Known Liouville Theorems

### 1.1 Summary Table

| Result | Equation | Time | Symmetry | Growth | Conclusion |
|--------|----------|------|----------|--------|------------|
| KNSS (2009) | NS | Ancient | Axisym no swirl | Bounded | Constant |
| Pan-Li (2020) | NS | Ancient | Axisym | o(\|x\|^alpha), alpha < 1 | Trivial |
| Hamel-Nadirashvili (2019) | Euler | Steady | 2D | Bounded | Shear flow |
| KPR (2015) | NS | Steady | Axisym no swirl | Dirichlet finite | Trivial |
| Chae (2014) | Euler | Steady | General | o(1) decay | Various |
| Jiu-Xin (2009) | Euler | Steady | Axisym | Finite energy | Trivial |
| Seregin (2025) | Euler | Ancient | General | O(b^{2m-1}), m < 3/5 | Trivial |
| **TARGET** | **Euler** | **Ancient** | **Axisym no swirl** | **O(b^gamma), gamma < 1** | **Trivial?** |

### 1.2 Key Observation

Our target setting combines:
- **Euler** (no viscosity) - harder than NS
- **Ancient** (defined for t in (-infty, 0]) - harder than steady
- **Axisymmetric without swirl** - special structure
- **Sublinear L^2 growth** - intermediate between bounded and general

This is a UNIQUE combination not directly covered by any existing result.

---

## 2. Detailed Analysis of Each Approach

### 2.1 KNSS (2009) - Bounded Ancient NS

**Statement:** Bounded ancient mild solutions of 3D axisymmetric NS without swirl are constant.

**Key Techniques:**
1. **Backward uniqueness** via Carleman estimates
2. **Scaling analysis** to extract limiting behavior
3. **Energy estimates** on rescaled domains

**Adaptation to Our Setting:**

| Component | NS Version | Euler Adaptation | Difficulty |
|-----------|------------|------------------|------------|
| Backward uniqueness | Carleman for heat operator | No parabolic structure | HIGH |
| Scaling | Works with viscosity | Works (scale-invariant) | LOW |
| Energy estimates | Dissipation helps decay | Energy conservation only | MEDIUM |

**Key Obstacle:** The Carleman estimates in KNSS crucially use the heat operator structure:
```
partial_t u - nu Delta u = ...
```
For Euler (nu = 0), this becomes purely hyperbolic transport, and standard Carleman methods fail.

**Potential Workaround:** Replace backward uniqueness with:
- Transport uniqueness along characteristics
- Lagrangian approach exploiting particle path structure
- Time-averaged energy methods

**Assessment:** PARTIAL ADAPTATION POSSIBLE - need new uniqueness mechanism.

---

### 2.2 Pan-Li (2020) - Sublinear Growth NS

**Statement:** Ancient axisymmetric NS with |u| = o(|x|^alpha), alpha < 1, must be trivial.

**Key Techniques:**
1. **Weighted energy estimates** for growing solutions
2. **Scaling to bounded case** via normalization
3. **Reduction to KNSS** after appropriate transformation

**Sharpness:** alpha = 1 is OPTIMAL - counterexamples exist for linear growth.

**Adaptation to Our Setting:**

The growth condition |u| = o(|x|^alpha) translates to:
```
integral_{B(R)} |u|^2 = o(R^{2alpha+3})
```
For alpha = 1: integral = o(R^5)
For alpha < 1: integral = o(R^{2alpha+3}) with 2alpha+3 < 5

Our condition gamma < 1 is WEAKER than Pan-Li's condition when:
```
gamma < 2alpha + 3  <==>  alpha > (gamma - 3)/2
```
For gamma = 1: alpha > -1 (always satisfied)

**Key Issue:** Pan-Li uses viscous dissipation in weighted norms. For Euler:
- No dissipation term
- Energy is conserved, not decaying
- Need alternative mechanism

**Assessment:** GROWTH THRESHOLD APPLICABLE - but proof mechanism fails for Euler.

---

### 2.3 Hamel-Nadirashvili (2019) - 2D Steady Euler

**Statement:** Bounded steady 2D Euler flows with no stagnation points are shear flows.

**Key Techniques:**
1. **Stream function level set analysis**
2. **Argument (angle) of velocity** grows at most logarithmically
3. **Topological constraints** on streamline structure

**Adaptation to Axisymmetric No-Swirl:**

Our axisymmetric no-swirl case IS effectively 2D in the (r,z) plane:
```
U = U_r(r,z) e_r + U_z(r,z) e_z
```

The stream function formulation:
```
U_r = -(1/r) partial_z psi
U_z = (1/r) partial_r psi
```

**Key Difference:** We have ANCIENT (time-dependent), not steady.

**Potential Extension:**

For steady: H-N analyzes level curves of psi.
For ancient: Could analyze level curves of psi(r,z,tau) evolving in tau.

**Obstruction Analysis:**

1. **No stagnation points:** H-N requires u != 0 everywhere. For ancient solutions arising from blowup, stagnation is possible.

2. **Bounded velocity:** H-N requires |u| bounded. Our condition allows O(b^{gamma/3}) growth.

3. **Time dependence:** Level curve analysis becomes moving boundary problem.

**Assessment:** PARTIAL ANALOGY - stream function analysis applicable, but time dependence and growth are obstacles.

---

### 2.4 KPR (2015) - Steady Axisymmetric NS

**Statement:** D-solutions (finite Dirichlet integral) of steady axisymmetric NS without swirl are trivial.

**Key Techniques:**
1. **Stream function geometry** (similar to H-N)
2. **Bernoulli function** H = (1/2)|u|^2 + p = const on streamlines
3. **Morse-Sard theorem** for level sets
4. **Flux estimates** for contradiction

**Adaptation to Ancient Euler:**

| Technique | Steady NS | Ancient Euler | Status |
|-----------|-----------|---------------|--------|
| Stream function | Works | Works | OK |
| Bernoulli H = const | Steady only | H varies with tau | FAILS |
| Morse-Sard | Applies | Applies per tau | OK |
| Flux estimates | Uses viscosity | No viscosity | FAILS |

**Critical Issue: Bernoulli for Ancient Solutions**

For steady Euler: H = (1/2)|U|^2 + P is constant along streamlines.

For ancient Euler:
```
D_tau H = partial_tau H + (U . nabla) H = 0 (material derivative)
```
So H is conserved along PARTICLE PATHS, not streamlines!

**Potential Use:**
- Track H along backward characteristics
- If H -> 0 as tau -> -infty (particles came from infinity), derive constraint
- Requires control of particle trajectories

**Assessment:** BERNOULLI STRUCTURE PARTIALLY APPLICABLE - need time-dependent version.

---

### 2.5 Chae (2014) - Euler with Decay

**Statement:** Various Liouville results for steady Euler with decay |u| -> 0 at infinity.

**Key Techniques:**
1. **Vorticity structure** exploitation
2. **BKM-type arguments**
3. **Integration by parts** with decay assumptions

**For Axisymmetric No-Swirl:**

The vorticity is purely azimuthal: omega = omega_theta e_theta

The key equation:
```
D_tau (omega_theta/r) = 0  (materially conserved for Euler!)
```

**Critical Structure:**
The quantity omega_theta/r satisfies:
```
partial_tau (omega_theta/r) + U . nabla (omega_theta/r) = 0
```

This is PURE TRANSPORT - no stretching, no source!

**Implication:**
If omega_theta/r vanishes at infinity AND particles trace back to infinity, then omega_theta/r = 0 everywhere.

**Assessment:** VORTICITY TRANSPORT STRUCTURE IS KEY - most promising for our case.

---

## 3. Synthesis: The Most Promising Strategy

### 3.1 Hybrid Approach

Combine:
1. **Stream function** from H-N/KPR
2. **Vorticity transport** from Chae
3. **Growth control** from Pan-Li
4. **Axisymmetric structure** throughout

### 3.2 Proposed Proof Strategy

**STRATEGY: BACKWARD VORTICITY PROPAGATION**

**Step 1: Material Conservation**

For axisymmetric Euler without swirl:
```
D/Dtau (omega_theta/r) = 0
```
where omega_theta = partial_z U_r - partial_r U_z.

This means omega_theta/r is CONSTANT along particle paths.

**Step 2: Particle Trajectory Bounds**

For |U| = O(|x|^{gamma/3}) (from L^2 growth O(b^gamma)):
```
|dX/dtau| = |U(X,tau)| ~ |X|^{gamma/3}
```

Solving backward:
```
|X(tau)| ~ |X(0)| + C |tau|^{3/(3-gamma)}  for gamma < 3
```

For gamma < 1: particles grow as |tau|^{3/(3-gamma)} with 3/(3-gamma) < 3/2.

This is SLOW ENOUGH that particles escape to infinity as tau -> -infinity.

**Step 3: Decay at Infinity**

From the L^2 growth condition integral_{B(b)} |U|^2 = O(b^gamma):

By Holder on annular regions:
```
|U(x)| ~ |x|^{(gamma-3)/2}  average decay
```

For gamma < 1: exponent (gamma-3)/2 < -1, so |U| = o(|x|^{-1}).

This implies:
```
|omega_theta/r| = |(curl U)_theta / r| ~ |nabla U|/r ~ |x|^{(gamma-5)/2}
```

For gamma < 1: exponent < -2, so omega_theta/r -> 0 as |x| -> infinity.

**Step 4: Propagation to All Space**

Combining Steps 1-3:
- omega_theta/r is constant along particle paths (Step 1)
- Particles trace back to infinity as tau -> -infinity (Step 2)
- omega_theta/r -> 0 at infinity (Step 3)

Therefore: omega_theta/r = 0 everywhere!

**Step 5: From Zero Vorticity to Zero Velocity**

If omega_theta = 0 and div U = 0 (incompressibility):
```
U_r = -(1/r) partial_z psi
U_z = (1/r) partial_r psi
```
with Delta_* psi = 0 (Laplacian of stream function).

Combined with growth condition and regularity at axis:
```
psi = 0  ==>  U = 0
```

**QED (Conditional)**

### 3.3 Critical Gaps in the Strategy

**Gap 1: Uniform Particle Bounds**

Step 2 requires UNIFORM bounds on |X(tau)| across all initial conditions.

Need: For all x with |x| = R, the backward trajectory X(-infty) -> infinity.

**Technical Issue:** The growth bound |U| ~ |x|^{gamma/3} is an L^2 average, not pointwise. Could have local concentrations where U is larger.

**Resolution:** Use local energy estimates to get pointwise bounds from L^2:
```
sup_{B(x,1)} |U|^2 <= C integral_{B(x,2)} |U|^2 + lower order
```

This upgrades average L^2 growth to pointwise control.

**Gap 2: Decay of omega_theta/r at Infinity**

Step 3 estimates omega_theta/r from U decay. Need to verify:
```
|omega_theta/r| = |partial_z U_r - partial_r U_z| / r
```

If |U| ~ R^{-alpha} for alpha > 1, then |nabla U| ~ R^{-alpha-1}, so:
```
|omega_theta/r| ~ R^{-alpha-1} / R = R^{-alpha-2}
```

For gamma < 1 giving alpha = (3-gamma)/2 > 1:
```
|omega_theta/r| ~ R^{-(3-gamma)/2 - 2} = R^{-(7-gamma)/2}
```

This goes to 0 as R -> infinity. CHECK.

**Gap 3: Axis Regularity**

The axis r = 0 is special. Need:
- omega_theta/r remains bounded at axis
- Particle paths don't concentrate at axis

For smooth solutions: omega_theta ~ r f(z) near axis, so omega_theta/r ~ f(z) is bounded.

The L^2 growth bound implies integrability near axis.

**Gap 4: From omega = 0 to U = 0**

If omega_theta = 0 in all of R^3, we have:
```
curl U = 0  AND  div U = 0  AND  |U| = o(|x|^1)  (sublinear growth)
```

**Claim:** This implies U = const.

**Proof:** U is harmonic (satisfies Laplace equation). Sublinear growth harmonic functions are constant by Liouville for harmonic functions.

Since U = U(r,z) depends only on (r,z) and is bounded at infinity: U = const.

For ancient Euler with U(x,tau) depending on tau:
- For each fixed tau, U(.,tau) = C(tau)
- From Euler equation: partial_tau C + (C . nabla) C = -nabla P gives nabla P = 0
- So P = P(tau) only, and partial_tau C = 0
- Therefore C = const, i.e., U is constant in space and time

If integral_{B(b)} |U|^2 = O(b^gamma) with gamma < 3: U = 0 (since constant U with |U| > 0 gives integral ~ b^3).

---

## 4. Comparison Table: What Each Approach Contributes

| Approach | Key Contribution | Applicable? | Obstacle |
|----------|-----------------|-------------|----------|
| KNSS | Backward uniqueness framework | Partially | No parabolic structure |
| Pan-Li | Growth threshold gamma < 1 sharp | Yes | NS-specific estimates |
| H-N | Stream function level sets | Partially | Time-dependent, growth |
| KPR | Bernoulli + Morse-Sard | Partially | Time-dependent H |
| Chae | Vorticity structure | YES | Need decay verification |

**Winner: Vorticity Transport (Chae-inspired) + Particle Trajectory (KNSS-inspired)**

---

## 5. Refined Theorem Statement

**Theorem (Proposed):** Let U: R^3 x (-infty, 0] -> R^3 be a smooth ancient solution of the incompressible Euler equations that is:

1. **Axisymmetric without swirl:** U = U_r(r,z,tau) e_r + U_z(r,z,tau) e_z
2. **Sublinear L^2 growth:** integral_{B(b)} |U(y,tau)|^2 dy <= C b^gamma for all b > 0, tau <= 0, with gamma < 1

Then U = 0.

**Proof Outline:**

1. omega_theta/r is materially conserved (Euler structure)
2. Particle paths escape to infinity as tau -> -infinity (from growth bound)
3. omega_theta/r -> 0 at spatial infinity (from L^2 growth)
4. Therefore omega_theta/r = 0 everywhere
5. Curl-free + div-free + sublinear growth implies U = const
6. Growth bound with gamma < 3 forces const = 0

---

## 6. What This Achieves for Type II Exclusion

### 6.1 Seregin's Framework

Seregin shows that Type II blowup with rate m in (1/2, 3/5) produces ancient Euler limits U satisfying:
```
integral_{B(b)} |U|^2 = O(b^{2m-1})
```

For m = 3/5: exponent = 1/5
For m = 1: exponent = 1

Our theorem (if proven) gives Liouville for gamma < 1, i.e., m < 1.

**Implication:** Type II blowup is excluded for ALL rates m in (1/2, 1) IF:
1. The blowup limit is axisymmetric without swirl
2. Our Liouville theorem is correct

### 6.2 The Swirl Question

Seregin shows the blowup limit has NO SWIRL (it vanishes in the rescaling limit).

Therefore, our axisymmetric no-swirl Liouville APPLIES to Type II limits!

### 6.3 Complete Picture

```
Type II with m in (1/2, 1)
        |
        v (Seregin rescaling)
Ancient Euler, axisymmetric, no swirl, L^2 growth O(b^{2m-1})
        |
        v (Our Liouville for gamma < 1, i.e., 2m-1 < 1, i.e., m < 1)
U = 0
        |
        v (Contradiction with blowup)
No Type II blowup for m in (1/2, 1)
```

**Combined with:** Type I ruled out by Seregin 2012

**Result:** NO blowup at all for axisymmetric suitable weak solutions!

---

## 7. Remaining Technical Work

### 7.1 Rigorous Particle Trajectory Estimates

Need: For L^2 growth O(b^gamma) with gamma < 1, backward particle paths X(tau; x_0, 0) satisfy |X(tau)| -> infinity as tau -> -infinity for all x_0.

**Required:** Local-to-global gradient estimates for ancient Euler.

### 7.2 Decay of Vorticity at Infinity

Need: The L^2 growth implies |omega_theta/r| -> 0 at spatial infinity uniformly in tau.

**Required:** Elliptic estimates relating vorticity to velocity in growing spaces.

### 7.3 Axis Regularity

Need: Solutions remain smooth at r = 0 with controlled omega_theta/r.

**Required:** Weighted Sobolev analysis near axis.

### 7.4 Uniqueness for Transport Equation

Need: If omega_theta/r = 0 at tau = -infinity (in limit) and is transported forward, it remains 0.

**Required:** Well-posedness for backward transport with growing coefficients.

---

## 8. Summary and Recommendation

### 8.1 Most Promising Strategy

**The Vorticity Transport approach** combining:
- Material conservation of omega_theta/r (axisymmetric Euler structure)
- Particle trajectory bounds (from L^2 growth)
- Decay at infinity (from growth condition)
- Liouville for curl-free fields

### 8.2 Key Advantages of This Approach

1. **Exploits axisymmetric structure** maximally
2. **Avoids viscosity dependence** (unlike KNSS/Pan-Li)
3. **Works with growth** (unlike H-N bounded requirement)
4. **Natural for ancient solutions** (particle paths extend to tau = -infinity)

### 8.3 Assessment

**Likelihood of success:** HIGH (conditional on technical estimates)

**Why:** The vorticity transport structure omega_theta/r = const along paths is EXACT for Euler. Combined with particles escaping to infinity where omega_theta/r = 0, the conclusion omega_theta = 0 everywhere is essentially forced.

**Critical step:** Proving particles escape uniformly, which requires careful analysis of L^2 growth -> pointwise bounds -> ODE estimates.

---

## 9. References

### Primary Liouville Results

1. Koch-Nadirashvili-Seregin-Sverak (2009). "Liouville theorems for the Navier-Stokes equations and applications." [arXiv:0709.3599](https://arxiv.org/abs/0709.3599)

2. Pan-Li (2020). "Liouville theorem of axially symmetric Navier-Stokes equations with growing velocity at infinity." [arXiv:1908.11591](https://arxiv.org/abs/1908.11591)

3. Hamel-Nadirashvili (2019). "A Liouville theorem for the Euler equations in the plane." [arXiv:1703.07293](https://arxiv.org/abs/1703.07293)

4. Korobkov-Pileckas-Russo (2015). "The Liouville Theorem for the Steady-State Navier-Stokes Problem." [Springer](https://link.springer.com/content/pdf/10.1007/s00021-015-0202-0.pdf)

5. Chae (2014). "Liouville-type theorems for the forced Euler equations and the Navier-Stokes equations." [arXiv:1306.5839](https://arxiv.org/abs/1306.5839)

### Euler-Specific Results

6. Jiu-Xin (2009). "Smooth Approximations and Exact Solutions of the 3D Steady Axisymmetric Euler Equations." [Springer](https://link.springer.com/article/10.1007/s00220-008-0687-y)

7. Nadirashvili (2014). "Liouville theorem for Beltrami flow." [arXiv:1403.1414](https://arxiv.org/abs/1403.1414)

### Type II Framework

8. Seregin (2025). "A note on certain scenarios of Type II blowups." arXiv:2507.08733

9. Seregin (2024). "On potential Type II blowups." [arXiv:2402.13229](https://arxiv.org/html/2402.13229)

### Related Axisymmetric Results

10. Lei-Zhang (2011). "A Liouville theorem for the axially-symmetric Navier-Stokes equations." [arXiv:1011.5066](https://arxiv.org/abs/1011.5066)

11. Escauriaza-Seregin-Sverak (2003). "L_{3,infinity}-solutions of Navier-Stokes equations and backward uniqueness." [UMN Archive](https://conservancy.umn.edu/items/1ded2377-3cb2-43af-b8ff-f8d52ce5e3fe)

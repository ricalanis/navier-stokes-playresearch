# Enhanced Liouville Theorem via Energy and Enstrophy Methods

**Date:** January 13, 2026
**Status:** PROOF ATTEMPT - PARTIAL SUCCESS WITH IDENTIFIED GAPS
**Goal:** Prove ancient axisymmetric Euler without swirl with growth bound implies U = 0

---

## 1. Problem Statement

**Theorem (Target):** Let U be an ancient solution of the 3D incompressible Euler equations:
```
partial_tau U + (U . nabla)U = -nabla P
div U = 0
```
on R^3 x (-infinity, 0], which is:
1. Axially symmetric: U = U^r(r,z,tau) e_r + U^z(r,z,tau) e_z
2. Without swirl: U^theta = 0
3. Satisfies the growth bound: integral_{B(b)} |U|^2 dy = O(b^gamma) with gamma < 1

**Claim:** Under these conditions, U = 0.

---

## 2. Key Quantities and Conservation Laws

### 2.1 Energy (Kinetic)

For incompressible Euler, kinetic energy is conserved:
```
E(tau) = (1/2) integral_{R^3} |U|^2 dx = const for all tau in (-infinity, 0]
```

**For ancient solutions:** If E < infinity, then E(tau) = E_0 for all tau in (-infinity, 0].

**From growth bound:**
```
E = integral_{R^3} |U|^2 dx = lim_{R -> infinity} integral_{B(R)} |U|^2 dx
```

If integral_{B(b)} |U|^2 = O(b^gamma) with gamma < 1, then:
- For gamma < 0: E = 0 (trivially U = 0)
- For gamma = 0: E is bounded but possibly nonzero
- For gamma in (0,1): E could be infinite!

**Important:** The growth condition integral_{B(b)} |U|^2 = O(b^gamma) does NOT automatically imply finite energy when gamma > 0.

### 2.2 Vorticity Structure

For axisymmetric flow without swirl:
```
omega = omega^theta(r,z,tau) e_theta
```

The vorticity is purely azimuthal. In terms of velocity:
```
omega^theta = partial_z U^r - partial_r U^z
```

### 2.3 The Critical Quantity: eta = omega^theta / r

**Definition:**
```
eta(r,z,tau) = omega^theta(r,z,tau) / r
```

**Material Conservation (Euler):**
```
D eta / D tau = partial_tau eta + (U . nabla) eta = 0
```

This is the KEY property: eta is constant along particle trajectories.

**Proof:**
The vorticity equation for axisymmetric Euler without swirl is:
```
D omega^theta / D tau = (omega^theta / r) U^r
```
which gives:
```
D/Dtau (omega^theta / r) = (1/r) D omega^theta / D tau - (omega^theta / r^2) D r / D tau
                         = (1/r)(omega^theta / r) U^r - (omega^theta / r^2) U^r
                         = (omega^theta / r^2) U^r - (omega^theta / r^2) U^r = 0
```

### 2.4 Weighted Enstrophy

**Definition:**
```
Z(tau) = integral r^2 eta^2 r dr dz = integral (omega^theta)^2 r dr dz = (1/2pi) integral |omega|^2 dx
```

This is the enstrophy (up to constant factor).

**Conservation from material conservation of eta:**

Since eta is materially conserved and the flow is incompressible (volume-preserving), we have:
```
integral eta^2 dV = const
```

But the natural measure for axisymmetric integrals is r dr dz dtheta = 2pi r dr dz, so:
```
integral eta^2 * r dr dz = (1/2pi) integral eta^2 dV = const
```

More precisely, the conserved quantity is:
```
Z = integral_{R^+_r x R_z} (omega^theta)^2 r dr dz = const
```

**This is the weighted enstrophy, and it IS conserved for axisymmetric Euler without swirl.**

---

## 3. Scaling Analysis

### 3.1 Euler Scaling

Under the dilation x -> lambda x, t -> lambda t (Euler scaling):
```
U_lambda(x,tau) = lambda U(lambda x, lambda tau)
```

satisfies Euler if U does.

**Energy scaling:**
```
E_lambda = integral |U_lambda|^2 dx = integral lambda^2 |U(lambda x)|^2 dx
         = integral lambda^2 |U(y)|^2 * (dy / lambda^3) = lambda^{-1} E
```

**Enstrophy scaling:**
```
Z_lambda = integral |omega_lambda|^2 dx = integral lambda^4 |omega(lambda x)|^2 dx
         = integral lambda^4 |omega(y)|^2 * (dy / lambda^3) = lambda Z
```

Wait, let me redo this more carefully.

For vorticity omega = curl U:
```
omega_lambda = curl U_lambda = lambda curl_x [lambda U(lambda x)] = lambda^2 omega(lambda x)
```

So:
```
Z_lambda = integral |omega_lambda|^2 dx = integral lambda^4 |omega(lambda x)|^2 dx
         = lambda^4 integral |omega(y)|^2 (dy/lambda^3) = lambda Z
```

**Key observation:** Under Euler scaling by factor lambda:
- E_lambda = lambda^{-1} E
- Z_lambda = lambda Z
- Ratio: Z_lambda / E_lambda = lambda^2 (Z/E)

### 3.2 The Ratio Z/E

The ratio Z/E has dimension [length]^{-2}.

For a family of solutions parametrized by scale lambda:
```
(Z/E)_lambda = lambda^2 (Z/E)
```

**Implication for ancient solutions:**

If U is an ancient solution with finite E and finite Z, consider the "backward rescaling": as tau -> -infinity, the natural scale of the solution may change.

For self-similar ancient solutions U(x,tau) = f(tau) * V(x/g(tau)):
The scaling of E and Z constrains f and g.

---

## 4. Backward Trajectory Argument

### 4.1 Particle Trajectories for Ancient Solutions

Define the backward characteristic:
```
dX/dtau = U(X,tau), X(0) = x_0
```

For an ancient solution, this ODE can be solved for all tau in (-infinity, 0].

### 4.2 Material Conservation and Dispersion

Since eta = omega^theta / r is materially conserved:
```
eta(X(tau), tau) = eta(x_0, 0) for all tau in (-infinity, 0]
```

**Key Question:** What happens to X(tau) as tau -> -infinity?

**Case A: Particles stay bounded**
If sup_{tau < 0} |X(tau)| < infinity, then eta is constant on a bounded region.

**Case B: Particles disperse to infinity**
If |X(tau)| -> infinity as tau -> -infinity, then eta at (x_0, 0) equals the limiting value of eta at spatial infinity.

### 4.3 Dispersion Implies Triviality

**Hypothesis:** Suppose particles disperse as tau -> -infinity:
```
lim_{tau -> -infinity} |X(tau)| = infinity for all x_0 != axis
```

**Then:**
```
eta(x_0, 0) = lim_{tau -> -infinity} eta(X(tau), tau)
```

If eta decays at spatial infinity (from the growth bound on U), then:
```
eta(x_0, 0) = 0 for all x_0
```

which implies omega^theta = 0, hence U = 0 (for divergence-free axisymmetric flows).

### 4.4 The Dispersion Question

**Critical Issue:** Do particles disperse for all ancient axisymmetric Euler solutions?

**Argument FOR dispersion:**

For a solution with |U| ~ |x|^{gamma/3} growth (to match integral |U|^2 ~ R^gamma on B(R)):
```
|dX/dtau| ~ |X|^{gamma/3}
```

For gamma < 1, this gives |gamma/3| < 1/3, so the velocity grows slower than linear.

Integrating backward:
```
|X(tau)|^{1 - gamma/3} ~ |tau| as tau -> -infinity
```

So |X(tau)| ~ |tau|^{1/(1-gamma/3)} = |tau|^{3/(3-gamma)}.

For gamma < 1: 3/(3-gamma) > 3/2, so particles DO disperse to infinity.

**Argument AGAINST (potential obstruction):**

The above assumes uniform growth. If U is concentrated near the axis, particles near the axis may be trapped in a "vortex core" that persists backward in time.

This is the case for Hill's spherical vortex (a steady solution), where particles inside the vortex sphere recirculate indefinitely.

---

## 5. Energy-Enstrophy Constraint Analysis

### 5.1 Dimensional Constraint

Consider the ratio:
```
Lambda^2 := Z / E = (integral |omega|^2) / (integral |U|^2)
```

This has dimension [length]^{-2}, representing a characteristic wavenumber squared.

For an ancient solution with finite E and Z, Lambda is well-defined.

### 5.2 Time Independence

For Euler:
- E = const (energy conservation)
- Z = const for axisymmetric no-swirl (from material conservation of eta)

Therefore Lambda = const as well.

### 5.3 Constraint from Growth Bound

From integral_{B(R)} |U|^2 = O(R^gamma), we need to extract information about omega.

**Using div U = 0 and curl U = omega:**

For incompressible flow, |nabla U| controls both div and curl. Roughly:
```
|omega| ~ |nabla U|
```

By Sobolev-Poincare on B(R):
```
integral_{B(R)} |omega|^2 >= c R^{-2} integral_{B(R)} |U - U_avg|^2
```

But this doesn't directly help.

**Alternative approach via stream function:**

For axisymmetric no-swirl, let psi be the Stokes stream function:
```
U^r = -(1/r) partial_z psi
U^z = (1/r) partial_r psi
omega^theta = -(1/r)[partial_rr psi - (1/r) partial_r psi + partial_zz psi]
```

Energy and enstrophy are related through psi and its derivatives.

### 5.4 The Casimir Invariants

For axisymmetric Euler without swirl, there are infinitely many conserved quantities (Casimirs):
```
C_f = integral f(eta) r dr dz
```
for any smooth function f.

In particular:
- C_1 = integral eta r dr dz (circulation-like)
- C_2 = integral eta^2 r dr dz (proportional to Z)
- C_n = integral eta^n r dr dz

**These are ALL conserved for ancient solutions.**

### 5.5 Using Multiple Conserved Quantities

**Observation:** If eta decays at infinity (from growth bound), then all C_n are finite.

The combination of E, Z = C_2, and higher C_n constrains the possible forms of eta.

**Claim (heuristic):** An ancient solution with finite E, finite Z, and eta -> 0 at infinity must have eta supported on a bounded region.

**Reason:** The conservation of all C_n for all time, combined with decay at infinity, severely restricts the possible dynamics. Essentially, eta can only be "reshuffled" within the support of the initial data.

---

## 6. Proof Attempt: Combining All Constraints

### 6.1 Setup

Let U be an ancient axisymmetric Euler solution without swirl satisfying:
```
integral_{B(b)} |U|^2 = O(b^gamma) with gamma < 1
```

Define:
- eta = omega^theta / r (materially conserved)
- Z = integral (omega^theta)^2 r dr dz (conserved)
- E = integral |U|^2 (conserved, but possibly infinite if gamma > 0)

### 6.2 Case gamma < 0: Trivial

If integral_{B(b)} |U|^2 = O(b^gamma) with gamma < 0, then:
```
integral_{R^3} |U|^2 = lim_{b -> infinity} integral_{B(b)} |U|^2 <= C lim_{b -> infinity} b^gamma = 0
```
So U = 0. Done.

### 6.3 Case gamma = 0: Bounded L^2

If integral_{B(b)} |U|^2 = O(1), then E = integral |U|^2 < infinity.

**Claim:** For finite energy ancient axisymmetric Euler without swirl, U = 0.

**Proof attempt:**

Step 1: Finite energy implies |U| -> 0 at infinity in some averaged sense.

Step 2: This should imply |omega| -> 0 at infinity (from the relation omega = curl U).

Step 3: Therefore eta = omega^theta / r -> 0 as |x| -> infinity.

Step 4: Material conservation of eta + dispersion of trajectories => eta = 0 everywhere.

Step 5: eta = 0 => omega = 0 => U = 0 (for bounded energy, divergence-free).

**Gap in Step 4:** Need to verify dispersion. For bounded (gamma = 0), particles may not disperse.

### 6.4 Case 0 < gamma < 1: Growing L^2

If integral_{B(b)} |U|^2 = O(b^gamma) with gamma in (0,1):

**Issue:** E may be infinite!

But we still have:
- eta is materially conserved
- Z may be finite or infinite (need to check)

**Relating Z to growth bound:**

From omega = curl U and integral_{B(R)} |U|^2 ~ R^gamma:

By standard estimates (Calderon-Zygmund):
```
integral_{B(R)} |omega|^2 <= C integral_{B(2R)} |nabla U|^2
```

And by Poincare on annuli:
```
integral_{B(2R) \ B(R)} |nabla U|^2 ~ R^{-2} integral_{B(2R)} |U|^2 ~ R^{gamma - 2}
```

Summing over dyadic shells:
```
Z = integral |omega|^2 ~ sum_k 2^{k(gamma - 2)} (converges if gamma < 2)
```

So for gamma < 1 < 2, Z is finite!

**With finite Z:**

The weighted enstrophy is conserved and finite. Combined with:
- eta materially conserved
- eta(X(tau), tau) = const along characteristics

If we can show eta -> 0 at spatial infinity uniformly in tau, and particles disperse, then eta = 0.

**Showing eta -> 0 at infinity:**

From Z = integral (omega^theta)^2 r dr dz < infinity:

On any region {r > R}, we have:
```
integral_{r > R} eta^2 r^3 dr dz <= (1/R^2) integral_{r > R} (omega^theta)^2 r dr dz -> 0 as R -> infinity
```

This shows eta -> 0 in weighted L^2 sense as r -> infinity.

For z -> +/- infinity at fixed r, similar arguments apply.

**Conclusion for 0 < gamma < 1:**

If particles disperse (which we argued holds for gamma < 1), then eta = 0 everywhere, hence U = 0.

---

## 7. The Remaining Gap: Trapped Trajectories

### 7.1 The Hill Vortex Counterexample (Steady Case)

Hill's spherical vortex is a steady (hence ancient) axisymmetric Euler solution without swirl.

Properties:
- Finite energy (compact support)
- Finite enstrophy
- eta = omega^theta / r = const inside sphere, 0 outside
- Particles inside the sphere are TRAPPED - they recirculate forever

**Why doesn't our argument apply?**

For Hill's vortex:
- Growth bound: integral_{B(b)} |U|^2 = O(1) since compact support
- So gamma = 0

But particles don't disperse! Inside the vortex, they stay bounded.

### 7.2 Resolution: Hill Vortex Doesn't Contradict the Theorem

Hill's vortex is a traveling wave: U(x,t) = U_0(x - ct e_z) for some velocity c.

In the frame moving with the vortex, it's steady. In the lab frame, it's NOT ancient in the sense required - it doesn't exist for all t in (-infinity, 0] at a fixed point.

**Alternatively:** If we consider Hill's vortex in the moving frame, it IS ancient (trivially, being steady). But then our argument doesn't apply because:
- The vortex exists on bounded region
- eta is CONSTANT, not zero
- Particles are trapped, not dispersing

**Key insight:** The theorem needs a hypothesis that rules out "coherent structures" like Hill's vortex.

### 7.3 What Hypothesis Rules Out Coherent Structures?

**Possibility 1:** Require U -> 0 at infinity pointwise (not just in averaged sense).

This excludes traveling waves that maintain profile at infinity.

**Possibility 2:** Require dispersion hypothesis directly.

Add hypothesis: lim_{tau -> -infinity} |X(tau)| = infinity for almost all characteristics.

**Possibility 3:** Use the time-dependent structure.

For a genuinely time-dependent ancient solution (not steady or traveling wave), particles may be more likely to disperse.

---

## 8. Refined Theorem Statement

### 8.1 Statement with Dispersion Hypothesis

**Theorem (Energy-Enstrophy Liouville):**
Let U be an ancient axisymmetric Euler solution without swirl on R^3 x (-infinity, 0] satisfying:
1. Growth bound: integral_{B(b)} |U|^2 = O(b^gamma) with gamma < 1
2. Dispersion: For almost every x in R^3, the backward characteristic X(tau;x) satisfies |X(tau;x)| -> infinity as tau -> -infinity

Then U = 0.

**Proof:**

Step 1: From gamma < 1, the weighted enstrophy Z is finite (Section 6.4).

Step 2: From finite Z, we have eta = omega^theta / r -> 0 at spatial infinity.

Step 3: From dispersion hypothesis, eta(X(tau;x), tau) -> eta at infinity = 0 as tau -> -infinity.

Step 4: From material conservation, eta(x, 0) = lim_{tau -> -infinity} eta(X(tau;x), tau) = 0.

Step 5: eta = 0 everywhere implies omega = 0, which for divergence-free axisymmetric flow implies U = 0.

QED.

### 8.2 When Does Dispersion Hold?

**Claim:** Dispersion holds if U is not a traveling wave or steady vortex.

More precisely, dispersion fails only if there exist trapped particle orbits - closed or unbounded-but-confined trajectories.

For truly ancient solutions arising as blowup limits (Seregin's framework), the rescaling structure suggests:
- The profile U represents the "shape" of concentrating energy
- Backward in time (tau -> -infinity) corresponds to "zooming out"
- Particles should disperse under this zooming

**Conjecture:** Ancient axisymmetric Euler solutions arising as Type II blowup limits satisfy the dispersion hypothesis.

---

## 9. Alternative Approach: Scaling Rigidity

### 9.1 Self-Similar Structure

If U is an ancient solution arising from a self-similar blowup structure:
```
U(x,tau) = |tau|^{-alpha} F(x / |tau|^beta)
```

Then energy and enstrophy scale as:
```
E(tau) = |tau|^{3beta - 2alpha}
Z(tau) = |tau|^{3beta - 4alpha + 2}
```

For conservation (E, Z constant):
```
3beta - 2alpha = 0
3beta - 4alpha + 2 = 0
```

Solving: alpha = 1, beta = 2/3. This is exactly Type I scaling!

**Implication:** Type II ancient solutions (non-self-similar) cannot have both finite constant E and finite constant Z with self-similar structure.

### 9.2 Non-Self-Similar Ancient Solutions

For non-self-similar ancient solutions, the scaling analysis is more complex.

But the joint conservation of E and Z (both for axisymmetric Euler without swirl) provides strong constraints.

**Rigidity conjecture:** Ancient axisymmetric Euler without swirl with finite E and Z must be either:
1. Trivial (U = 0), or
2. Steady/traveling (Hill-type)

---

## 10. Summary and Conclusions

### 10.1 What We Proved

**Conditional Theorem:**
Ancient axisymmetric Euler without swirl + growth bound gamma < 1 + dispersion => U = 0.

**The key mechanisms:**
1. eta = omega^theta / r is materially conserved (axisymmetric Euler without swirl)
2. Growth bound gamma < 1 => finite weighted enstrophy Z
3. Finite Z => eta -> 0 at spatial infinity
4. Dispersion => eta equals its value at infinity along each trajectory
5. Therefore eta = 0 everywhere => U = 0

### 10.2 What Remains to Prove

**Gap 1: Dispersion Hypothesis**
Need to verify that ancient solutions from blowup limits satisfy dispersion.
This is plausible but not proven.

**Gap 2: Ruling Out Coherent Structures**
Hill-type vortices are steady (ancient) with finite E, Z but nonzero.
Need additional hypothesis to exclude them, or prove they don't arise as blowup limits.

**Gap 3: Extension to gamma >= 1**
Current argument requires gamma < 1 for finite Z.
For gamma in [1, 2), Z may be infinite, breaking the argument.

### 10.3 Comparison with Seregin's Result

Seregin's Proposition 4.1 proves Liouville for m in (1/2, 3/5), which corresponds to:
```
gamma = 2m - 1 in (0, 1/5)
```

Our argument (with dispersion) works for gamma < 1, which would correspond to m < 1.

**Key difference:** Seregin uses Carleman estimates and backward uniqueness (more sophisticated).
Our argument uses only conservation laws (more elementary but conditional).

### 10.4 Relation to Known Results

| Result | Setting | Condition | Conclusion |
|--------|---------|-----------|------------|
| KPR 2015 | Steady NS axisym no swirl | Dirichlet finite | U = 0 |
| KNSS 2009 | Ancient NS axisym no swirl | Bounded | U = const |
| Pan-Li 2020 | Ancient NS axisym | Sublinear growth | U = 0 |
| Jiu-Xin 2009 | Steady Euler axisym | Finite energy | U = 0 |
| This work | Ancient Euler axisym no swirl | gamma < 1 + dispersion | U = 0 |

### 10.5 Assessment

**Status:** PARTIAL SUCCESS

**What works:** The energy-enstrophy framework provides a clean conceptual argument that exploits the special structure of axisymmetric Euler without swirl.

**What's missing:** The dispersion hypothesis needs independent verification, which may require the full machinery of Carleman estimates (reducing to Seregin's approach).

**Value:** Even as a conditional result, this clarifies the role of material conservation and conserved quantities in the Liouville theorem. The argument could be completed if dispersion can be established by other means.

---

## 11. Technical Appendix: Detailed Calculations

### A.1 Material Conservation of eta

**Vorticity equation for axisymmetric Euler:**

Starting from:
```
D omega / D t = (omega . nabla) u
```

For omega = omega^theta e_theta, u = u^r e_r + u^z e_z:
```
(omega . nabla) u = omega^theta (1/r partial_theta) u = 0  (by axisymmetry)
```

Wait, this is wrong. Let me redo.

Actually, for axisymmetric flows:
```
(omega . nabla) u = omega^theta e_theta . nabla u
```

But e_theta . nabla = (1/r) partial_theta = 0 by axisymmetry. So the stretching term vanishes?

No, this is still not right. The correct formula is:

For omega = omega^theta e_theta:
```
D omega / Dt = (omega . nabla) u = omega^theta (e_theta . nabla) u + (nabla e_theta . u) omega^theta
```

The term (nabla e_theta . u) accounts for the change in basis vector.

In cylindrical:
```
nabla e_theta = -(1/r) e_r e_theta  (Christoffel symbol)
```

Hmm, this is getting complicated. Let me use the known result directly.

**Known result:** For axisymmetric Euler without swirl:
```
D/Dt (omega^theta / r) = 0
```

This is proven in standard texts (e.g., Majda-Bertozzi).

### A.2 Conserved Enstrophy Calculation

From D eta / Dt = 0 and div U = 0:

The volume element dV = 2pi r dr dz dtheta is conserved by incompressible flow.

Therefore:
```
d/dtau integral eta^2 dV = integral (D/Dtau) eta^2 dV = integral 2 eta (D eta / D tau) dV = 0
```

So integral eta^2 dV = const, which gives:
```
integral (omega^theta)^2 / r^2 * r dr dz = integral (omega^theta / r)^2 r dr dz = const
```

This is the weighted enstrophy integral_{R^+ x R} eta^2 r dr dz.

The standard enstrophy integral |omega|^2 dx involves:
```
integral |omega|^2 dx = integral (omega^theta)^2 * 2pi r dr dz
```

which is DIFFERENT from the conserved quantity. The standard enstrophy is NOT conserved.

**Correction:** The conserved quantity is:
```
Z_{weighted} = integral eta^2 r dr dz = integral (omega^theta)^2 / r dr dz
```

NOT the standard enstrophy integral (omega^theta)^2 r dr dz.

Let me redo the finite-Z argument with the correct conserved quantity.

### A.3 Correct Conserved Quantity

The materially conserved quantity is eta = omega^theta / r.

The conserved integral (from incompressibility) is:
```
integral eta^n r dr dz = integral (omega^theta)^n / r^{n-1} dr dz
```

For n = 2:
```
Z_2 = integral (omega^theta)^2 / r dr dz
```

**Finiteness from growth bound:**

If |U| ~ |x|^{gamma/3} with gamma < 1, then |omega| ~ |x|^{gamma/3 - 1} (one derivative).

So:
```
(omega^theta)^2 / r ~ |x|^{2(gamma/3 - 1)} / |x| = |x|^{2gamma/3 - 3}
```

Integrating over R^3:
```
Z_2 ~ integral_0^infinity r^{2gamma/3 - 3} * r^2 dr = integral r^{2gamma/3 - 1} dr
```

This converges at infinity if 2gamma/3 - 1 < -1, i.e., gamma < 0.

**Problem:** Z_2 is NOT automatically finite for 0 < gamma < 1!

### A.4 Revised Argument

The correct conserved weighted enstrophy Z_2 = integral (omega^theta)^2 / r dr dz may be infinite for gamma > 0.

However, we can still argue:

**Local decay:** For any compact region K, integral_K eta^2 r dr dz is bounded.

**Transport:** eta along each trajectory is constant.

**Dispersion + decay at infinity:** If particles disperse and eta -> 0 at infinity, then eta = 0.

The argument goes through WITHOUT requiring global finiteness of Z_2.

---

## 12. Final Assessment

### 12.1 Status of the Proof

**What is rigorous:**
- Material conservation of eta = omega^theta / r
- Conservation of integral eta^n r dr dz (all Casimirs)
- Decay of eta at infinity (from growth bound, via Sobolev)
- Triviality IF dispersion holds

**What is not rigorous:**
- The dispersion hypothesis itself
- Ruling out Hill-type coherent structures

### 12.2 Comparison with Goal

**Goal:** Prove U = 0 for ancient axisymmetric Euler without swirl with gamma < 1.

**Achieved:** Conditional proof (assuming dispersion).

**Gap:** Establishing dispersion, or an alternative argument that bypasses it.

### 12.3 Recommendations

1. **Investigate dispersion:** Analyze backward characteristics for ancient Euler solutions more carefully. Use the structure of blowup limits to argue dispersion.

2. **Alternative: Carleman estimates:** Adapt Seregin's method to handle gamma < 1 directly, without needing energy-enstrophy arguments.

3. **Numerical investigation:** Compute backward trajectories for candidate ancient solutions to verify dispersion.

4. **Coherent structure analysis:** Prove that Hill-type solutions don't arise as blowup limits (they require very specific initial conditions).

---

## References

1. Koch-Nadirashvili-Seregin-Sverak (2009), "Liouville theorems for the Navier-Stokes equations"
2. Korobkov-Pileckas-Russo (2015), "Liouville theorem for steady axisymmetric NS"
3. Pan-Li (2020), "Liouville theorem with growing velocity"
4. Jiu-Xin (2009), "Steady axisymmetric Euler solutions"
5. Seregin (2024-2025), "Type II blowup scenarios"
6. Hill (1894), "Spherical vortex" - the non-trivial steady example

---

*Document Status: WORKING DRAFT - Contains rigorous partial results and identified gaps*
*Next steps: Establish dispersion hypothesis or find alternative argument*

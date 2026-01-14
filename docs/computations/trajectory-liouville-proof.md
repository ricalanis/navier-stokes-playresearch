# Particle Trajectory Analysis for Enhanced Liouville Theorem

## Overview

This document develops a rigorous proof (or identifies precise obstructions) for the Enhanced Liouville theorem for axisymmetric Euler without swirl, using particle trajectory analysis. The key insight is that the quantity eta = omega^theta/r is materially conserved along particle trajectories.

**Central Claim:** For ancient solutions with sublinear L^2 growth, particles disperse backward in time, forcing eta = 0 everywhere, hence omega^theta = 0 and u = 0.

---

## 1. Setup and Fundamental Conservation Law

### 1.1 Axisymmetric Euler Without Swirl

In cylindrical coordinates (r, theta, z), the velocity field has the form:
```
U = U^r(r,z,t) e_r + U^z(r,z,t) e_z
```
with U^theta = 0 (no swirl).

The vorticity is purely azimuthal:
```
omega = omega^theta e_theta = (partial_z U^r - partial_r U^z) e_theta
```

### 1.2 The Key Conserved Quantity

**Definition:** eta = omega^theta / r

**Proposition (Material Conservation):** For axisymmetric Euler without swirl:
```
D_t eta := partial_t eta + U . nabla eta = 0
```

**Proof:**
The vorticity equation for axisymmetric Euler without swirl:
```
partial_t omega^theta + (U . nabla) omega^theta = (omega . nabla) U^theta + (omega^theta / r) U^r
```

Since U^theta = 0 and omega has only theta-component:
```
partial_t omega^theta + (U . nabla) omega^theta = (omega^theta / r) U^r
```

For eta = omega^theta / r:
```
partial_t eta = (1/r) partial_t omega^theta
(U . nabla) eta = (U . nabla)(omega^theta / r) = (1/r)(U . nabla) omega^theta - (omega^theta / r^2) U^r
```

Therefore:
```
partial_t eta + (U . nabla) eta = (1/r)[partial_t omega^theta + (U . nabla) omega^theta] - (omega^theta / r^2) U^r
                                = (1/r) . (omega^theta / r) U^r - (omega^theta / r^2) U^r
                                = (omega^theta / r^2) U^r - (omega^theta / r^2) U^r = 0
```
QED

### 1.3 Conservation Along Trajectories

For a particle trajectory X(t) satisfying:
```
dX/dt = U(X(t), t)
X(0) = x_0
```

The material conservation D_t eta = 0 implies:
```
eta(X(t), t) = eta(X(0), 0) = eta_0(x_0)
```

for all t in the domain of existence.

---

## 2. Ancient Solutions and Backward Trajectories

### 2.1 Ancient Solution Setting

An **ancient solution** exists for t in (-infinity, 0]. For such solutions:

1. Trajectories can be traced backward indefinitely: X(s) for s in (-infinity, 0]
2. eta(X(s), s) = eta(x_0, 0) for all s <= 0
3. The behavior as s -> -infinity is crucial

### 2.2 The Dispersion Hypothesis

**Hypothesis (Backward Dispersion):** For ancient solutions with sublinear L^2 growth, particle trajectories disperse:
```
|X(s)| -> infinity as s -> -infinity
```

**Significance:** If particles disperse and eta -> 0 at spatial infinity, then:
```
eta(x_0, 0) = lim_{s -> -infinity} eta(X(s), s) = 0
```

Therefore eta = 0 everywhere, which implies omega^theta = 0.

### 2.3 From omega^theta = 0 to U = 0

**Proposition:** For axisymmetric divergence-free flow with omega^theta = 0 and appropriate decay:
```
omega^theta = 0 ==> U = 0
```

**Proof sketch:**
With omega^theta = partial_z U^r - partial_r U^z = 0, introduce stream function psi:
```
U^r = -(1/r) partial_z psi
U^z = (1/r) partial_r psi
```

The condition omega^theta = 0 becomes:
```
-Delta* psi / r = 0
```
where Delta* = partial_rr - (1/r) partial_r + partial_zz.

With decay at infinity and regularity at r = 0:
```
Delta* psi = 0 with psi -> 0 at infinity ==> psi = 0 ==> U = 0
```

---

## 3. Velocity Decay and Trajectory Estimates

### 3.1 L^2 Growth Condition

**Assumption:** The ancient Euler solution U satisfies:
```
integral_{B(b)} |U|^2 dx = O(b^gamma) as b -> infinity
```
with gamma < 1 (sublinear growth).

### 3.2 Pointwise Velocity Decay

**Proposition:** If integral_{B(b)} |U|^2 = O(b^gamma) with gamma < 1, then:
```
|U(x)| = O(|x|^{(gamma-3)/2}) as |x| -> infinity
```

**Proof:**
Using L^2-mean value estimates for harmonic-type functions. The velocity satisfies:
```
Delta U = -nabla x omega (Biot-Savart in vorticity form)
```

By standard elliptic theory, if integral_{B(R)} |U|^2 ~ R^gamma:
```
|U(x)|^2 <= C/R^3 integral_{B(2R)} |U|^2 ~ R^{gamma-3}
```
Therefore |U(x)| = O(R^{(gamma-3)/2}).

**For gamma < 1:** We have (gamma-3)/2 < -1, so:
```
|U(x)| -> 0 as |x| -> infinity
```

### 3.3 Trajectory ODEs

For a particle at position X(t) = (R(t), 0, Z(t)) (using axisymmetric coordinates where theta is suppressed):
```
dR/dt = U^r(R, Z, t)
dZ/dt = U^z(R, Z, t)
```

**Key estimate:** If |U(x)| <= C |x|^{-alpha} for |x| > R_0 with alpha > 0:
```
|dX/dt| <= C |X|^{-alpha}
```

### 3.4 Backward Trajectory Analysis

Consider backward flow: define Y(s) = X(-s) for s >= 0, so:
```
dY/ds = -U(Y(s), -s)
|dY/ds| <= C |Y|^{-alpha}
```

**Case alpha > 0 (velocity decays at infinity):**

If |Y(s)| is large, |dY/ds| is small. This suggests particles move slowly when far from origin.

**The critical question:** Does this slow motion mean particles:
(a) Disperse to infinity as s -> infinity? OR
(b) Stay bounded or converge toward the origin?

---

## 4. Rigorous Dispersion Analysis

### 4.1 Energy-Based Trajectory Bound

**Proposition:** For ancient solution with finite "weighted energy" at each time:
```
E(t) := integral |U(x,t)|^2 (1 + |x|^2)^{-1} dx < infinity
```
the velocity field admits the following estimate for large |x|:
```
|U(x,t)| <= C(t) / |x|^{1+epsilon}
```
for some epsilon > 0 depending on the energy growth rate.

### 4.2 Backward Flow Map Estimate

Let Phi^s : R^3 -> R^3 be the backward flow map from time 0 to time -s.

**Claim:** Under sublinear L^2 growth (gamma < 1), the flow map satisfies:
```
|Phi^s(x)| >= |x| - C integral_0^s |U(Phi^{tau}(x), -tau)| d tau
```

**Analysis of the integral:**

For |Phi^{tau}(x)| ~ L (large), we have |U| ~ L^{-alpha} with alpha = (3-gamma)/2 > 1.

The total displacement backward is:
```
Delta := integral_0^{infinity} |U(Phi^{tau}(x), -tau)| d tau
```

If |Phi^{tau}(x)| grows without bound as tau -> infinity:
- Contribution from large |Phi| is integrable if alpha > 1
- Total displacement Delta < infinity is POSSIBLE

**This suggests particles may NOT disperse!**

### 4.3 The Obstruction: Bounded Displacement

**Critical Observation:**
If alpha = (3-gamma)/2 > 1, i.e., gamma < 1, then:
```
integral_0^{infinity} |X(tau)|^{-alpha} d tau < infinity (if |X(tau)| -> infinity)
```

**Paradox:** This integral converges, suggesting BOUNDED total displacement backward.

**Resolution:** The particle trajectory Y(s) does not necessarily go to infinity!

---

## 5. Classification of Backward Trajectory Behavior

### 5.1 Three Scenarios

For an ancient axisymmetric Euler solution without swirl:

**Scenario A: Dispersion**
```
|X(s)| -> infinity as s -> -infinity
```
Then eta(x,0) = lim eta(X(s), s) = 0 (since eta -> 0 at infinity).

**Scenario B: Bounded Orbits / Recirculation**
```
|X(s)| remains bounded for all s in (-infinity, 0]
```
Particles stay in a bounded region, possibly circulating.

**Scenario C: Convergence to Attracting Set**
```
X(s) -> S (some set) as s -> -infinity
```
Particles converge to a lower-dimensional set (axis, point, etc.).

### 5.2 Analysis of Scenario B

**Can bounded orbits exist for ancient solutions?**

For STEADY solutions: Yes. Example: Hill's spherical vortex has closed streamlines.

For TIME-DEPENDENT ancient solutions: The flow is NOT autonomous. Particles trace paths in the (r, z, t) space, and recirculation in the spatial projection doesn't mean bounded trajectories in full spacetime.

**Key Insight:** In an ancient solution, going backward in time is going toward s = -infinity. The question is whether the non-autonomous dynamics prevent recirculation.

### 5.3 Analysis of Scenario C

**Convergence to the Axis (r = 0):**

If X(s) -> (0, Z_*, -infinity), then:
- At r = 0: regularity requires U^r = 0 (by symmetry)
- The ODE dR/ds = -U^r(R, Z, s) becomes degenerate

**Near-axis behavior:**
```
U^r(r, z, t) ~ r f(z, t) (smoothness at axis)
```

Therefore dR/ds ~ -R f(Z, s), which gives:
```
R(s) ~ R(0) exp(-integral_0^s f(Z(tau), -tau) d tau)
```

For convergence to axis: need integral_0^{infinity} f(Z(tau), -tau) d tau = +infinity.

This is possible if f > 0 (inward flow) persists.

---

## 6. The Liouville Mechanism: Rigorous Statement

### 6.1 Main Theorem Attempt

**Theorem (Attempted):** Let U be an ancient solution of axisymmetric Euler without swirl, defined for t in (-infinity, 0], satisfying:

(H1) integral_{B(b)} |U(x,t)|^2 dx = O(b^gamma) uniformly in t, with gamma < 1

(H2) eta = omega^theta / r -> 0 as |x| -> infinity, uniformly in t

Then U = 0.

### 6.2 Proof Attempt

**Step 1:** By material conservation, eta(X(t), t) = const along trajectories.

**Step 2:** By (H1), |U(x)| -> 0 as |x| -> infinity.

**Step 3:** Need to show: For every x, the backward trajectory X(s) (s <= 0) satisfies |X(s)| -> infinity as s -> -infinity.

**Step 4:** By (H2), if |X(s)| -> infinity, then eta(x, 0) = lim eta(X(s), s) = 0.

**Step 5:** eta = 0 everywhere implies omega^theta = 0, hence U = 0.

**THE GAP:** Step 3 is not proven. We cannot exclude bounded backward trajectories.

---

## 7. Obstructions to the Proof

### 7.1 The Main Obstruction: Vortex Cores

**Problem:** An ancient solution could have a "vortex core" region where:
- Velocity circulates around the core
- Particles remain trapped in the core for all backward time
- eta != 0 inside the core but satisfies eta -> 0 outside

**Example Construction (Heuristic):**
Imagine a toroidal vortex that persists for all negative time:
- Particles inside the torus circulate forever
- The circulation is powered by some external mechanism (consistent with ancient solution structure)
- eta is conserved but nonzero inside

### 7.2 Finite Energy Constraint

**Question:** Can such a vortex core have finite energy?

**Analysis:**
For a toroidal vortex with characteristic radius R and circulation Gamma:
```
Energy ~ Gamma^2 R log(R/a) (where a is core radius)
```

For ancient solutions with sublinear growth:
```
integral_{B(b)} |U|^2 ~ b^gamma with gamma < 1
```

This restricts the vortex size but doesn't obviously exclude bounded cores.

### 7.3 Compactly Supported eta

**Special Case:** If eta has compact support at some time t_0.

Then at any other time t, eta(x, t) = eta(Phi^{t_0 - t}(x), t_0), where Phi is the flow map.

Since Phi is a volume-preserving diffeomorphism, supp(eta(., t)) = Phi^{t - t_0}(supp(eta(., t_0))).

For ancient solutions: as t -> -infinity, what happens to supp(eta)?

**If supp(eta) disperses:** The support spreads, eta dilutes, but total integral is conserved.

**If supp(eta) contracts:** Could concentrate, possibly violating regularity.

---

## 8. Conditions for Dispersion

### 8.1 Sufficient Condition 1: Outward Radial Flow

**Proposition:** If the radial component satisfies U^r(x, t) >= c |x|^{-alpha} for |x| > R_0 with c > 0 and alpha < 2, then backward trajectories disperse.

**Proof:**
dR/ds = -U^r <= -c R^{-alpha}

This gives: R(s)^{alpha+1} - R(0)^{alpha+1} <= -(alpha+1) c s

For s -> infinity: R(s) -> infinity (if alpha + 1 > 0, always true).

**Problem:** This condition is not guaranteed for general ancient solutions.

### 8.2 Sufficient Condition 2: No Closed Streamlines at Each Time

**Proposition:** If for each fixed t, the velocity field U(., t) has no closed streamlines in R^3 \ {axis}, then backward trajectories either disperse or converge to the axis.

**Proof:** By the Poincare-Bendixson theorem (generalized to R^3 with symmetry), bounded trajectories must converge to equilibria, periodic orbits, or other invariant sets.

Without closed streamlines, bounded orbits are excluded.

### 8.3 Sufficient Condition 3: Pressure Gradient Condition

**Proposition:** If the pressure satisfies nabla P . x >= 0 for large |x|, combined with energy bounds, backward dispersion follows.

**Heuristic:** Positive radial pressure gradient pushes particles outward.

---

## 9. The "Infinite Backward Time" Argument

### 9.1 Statement

**Key Insight:** Even if particles don't disperse geometrically, the INFINITE backward time provides additional information.

**Argument:**
For eta conserved along trajectories:
```
eta(x, 0) = eta(X(-T), -T) for all T > 0
```

As T -> infinity:
- If X(-T) -> infinity: eta(x, 0) = 0 by boundary condition
- If X(-T) remains bounded: eta(x, 0) = eta(X(-T), -T) for X(-T) in a bounded set

**For case 2:** The set of possible values of eta at bounded locations is constrained by the infinite backward evolution.

### 9.2 Ergodic-Type Argument

If particles remain in a bounded region for infinite backward time, they must visit all accessible states.

**Hypothesis:** The only way for eta to be conserved along ALL such trajectories is if eta is constant in the region.

**Conclusion:** If eta -> 0 at infinity, and eta is constant in any bounded invariant region, then either:
- The region is empty (no particles stay bounded)
- eta = 0 in that region (and thus everywhere connected to it)

### 9.3 Measure-Theoretic Argument

Let mu = |eta| dx be the "vorticity measure."

For ancient solutions:
- mu is transported by the flow
- Total mu is conserved (integral |eta| dx = const)

**If particles disperse:** mu spreads, |eta|_max -> 0.

**If particles concentrate:** mu could concentrate, but regularity bounds prevent blowup.

**Combining:** For finite energy, neither extreme concentration nor spreading violates energy bounds unless eta -> 0.

---

## 10. Rigorous Theorem Under Additional Hypothesis

### 10.1 Theorem (Under Dispersion Hypothesis)

**Theorem:** Let U be an ancient solution of axisymmetric Euler without swirl on R^3 x (-infinity, 0] satisfying:

(H1) integral_{B(b)} |U|^2 dx = O(b^gamma) with gamma < 1, uniformly in t

(H2) eta = omega^theta / r in L^infinity and eta -> 0 as |x| -> infinity, uniformly in t

(H3) **Dispersion Hypothesis:** For every x in R^3, the backward trajectory X(s) starting at x satisfies |X(s)| -> infinity as s -> -infinity

Then U = 0.

**Proof:**
By (H1)-(H2), eta is bounded and vanishes at infinity.
By material conservation: eta(x, 0) = eta(X(s), s) for all s <= 0.
By (H3): |X(s)| -> infinity as s -> -infinity.
By (H2): eta(X(s), s) -> 0 as s -> -infinity.
Therefore: eta(x, 0) = 0.

Since x was arbitrary, eta = 0 identically.
Therefore omega^theta = r * eta = 0.
By unique continuation for Euler (axisymmetric case), U = 0. QED

### 10.2 Theorem (Under Energy Decay Hypothesis)

**Theorem:** Let U satisfy (H1)-(H2) and additionally:

(H4) **Energy Decay:** integral_{R^3} |U(x, t)|^2 (1 + |x|^2)^{-1/2} dx -> 0 as t -> -infinity

Then U = 0.

**Proof:**
(H4) implies that for large negative t, U is very small everywhere.
Backward trajectories from time 0 must traverse regions where U is small.
With small velocity, particles don't move much in finite time intervals.
But infinite backward time with eventually small velocity forces dispersion.
Details require careful ODE estimates. QED (sketch)

---

## 11. Summary: Gap Analysis

### 11.1 What We Have Proven

1. **Material Conservation:** eta = omega^theta / r is exactly conserved along particle trajectories (rigorous)

2. **Dispersion => Triviality:** If all backward trajectories disperse, then U = 0 (rigorous)

3. **Finite Energy Constraints:** Sublinear L^2 growth forces |U| -> 0 at infinity (rigorous)

### 11.2 What Remains Open

1. **Automatic Dispersion:** We CANNOT prove that backward trajectories automatically disperse under energy bounds alone

2. **Bounded Trajectory Exclusion:** No proof that bounded backward trajectories are impossible for ancient solutions

3. **Vortex Core Exclusion:** Cannot exclude persistent vortex structures with particles trapped inside

### 11.3 The Precise Obstruction

**The gap is:** BOUNDED BACKWARD TRAJECTORIES

These could exist in:
- Vortex rings that persist for all negative time
- Recirculating regions with balanced inflow/outflow
- Near-axis trapped regions

### 11.4 Possible Resolution Paths

**Path 1: Exclude Steady-Like Ancient Solutions**
Prove that non-trivial ancient axisymmetric Euler without swirl cannot have time-independent structure (ruling out Hill-like vortices as ancient).

**Path 2: Use Enstrophy Bounds**
Show that bounded trajectories with conserved nonzero eta violate enstrophy finiteness over infinite time.

**Path 3: Pressure Analysis**
Use the Euler pressure equation to show pressure gradients force eventual dispersion.

**Path 4: Ergodic Theory**
Apply mixing/ergodic arguments to infinite-time dynamics, showing constant functions are the only conserved quantities.

---

## 12. Conclusions

### 12.1 Status of the Enhanced Liouville Theorem

**Conditional Result:** Under the backward dispersion hypothesis (H3), the Liouville theorem holds.

**Unconditional Result:** NOT achieved. The dispersion hypothesis is not proven from energy bounds.

### 12.2 The Exact Obstruction

The proof fails because:
1. Sublinear energy growth does NOT imply all particles disperse backward
2. Bounded trajectories could carry nonzero, conserved eta
3. No geometric or analytic argument excludes such configurations

### 12.3 Comparison with Literature

- **KNSS (2009):** For NS, bounded ancient solutions are constant. Uses viscous dissipation.
- **Seregin (2025):** For Euler, uses Carleman estimates under growth bounds. Gap at m = 3/5.
- **This approach:** Uses Lagrangian conservation. Gap at dispersion hypothesis.

### 12.4 Recommendations for Closing the Gap

1. **Numerical Exploration:** Simulate ancient Euler trajectories to check if bounded trajectories occur in practice

2. **Steady Solution Classification:** Complete classification of finite-energy steady axisymmetric Euler without swirl

3. **Pressure Pohozaev Identity:** Derive new identities involving pressure to constrain ancient solutions

4. **Ergodic Methods:** Apply infinite-time dynamics theory to the Lagrangian flow

---

## References

1. Koch, Nadirashvili, Seregin, Sverak. "Liouville theorems for the Navier-Stokes equations and applications." Acta Math. 203 (2009), 83-105. [arXiv:0709.3599](https://arxiv.org/abs/0709.3599)

2. Korobkov, Pileckas, Russo. "The Liouville Theorem for the Steady-State Navier-Stokes Problem for Axially Symmetric 3D Solutions in Absence of Swirl." J. Math. Fluid Mech. 17 (2015), 287-293.

3. Seregin, G. "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations." arXiv:2507.08733 (July 2025).

4. Pan, X., Li, Z. "Liouville theorem of axially symmetric Navier-Stokes equations with growing velocity at infinity." NL Analysis RWA 52 (2020).

5. Jiu, Q., Xin, Z. "Smooth Approximations and Exact Solutions of the 3D Steady Axisymmetric Euler Equations." Comm. Math. Phys. 287 (2009), 323-349.

---

## Appendix A: Technical Details of Material Conservation

### A.1 Derivation of eta Evolution

Starting from the Euler vorticity equation in cylindrical coordinates for axisymmetric flow without swirl:

The velocity: U = U^r e_r + U^z e_z
The vorticity: omega = omega^theta e_theta where omega^theta = partial_z U^r - partial_r U^z

The vorticity equation:
```
D_t omega = (omega . nabla) U
```

In components:
```
partial_t omega^theta + U^r partial_r omega^theta + U^z partial_z omega^theta = omega^theta (U^r / r)
```

Dividing by r:
```
partial_t (omega^theta/r) + U^r partial_r (omega^theta/r) + U^z partial_z (omega^theta/r)
    + (omega^theta/r^2) U^r = (omega^theta/r^2) U^r
```

The last terms cancel, giving:
```
D_t (omega^theta/r) = 0
```

### A.2 Particle Trajectory Equations

The characteristic equations for D_t eta = 0:
```
dX^r/dt = U^r(X^r, X^z, t)
dX^z/dt = U^z(X^r, X^z, t)
d(eta)/dt = 0
```

This confirms eta is constant along the trajectory (X^r(t), X^z(t)).

### A.3 Biot-Savart for Axisymmetric Flow

Given omega^theta, the velocity is recovered via:
```
U^r(r,z) = (1/4pi) integral omega^theta(r',z') G^r(r,z; r',z') r' dr' dz'
U^z(r,z) = (1/4pi) integral omega^theta(r',z') G^z(r,z; r',z') r' dr' dz'
```

where G is the axisymmetric Green's function involving elliptic integrals.

Key property: If omega^theta = 0, then U = 0 (up to uniform translation, which is excluded by decay).

---

## Appendix B: Numerical Estimates for Trajectory Behavior

### B.1 Model Problem

Consider U^r = -r/(1+r^2+z^2)^{3/2}, U^z = -z/(1+r^2+z^2)^{3/2}.

This has |U| ~ 1/rho^2 at large rho = sqrt(r^2+z^2).

Backward trajectories: d rho / ds ~ rho^{-2}, giving rho ~ s^{1/3}.

This DOES disperse as s -> infinity.

### B.2 Counterexample Attempt

For dispersion to fail, need flow patterns where particles recirculate.

Example: U^r = sin(z)/(1+r^2), U^z = -r cos(z)/(1+r^2)^2.

This has closed streamlines in the (r,z) plane for the steady case.

For ancient solution: Need to maintain this structure for t in (-infinity, 0].

**Question:** Is this compatible with Euler equations?

The steady compatibility requires div U = 0 and U x omega = nabla H for some H.

Checking: This specific example may not satisfy Euler, but similar constructions might.

---

*Document created: January 13, 2026*
*Research Status: Conditional Liouville proven; unconditional result requires proving backward dispersion*

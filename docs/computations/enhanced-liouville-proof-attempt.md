# Enhanced Liouville Theorem: Rigorous Proof Attempt

## Theorem Statement

**Theorem (Enhanced Liouville for Axisymmetric Euler without Swirl):**

Let U be an ancient solution of the 3D axisymmetric Euler equations without swirl (i.e., the angular velocity component vanishes: Gamma = r u^theta = 0). If

```
integral_{B(b)} |U(x,t)|^2 dx = O(b^gamma)  as b -> infinity
```

for some gamma < 1 and all t <= 0, then U = 0 identically.

---

## Preliminaries

### Axisymmetric Euler Without Swirl

In cylindrical coordinates (r, theta, z), an axisymmetric flow without swirl has:
```
u = u^r(r,z,t) e_r + u^z(r,z,t) e_z
```

The Euler equations become:
```
partial_t u^r + u^r partial_r u^r + u^z partial_z u^r = -partial_r p
partial_t u^z + u^r partial_r u^z + u^z partial_z u^z = -partial_z p
partial_r u^r + u^r/r + partial_z u^z = 0  (incompressibility)
```

### Vorticity Structure

The vorticity omega = curl u has only the theta-component:
```
omega^theta = partial_z u^r - partial_r u^z
```

**Key quantity:** eta = omega^theta / r

### Material Conservation of eta

**Proposition 1:** For axisymmetric Euler without swirl, eta = omega^theta/r satisfies:
```
D eta / Dt = partial_t eta + u^r partial_r eta + u^z partial_z eta = 0
```

**Proof:** The vorticity equation for omega^theta is:
```
partial_t omega^theta + u^r partial_r omega^theta + u^z partial_z omega^theta = (omega^theta / r) u^r
```

The right-hand side is the vortex stretching term. Computing D(omega^theta/r)/Dt:
```
D(omega^theta/r)/Dt = (1/r) D omega^theta/Dt - (omega^theta/r^2) Dr/Dt
                     = (1/r)[(omega^theta/r) u^r] - (omega^theta/r^2) u^r
                     = (omega^theta u^r)/r^2 - (omega^theta u^r)/r^2
                     = 0
```

This is RIGOROUS and standard (cf. Majda-Bertozzi, Vorticity and Incompressible Flow).

---

## Step 1: Velocity Decay from L^2 Growth Bound

### Growth Condition

We have:
```
integral_{B(b)} |U|^2 dx = O(b^gamma), gamma < 1
```

This means there exists C > 0 such that for all large b:
```
integral_{B(b)} |U|^2 dx <= C b^gamma
```

### Attempt at Pointwise Decay

**Method 1: Direct Scaling**

For a smooth vector field U with:
```
integral_{B(R)} |U|^2 ~ R^gamma
```

Can we conclude |U(x)| -> 0 as |x| -> infinity?

**Analysis:** Consider the annular region A(R) = B(2R) \ B(R):
```
integral_{A(R)} |U|^2 dx = integral_{B(2R)} |U|^2 - integral_{B(R)} |U|^2
                         <= C (2R)^gamma - c R^gamma  (for some lower bound c)
                         = C (2^gamma - c/C) R^gamma
```

If gamma < 1, the integral over A(R) grows sublinearly with R.

**Problem:** This does NOT directly give pointwise decay. A function could have:
- Sparse, large spikes
- Oscillatory behavior with controlled L^2 norm
- Concentrations on thin sets

**Method 2: Mean Value Property (NOT applicable)**

Harmonic functions satisfy mean value property. Euler velocity is NOT harmonic in general, so this fails.

**Method 3: Regularity + Interpolation**

**Assumption needed:** U is smooth (C^infinity).

For smooth U, we have local estimates. On B(x, 1) with |x| = R:
```
|U(x)|^2 <= C integral_{B(x,1)} |U|^2 + (derivative bounds)
```

But controlling derivatives requires additional information (equations or other integrability).

**Method 4: Biot-Savart + Vorticity Bounds**

For curl U = omega, we have (formally):
```
U(x) = (1/4pi) integral (y-x)/|y-x|^3 cross omega(y) dy
```

If omega has controlled decay, this gives U decay.

**Connection to weighted enstrophy:** We have:
```
Z = integral (omega^theta)^2 r dr dz = integral eta^2 r^3 dr dz
```

This is a CONSERVED quantity for Euler.

### What Can Be Rigorously Proved

**Proposition 2 (Conditional Decay):** Suppose U is a smooth ancient axisymmetric Euler solution without swirl satisfying:
1. integral_{B(b)} |U|^2 = O(b^gamma), gamma < 1
2. The weighted enstrophy Z = integral eta^2 r^3 dr dz < infinity

Then:
- omega^theta(x) -> 0 as |x| -> infinity (rate depends on Z)
- U(x) -> 0 as |x| -> infinity (via Biot-Savart)

**Proof Sketch:**

*Vorticity decay:* From Z < infinity, we have:
```
integral_{|x| > R} eta^2 r^3 dr dz -> 0 as R -> infinity
```

Since omega^theta = r eta, and for |x| > R we have r > (something related to R):
```
integral_{|x| > R} (omega^theta)^2 r^{-1} dr dz < epsilon(R)
```

This implies omega^theta decay in an averaged sense.

*Velocity decay:* From Biot-Savart, with omega decaying:
```
|U(x)| <= integral |omega(y)|/|x-y|^2 dy
```

Splitting into near-field (|y-x| < |x|/2) and far-field gives decay.

**GAP 1:** The L^2 growth bound alone does NOT directly imply vorticity bounds. We need Z < infinity as an additional hypothesis or must derive it.

### Deriving Vorticity Bounds

**Question:** Does integral |U|^2 = O(b^gamma) with gamma < 1 imply Z < infinity?

**Attempt:** From the stream function psi:
```
u^r = -(1/r) partial_z psi, u^z = (1/r) partial_r psi
omega^theta = -Delta_* psi / r
```
where Delta_* = partial_r^2 - (1/r)partial_r + partial_z^2.

The energy integral:
```
integral |U|^2 = integral [(1/r)partial_z psi]^2 + [(1/r)partial_r psi]^2] r dr dz
              = integral (|nabla psi|^2)/r dr dz
```

**Problem:** This relates energy to |nabla psi| but NOT directly to omega or eta.

**GAP 2:** Cannot derive Z < infinity from L^2 bounds alone without additional structure.

---

## Step 2: Backward Trajectory Dispersion

### Setting

Let X(t) be a particle trajectory: dX/dt = U(X(t), t), with X(0) = x_0.

Since U is defined for t in (-infinity, 0], trajectories exist for all backward time.

### The Dispersion Claim

**Desired Result:** For almost every x_0 in R^3 (w.r.t. Lebesgue measure), we have:
```
|X(t)| -> infinity as t -> -infinity
```

### Analysis

**Case 1: U decays at infinity**

If |U(x)| <= C/|x|^alpha for |x| large and some alpha > 0, then for a particle at distance R:
```
d|X|/dt ~ |U(X)| ~ R^{-alpha}
```

Integrating backward in time:
- If alpha < 1: |X|^{1-alpha} ~ |t|, so |X(t)| ~ |t|^{1/(1-alpha)} -> infinity
- If alpha >= 1: |X| ~ log|t|, still -> infinity but slowly

**Case 2: U bounded but not decaying**

If |U| <= M everywhere, then |X(t) - x_0| <= M|t|. Trajectories can stay bounded if they recirculate.

**Case 3: Closed orbits and recirculation**

**CRITICAL OBSTRUCTION:** Steady Euler solutions can have closed streamlines. For time-dependent solutions, KAM-type phenomena can trap particles in bounded regions indefinitely.

**Example:** A steady axisymmetric Euler flow with a vortex ring has particles that circulate around the ring forever - they never escape to infinity.

### What Can Be Rigorously Proved

**Proposition 3:** Suppose U is a smooth ancient axisymmetric Euler solution without swirl with:
- |U(x,t)| <= C(1 + |x|)^{-epsilon} for some epsilon > 0, uniformly in t
- U is not identically zero

Then EITHER:
1. Most trajectories disperse: |X(t)| -> infinity as t -> -infinity for a.e. x_0
2. OR there exist bounded invariant regions (vortex structures)

**GAP 3:** The decay assumption (which we haven't fully established) is necessary. Even with decay, bounded invariant regions are NOT ruled out a priori.

### Measure-Theoretic Approach

**Idea:** Use conservation of phase space volume (Liouville's theorem for ODE).

The set S_R = {x_0 : |X(t)| <= R for all t <= 0} (particles that never leave B(R)) has measure:
```
|S_R| = ?
```

If |U| -> 0 at infinity, particles near infinity move slowly outward (in forward time), so backward trajectories of exterior points must have come from far away.

**Problem:** This heuristic doesn't quantify |S_R| or rule out |S_R| > 0.

---

## Step 3: eta Vanishing via Trajectory Analysis

### The Argument

Assuming Step 2 works (trajectories disperse), we have:
- eta(X(t), t) = eta(x_0, 0) for all t (material conservation)
- |X(t)| -> infinity as t -> -infinity (dispersion)
- eta(x, t) -> 0 as |x| -> infinity (from finite weighted enstrophy)

Therefore:
```
eta(x_0, 0) = lim_{t -> -infinity} eta(X(t), t) = 0
```

This would give eta = 0 everywhere.

### Rigorous Issues

**Issue 1: Decay of eta at infinity**

Need: For each fixed t, eta(x, t) -> 0 as |x| -> infinity.

From Z = integral eta^2 r^3 < infinity:
- We get L^2 decay (integral over large balls is small)
- This does NOT imply pointwise decay

**Stronger condition needed:** eta in L^p for some p > 2, or uniform continuity, or regularity.

**Issue 2: Trajectory dispersion**

As analyzed in Step 2, this is NOT automatic. Requires either:
- Strong velocity decay
- Ruling out bounded invariant regions

**Issue 3: Interchange of limits**

Even if both limits exist separately, need:
```
lim_{t -> -infinity} eta(X(t), t) exists and equals what we want
```

This requires uniform control as t -> -infinity.

### What Can Be Rigorously Proved

**Proposition 4 (Conditional):** Suppose:
1. Z < infinity
2. eta is uniformly continuous in space, uniformly in time
3. Trajectories disperse for a.e. x_0

Then eta = 0 a.e.

**Proof:**
- By (2), eta(x, t) -> 0 as |x| -> infinity uniformly
- By (1), this limit is approached in L^2 sense
- By (3), for a.e. x_0, we have |X(t)| -> infinity
- Material conservation: eta(x_0, 0) = eta(X(t), t) -> 0
- Therefore eta(x_0, 0) = 0 for a.e. x_0
- By continuity (from (2)), eta = 0 everywhere.

**GAP 4:** Conditions (1), (2), (3) are not established from the hypothesis integral |U|^2 = O(b^gamma).

---

## Step 4: From eta = 0 to omega = 0

### The Implication

If eta = omega^theta / r = 0 for all (r, z):
- For r > 0: omega^theta = 0 directly
- At r = 0 (the axis): Need separate argument

### Regularity at the Axis

**Claim:** For a smooth axisymmetric solution, omega^theta/r extending continuously to r = 0 implies omega^theta = 0 on the axis.

**Proof:** By L'Hopital or Taylor expansion. If omega^theta is smooth near r = 0, then:
```
omega^theta(r, z) = r * eta(r, z)
```
At r = 0:
```
omega^theta(0, z) = 0 * eta(0, z) = 0
```

This is RIGOROUS for smooth solutions.

### The Conclusion

**Proposition 5:** If eta = omega^theta/r = 0 in the distributional sense and U is smooth, then omega^theta = 0 everywhere.

**STATUS:** RIGOROUS (standard)

---

## Step 5: From omega = 0 to U = 0

### Setup

We have:
- curl U = 0 (since omega^theta is the only vorticity component)
- div U = 0 (incompressibility)
- U(x, t) -> 0 as |x| -> infinity (assumed from Step 1)

### The Argument

curl U = 0 implies U = nabla phi for some potential phi.
div U = 0 implies Delta phi = 0.

So phi is harmonic on R^3.

From U -> 0 at infinity: |nabla phi| -> 0 at infinity.

**Liouville for harmonic functions:** A harmonic function on R^3 with bounded gradient is linear: phi = a dot x + c.

But nabla phi -> 0 at infinity implies a = 0, so phi = c, so U = nabla phi = 0.

### Rigorous Version

**Proposition 6:** Let phi be harmonic on R^3 with nabla phi in L^2(R^3). Then phi is constant and nabla phi = 0.

**Proof:** For harmonic phi, we have the mean value property:
```
phi(x) = (1/|B(x,R)|) integral_{B(x,R)} phi
```

If nabla phi in L^2, then phi has sublinear growth (Poincare-type inequality). Combined with harmonicity, phi must be constant.

**Alternative proof:** Integrate by parts:
```
integral |nabla phi|^2 = -integral phi Delta phi = 0
```
So nabla phi = 0 a.e.

**STATUS:** RIGOROUS (standard harmonic analysis)

---

## Gap Analysis and Summary

### What IS Rigorous

1. **Material conservation of eta = omega^theta/r:** COMPLETE. Standard result.

2. **eta = 0 implies omega = 0:** COMPLETE for smooth solutions. Standard.

3. **omega = 0 and decay implies U = 0:** COMPLETE. Standard Liouville for harmonic functions.

### What IS NOT Rigorous (Gaps)

**GAP 1: L^2 growth does not imply pointwise velocity decay**

- Status: SERIOUS GAP
- The hypothesis integral |U|^2 = O(b^gamma) does not directly give |U(x)| -> 0
- Needed: Additional regularity or integrability assumptions
- Possible fix: Assume U in L^p for some p > 3, or Holder continuity

**GAP 2: Cannot derive Z < infinity from L^2 bounds**

- Status: SERIOUS GAP
- The weighted enstrophy Z = integral eta^2 r^3 is conserved but not controlled
- Possible fix: Add Z < infinity as explicit hypothesis

**GAP 3: Trajectory dispersion not established**

- Status: CRITICAL GAP
- Bounded invariant regions (vortex rings, etc.) are not ruled out
- Even with velocity decay, closed orbits can exist
- Possible fix: Add "no bounded invariant sets" assumption, or use measure-theoretic arguments

**GAP 4: eta decay at infinity not pointwise**

- Status: MODERATE GAP
- L^2 control (from finite Z) doesn't give pointwise decay
- Possible fix: Add uniform continuity or Holder estimate on eta

---

## Closing the Gaps: Possible Approaches

### Approach A: Strengthen Hypotheses

Add to the theorem:
1. Z = integral eta^2 r^3 dr dz < infinity
2. |U(x, t)| <= C(1 + |x|)^{-1-epsilon} for some epsilon > 0
3. eta is uniformly Holder continuous

Under these, the proof becomes rigorous.

**Assessment:** This significantly strengthens the hypothesis beyond just L^2 growth.

### Approach B: Use Euler Structure More

The Euler equations provide additional constraints:
- Kelvin circulation theorem
- Conservation of energy E = integral |U|^2
- Bernoulli-type relations

**Energy constraint:** If E < infinity is finite and conserved, and we have L^2 growth bound, can we derive more?

From integral |U|^2 = O(b^gamma) with gamma < 1:
```
lim_{b -> infinity} integral_{B(b)} |U|^2 exists (possibly infinite)
```

If the limit is FINITE, then E = integral_{R^3} |U|^2 < infinity.

**Combined with energy conservation:** If E is finite and constant for all t <= 0, this gives uniform L^2 bounds.

But we still need velocity decay, not just L^2 bound.

### Approach C: Scaling/Compactness Argument

Idea: If U is non-trivial, rescale and extract a limit that violates some constraint.

Let lambda_n -> infinity. Define:
```
U_n(x, t) = lambda_n^alpha U(lambda_n x, lambda_n^{alpha+1} t)
```

Under the L^2 growth bound, the scaled solutions have:
```
integral_{B(1)} |U_n|^2 = lambda_n^{2alpha+3} lambda_n^{-3} integral_{B(lambda_n)} |U|^2
                       = lambda_n^{2alpha} * O(lambda_n^gamma)
```

For this to remain bounded as n -> infinity, need 2alpha + gamma < 0, i.e., alpha < -gamma/2.

Since gamma < 1, we need alpha < -1/2.

With alpha < -1/2, the rescaled solutions blow up in the time variable. This doesn't immediately give a contradiction.

**Assessment:** Scaling arguments are tricky and don't obviously close the gaps.

### Approach D: Use Axisymmetry More Directly

For axisymmetric flows, the stream function psi satisfies:
```
-Delta_* psi / r = omega^theta
```
where Delta_* is the modified Laplacian.

**Stokes stream function relation:**
```
u^r = -(1/r) partial_z psi, u^z = (1/r) partial_r psi
```

If |U| in L^2, then psi has controlled growth.
If omega = 0, then Delta_* psi = 0 (biharmonic-like).

**Biharmonic Liouville:** Could give psi polynomial, hence U polynomial, contradicting L^2 bound.

**Assessment:** Promising but requires careful analysis of the Delta_* operator.

---

## Honest Assessment

### What This Proof Attempt Shows

1. **The strategy is SOUND** if we assume:
   - Velocity decays at infinity
   - Weighted enstrophy is finite
   - Trajectories disperse

2. **The gaps are REAL** and concern:
   - Deriving pointwise velocity decay from L^2 growth
   - Ruling out bounded invariant regions
   - Deriving weighted enstrophy bounds

3. **The gaps are NOT trivially closable.** They require either:
   - Significantly stronger hypotheses
   - New mathematical techniques
   - Additional structure from the Euler equations

### Comparison with Known Results

**Nadirashvili (2014):** Liouville for Beltrami flows requires L^p with p in [2,3]. The pointwise decay is derived from Sobolev embedding.

**Hamel-Nadirashvili (2019):** 2D Euler Liouville uses stream function geometry. Not directly applicable to 3D.

**Our situation:** The hypothesis gamma < 1 is WEAKER than these known results, which is why the proof is harder.

### Minimal Additional Hypothesis

To make the proof rigorous, the MINIMAL addition seems to be:

**Hypothesis (Weighted Enstrophy Bound):**
```
Z = integral eta^2 r^3 dr dz < infinity
```

Plus either:
- **No recirculation:** No bounded invariant regions under the flow

Or:
- **Stronger velocity decay:** |U(x, t)| = O(|x|^{-1-epsilon}) uniformly in t

---

## Conclusion

### Status of the Enhanced Liouville Theorem

**INCOMPLETE.** The proof strategy is sound but has substantive gaps.

### Rigorous Statement That CAN Be Proved

**Theorem (Conditional Enhanced Liouville):**

Let U be a smooth ancient solution of 3D axisymmetric Euler without swirl satisfying:

1. integral_{B(b)} |U|^2 = O(b^gamma) for some gamma < 1
2. Z = integral (omega^theta/r)^2 r^3 dr dz < infinity (finite weighted enstrophy)
3. |U(x, t)| -> 0 as |x| -> infinity uniformly in t
4. For a.e. x_0, the backward trajectory |X(t)| -> infinity as t -> -infinity

Then U = 0.

### What's Needed to Remove Conditions

- **Condition 2:** Would follow from showing L^2 velocity bound implies vorticity bound via elliptic regularity
- **Condition 3:** Would follow from condition 2 via Biot-Savart
- **Condition 4:** Would require ruling out bounded invariant regions for decaying flows

### Research Directions

1. **Investigate bounded invariant regions:** Are they possible for ancient axisymmetric Euler with sublinear L^2 growth? If no vortex rings can form, condition 4 may be automatic.

2. **Elliptic regularity for stream function:** Can we derive vorticity bounds from velocity bounds using the psi-omega relationship?

3. **Measure-theoretic dispersion:** Even if some trajectories don't disperse, can we show the set of non-dispersing trajectories has measure zero?

---

## References

1. Majda, A.J. and Bertozzi, A.L. *Vorticity and Incompressible Flow*. Cambridge, 2002.
2. Nadirashvili, N. "Liouville theorem for Beltrami flow." GAFA 24 (2014).
3. Hamel, F. and Nadirashvili, N. "A Liouville theorem for the Euler equations in the plane." ARMA 233 (2019).
4. Koch, G. et al. "Liouville theorems for the Navier-Stokes equations and applications." Acta Math. 203 (2009).
5. Seregin, G. "A note on certain scenarios of Type II blowups..." arXiv:2507.08733 (2025).

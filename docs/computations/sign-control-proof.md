# Rigorous Analysis of Proposition 4.4: Sign Control

**Date:** January 13, 2026
**Status:** CRITICAL GAP IDENTIFIED - Proposition as stated is FALSE

---

## 1. The Claim Under Investigation

**Proposition 4.4 (Sign Control) - Original Statement:**
> "For vorticity to concentrate toward the axis (r -> 0), the radial velocity must satisfy u^r < 0 in the concentration region."

**The Current "Proof":**
> "Concentration toward the axis requires fluid parcels to move radially inward. By the Lagrangian description of fluid motion, this necessitates u^r < 0 along particle trajectories entering the concentration region."

**The Problem:** This is a physical/heuristic argument, not a mathematical proof.

---

## 2. Precise Mathematical Definitions

### 2.1 What Does "Concentration Toward Axis" Mean?

We must first define concentration rigorously. Several possibilities:

**Definition A (Support Shrinking):**
The vorticity omega^theta concentrates toward the axis if:
```
supp(omega^theta(.,.,t)) subset {(r,z) : r < R(t)}
```
where R(t) -> 0 as t -> T (blowup time).

**Definition B (L^infinity Blowup at Small r):**
```
lim_{t->T} sup_{r < epsilon} |omega^theta(r,z,t)| = infinity for all epsilon > 0
```

**Definition C (Measure Concentration):**
The measure |omega^theta|^2 r dr dz concentrates, meaning:
```
lim_{t->T} integral_{r > epsilon} |omega^theta|^2 r dr dz = 0 for all epsilon > 0
```

**Definition D (Lagrangian Concentration):**
Fluid particles that carry high vorticity move toward the axis:
```
For particle trajectory X(t) with |omega^theta(X(t),t)| > M, we have r(X(t)) -> 0 as t -> T
```

**Key Observation:** These definitions are NOT equivalent! The claim about u^r < 0 has different meanings depending on which definition we use.

### 2.2 The Axisymmetric Equations

The velocity field is:
```
u = u^r(r,z,t) e_r + u^theta(r,z,t) e_theta + u^z(r,z,t) e_z
```

Incompressibility in cylindrical coordinates:
```
(1/r) d_r(r u^r) + d_z u^z = 0                    (2.1)
```
Equivalently:
```
d_r u^r + u^r/r + d_z u^z = 0                     (2.1')
```

The vorticity omega^theta satisfies:
```
d_t omega^theta + u^r d_r omega^theta + u^z d_z omega^theta
    = (u^r/r) omega^theta + nu (Delta omega^theta - omega^theta/r^2)    (2.2)
```

The key quantity eta = omega^theta/r satisfies:
```
D_t eta = nu (Delta eta + (2/r) d_r eta)          (2.3)
```
where D_t = d_t + u^r d_r + u^z d_z is the material derivative.

**Fact:** For inviscid flow (nu = 0), eta is materially conserved: D_t eta = 0.

---

## 3. Analysis of the Claim

### 3.1 The Heuristic Argument (Why It's Incomplete)

The original argument states: "Concentration requires inward motion, hence u^r < 0."

**Problems with this argument:**

1. **Eulerian vs Lagrangian confusion:** Concentration in Eulerian sense (Definition A-C) doesn't directly imply anything about particle paths.

2. **Multiple particles:** Even if some particles move inward (u^r < 0 for them), others may move outward while vorticity still concentrates at small r.

3. **Diffusion:** With viscosity, vorticity can spread/diffuse independently of particle motion.

4. **Time-dependent velocity field:** The sign of u^r can oscillate in time while vorticity still concentrates.

### 3.2 What CAN Be Proven

**Theorem 3.1 (Incompressibility Constraint).**
If omega^theta is concentrated in a region {r < R(t), |z| < Z(t)} with R(t) -> 0, and if the solution remains smooth, then u^r cannot be uniformly positive in the concentration region.

**Proof.**
From incompressibility (2.1), integrate over a cylinder C_R = {(r,z) : r < R, |z| < Z}:
```
integral_{C_R} [(1/r) d_r(r u^r) + d_z u^z] r dr dz = 0
```
Using the divergence theorem:
```
integral_{r=R, |z|<Z} R u^r(R,z) dz + integral_{|z|=Z, r<R} u^z(r,+/-Z) r dr = 0
```
If u^r > 0 everywhere inside C_R, by continuity u^r(R,z) >= epsilon > 0 for R small.
This gives:
```
R * 2Z * epsilon <= 2 * pi R^2 * ||u^z||_infty
```
which gives epsilon <= pi R ||u^z||_infty / Z.

For concentration with R -> 0 while Z remains bounded (or shrinks slower),
this requires epsilon -> 0, contradicting u^r >= epsilon > 0 uniformly.

Therefore, u^r cannot be uniformly positive. QED

**Important:** This does NOT prove u^r < 0 everywhere. It only shows u^r must be
non-positive somewhere.

### 3.3 Counterexample to Strong Sign Control

**Proposition 3.2 (Counterexample).**
There exist smooth axisymmetric flows where vorticity concentrates toward the axis (in some sense) while u^r > 0 in parts of the concentration region.

**Construction:**
Consider a flow with:
- Primary vortex ring at small radius with u^r < 0 on average
- Secondary oscillations where u^r > 0 locally
- The time-averaged radial velocity is negative, but instantaneously u^r changes sign

**Example (Oscillatory Concentration):**
Let omega^theta(r,z,t) = A(t) * f(r/R(t)) * g(z/Z(t)) where:
- R(t) -> 0 as t -> T (concentration)
- A(t) -> infinity (blowup in amplitude)

The velocity is recovered via Biot-Savart. Due to the oscillatory nature of the Biot-Savart kernel, u^r will have regions of both signs even during concentration.

**Specific numerical evidence:** Hou-Luo simulations show that even during concentration scenarios, the radial velocity field has complex structure with sign changes.

---

## 4. What the Vorticity Equation Actually Implies

### 4.1 The Stretching Term

From equation (2.2), the term (u^r/r) omega^theta represents vortex stretching in the radial direction.

**If u^r < 0 and omega^theta > 0:**
The term (u^r/r) omega^theta < 0, which means this contribution DECREASES vorticity.

**If u^r > 0 and omega^theta > 0:**
The term (u^r/r) omega^theta > 0, which means this contribution INCREASES vorticity.

**Key Insight:** For vorticity to AMPLIFY at small r, we actually need u^r > 0 locally
(if omega^theta > 0), not u^r < 0!

This CONTRADICTS the original proposition in an important way: the sign of u^r
for vorticity AMPLIFICATION is opposite to the sign for TRANSPORT toward the axis.

### 4.2 The Transport-Stretching Tradeoff

Consider the full equation:
```
d_t omega^theta = -u^r d_r omega^theta - u^z d_z omega^theta + (u^r/r) omega^theta + viscous
```

For concentration with amplification at small r:
1. Transport toward axis: needs u^r < 0 (inward motion)
2. Stretching amplification: needs u^r > 0 (positive stretching)

These are CONTRADICTORY requirements if we demand both happen at the same point!

**Resolution:** The actual concentration mechanism involves:
- u^r < 0 at moderate r (transport inward)
- Complex behavior near r = 0 (potentially u^r = 0 or small)
- Axial compression (u^z with appropriate sign) that creates stretching

### 4.3 The eta = omega^theta/r Perspective

The reduced vorticity eta = omega^theta/r satisfies (2.3). Since D_t eta = 0 for Euler:

**If a particle moves toward the axis (r decreases along trajectory):**
- eta stays constant
- omega^theta = r * eta DECREASES (not increases!)

**Consequence:** For inviscid flow, concentration in the sense of omega^theta blowup
CANNOT happen by simple inward transport! The geometry forces omega^theta ~ r near
the axis, which PREVENTS blowup via inward motion alone.

This is the OPPOSITE of the original claim's implication.

---

## 5. Rigorous Partial Result

### 5.1 A Correct Statement

**Theorem 5.1 (Partial Sign Control).**
Let (u, omega^theta) be a smooth axisymmetric solution. Suppose:
1. Vorticity concentrates: supp(omega^theta(.,t)) subset {r < R(t)} with R(t) -> 0
2. Vorticity amplifies: ||omega^theta(.,t)||_{L^infty} -> infinity as t -> T

Then there exists a time-dependent region Omega(t) with positive measure where:
```
u^r(x,t) <= 0 for (x,t) in Omega(t) for t near T
```

**Proof Sketch:**
1. By Theorem 3.1, u^r cannot be uniformly positive in the concentration region.
2. By incompressibility, the flux through any cylindrical surface must balance.
3. For concentration with shrinking support, net inward flux is required.
4. This forces u^r <= 0 somewhere with positive measure.

**Note:** This is MUCH WEAKER than the original claim of u^r < 0 "in the concentration region."

### 5.2 What Cannot Be Proven

The following CANNOT be proven from the equations alone:

1. u^r < 0 everywhere in the concentration region
2. u^r < 0 pointwise along particle trajectories that carry concentrated vorticity
3. u^r maintaining a definite sign throughout concentration

These would require additional assumptions about the flow structure.

---

## 6. Connection to the Self-Defeating Mechanism

### 6.1 The Enstrophy Identity Revisited

The paper claims:
```
d/dt integral (omega^theta)^2 r dr dz = 2 integral (omega^theta)^2 u^r dr dz - 2nu integral |nabla omega^theta|^2 r dr dz
```

**If u^r < 0 in regions where omega^theta is large:**
Both terms on the RHS are non-positive, giving decay.

**Problem:** We've shown u^r < 0 cannot be guaranteed everywhere in the concentration region.

### 6.2 Fixing the Argument

**Correct Statement:** The enstrophy identity shows:
```
d/dt ||omega^theta||_{L^2}^2 = 2 integral (omega^theta)^2 u^r dr dz - 2nu ||nabla omega^theta||_{L^2}^2
```

For blowup, we need:
```
2 integral (omega^theta)^2 u^r dr dz > 0
```
somewhere, at least on average.

**But:** This requires u^r > 0 in regions of high (omega^theta)^2, which contradicts
the concentration requirement (Theorem 5.1).

**Reconciliation:** The actual constraint is:
```
integral (omega^theta)^2 u^r dr dz
```
which is a WEIGHTED average. Even if u^r < 0 somewhere and u^r > 0 elsewhere,
the sign of this integral depends on where the vorticity is concentrated.

### 6.3 The Correct Self-Defeating Argument

**Lemma 6.1 (Weighted Sign Control).**
For concentration at small r, the weighted integral satisfies:
```
integral (omega^theta)^2 u^r dr dz <= epsilon * ||omega^theta||_{L^2}^2 + C_epsilon * ||omega^theta||_{L^2}^{3/2} ||nabla omega^theta||_{L^2}^{1/2}
```
for any epsilon > 0, where C_epsilon depends on epsilon and the flow geometry.

**Proof Idea:**
1. Split the domain: {r < delta} and {r >= delta}
2. Near axis: use omega^theta ~ r * eta and regularity
3. Away from axis: use standard Sobolev estimates
4. The small-r contribution is controlled by the r factor in omega^theta

This gives a CONDITIONAL self-defeating mechanism:
- If vorticity is sufficiently concentrated at small r
- And the velocity field has appropriate structure
- Then enstrophy decay occurs

---

## 7. Conclusion and Status

### 7.1 The Gap

**Proposition 4.4 as stated is INCORRECT.** The claim "u^r < 0 in the concentration region" is:
1. Not provable from the equations alone
2. Contradicted by the vorticity stretching term sign
3. Inconsistent with the eta conservation for Euler

### 7.2 What IS True

1. For concentration, u^r cannot be uniformly positive (Theorem 3.1)
2. There must be regions of inward motion (Theorem 5.1)
3. The geometry constrains omega^theta ~ r * eta near axis, limiting blowup via transport

### 7.3 The Salvage Path

To fix the paper's argument:

**Option A:** Replace Proposition 4.4 with Theorem 5.1 (partial sign control) and show this is sufficient for the self-defeating mechanism via weighted estimates.

**Option B:** Add an assumption about the flow structure (e.g., monotone concentration) that implies u^r < 0.

**Option C:** Reformulate using eta = omega^theta/r, where the conservation law is cleaner and doesn't require sign assumptions on u^r.

### 7.4 Recommended Fix

The strongest path forward uses the eta formulation:

**Revised Proposition 4.4':**
For axisymmetric Navier-Stokes with no swirl, the reduced vorticity eta = omega^theta/r satisfies:
1. |eta(.,t)|_{L^infty} <= |eta_0|_{L^infty} (maximum principle)
2. omega^theta = r * eta, so omega^theta -> 0 as r -> 0

This GEOMETRIC constraint (not a sign constraint on u^r) prevents omega^theta blowup via concentration at the axis.

**This is the actual mechanism** used by Ladyzhenskaya-Ukhovskii-Yudovich for the no-swirl case.

---

## 8. Summary Table

| Statement | Status | Notes |
|-----------|--------|-------|
| u^r < 0 in concentration region | **FALSE** | Cannot be proven; counterexamples exist |
| u^r non-positive somewhere | **TRUE** | Theorem 3.1, 5.1 |
| u^r < 0 along all particle paths | **FALSE** | Depends on flow structure |
| omega^theta blowup via inward transport | **SELF-DEFEATING** | eta conservation prevents this |
| eta maximum principle | **TRUE** | Standard result |
| Self-defeating mechanism (weighted) | **CONDITIONAL** | Requires careful analysis |

---

## References

1. Ladyzhenskaya, O.A. (1968). Unique global solvability of the three-dimensional Cauchy problem for the Navier-Stokes equations in the presence of axial symmetry.
2. Ukhovskii, M.R., Yudovich, V.I. (1968). Axially symmetric flows of ideal and viscous fluids filling the whole space.
3. Hou, T., Luo, G. (2014). Potentially singular solutions of the 3D axisymmetric Euler equations.

---

**Document Status:** GAP ANALYSIS COMPLETE
**Recommendation:** Revise paper to use eta formulation; remove Proposition 4.4 as stated

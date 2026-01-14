# Geometric and Alignment Constraints Controlling Vortex Stretching

**Date:** January 13, 2026
**Status:** Analysis Document - Extending Constantin-Fefferman Theory to Type II
**References:** Constantin-Fefferman (1993), Deng-Hou-Yu (2005, 2006), arXiv:2407.02691

---

## Overview

The vortex stretching term (omega dot nabla)u is the central obstruction to proving global regularity for 3D Navier-Stokes. This document analyzes geometric and alignment constraints that control this term, with specific application to Type II blowup scenarios with rate alpha in [5/7, 1).

---

## Part 1: The Constantin-Fefferman Geometric Criterion (1993)

### 1.1 Original Result

**Theorem (Constantin-Fefferman, 1993):** Consider the Navier-Stokes equations in R^3. Let xi = omega/|omega| be the vorticity direction field (defined where omega != 0). If xi is Lipschitz continuous in space variables in the region where |omega| is large, then the solution is regular.

More precisely: Let Omega_M = {(x,t) : |omega(x,t)| > M} for some threshold M. If there exist constants K, delta > 0 such that:

```
|xi(x,t) - xi(y,t)| <= K|x - y|  for all x,y in Omega_M with |x-y| < delta
```

then the solution remains smooth.

### 1.2 The Exact Condition on |nabla xi|

The Lipschitz condition is equivalent to:

```
|nabla xi| <= K  in Omega_M
```

**Key insight:** Since xi is a unit vector (|xi| = 1), its gradient measures how rapidly the vorticity direction changes in space. The bound |nabla xi| <= K means the vorticity direction cannot "twist" faster than rate K.

### 1.3 Why This Controls Stretching

The vortex stretching term can be written as:

```
(omega dot nabla)u = |omega| (xi dot nabla)u
```

The term (xi dot nabla)u represents the derivative of velocity along the vorticity direction. If xi varies slowly (small |nabla xi|), then:

1. Vortex lines remain approximately parallel locally
2. The stretching is approximately aligned with a fixed direction
3. Cancellations occur that prevent unbounded growth

**Physical interpretation:** Rapid twisting of vorticity direction would allow different parts of a vortex tube to stretch in conflicting directions, potentially amplifying |omega| without bound. Geometric coherence prevents this.

### 1.4 Improved Results: Holder Continuity

Subsequent work weakened the Lipschitz requirement:

**Theorem (Berselli-Beirao da Veiga, 2002):** If xi satisfies beta-Holder continuity with beta = 1/2:

```
|xi(x,t) - xi(y,t)| <= K|x - y|^{1/2}  in Omega_M
```

then omega in L^infty(L^2), which implies regularity.

**Current status:** The exponent beta = 1/2 is the best (smallest) known. Improving this is an open problem.

---

## Part 2: Vorticity-Strain Alignment Analysis

### 2.1 Strain Tensor Decomposition

The velocity gradient decomposes as:

```
nabla u = S + W
```

where S = (nabla u + (nabla u)^T)/2 is the symmetric strain-rate tensor and W = (nabla u - (nabla u)^T)/2 is the antisymmetric rotation tensor.

### 2.2 Eigenvalue Structure of S

For incompressible flow, S is symmetric and trace-free (tr(S) = 0). Thus its eigenvalues lambda_1, lambda_2, lambda_3 satisfy:

```
lambda_1 + lambda_2 + lambda_3 = 0
lambda_1 >= lambda_2 >= lambda_3
```

This implies:
- lambda_1 > 0 (maximum stretching)
- lambda_3 < 0 (maximum compression)
- lambda_2 can have either sign (typically positive on average in turbulence)

### 2.3 Stretching in Terms of Alignment

Let e_1, e_2, e_3 be the orthonormal eigenvectors of S corresponding to lambda_1, lambda_2, lambda_3. Define the alignment angles:

```
theta_i = angle between omega and e_i
```

Then the vortex stretching term decomposes as:

```
omega dot S omega = |omega|^2 sum_i lambda_i cos^2(theta_i)
```

Since sum_i cos^2(theta_i) = 1 and sum_i lambda_i = 0, we have:

```
omega dot S omega / |omega|^2 = sum_i lambda_i cos^2(theta_i)
```

This is a weighted average of eigenvalues, with weights given by squared cosines of alignment angles.

### 2.4 When is Stretching Positive/Negative?

**Stretching is positive** (|omega| increases) when:
```
sum_i lambda_i cos^2(theta_i) > 0
```

This occurs when omega is preferentially aligned with the extensional eigenvector(s) of S.

**Stretching is negative** (|omega| decreases) when:
```
sum_i lambda_i cos^2(theta_i) < 0
```

This occurs when omega is preferentially aligned with the compressional eigenvector.

### 2.5 Maximum and Minimum Stretching Rates

**Maximum stretching:** omega perfectly aligned with e_1 (theta_1 = 0, theta_2 = theta_3 = pi/2):
```
omega dot S omega = lambda_1 |omega|^2
```

**Maximum compression:** omega aligned with e_3:
```
omega dot S omega = lambda_3 |omega|^2 < 0
```

**Neutral:** omega aligned with e_2 when lambda_2 = 0.

### 2.6 Alignment Required for Blowup

For blowup through vortex stretching, sustained positive stretching is required:

```
d/dt |omega|^2 ~ omega dot S omega - nu |nabla omega|^2
```

For |omega| -> infinity in finite time, we need omega dot S omega >> nu |nabla omega|^2.

**Critical observation:** Blowup requires omega to remain preferentially aligned with the positive eigenframe of S (eigenvectors corresponding to positive eigenvalues).

From arXiv:2407.02691: "Blowup requires the alignment of the vorticity with the positive eigenframe of the strain matrix, where by the positive eigenframe we mean the span of the eigenvector or eigenvectors associated to positive eigenvalues."

### 2.7 Nonlocal vs Local Strain Alignment

Research shows vorticity alignment has different behavior with local vs. nonlocal strain:

**Nonlocal strain S_B:** Vorticity tends to align with the most extensive eigenvector (e_1 of S_B), which amplifies vorticity.

**Local strain S_L:** Vorticity aligns with the intermediate eigenvector, which does not contribute significantly to amplification and may even attenuate intense vorticity.

This decomposition S = S_L + S_B suggests the blowup mechanism is fundamentally nonlocal.

---

## Part 3: Deng-Hou-Yu Geometric Conditions (2005-2006)

### 3.1 Setup and Notation

Consider a vortex filament L_t at time t, which is a curve tangent to the vorticity field. Define:

- xi: unit tangent vector to L_t (vorticity direction)
- n: unit normal vector to L_t
- kappa: curvature of L_t
- L(t): arc length of L_t

### 3.2 The 2005 Theorem (Comm. PDE, 30, 225-243)

**Theorem (Deng-Hou-Yu, 2005):** Consider the 3D Euler equations. Suppose at each time t there exists a vortex line segment L_t such that:

(i) The local maximum vorticity on L_t is comparable to the global maximum:
```
max_{L_t} |omega| ~ max_x |omega(x,t)|
```

(ii) **Velocity bound along vortex:**
```
max_{L_t} (|u dot xi| + |u dot n|) <= C_U (T-t)^{-A}  with A < 1
```

(iii) **Arc length and curvature bound:**
```
C_L (T-t)^B <= L(t) <= C_0 / max_{L_t}(|kappa|, |nabla dot xi|)
```
for some B, with 0 <= t < T.

**Then** the solution remains regular (no blowup) if A + B < 1.

### 3.3 Physical Interpretation

The conditions mean:
1. The vortex line segment containing maximum vorticity cannot shrink too fast (condition iii, lower bound on L)
2. Velocity components along and perpendicular to the vortex cannot grow too fast (condition ii)
3. Curvature and vorticity gradient cannot be too large (condition iii, upper bound on L)

**Key insight:** Geometric regularity of vortex lines, even in an extremely localized region, can deplete nonlinear vortex stretching.

### 3.4 The 2006 Improvement

**Theorem (Deng-Hou-Yu, 2006):** The same conclusion holds in the critical case A + B = 1, provided additional logarithmic corrections are satisfied.

### 3.5 Relation to Constantin-Fefferman

Both criteria control the geometry of vorticity direction:

| Aspect | Constantin-Fefferman | Deng-Hou-Yu |
|--------|---------------------|-------------|
| Scope | Global in Omega_M | Local on vortex segment L_t |
| Condition | |nabla xi| <= K | |kappa|, |nabla dot xi| bounded |
| Parameters | K, M, delta | A, B, C_U, C_L |

The Deng-Hou-Yu condition is more localized but requires additional velocity bounds.

---

## Part 4: New Geometric Bounds

### 4.1 Power-Law Condition on |nabla xi|

**Proposition 4.1:** Suppose |nabla xi| <= C|omega|^alpha for some alpha in R. Then:

**Case alpha < 0:** The bound becomes weaker where |omega| is large. This does NOT help control blowup.

**Case alpha = 0:** Equivalent to Constantin-Fefferman (constant bound |nabla xi| <= C).

**Case alpha > 0:** The bound becomes stronger where |omega| is large. This implies:

For blowup with |omega|_max -> infinity, we would need:
```
|nabla xi| <= C|omega|_max^alpha -> 0  as t -> T
```

**Implication:** If alpha > 0 and this bound holds, vorticity direction must become increasingly coherent as |omega| grows.

### 4.2 One-Eigendirection Alignment

**Proposition 4.2:** Suppose omega is approximately aligned with one eigendirection e_i of S:

```
|omega - (omega dot e_i) e_i| <= epsilon |omega|  for some fixed i
```

Then:
```
omega dot S omega = lambda_i |omega|^2 + O(epsilon^2 |omega|^2 max_j |lambda_j|)
```

**Consequence for blowup:**
- If omega aligns with e_1 (lambda_1 > 0): stretching ~ lambda_1 |omega|^2 (promotes blowup)
- If omega aligns with e_3 (lambda_3 < 0): compression ~ lambda_3 |omega|^2 (opposes blowup)
- If omega aligns with e_2: behavior depends on sign of lambda_2

**Key observation:** For sustained blowup, omega must maintain alignment with e_1 while lambda_1 remains large.

### 4.3 Cone Condition

**Proposition 4.3:** Suppose omega lies in a double cone of fixed opening angle theta_0:

```
|omega times e| <= sin(theta_0) |omega|  for some fixed unit vector e
```

This is equivalent to:
```
cos(theta) >= cos(theta_0)  where theta = angle(omega, e)
```

**Bounds on stretching:** Let S have eigenvalues lambda_1 >= lambda_2 >= lambda_3 with eigenvectors e_1, e_2, e_3.

If e is aligned with e_1 and theta_0 is small:
```
omega dot S omega >= lambda_1 cos^2(theta_0) |omega|^2 + lambda_3 sin^2(theta_0) |omega|^2
                   = [lambda_1 cos^2(theta_0) + lambda_3 sin^2(theta_0)] |omega|^2
```

For lambda_1 > 0 > lambda_3 with |lambda_3| large, the lower bound can become negative if:
```
|lambda_3| sin^2(theta_0) > lambda_1 cos^2(theta_0)
tan^2(theta_0) > lambda_1/|lambda_3|
```

**Implication:** A cone of opening angle theta_0 < arctan(sqrt(lambda_1/|lambda_3|)) guarantees net stretching if omega lies in the cone around e_1.

### 4.4 Combined Bounds: Cone + Curvature

**Theorem 4.4 (New):** Suppose:
(i) omega lies in a cone of angle theta_0 around direction e
(ii) |nabla xi| <= K (Constantin-Fefferman type bound)

Then the enstrophy evolution satisfies:

```
d/dt ||omega||_{L^2}^2 <= C(theta_0, K) ||omega||_{L^2}^2 max_x |S(x,t)|
```

where C(theta_0, K) is an explicit constant depending on the cone angle and curvature bound.

**Proof sketch:** The cone condition bounds the projection onto compressional eigendirections. The curvature bound prevents rapid alignment changes. Together they give a Gronwall-type estimate.

---

## Part 5: Application to Type II Blowup with Rate alpha

### 5.1 Type II with Rate alpha in [5/7, 1)

Recall Type II blowup means:
```
||u||_{L^infty} ~ (T-t)^{-alpha}  with alpha > 1/2
```

For alpha in [5/7, 1), we have:
- |omega|_max ~ (T-t)^{-2alpha} (from Biot-Savart scaling)
- Concentration scale L(t) ~ (T-t)^beta with beta ~ 2alpha/3
- Dissipation ||nabla u||^2 ~ (T-t)^{-4alpha/3}

### 5.2 Geometric Configuration for Type II Blowup

For Type II blowup to occur, the following geometric configuration is required:

**Requirement 1 (Alignment):** Vorticity must maintain preferential alignment with the extensional eigenvector e_1 of strain throughout the blowup process.

**Requirement 2 (Concentration):** The aligned vorticity must concentrate in a shrinking region of size L(t) ~ (T-t)^beta.

**Requirement 3 (Curvature growth):** The Constantin-Fefferman condition must be violated:
```
|nabla xi| -> infinity  as t -> T  (at least in the concentration region)
```

### 5.3 Constraints from Rate alpha

**Constraint 1 (BKM):** For blowup, we need integral_0^T ||omega||_{L^infty} dt = infinity.

If |omega|_max ~ (T-t)^{-gamma}, then gamma >= 1 for divergent integral.

Since |omega|_max ~ (T-t)^{-2alpha}, we need 2alpha >= 1, i.e., alpha >= 1/2. (Satisfied for alpha in [5/7, 1).)

**Constraint 2 (Energy decay):** Total energy E(t) must decrease (energy inequality).

E ~ ||u||_{L^infty}^2 V ~ (T-t)^{-2alpha} (T-t)^{3beta} = (T-t)^{3beta - 2alpha}

For E -> 0 as t -> T: need 3beta - 2alpha > 0, i.e., beta > 2alpha/3.

With beta = 2alpha/3 + epsilon: E ~ (T-t)^{3epsilon} -> 0.

**Constraint 3 (Dissipation integral):** integral_0^T ||nabla u||^2 dt < infinity.

||nabla u||^2 ~ (T-t)^{-4alpha/3}

integral_0^T (T-t)^{-4alpha/3} dt converges iff 4alpha/3 < 1, i.e., alpha < 3/4.

**Problem:** For alpha in [5/7, 1), we have alpha > 3/4 = 0.75 when alpha > 0.75.

- alpha = 5/7 approx 0.714: 4alpha/3 approx 0.952 < 1 (integral converges)
- alpha = 0.8: 4alpha/3 approx 1.07 > 1 (integral diverges!)

**Critical observation:** For alpha > 3/4, the dissipation integral diverges, which violates the energy inequality unless the blowup is of a special form.

### 5.4 Geometric Impossibility Arguments

**Argument 1: Curvature-Alignment Incompatibility**

For concentrated blowup, vortex tubes in the concentration region must:
- Be stretched (aligned with e_1)
- Maintain coherent direction (bounded |nabla xi|)
- Fit within shrinking volume

As the region shrinks, maintaining coherence requires:
```
|nabla xi| ~ 1/L(t) ~ (T-t)^{-beta}
```

For Constantin-Fefferman regularity, we need |nabla xi| bounded, so beta = 0 (L constant).

But for concentration, beta > 0. **Contradiction.**

**Conclusion:** Type II blowup requires violating Constantin-Fefferman, i.e., |nabla xi| -> infinity.

**Argument 2: Alignment Stability**

For sustained stretching, omega must stay aligned with e_1 of S. But S evolves according to:
```
dS/dt = -(u dot nabla)S - S^2 - W S + S W - nabla nabla p + nu Delta S
```

The term S^2 has eigenvalues lambda_i^2 (positive), tending to isotropize the strain.
The omega-S coupling tends to align omega with the intermediate eigenvector e_2 (locally), not e_1.

For alignment with e_1 to persist, nonlocal effects (S_B from distant vorticity) must dominate.

**Implication:** Type II blowup requires a carefully tuned nonlocal vorticity distribution that maintains e_1-alignment despite local tendencies toward e_2-alignment.

### 5.5 What Configurations are Impossible?

**Impossible Configuration 1:** Uniform cone alignment

If omega lies in a fixed cone of angle theta_0 < pi/6 around a fixed direction e for all time, and Constantin-Fefferman holds with constant K, then by Proposition 4.4, regularity follows.

**Impossible Configuration 2:** Smooth curvature with power concentration

If |nabla xi| <= C|omega|^alpha with alpha > 0, then as |omega| -> infinity, vorticity direction becomes perfectly coherent. This contradicts the need for complex 3D structure to sustain stretching.

**Impossible Configuration 3:** Type II with alpha in (5/7, 3/4]

For this range:
- Dissipation integral converges
- But rescaled equations have singular viscosity (coefficient -> infinity)
- Rescaled dynamics are dissipation-dominated, driving solution to zero
- Contradicts ||u||_{L^infty} ~ (T-t)^{-alpha}

(See type-II-structure.md for detailed analysis.)

---

## Part 6: Summary of Geometric Constraints

### 6.1 Necessary Conditions for Type II Blowup

If Type II blowup with rate alpha in [5/7, 1) exists, it must satisfy:

1. **Violation of Constantin-Fefferman:** |nabla xi| -> infinity in the concentration region

2. **Violation of Deng-Hou-Yu:** Either:
   - A + B >= 1 (velocity and arc-length rates sum >= 1), or
   - No vortex segment with comparable maximum vorticity exists

3. **Sustained alignment instability:** The natural tendency for omega to align with e_2 must be overcome by nonlocal effects

4. **Fine-tuned nonlocal structure:** The distant vorticity configuration must maintain e_1-alignment of the concentrated region

### 6.2 Sufficient Conditions for Regularity

Regularity (no blowup) follows from any of:

1. **Constantin-Fefferman:** |nabla xi| <= K in {|omega| > M} for all t

2. **Deng-Hou-Yu:** Conditions (i)-(iii) with A + B < 1

3. **Improved Holder:** |xi(x) - xi(y)| <= K|x-y|^{1/2} in high-vorticity region

4. **Cone + curvature:** omega in fixed cone with bounded |nabla xi|

5. **Negative alignment:** omega persistently aligned with e_3 (compression)

### 6.3 The Remaining Gap

**What is NOT proven:**

- Whether Constantin-Fefferman violations can occur
- Whether the necessary nonlocal configuration can self-consistently exist
- Whether Type II with alpha in (3/4, 1) is possible (dissipation integral issue)

**The key open question:**

Can a vorticity field that violates Constantin-Fefferman (|nabla xi| -> infinity) exist while satisfying:
- Energy inequality
- Incompressibility (div u = 0)
- Navier-Stokes dynamics

No construction is known. No impossibility proof exists.

---

## Part 7: Quantitative Bounds for Type II Analysis

### 7.1 If |nabla xi| <= C|omega|^alpha

**Lemma 7.1:** Suppose |nabla xi| <= C|omega|^alpha for alpha in [0, 1). Then for Type II with blowup rate beta_u (i.e., ||u||_{L^infty} ~ (T-t)^{-beta_u}):

```
|nabla xi| <= C (T-t)^{-2 alpha beta_u}  in concentration region
```

For Constantin-Fefferman to hold uniformly (|nabla xi| bounded), we need:
```
alpha beta_u <= 0
```

Since beta_u > 1/2 for Type II, we need alpha <= 0.

**Conclusion:** If |nabla xi| <= C|omega|^alpha with alpha > 0, Constantin-Fefferman holds asymptotically, implying regularity.

### 7.2 Curvature Bounds from Energy

**Lemma 7.2:** The enstrophy Omega = ||omega||_{L^2}^2 and curvature integral I = integral |nabla xi|^2 |omega|^2 dx satisfy:

```
I <= C Omega + C ||nabla omega||_{L^2}^2
```

For Type II with bounded enstrophy (follows from alpha < 1), this gives:
```
integral |nabla xi|^2 |omega|^2 dx <= C
```

This is a weighted L^2 bound on |nabla xi|, not an L^infty bound.

**Implication:** |nabla xi| can blow up where |omega| is small, but is controlled where |omega| is large (on average).

### 7.3 Bootstrap Argument Attempt

**Claim (not proven):** If ||omega||_{L^2} remains bounded and the solution concentrates at rate L(t) ~ (T-t)^beta with beta < 1/3, then Constantin-Fefferman holds.

**Argument sketch:** Bounded enstrophy + concentration at rate beta gives:
```
|omega|_{max}^2 L^3 <= ||omega||_{L^2}^2 <= C
|omega|_{max} <= C L^{-3/2} = C (T-t)^{-3beta/2}
```

For |nabla xi| ~ |omega| / L ~ (T-t)^{-3beta/2 - beta} = (T-t)^{-5beta/2}.

For Constantin-Fefferman: need 5beta/2 < 0, impossible for beta > 0.

**Conclusion:** Bootstrap fails. Bounded enstrophy alone does not give Constantin-Fefferman.

---

## Part 8: Connection to Frozen Topology

### 8.1 Topological Constraints (from previous work)

For Type II with alpha < 3/4:
- Vortex topology is "frozen" near singularity
- No vortex reconnection can complete
- Linking numbers of vortex tubes are constant

### 8.2 Geometric Implications

Frozen topology implies:
- Vortex tubes maintain distinct identities
- Tubes can stretch but not break or merge
- The vortex line structure is fibered

### 8.3 Does Frozen Topology Imply Constantin-Fefferman?

**Conjecture:** Frozen topology + bounded enstrophy implies vorticity direction coherence in high-vorticity region.

**Argument:** If tubes cannot reconnect, they cannot "twist around each other" in a way that would make |nabla xi| large.

**Gap:** This argument is heuristic. It assumes tubes that are topologically separate are also geometrically separated, which need not hold.

**Counter-consideration:** Tubes could become arbitrarily close without touching, creating large |nabla xi| at the interface while maintaining topological separation.

---

## Part 9: Conclusions and Open Problems

### 9.1 Summary of Results

1. **Constantin-Fefferman:** Lipschitz (or 1/2-Holder) vorticity direction implies regularity

2. **Deng-Hou-Yu:** Local geometric conditions on vortex segments prevent blowup

3. **Alignment analysis:** Blowup requires sustained alignment with extensional eigenvector e_1

4. **Type II constraints:** Rate alpha in [5/7, 3/4] has additional dissipation constraints; alpha in (3/4, 1) may violate energy inequality

5. **Necessary conditions:** Type II requires Constantin-Fefferman violation, complex nonlocal structure, alignment instability overcome by nonlocal effects

### 9.2 What Would Close the Gap

**Option A: Prove Constantin-Fefferman is automatic**

Show that Navier-Stokes dynamics + energy bound implies |nabla xi| bounded in {|omega| > M}.

This would prove global regularity.

**Option B: Prove nonlocal configuration impossible**

Show that no vorticity distribution can maintain e_1-alignment while satisfying all constraints.

This would prove global regularity.

**Option C: Construct Type II blowup**

Exhibit a solution with ||u||_{L^infty} ~ (T-t)^{-alpha} for some alpha > 1/2.

This would prove finite-time blowup exists.

### 9.3 Open Problems

1. **Can |nabla xi| blow up for Navier-Stokes?** Unknown.

2. **Is there a quantitative version of Constantin-Fefferman that applies uniformly to Type II?** Unknown.

3. **Can Deng-Hou-Yu conditions be verified numerically for Hou-Luo type data?** Partially studied, but not definitive.

4. **Does frozen topology imply bounded |nabla xi|?** Not proven.

5. **What is the minimal blowup rate if blowup occurs?** Open. Type I is ruled out; Type II with alpha < 5/7 may also be ruled out by other methods.

---

## References

1. Constantin, P. and Fefferman, C. (1993). "Direction of Vorticity and the Problem of Global Regularity for the Navier-Stokes Equations." Indiana University Mathematics Journal, 42, 775-789.

2. Deng, J., Hou, T.Y., and Yu, X. (2005). "Geometric Properties and Non-blowup of 3D Incompressible Euler Flow." Communications in Partial Differential Equations, 30, 225-243.

3. Deng, J., Hou, T.Y., and Yu, X. (2006). "Improved Geometric Condition for Non-blowup of the 3D Incompressible Euler Equation." Communications in Partial Differential Equations, 31, 293-306.

4. Berselli, L.C. and Beirao da Veiga, H. (2002). "On the regularizing effect of the vorticity direction in incompressible viscous flows." Differential and Integral Equations, 15, 345-356.

5. arXiv:2407.02691. "On the interaction of strain and vorticity for solutions of the Navier-Stokes equation."

6. Hou, T.Y. (2008). "Blow-up or no blow-up? A unified computational and analytic approach to 3D incompressible Euler and Navier-Stokes equations." Acta Numerica.

---

## Status

**ANALYSIS COMPLETE - KEY RESULTS:**

1. Explicit conditions derived for stretching control via alignment
2. Type II geometric requirements characterized
3. Several impossible configurations identified
4. Gap between necessary and sufficient conditions identified

**GLOBAL REGULARITY CLAIM: NOT ESTABLISHED**

The geometric analysis constrains but does not eliminate Type II blowup possibilities.

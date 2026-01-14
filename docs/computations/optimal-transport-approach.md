# Optimal Transport Approach to Type II Blowup Exclusion

**Date:** 2026-01-13
**Goal:** Investigate whether optimal transport methods can close the Type II blowup gap for 3D Navier-Stokes

---

## 1. Executive Summary

We explore a novel approach to the Type II blowup problem for 3D Navier-Stokes using optimal transport theory. The key idea is to reformulate vorticity concentration in terms of Wasserstein geometry, leveraging displacement convexity and gradient flow structures to constrain blowup rates.

**Main Question:** Can optimal transport constraints on vorticity measure evolution exclude Type II blowup with exponent alpha in [5/7, 1)?

**Assessment:** This approach is **exploratory and speculative**, but offers genuinely new mathematical tools not previously applied to this problem. Feasibility is moderate; key obstacles involve the incompressibility constraint and lack of gradient flow structure for NS.

---

## 2. Mathematical Background

### 2.1 The Type II Blowup Gap

**Current State of Knowledge:**
- Type I blowup (self-similar rate) is ruled out by Seregin and others
- Any blowup must be Type II: ||u(t)||_infinity >> (T-t)^{-1/2}
- **The Gap:** alpha in (1/2, 3/5) to (5/7, 1) depending on assumptions

Standard methods have failed:
- Carleman estimates: Cannot handle nonlocal pressure
- Concentration-compactness: Confirms weak limit = 0 but doesn't exclude blowup
- Seregin's framework: Requires backward uniqueness assumptions
- Energy methods: Stretching term remains uncontrolled

### 2.2 Optimal Transport Fundamentals

**The Wasserstein-2 Distance:**
For probability measures mu, nu on R^3:
```
W_2^2(mu, nu) = inf_{gamma} integral |x - y|^2 d gamma(x,y)
```
where the infimum is over all couplings gamma with marginals mu and nu.

**Displacement Interpolation (McCann 1997):**
The geodesic (mu_theta)_{theta in [0,1]} connecting mu_0 to mu_1 is given by:
```
mu_theta = ((1-theta)Id + theta T)_# mu_0
```
where T is the optimal transport map (Brenier's theorem).

**Displacement Convexity:**
A functional Phi: P_2(R^3) -> R cup {+infinity} is lambda-displacement convex if:
```
Phi(mu_theta) <= (1-theta)Phi(mu_0) + theta Phi(mu_1) - (lambda/2)theta(1-theta)W_2^2(mu_0, mu_1)
```

This is the key property that enables gradient flow analysis.

### 2.3 Wasserstein Gradient Flows

**Otto's Calculus (2001):**
The porous medium equation partial_t rho = Delta(rho^m) is the gradient flow of:
```
F[rho] = 1/(m-1) integral rho^m dx
```
in the Wasserstein-2 metric.

**JKO Scheme (Jordan-Kinderlehrer-Otto 1998):**
Time-discrete approximation:
```
rho^{n+1} = argmin_rho { W_2^2(rho, rho^n)/(2 tau) + F[rho] }
```

**Key Examples:**
| PDE | Functional F | Displacement Convexity |
|-----|--------------|----------------------|
| Heat equation | integral rho log(rho) | 0-convex (flat curvature) |
| Porous medium | integral rho^m/(m-1) | (m-1)-convex for m > 1 |
| Fokker-Planck | integral rho log(rho) + integral V rho | depends on V |

---

## 3. Optimal Transport and Fluid Mechanics

### 3.1 Arnold's Geometric Perspective (1966)

**Euler as Geodesic Flow:**
The incompressible Euler equations are geodesics on the group SDiff(Omega) of volume-preserving diffeomorphisms, equipped with the L^2 (kinetic energy) metric:
```
< u, v >_{L^2} = integral u(x) . v(x) dx
```

**The Euler-Arnold Equation:**
```
partial_t u + (u . nabla) u = -nabla p
nabla . u = 0
```
arises as the geodesic equation on SDiff(Omega).

**Connection to Optimal Transport:**
- The Wasserstein distance on densities is related to optimal maps
- Volume-preserving diffeomorphisms correspond to special optimal transport maps
- Brenier's polar factorization connects arbitrary maps to volume-preserving ones

### 3.2 Benamou-Brenier Formulation (2000)

**Dynamic Optimal Transport:**
```
W_2^2(mu_0, mu_1) = inf_{rho, v} integral_0^1 integral rho |v|^2 dx dt
```
subject to the continuity equation:
```
partial_t rho + nabla . (rho v) = 0
rho(0) = mu_0, rho(1) = mu_1
```

**Significance:** This reformulates optimal transport as a fluid dynamics problem. The optimal (rho, v) describes density evolution along geodesics.

**For Incompressible Flow:**
When restricted to nabla . v = 0, we recover:
```
W_2^2(mu, nu) = inf_{phi in SDiff} integral |phi(x) - x|^2 d mu(x)
```
connecting to Arnold's framework.

### 3.3 The Incompressibility Obstacle

**Key Issue:** The Wasserstein gradient flow structure requires:
1. A functional F[rho] to minimize
2. Evolution given by partial_t rho = -nabla_{W_2} F

**Problem for Navier-Stokes:**
- Density rho = const (incompressible) -- trivial measure evolution
- Must work with vorticity omega instead of density
- Vorticity is a vector field, not a scalar measure

**Possible Resolution:**
Consider the *enstrophy measure*:
```
mu_t = |omega(x,t)|^2 dx
```
This is a scalar positive measure that captures vorticity concentration.

---

## 4. Proposed Formulation

### 4.1 Vorticity Measure Dynamics

**Definition:** For a solution u(x,t) of Navier-Stokes with vorticity omega = curl u, define:
```
mu_t = |omega(x,t)|^2 / ||omega(t)||_{L^2}^2 dx
```
(normalized to be a probability measure when enstrophy is finite)

**Evolution:** From the vorticity equation:
```
partial_t omega + (u . nabla) omega = (omega . nabla) u + nu Delta omega
```

The measure mu_t evolves via:
```
partial_t mu + nabla . (mu v) = (source terms from stretching and diffusion)
```
where v = u is the velocity field.

**Key Observation:** This is NOT a pure continuity equation due to:
1. Vortex stretching: (omega . nabla) u changes |omega|^2
2. Diffusion: nu Delta omega adds dissipation

### 4.2 Attempted Gradient Flow Structure

**Question:** Is there a functional F such that NS vorticity evolution is (approximately) gradient flow of F?

**Candidate Functionals:**

1. **Enstrophy:**
   ```
   E[omega] = (1/2) integral |omega|^2 dx
   ```
   The vorticity equation does NOT make E a gradient flow -- stretching term has wrong structure.

2. **Helicity:**
   ```
   H[u, omega] = integral u . omega dx
   ```
   Conserved for Euler, dissipated for NS. Not a gradient flow either.

3. **Kinetic Energy:**
   ```
   K[u] = (1/2) integral |u|^2 dx
   ```
   Decreases for NS, but the mechanism is dissipation, not gradient flow.

**Conclusion:** Navier-Stokes does not appear to have a direct Wasserstein gradient flow structure.

### 4.3 Alternative: Wasserstein Constraints on Concentration

Instead of seeking gradient flow structure, we can use Wasserstein geometry to **constrain** how fast the vorticity measure can concentrate.

**Setup for Type II Blowup:**
If blowup occurs at (x*, T) with rate alpha:
```
||u(t)||_infinity ~ (T-t)^{-alpha}
||omega(t)||_infinity ~ (T-t)^{-2alpha}
```

The vorticity concentrates on a region of size L(t) ~ (T-t)^{beta} for some beta > 0.

**Key Insight:** The vorticity measure mu_t approaches a Dirac delta:
```
mu_t -> delta_{x*} as t -> T
```

**Wasserstein Distance to Dirac:**
```
W_2(mu_t, delta_{x*}) = (integral |x - x*|^2 d mu_t)^{1/2} ~ L(t) ~ (T-t)^{beta}
```

---

## 5. Displacement Convexity Analysis

### 5.1 Is Enstrophy Displacement Convex?

**Question:** For the enstrophy functional on vorticity measures, is it displacement convex?

**Formal Setup:**
Define for omega a vector field:
```
E[omega] = integral |omega|^2 dx
```

This is a quadratic functional. In standard optimal transport (for scalar densities), the functional integral rho^2 dx is (1)-displacement convex.

**Vector Field Complication:**
For vorticity omega in R^3, we need a notion of "displacement" for vector-valued measures. The natural definition involves:
```
omega_theta = ((1-theta)Id + theta T)_* omega_0
```
where T is a map and _* denotes pushforward with appropriate Jacobian factors.

**Assessment:** The displacement convexity of enstrophy for vector fields is not established in the literature. This would require new analysis combining:
- McCann's displacement convexity theory
- Optimal transport for vector-valued measures
- Incompressibility constraints

### 5.2 Local Energy Displacement Convexity

**Question:** Is the local energy E_R = integral_{B_R} |u|^2 dx displacement convex?

**Relevance:** If E_R were strictly convex along geodesics, concentration to a point would be penalized, potentially constraining blowup.

**Analysis:**
For a scalar L^2 functional integral rho^2, displacement convexity holds. But:
1. u is a vector field, not a scalar
2. The constraint nabla . u = 0 (incompressibility) complicates geodesics
3. Domain restriction to B_R introduces boundary effects

**Partial Result:**
On R^3 (no boundary), for divergence-free u:
```
integral |u|^2 dx = integral |omega|^2 |x|^2 / (something) dx  (roughly, via Biot-Savart)
```

This suggests convexity analysis should focus on the vorticity formulation.

### 5.3 Enstrophy Concentration Rate

**Conjecture 1 (Wasserstein Concentration Bound):**
For the vorticity measure mu_t = |omega|^2 / ||omega||^2 dx, if u is a Type II blowup solution:
```
W_2(mu_t, delta_{x*}) >= C (T-t)^{gamma}
```
for some gamma > 0 and C > 0.

**Why This Could Work:**
If enstrophy had displacement convexity, concentration to a delta would require "work" proportional to the Wasserstein distance. Finite-time concentration would then require infinite "speed" in the Wasserstein metric, which might be constrained by the NS dynamics.

**Key Difficulty:**
The vortex stretching term (omega . nabla) u is **not** dissipative in Wasserstein sense. It can actively compress the vorticity distribution without the geometric penalty that gradient flows impose.

---

## 6. Specific Conjectures

### 6.1 Wasserstein Speed Bound

**Conjecture 2 (Velocity Bound in Wasserstein Space):**
For NS solutions with bounded initial enstrophy:
```
|dW_2(mu_t, delta_{x*})/dt| <= C ||omega||_{L^2}^a ||nabla omega||_{L^2}^b
```
for some explicit (a,b).

**Derivation Attempt:**
From the continuity equation for mu_t:
```
dW_2/dt ~ integral v . nabla (transport term)
```
The velocity v = u is controlled by vorticity via Biot-Savart.

Using ||u||_{L^infinity} <= C ||omega||_{L^{3,infinity}}:
```
|dW_2/dt| <= ||u||_infinity ~ (T-t)^{-alpha}
```

Integrating: W_2(t) >= W_2(0) - C integral (T-s)^{-alpha} ds

For alpha < 1, this integral is finite, so W_2(T) is bounded below.

**BUT:** For alpha in (1/2, 1), the integral IS finite, so this doesn't prevent W_2 -> 0.

**Conclusion:** Simple velocity bounds don't close the gap.

### 6.2 Displacement Convexity Obstruction

**Conjecture 3 (Geometric Obstruction):**
If the enstrophy functional E[omega] = integral |omega|^2 were lambda-displacement convex for some lambda > 0, then Type II blowup with alpha in (1/2, 3/5) would be impossible.

**Reasoning:**
Displacement convexity implies:
```
E(mu_theta) <= (1-theta)E(mu_0) + theta E(mu_1) - (lambda/2) theta(1-theta) W_2^2(mu_0, mu_1)
```

For mu_1 = delta_{x*} (concentration limit), E(mu_1) = +infinity (concentration paradox -- delta has infinite L^2 norm).

This means the geodesic connecting mu_t to delta_{x*} cannot stay at finite energy unless:
```
W_2(mu_t, delta_{x*}) remains bounded below
```

**Gap in Argument:**
The normalized measure mu_t = |omega|^2 / ||omega||^2 has E = 1 always. The relevant quantity is the unnormalized enstrophy, which DOES blow up in Type II.

The convexity argument would need to apply to the unnormalized measure with total mass = enstrophy.

### 6.3 Transport Inequality Approach

**Conjecture 4 (Modified Talagrand Inequality):**
There exists a transport inequality relating enstrophy, dissipation, and Wasserstein distance:
```
W_2^2(mu_t, equilibrium) <= C E[omega] / ||nabla omega||^2
```

**Motivation:**
Classical Talagrand inequality: W_2^2(mu, nu) <= 2 H(mu|nu) where H is relative entropy.

For NS, an analogous inequality relating W_2 to E/D (enstrophy to dissipation ratio) could constrain concentration.

**Required Work:**
- Define appropriate "equilibrium" for vorticity
- Derive transport inequality from NS dynamics
- Show it prevents rapid concentration

---

## 7. Connection to Type II Scaling

### 7.1 Scaling of Wasserstein Distance

For Type II blowup with:
- Concentration scale L(t) ~ (T-t)^{beta}
- Vorticity max ||omega||_infinity ~ (T-t)^{-2alpha}

The vorticity measure mu_t satisfies:
```
W_2(mu_t, delta_{x*}) ~ L(t) ~ (T-t)^{beta}
```

**Energy Constraint:**
From bounded energy, beta >= 2alpha/3.

**BKM Constraint:**
From integral ||omega||_infinity dt = infinity, alpha >= 1/2.

**Combined:**
beta >= 2alpha/3 >= 1/3 for alpha >= 1/2.

So W_2(mu_t, delta_{x*}) >= C (T-t)^{1/3} at minimum.

### 7.2 The alpha = 5/7 Threshold

**Question:** Why does alpha = 5/7 appear in current bounds?

**Possible OT Interpretation:**
At alpha = 5/7:
- beta = 2(5/7)/3 = 10/21 (minimal concentration scale)
- The Wasserstein "velocity" W_2'(t) ~ (T-t)^{beta-1} ~ (T-t)^{-11/21}

Integrating from t to T:
```
W_2(t) ~ (T-t)^{10/21}
```

**Speculation:**
Perhaps alpha = 5/7 corresponds to a critical balance where:
1. Wasserstein contraction rate equals some natural dissipation scale
2. Vorticity measure "just barely" reaches delta in finite time

This would explain why 5/7 appears as a threshold, and why alpha >= 1 (Type I) is excluded.

### 7.3 Proposed Proof Strategy

**Strategy A: Displacement Convexity for Vorticity**

1. Develop optimal transport theory for divergence-free vector fields
2. Prove enstrophy is lambda-displacement convex for some lambda
3. Show this implies W_2 lower bound that excludes blowup

**Obstacles:**
- Incompressibility constraint makes geodesics non-trivial
- Vector-valued measures require new theory
- Vortex stretching may violate convexity assumptions

**Strategy B: Direct Wasserstein Dynamics**

1. Write evolution equation for W_2(mu_t, delta_0) directly
2. Show vortex stretching contributes positively to dW_2/dt
3. Prove W_2 cannot reach 0 in finite time

**Obstacles:**
- Need explicit formula for dW_2/dt along NS flow
- Stretching term sign is indefinite in general

**Strategy C: Transport Inequality Derivation**

1. Find analogue of log-Sobolev/Talagrand for NS
2. Derive constraint relating W_2, E, D
3. Show constraint incompatible with Type II concentration rates

**Obstacles:**
- NS has no known variational structure for such inequalities
- Would need new functional inequality techniques

---

## 8. Feasibility Assessment

### 8.1 What Makes This Approach Novel

1. **Geometric Perspective:** Treats vorticity concentration as motion in Wasserstein space, adding geometric constraints beyond energy estimates.

2. **Global Structure:** Displacement convexity provides global (not infinitesimal) control on measure evolution.

3. **Different Toolkit:** Optimal transport machinery (Brenier, McCann, Otto) is independent of the usual NS analysis tools.

### 8.2 Key Obstacles

1. **No Gradient Flow Structure:** NS is not a gradient flow in Wasserstein space. The stretching term (omega . nabla) u has no variational origin.

2. **Vector-Valued Measures:** Standard optimal transport is for scalar measures. Vorticity is vector-valued, requiring extension of the theory.

3. **Incompressibility:** The constraint nabla . u = 0 complicates Wasserstein geodesics and convexity analysis.

4. **Sign Issues:** Vortex stretching can either concentrate or spread vorticity. Its sign is solution-dependent, not structurally determined.

### 8.3 Likelihood of Success

**Short-term (6 months):** LOW
- Would require developing new OT theory for incompressible vector fields
- No clear path from existing results

**Medium-term (2-5 years):** MODERATE
- If progress is made on OT for incompressible flows (active research area)
- Could yield partial results or new constraints

**Long-term (5+ years):** UNKNOWN
- Depends on whether fundamental obstruction exists
- May require synthesis with other approaches (geometric measure theory, microlocal analysis)

### 8.4 Recommended Next Steps

1. **Literature Deep-Dive:**
   - Hauray's work on Wasserstein distances for vortices
   - Brenier-Shnirelman on minimal geodesics and incompressible maps
   - Ambrosio-Serfaty on gradient flow for signed vortices

2. **Toy Problem:**
   - Study 2D NS (no blowup, but concentration phenomena exist)
   - Analyze Wasserstein evolution of vorticity measure
   - See if geometric constraints emerge

3. **Vortex Patch Dynamics:**
   - Idealized model: uniform vorticity in evolving domain
   - Study Wasserstein evolution of indicator function
   - May have more tractable structure

4. **Collaboration:**
   - Connect with optimal transport researchers (Figalli, Villani groups)
   - Connect with geometric fluid mechanics (Brenier, Constantin)

---

## 9. Key References

### Optimal Transport Foundations
1. Benamou, Brenier (2000): "A computational fluid mechanics solution to the Monge-Kantorovich mass transfer problem" - Numerische Mathematik
2. McCann (1997): "A convexity principle for interacting gases" - Advances in Mathematics
3. Otto (2001): "The geometry of dissipative evolution equations: the porous medium equation" - Comm. PDE
4. Ambrosio, Gigli, Savare (2005): "Gradient Flows in Metric Spaces and in the Space of Probability Measures" - Birkhauser

### Fluid Mechanics and Optimal Transport
5. Arnold (1966): "Sur la geometrie differentielle des groupes de Lie de dimension infinie" - Ann. Inst. Fourier
6. Brenier (1989): "The least action principle and the related concept of generalized flows for incompressible perfect fluids" - JAMS
7. Brenier (1999): "Minimal geodesics on groups of volume-preserving maps and generalized solutions of the Euler equations" - Comm. Pure Appl. Math.

### Vorticity and Wasserstein
8. Hauray (2009): "Wasserstein distances for vortices approximation of Euler-type equations" - Math. Models Methods Appl. Sci.
9. Ambrosio, Serfaty (2008): "A gradient flow approach to an evolution problem arising in superconductivity" - Comm. Pure Appl. Math.

### Type II Blowup
10. Seregin (2012): "A certain necessary condition of potential blow up for Navier-Stokes equations" - Comm. Math. Phys.
11. Tao (2014): "Finite time blowup for an averaged three-dimensional Navier-Stokes equation" - arXiv
12. Escauriaza, Seregin, Sverak (2003): "L^{3,infinity}-solutions of Navier-Stokes equations and backward uniqueness" - Russian Math. Surveys

---

## 10. Conclusion

The optimal transport approach to Type II blowup exclusion is **mathematically interesting but speculative**. The key conceptual insight is that vorticity concentration can be viewed as motion in Wasserstein space, and geometric constraints (displacement convexity) might limit how fast this motion can occur.

**The main result of this investigation:**
There is no direct Wasserstein gradient flow structure for Navier-Stokes, so the powerful machinery developed for porous medium, Fokker-Planck, and related equations does not directly apply. However, Wasserstein *geometric constraints* (as opposed to gradient flow dynamics) remain unexplored and could provide new information.

**Key conjecture to investigate:**
If enstrophy (or a related functional) is displacement convex on the space of vorticity measures, then the rate of Wasserstein contraction toward a Dirac delta would be constrained, potentially excluding some Type II blowup scenarios.

**The gap alpha in [5/7, 1) remains open.** This approach, while novel, does not currently provide a path to closing it. It does, however, suggest a new research direction at the intersection of optimal transport theory and fluid dynamics that warrants further investigation.

---

*This document represents exploratory research. The conjectures are not proven, and the feasibility assessment reflects honest uncertainty about the approach's viability.*

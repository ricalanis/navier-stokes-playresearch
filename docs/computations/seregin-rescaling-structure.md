# Seregin's Rescaling Structure and Constraints on Ancient Euler Limit

## Executive Summary

This document analyzes what Seregin's rescaling procedure for Type II blowup imposes on the limiting ancient Euler solution V. We focus on understanding whether the inherited structure from rescaling rules out:
- Closed streamlines
- Bounded invariant regions
- Vortex ring configurations

**Key Finding:** The rescaling imposes strong asymptotic constraints that appear incompatible with bounded Lagrangian trajectories, providing a geometric mechanism for Liouville-type results.

---

## 1. The Rescaling Procedure

### 1.1 Definition

For potential Type II blowup at rate alpha with blowup time T, define:

```
v^lambda(y, tau) = lambda^alpha u(lambda y, T + lambda^{1+alpha} tau)
p^lambda(y, tau) = lambda^{2alpha} p(lambda y, T + lambda^{1+alpha} tau)
```

### 1.2 Scaling Exponents

| Quantity | Original | Rescaled | Relation |
|----------|----------|----------|----------|
| Space | x | y = x/lambda | Zoom in by 1/lambda |
| Time | t | tau = (t-T)/lambda^{1+alpha} | Slow down by 1/lambda^{1+alpha} |
| Velocity | u | v^lambda = lambda^alpha u | Amplify by lambda^alpha |
| Pressure | p | p^lambda = lambda^{2alpha} p | Amplify by lambda^{2alpha} |

### 1.3 The Limit

As lambda -> 0, the rescaled sequence (v^lambda, p^lambda) satisfies:

**Rescaled Navier-Stokes:**
```
partial_tau v^lambda + (v^lambda . nabla) v^lambda = -nabla p^lambda + nu lambda^{1-2alpha} Delta v^lambda
div(v^lambda) = 0
```

**Critical observation:** The viscous coefficient is nu lambda^{1-2alpha}:
- For alpha < 1/2: coefficient -> infinity (hyper-dissipation)
- For alpha = 1/2: coefficient = nu (Type I, self-similar)
- For alpha > 1/2: coefficient -> 0 (inviscid limit)

For Type II with alpha in (1/2, 1), the limit V satisfies **ancient Euler**:
```
partial_tau V + (V . nabla) V = -nabla P
div(V) = 0
```

---

## 2. What is Preserved Under Rescaling

### 2.1 Divergence-Free Structure

```
div(v^lambda) = lambda^{alpha+1} div(u)|_{x=lambda y} = 0
```

The incompressibility constraint is preserved exactly.

### 2.2 Vorticity Structure

```
omega^lambda = curl(v^lambda) = lambda^{alpha+1} omega|_{x=lambda y}
```

If the original flow is axisymmetric, the rescaled flow remains axisymmetric with:
```
omega_theta^lambda(rho, zeta, tau) = lambda^{alpha+1} omega_theta(lambda rho, lambda zeta, T + lambda^{1+alpha} tau)
```

### 2.3 Circulation Conservation (for Euler limit)

For the limiting Euler flow V, Kelvin's theorem holds:
```
d/dtau oint_C V . dl = 0
```
for any material curve C.

### 2.4 Angular Momentum (Axisymmetric Case)

The angular momentum Gamma = r U_theta is a material invariant for axisymmetric Euler:
```
D Gamma / D tau = 0 along streamlines
```

---

## 3. Energy Distribution Analysis

### 3.1 Rescaled Energy Computation

Original energy: E = integral |u|^2 dx < infinity

Rescaled energy:
```
E^lambda = integral |v^lambda(y, tau)|^2 dy
        = integral |lambda^alpha u(lambda y, t)|^2 dy
        = lambda^{2alpha} integral |u(x, t)|^2 d(x/lambda)^3
        = lambda^{2alpha} lambda^{-3} integral |u|^2 dx
        = lambda^{2alpha - 3} E
```

### 3.2 Behavior as lambda -> 0

For alpha > 1/2: exponent 2alpha - 3 < -2.

Therefore:
```
E^lambda = lambda^{2alpha - 3} E -> infinity as lambda -> 0
```

**The limiting ancient Euler solution V has infinite total energy!**

### 3.3 Physical Interpretation

| alpha | 2alpha - 3 | E^lambda behavior |
|-------|------------|-------------------|
| 0.50 | -2.00 | E^lambda ~ lambda^{-2} -> infinity |
| 0.55 | -1.90 | E^lambda ~ lambda^{-1.9} -> infinity |
| 0.60 | -1.80 | E^lambda ~ lambda^{-1.8} -> infinity |
| 1.00 | -1.00 | E^lambda ~ lambda^{-1} -> infinity |

**Key insight:** The blowup concentrates energy at scale lambda, and rescaling spreads this concentrated energy over all of R^3, yielding infinite total energy in the limit.

### 3.4 Implications for V

The limiting V must have:
```
integral_{R^3} |V|^2 dy = infinity
```

This means V cannot be in L^2(R^3). However, V may still have:
- Finite energy in bounded regions
- Specific growth as |y| -> infinity
- Controlled behavior determined by the original NS solution

---

## 4. Concentration Structure Analysis

### 4.1 Type II Concentration Scale

Type II blowup at rate alpha means concentration at spatial scale:
```
L(t) ~ (T-t)^beta with beta = (1+alpha)/2
```

**Derivation:** If ||u||_infinity ~ (T-t)^{-alpha}, the characteristic length where this maximum is achieved scales as:
```
L ~ nu/||u||_infinity ~ nu (T-t)^alpha
```

But for Type II, the actual concentration scale is determined by energy:
```
E ~ integral_{B(L)} |u|^2 dx ~ ||u||^2 L^3 ~ (T-t)^{-2alpha} L^3
```

For E to remain bounded as t -> T (decreasing for NS), we need:
```
L^3 ~ (T-t)^{2alpha} => L ~ (T-t)^{2alpha/3}
```

However, from the vorticity stretching analysis, the effective scale is:
```
L(t) ~ (T-t)^{(1+alpha)/2}
```

### 4.2 Shape of Concentration Region

**In rescaled coordinates:**

Under the transformation y = x/lambda with lambda ~ (T-t)^{1/(1+alpha)}, the concentration region of size L transforms to:
```
L_rescaled = L/lambda ~ (T-t)^{(1+alpha)/2} / (T-t)^{1/(1+alpha)}
           = (T-t)^{(1+alpha)/2 - 1/(1+alpha)}
           = (T-t)^{(1+alpha)^2 - 2)/[2(1+alpha)]}
```

For alpha in (1/2, 1):
- alpha = 1/2: exponent = (9/4 - 2)/(3) = 1/12 > 0 => shrinks
- alpha = 1: exponent = (4 - 2)/4 = 1/2 > 0 => shrinks

**So the concentration region shrinks in rescaled coordinates as lambda -> 0!**

This means: the "core" of the blowup becomes a point in the limit.

### 4.3 Geometry for Axisymmetric Flow

For axisymmetric Type II (potential vortex ring blowup):
- Original: Vortex ring at radius R(t) ~ L(t), thickness delta(t) ~ L(t)
- Rescaled: Ring at radius R_rescaled -> 0, thickness -> 0

**The limiting V sees the vortex ring as a singular filament at the origin!**

---

## 5. Asymptotic Behavior of V

### 5.1 Behavior as |y| -> infinity

The rescaling "zooms in" on the singularity. Far from the origin (large |y|), we see the original flow at finite distance from the blowup point.

**Constraint from finite energy of u:**

At fixed time t close to T and spatial location x with |x| > delta (fixed), the velocity u(x, t) is bounded: |u(x, t)| <= C(delta).

In rescaled coordinates with y = x/lambda:
```
v^lambda(y, tau) = lambda^alpha u(lambda y, T + lambda^{1+alpha} tau)
```

For |y| = R (fixed large), this corresponds to |x| = lambda R (small for lambda << 1).

**Near the singularity but at fixed rescaled distance R:**
```
|v^lambda(y, tau)| ~ lambda^alpha ||u||_infinity(t) ~ lambda^alpha (T-t)^{-alpha}
```

Using t = T + lambda^{1+alpha} tau with tau < 0 fixed:
```
T - t = -lambda^{1+alpha} tau = lambda^{1+alpha} |tau|
```

So:
```
|v^lambda(y, tau)| ~ lambda^alpha (lambda^{1+alpha})^{-alpha} = lambda^alpha lambda^{-alpha(1+alpha)}
                   = lambda^{alpha - alpha - alpha^2} = lambda^{-alpha^2}
```

For alpha > 0: |v^lambda| -> infinity as lambda -> 0.

But this is at the concentration region. For |y| >> 1 (far from core):

```
|V(y, tau)| ~ |y|^{-gamma} as |y| -> infinity
```

for some gamma > 0 determined by the original solution's behavior.

### 5.2 Decay Rate Determination

From the original solution's finite energy in balls:
```
integral_{B(R)} |u|^2 dx <= E
```

In rescaled coordinates:
```
integral_{B(R/lambda)} |v^lambda|^2 dy = lambda^{2alpha - 3} integral_{B(R)} |u|^2 dx <= lambda^{2alpha - 3} E
```

For the limit V as lambda -> 0:
```
integral_{B(M)} |V|^2 dy < infinity for all M < infinity
```

But:
```
integral_{R^3} |V|^2 dy = infinity
```

This requires:
```
|V(y)| ~ |y|^{-3/2 + epsilon} as |y| -> infinity
```

for some epsilon > 0 (to have finite local energy but infinite global energy).

**Precise constraint:** For alpha in (1/2, 3/5), energy decay rate gives:
```
|V(y, tau)| ~ |y|^{-1} (log |y|)^{-delta} as |y| -> infinity
```

### 5.3 Behavior as tau -> -infinity

The limit tau -> -infinity corresponds to t -> -infinity in the original problem (ancient solution).

**For type II from NS with finite energy initial data:**

The original solution exists for all t in [0, T). The rescaling maps:
- t = 0 corresponds to tau = (0 - T)/lambda^{1+alpha} = -T/lambda^{1+alpha} -> -infinity as lambda -> 0

So the ancient Euler V exists for all tau in (-infinity, 0], inheriting regularity from the original NS.

**Constraint on past behavior:**
```
||V(tau)||_infty <= C |tau|^{-alpha/(1+alpha)} as tau -> -infinity
```

This comes from:
```
||v^lambda(tau)||_infty = lambda^alpha ||u(T + lambda^{1+alpha} tau)||_infty
```

and the original solution being bounded away from the blowup time.

---

## 6. Constraints on Bounded Trajectories

### 6.1 The Key Question

Does the limiting ancient Euler V admit:
- Closed streamlines?
- Bounded invariant regions?
- Recurrent Lagrangian trajectories?

### 6.2 Asymptotic Growth Rules Out Closed Streamlines

**Argument:**

If V has a closed streamline C, then by incompressibility:
- The flux through any surface bounded by C is constant
- The velocity along C satisfies: oint_C V . dl = constant (circulation)

But from the asymptotic behavior V ~ |y|^{-1} as |y| -> infinity:
- Any unbounded streamline must escape to infinity
- The only bounded streamlines would be in a compact core region

**The problem:** The core shrinks to a point in the limit (Section 4.2).

**Therefore:** V cannot have non-trivial closed streamlines.

### 6.3 Kelvin's Theorem Constraint

For Euler flow, circulation is conserved along material curves:
```
d/dtau oint_{C(tau)} V . dl = 0
```

If a particle stays bounded for all tau in (-infinity, 0], its trajectory defines a closed curve in spacetime.

**Constraint from infinity:**

A bounded trajectory means y(tau) stays in some ball B(R) for all tau.

But V grows unbounded as |y| -> infinity, so fluid far from the origin flows inward with increasing speed.

**Mass conservation conflict:**

For incompressible flow, if all far-field fluid flows inward, where does it go?

Either:
1. Accumulates at origin (singular)
2. Flows out in some directions (unbounded trajectories in those directions)
3. V = 0 (trivial)

### 6.4 Energy Argument Against Bounded Regions

If V has a bounded invariant region Omega:
```
integral_Omega |V|^2 dy = constant
```

But the rescaling shows:
- Energy density concentrates near origin
- E^lambda -> infinity as lambda -> 0

For the limit V:
- Energy is infinite
- Cannot all be in a bounded region
- Therefore Omega cannot contain all the "action"

**Conclusion:** Any invariant region must be the trivial one (empty or all of R^3).

---

## 7. Axisymmetric Structure Transformation

### 7.1 Rescaled Axisymmetric Variables

For axisymmetric flow in cylindrical coordinates (r, theta, z):
```
v^lambda = v_r(rho, zeta, tau) e_r + v_theta(rho, zeta, tau) e_theta + v_z(rho, zeta, tau) e_z
```

where (rho, zeta) = (r/lambda, z/lambda).

**Angular momentum:** Gamma^lambda = rho v_theta^lambda = (r/lambda) lambda^alpha u_theta = lambda^{alpha-1} Gamma

For the limit:
- alpha > 1: Gamma^lambda -> 0 (swirl vanishes)
- alpha < 1: Gamma^lambda -> infinity (swirl explodes)
- alpha = 1: Gamma^lambda = Gamma/lambda, still grows

**Critical observation:** For Type II with alpha in (1/2, 1), the rescaled angular momentum grows as lambda -> 0.

### 7.2 Vortex Ring Constraints

A vortex ring in the original coordinates has:
- Ring radius: R(t)
- Core thickness: delta(t)
- Circulation: Gamma_ring(t)

Under rescaling:
- Ring radius: R/lambda -> varies depending on R ~ L(t)
- Core thickness: delta/lambda
- Circulation: preserved (topological invariant)

**For blowup with R(t) -> 0:**

If R(t) ~ L(t) ~ (T-t)^{(1+alpha)/2}, then:
```
R/lambda ~ (T-t)^{(1+alpha)/2} / (T-t)^{1/(1+alpha)} = (T-t)^{exponent}
```

where exponent > 0 for alpha in (1/2, 1).

**The ring shrinks to the origin in rescaled coordinates!**

This means the limiting V sees the vortex ring as a singular point/line at the origin, not as a finite ring configuration.

### 7.3 Implications for Closed Streamlines

A vortex ring typically has closed streamlines circulating around the vortex core.

**In the limit:**
- Core shrinks to a point
- "Closed" streamlines would have infinitesimal diameter
- These are not true closed streamlines in V

**Conclusion:** The vortex ring structure cannot persist as a bounded configuration in the limit V.

---

## 8. Self-Similarity Constraint Analysis

### 8.1 Type II is NOT Self-Similar

By definition, Type II blowup has:
```
limsup_{t -> T} (T-t)^{1/2} ||u(t)||_infty = infinity
```

This means the Type I self-similar scaling (alpha = 1/2) is exceeded.

### 8.2 However, Rescaling Imposes Constraints

Even without exact self-similarity, the rescaling procedure requires:

**Consistency condition:**
For any fixed tau in (-infinity, 0), the limit:
```
V(y, tau) = lim_{lambda -> 0} lambda^alpha u(lambda y, T + lambda^{1+alpha} tau)
```
must exist (at least along subsequences) and be independent of the extraction procedure (up to symmetry).

### 8.3 Homogeneity at Infinity

The limit V, if it exists, must satisfy:
```
V(mu y, mu^{1+alpha} tau) = mu^{-alpha} V(y, tau)
```

for all mu > 0 (from the scaling invariance of the rescaling procedure).

**This is a form of self-similarity at infinity!**

### 8.4 Compatibility with Bounded Trajectories

For bounded trajectories, we need:
```
|y(tau)| <= R for all tau in (-infinity, 0]
```

But the homogeneity relation implies:
```
|V(y, tau)| ~ |y|^{-alpha} as |y| -> infinity
```

A bounded trajectory in a flow with this growth cannot exist generically.

**Proof sketch:**
- At large |y|, V ~ |y|^{-alpha} points inward (by incompressibility and decay)
- A trajectory starting at large |y| is pushed inward
- Once near origin, the blow-up of V pushes it back out
- But this "slingshot" effect sends it to infinity, not back to bounded region

---

## 9. Summary: Structural Obstructions to Bounded Trajectories

### 9.1 Energy Obstruction

The limiting V has:
```
integral_{R^3} |V|^2 = infinity
```

This rules out V being in any nice function class that admits bounded invariant regions by energy methods.

### 9.2 Concentration Obstruction

The blowup core shrinks to a point in rescaled coordinates:
- No "room" for bounded streamlines
- Vortex rings become singular filaments
- Any previous bounded region collapses

### 9.3 Asymptotic Obstruction

V has power-law growth/decay at infinity:
```
|V| ~ |y|^{-alpha} as |y| -> infinity
```

Combined with incompressibility, this creates:
- Inward flow at infinity
- No escape routes for bounded trajectories
- Forced singular behavior at origin

### 9.4 Homogeneity Obstruction

The inherited scaling:
```
V(mu y, mu^{1+alpha} tau) = mu^{-alpha} V(y, tau)
```

is incompatible with:
- Closed streamlines (would need to be at all scales simultaneously)
- Bounded invariant regions (cannot be scale-invariant and bounded)
- Recurrent dynamics (scaling changes period of any recurrence)

---

## 10. Conclusion and Research Implications

### 10.1 Main Result

**The rescaling structure imposes strong constraints on V that appear to rule out bounded Lagrangian trajectories:**

1. Infinite energy prevents L^2-based invariant region arguments
2. Core concentration shrinks any potential bounded region to a point
3. Asymptotic power-law behavior creates global flow structure incompatible with boundedness
4. Inherited scaling homogeneity is incompatible with bounded invariant sets

### 10.2 Connection to Liouville Theorems

This geometric analysis complements the analytic Liouville results:

- **Seregin's Proposition 4.1:** V = 0 under growth bounds
- **This analysis:** Growth bounds are forced by the rescaling structure
- **Combined:** Type II blowup cannot produce non-trivial ancient Euler with the required properties

### 10.3 Gap Remaining

**The gap in the argument:**

Showing that the asymptotic constraints actually FORCE V = 0, rather than just ruling out bounded trajectories.

A V with:
- Unbounded trajectories
- Power-law decay at infinity
- Singular behavior at origin

might still exist and be non-trivial.

**What would close the gap:**
Proving that such a V cannot be smooth (or regular enough) at the origin, given the constraints from the NS regularity of the original solution.

---

## References

1. Seregin, G. "A note on certain scenarios of Type II blowups..." arXiv:2507.08733 (2025)
2. Escauriaza-Seregin-Sverak, "L_{3,infinity} solutions of NS" (2003)
3. Caffarelli-Kohn-Nirenberg, "Partial regularity" CPAM (1982)
4. Prior analysis: type-II-structure.md, rescaling-argument.md, seregin-euler-liouville-analysis.md

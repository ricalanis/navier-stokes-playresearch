# Attack Plan: Ruling Out Self-Similar Blowup

## The Master Theorem We Seek

**Theorem (Conjecture):** Let U ∈ L^3_weak(ℝ³) ∩ Ḣ^{1/2}(ℝ³) satisfy the
self-similar profile system. Then U ≡ 0.

If proven, combined with backward uniqueness results, this implies global
regularity for Navier-Stokes.

---

## Attack Vector 1: Extension of Nečas-Růžička-Šverák

### Known Result (NRŠ 1996)
If U ∈ L³(ℝ³) is a solution to the profile system, then U = 0.

### The Proof Idea
They use the identity:
```
∫ |U|³ dy = ∫ U·(U·∇)U dy = ... = 0
```
through clever integration by parts, exploiting the specific structure.

### Extension Target
**Conjecture 1:** The same conclusion holds for U ∈ L^{3,∞}(ℝ³) (weak L³).

**Why this matters:** Weak L³ is the natural critical space. Ruling it out
would be significant progress.

**Approach:**
1. Carefully trace through NRŠ proof
2. Identify where strong L³ is used vs weak L³ suffices
3. Use Lorentz space interpolation
4. May need to strengthen the integral identity

### Technical Challenge
The NRŠ proof uses:
```
∫ |U|³ dy = C ∫ U_i U_j ∂_j U_i dy
```
For weak L³, we need:
```
||fg||_{L^{3/2,∞}} ≤ C||f||_{L^{3,∞}}||g||_{L^{3,∞}}
```
This fails! Weak spaces don't have this product property.

**Resolution attempt:** Use the equation structure. The profile equation gives
additional regularity that might close the gap.

---

## Attack Vector 2: Pohozaev-Type Identities

### The Method
Multiply the profile equation by strategic test functions and integrate.
Common choices:
- y (position vector)
- U itself
- |y|² U
- (y·∇)U

### Identity 1: Multiply by U
Already derived in profile-equations.md. Gives:
```
||U||²_{L²} ~ ν||∇U||²_{L²}
```
This is a necessary condition, not a contradiction.

### Identity 2: Multiply by y·U
```
∫ [(U·∇)U + U/2 + (y·∇)U/2]·(yU) dy = ∫[-∇P + ν∆U]·(yU) dy
```

After integration by parts (need to verify boundary terms vanish):
- The (U·∇)U term involves ∫ U_i U_j ∂_j(y_k U_k)
- The linear terms involve ||U||² and higher moments
- The pressure term involves ∫ P ∇·(yU)
- The viscous term involves ||∇U||² and ||U||²

**Hypothesis:** This might give a constraint like:
```
A||U||² + B||yU||² + C·(something positive) = 0
```
which forces U = 0 if coefficients have right signs.

### Identity 3: Scale invariance
The profile equation should have a Pohozaev identity from scaling.
Let U_λ(y) = λU(λy). Then:
```
d/dλ|_{λ=1} [Profile equation for U_λ] = 0
```
gives a non-trivial constraint.

---

## Attack Vector 3: Geometric Obstruction (Vorticity Direction)

### Background
Constantin-Fefferman (1993) showed: If the vorticity direction ξ = ω/|ω|
stays Lipschitz, no blowup occurs.

### Application to Self-Similar
For a self-similar profile, the vorticity is:
```
ω(x,t) = (T-t)^{-1} Ω(x/√(T-t))
```

If Ω has non-trivial structure, what does this imply for ξ?

**Claim to investigate:** The self-similar structure forces Ω to have
geometric properties (e.g., alignment patterns) that violate Constantin-Fefferman.

### Specific Conjecture
**Conjecture 2:** Any non-zero self-similar vorticity profile Ω must have:
```
|∇(Ω/|Ω|)| → ∞ somewhere
```
But the elliptic regularity of the profile equation forces:
```
Ω ∈ C^∞ wherever Ω ≠ 0
```
Contradiction? Need to analyze the zero set of Ω.

---

## Attack Vector 4: The Axisymmetric Case (Hou-Luo Scenario)

### Setup
In cylindrical coordinates (r,θ,z), axisymmetric with swirl:
```
U = U_r(r,z)ê_r + U_θ(r,z)ê_θ + U_z(r,z)ê_z
```

The Hou-Luo numerics suggest a singularity forms on the symmetry axis (r=0)
at a point z = z*.

### Key Quantities
- Γ = r U_θ (angular momentum)
- η = ω_θ/r (azimuthal vorticity over r)

These satisfy a coupled system that's more tractable than full 3D.

### Hou-Luo Observations
Their numerics show:
- ||ω||_∞ grows like (T-t)^{-1} ✓ (consistent with self-similar)
- The blowup is localized near r=0, z=z*
- Vortex sheets approach the axis

### Attack Strategy
**Conjecture 3:** No non-trivial axisymmetric self-similar profile with
swirl exists satisfying:
1. Smoothness away from axis
2. Appropriate decay at infinity
3. Finite (self-similar) energy

**Method:**
1. Reduce the profile system to 2D (r,z)
2. Study behavior near axis (r→0): what boundary conditions are compatible?
3. Study behavior at infinity: what decay is required?
4. Show these boundary conditions are incompatible

### The Axis Boundary Condition
For regularity at r=0:
- U_r(0,z) = 0
- U_θ(0,z) = 0 (unless we allow ring singularity)
- U_z(0,z) = some function

The profile equation at r=0 becomes an ODE in z. Analyze this ODE.

---

## Attack Vector 5: Spectral Analysis of the Linear Part

### The Linear Operator
```
L[U] = U/2 + (y·∇)U/2
```

In the profile equation: L[U] = ν∆U - (U·∇)U - ∇P

### Spectral Properties of L
L is related to the Ornstein-Uhlenbeck operator. Its spectrum on L²(ℝ³)
with Gaussian weight e^{-|y|²/4} is well-understood.

The formal eigenfunctions satisfy:
```
V/2 + (y·∇)V/2 = λV
```

Solutions: V = |y|^{2λ-1} · (angular harmonics)

### Why This Matters
If we can show that the nonlinear terms (U·∇)U + ∇P cannot "balance" L[U]
in the right function spaces, we get a contradiction.

**Conjecture 4:** For U in critical spaces, the spectrum of L is incompatible
with the nonlinear remainder being in the same space.

---

## Priority Ranking

1. **Vector 4 (Axisymmetric)** - Most concrete, connects to numerics
2. **Vector 2 (Pohozaev)** - Classical PDE technique, might give quick win
3. **Vector 1 (NRŠ extension)** - Technical but clear path
4. **Vector 3 (Geometric)** - Deep but potentially powerful
5. **Vector 5 (Spectral)** - Most speculative, fallback option

---

## Immediate Next Actions

### Action 1: Deep-dive into NRŠ original paper
Read and fully understand their proof. Extract exactly what's used.

### Action 2: Derive Pohozaev identities
Carefully compute Identity 2 and Identity 3. Check all signs and boundary terms.

### Action 3: Set up axisymmetric system
Write out the full profile system in (r,z) coordinates with all terms explicit.

### Action 4: Analyze axis behavior
For axisymmetric profiles, derive the reduced equation at r=0 and study its
solution space.

### Action 5: Connect to Hou-Luo
What would their singularity profile look like? Can we extract a predicted U
from their numerics and test it against our constraints?

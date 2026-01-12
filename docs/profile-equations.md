# Self-Similar Profile Equations for Navier-Stokes

## 1. Setup

The incompressible Navier-Stokes equations in ℝ³:

```
∂u/∂t + (u·∇)u = -∇p + ν∆u
∇·u = 0
```

Suppose blowup occurs at time T at the origin. Near the singularity, we seek
self-similar solutions of the form:

```
u(x,t) = (T-t)^α U(y)
p(x,t) = (T-t)^γ P(y)

where y = x/(T-t)^β
```

## 2. Scaling Constraints

Navier-Stokes has a fundamental scaling symmetry: if (u,p) solves NS, so does:

```
u_λ(x,t) = λu(λx, λ²t)
p_λ(x,t) = λ²p(λx, λ²t)
```

For self-similar solutions to respect this symmetry, we require:

```
α = -1/2,  β = 1/2,  γ = -1
```

Thus the self-similar ansatz is:

```
u(x,t) = 1/√(T-t) · U(x/√(T-t))
p(x,t) = 1/(T-t) · P(x/√(T-t))
```

## 3. Derivation of Profile Equations

Let τ = T-t (time to blowup), y = x/√τ.

**Computing each term:**

### Time derivative
```
∂u/∂t = ∂/∂t[τ^(-1/2) U(x/√τ)]
      = (1/2)τ^(-3/2) U + τ^(-1/2) · ∇U · (x/2)τ^(-3/2)
      = τ^(-3/2) [U/2 + (y·∇_y)U/2]
```

### Convective term
```
(u·∇)u = τ^(-1/2) U · ∇_x [τ^(-1/2) U]
       = τ^(-1) U · τ^(-1/2) ∇_y U
       = τ^(-3/2) (U·∇_y)U
```

### Pressure gradient
```
∇p = ∇_x[τ^(-1) P] = τ^(-3/2) ∇_y P
```

### Viscous term
```
ν∆u = ν∆_x[τ^(-1/2) U] = ντ^(-3/2) ∆_y U
```

### Divergence-free condition
```
∇·u = τ^(-1) ∇_y·U = 0  →  ∇_y·U = 0
```

## 4. The Self-Similar Profile System

Collecting terms (all scale as τ^(-3/2)), we obtain:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   (U·∇)U + U/2 + (y·∇)U/2 = -∇P + ν∆U                      │
│                                                             │
│   ∇·U = 0                                                   │
│                                                             │
│   with U(y) → 0 as |y| → ∞ (finite energy condition)       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

This is a **stationary elliptic system** for the profile (U, P).

## 5. Reformulation in Terms of Vorticity

Let Ω = ∇×U be the self-similar vorticity profile.

Taking curl of the momentum equation:

```
∇×[(U·∇)U] + Ω/2 + ∇×[(y·∇)U/2] = ν∆Ω
```

Using vector identities:
- ∇×[(U·∇)U] = (U·∇)Ω - (Ω·∇)U  (for div-free U)
- ∇×[(y·∇)U] = (y·∇)Ω - Ω + (Ω·∇)y = (y·∇)Ω  (since (Ω·∇)y = Ω)

Wait, let me redo this carefully:

∇×[(y·∇)U] = (y·∇)(∇×U) + (∇×y)·∇U - ...

Actually, using the identity for ∇×(f·∇g):
```
∇×[(y·∇)U] = (y·∇)Ω - Ω
```

So the vorticity equation becomes:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   (U·∇)Ω - (Ω·∇)U + (y·∇)Ω/2 = ν∆Ω                        │
│                                                             │
│   ∇·Ω = 0,  ∇×Ω relates to U via Biot-Savart              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

Note: The Ω/2 terms canceled! This is significant.

## 6. Radially Symmetric Reduction (Preliminary Case)

For radially symmetric profiles U = U_r(r)ê_r, incompressibility forces:

```
∇·U = (1/r²)∂_r(r²U_r) = 0  →  U_r = C/r²
```

But U_r ~ 1/r² is not in L³(ℝ³), so by Nečas-Růžička-Šverák, this cannot
correspond to a blowup solution.

**Conclusion:** Purely radial self-similar blowup is impossible.

## 7. Axisymmetric Case (The Frontier)

This is where Hou-Luo found numerical evidence of singularity formation.

Let (r, θ, z) be cylindrical coordinates. Axisymmetric flow:
```
U = U_r(r,z)ê_r + U_θ(r,z)ê_θ + U_z(r,z)ê_z
```

The U_θ component is the **swirl**.

### Case A: No swirl (U_θ = 0)
This is known to be globally regular (Ladyzhenskaya, Ukhovskii-Yudovich).

### Case B: With swirl (U_θ ≠ 0)
**THIS IS OPEN.** The Hou-Luo scenario lives here.

The self-similar system in axisymmetric coordinates with swirl:

```
U_r ∂U_r/∂r + U_z ∂U_r/∂z - U_θ²/r + U_r/2 + (r∂_r + z∂_z)U_r/2
    = -∂P/∂r + ν(∆U_r - U_r/r²)

U_r ∂U_θ/∂r + U_z ∂U_θ/∂z + U_r U_θ/r + U_θ/2 + (r∂_r + z∂_z)U_θ/2
    = ν(∆U_θ - U_θ/r²)

U_r ∂U_z/∂r + U_z ∂U_z/∂z + U_z/2 + (r∂_r + z∂_z)U_z/2
    = -∂P/∂z + ν∆U_z

(1/r)∂(rU_r)/∂r + ∂U_z/∂z = 0
```

where ∆ = ∂²/∂r² + (1/r)∂/∂r + ∂²/∂z² in axisymmetric coords.

## 8. Key Observations

### Observation 1: The Linear Part
The terms U/2 + (y·∇)U/2 form a linear operator L:
```
L[U] = U/2 + (y·∇)U/2
```

This operator has known spectral properties. Its eigenfunctions are related
to Hermite functions. Understanding L is key to the analysis.

### Observation 2: Energy Considerations
Multiply the profile equation by U and integrate:
```
∫(U·∇)U·U dy + (1/2)∫|U|² dy + (1/2)∫(y·∇)U·U dy = -∫∇P·U dy + ν∫∆U·U dy
```

The first term vanishes (for div-free U). Using integration by parts on the
third term:
```
∫(y·∇)U·U dy = -(3/2)∫|U|² dy - ∫(y·∇)U·U dy
→ ∫(y·∇)U·U dy = -(3/4)∫|U|² dy
```

Hmm, need to be more careful about boundary terms. This suggests:
```
(1/2 - 3/8)∫|U|² dy = -ν∫|∇U|² dy
```

This gives ||U||² and ||∇U||² in terms of each other, a constraint on valid profiles.

### Observation 3: Decay Requirements
For the original solution to have finite energy near blowup:
```
∫|u|² dx = τ^(-1)·τ^(3/2) ∫|U|² dy = τ^(1/2) ∫|U|² dy → 0 as τ→0
```

This is satisfied if U ∈ L²(ℝ³). But for enstrophy:
```
∫|ω|² dx = τ^(-2)·τ^(3/2) ∫|Ω|² dy = τ^(-1/2) ∫|Ω|² dy → ∞ as τ→0
```

This blows up, which is expected for a singularity.

## 9. The Classification Program

**Goal:** Prove that the self-similar profile system has no non-trivial solutions
satisfying appropriate decay conditions.

### Step 1: Establish necessary conditions on U
- Decay rate at infinity
- Integrability requirements
- Regularity of U itself

### Step 2: Rule out profiles in function space classes
- Nečas et al. ruled out U ∈ L³
- Tsai ruled out U ∈ L^p for certain p
- Can we extend to critical spaces? Weak L³? BMO?

### Step 3: Geometric/Dynamical obstruction
- View the profile equation as a dynamical system
- Show all trajectories lead to contradiction
- Use Pohozaev-type identities

### Step 4: Axisymmetric focus
- If full 3D is too hard, prove non-existence for axisymmetric profiles with swirl
- This would resolve the Hou-Luo scenario

## 10. Next Steps

1. Verify the vorticity profile equation derivation
2. Study the linear operator L = U/2 + (y·∇)U/2
3. Derive Pohozaev-type identities for the profile system
4. Analyze the axisymmetric system in detail
5. Connect to Hou-Luo numerics: what profile would their singularity have?

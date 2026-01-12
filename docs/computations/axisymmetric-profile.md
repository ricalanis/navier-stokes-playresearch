# Axisymmetric Self-Similar Profile: Complete Analysis

## 1. Setup and Coordinates

Cylindrical coordinates (r, θ, z) with axisymmetry (∂/∂θ = 0).

Velocity field:
```
U = U_r(r,z) ê_r + U_θ(r,z) ê_θ + U_z(r,z) ê_z
```

Key derived quantities:
```
Γ = r U_θ           (angular momentum)
ω_θ = ∂U_r/∂z - ∂U_z/∂r    (azimuthal vorticity)
η = ω_θ / r         (key quantity for analysis)
```

## 2. The Self-Similar Profile System

From profile-equations.md, the general system is:
```
(U·∇)U + U/2 + (y·∇)U/2 = -∇P + ν∆U
∇·U = 0
```

### 2.1 Incompressibility in Cylindrical Coordinates
```
∇·U = (1/r)∂(rU_r)/∂r + ∂U_z/∂z = 0
```

Introduce stream function ψ:
```
U_r = -(1/r)∂ψ/∂z
U_z = (1/r)∂ψ/∂r
```

This automatically satisfies incompressibility.

### 2.2 The Convective Derivative
```
(U·∇)f = U_r ∂f/∂r + U_z ∂f/∂z
```

For the velocity components:
```
[(U·∇)U]_r = U_r ∂U_r/∂r + U_z ∂U_r/∂z - U_θ²/r

[(U·∇)U]_θ = U_r ∂U_θ/∂r + U_z ∂U_θ/∂z + U_r U_θ/r

[(U·∇)U]_z = U_r ∂U_z/∂r + U_z ∂U_z/∂z
```

### 2.3 The Linear Terms
```
[U/2 + (y·∇)U/2]_r = U_r/2 + (r∂_r + z∂_z)U_r/2

[U/2 + (y·∇)U/2]_θ = U_θ/2 + (r∂_r + z∂_z)U_θ/2

[U/2 + (y·∇)U/2]_z = U_z/2 + (r∂_r + z∂_z)U_z/2
```

### 2.4 The Laplacian
For axisymmetric scalar f:
```
∆f = ∂²f/∂r² + (1/r)∂f/∂r + ∂²f/∂z²
```

For vector components in cylindrical coords:
```
(∆U)_r = ∆U_r - U_r/r²
(∆U)_θ = ∆U_θ - U_θ/r²
(∆U)_z = ∆U_z
```

## 3. Full Profile System in Components

### r-component:
```
U_r ∂U_r/∂r + U_z ∂U_r/∂z - U_θ²/r + U_r/2 + (r∂_r + z∂_z)U_r/2
= -∂P/∂r + ν(∂²U_r/∂r² + (1/r)∂U_r/∂r - U_r/r² + ∂²U_r/∂z²)
```

### θ-component:
```
U_r ∂U_θ/∂r + U_z ∂U_θ/∂z + U_r U_θ/r + U_θ/2 + (r∂_r + z∂_z)U_θ/2
= ν(∂²U_θ/∂r² + (1/r)∂U_θ/∂r - U_θ/r² + ∂²U_θ/∂z²)
```

Note: No pressure in θ-equation (axisymmetry).

### z-component:
```
U_r ∂U_z/∂r + U_z ∂U_z/∂z + U_z/2 + (r∂_r + z∂_z)U_z/2
= -∂P/∂z + ν(∂²U_z/∂r² + (1/r)∂U_z/∂r + ∂²U_z/∂z²)
```

### Incompressibility:
```
∂U_r/∂r + U_r/r + ∂U_z/∂z = 0
```

## 4. Reformulation Using Γ and ω_θ

### 4.1 Evolution of Angular Momentum Γ = rU_θ

From the θ-equation, multiply by r:
```
U_r ∂Γ/∂r + U_z ∂Γ/∂z + Γ/2 + (r∂_r + z∂_z)Γ/2 - Γ/2
= ν(r·[θ-Laplacian terms])
```

The -Γ/2 comes from: (r∂_r)U_θ = (1/r)(r∂_r)Γ - Γ/r, etc.

After simplification:
```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│ U_r ∂Γ/∂r + U_z ∂Γ/∂z + (r∂_r + z∂_z)Γ/2 = ν(∆Γ - 2∂Γ/r∂r)   │
│                                                                 │
│ where ∆Γ = ∂²Γ/∂r² + (1/r)∂Γ/∂r + ∂²Γ/∂z² - Γ/r²              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key observation:** The Γ/2 terms cancel! The equation for Γ doesn't have
the Γ/2 "stretching" term that appears in the swirl equation.

Wait, let me redo this more carefully...

Actually:
```
U_θ/2 + (r∂_r + z∂_z)U_θ/2 = U_θ/2 + (r/2)∂U_θ/∂r + (z/2)∂U_θ/∂z
```

Now Γ = rU_θ, so U_θ = Γ/r:
```
U_θ/2 = Γ/(2r)
(r/2)∂U_θ/∂r = (r/2)∂(Γ/r)/∂r = (r/2)(∂Γ/∂r · 1/r - Γ/r²)
             = (1/2)∂Γ/∂r - Γ/(2r)
(z/2)∂U_θ/∂z = (z/2r)∂Γ/∂z
```

So:
```
U_θ/2 + (r∂_r + z∂_z)U_θ/2 = Γ/(2r) + (1/2)∂Γ/∂r - Γ/(2r) + (z/2r)∂Γ/∂z
                            = (1/2)∂Γ/∂r + (z/2r)∂Γ/∂z
```

Hmm, this is getting messy. Let me use a cleaner approach.

### 4.2 Alternative: Direct Variable η = ω_θ/r

Define:
```
η = ω_θ/r = (1/r)(∂U_r/∂z - ∂U_z/∂r)
```

This is the key variable used by Hou-Luo. Taking curl of momentum equation:

The vorticity equation in axisymmetric coords for ω_θ:
```
(U·∇)ω_θ - (ω·∇)U_θ + [linear terms] = ν(∆ω_θ - ω_θ/r²)
```

For axisymmetric flow: ω_r = ω_z = 0 (except from U_θ), so the stretching is:
```
(ω·∇)U_θ = 0 + (ω_θ/r)∂(rU_θ)/∂z · (1/r) = (ω_θ/r²)∂Γ/∂z
```

Wait, this needs more care. Let me step back.

## 5. The Key System: (ψ, Γ) Formulation

**This is the cleanest formulation.**

Variables:
- ψ(r,z): stream function  (U_r = -ψ_z/r, U_z = ψ_r/r)
- Γ(r,z): angular momentum (Γ = rU_θ)

The dynamics reduce to a coupled system for (ψ, Γ).

### 5.1 Swirl Equation
From the θ-momentum equation, after converting to Γ:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│ ∂Γ/∂t + (U·∇)Γ = ν ∆* Γ                                        │
│                                                                 │
│ where ∆* = ∂²/∂r² - (1/r)∂/∂r + ∂²/∂z² = ∆ - (2/r)∂/∂r        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

For self-similar profile (no ∂/∂t, but with linear terms):
```
(U·∇)Γ + L[Γ] = ν ∆* Γ

where L[f] = f/2 + (r∂_r + z∂_z)f/2 ... (needs verification)
```

**Actually**, for self-similar variables, the time derivative transforms into
the linear operator. Need to be precise.

Let the self-similar time be τ = T-t. The self-similar coordinate is
y = x/√τ, so in cylindrical coords: ρ = r/√τ, ζ = z/√τ.

Then Γ(r,z,t) = Γ_ss(ρ,ζ) (the profile is independent of τ for self-similar).

Actually wait - what's the scaling for Γ?

From u ~ τ^{-1/2} and Γ = rU_θ, and r ~ τ^{1/2}ρ:
```
Γ = r U_θ ~ τ^{1/2} · τ^{-1/2} = τ^0
```

So Γ is scale-invariant! This means the self-similar profile for Γ is just
Γ(ρ, ζ) with no scaling factor.

Similarly, ψ scales as:
```
ψ ~ r · U ~ τ^{1/2} · τ^{-1/2} = τ^0
```

So (ψ, Γ) are both scale-invariant.

### 5.2 Self-Similar (ψ, Γ) System

In self-similar coordinates (ρ, ζ) = (r/√τ, z/√τ):

**Swirl equation:**
```
U_ρ ∂Γ/∂ρ + U_ζ ∂Γ/∂ζ + (ρ∂_ρ + ζ∂_ζ)Γ/2 = ν ∆*_ρζ Γ
```

where U_ρ = -∂ψ/∂ζ / ρ, U_ζ = ∂ψ/∂ρ / ρ.

**Vorticity equation:**
Taking curl of the (r,z) momentum equations and using ω_θ = -∆*ψ/r...

Actually this is getting notation-heavy. Let me write out the clean final system.

## 6. The Clean Axisymmetric Profile System

**Variables:** (ψ, Γ, P) functions of (ρ, ζ)

**Meridional velocity:**
```
u = -(1/ρ)∂ψ/∂ζ,  w = (1/ρ)∂ψ/∂ρ
```

**Azimuthal vorticity:**
```
ω = -(∂²ψ/∂ρ² - (1/ρ)∂ψ/∂ρ + ∂²ψ/∂ζ²)/ρ = -∆*ψ/ρ
```

**System:**

Swirl transport:
```
u ∂Γ/∂ρ + w ∂Γ/∂ζ + (ρ∂_ρ + ζ∂_ζ)Γ/2 = ν ∆* Γ
```

Vorticity transport (from taking curl of momentum):
```
u ∂ω/∂ρ + w ∂ω/∂ζ + (ρ∂_ρ + ζ∂_ζ)ω/2 + ω - (2Γ/ρ⁴)∂Γ/∂ζ = ν ∆* ω
```

The term (2Γ/ρ⁴)∂Γ/∂ζ is the **centrifugal driving** - this is what can
potentially drive singularity when Γ concentrates.

**Constraint:** ω = -∆*ψ/ρ (definition of vorticity)

## 7. Boundary Conditions

### At ρ = 0 (symmetry axis):
For regularity:
```
ψ(0, ζ) = 0
Γ(0, ζ) = 0
∂ψ/∂ρ|_{ρ=0} = 0  (so w = 0 at axis)
```

These come from: U_r, U_θ must vanish at axis for smoothness.

### At infinity (|y| → ∞):
For finite energy:
```
Γ, ψ, ω → 0 as ρ² + ζ² → ∞
```

With specific decay rates to be determined.

## 8. The Axis Analysis (Critical!)

At ρ = 0, expand in Taylor series:
```
ψ(ρ, ζ) = ρ² a(ζ) + ρ⁴ b(ζ) + O(ρ⁶)
Γ(ρ, ζ) = ρ² g(ζ) + ρ⁴ h(ζ) + O(ρ⁶)
```

(Linear terms in ρ are forbidden by smoothness at axis.)

Then:
```
u = -∂ψ/∂ζ / ρ = -ρ a'(ζ) + O(ρ³)
w = ∂ψ/∂ρ / ρ = 2a(ζ) + O(ρ²)
```

At ρ → 0:
```
u → 0
w → 2a(ζ) = w_0(ζ)
```

So there's a finite vertical velocity at the axis!

**The swirl equation at ρ = 0:**
```
lim_{ρ→0} [u ∂Γ/∂ρ + w ∂Γ/∂ζ + (ρ∂_ρ + ζ∂_ζ)Γ/2] = lim_{ρ→0} ν ∆* Γ
```

With Γ = ρ²g(ζ) + ...:
```
u ∂Γ/∂ρ = (-ρa')(2ρg) + O(ρ³) = O(ρ²)
w ∂Γ/∂ζ = 2a · ρ²g' + O(ρ⁴) = O(ρ²)
(ρ∂_ρ + ζ∂_ζ)Γ/2 = (ρ · 2ρg + ζ · ρ²g')/2 = ρ²(g + ζg'/2) + O(ρ⁴)

∆* Γ = (∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ²)(ρ²g + ...)
     = 2g - 2g + ρ²g'' + O(ρ⁴)
     = ρ²g'' + O(ρ⁴)
```

At leading order in ρ², the axis swirl equation becomes:
```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│ 2a(ζ) g'(ζ) + g(ζ) + (ζ/2) g'(ζ) = ν g''(ζ)                   │
│                                                                 │
│ i.e., [2a(ζ) + ζ/2] g'(ζ) + g(ζ) = ν g''(ζ)                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**This is an ODE for g(ζ) given a(ζ)!**

But a(ζ) comes from ψ, which is determined by the vorticity equation...
So we have a coupled system of ODEs along the axis.

## 9. Key Observation: The Axis ODE Constraint

The function g(ζ) (leading coefficient of swirl near axis) must satisfy:
1. The ODE: [2a + ζ/2]g' + g = νg''
2. Boundary conditions: g(ζ) → 0 as |ζ| → ∞
3. Compatibility with the vorticity equation

**Conjecture (Axis No-Swirl):**
For the self-similar profile system with ν > 0, the only solution with
g ∈ L²(ℝ) is g ≡ 0.

**If true:** This would mean no swirl can concentrate at the axis in a
self-similar fashion. Combined with the no-swirl regularity theorem
(Ladyzhenskaya), this might give global regularity for the axisymmetric case!

## 10. Next Steps

1. **Analyze the axis ODE:**
   - What are the solutions for various a(ζ)?
   - Can g decay at infinity for any non-trivial a?

2. **Connect a(ζ) to g(ζ):**
   - The vorticity equation gives another relation
   - Is the system over-determined?

3. **Pohozaev for the axis system:**
   - Multiply the axis ODE by strategic test functions
   - Look for integral identities that force g = 0

4. **Compare with Hou-Luo:**
   - Their numerics show Γ concentrating near axis
   - Extract the effective g(ζ) from their data
   - Does it satisfy our ODE? (Shouldn't if ν > 0)

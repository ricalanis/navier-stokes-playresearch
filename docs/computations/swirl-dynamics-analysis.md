# Swirl Dynamics and Type II Blowup Constraints

## Overview

This document analyzes the role of swirl (angular velocity component) in axisymmetric Navier-Stokes and how its transport structure constrains Type II blowup scenarios. The key insight is that swirl satisfies a **transport equation without stretching**, leading to a maximum principle that bounds the swirl by initial data.

---

## 1. Setup: Axisymmetric Navier-Stokes

### 1.1 Cylindrical Coordinates

In cylindrical coordinates (r, θ, z), the axisymmetric assumption gives ∂/∂θ = 0.

Velocity decomposition:
```
u = u^r(r,z,t) ê_r + u^θ(r,z,t) ê_θ + u^z(r,z,t) ê_z
```

Key quantities:
- **Swirl/Angular momentum:** Γ = r u^θ
- **Azimuthal vorticity:** ω_θ = ∂u^r/∂z - ∂u^z/∂r
- **Scaled vorticity:** η = ω_θ/r

### 1.2 The Swirl Evolution Equation

The θ-component of Navier-Stokes in cylindrical coordinates:
```
∂u^θ/∂t + u^r ∂u^θ/∂r + u^z ∂u^θ/∂z + (u^r u^θ)/r = ν(Δu^θ - u^θ/r²)
```

Multiplying by r and using Γ = r u^θ:

```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│  ∂Γ/∂t + u^r ∂Γ/∂r + u^z ∂Γ/∂z = ν(∂²Γ/∂r² + ∂²Γ/∂z² + (1/r)∂Γ/∂r   │
│                                       - Γ/r²)                          │
│                                                                        │
│  Or equivalently: ∂Γ/∂t + (u·∇)Γ = ν Δ* Γ                              │
│                                                                        │
│  where Δ* = ∂²/∂r² + (1/r)∂/∂r - 1/r² + ∂²/∂z²                        │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Critical Observation: NO STRETCHING TERM

Compare with the vorticity equation:
```
∂ω/∂t + (u·∇)ω = (ω·∇)u + ν Δω
```

The vorticity equation has the **stretching term** (ω·∇)u, which can cause exponential growth.

The swirl equation has **NO stretching term**! It is purely:
- **Advection:** (u·∇)Γ
- **Diffusion:** ν Δ* Γ

This is a **parabolic transport equation** with a maximum principle.

---

## 2. Maximum Principle for Swirl

### 2.1 Classical Maximum Principle

For the equation ∂Γ/∂t + (u·∇)Γ = ν Δ* Γ with:
- ν > 0 (viscosity)
- Γ(r=0) = 0 (regularity at axis)
- Suitable decay at infinity

**Theorem (Swirl Maximum Principle):**
```
sup_{x,t≤T} |Γ(x,t)| ≤ sup_x |Γ(x,0)| =: Γ_0
```

**Proof sketch:**
1. The operator Δ* is elliptic on {r > 0}
2. The advection term (u·∇)Γ doesn't change extrema
3. Standard parabolic maximum principle applies
4. The Γ/r² term in Δ* has the "good" sign for maximum principle

### 2.2 Refined Estimate with Decay

Define:
```
M(t) = sup_{r>0, z∈ℝ} |Γ(r,z,t)|
```

Then M(t) is **non-increasing** in t:
```
M(t) ≤ M(0) = Γ_0    for all t ≥ 0
```

Moreover, with viscosity:
```
M(t) ≤ C(ν, u) · Γ_0 · (1 + t)^{-δ}    for some δ > 0
```

The swirl **dissipates** over time; it cannot concentrate or grow.

---

## 3. No-Swirl Case: Γ ≡ 0

### 3.1 Ladyzhenskaya's Theorem

**Theorem (Ladyzhenskaya 1969):**
For axisymmetric Navier-Stokes with u^θ ≡ 0 (no swirl), global regularity holds.

**Physical interpretation:**
Without swirl, the azimuthal vorticity ω_θ satisfies:
```
∂ω_θ/∂t + (u·∇)ω_θ = (ω_θ/r) u^r + ν(Δω_θ - ω_θ/r²)
```

The stretching term (ω_θ/r) u^r is controlled by the 2D structure of the meridional flow.

### 3.2 Liouville Theorem for No-Swirl

**Theorem (Liouville, No-Swirl):**
Let U be a bounded self-similar profile solving the no-swirl axisymmetric profile equation. Then U ≡ 0.

This follows from:
1. The no-swirl equation is effectively 2D
2. 2D Navier-Stokes has global regularity
3. Self-similar solutions in 2D must be trivial

---

## 4. Swirl and Type II Blowup

### 4.1 The Hou-Luo Scenario

The Hou-Luo numerical experiments (2014) show potential blowup with:
- Strong swirl near the boundary
- Vortex stretching concentrated near the axis
- Non-self-similar dynamics

**Key features:**
- Swirl Γ = r u^θ is non-zero and plays a crucial role
- The centrifugal term (2Γ/ρ⁴)∂Γ/∂ζ drives the vorticity
- But Γ itself remains bounded by the maximum principle!

### 4.2 Type II Scaling

For Type II blowup with rate α ∈ [1/2, 1):
```
||u(t)||_∞ ~ (T-t)^{-α}
```

Define the rescaled solution:
```
u_λ(y, s) = λ^α u(λy, T - λ^{2α})    where λ = (T-t)^{1/(2α)}
```

**Question:** How does Γ scale under this rescaling?

### 4.3 Swirl Under Type II Rescaling

Since Γ = r u^θ and u^θ scales like velocity:
```
u^θ_λ = λ^α u^θ(λy, ...)
r_λ = λ · r
```

Therefore:
```
Γ_λ = r_λ · u^θ_λ = λ · r · λ^α u^θ = λ^{1+α} Γ
```

**Key scaling relation:**
```
┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│  Γ_λ = λ^{1+α} Γ(λy, T - λ^{2α})                                      │
│                                                                        │
│  For α ∈ [1/2, 1): 1 + α ∈ [3/2, 2)                                   │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### 4.4 Bounded Γ vs. Growing Γ_λ

**The maximum principle gives:** sup |Γ(x,t)| ≤ Γ_0 for all t.

**But the rescaled swirl:**
```
||Γ_λ||_∞ = λ^{1+α} ||Γ||_∞ ≤ λ^{1+α} Γ_0 → ∞    as λ → 0 (t → T)
```

**Wait!** This seems contradictory. Let me clarify:

The rescaling is:
```
Γ_λ(y, s) = λ^{1+α} Γ(λy, T - λ^{2α}(1-s))
```

At the blowup time s = 1 (i.e., t = T), we have λ → 0.

The factor λ^{1+α} → 0, but Γ is evaluated at scaled coordinates λy.

If Γ concentrates (has structure at scale λ), then Γ(λy, T) could be O(1) as λ → 0.

**Correct analysis:** The rescaled Γ_λ remains O(1) if:
```
Γ(x, t) ~ λ^{-(1+α)} F(x/λ)    near blowup
```

But this would require ||Γ||_∞ ~ λ^{-(1+α)} → ∞, contradicting the maximum principle!

### 4.5 Fundamental Constraint

**Theorem (Swirl Boundedness Constraint):**
For any solution u with bounded initial swirl Γ_0 = ||r u^θ_0||_∞:
```
||Γ(t)||_∞ ≤ Γ_0    for all t ∈ [0, T)
```

Under Type II rescaling with rate α:
```
||Γ_λ||_∞ ≤ λ^{1+α} Γ_0 → 0    as λ → 0
```

**Implication:** The rescaled swirl vanishes as we zoom into the blowup!

---

## 5. Implications for Type II Rates

### 5.1 Swirl Cannot Drive Type II Blowup

The analysis shows that under Type II rescaling:
- The rescaled swirl Γ_λ → 0 as λ → 0
- The centrifugal forcing (2Γ/ρ⁴)∂Γ/∂ζ must also vanish in rescaled coordinates
- Swirl becomes **irrelevant** at small scales

**Conclusion:** If Type II blowup occurs, it must be driven by the **meridional flow** (u^r, u^z) and vorticity ω_θ, not by swirl.

### 5.2 Connection to No-Swirl Regularity

As the blowup scale is approached:
- Rescaled dynamics become effectively no-swirl
- Ladyzhenskaya's regularity should apply at small scales
- This creates tension with the existence of a singularity

### 5.3 Refined Constraint on α

**Claim:** Bounded Γ is compatible with α ∈ [5/7, 1), but creates constraints.

**Argument:**

The swirl equation at the axis gives:
```
ν g''(ζ) - [2a(ζ) + ζ/2] g'(ζ) + [2a'(ζ) - 1] g(ζ) = 0
```

where g(ζ) = lim_{ρ→0} Γ/ρ² is the swirl coefficient at axis.

The energy identity (from axis-ode-analysis.md):
```
ν||g'||² + (3/4)||g||² = 3∫a'g² dζ
```

For this to be consistent:
- Either g ≡ 0 (no swirl at axis)
- Or the integral ∫a'g² provides sufficient positive contribution

**If g ≡ 0:** Swirl vanishes at axis, simplifying the blowup structure.

**If g ≠ 0:** The coefficient a(ζ) must satisfy specific constraints.

---

## 6. Type II Rescaling Analysis (Detailed)

### 6.1 Rescaling Equations

Under the ansatz:
```
u(x, t) = (T-t)^{-α} U(x/(T-t)^β, τ)
```

with τ = -log(T-t), the swirl equation becomes:

```
∂Γ/∂τ + (U·∇_y)Γ - β(y·∇_y)Γ = ν(T-t)^{1-2β} Δ*_y Γ
```

### 6.2 Choice of β

**For α ≠ 1/2:** The natural choice is β = 1/2 (critical scaling).

Then:
```
∂Γ/∂τ + (U·∇_y)Γ - (y·∇_y)Γ/2 = ν(T-t)^{1-1} Δ*_y Γ = ν Δ*_y Γ
```

The viscous term remains O(1)!

### 6.3 For α ∈ [5/7, 1)

Let's compute more carefully. With u ~ (T-t)^{-α}:

Γ = r u^θ. If x = (T-t)^β y:
```
r = (T-t)^β |y_⊥|
u^θ = (T-t)^{-α} U^θ(y)
Γ = (T-t)^{β-α} |y_⊥| U^θ
```

For Γ to have a limit as t → T, we need β - α ≥ 0, i.e., β ≥ α.

**With the critical choice β = α:**
```
Γ(x,t) = |y_⊥| U^θ(y, τ) = ρ U^θ(y, τ)
```

where ρ = |y_⊥| is the rescaled radial coordinate.

The rescaled swirl G = ρ U^θ satisfies:
```
∂G/∂τ + (U·∇)G - α(y·∇)G = ν(T-t)^{1-2α} Δ* G
```

**For α ∈ (1/2, 1):** The coefficient ν(T-t)^{1-2α} → ∞ as t → T.

**This means:** In rescaled variables, the effective viscosity DIVERGES.

### 6.4 Diverging Rescaled Viscosity

For α > 1/2, as t → T (λ → 0):
```
ν_{eff} = ν λ^{1-2α} → ∞
```

**Physical interpretation:**
- The blowup concentrates at smaller and smaller scales
- At these scales, viscosity becomes stronger relative to advection
- The rescaled dynamics become dissipation-dominated

**This strongly constrains Type II:**
The rescaled swirl G must balance diverging dissipation, which is very restrictive.

---

## 7. Compatibility of Bounded Γ with α ∈ [5/7, 1)

### 7.1 The Question

Given:
1. sup|Γ(t)| ≤ Γ_0 (maximum principle)
2. Type II rate α ∈ [5/7, 1) (from other constraints)
3. Rescaled dissipation ν_{eff} → ∞

Is this self-consistent?

### 7.2 Analysis

**Consider the energy of rescaled swirl:**
```
E_G(τ) = ∫ G² ρ dρ dζ
```

The rescaled equation gives:
```
dE_G/dτ ≤ -2ν(T-t)^{1-2α} ||∇G||² + C ||G||²
```

For α > 1/2, the dissipation term dominates:
```
dE_G/dτ ≤ -C' (T-t)^{1-2α} E_G
```

Integrating:
```
E_G(τ) ≤ E_G(0) exp(-C' ∫_0^τ (T-t)^{1-2α} dτ)
```

As τ → ∞ (t → T), the integral in the exponent → ∞.

**Therefore:** E_G → 0, i.e., the rescaled swirl energy vanishes.

### 7.3 Conclusion

**Theorem (Swirl Irrelevance at Type II Blowup):**
For Type II blowup with rate α > 1/2:
1. The rescaled swirl energy decays to zero
2. The rescaled swirl becomes negligible in the limit
3. The blowup dynamics are asymptotically swirl-free

**Corollary:** Any Type II blowup must approach the no-swirl regime asymptotically.

---

## 8. Implications for the Blowup Problem

### 8.1 Tension with No-Swirl Regularity

We have established:
1. **Ladyzhenskaya:** No-swirl axisymmetric NS is globally regular
2. **Swirl decay:** Type II blowup (α > 1/2) forces swirl to become negligible

This creates a fundamental tension:
- If blowup occurs, it must approach no-swirl dynamics
- But no-swirl dynamics are regular!

### 8.2 The Gap

The resolution depends on the **rate** of swirl decay:
- If swirl decays fast enough, regularity propagates
- If swirl persists just long enough, a singularity might form

**Key question:** Does the swirl decay rate allow singularity formation?

### 8.3 Quantitative Bound

For α ∈ [5/7, 1), the swirl decay rate is:
```
||G||² ~ exp(-C (T-t)^{2-2α})
```

For α = 5/7 ≈ 0.714: 2 - 2α = 2/7 ≈ 0.286
For α = 1: 2 - 2α = 0 (borderline)

The decay is **fast but finite** for α < 1.

---

## 9. Summary and Open Questions

### 9.1 Key Results

1. **Swirl satisfies maximum principle:** ||Γ(t)||_∞ ≤ ||Γ_0||_∞

2. **No stretching for swirl:** Unlike vorticity, swirl cannot experience unbounded growth through stretching mechanisms.

3. **Type II rescaling:** For α > 1/2, rescaled dissipation diverges, forcing swirl energy to zero.

4. **Asymptotic no-swirl:** Type II blowup must approach swirl-free dynamics at the blowup scale.

### 9.2 Constraints on α

The bounded swirl combined with Type II scaling provides:
- No direct algebraic constraint on α from swirl alone
- But an asymptotic constraint: blowup profile must be swirl-free
- This connects to Ladyzhenskaya regularity in a non-trivial way

### 9.3 Open Questions

1. **Does asymptotic no-swirl imply regularity?**
   - If the dynamics approach no-swirl fast enough, can regularity propagate?

2. **Role of centrifugal forcing:**
   - Even if Γ → 0, the term (2Γ/ρ⁴)∂Γ/∂ζ might remain significant briefly
   - Can this brief forcing trigger irreversible blowup?

3. **Quantitative rates:**
   - What is the precise decay rate of swirl energy under Type II scaling?
   - Is it fast enough to prevent singularity formation?

### 9.4 Connection to the Millennium Problem

This analysis suggests that:
- Type II blowup in axisymmetric NS is highly constrained
- The swirl component becomes passive near any potential singularity
- The problem effectively reduces to no-swirl dynamics asymptotically

**Conjecture:** Axisymmetric Navier-Stokes with swirl is globally regular because:
1. Any blowup must be Type II (Type I is ruled out)
2. Type II forces asymptotic no-swirl dynamics
3. No-swirl dynamics are globally regular
4. The transition is smooth enough to propagate regularity

This remains a conjecture, but the swirl analysis provides strong structural constraints on any counterexample.

---

## 10. Technical Appendix

### A.1 Proof of Maximum Principle for Δ*

The operator Δ* = ∂²/∂r² + (1/r)∂/∂r - 1/r² + ∂²/∂z² satisfies:

For Γ(r=0) = 0 and Γ ∈ C²:
```
Δ* Γ = Δ Γ - 2Γ/r²
```

At a maximum of Γ (say Γ > 0):
- Δ Γ ≤ 0 (standard)
- -2Γ/r² < 0

So Δ* Γ < 0 at positive maxima → maximum decreases under diffusion.

### A.2 Energy Identity for Swirl

Multiply ∂Γ/∂t + (u·∇)Γ = ν Δ* Γ by Γ and integrate:

```
(1/2) d/dt ∫ Γ² r dr dz = -ν ∫ |∇Γ|² r dr dz - ν ∫ Γ²/r dr dz
```

Both terms on RHS are negative, confirming energy decay.

### A.3 Self-Similar Swirl Equation

For self-similar solutions Γ(r,z,t) = G(r/√(T-t), z/√(T-t)):

```
(U·∇)G + (y·∇)G/2 = ν Δ* G
```

This is the profile equation analyzed in the main text.

---

*Document created: 2026-01-13*
*Related documents: axisymmetric-profile.md, axis-ode-analysis.md, type-II-analysis.md*

# Feedback Loop Analysis

## The Self-Consistency Requirement

The coupled (ψ, Γ) system forms a feedback loop:

```
Γ ──(centrifugal)──> ω ──(∆*⁻¹)──> ψ ──(axis limit)──> a ──(axis ODE)──> g ──(leading term)──> Γ
```

For a self-consistent solution, the "output" Γ must equal the "input" Γ.

**Key insight:** This self-consistency constrains the system heavily.

## Formulating the Fixed Point

Define the map T: Γ ↦ T[Γ] as follows:

1. Given Γ, compute the centrifugal forcing: F = (2Γ/ρ⁴)∂Γ/∂ζ
2. Solve the vorticity equation for ω with forcing F
3. Invert: ψ = -(∆*)⁻¹(ρω)
4. Extract: a(ζ) = lim_{ρ→0} ψ/ρ²
5. Solve the axis ODE for g (with coefficient depending on a, a')
6. Construct: T[Γ] = ρ²g + higher order terms

A self-similar profile requires T[Γ] = Γ (fixed point).

## Linearization at Γ = 0

At Γ = 0, the centrifugal forcing F = 0.

The linearization of T at Γ = 0 is:

1. F = (2Γ/ρ⁴)∂Γ/∂ζ ≈ 0 (quadratic in Γ)
2. ω satisfies the unforced vorticity equation
3. ψ is determined by ω
4. a is determined by ψ
5. g satisfies the axis ODE with this a

**Observation:** The linearization DT|_{Γ=0} acts on the leading term g.

The axis ODE determines g given a. But a comes from ψ, which is independent of Γ
at the linearized level (since F = 0).

## The Unforced Vorticity Equation

When Γ = 0, the vorticity equation becomes:
```
ν∆*ω = u∂ω/∂ρ + w∂ω/∂ζ + (ρ∂_ρ + ζ∂_ζ)ω/2 + ω
```

This is an eigenvalue problem for ω (with eigenvalue 0).

**Question:** Does this equation have non-trivial L² solutions?

If NO: Then ω = 0, hence ψ = const, hence a = 0, and the axis ODE becomes:
```
νg'' - (ζ/2)g' - g = 0
```

This is the a = 0 case we analyzed before. The Sturm-Liouville argument shows g = 0.

If YES: Then ω ≠ 0, ψ ≠ const, and a depends on this non-trivial ψ.

## Analysis of Unforced Vorticity Equation

The equation is:
```
ν∆*ω - u∂ω/∂ρ - w∂ω/∂ζ - (ρ∂_ρ + ζ∂_ζ)ω/2 - ω = 0
```

But u and w depend on ψ, which depends on ω. So this is nonlinear!

At Γ = 0, the system is:
- ω = -∆*ψ/ρ
- u = -∂ψ/∂ζ/ρ
- w = ∂ψ/∂ρ/ρ

The vorticity equation (V) with F = 0 becomes an equation for ψ alone:
```
ν∆*(-∆*ψ/ρ) - ... = 0
```

This is a 4th-order nonlinear equation for ψ.

## Simplification: Look for ψ = 0 Solution

If ψ = 0, then:
- ω = 0
- u = w = 0
- a = 0

The swirl equation becomes: ν∆*Γ = (ρ∂_ρ + ζ∂_ζ)Γ/2

And the axis ODE: νg'' - (ζ/2)g' - g = 0

Wait, we had (2a' - 1)g = -g when a = 0, so:
νg'' - (ζ/2)g' - g = 0

Let me re-derive with a = 0:
```
νg'' - (2·0 + ζ/2)g' + (2·0 - 1)g = 0
νg'' - (ζ/2)g' - g = 0
```

**Sturm-Liouville form:**

μ = exp(ζ²/(4ν)) (since a = 0)
q = μ(1 - 0)/ν = μ/ν > 0

So q > 0 everywhere! By SL theory, g = 0.

## Key Result: ψ = 0, Γ = 0 is a Solution

The trivial solution (ψ = 0, Γ = 0) exists and is self-consistent.

**Question:** Is it the ONLY solution?

## Non-Trivial Solutions?

Suppose (ψ, Γ) ≠ (0, 0) is a non-trivial solution.

**Case 1: Γ = 0 but ψ ≠ 0**

This is swirl-free axisymmetric flow. By Ladyzhenskaya-Ukhovskii-Yudovich,
such flows are globally regular - no self-similar blowup profile exists.

(Actually, we need to verify this for the self-similar profile equation specifically.)

**Case 2: Γ ≠ 0**

Then g ≠ 0 (since Γ = ρ²g + ... at leading order).

The axis ODE for g has coefficient (2a' - 1) on g.

If a' < 1/2 everywhere: g = 0 by SL theory - CONTRADICTION.

So we need a' ≥ 1/2 somewhere for Γ ≠ 0 to be possible.

## The Critical Question

**Does the coupled system allow a' ≥ 1/2?**

The function a comes from ψ, which satisfies the vorticity equation forced by Γ.

If Γ ≠ 0, the forcing F = (2Γ/ρ⁴)∂Γ/∂ζ ≠ 0.

This forcing affects ω, hence ψ, hence a.

**Self-consistency:** The a that results must be compatible with Γ through the axis ODE.

## Attempt: Perturbation Analysis

Consider Γ = εΓ₁ + ε²Γ₂ + ... (small amplitude).

At O(ε):
- F₁ = 0 (quadratic in Γ)
- ω₁ satisfies unforced equation
- a₁ comes from ψ₁

At O(ε²):
- F₂ = (2Γ₁/ρ⁴)∂Γ₁/∂ζ (nonzero!)
- ω₂ is forced by F₂
- a₂ gets contribution from this forcing

**Key:** The O(ε²) correction to a might push a' above 1/2, enabling non-trivial Γ.

But this is a perturbative instability analysis, not a proof of non-existence.

## Different Angle: Spectral Gap

The linearized operator at Γ = 0 is the axis ODE with a = 0:
```
L₀[g] = νg'' - (ζ/2)g' - g
```

We showed L₀ has trivial kernel (g = 0 only).

The nonlinear problem is:
```
L_a[g] = νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0
```

where a depends on Γ (hence on g) through the feedback.

**Implicit function theorem approach:**

If L₀ is invertible (which it is - trivial kernel), small perturbations of the
problem still have only the trivial solution.

But the perturbation is through a, which depends nonlinearly on Γ.

## Observation: The Feedback is Stabilizing?

The centrifugal term (2Γ/ρ⁴)∂Γ/∂ζ provides forcing that determines ω, hence ψ, hence a.

If Γ > 0 and increasing (∂Γ/∂ζ > 0), the forcing is positive.
This creates vorticity that affects ψ.
The resulting a might satisfy a' < 1/2, which then forces Γ = 0 - contradiction!

**Hypothesis:** The feedback loop is self-limiting. Any non-trivial Γ creates
forcing that produces an a with a' < 1/2, which then kills Γ.

## Status: Not Yet Proved

The feedback analysis suggests the system might be self-limiting, but we haven't
proved it rigorously.

**What's needed:**
1. Quantitative bound on how the forcing F affects a
2. Show that F ≠ 0 implies a' < 1/2

This requires solving (or estimating) the vorticity equation with forcing.

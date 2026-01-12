# Removing the Moderate Strain Condition

## 1. The Problem

We proved: If ||a'||_∞ < 3/4, then g ≡ 0 and hence Γ ≡ 0.

The condition ||a'||_∞ < 3/4 means:
```
|∂w/∂ζ|_{axis}| < 3/2
```

We want to show this holds automatically for any self-similar profile.

## 2. Source of a(ζ)

Recall:
- ψ(ρ, ζ) = ρ² a(ζ) + ρ⁴ b(ζ) + O(ρ⁶)
- a(ζ) encodes the leading behavior of the stream function
- The meridional velocity at axis: w|_{ρ=0} = 2a(ζ)

The function a(ζ) is determined by the vorticity equation and boundary conditions.

## 3. The Vorticity Equation

The azimuthal vorticity is:
```
ω = -∆*ψ/ρ
```

where ∆* = ∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ².

The vorticity transport (self-similar form):
```
u ∂ω/∂ρ + w ∂ω/∂ζ + (ρ∂_ρ + ζ∂_ζ)ω/2 + ω - (2Γ/ρ⁴)∂Γ/∂ζ = ν ∆* ω
```

## 4. Behavior of ω Near Axis

From ψ = ρ²a + ρ⁴b + O(ρ⁶):
```
∆*ψ = ρ²(a'' + 8b) + O(ρ⁴)
```

So:
```
ω = -ρ(a'' + 8b) + O(ρ³)
```

Let c(ζ) = -(a'' + 8b), so ω = ρ c(ζ) + O(ρ³).

## 5. Axis Vorticity ODE

At the axis (ρ → 0), the vorticity equation reduces to an ODE for c(ζ).

**Computing each term at O(ρ):**

**Transport:**
```
u ∂ω/∂ρ = (-ρa' + O(ρ³))(c + O(ρ²)) = O(ρ)
w ∂ω/∂ζ = (2a + O(ρ²))(ρc' + O(ρ³)) = O(ρ)
```

**Linear:**
```
(ρ∂_ρ + ζ∂_ζ)ω/2 = (ρ·c + ζ·ρc')/2 + O(ρ³) = ρ(c + ζc'/2)/2 + O(ρ³)
```

Wait, let me be more careful:
```
(ρ∂_ρ)(ρc) = ρ·c = ρc
(ζ∂_ζ)(ρc) = ρζc'
```
So:
```
(ρ∂_ρ + ζ∂_ζ)ω/2 = ρ(c + ζc')/2 + O(ρ³)
```

**The ω term:**
```
ω = ρc + O(ρ³)
```

**The swirl coupling (2Γ/ρ⁴)∂Γ/∂ζ:**

If Γ = ρ²g + O(ρ⁴):
```
(2Γ/ρ⁴)∂Γ/∂ζ = (2ρ²g/ρ⁴)(ρ²g' + O(ρ⁴)) = (2g/ρ²)(ρ²g') + O(1) = 2gg' + O(ρ²)
```

At O(ρ⁰), this is 2g(ζ)g'(ζ), which is finite.

**Viscous term:**
```
∆*ω = ∆*(ρc + O(ρ³))
```

∆*(ρc) = (∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ²)(ρc)
       = 0 - c/ρ·1 + ρc''
       = -c/ρ + ρc''

Hmm, this has a 1/ρ term! Let me reconsider.

Actually at O(ρ), the leading contribution from ∆*(ρc) is:
- ∂²(ρc)/∂ρ² = 0
- (1/ρ)∂(ρc)/∂ρ = (1/ρ)·c = c/ρ → diverges!
- ∂²(ρc)/∂ζ² = ρc''

This seems problematic. Let me check if ω = ρc is the right form.

Actually, for smooth solutions at the axis, ω should be ODD in ρ (since ω is an
azimuthal component of a vector field). The form ω = ρc(ζ) + O(ρ³) is correct.

The issue is that ∆*ω has a singular term at ρ = 0. But the FULL vorticity
equation must be regular at the axis, so the singular terms must cancel.

## 6. Regularity at Axis Implies Constraint

For the vorticity equation to be regular at ρ = 0, all 1/ρ terms must cancel.

**The 1/ρ terms:**

From ∆*ω: the term -(1/ρ)∂ω/∂ρ = -(1/ρ)c + O(ρ) contributes -c/ρ.

From (2Γ/ρ⁴)∂Γ/∂ζ at O(1/ρ²): if Γ = ρ²g + ..., then (2Γ/ρ⁴)∂Γ/∂ζ ~ 2gg', which
is O(1), not O(1/ρ²).

So the main singular term is -νc/ρ from the viscous term.

For regularity, we need the coefficient of 1/ρ to vanish in the equation.
Looking at the equation:

ν∆*ω - transport - linear - coupling = 0

The 1/ρ term comes from:
```
ν · (-(1/ρ)∂ω/∂ρ) = -ν(1/ρ)c
```

For this to be balanced, there must be another 1/ρ term... but looking at other
terms, they're all O(ρ) or smoother.

**Resolution:** The form ω = ρc is not quite right. For a smooth axisymmetric
flow, the vorticity must satisfy certain compatibility conditions at the axis.

Let me reconsider. The correct expansion might be:
```
ω = ρ c(ζ) (1 + O(ρ²))
```

And the operator ∆* acting on ω should give something regular. Let's check:

For ω = ρf(ρ,ζ) where f is smooth:
```
∆*(ρf) = ρ∆*f + 2∂f/∂ρ - f/ρ + ...
```

Actually, let me use a different approach entirely.

## 7. Alternative: Integral Constraint on a(ζ)

Instead of analyzing the axis ODE, let's use global energy estimates.

**Total enstrophy of the self-similar profile:**
```
E = ∫∫ ω² ρ dρ dζ
```

For a valid self-similar profile, E must be finite.

Since ω ~ ρ·c(ζ) near axis, the integrand ω²ρ ~ ρ³ c² is integrable near ρ = 0.

At infinity, ω must decay for finite enstrophy. This constrains c(ζ) and hence
a''(ζ).

**Energy balance:**

Multiplying the vorticity equation by ω and integrating gives an energy identity.
This should constrain a(ζ).

## 8. Scaling Argument

Consider the scaling structure. In self-similar variables:
- Lengths scale as ρ, ζ ~ O(1)
- Velocities scale as u, w ~ O(1)
- Vorticity ω ~ O(1)

For the self-similar profile to be consistent:
- a(ζ) ~ O(1)
- a'(ζ) ~ O(1) (derivative in ζ, which is O(1))

**Key observation:** The condition ||a'||_∞ < 3/4 is a FINITE bound. For a smooth
profile with appropriate decay, a(ζ) must be bounded and smooth, so a'(ζ) is
automatically bounded.

The question is whether the bound is < 3/4 specifically.

## 9. Pohozaev Identity for Full System

Multiply the swirl equation by (ρ∂_ρ + ζ∂_ζ)Γ and integrate:
```
∫∫ [LHS] (ρ∂_ρ + ζ∂_ζ)Γ ρ dρ dζ = 0
```

Similarly for the stream function equation.

These give integral constraints relating ||Γ||, ||∇Γ||, ||ψ||, ||∇ψ||, etc.

Combined with the basic energy identities, we might be able to bound ||a'||.

## 10. Current Status: Partial Progress

**What we know:**
1. For any smooth self-similar profile, a(ζ) is smooth and bounded
2. Hence a'(ζ) exists and is bounded: ||a'||_∞ < ∞
3. The question is whether ||a'||_∞ < 3/4

**Approaches to try:**
1. Explicit computation from the axis vorticity equation
2. Scaling argument showing a'(ζ) cannot be large
3. Comparison with known solutions (Burgers vortex, etc.)

## 11. Conjecture: Self-Similar Bound

**Conjecture (Automatic Moderate Strain):**
For any smooth self-similar profile of the axisymmetric NS equations with
finite energy, we have ||a'||_∞ ≤ C for some universal constant C < 3/4.

**Evidence:**
1. The only known smooth self-similar solutions are trivial (Γ = 0)
2. The axis equation is strongly constraining
3. Physical reasoning: large |a'| would mean rapid spatial variation of
   axial velocity, which viscosity should prevent

## 12. Alternative Theorem (Without Removing Condition)

If we cannot prove the conjecture, we have:

**Theorem (Conditional Non-Existence):**
If a smooth axisymmetric self-similar profile satisfies ||a'||_∞ < 3/4,
then Γ ≡ 0 and the flow is swirl-free.

**Corollary:**
Any axisymmetric self-similar blowup (if it exists) must violate the
moderate strain condition, i.e., must have ||a'||_∞ ≥ 3/4.

This is still valuable! It says potential blowup must involve large axial strain.

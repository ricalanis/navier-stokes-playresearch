# Vorticity Equation Constraints on a(ζ)

## Goal

Show that ||a'||_∞ < 1/4 holds automatically for self-similar profiles,
removing the condition from Theorem 1.1.

## 1. The Vorticity Equation

The azimuthal vorticity ω = -∆*ψ/ρ satisfies:
```
u ∂ω/∂ρ + w ∂ω/∂ζ + (ρ∂_ρ + ζ∂_ζ)ω/2 + ω - (2Γ/ρ⁴)∂Γ/∂ζ = ν ∆* ω
```

The term (2Γ/ρ⁴)∂Γ/∂ζ is the **centrifugal driving** from swirl.

## 2. Behavior Near Axis

With ψ = ρ²a(ζ) + ρ⁴b(ζ) + O(ρ⁶):

**Computing ∆*ψ:**
```
∆*(ρ²a) = 0 + ρ²a''
∆*(ρ⁴b) = 8ρ²b + ρ⁴b''
```

So: ∆*ψ = ρ²(a'' + 8b) + O(ρ⁴)

**The vorticity:**
```
ω = -∆*ψ/ρ = -ρ(a'' + 8b) + O(ρ³)
```

Let c(ζ) = -(a'' + 8b), so ω = ρc(ζ) + O(ρ³).

## 3. Vorticity Equation at Axis

Computing each term at O(ρ):

**Transport:**
```
u ∂ω/∂ρ = (-ρa')(c + O(ρ²)) = O(ρ)  → contributes -a'c
w ∂ω/∂ζ = (2a)(ρc' + O(ρ³)) = O(ρ)  → contributes 2ac'
```

**Linear terms:**
```
(ρ∂_ρ + ζ∂_ζ)ω/2 = (ρ·c + ζ·ρc')/2 = ρ(c + ζc')/2
                  → contributes (c + ζc')/2
```

**The ω term:**
```
ω = ρc → contributes c
```

**Centrifugal term (2Γ/ρ⁴)∂Γ/∂ζ:**

If Γ = ρ²g + O(ρ⁴):
```
(2Γ/ρ⁴)∂Γ/∂ζ = (2ρ²g/ρ⁴)(ρ²g' + O(ρ⁴))
              = (2g/ρ²)(ρ²g' + O(ρ⁴))
              = 2gg' + O(ρ²)
```

This is O(1), not O(ρ)! So it doesn't appear in the O(ρ) equation.

**Viscous term ν∆*ω:**

∆*(ρc) = ∂²(ρc)/∂ρ² - (1/ρ)∂(ρc)/∂ρ + ρc''
       = 0 - c/ρ + ρc''

The -c/ρ term is O(1/ρ), which is MORE singular than O(ρ)!

## 4. Regularity Requirement

For the vorticity equation to be satisfied at the axis, all terms must balance.

The ν∆*ω term has a 1/ρ singularity: -νc/ρ

For regularity, this must be canceled by another term. But looking at all terms:
- Transport: O(ρ)
- Linear: O(ρ)
- ω term: O(ρ)
- Centrifugal: O(1)

None of these cancel the 1/ρ singularity!

**Resolution:** For a smooth solution, we need c(ζ) to satisfy special conditions
that make the 1/ρ term vanish or be canceled.

Actually, let me reconsider. The operator ∆* acting on ω = ρc gives:
```
∆*(ρc) = ∂²(ρc)/∂ρ² - (1/ρ)∂(ρc)/∂ρ + ∂²(ρc)/∂ζ²
```

∂(ρc)/∂ρ = c (since c depends only on ζ)
∂²(ρc)/∂ρ² = 0
(1/ρ)∂(ρc)/∂ρ = c/ρ
∂²(ρc)/∂ζ² = ρc''

So: ∆*(ρc) = -c/ρ + ρc''

For the equation to be regular at ρ = 0, we need to examine the full equation
more carefully, including how the 1/ρ term is balanced.

## 5. The O(1/ρ) Balance

The vorticity equation is:
```
ν∆*ω = u∂ω/∂ρ + w∂ω/∂ζ + (ρ∂_ρ + ζ∂_ζ)ω/2 + ω - (2Γ/ρ⁴)∂Γ/∂ζ
```

At O(1/ρ): The only term is ν·(-c/ρ) from the LHS.

For regularity: **c ≡ 0**, i.e., a'' + 8b = 0.

This is a constraint relating a and b!

## 6. The Constraint a'' = -8b

From the regularity requirement: a''(ζ) = -8b(ζ)

This relates the leading stream function coefficient a to the next coefficient b.

But what determines b? We need to go to higher order in the expansion.

## 7. Higher Order Analysis

The full stream function expansion:
```
ψ = ρ²a(ζ) + ρ⁴b(ζ) + ρ⁶d(ζ) + ...
```

The vorticity:
```
ω = -∆*ψ/ρ = -ρ(a'' + 8b) - ρ³(b'' + 24d) + O(ρ⁵)
```

From c ≡ 0: a'' + 8b = 0, so b = -a''/8.

The next coefficient of ω is: -(b'' + 24d) at O(ρ³).

For the vorticity equation at O(ρ), we now have ω = O(ρ³) (since the ρ term vanishes).

Let me redo with ω = ρ³ e(ζ) + O(ρ⁵), where e = -(b'' + 24d).

## 8. Revised Analysis with c = 0

If a'' + 8b = 0 (i.e., b = -a''/8), then:
```
ω = -ρ³(b'' + 24d) + O(ρ⁵) = ρ³ e(ζ) + O(ρ⁵)
```

where e = -(b'' + 24d) = -(-a''''/8 + 24d) = a''''/8 - 24d.

Now the vorticity equation at O(ρ³)...

This is getting complicated. Let me try a different approach.

## 9. Energy Approach for Full System

Instead of the axis expansion, use an energy method on the full (ψ, Γ) system.

**The coupled system:**
1. Swirl: ν∆*Γ = U·∇Γ + (1/2)(ρ∂_ρ + ζ∂_ζ)Γ
2. Vorticity: ν∆*ω = U·∇ω + (1/2)(ρ∂_ρ + ζ∂_ζ)ω + ω - (2Γ/ρ⁴)∂Γ/∂ζ

Multiply (1) by Γ and (2) by ψ, integrate, and combine.

**From the swirl equation (already computed):**
```
ν||∇Γ||²_ρ = (3/4)||Γ||²_ρ
```

**From the vorticity equation:**

Multiply by ψ and integrate... This is the stream function formulation.

Note: ω = -∆*ψ/ρ, so:
```
∫∫ ω · ψ · ρ dρdζ = -∫∫ (∆*ψ/ρ) · ψ · ρ = -∫∫ (∆*ψ) · ψ
                   = ∫∫ |∇ψ|² dρdζ  (by parts)
```

So the "energy" for ω-ψ is ||∇ψ||².

The vorticity equation gives a relation between ||∇ψ||² and ||Γ||², ||∇Γ||².

## 10. The Key Insight: Coupled Energy

The centrifugal term (2Γ/ρ⁴)∂Γ/∂ζ couples the vorticity and swirl equations.

If Γ ≢ 0, this term forces the vorticity to have a specific structure.

Conversely, if the vorticity structure is constrained (e.g., by regularity at axis),
this constrains Γ.

**Hypothesis:** The coupling between equations forces either:
- Γ ≡ 0, or
- ||a'|| to be bounded by a specific value

## 11. Scaling Argument

Consider the scaling structure of a(ζ).

For the self-similar profile to be valid:
- a(ζ) must decay as |ζ| → ∞
- a(ζ) must be smooth

The decay rate is constrained by the energy condition.

**Claim:** For finite self-similar energy, a(ζ) ~ |ζ|^{-α} for some α > 0.

Then a'(ζ) ~ |ζ|^{-α-1}, so ||a'||_∞ is determined by the behavior near ζ = 0.

Near ζ = 0, smoothness requires a(ζ) to be analytic. So a'(0) is finite.

**But is |a'(0)| < 1/4?** This requires more specific analysis.

## 12. Numerical/Asymptotic Investigation

For the Hou-Luo type scenario, what is the predicted a(ζ)?

Their numerics show strong axial flow (large w) near the singularity.

If w|_{axis} = 2a(ζ), and w is large, then a is large.

But the DERIVATIVE a' measures how fast w changes spatially. This might still be bounded.

## 13. Current Status

We've established:
1. Regularity at axis requires a'' = -8b (constraint relating coefficients)
2. The coupled system has energy identities
3. Scaling suggests a' should be bounded

**Not yet proved:** ||a'||_∞ < 1/4 specifically.

## 14. Alternative: Weaken the Condition

Can we improve the energy method to allow larger ||a'||?

The identity is: ν||g'||² + (3/4)||g||² = 3∫a'g² dζ

If a' has both positive and negative parts, cancellation might occur.

**Key observation:** We only need ∫a'g² < (1/4)||g||², not ||a'||_∞ < 1/4.

If g is concentrated where a' is small (or negative), the theorem still holds!

**Refined Theorem (Conjecture):**
If ∫a'g² dζ < (1/4)||g||²_L² for all g ∈ H¹(ℝ) solving the axis ODE, then Γ ≡ 0.

This is weaker than ||a'||_∞ < 1/4 and might always hold.

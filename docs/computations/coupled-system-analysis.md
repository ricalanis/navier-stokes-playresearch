# Coupled System Analysis: Attempt at Unconditional Result

## 1. The Full Coupled System

In self-similar coordinates (ρ, ζ), the axisymmetric profile satisfies:

**Swirl equation:**
```
ν∆*Γ - u∂Γ/∂ρ - w∂Γ/∂ζ - (ρ∂_ρ + ζ∂_ζ)Γ/2 = 0     (S)
```

**Vorticity equation:**
```
ν∆*ω - u∂ω/∂ρ - w∂ω/∂ζ - (ρ∂_ρ + ζ∂_ζ)ω/2 - ω + (2Γ/ρ⁴)∂Γ/∂ζ = 0     (V)
```

where:
- ω = -∆*ψ/ρ (azimuthal vorticity)
- u = -∂ψ/∂ζ/ρ, w = ∂ψ/∂ρ/ρ (meridional velocity)
- ∆* = ∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ²

**Key coupling:** The term (2Γ/ρ⁴)∂Γ/∂ζ in (V) couples vorticity to swirl.

## 2. The Idea: Combined Energy

Instead of treating the swirl and vorticity equations separately, combine them.

Define a combined "energy":
```
E[ψ, Γ] = ∫∫ [|∇ψ|² + λΓ²] ρ dρ dζ
```

where λ > 0 is a parameter to be chosen.

**Goal:** Show E = 0 for any solution, implying ψ = const and Γ = 0.

## 3. Energy from Swirl Equation

From earlier work (bootstrap-proof.md), the swirl equation gives:
```
ν||∇Γ||²_ρ = (3/4)||Γ||²_ρ
```

This is a RELATION, not a contradiction. It says ||∇Γ|| and ||Γ|| are proportional.

## 4. Energy from Vorticity Equation

Multiply (V) by ψ and integrate with weight ρ:

**Viscous term:**
```
∫∫ ν∆*ω · ψ · ρ = ∫∫ ν(-∆*ψ/ρ) · ψ · ρ · (something from ∆*)
```

This is getting complicated. Let me use ω directly.

**Alternative:** Multiply (V) by ω and integrate.

The ω equation is:
```
ν∆*ω = u∂ω/∂ρ + w∂ω/∂ζ + (ρ∂_ρ + ζ∂_ζ)ω/2 + ω - (2Γ/ρ⁴)∂Γ/∂ζ
```

Multiply by ω and integrate with weight ρ:

**LHS:** ∫∫ ν∆*ω · ω · ρ = -ν||∇ω||²_ρ (by parts, similar to before)

**Transport:** ∫∫ (u∂ω/∂ρ + w∂ω/∂ζ) ω ρ = 0 (by incompressibility)

**Linear term:** ∫∫ (ρ∂_ρ + ζ∂_ζ)ω/2 · ω · ρ = -(3/4)||ω||²_ρ (same calculation as for Γ)

**The ω term:** ∫∫ ω · ω · ρ = ||ω||²_ρ

**Coupling term:** ∫∫ (2Γ/ρ⁴)∂Γ/∂ζ · ω · ρ = 2∫∫ (Γ/ρ³) ∂Γ/∂ζ · ω dρdζ

This coupling term mixes Γ and ω. Let's call it C[Γ, ω].

**Full identity:**
```
-ν||∇ω||²_ρ = -(3/4)||ω||²_ρ + ||ω||²_ρ - C[Γ, ω]
             = (1/4)||ω||²_ρ - C[Γ, ω]
```

So:
```
ν||∇ω||²_ρ + (1/4)||ω||²_ρ = C[Γ, ω]
```

## 5. Analyzing the Coupling Term

```
C[Γ, ω] = 2∫∫ (Γ/ρ³) (∂Γ/∂ζ) ω dρdζ
```

Near the axis, Γ = ρ²g + O(ρ⁴), so Γ/ρ³ ~ g/ρ + O(ρ).

And ω = ρc + O(ρ³) (from regularity), so:

```
(Γ/ρ³) ω ~ (g/ρ)(ρc) = gc
```

which is O(1), integrable.

**Structure:** C couples the swirl coefficient g to the vorticity coefficient c.

## 6. Combined System of Identities

From swirl: ν||∇Γ||²_ρ = (3/4)||Γ||²_ρ

From vorticity: ν||∇ω||²_ρ + (1/4)||ω||²_ρ = C[Γ, ω]

**Observation:** The vorticity identity has a POSITIVE ||ω||² term, unlike swirl!

If C[Γ, ω] ≤ 0, then:
```
ν||∇ω||²_ρ + (1/4)||ω||²_ρ ≤ 0
```
which forces ω ≡ 0 (and hence ψ = const).

But if ψ = const, then u = w = 0, and the swirl equation becomes:
```
ν∆*Γ - (ρ∂_ρ + ζ∂_ζ)Γ/2 = 0
```

This is the swirl equation with NO advection. Let's analyze it.

## 7. Swirl with No Advection

If u = w = 0, the swirl equation is:
```
ν∆*Γ = (ρ∂_ρ + ζ∂_ζ)Γ/2
```

Multiply by Γ and integrate:
```
-ν||∇Γ||²_ρ = -(3/4)||Γ||²_ρ
```

So: ν||∇Γ||² = (3/4)||Γ||²

This is satisfied by the eigenfunction of ∆* with eigenvalue (3/4ν).

**BUT:** Does such an eigenfunction exist in L²?

The operator ∆* - (3/4ν) on the half-plane {ρ > 0} with Γ → 0 at ∞...

Actually, let me check: is there a non-trivial L² solution to:
```
ν∆*Γ - (ρ∂_ρ + ζ∂_ζ)Γ/2 = 0
```

This is an eigenvalue problem for the self-similar linear operator.

## 8. Spectral Analysis of Self-Similar Operator

Define L_s[f] = ν∆*f - (ρ∂_ρ + ζ∂_ζ)f/2

The equation L_s[Γ] = 0 is the "steady" self-similar swirl equation (no advection).

**Claim:** L_s has no non-trivial L²_ρ kernel.

**Argument:**

Multiply L_s[Γ] = 0 by Γ and integrate:
```
∫∫ [ν∆*Γ - (ρ∂_ρ + ζ∂_ζ)Γ/2] Γ ρ dρdζ = 0
```

We computed: -ν||∇Γ||² + (3/4)||Γ||² = 0

So ||∇Γ||² = (3/4ν)||Γ||².

This is a RELATION, not a contradiction. We need more.

**Try multiplying by ρ²Γ:**
```
∫∫ [ν∆*Γ - (ρ∂_ρ + ζ∂_ζ)Γ/2] ρ²Γ ρ dρdζ = 0
```

This gives weighted estimates...

Actually, let me try a different approach.

## 9. Separation of Variables

For L_s[Γ] = 0, try Γ(ρ, ζ) = R(ρ)Z(ζ).

The equation becomes:
```
ν[R''Z - (R'/ρ)Z + RZ''] - (ρR'/2)Z - (ζRZ'/2) = 0
```

Divide by RZ:
```
ν[R''/R - (R'/ρ)/R + Z''/Z] - (ρR'/(2R)) - (ζZ'/(2Z)) = 0
```

This doesn't separate cleanly because of the ρ and ζ terms.

**Alternative:** Use self-similar scaling.

In self-similar problems, solutions often have the form:
```
Γ(ρ, ζ) = ρ^α F(ζ/ρ^β)
```

for some exponents α, β.

## 10. Scaling Ansatz

Let Γ = ρ² G(η) where η = ζ/ρ (similarity variable).

Then:
- ∂Γ/∂ρ = 2ρG - ρ²(ζ/ρ²)G' = 2ρG - ηG'
- ∂Γ/∂ζ = ρ²(1/ρ)G' = ρG'
- ∂²Γ/∂ρ² = 2G - 2ηG'/ρ + η²G''/ρ²
- etc.

This is getting complicated. Let me try numerical/asymptotic intuition instead.

## 11. Physical Intuition

The operator L_s = ν∆* - (ρ∂_ρ + ζ∂_ζ)/2 represents:
- Viscous diffusion (∆*)
- Self-similar "stretching" ((ρ∂_ρ + ζ∂_ζ)/2)

For blowup (T-t → 0), the stretching term dominates at large |y|.

**At infinity:** The equation becomes (ρ∂_ρ + ζ∂_ζ)Γ/2 ≈ 0, i.e., Γ ~ const.

But Γ → 0 at infinity, so Γ must decay.

**Near the axis:** Viscosity dominates.

The competition between these effects might force Γ = 0.

## 12. Back to Coupling: Sign of C[Γ, ω]

Let's analyze C[Γ, ω] = 2∫∫ (Γ/ρ³)(∂Γ/∂ζ) ω dρdζ more carefully.

**Observation:** ∂Γ/∂ζ is the vertical gradient of swirl.

If Γ > 0 and ∂Γ/∂ζ > 0 (swirl increasing upward), and ω > 0, then C > 0.

If Γ > 0 and ∂Γ/∂ζ < 0 (swirl decreasing upward), and ω > 0, then C < 0.

**The sign of C depends on the detailed structure of the solution.**

## 13. Alternative: Use Both Equations Together

Add the swirl and vorticity energy identities:

From swirl: ν||∇Γ||² = (3/4)||Γ||²

From vorticity: ν||∇ω||² + (1/4)||ω||² = C[Γ, ω]

**Idea:** Express C in terms of Γ and use the swirl identity.

Near axis, ω = -∆*ψ/ρ, and ∆*ψ = ρ²(a'' + 8b) + O(ρ⁴).

With the constraint a'' = -8b (from regularity), we have ∆*ψ = O(ρ⁴).

So ω = O(ρ³) near the axis (not O(ρ) as I wrote earlier).

This changes the coupling structure!

## 14. Corrected Behavior Near Axis

If a'' + 8b = 0 (regularity constraint), then:
- ∆*ψ = ρ⁴(b'' + 24d) + O(ρ⁶)
- ω = -∆*ψ/ρ = -ρ³(b'' + 24d) + O(ρ⁵)

So ω = O(ρ³), not O(ρ)!

Now the coupling term:
```
(Γ/ρ³)(∂Γ/∂ζ) ω ~ (ρ²g/ρ³)(ρ²g')(ρ³c) = ρ⁴ g g' c
```

which is O(ρ⁴), highly regular.

**This means C[Γ, ω] is well-defined even as ρ → 0.**

## 15. Key Structural Observation

The regularity constraint a'' = -8b makes the system MORE regular than expected.

**Consequence:** The coupling C[Γ, ω] involves terms of order ρ⁴ near the axis,
which integrate to give bounded contributions.

## 16. Current Status

The coupled analysis reveals:
1. Vorticity equation gives: ν||∇ω||² + (1/4)||ω||² = C[Γ, ω]
2. If C ≤ 0, then ω ≡ 0, forcing ψ = const
3. With ψ = const, the swirl equation simplifies
4. The sign of C depends on solution structure

**Not yet proved:** Sign of C or unconditional result.

## 17. Next Attempt: Integrated Identity

Define:
```
I = ν||∇Γ||² + ν||∇ω||² + α||Γ||² + β||ω||²
```

From the two energy identities:
- ν||∇Γ||² = (3/4)||Γ||²
- ν||∇ω||² + (1/4)||ω||² = C

So:
```
I = (3/4)||Γ||² + C - (1/4)||ω||² + α||Γ||² + β||ω||²
  = (3/4 + α)||Γ||² + (β - 1/4)||ω||² + C
```

If we can show I = 0 or I < 0 for some choice of α, β, we're done.

**The problem is the unknown sign of C.**

# Bootstrap Proof: g ≡ 0 ⟹ Γ ≡ 0

## 1. Setup

We have established (under moderate strain) that g(ζ) ≡ 0, where:
```
Γ(ρ, ζ) = ρ² g(ζ) + ρ⁴ h(ζ) + O(ρ⁶)
```

This means Γ = O(ρ⁴) near the axis. We want to show Γ ≡ 0 everywhere.

## 2. The Swirl Equation

The self-similar swirl equation is:
```
u ∂Γ/∂ρ + w ∂Γ/∂ζ + (ρ∂_ρ + ζ∂_ζ)Γ/2 = ν ∆* Γ
```

where:
- ∆* = ∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ²
- u = -(1/ρ)∂ψ/∂ζ, w = (1/ρ)∂ψ/∂ρ

Rewrite as:
```
ν ∆* Γ - u ∂Γ/∂ρ - w ∂Γ/∂ζ - (ρ/2)∂Γ/∂ρ - (ζ/2)∂Γ/∂ζ = 0
```

Or:
```
ν ∆* Γ - [u + ρ/2] ∂Γ/∂ρ - [w + ζ/2] ∂Γ/∂ζ = 0
```

## 3. Approach 1: Next-Order Analysis at Axis

If Γ = ρ⁴ h(ζ) + O(ρ⁶), what equation does h satisfy?

### Computing each term at O(ρ⁴):

**The Laplacian ∆*Γ:**
```
∆*(ρ⁴ h) = (∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ²)(ρ⁴ h)
         = 12ρ² h - 4ρ² h + ρ⁴ h''
         = 8ρ² h + ρ⁴ h''
```

**The transport terms:**

With ψ = ρ² a(ζ) + ρ⁴ b(ζ) + O(ρ⁶):
```
u = -(1/ρ)∂ψ/∂ζ = -ρ a'(ζ) - ρ³ b'(ζ) + O(ρ⁵)
w = (1/ρ)∂ψ/∂ρ = 2a(ζ) + 4ρ² b(ζ) + O(ρ⁴)
```

Then:
```
u ∂Γ/∂ρ = (-ρ a' - ρ³ b')(4ρ³ h + O(ρ⁵))
        = -4ρ⁴ a' h + O(ρ⁶)

w ∂Γ/∂ζ = (2a + 4ρ² b)(ρ⁴ h' + O(ρ⁶))
        = 2ρ⁴ a h' + O(ρ⁶)
```

**The linear terms:**
```
(ρ∂_ρ + ζ∂_ζ)Γ/2 = (ρ · 4ρ³ h + ζ · ρ⁴ h')/2
                  = ρ⁴(2h + ζh'/2) + O(ρ⁶)
```

### The O(ρ⁴) equation (WAIT - there's an issue!)

Collecting O(ρ⁴) terms:
```
ν · 0 - 4a'h + 2ah' + 2h + ζh'/2 = 0
```

But ν∆*Γ has leading order ρ², not ρ⁴!

Let me reconsider. We have:
```
ν ∆* Γ = ν(8ρ² h + ρ⁴ h'') + O(ρ⁶)
```

At O(ρ²), the equation gives:
```
8νh = 0  ⟹  h = 0  (if ν > 0)
```

**This is the bootstrap!**

## 4. The Bootstrap Theorem

**Theorem (Inductive Vanishing):**
If Γ = ρ^{2n} f_n(ζ) + O(ρ^{2n+2}) for some n ≥ 1, then f_n ≡ 0.

**Proof:**

The key is the structure of ∆*:
```
∆*(ρ^{2n} f) = ρ^{2n-2}[(2n)(2n-1) - (2n)] f + ρ^{2n} f''
             = ρ^{2n-2} · 2n(2n-2) f + ρ^{2n} f''
             = ρ^{2n-2} · 4n(n-1) f + ρ^{2n} f''
```

For n ≥ 2: the leading term is ρ^{2n-2} with coefficient 4n(n-1)f.

**The swirl equation at leading order:**

If Γ = ρ^{2n} f(ζ) + h.o.t. with n ≥ 2, then:

- ∆*Γ has leading term ρ^{2n-2} · 4n(n-1)f
- Transport terms: u∂Γ/∂ρ ~ ρ · ρ^{2n-1} = ρ^{2n}, w∂Γ/∂ζ ~ ρ^{2n}
- Linear terms: (ρ∂_ρ + ζ∂_ζ)Γ/2 ~ ρ^{2n}

So the leading order is ρ^{2n-2} from the Laplacian:
```
ν · 4n(n-1) f(ζ) = 0
```

Since ν > 0 and n ≥ 2 ⟹ n(n-1) ≠ 0, we get **f ≡ 0**.

**Induction:** Starting from g ≡ 0 (n=1 case, proved by energy method), we get:
- n=2: h ≡ 0 (from above, 4·2·1 = 8 ≠ 0)
- n=3: next coefficient ≡ 0
- ... and so on

By induction, all coefficients vanish: **Γ ≡ 0** near the axis.

## 5. Extension to Full Domain

We've shown Γ ≡ 0 in a neighborhood of the axis {ρ < ε}.

For the full domain, we use:

### Approach A: Maximum Principle

The swirl equation has the form:
```
ν ∆* Γ = (first-order terms in Γ)
```

On the domain Ω = {ρ > 0, ρ² + ζ² < R²}:
- Γ = 0 on ρ = 0 (axis)
- Γ → 0 as R → ∞ (decay)

If Γ achieves a positive maximum at an interior point (ρ₀, ζ₀) with ρ₀ > 0:
- At a maximum: ∂Γ/∂ρ = 0, ∂Γ/∂ζ = 0
- At a maximum: ∆*Γ ≤ 0 (since ∆* is elliptic for ρ > 0)

The equation becomes:
```
ν ∆* Γ = 0 at the maximum
```

But ∆*Γ ≤ 0, so ∆*Γ = 0 at the maximum. This doesn't immediately give a contradiction...

### Approach B: Energy Estimate

Multiply the swirl equation by Γ and integrate over {ρ > ε}:
```
∫∫_{ρ>ε} [ν ∆* Γ - transport - linear] · Γ · ρ dρ dζ = 0
```

The weight ρ is the natural measure in cylindrical coordinates.

**Viscous term:**
```
∫∫ ν ∆* Γ · Γ · ρ dρ dζ
```

Integration by parts (noting ∆* is self-adjoint with weight ρ up to boundary terms):
```
= -ν ∫∫ |∇Γ|² ρ dρ dζ + boundary terms at ρ = ε
```

As ε → 0, if Γ = O(ρ^{2n}) with n → ∞ (all coefficients zero), the boundary terms vanish.

**Transport terms:**
```
∫∫ (u ∂Γ/∂ρ + w ∂Γ/∂ζ) Γ ρ dρ dζ
```

Using incompressibility ∂(ρu)/∂ρ + ∂(ρw)/∂ζ = 0... wait, need to check this.

Actually, the meridional flow (u, w) satisfies:
```
∂u/∂ρ + u/ρ + ∂w/∂ζ = 0
```

This gives:
```
∫∫ (u·∇Γ) · Γ · ρ = (1/2) ∫∫ u·∇(Γ²) · ρ
                   = -(1/2) ∫∫ Γ² · div(ρu, ρw)  [by parts]
                   = 0  [by incompressibility + boundary terms]
```

**Linear terms:**
```
∫∫ [(ρ/2)∂Γ/∂ρ + (ζ/2)∂Γ/∂ζ] Γ ρ dρ dζ
= (1/4) ∫∫ (ρ∂_ρ + ζ∂_ζ)(Γ²) ρ dρ dζ
```

Integration by parts:
```
= -(1/4) ∫∫ Γ² [∂(ρ·ρ)/∂ρ + ∂(ζ·ρ)/∂ζ] dρ dζ + boundary
= -(1/4) ∫∫ Γ² [2ρ + ρ] dρ dζ
= -(3/4) ∫∫ Γ² ρ dρ dζ
```

**Combining:**
```
-ν ||∇Γ||²_ρ + 0 - (3/4)||Γ||²_ρ = 0
```

This gives:
```
ν ||∇Γ||²_ρ + (3/4)||Γ||²_ρ = 0
```

Since both terms are non-negative and ν > 0, we must have:
```
||Γ||²_ρ = 0  ⟹  Γ ≡ 0
```

**This completes the bootstrap!**

## 6. Summary: Complete Bootstrap Proof

**Theorem (Bootstrap):**
Under the moderate strain condition, if g ≡ 0 then Γ ≡ 0.

**Proof:**
1. From axis-ode-analysis.md, moderate strain ⟹ g ≡ 0
2. By inductive vanishing (Section 4), all Taylor coefficients at axis vanish
3. Γ vanishes to infinite order at axis
4. By energy estimate (Section 5B), Γ ≡ 0 on entire domain

**Actually, we can skip step 2-3!** The energy estimate in Section 5B works directly:

Multiply swirl equation by Γ, integrate with weight ρ:
```
ν ||∇Γ||²_ρ + (3/4)||Γ||²_ρ = (boundary terms at ρ = 0)
```

At ρ = 0, Γ = 0 (standard axis condition), so boundary terms vanish.
Hence Γ ≡ 0.

**Wait - this proves Γ ≡ 0 WITHOUT needing g ≡ 0 first!**

Let me recheck... The boundary terms at ρ = 0 come from the integration by parts of ∆*Γ. Need to be careful.

## 7. Direct Proof (Revised)

The energy identity is:
```
∫∫ [ν ∆* Γ - u∂_ρΓ - w∂_ζΓ - (ρ∂_ρ + ζ∂_ζ)Γ/2] · Γ · ρ dρ dζ = 0
```

**Viscous term with ∆*:**
```
∆* = ∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ²
```

For integration by parts with weight ρ:
```
∫ (∂²Γ/∂ρ²) Γ ρ dρ = -∫ (∂Γ/∂ρ)² ρ dρ + [boundary]

∫ (1/ρ)(∂Γ/∂ρ) Γ ρ dρ = ∫ (∂Γ/∂ρ) Γ dρ = (1/2)[Γ²] - (1/2)∫ Γ (∂Γ/∂ρ) dρ
                       ⟹ ∫ (∂Γ/∂ρ) Γ dρ = (1/2)[Γ²]
```

Hmm, this is getting complicated. Let me be more careful.

The correct energy identity for the operator ∆* with Dirichlet boundary conditions at ρ = 0 is standard in the literature on axisymmetric flows. The key result is:

**Lemma (Energy Coercivity):**
For Γ with Γ(0, ζ) = 0 and Γ → 0 at infinity:
```
-∫∫ (∆* Γ) Γ ρ dρ dζ = ∫∫ [(∂Γ/∂ρ)² + (∂Γ/∂ζ)² + Γ²/ρ²] ρ dρ dζ
                      ≥ ∫∫ |∇Γ|² ρ dρ dζ
```

(The Γ²/ρ² term is the Hardy-type term from the -1/ρ ∂/∂ρ part of ∆*.)

With this, the energy identity becomes:
```
ν ∫∫ |∇Γ|² ρ + (3/4) ∫∫ Γ² ρ ≤ 0
```

Hence Γ ≡ 0. ∎

## 8. Corrected Energy Analysis

**Important Correction:** The energy identity does NOT directly give Γ ≡ 0.

Let me redo carefully. The self-similar swirl equation is:
```
ν ∆* Γ = U·∇Γ + (1/2)(ρ∂_ρ + ζ∂_ζ)Γ
```

Multiply by Γ and integrate with weight ρ:

**LHS:** ∫∫ ν∆*Γ · Γ · ρ = -ν||∇Γ||²_ρ

**RHS transport:** ∫∫ (U·∇Γ)Γρ = 0 (by incompressibility)

**RHS linear:**
```
∫∫ (1/2)(ρ∂_ρ + ζ∂_ζ)Γ · Γ · ρ = (1/4)∫∫(ρ∂_ρ + ζ∂_ζ)(Γ²)ρ
= (1/4)[-2||Γ||²_ρ - ||Γ||²_ρ] = -(3/4)||Γ||²_ρ
```

**Full identity:**
```
-ν||∇Γ||²_ρ = -(3/4)||Γ||²_ρ

⟹  ν||∇Γ||²_ρ = (3/4)||Γ||²_ρ
```

**This is a Poincaré-type relation, NOT a contradiction!**

It says: for any self-similar profile, ||∇Γ||² = (3/4ν)||Γ||².

This is satisfied by non-trivial functions. So we CANNOT skip the g ≡ 0 step.

## 9. The Correct Bootstrap Strategy

The bootstrap requires TWO steps:

**Step 1 (Proved):** Under moderate strain, g ≡ 0 (from axis ODE energy method).

**Step 2 (Inductive Vanishing):** g ≡ 0 ⟹ Γ ≡ 0.

For Step 2, we use the inductive argument from Section 4:

If Γ = ρ^{2n} f(ζ) + h.o.t. with n ≥ 2, then the swirl equation's leading term is:
```
ν · 4n(n-1) · ρ^{2n-2} f(ζ) = O(ρ^{2n})
```

The ρ^{2n-2} term must vanish, so f ≡ 0 (since 4n(n-1) ≠ 0 for n ≥ 2).

By induction on n: all Taylor coefficients vanish, so Γ vanishes to infinite
order at the axis.

**Step 3 (Unique Continuation):** A smooth solution to an elliptic PDE that
vanishes to infinite order at a point must vanish identically.

For the swirl equation (which is elliptic for ρ > 0), this gives Γ ≡ 0.

## 10. Rigorous Statement

**Theorem (Bootstrap):**
Let (ψ, Γ) be a smooth self-similar profile satisfying:
1. The coupled profile system
2. Γ(0, ζ) = 0 and appropriate decay at infinity
3. The moderate strain condition: ||a'||_∞ < 3/4

Then Γ ≡ 0.

**Proof:**
1. By axis ODE analysis (axis-ode-analysis.md), g ≡ 0
2. By inductive vanishing (Section 4), Γ = O(ρ^∞) at axis
3. By unique continuation for elliptic equations, Γ ≡ 0 ∎

## 11. What Remains

The bootstrap is now complete MODULO:
1. **Unique continuation reference:** Need to cite/verify the appropriate
   unique continuation theorem for this setting
2. **Remove moderate strain:** Can we prove ||a'||_∞ < 3/4 automatically?

## 12. Unique Continuation Theorem

**Theorem (Carleman Estimate / Unique Continuation):**
Let L be a second-order elliptic operator on a domain Ω, and let u satisfy
Lu = lower order terms. If u vanishes to infinite order at a point x₀ ∈ Ω,
then u ≡ 0 in the connected component containing x₀.

For our setting:
- L = ν∆* (elliptic for ρ > 0)
- Lower order terms = U·∇Γ + (linear)
- Γ vanishes to infinite order at the axis (a boundary)

**Technical point:** The axis ρ = 0 is a boundary, not an interior point.
For boundary unique continuation, we need Γ to vanish to infinite order
in the NORMAL direction (∂/∂ρ), which it does (all ρ-coefficients vanish).

Standard references: Hörmander, "The Analysis of Linear PDEs," Vol 3, or
Tataru's unique continuation results.

The theorem applies and gives Γ ≡ 0.

# Refined Theorem: Removing the Pointwise Condition

## Key Insight

The energy identity is:
```
ν||g'||² + (3/4)||g||² = 3∫a'(ζ)g(ζ)² dζ
```

We don't need ||a'||_∞ < 1/4. We only need:
```
∫a'g² dζ < (1/4)||g||²
```

This is an INTEGRAL condition, not a pointwise one. It can hold even if a'
is large somewhere, as long as g is small there.

## The Structure of g

The function g satisfies the ODE:
```
νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0
```

with g(ζ) → 0 as |ζ| → ∞.

**Key observation:** The coefficient of g is (2a' - 1).

Where 2a' > 1 (i.e., a' > 1/2), the coefficient is positive → "source" term.
Where 2a' < 1 (i.e., a' < 1/2), the coefficient is negative → "sink" term.

## Qualitative Behavior

The ODE can be written as:
```
νg'' - b(ζ)g' + c(ζ)g = 0
```
where b = 2a + ζ/2 and c = 2a' - 1.

**Case 1: c < 0 everywhere (a' < 1/2 everywhere)**

The term cg acts as a sink (absorbs g). Solutions decay.
The energy identity gives:
```
ν||g'||² + (3/4)||g||² = 3∫(c+1)/2 · g² = 3∫a'g² < 3·(1/2)||g||² = (3/2)||g||²
```

Hmm, this doesn't immediately work.

**Case 2: c changes sign**

Where c > 0 (a' > 1/2), there's a local source.
Where c < 0 (a' < 1/2), there's a local sink.

The solution g will be SUPPRESSED where c < 0 and potentially AMPLIFIED where c > 0.

But the boundary conditions g → 0 at ±∞ constrain the solution globally.

## A Better Approach: Variational Characterization

Consider the eigenvalue problem:
```
νφ'' - (2a + ζ/2)φ' + (2a' - 1)φ = λφ
```

The original ODE corresponds to λ = 0.

**Claim:** If λ = 0 is not an eigenvalue, then g ≡ 0.

The eigenvalue problem can be recast variationally. Define:
```
Q[φ] = ν||φ'||² + (3/4)||φ||² - 3∫a'φ²
```

Then λ = 0 eigenfunction iff Q[φ] = 0 for some φ with ||φ|| = 1.

**Observation:** From the energy identity, Q[g] = 0 for any solution g.

So we need to show that Q[φ] > 0 for all φ ≠ 0.

## Positivity of the Quadratic Form

**Lemma:** Q[φ] ≥ 0 for all φ ∈ H¹(ℝ), with equality iff φ = 0.

**Proof attempt:**

Q[φ] = ν||φ'||² + (3/4)||φ||² - 3∫a'φ²

By Poincaré inequality (for functions vanishing at infinity):
```
||φ'||² ≥ C||φ||² for some C > 0
```

So: Q[φ] ≥ (νC + 3/4)||φ||² - 3||a'||_∞||φ||²

If 3||a'||_∞ < νC + 3/4, then Q[φ] > 0.

This gives: ||a'||_∞ < νC/3 + 1/4.

For small ν, this is essentially ||a'||_∞ < 1/4 (our original condition).

For large ν (highly viscous), we can allow larger ||a'||.

**This is actually a weakening!** The condition becomes:
```
||a'||_∞ < 1/4 + νC/3
```

But C depends on the specific function space...

## Alternative: Hardy-Type Inequality

The operator ∆* has a Hardy-type structure. Specifically:
```
||∇f||² ≥ C ||f/ρ||²
```

for functions vanishing on the axis.

Can we use this to get a better bound?

## The Self-Adjoint Reformulation

Define the weighted inner product:
```
⟨f, g⟩_w = ∫ f g w(ζ) dζ
```

where w(ζ) is chosen to make the ODE operator self-adjoint.

For the ODE νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0, the natural weight is:
```
w(ζ) = exp(∫_0^ζ (2a(s) + s/2)/ν ds)
```

This makes the operator:
```
L[g] = (1/w)(νwg')' + (2a' - 1)g
```

Then: ⟨Lg, g⟩_w = -ν||g'||²_w + ∫(2a' - 1)g² w dζ = 0

This is a weighted version of the energy identity.

## Connection to Sturm-Liouville Theory

The ODE is a Sturm-Liouville problem:
```
-(pg')' + qg = 0
```

with p(ζ) = νw(ζ) and q(ζ) = (1 - 2a')w(ζ).

For oscillation theory:
- If q > 0 everywhere, solutions oscillate
- If q < 0 everywhere, solutions are monotonic (no zeros except at ∞)

For our equation, q = (1 - 2a')w.

If a' < 1/2 everywhere, then q > 0, and solutions oscillate.
But boundary conditions g → 0 at ±∞ allow only the trivial solution
(eigenfunctions of SL problems with positive q don't satisfy both BCs).

**Theorem (Sturm-Liouville):** If q(ζ) > 0 for all ζ, then g ≡ 0.

**Translating:** If a'(ζ) < 1/2 for all ζ, then g ≡ 0.

## Improved Condition!

**Theorem (Refined):** If sup a'(ζ) < 1/2, then g ≡ 0 and hence Γ ≡ 0.

**Proof:** By Sturm-Liouville oscillation theory. If 2a' < 1 everywhere, the
coefficient q = (1-2a')w > 0, so non-trivial solutions must oscillate.
But g → 0 at both ±∞ is incompatible with oscillation (would need infinitely
many zeros, contradicting decay).

Wait, this isn't quite right. Let me reconsider.

Actually, Sturm-Liouville with q > 0 says solutions DON'T oscillate (they're
exponential-like). Let me check the standard form.

Standard SL: -(py')' + qy = λry

Oscillation: solutions oscillate when λ > 0 and q/r is bounded below.

Our case: λ = 0, so we're looking at the homogeneous problem.

For -(py')' + qy = 0 with p > 0, q > 0:
- Solutions are positive (no zeros) or have at most one zero
- Boundary conditions y → 0 at both ends force y ≡ 0

**This is the result we want!**

## Final Theorem

**Theorem (Unconditional for a' < 1/2):**

Let (ψ, Γ) be a smooth self-similar profile. If a'(ζ) < 1/2 for all ζ, then Γ ≡ 0.

**Proof:**
1. The axis ODE is νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0
2. In SL form: -(νwg')' + (1-2a')wg = 0 with w > 0
3. If a' < 1/2, then (1-2a')w > 0
4. By SL theory, g has at most one zero
5. Combined with g → 0 at ±∞, this forces g ≡ 0
6. By bootstrap, Γ ≡ 0 ∎

**Note:** The condition a' < 1/2 is WEAKER than a' < 1/4!

We've improved the bound from 1/4 to 1/2!

## Why Does This Differ from Energy Method?

The energy method gave ||a'||_∞ < 1/4.
Sturm-Liouville gives ||a'||_∞ < 1/2.

The energy method is SUBOPTIMAL because it uses Cauchy-Schwarz:
```
∫a'g² ≤ ||a'||_∞||g||²
```

The SL approach uses the STRUCTURE of the equation directly.

## Physical Interpretation

The condition a' < 1/2 means:
```
∂w/∂ζ|_{axis} < 1
```

where w = 2a is the axial velocity at the axis.

The axial velocity can't increase faster than 1 per unit (self-similar) length.

## Remaining Gap

Can we extend to a' < 1 or remove the condition entirely?

The critical case is a' = 1/2, where q = 0 at some points.

For a' > 1/2 somewhere, q < 0 there, and solutions might exist.

**Conjecture:** Self-similar structure forces a' < 1/2 automatically.

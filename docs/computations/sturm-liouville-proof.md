# Sturm-Liouville Proof of Improved Bound

## The Axis ODE

```
νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0
```

with g(ζ) → 0 as |ζ| → ∞.

## Conversion to Sturm-Liouville Form

Divide by ν:
```
g'' - [(2a + ζ/2)/ν]g' + [(2a' - 1)/ν]g = 0
```

Let P(ζ) = -(2a + ζ/2)/ν, Q(ζ) = (2a' - 1)/ν.

**Integrating factor:**
```
μ(ζ) = exp(∫P dζ) = exp(-(1/ν)∫(2a + ζ/2)dζ)
     = exp(-(2A(ζ) + ζ²/4)/ν)
```
where A(ζ) = ∫₀^ζ a(s)ds.

Note: μ(ζ) > 0 for all ζ.

**Multiplying by μ:**

Since (μg')' = μg'' + μ'g' = μg'' + μPg', we have:

μg'' + μPg' = (μg')'

So the equation becomes:
```
(μg')' + μQg = 0
```

Or in standard SL form:
```
-(pg')' + qg = 0
```

where:
- p(ζ) = μ(ζ) = exp(-(2A + ζ²/4)/ν) > 0
- q(ζ) = -μQ = μ(1 - 2a')/ν

## The Condition q > 0

For q(ζ) > 0, we need:
```
μ(1 - 2a')/ν > 0
```

Since μ > 0 and ν > 0, this requires:
```
1 - 2a'(ζ) > 0  ⟺  a'(ζ) < 1/2
```

## Variational Principle

The SL equation -(pg')' + qg = 0 is the Euler-Lagrange equation for:
```
J[g] = ∫_{-∞}^{∞} [p(g')² + qg²] dζ
```

**Key property:** If p > 0 and q > 0 everywhere, then J[g] > 0 for all g ≢ 0.

**Proof:**
```
J[g] = ∫ p(g')² dζ + ∫ qg² dζ ≥ ∫ qg² dζ > 0
```
since q > 0 and g ≢ 0 implies ∫qg² > 0.

## The Main Result

**Lemma:** If p > 0 and q > 0 on ℝ, the only solution to -(pg')' + qg = 0
with g ∈ H¹(ℝ) is g ≡ 0.

**Proof:**

Multiply the equation by g and integrate:
```
-∫(pg')'g dζ + ∫qg² dζ = 0
```

Integrate by parts (boundary terms vanish since g → 0 at ±∞):
```
∫p(g')² dζ + ∫qg² dζ = 0
```

Since p > 0 and q > 0:
```
∫p(g')² dζ ≥ 0
∫qg² dζ ≥ 0
```

For the sum to be zero, both integrals must be zero.

∫qg² = 0 with q > 0 implies g ≡ 0. ∎

## Application to Our Problem

**Theorem (Improved Axis Non-Existence):**

If ||a'||_∞ < 1/2, then g ≡ 0.

**Proof:**

Under the hypothesis a'(ζ) < 1/2 for all ζ:
- The SL coefficient q = μ(1 - 2a')/ν > 0
- By the Lemma, g ≡ 0 ∎

## Comparison with Energy Method

| Method | Condition |
|--------|-----------|
| Energy (Cauchy-Schwarz) | ||a'||_∞ < 1/4 |
| Sturm-Liouville | ||a'||_∞ < 1/2 |

The SL method gives a **factor of 2 improvement** by using the structure
of the ODE directly instead of applying crude estimates.

## Physical Interpretation

The condition a' < 1/2 translates to:
```
|∂w/∂ζ|_{axis}| < 1
```

where w|_{axis} = 2a(ζ) is the axial velocity on the symmetry axis.

**Meaning:** The axial velocity gradient (in self-similar units) must be
bounded by 1. The flow cannot have arbitrarily steep axial velocity gradients.

## What About a' ≥ 1/2?

If a'(ζ₀) ≥ 1/2 at some point, then q(ζ₀) ≤ 0, and the SL argument fails.

In this regime, non-trivial solutions g might exist.

**Open question:** Does the self-similar structure force a' < 1/2?

## Summary

We have proved:

**Theorem 1.1 (Improved):** Let (ψ, Γ) be a smooth self-similar profile.
If ||a'||_∞ < 1/2, then Γ ≡ 0.

This is a strict improvement over the original ||a'||_∞ < 1/4 condition.

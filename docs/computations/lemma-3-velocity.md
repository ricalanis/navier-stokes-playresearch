# Lemma 3 Attempt: Velocity → A_{m₁} Bound

**Objective:** Derive a bound on A_{m₁}(v,r) from CKN partial regularity.

---

## Statement to Prove

**Conjecture:**
```
A_{m₁}(v,r) ≤ C(m,α) [r^{h(m,α)} + E_m(v,r)^θ]
```

for some exponents making sup_{r<1} A_{m₁} bounded.

---

## A_{m₁} Definition

```
A_{m₁}(v,r) = sup_{-r² < t < 0} r^{-(2m-1)} ∫_{B(r)} |u(x,t)|² dx
```

For m ∈ (1/2, 3/5), we have m₁ = 2m-1 ∈ (0, 1/5).

---

## CKN Partial Regularity

**Theorem (CKN):** There exists ε > 0 such that if:
```
r^{-2} ∫_{Q(r)} (|u|³ + |p|^{3/2}) dz < ε
```
then u is regular at (0,0) (the center of Q(r)).

**Corollary:** The singular set S has H¹(S) = 0.

---

## Attempt: From ε-Regularity

If the origin is a regular point:
```
|u(x,t)| ≤ M  near (0,0)
```

Then:
```
∫_{B(r)} |u|² dx ≤ M² |B(r)| = C M² r³
```

So:
```
A_{m₁}(v,r) = r^{-(2m-1)} ∫_{B(r)} |u|² dx
            ≤ C M² r^{3-(2m-1)}
            = C M² r^{4-2m}
```

For m < 3/5 < 2, we have 4-2m > 4-2·0.6 = 2.8 > 0.

**Conclusion:** At regular points, A_{m₁} → 0 as r → 0.

---

## At Singular Points

If the origin is potentially singular, we cannot use the boundedness of u directly.

**Key issue:** Near a Type II singularity:
```
||u(t)||_∞ ~ (T-t)^{-α}  with α < 1
```

The velocity is blowing up, so:
```
sup_t ∫_{B(r)} |u|² dx  could diverge
```

---

## Scaling Analysis

For a self-similar Type II blowup with rate α:
```
u(x,t) ~ (T-t)^{-α} U(x/(T-t)^{α/2})
```

Near the singularity at time t = T - r²:
```
||u||_{L²(B(r))}² ~ r^{2α} r³ ||U||_{L²}²
                  = r^{3+2α} ||U||_{L²}²
```

So:
```
A_{m₁} ~ r^{-(2m-1)} r^{3+2α} = r^{4-2m+2α}
```

For A_{m₁} bounded as r → 0, need:
```
4 - 2m + 2α ≥ 0  ⟹  α ≥ m - 2
```

Since α > 0 and m < 1, this is always satisfied for α > 0.

**But:** This is for self-similar, which is ruled out by Theorems D,F.

---

## Non-Self-Similar Analysis

For non-self-similar Type II:
- Blowup profile varies with scale
- Concentration structure can be arbitrary

No general bound is available relating ||u||_{L²(B(r))} to r^β for any fixed β.

---

## Barker-Prange Concentration

**Theorem (Barker-Prange, 2021):** Near a potential Type I singularity, there is spatial concentration:
```
||u(t)||_{L²(B(r(t)))} → bounded  as t → T
```
for appropriate r(t) → 0.

For Type II, the concentration is weaker:
- Energy can spread over larger regions
- L² norm in fixed balls may not be controlled

---

## Tao's Quantitative Bounds

**Theorem (Tao):** For ||u||_{L^{3,∞}} ≤ A:
```
||D^k u|| ≤ exp(exp(...exp(A^C)...))  (k+2 exponentials)
```

This gives bounds on derivatives, but:
- Not directly on L² in balls
- Constants grow multiply-exponentially

---

## Obstacle

The fundamental issue for A_{m₁}:

1. **At regular points:** A_{m₁} → 0, bounded trivially
2. **Near singular points:** ||u||_{L²(B(r))} could grow as r → 0

The ε-regularity criterion controls:
```
r^{-2} ∫_{Q(r)} |u|³ dz
```

But A_{m₁} involves |u|² with different r-weight.

**Dimensional mismatch:** |u|³ has different scaling than |u|².

---

## Partial Result

**Lemma 3 (Conditional):** If the origin is ε-regular (i.e., the CKN criterion holds at all scales), then:
```
A_{m₁}(v,r) ≤ C r^{4-2m} → 0 as r → 0
```

**Corollary:** At all regular points (which form a set of full H¹ measure), condition (1.4) is trivially satisfied.

**The Gap:** We need to control A_{m₁} near potentially singular points, which requires additional assumptions.

---

## Conclusion

**Status:** INCOMPLETE

A_{m₁} boundedness requires control of ||u||_{L²} in balls near singularities.
This is exactly what condition (1.4) assumes.

The numerical experiments show A_{m₁} is the dominant term (~95% of total).
This aligns with the theoretical observation that A_{m₁} is the hardest to control.

---

## Summary of Lemmas

| Lemma | Quantity | Status | Difficulty |
|-------|----------|--------|------------|
| 1 | E_m (dissipation) | Bounded for smooth | Missing: singular extension |
| 2 | D_m (pressure) | ≤ f(E_m) | Solved modulo E_m |
| 3 | A_{m₁} (velocity) | Bounded at regular points | Missing: singular control |

**Bottleneck:** A_{m₁} near singularities.

---

## What Would Complete the Proof

To prove condition (1.4) automatic, we need:
```
sup_t ||u(t)||_{L²(B(r))} ≤ C r^{β}  with β > 2m-1
```
for some β > 0, uniformly as r → 0 near any point.

This is NOT known for general suitable weak solutions.

---

## References

- CKN (1982): Partial regularity, ε-criterion
- Barker-Prange (2021): Quantitative concentration near singularities
- Tao (2019): Quantitative bounds on derivatives

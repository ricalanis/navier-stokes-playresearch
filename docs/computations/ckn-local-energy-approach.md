# CKN Local Energy Approach to A_{m₁} Bound

**Date:** January 13, 2026
**Status:** ALTERNATIVE PROOF ATTEMPT

---

## The CKN Local Energy Inequality

For suitable weak solutions and smooth cutoff φ ≥ 0:

```
∫ |u|² φ dx |_{t=t₂} + 2ν ∫_{t₁}^{t₂} ∫ |∇u|² φ dx dt
≤ ∫ |u|² φ dx |_{t=t₁} + ∫_{t₁}^{t₂} ∫ |u|² (∂_t φ + ν Δφ) dx dt
  + ∫_{t₁}^{t₂} ∫ (|u|² + 2p)(u · ∇φ) dx dt
```

---

## Strategy

Choose φ = φ_r to localize to ball B(r):
- φ_r = 1 on B(r/2)
- φ_r = 0 outside B(r)
- |∇φ_r| ≤ C/r, |Δφ_r| ≤ C/r²

Then bound the RHS terms in terms of known quantities.

---

## Term-by-Term Analysis

### Setup

Let Q_r = B(r) × (-r², 0) (parabolic cylinder).
Take t₁ = -r², t₂ = 0.

### LHS: What We Want to Bound

```
LHS = ∫_{B(r/2)} |u(0)|² dx + 2ν ∫_{Q_r} |∇u|² φ_r dx dt
    ≥ ∫_{B(r/2)} |u(0)|² dx
```

This bounds ||u(0)||²_{L²(B(r/2))}.

### RHS Term 1: Initial Energy

```
∫ |u(-r²)|² φ_r dx ≤ ||u(-r²)||²_{L²(B(r))}
```

**Problem:** This requires control of ||u||_{L²} at earlier time.

For global energy bound: ||u(t)||_{L²} ≤ ||u_0||_{L²} = √(2E₀)

So: Term 1 ≤ 2E₀

### RHS Term 2: Time-Space Derivative

```
∫_{Q_r} |u|² (∂_t φ + ν Δφ) dx dt
```

Since φ_r is time-independent, ∂_t φ = 0.

```
|∫_{Q_r} |u|² ν Δφ dx dt| ≤ (ν C/r²) ∫_{Q_r} |u|² dx dt
                         ≤ (ν C/r²) × r² × ||u||²_{L^∞_t L²_x}
                         = ν C × 2E₀
```

### RHS Term 3: Convective + Pressure

```
∫_{Q_r} (|u|² + 2p)(u · ∇φ) dx dt
```

This is the HARD term. It involves:
- |u|³ (cubic nonlinearity)
- p·u (pressure-velocity coupling)

**Estimate for |u|³ term:**
```
|∫_{Q_r} |u|² (u · ∇φ) dx dt| ≤ (C/r) ∫_{Q_r} |u|³ dx dt
```

By Hölder:
```
∫_{Q_r} |u|³ dx dt ≤ (∫_{Q_r} |u|^{10/3})^{9/10} |Q_r|^{1/10}
```

This requires bounds on ||u||_{L^{10/3}(Q_r)}.

**Estimate for pressure term:**
```
|∫_{Q_r} 2p (u · ∇φ) dx dt| ≤ (C/r) ∫_{Q_r} |p||u| dx dt
```

Pressure satisfies Δp = -div(u·∇u), so ||p||_{L^{3/2}} ≤ C ||u||²_{L³}.

By Hölder:
```
∫_{Q_r} |p||u| dx dt ≤ ||p||_{L^{3/2}(Q_r)} ||u||_{L³(Q_r)}
                     ≤ C ||u||³_{L³(Q_r)}
```

---

## The CKN ε-Regularity Criterion

**Theorem (CKN):** There exists ε > 0 such that if:
```
r^{-2} ∫_{Q_r} (|u|³ + |p|^{3/2}) dx dt < ε
```
then u is regular at (0,0).

### Connection to Our Problem

The CKN criterion controls |u|³ with weight r^{-2}.
We need to control |u|² with weight r^{-(2m-1)}.

**The dimensional mismatch:**
- CKN: |u|³ / r² ~ dimension 0 (scale-invariant)
- A_{m₁}: |u|² / r^{2m-1} ~ dimension 1-2m ≈ 0.9 (NOT scale-invariant)

---

## Attempt: Bootstrap from CKN

### Near Regular Points

If the CKN criterion is satisfied (origin is regular):
- |u(x,t)| ≤ M in Q_{r/2}
- ||u||²_{L²(B(r/2))} ≤ M² |B(r/2)| = C M² r³

So:
```
A_{m₁}(r/2) = (r/2)^{-(2m-1)} ||u||²_{L²(B(r/2))} ≤ C M² r^{3-(2m-1)} = C M² r^{4-2m}
```

For m < 2: A_{m₁} → 0 as r → 0. **BOUNDED!**

### Near Singular Points

If CKN criterion fails (potential singularity):
```
r^{-2} ∫_{Q_r} |u|³ dx dt ≥ ε
```

This means:
```
∫_{Q_r} |u|³ dx dt ≥ ε r²
```

By Hölder:
```
∫_{Q_r} |u|³ ≤ ||u||_{L²(Q_r)}^{3/2} ||u||_{L^6(Q_r)}^{3/2}
```

Using Sobolev (||u||_{L^6} ≤ C ||∇u||_{L²}):
```
∫_{Q_r} |u|³ ≤ C ||u||_{L²(Q_r)}^{3/2} ||∇u||_{L²(Q_r)}^{3/2}
```

From global energy:
```
||u||_{L²(Q_r)} ≤ r × ||u||_{L^∞_t L²_x} ≤ r √(2E₀)
||∇u||_{L²(Q_r)} ≤ (E₀/ν)^{1/2} (from dissipation integral)
```

So:
```
∫_{Q_r} |u|³ ≤ C r^{3/2} E₀^{3/4} (E₀/ν)^{3/4} = C r^{3/2} E₀^{3/2} / ν^{3/4}
```

CKN failure requires:
```
r^{3/2} E₀^{3/2} / ν^{3/4} ≥ C ε r²
⟹ r^{-1/2} ≥ C ε ν^{3/4} / E₀^{3/2}
⟹ r ≤ C (E₀/ν)^3 / ε²
```

**Conclusion:** CKN can only fail for r ≤ r_* ~ (E₀/ν)³.

For r > r_*, the origin is ε-regular, and A_{m₁} is bounded!

---

## The Remaining Problem

For r ≤ r_*, we need to bound A_{m₁} differently.

At these small scales, near a potential singularity:
- The flow is NOT ε-regular
- We cannot use the regularity bound
- Must use direct estimates

### Type II Structure at Small r

For Type II with rate α:
- ||u||_∞ ~ (T-t)^{-α}
- Concentration at scale L ~ (T-t)^{2α/3}

When r ~ L (near singularity scale):
```
||u||²_{L²(B(r))} ~ ||u||_∞² × r³ ~ (T-t)^{-2α} × (T-t)^{2α} = O(1)
```

Wait, this suggests bounded L² at the concentration scale!

### Refined Estimate

At r ~ L ~ (T-t)^{2α/3}:
```
A_{m₁}(r) = r^{-(2m-1)} ||u||²_{L²(B(r))}
          ~ L^{-(2m-1)} × (constant)
          ~ (T-t)^{-(2m-1)·2α/3}
          = (T-t)^{-2α(2m-1)/3}
```

For m = 0.55: exponent = -2α(0.1)/3 = -0.067α

For α = 0.55: exponent ≈ -0.037

This is NEGATIVE, so A_{m₁}(L) GROWS as t → T!

**But:** The growth is very slow: ~ (T-t)^{-0.037}.

---

## Integrating Over Scales

### Supremum Over r

```
sup_{r < 1} A_{m₁}(r) = max{ sup_{r > r_*} A_{m₁}(r), sup_{r < r_*} A_{m₁}(r) }
```

**For r > r_*:** ε-regular, A_{m₁} bounded by regularity theory.

**For r < r_*:** Near singularity, need different bound.

### The Key Scale

The worst case is r ~ L(t) ~ (T-t)^{2α/3}.

As t → T: L → 0, and we need to check if A_{m₁}(L) stays bounded.

From above: A_{m₁}(L) ~ (T-t)^{-0.037} for α = 0.55.

This diverges (slowly) as t → T.

---

## Conclusion of CKN Approach

### What We Get

1. For r > r_* (away from singularity scale): A_{m₁} bounded by ε-regularity
2. For r ~ L (at singularity scale): A_{m₁} ~ (T-t)^{-small exponent}

### The Gap

At the critical scale r ~ L, A_{m₁} grows slowly but does grow.

The exponent -(2m-1)·2α/3 is:
- Negative for m > 1/2 and α > 0
- Small (≈ -0.04) for m ≈ 0.55, α ≈ 0.55

### What This Means

**The CKN approach does NOT prove (1.4) bounded.**

It shows A_{m₁} grows SLOWLY (weaker than any power), but doesn't prove boundedness.

---

## Final Assessment

### Approaches Tried

| Approach | Result | Gap |
|----------|--------|-----|
| Topological | Topology frozen | Stretching unbounded |
| Energy-Geometry | Length bounded | Local L² not controlled |
| CKN Local Energy | Large r bounded | Small r grows slowly |

### Common Theme

All approaches fail at the CONCENTRATION SCALE r ~ L(t).

At this scale:
- Regularity theory doesn't apply
- Energy bounds are saturated
- Topological constraints don't prevent stretching

### The Fundamental Obstruction

**The dimensional mismatch persists:**

CKN controls: r^{-2} ∫|u|³ (dimension 0)
We need: r^{-(2m-1)} ∫|u|² (dimension 1-2m ≈ 0.9)

No combination of known estimates bridges this gap.

---

## Honest Final Assessment

**The topological proof CANNOT be completed rigorously.**

The gap at Step 3 (topology → local L² bound) is fundamental.

Possible resolutions:
1. **New conservation law:** A quantity that bounds ||u||_{L²(B(r))} and is conserved
2. **Structural result:** Prove Type II concentration has special geometry
3. **New inequality:** Directly relate A_{m₁} to known quantities

None of these currently exist in the mathematical literature.

**The gap (1/2, 3/5) remains open.**

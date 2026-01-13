# Lemma 1 Attempt: Energy → E_m Bound

**Objective:** Derive a bound on E_m(v,r) from global energy estimates.

---

## Statement to Prove

**Conjecture:** For suitable weak solutions with initial energy E₀ = ||u₀||²_{L²}/2:

```
E_m(v,r) ≤ C(m) r^{f(m)} E₀ / ν
```

for some f(m) > m making sup_{r<1} E_m bounded.

---

## Known Estimates

### Global Energy Inequality

For suitable weak solutions:
```
||u(t)||²_{L²} + 2ν ∫₀ᵗ ||∇u(s)||²_{L²} ds ≤ ||u₀||²_{L²}
```

Implies:
```
∫₀^∞ ||∇u(t)||²_{L²} dt ≤ E₀/ν
```

### Local Energy Inequality (CKN)

For suitable weak solutions and smooth cutoff φ ≥ 0:
```
∫ |u|² φ dx |_{t₂} + 2ν ∫∫ |∇u|² φ dx dt
≤ ∫ |u|² φ dx |_{t₁} + ∫∫ |u|² (∂_t φ + ν Δφ) dx dt
  + ∫∫ (|u|² + 2p)(u · ∇φ) dx dt
```

---

## Analysis

### E_m Definition

```
E_m(v,r) = r^{-m} ∫_{Q(r)} |∇v|² dz
         = r^{-m} ∫_{-r²}^0 ∫_{B(r)} |∇u|² dx dt
```

### Attempt 1: Direct from Global Energy

Global bound gives:
```
∫_{Q(r)} |∇u|² dz ≤ ∫_{-r²}^0 ||∇u||²_{L²} dt ≤ r² · (E₀/ν) / T_total
```

This doesn't give a useful bound because T_total could be arbitrarily large.

### Attempt 2: From Local Energy Inequality

Choose φ_r = smooth cutoff supported in B(2r) with φ_r = 1 on B(r).

Then:
```
∫_{B(r)} |u|² dx + 2ν ∫_{-r²}^0 ∫_{B(r)} |∇u|² dx dt
≤ ∫_{B(2r)} |u(-r²)|² dx + C₁ r^{-2} ∫_{Q(2r)} |u|² dz
  + C₂ ∫_{Q(2r)} (|u|² + 2|p|)|u|/r dz
```

### Estimate for Dissipation

```
2ν ∫_{Q(r)} |∇u|² dz ≤ ||u(-r²)||²_{L²(B(2r))} + error terms
```

The error terms involve:
- |u|² over Q(2r)
- |p||u| over Q(2r)

---

## Obstacle

The key difficulty: **Local energy inequality gives bounds involving |u|² and |p|, not directly in terms of initial energy E₀**.

To close the argument, we would need:
```
||u(-r²)||²_{L²(B(r))} ≤ C r^{α} E₀
```
for some α > 0, uniformly as r → 0.

This is NOT automatic for general suitable weak solutions near a potential singularity.

---

## Partial Result

For SMOOTH solutions (before any potential blowup):
```
E_m(v,r) = r^{-m} ∫_{Q(r)} |∇u|² dz
         ≤ r^{-m} · r² · sup_{t∈[-r²,0]} ||∇u||²_{L²}
         = r^{2-m} · sup_t ||∇u||²_{L²}
```

If ||∇u||_{L²} stays bounded (which it does for smooth solutions), then:
```
E_m(v,r) ≤ C r^{2-m}
```

Since m < 3/5 < 2, we have 2-m > 0, so:
```
sup_{r<1} E_m(v,r) ≤ C < ∞
```

**This works for smooth solutions but doesn't extend to the singular limit.**

---

## Required Mathematics

To prove E_m bounded automatically near a singularity, we need one of:

1. **Concentration control:** Show that ||∇u||_{L²(B(r))} cannot grow faster than r^{-α} for some α < 2-m
2. **Parabolic regularity:** Show that local energy controls spatial concentration
3. **Self-improvement:** Bootstrap from ε-regularity to full regularity

None of these are currently established for Type II behavior.

---

## Conclusion

**Status:** INCOMPLETE

The energy bound for E_m works for smooth solutions but we cannot extend it to the singular limit without additional assumptions.

The gap is exactly what Seregin assumes in condition (1.4).

---

## References

- CKN (1982): Original local energy inequality
- Escauriaza-Seregin-Šverák (2003): L^{3,∞} endpoint regularity
- Our numerical experiments: E_m bounded in all tested cases

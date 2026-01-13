# Energy Balance Approach to Cascade Constraint

**Date:** January 13, 2026
**Status:** RIGOROUS ATTEMPT - ITERATION 16

---

## Goal

Use the NS energy balance equation to derive rigorous constraints on the cascade concentration factor f.

---

## Part 1: Scale-by-Scale Energy Balance

### 1.1 Setup

Define energy at scale k (in ball B(r_k) where r_k = 2^{-k}):
```
E_k = ||u||²_{L²(B(r_k))}
```

For cascade: E_k = f^k E_0 where f ∈ (0,1).

### 1.2 Local Energy Equation

From NS: ∂_t(|u|²/2) + ∇·(u |u|²/2) + u·∇p = ν Δ(|u|²/2) - ν|∇u|²

Integrating over B(r_k):
```
dE_k/dt = -∫_{∂B(r_k)} [u|u|²/2 + pu] · n dS - ν||∇u||²_{L²(B(r_k))} + ν∫_{∂B(r_k)} ∂_n(|u|²/2) dS
```

### 1.3 Flux Terms

Define:
- F_k = ∫_{∂B(r_k)} [u|u|²/2 + pu] · n dS (energy flux OUT of B(r_k))
- D_k = ν||∇u||²_{L²(B(r_k))} (dissipation in B(r_k))
- S_k = ν∫_{∂B(r_k)} ∂_n(|u|²/2) dS (viscous surface term)

Then: dE_k/dt = -F_k - D_k + S_k

### 1.4 In Shell S_k = B(r_k) \ B(r_{k+1})

Energy in shell:
```
e_k = E_k - E_{k+1} = (1-f) f^k E_0
```

Energy balance in shell:
```
de_k/dt = (dE_k/dt) - (dE_{k+1}/dt)
        = -F_k + F_{k+1} - (D_k - D_{k+1}) + (S_k - S_{k+1})
        = T_k^{in} - T_k^{out} - d_k + s_k
```

where:
- T_k^{in} = F_{k+1} (flux into shell from larger r)
- T_k^{out} = F_k (flux out of shell to smaller r)
- d_k = D_k - D_{k+1} (dissipation in shell)
- s_k = S_k - S_{k+1} (viscous surface contribution)

---

## Part 2: Estimating the Flux

### 2.1 Kinetic Energy Flux

```
F_k^{kinetic} = ∫_{∂B(r_k)} u|u|²/2 · n dS
```

By Hölder:
```
|F_k^{kinetic}| ≤ ||u||_{L³(∂B(r_k))} · ||u||²_{L⁶(∂B(r_k))}
```

Using trace inequalities:
```
||u||_{L³(∂B(r_k))} ≤ C [||u||_{L³(B(r_k))} + r_k ||∇u||_{L³(B(r_k))}]
```

### 2.2 Pressure Flux

```
F_k^{pressure} = ∫_{∂B(r_k)} pu · n dS
```

Pressure satisfies: -Δp = ∂_i u_j ∂_j u_i

So: ||p||_{L^{3/2}} ≤ C ||u||²_{L³}

And:
```
|F_k^{pressure}| ≤ ||p||_{L^{3/2}(∂B(r_k))} ||u||_{L³(∂B(r_k))}
                ≤ C ||u||²_{L³} ||u||_{L³(∂B(r_k))}
```

### 2.3 Combined Flux Estimate

```
|F_k| ≤ C ||u||³_{L³(B(r_k) vicinity)} ≤ C ||u||³_{L³(S_k)} + smaller
```

For cascade with ||u||_{L²(S_k)} ~ (1-f)^{1/2} f^{k/2} E_0^{1/2}:

Using ||u||_{L³} ≤ ||u||_{L²}^{1/2} ||u||_{L⁶}^{1/2} ≤ C ||u||_{L²}^{1/2} ||∇u||_{L²}^{1/2}:
```
||u||_{L³(S_k)} ≤ C (f^{k/2} E_0^{1/2})^{1/2} (f^{k/2} E_0^{1/2} / r_k)^{1/2}
              = C f^{k/2} E_0^{1/2} / r_k^{1/2}
              = C (2^{1/2} f)^{k/2} E_0^{1/2}
```

Therefore:
```
|F_k| ≤ C ((2^{1/2} f)^{k/2} E_0^{1/2})³ = C (2^{3/2} f^{3/2})^{k/2} E_0^{3/2}
      = C (2^{3/4} f^{3/4})^k E_0^{3/2}
```

### 2.4 For Cascade Sustainability

For stationary cascade: de_k/dt = 0, so T_k^{in} = T_k^{out} + d_k.

This requires flux balance: F_{k+1} - F_k = d_k (ignoring surface terms).

From above:
```
|F_{k+1} - F_k| ≤ |F_{k+1}| + |F_k| ≤ C (2^{3/4} f^{3/4})^k E_0^{3/2} (1 + 2^{-3/4} f^{-3/4})
```

And:
```
d_k ~ ν ||∇u||²_{L²(S_k)} ~ ν e_k / r_k² ~ ν (4f)^k (1-f) E_0
```

### 2.5 Flux-Dissipation Balance

For cascade: |F_{k+1} - F_k| ~ d_k requires:
```
(2^{3/4} f^{3/4})^k E_0^{3/2} ~ ν (4f)^k (1-f) E_0
```

Taking ratio:
```
(2^{3/4} f^{3/4})^k / (4f)^k ~ ν (1-f) E_0^{-1/2}
(2^{-5/4} f^{-1/4})^k ~ ν (1-f) E_0^{-1/2}
```

As k → ∞:
- If 2^{-5/4} f^{-1/4} > 1, i.e., f < 2^{-5}, LHS → ∞ (flux dominates)
- If 2^{-5/4} f^{-1/4} < 1, i.e., f > 2^{-5} ≈ 0.031, LHS → 0 (dissipation dominates)

**For f > 0.031, dissipation dominates flux at small scales.**

---

## Part 3: Interpretation

### 3.1 What This Means

If f > 0.031:
- Dissipation in each shell exceeds net flux through that scale
- Energy is dissipated faster than it can cascade down
- **Cascade cannot be sustained to infinitely small scales**

### 3.2 But This Doesn't Constrain f < 1

The condition f > 0.031 is satisfied for most f ∈ (0,1).

This means:
- For f ∈ (0.031, 1): dissipation dominates at small k
- Cascade terminates at some scale k_max
- Below k_max: no further concentration

### 3.3 Relating to Our Goal

We need f < 2^{1-2m} ≈ 0.93 for A_{m₁} bounded.

The flux-dissipation analysis shows:
- For f > 0.031: cascade terminates
- **But cascade could still exist for k < k_max**
- This doesn't rule out f ∈ (0.031, 0.93)

---

## Part 4: Refined Analysis - Finding k_max

### 4.1 Cascade Termination Scale

The cascade continues while flux exceeds dissipation:
```
|F_k| ≥ d_k
```

From Part 2:
```
(2^{3/4} f^{3/4})^k E_0^{3/2} ≥ ν (4f)^k (1-f) E_0
```

This requires:
```
(2^{-5/4} f^{-1/4})^k ≥ ν (1-f) E_0^{-1/2}
```

For f > 2^{-5}: LHS decreases with k. Cascade ends when LHS = RHS:
```
k_max = log[ν(1-f)E_0^{-1/2}] / log[2^{5/4} f^{1/4}]
```

### 4.2 Termination Scale r_max

```
r_max = 2^{-k_max} = (ν(1-f)E_0^{-1/2})^{1/log_2(2^{5/4}f^{1/4})}
```

For f ≈ 0.5, ν = 0.001, E_0 = 1:
```
k_max ≈ log(0.0005) / log(0.84) ≈ 43
r_max ≈ 2^{-43} ≈ 10^{-13}
```

### 4.3 Implications

The cascade can extend to extremely small scales (r ~ 10^{-13}) before termination!

This is because:
- Dissipation is weak at large scales
- Flux can transport energy through many decades
- Termination happens very late in the cascade

**The cascade termination doesn't help for our bound.**

---

## Part 5: Alternative - Time-Dependent Cascade

### 5.1 Non-Stationary Analysis

Near singularity at T, the cascade is NOT stationary:
- Active scales: r > L(t) ~ (T-t)^{2α/3}
- At time t: k_active < k_max(t) = -log(L(t))/log(2)

### 5.2 Time Evolution of E_k

For k < k_active: cascade dynamics
For k > k_active: E_k ~ r_k³ (smooth filling)

At time t:
```
E_k(t) ~ f^k E_0  for k < k_active(t)
E_k(t) ~ r_k³ E_0 / L(t)³  for k > k_active(t)
```

### 5.3 Total Energy

```
E_0 = Σ_k e_k = Σ_{k < k_active} (1-f) f^k E_0 + Σ_{k > k_active} [E_k(t) - E_{k+1}(t)]
```

The first sum: (1-f) E_0 Σ_{k=0}^{k_active-1} f^k = E_0 (1 - f^{k_active})

As k_active → ∞ (t → T): this → E_0.

**Energy conservation is satisfied for any f ∈ (0,1).**

---

## Part 6: Conclusion

### 6.1 What We Found

The NS energy balance shows:
1. Flux-dissipation balance constrains cascade dynamics
2. For f > 0.031: cascade eventually terminates (dissipation wins)
3. But termination scale can be extremely small (r ~ 10^{-13})
4. Energy conservation satisfied for any f ∈ (0,1)

### 6.2 Why This Doesn't Close the Gap

The energy balance doesn't constrain f to be < 2^{1-2m} ≈ 0.93.

The constraint f > 0.031 (from flux-dissipation) is:
- Too weak (we need upper bound, not lower)
- The wrong direction

### 6.3 The Fundamental Issue

Energy is a global quantity. Local constraints like A_{m₁} require:
- Local energy distribution bounds
- Not just global energy conservation

**The NS energy balance is too coarse to constrain local L² norms.**

---

## Part 7: Final Assessment

### What Would Work

1. **Local monotone quantity:** Find Q(r) monotone with r, controlling ||u||_{L²(B(r))}
2. **Structural constraint:** Prove Type II has specific geometry limiting cascade
3. **New flux identity:** Find refined flux that constrains f directly

### Status

**PROOF NOT COMPLETE**

The energy balance approach cannot constrain the cascade factor f < 1.

The gap (1/2, 3/5) remains open.

---

## Summary Table

| Approach | Result | Status |
|----------|--------|--------|
| Carleman + CKN | Works under Hypothesis H | Conditional |
| Coherent cascade | Requires f >> 1 | Heuristic |
| Incoherent cascade | Terminates at r_d | Heuristic |
| Dissipation bound | f < 2^{3/(2α)-2} > 1 | No constraint |
| Energy balance | f > 0.031 (wrong direction) | No constraint |
| Flux-dissipation | Cascade terminates at r ~ 10^{-13} | Too late to help |

**All approaches fail to prove f < 0.93 rigorously.**

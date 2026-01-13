# Quantitative Carleman Approach to Condition (1.4)

**Date:** January 13, 2026
**Reference:** arXiv:2510.20757 (Quantitative classification of singular solutions)
**Status:** PROPOSED APPROACH - NOT YET PROVEN

---

## The Key Insight

The paper arXiv:2510.20757 provides **quantitative lower bounds** near potential blow-up times using:
1. Recursive Carleman inequality arguments
2. Careful bookkeeping to avoid exponential losses
3. Physical space methods (not Fourier)
4. α-dependent tracking through all estimates

**Why this matters:** Our gap comes from dimensional mismatch. Carleman methods work in physical space and can track explicit dependence on the blowup rate α.

---

## The Dimensional Gap We're Bridging

**Current obstruction:**
- CKN criterion: r^{-2}∫_{Q_r} |u|³ (dimension 0, scale-invariant)
- Seregin A_{m₁}: r^{-(2m-1)}∫_{B_r} |u|² (dimension 1-2m ≈ 0.9)

**Why interpolation fails:**
- Hölder/Gagliardo-Nirenberg give wrong direction
- Missing ½ derivative gap between L² and L³

**Carleman advantage:**
- Works with weighted exponential multipliers
- Can bridge different spatial scalings
- Explicit constant tracking

---

## Proposed Strategy

### Step 1: Apply CKN for Large Scales (r > r_*)

For r > r_*(E₀, ν) = C(E₀/ν)³, the CKN ε-regularity criterion gives:
```
r^{-2}∫_{Q_r} |u|³ ≤ ε  ⟹  |u| ≤ M in Q_{r/2}
```

This bounds A_{m₁}(r) for r > r_* via:
```
A_{m₁}(r) = r^{-(2m-1)} ||u||²_{L²(B_r)} ≤ M² r^{4-2m}
```

For m < 2: A_{m₁} → 0 as r → 0. **BOUNDED!**

### Step 2: Quantitative Carleman for Small Scales (r < r_*)

For r ~ L(t) ~ (T-t)^{2α/3} (concentration scale), use Carleman:

**Key estimate (proposed):**
```
||u||_{L²(B_r)}² ≤ C(α) exp(λ/r²) ∫_{B_{2r}} |u|² ψ_λ dx
```

where ψ_λ is the Carleman weight with parameter λ.

**Tracking α-dependence:**
- C(α) depends polynomially on 1/(α - 1/2)
- Blows up only as α → 1/2 (Type I boundary)
- For α ∈ (1/2, 3/5): C(α) remains bounded

### Step 3: Energy + Carleman Combination

**Global energy bound:**
```
||u(t)||_{L²}² ≤ ||u_0||_{L²}² = 2E_0
```

**Localized Carleman:**
```
||u||_{L²(B_r)}² ≤ C(α) r^{2+δ(α)} ||u||_{L²}² / r_*^{2+δ(α)}
```

where δ(α) > 0 for α > 1/2.

**Conclusion:**
```
A_{m₁}(r) = r^{-(2m-1)} ||u||²_{L²(B_r)}
         ≤ C(α) r^{3+δ(α)-2m} E_0 / r_*^{2+δ(α)}
         = C'(α, E_0, ν) r^{3+δ(α)-2m}
```

For m ∈ (1/2, 3/5) and δ(α) small: 3 + δ - 2m > 1.9 + δ > 0.

**Therefore A_{m₁}(r) → 0 as r → 0 ⟹ bounded!**

---

## The Carleman Inequality Framework

### Standard Carleman for Parabolic Equations

For u solving ∂_t u - νΔu = f:
```
∫ e^{2λφ} (λ³|u|² + λ|∇u|²) dx dt ≤ C ∫ e^{2λφ} |f|² dx dt
```

where φ(x,t) is a suitable weight function.

### Adaptation to Navier-Stokes

The NS nonlinearity u·∇u requires:
1. Treating it as a source term f = -u·∇u - ∇p
2. Using pressure estimates ||p||_{L^{3/2}} ≤ C||u||²_{L³}
3. Bootstrapping with regularity gained

**Key technical challenge:** Tracking constants through the iteration

### The Barker-Prange Quantitative Framework

From arXiv:2510.20757's methodology:
1. Start with improved energy estimates
2. Apply Carleman with explicit λ-dependence
3. Iterate **forward** in time (unusual!)
4. Avoid exponential losses via careful bookkeeping

---

## What Needs to Be Proven

### Lemma A (Carleman-Local Energy)

For suitable weak solutions near potential Type II singularity:
```
||u||_{L²(B_r)} ≤ C(α, E_0, ν) r^{β(α)} ||∇u||_{L²(B_{2r})}
```

where β(α) > (2m-1)/2 for m ∈ (1/2, 3/5).

### Lemma B (Dissipation Localization)

```
||∇u||_{L²(B_r)}² ≤ C(α) r^{γ(α)} ||∇u||_{L²}² + lower order
```

where γ(α) > 0 for α > 1/2.

### Main Theorem (Conditional)

**Theorem:** If Lemmas A and B hold with explicit α-dependence, then condition (1.4) is satisfied for α ∈ (1/2, 3/5).

**Proof sketch:**
1. A_{m₁}(r) ≤ r^{-(2m-1)} C r^{2β(α)} ||∇u||²_{L²(B_{2r})}
2. Apply Lemma B to bound ||∇u||_{L²(B_{2r})}
3. Sum over dyadic scales
4. Conclude sup_r A_{m₁}(r) < ∞

---

## Comparison with Failed Approaches

| Approach | Why it failed | Why Carleman might work |
|----------|---------------|------------------------|
| Hölder interpolation | Wrong direction | Exponential weights flip direction |
| CKN alone | Only works r > r_* | Carleman extends to r ~ L |
| Energy methods | Global, not local | Localized via weights |
| Topology | Stretching unbounded | Carleman bounds local L² |

---

## Implementation Plan

### Phase 1: Verify Framework
1. Study arXiv:2510.20757 in detail
2. Identify the key Carleman estimate used
3. Check if it applies to our weighted norms

### Phase 2: Derive Lemmas A and B
1. Adapt Barker-Prange estimates to our setting
2. Track α-dependence explicitly
3. Verify constants remain finite for α ∈ (1/2, 3/5)

### Phase 3: Combine with CKN
1. Split r > r_* (CKN) and r < r_* (Carleman)
2. Match at r = r_*
3. Conclude (1.4) bounded

---

## Assessment

### Likelihood of Success

**MODERATE-HIGH**

**For:**
- Carleman methods have succeeded on related problems
- arXiv:2510.20757 shows quantitative bounds are achievable
- Physical space avoids dimensional mismatch

**Against:**
- NS nonlinearity complicates Carleman application
- Constant tracking through iteration is hard
- May require new Carleman estimates

### Key Technical Risk

The Carleman estimate must give:
```
||u||_{L²(B_r)} ≤ C r^{β}  with β > (2m-1)/2 ≈ 0.05
```

This is a **very small** positive exponent. Any logarithmic losses could destroy it.

---

## Conclusion

**The quantitative Carleman approach is the most promising path to proving condition (1.4).**

It circumvents the dimensional mismatch by:
1. Working in physical space with explicit weights
2. Tracking α-dependence through estimates
3. Using recursive iteration with careful bookkeeping

**Next step:** Study arXiv:2510.20757's full text for the exact Carleman estimates used.

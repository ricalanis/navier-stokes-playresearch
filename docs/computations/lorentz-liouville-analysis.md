# Lorentz Spaces and Liouville-Type Theorems for Extending Seregin's Framework

## Overview

This document analyzes the role of Lorentz spaces L^{p,q} in extending Liouville-type theorems for ancient Euler solutions, building on Seregin's Type II blowup framework. The critical space L^{3,∞} (weak-L^3) plays a central role because it is the largest scale-invariant space where self-similar profiles are dimensionally consistent.

---

## 1. Lorentz Spaces L^{p,q}: Foundations

### 1.1 Definition via Distribution Function

For a measurable function f on R^3, the **distribution function** is:

```
d_f(λ) = |{x ∈ R^3 : |f(x)| > λ}|
```

The **decreasing rearrangement** is:

```
f*(t) = inf{λ > 0 : d_f(λ) ≤ t}
```

The **Lorentz space** L^{p,q}(R^3) is defined by the quasi-norm:

```
||f||_{L^{p,q}} = || t^{1/p} f*(t) ||_{L^q(dt/t)}
```

Explicitly:

- For q < ∞:
  ```
  ||f||_{L^{p,q}}^q = (q/p) ∫_0^∞ [t^{1/p} f*(t)]^q (dt/t)
                    = (q/p) ∫_0^∞ t^{q/p - 1} f*(t)^q dt
  ```

- For q = ∞:
  ```
  ||f||_{L^{p,∞}} = sup_{t > 0} t^{1/p} f*(t) = sup_{λ > 0} λ · d_f(λ)^{1/p}
  ```

### 1.2 Key Special Cases

| Space | Definition | Characterization |
|-------|------------|------------------|
| L^{p,p} | Standard Lorentz | = L^p (standard Lebesgue) |
| L^{p,∞} | Weak-L^p | d_f(λ) ≤ C/λ^p |
| L^{p,1} | Strong Lorentz | Strongest in the L^{p,q} family |

**Critical for NS:** L^{3,∞} = weak-L^3, where:
```
||f||_{L^{3,∞}} = sup_{λ > 0} λ · |{x : |f(x)| > λ}|^{1/3} < ∞
```

Equivalently: |{x : |f(x)| > λ}| ≤ C/λ^3 for all λ > 0.

### 1.3 Embeddings

For fixed p, the Lorentz scale is ordered by the secondary index:

```
L^{p,q_1} ⊂ L^{p,q_2}  whenever  q_1 < q_2
```

The inclusion is strict. In particular:
```
L^{3,1} ⊂ L^3 = L^{3,3} ⊂ L^{3,q} ⊂ L^{3,∞}  for any 3 < q < ∞
```

**Significance:** L^{3,∞} is the largest space in this family, containing functions that "just miss" being in L^3.

### 1.4 Scaling Property

Under the NS-critical rescaling f_λ(x) = f(λx):

```
||f_λ||_{L^{p,q}(R^3)} = λ^{-3/p} ||f||_{L^{p,q}(R^3)}
```

**For p = 3:** ||f_λ||_{L^{3,q}} = λ^{-1} ||f||_{L^{3,q}}

This scaling matches the self-similar ansatz:
```
u(x,t) = (T-t)^{-1/2} U(x/√(T-t))
```
where |U(y)| ~ |y|^{-1} is consistent with U ∈ L^{3,∞}.

---

## 2. The ESS Result in L^{3,∞}

### 2.1 Statement (Escauriaza-Seregin-Sverak 2003)

**Theorem (ESS):** Let u be a suitable weak solution of the 3D Navier-Stokes equations on R^3 × (0,T) with

```
u ∈ L^∞((0,T); L^{3,∞}(R^3))
```

Then u is smooth up to time T (i.e., the singularity is removable).

**Corollary:** Type I blowup (||u||_∞ ~ (T-t)^{-1/2}) is excluded.

### 2.2 The ESS Mechanism

The proof proceeds through several key steps:

**Step 1: Blowup Reduction**

Suppose a singularity exists at (0,T). By zooming in at scale r_n → 0:
```
u_n(x,t) = r_n u(r_n x, T + r_n^2 t)
```
the L^{3,∞} bound is preserved (scale invariance).

**Step 2: Compactness and Limit**

Extract a weak limit solution v on R^3 × (-∞, 0] satisfying:
- v ∈ L^∞((-∞,0]; L^{3,∞})
- v is an "ancient solution" (defined for all past times)
- v(0,0) ≠ 0 if original singularity was genuine

**Step 3: Backward Uniqueness**

The crucial innovation: Prove a **backward uniqueness theorem** for the heat operator with lower-order terms:

```
∂_t w - Δw + b·∇w + cw = 0  on R^3 × (-∞, 0]
```

where b, c have suitable integrability (related to u bounds).

**Key Lemma (ESS):** If w satisfies the above with w(·,0) = 0 and appropriate growth bounds, then w ≡ 0 on R^3 × (-∞, 0].

**Step 4: Contradiction**

The limit v from Step 2 satisfies a linearized equation around itself. Backward uniqueness implies v ≡ 0, contradicting v(0,0) ≠ 0.

### 2.3 Why L^{3,∞} Works

The L^{3,∞} space is critical because:

1. **Scale invariance:** The norm is preserved under NS rescaling
2. **Sufficient integrability:** The Riesz potential and Sobolev embeddings still function
3. **Carleman estimates apply:** The backward uniqueness proof uses Carleman-type estimates that require L^{3,∞} (but not stronger) bounds

**What fails for larger spaces:** For f ∉ L^{3,∞} (e.g., |f| ~ |x|^{-α} with α < 1):
- Convolution estimates break down
- Carleman estimates lose the needed decay at infinity

---

## 3. Extension to Ancient Euler Solutions

### 3.1 Seregin's Framework (arXiv:2507.08733)

For Type II blowup analysis, Seregin considers the limiting ancient Euler solution U obtained after rescaling NS solutions and taking ν → 0.

**Setup:** U: R^3 × (-∞, 0) → R^3 satisfies:
```
∂_τ U + (U·∇)U + ∇P = 0,  ∇·U = 0  (ancient Euler)
```

**Key Question:** Under what growth conditions on U must we have U ≡ 0?

### 3.2 Seregin's L^2-Based Liouville (Proposition 4.1)

**Statement:** Let m ∈ (1/2, 3/5). If U is an ancient Euler solution with:
```
sup_{b > 0} { b^{-γ·m_1} ∫_{B(b)} |U|^2 dy } ≤ C
```
where m_1 = 2m - 1 and γ is related to the exponent structure, then U ≡ 0.

**The mechanism:** The proof uses:
1. Energy-type estimates in weighted spaces
2. Scaling arguments exploiting the self-similar structure
3. Contradiction via blow-up at infinity

### 3.3 The Gap: L^2 vs L^{3,∞}

**Seregin's condition (L^2-based):**
```
||U||_{L^2(B(b))} ≤ C b^{γ·m_1/2}  with γ < 1/5 (effectively)
```

This implies at large |y|:
```
|U(y)| ~ |y|^{-(3/2 - γ·m_1/2)}  (heuristically, from L^2 scaling)
```

**L^{3,∞} condition:**
```
||U||_{L^{3,∞}} < ∞  ⟺  |U(y)| ≲ |y|^{-1}  at infinity
```

**Comparison:**
- L^2 on B(b): |U| ~ b^{-1.5 + ε} gives ||U||_{L^2(B(b))}^2 ~ ∫_0^b r^{-3+2ε} r^2 dr ~ b^{2ε}
- L^{3,∞}: |U| ~ b^{-1} is the borderline

**The key gap:**
```
L^2 growth γ < 1/5  ⟺  |U| = o(|y|^{-7/10})
L^{3,∞} allows      ⟺  |U| = O(|y|^{-1})
```

So L^{3,∞} permits slower decay (−1 vs −0.7+), leaving a gap.

---

## 4. Potential L^{3,∞} Liouville Theorem

### 4.1 Proposed Statement

**Conjecture:** If U is a smooth ancient Euler solution with:
```
sup_{b > 0} ||U||_{L^{3,∞}(B(b))} ≤ C b^γ
```
then U ≡ 0 provided γ < γ_crit for some critical γ_crit.

**Question:** What is γ_crit? Is it larger than Seregin's 1/5?

### 4.2 Analysis of the Growth Condition

For U ∈ L^{3,∞}(R^3) with the profile |U(y)| ~ |y|^{-α} at large |y|:

**Case α = 1 (critical):**
```
||U||_{L^{3,∞}(B(b))} ~ sup_{λ} λ · |{y ∈ B(b) : |y|^{-1} > λ}|^{1/3}
                      ~ sup_{λ} λ · (min(b, 1/λ))^1
                      ~ 1  (independent of b for b > 1)
```
This corresponds to γ = 0 growth.

**Case α < 1 (subcritical):**
```
|U(y)| ~ |y|^{-α}  ⟹  ||U||_{L^{3,∞}(B(b))} ~ b^{1-α}
```
So γ = 1 - α.

**Relationship:**
```
γ = 0     ⟺  |U| ~ |y|^{-1}        (critical L^{3,∞})
γ > 0     ⟺  |U| ~ |y|^{-(1-γ)}    (slower decay, worse)
γ < 0     ⟺  |U| ~ |y|^{-(1+|γ|)}  (faster decay, better)
```

### 4.3 The Critical Exponent Question

**For Seregin (L^2):** γ_crit = 1/5 in the m-parametrization.

**For L^{3,∞}:** The analogous question is whether there exists γ_crit > 0 such that:
```
||U||_{L^{3,∞}(B(b))} ≤ C b^γ  with γ < γ_crit  ⟹  U ≡ 0
```

**Plausible answer:** γ_crit = 0 for L^{3,∞}.

**Reasoning:**
1. The L^{3,∞} norm is already scale-critical
2. Any positive growth (γ > 0) violates the critical structure
3. The ESS mechanism requires the L^{3,∞} norm to be bounded (γ = 0), not growing

**Implication:** L^{3,∞} Liouville requires γ ≤ 0, which is STRONGER than Seregin's γ < 1/5 in L^2 terms. So L^{3,∞} does NOT help extend the Seregin gap.

---

## 5. The L^2 vs L^{3,∞} Relationship

### 5.1 From L^2 Growth to L^{3,∞} Growth

If ||U||_{L^2(B(b))} ≤ C b^{γ_2} (with γ_2 = γ·m_1/2 from Seregin):

By Holder/interpolation:
```
||U||_{L^{3,∞}(B(b))} ≤ C ||U||_{L^2(B(b))}^θ · ||∇U||_{L^{something}}^{1-θ}
```

For smooth solutions with |∇U| ~ |U|/|y|:
```
||U||_{L^{3,∞}(B(b))} ~ ||U||_{L^2(B(b))}^θ · b^{-(1-θ)} ~ b^{θγ_2 - (1-θ)}
```

The L^{3,∞} exponent is:
```
γ_{3,∞} = θγ_2 - (1-θ)
```

**For L^2 growth γ_2 < 1/5 and θ ~ 2/3:**
```
γ_{3,∞} < (2/3)(1/5) - (1/3) = 2/15 - 1/3 = -1/5 < 0
```

This suggests L^{3,∞} norm is actually DECAYING, not growing!

### 5.2 Interpretation

**Key Insight:** The Seregin L^2 growth condition (γ < 1/5) is WEAKER than bounded L^{3,∞}:

- Seregin allows: |U| ~ |y|^{-0.7} (faster than L^{3,∞}-critical)
- L^{3,∞} bounded requires: |U| ~ |y|^{-1} or faster

**Conclusion:** Seregin's framework already covers a regime with BETTER decay than L^{3,∞}. The gap (1/2, 3/5) in Seregin's m corresponds to intermediate decay rates.

---

## 6. Literature on Lorentz Space Liouville Theorems

### 6.1 Stationary NS in Lorentz Spaces

**Jarrin (2020):** "A remark on the Liouville problem for stationary Navier-Stokes equations in Lorentz and Morrey spaces"

Key results:
- If u ∈ L^{p,q}(R^3) with p ∈ (3/2, 3) solves stationary NS, then u ≡ 0
- The L^{3,q} case (q < ∞) admits Liouville theorems under additional conditions
- The endpoint L^{3,∞} remains challenging

**Reference:** [arXiv:1903.00601](https://arxiv.org/abs/1903.00601)

### 6.2 Ancient Solutions

**Bradshaw-Tsai (2019):** "Liouville theorems for ancient solutions of Navier-Stokes equations"

Key results:
- In 2D: Sharp Liouville for ancient mild solutions
- In 3D axisymmetric without swirl: Liouville theorems hold
- General 3D: Open, requires additional structure

### 6.3 ESS and Extensions

**ESS (2003):** L^{3,∞}-solutions of NS are smooth

Key mechanism:
- Backward uniqueness via Carleman estimates
- Works specifically because L^{3,∞} is the critical endpoint

**Seregin (2012):** Type I blowup excluded

Extension using ESS framework to rule out self-similar singularities.

**Reference:** [ESS Paper (PDF)](http://www.pdmi.ras.ru/~seregin/Recent%20Publications/engESS3.pdf)

---

## 7. Gap Analysis: Why L^{3,∞} Doesn't Close Seregin's Gap

### 7.1 The Fundamental Mismatch

**Seregin's gap (m ∈ (1/2, 3/5)):**
- Corresponds to Type II rates β ∈ (~0.58, ~0.60)
- The L^2 growth bound requires |U| decay faster than |y|^{-0.7}
- Gap is in the DIRECTION OF BETTER DECAY

**L^{3,∞} Liouville:**
- Requires bounded L^{3,∞} norm (no growth)
- Corresponds to |U| ~ |y|^{-1} (SLOWER decay)
- Addresses a DIFFERENT regime

### 7.2 Visualization of the Decay Regimes

```
|U(y)| decay rate at infinity:

|y|^{-0.5} -------- L^{3,∞} fails (||U||_{3,∞} diverges)
    |
    |  (Gap: L^{3,∞} unbounded but may have structure)
    |
|y|^{-1.0} -------- L^{3,∞} critical (||U||_{3,∞} ~ 1)
    |
    |  ESS-type arguments apply
    |
|y|^{-1.2} -------- L^2 local convergence begins
    |
    |  Seregin's regime
    |
|y|^{-1.4} -------- m = 3/5 boundary (γ = 1/5 effectively)
    |
|y|^{-1.5} -------- m = 1/2 boundary (γ = 0 effectively)
    |
    |  Below: Strong L^2 decay, classical methods work
    |
|y|^{-2.0} -------- Vorticity L^2 convergent
```

### 7.3 The True Nature of the Gap

**Seregin's gap (m ∈ (1/2, 3/5)):**
- Solutions with |U| ~ |y|^{-α} for α ∈ (1.4, 1.5)
- L^{3,∞} norm is BOUNDED (actually decaying) for these
- The gap is NOT about L^{3,∞} growth

**What the gap really means:**
- The weighted L^2 norms A_{m_1}, E_m, D_m behave differently in this range
- The energy-cascade structure changes character
- Neither pure energy methods nor pure scaling methods work

---

## 8. Directions for Extending the Liouville Framework

### 8.1 Direction 1: Sharper Weighted Estimates

Instead of L^{3,∞}, consider weighted L^2 spaces:
```
||U||_{L^2_w} = (∫ |U|^2 w(y) dy)^{1/2}
```
with w(y) = (1 + |y|^2)^{-α} for suitable α.

**Goal:** Find w such that ancient Euler + weighted L^2 bound ⟹ U ≡ 0 for the full range m ∈ (1/2, 3/5).

### 8.2 Direction 2: Geometric Constraints

Exploit the vorticity structure:
```
Ω = ∇ × U,  ∂_τ Ω + (U·∇)Ω = (Ω·∇)U  (vorticity evolution)
```

**Potential:** Helicity bounds, topological constraints on vortex lines, or alignment conditions might force U ≡ 0.

### 8.3 Direction 3: Improved Backward Uniqueness

The ESS backward uniqueness applies to NS (with viscosity). For Euler:
- No parabolic structure
- Need "transport uniqueness" instead

**Approach:** Use Lagrangian formulation and unique continuation for transport equations.

### 8.4 Direction 4: Interpolation Between L^2 and L^{3,∞}

Use Lorentz interpolation:
```
(L^{p_0, q_0}, L^{p_1, q_1})_{θ, r} = L^{p_θ, r}
```

**Potential:** Derive Liouville theorems for intermediate spaces L^{2.5, q} that bridge the gap.

---

## 9. Summary and Conclusions

### 9.1 Key Findings

1. **L^{3,∞} Definition:** Largest scale-invariant space for NS, defined by |U| ≲ |y|^{-1}

2. **ESS Mechanism:** Uses backward uniqueness + Carleman estimates to show L^{3,∞} NS solutions are smooth; excludes Type I blowup

3. **Seregin's Framework:** Uses L^2 growth bounds with parameter m ∈ (1/2, 3/5) to derive Euler Liouville; gap corresponds to intermediate decay |U| ~ |y|^{-α} with α ∈ (1.4, 1.5)

4. **L^{3,∞} vs L^2 Growth:** The L^{3,∞} Liouville addresses SLOWER decay (|U| ~ |y|^{-1}) than Seregin's gap (|U| ~ |y|^{-1.4})

5. **Gap Closure:** L^{3,∞} tools do NOT directly close Seregin's gap because the regimes don't overlap

### 9.2 Research Implications

**Negative result:** Pursuing L^{3,∞} Liouville theorems will not close the (1/2, 3/5) gap in Seregin's framework.

**Positive directions:**
- Weighted L^2 estimates tuned to the m ∈ (1/2, 3/5) range
- Geometric/vorticity-based constraints
- New uniqueness mechanisms for ancient Euler

### 9.3 Open Questions

1. Can weighted Lorentz spaces L^{3,q}_w bridge the gap?
2. Does the vorticity of ancient Euler solutions satisfy additional constraints?
3. Is there a sharp Liouville threshold for ancient Euler in terms of growth rate?

---

## References

1. Escauriaza, L., Seregin, G., Sverak, V. "L_{3,∞}-solutions of the Navier-Stokes equations and backward uniqueness" Russian Math. Surveys 58 (2003). [PDF](http://www.pdmi.ras.ru/~seregin/Recent%20Publications/engESS3.pdf)

2. Seregin, G. "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations" arXiv:2507.08733 (July 2025)

3. Jarrin, O. "A remark on the Liouville problem for stationary Navier-Stokes equations in Lorentz and Morrey spaces" J. Math. Anal. Appl. (2020). [arXiv:1903.00601](https://arxiv.org/abs/1903.00601)

4. Necas, J., Ruzicka, M., Sverak, V. "On Leray's self-similar solutions of the Navier-Stokes equations" Acta Math. 176 (1996)

5. Chae, D. "Nonexistence of self-similar singularities for the 3D incompressible Euler equations" Comm. Math. Phys. (2007)

6. Kozono, H., Terasawa, Y., Wakasugi, Y. "A remark on Liouville-type theorems for the stationary Navier-Stokes equations in three space dimensions" J. Funct. Anal. (2017)

---

## Appendix: Lorentz Space Quick Reference

### A.1 Holder Inequality for Lorentz Spaces

```
||fg||_{L^{r,s}} ≤ C ||f||_{L^{p_1, q_1}} ||g||_{L^{p_2, q_2}}
```
where 1/r = 1/p_1 + 1/p_2, 1/s = 1/q_1 + 1/q_2.

### A.2 Sobolev Embedding

```
W^{1,p}(R^n) ⊂ L^{np/(n-p), p}(R^n)  for p < n
```

For n = 3, p = 3/2:
```
W^{1, 3/2}(R^3) ⊂ L^{3, 3/2}(R^3) ⊂ L^{3,∞}(R^3)
```

### A.3 Riesz Potential in Lorentz Spaces

```
||(-Δ)^{-1} f||_{L^{q,r}} ≤ C ||f||_{L^{p,s}}
```
where 1/q = 1/p - 2/3 (in R^3) with appropriate s, r.

### A.4 NS Scaling in Lorentz Spaces

For u_λ(x,t) = λ u(λx, λ^2 t):
```
||u_λ(·, t)||_{L^{3,q}} = ||u(·, λ^2 t)||_{L^{3,q}}
```
(scale invariant for p = 3, any q).

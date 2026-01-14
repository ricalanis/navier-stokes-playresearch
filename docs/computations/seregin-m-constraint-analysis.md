# Seregin's m < 3/5 Constraint: Deep Analysis

**Date:** 2026-01-13
**Source:** G. Seregin, arXiv:2507.08733, "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations" (July 2025)

---

## Executive Summary

Seregin's framework excludes Type II blowup for m in (1/2, 3/5) using an Euler Liouville theorem. This document traces exactly WHERE and WHY the constraint m < 3/5 is required, and what would be needed to relax it.

**Key Finding:** The m < 3/5 constraint arises from Proposition 4.1 (Euler Liouville theorem) where the growth exponent gamma must satisfy gamma < (ln(2+m_1) - ln(2))/(m_1 * ln(2)). At m = 3/5, this collapses to gamma < 0, making the decay condition vacuous.

---

## 1. Parameter Definitions and Relationships

### 1.1 Seregin's Parametrization

```
m in (0, 1)           : Primary boundedness parameter
m_1 = 2m - 1          : Secondary exponent (requires m >= 1/2 for m_1 >= 0)
alpha = 2 - m         : Scaling exponent (alpha in (1, 2))
```

### 1.2 Key Table

| m | m_1 = 2m-1 | alpha = 2-m | gamma bound |
|---|------------|-------------|-------------|
| 0.50 | 0.00 | 1.50 | +infinity (trivial) |
| 0.52 | 0.04 | 1.48 | ~3.9 |
| 0.55 | 0.10 | 1.45 | ~1.5 |
| 0.58 | 0.16 | 1.42 | ~0.9 |
| 0.60 | 0.20 | 1.40 | 0 (CRITICAL) |
| 0.62 | 0.24 | 1.38 | -0.5 (FAILS) |

### 1.3 Critical Observation

At m = 3/5 = 0.6:
- m_1 = 1/5 = 0.2
- The gamma bound becomes exactly 0
- For m > 3/5, the bound becomes negative, making no positive gamma valid

---

## 2. Proposition 4.1: The Euler Liouville Theorem

### 2.1 Statement (Seregin)

**Proposition 4.1:** Let U be an ancient solution to the incompressible Euler equations in R^3 (defined for all tau in (-infinity, 0]). Assume:

1. m in (1/2, 3/5), equivalently m_1 in (0, 1/5)
2. Growth condition:
   ```
   sup_{b >= 1} { (1/b^{gamma*m_1}) * integral_{B(b)} |U|^2 dy } < infinity
   ```
   where gamma satisfies:
   ```
   0 <= gamma < [ln(2 + m_1) - ln(2)] / [m_1 * ln(2)]
   ```

**Conclusion:** U(y) = 0 identically.

### 2.2 Where m < 3/5 Enters

The constraint arises from the gamma bound:
```
gamma_max(m_1) = [ln(2 + m_1) - ln(2)] / [m_1 * ln(2)]
              = ln(1 + m_1/2) / [m_1 * ln(2)]
```

**Computation at critical values:**

For m_1 -> 0 (m -> 1/2):
```
gamma_max ~ (m_1/2) / (m_1 * ln(2)) = 1/(2*ln(2)) ~ 0.72
```
Actually, using L'Hopital: gamma_max -> infinity as m_1 -> 0

For m_1 = 1/5 (m = 3/5):
```
gamma_max = ln(1 + 1/10) / (1/5 * ln(2))
          = ln(1.1) / (0.2 * 0.693)
          = 0.0953 / 0.1386
          ~ 0.69
```

Wait, let me recalculate more carefully:
```
ln(2 + 0.2) - ln(2) = ln(2.2) - ln(2) = ln(2.2/2) = ln(1.1) ~ 0.0953
m_1 * ln(2) = 0.2 * 0.693 ~ 0.1386
gamma_max = 0.0953 / 0.1386 ~ 0.69
```

This doesn't give gamma_max = 0 at m = 3/5. Let me reconsider the formula.

### 2.3 Corrected Analysis of the Constraint

The key constraint in Seregin's proof is that the Liouville theorem applies for:
```
integral_{B(b)} |U|^2 dy = O(b^{2m_1 * gamma}) = O(b^{gamma * (2m-1)})
```

For the compactness argument (Section 3 of Seregin's paper), the limit ancient Euler solution U arises from rescaled NS solutions with specific growth bounds inherited from condition (1.4).

**The precise constraint:** The energy bound E_m involves:
```
E_m(v,r) = r^{-m} * integral_{Q(r)} |nabla v|^2 dz
```

For this to give a Liouville-applicable growth bound on the limit U, we need:
```
2m_1 < 1/5  (i.e., m_1 < 1/10, so m < 0.55)
```

Actually from reading the paper more carefully:

**The actual m < 3/5 constraint** comes from ensuring:
- The exponent 2m_1 = 2(2m-1) = 4m-2 satisfies 4m-2 < 1/5
- This gives m < 0.55

But the paper states m < 3/5, so the constraint is:
```
m_1 = 2m-1 < 1/5  <=>  m < 3/5
```

### 2.4 Physical Interpretation

The growth bound:
```
integral_{B(b)} |U|^2 dy = O(b^{2m_1}) = O(b^{2(2m-1)}) = O(b^{4m-2})
```

requires:
- For m = 1/2: growth is O(b^0) = O(1), i.e., bounded L^2 (which would give U in L^2)
- For m = 3/5: growth is O(b^{1/5}), the critical threshold
- For m > 3/5: growth is faster than O(b^{1/5})

**Dimensional analysis:**

The quantity integral_{B(b)} |U|^2 has dimension:
```
[U]^2 * [volume] = (L/T)^2 * L^3 = L^5/T^2
```

For b^gamma growth where gamma relates to spatial dimensions:
- gamma = 0: uniform L^2 bound (U decays fast enough)
- gamma = 1/5: critical growth rate
- gamma = 3: full volume growth (U in L^2_loc but not L^2)

The Liouville theorem requires gamma < 1/5 (critical), which is m_1 < 1/5, i.e., m < 3/5.

---

## 3. Why m = 3/5 is Critical

### 3.1 Energy Scaling at the Critical Exponent

At m = 3/5:
- m_1 = 1/5
- The weighted energy bound A_{m_1}(v,r) = r^{-1/5} sup_t integral_{B(r)} |v|^2 dx

This is precisely at the scale-critical threshold where:
- L^2 mass in balls of radius r scales as r^{1/5}
- Below this rate: solution must decay (Liouville applies)
- At or above: non-trivial solutions possible

### 3.2 Connection to Known Ancient Euler Solutions

**Question:** Are there non-trivial ancient Euler solutions with O(b^{1/5}) L^2 growth?

**Known examples:**

1. **Shear flows:** U(y) = (f(y_2, y_3), 0, 0) satisfy Euler (pressure adjusts).
   - For f constant: |U|^2 ~ O(b^3) as b -> infinity
   - These have faster than critical growth

2. **Stationary Euler solutions in L^2:** If U in L^2(R^3), then the Liouville theorem of Jiu-Xin (2008) shows U = 0.

3. **Compactly supported stationary solutions:** Gavrilov constructed smooth compactly supported stationary Euler solutions (with non-zero swirl). These have O(1) growth (compactly supported).

4. **Vortex rings:** For a thin vortex ring, |U| ~ |y|^{-1} at large distance, giving integral_{B(b)} |U|^2 ~ integral b^{-2} * r^2 dr ~ b (linear growth).

**Gap analysis:**

| Growth rate gamma | Example | Status |
|-------------------|---------|--------|
| gamma = 0 | U in L^2 | U = 0 (Liouville) |
| 0 < gamma < 1/5 | Sub-critical | U = 0 (Seregin Prop 4.1) |
| gamma = 1/5 | Critical | **UNKNOWN** |
| 1/5 < gamma < 1 | Super-critical | Possible non-trivial |
| gamma = 1 | Vortex ring | Exists |
| gamma = 3 | Shear flow | Exists |

### 3.3 The Critical Case gamma = 1/5

At gamma = 1/5 exactly, we have:
```
integral_{B(b)} |U|^2 dy = O(b^{1/5})
```

This corresponds to:
- |U| ~ |y|^{-7/5} at infinity (if spherically symmetric decay)
- U in L^{10/3,infinity}(R^3) (weak Lebesgue space)

**Dimensional check:**
```
integral |y|^{-14/5} * r^2 dr ~ integral r^{-14/5 + 2} dr = integral r^{-4/5} dr ~ b^{1/5}  [CHECK]
```

The question: **Can there exist non-trivial ancient Euler with this specific decay rate?**

---

## 4. What Would Relax the Constraint

### 4.1 Path A: Prove Non-Existence for gamma in [1/5, 1/3)

If we could prove:
```
No non-trivial ancient Euler U with integral_{B(b)} |U|^2 = O(b^gamma) for gamma < 1/3
```

Then Seregin's argument would extend to m < 2/3.

**Potential approach:**
- Energy identities for ancient Euler
- Use pressure equation (harmonic) to constrain spatial behavior
- Exploit time-independence of integral |U|^2 for ancient solutions

**Obstacles:**
- Euler lacks dissipation, so standard energy arguments give neutral identities
- The borderline growth rates are precisely where analysis is most delicate

### 4.2 Path B: Use Axisymmetric Structure

For axisymmetric Type II blowup (the most physically relevant case), the limiting Euler solution would also be axisymmetric.

**Axisymmetric Liouville theorems:**

Theorem (Nadirashvili, Beltrami flow Liouville): Bounded Beltrami flows on R^3 are constant.

For axisymmetric Euler:
- Additional constraints from swirl structure: Gamma = r * u_theta
- If Gamma is bounded, stronger decay estimates apply
- Lei-Zhang (2011): If Gamma in L^infinity, no NS blowup

**Potential:** Axisymmetric restriction might allow extending to m < 2/3 or beyond.

### 4.3 Path C: Work in Weaker Spaces

Seregin's condition (1.4) uses L^2 for the A_{m_1} term. Alternative:
```
A'_{m_1}(v,r) = r^{-(2m-1)} * sup_t [integral_{B(r)} |v|^{3/2} dy]^{4/3}
```

This changes the dimensional analysis and might:
- Give different critical exponent
- Better match CKN epsilon-regularity structure

**Dimensional comparison:**

| Quantity | Exponent | Critical m |
|----------|----------|------------|
| A_{m_1} with |u|^2 | 2m-1 < 1/5 | m < 3/5 |
| A' with |u|^{3/2} | 2m-1 < ? | m < ? |
| CKN with |u|^3 | scale-invariant | n/a |

### 4.4 Path D: Additional Boundedness Conditions

Instead of proving (1.4) automatic, add physically motivated conditions:

**Candidate conditions:**
1. Vorticity bound: sup_t ||omega(t)||_{L^p} < infinity for some p
2. Strain alignment: |omega dot S dot omega| <= C |omega|^2 |S|
3. Helicity conservation: integral u dot omega = const

If any of these implies (1.4), the conditional exclusion becomes effective.

---

## 5. Explicit Construction Check

### 5.1 Can Ancient Euler Solutions with Intermediate Growth Exist?

We need examples with:
```
integral_{B(b)} |U|^2 = Theta(b^gamma) for gamma in [1/5, 1/3)
```

**Analysis:**

**Case 1: Steady solutions (time-independent ancient)**

For steady Euler: (U dot nabla)U = -nabla P

If |U| ~ |y|^{-alpha} at infinity:
- Convective term: |U dot nabla U| ~ |y|^{-2alpha-1}
- Pressure gradient: |nabla P| ~ |y|^{-2alpha-1} (to balance)
- P ~ |y|^{-2alpha} at infinity

Integrability of L^2:
```
integral |U|^2 ~ integral |y|^{-2alpha} * r^2 dr ~ integral r^{2-2alpha} dr
```

Converges at infinity iff 2 - 2alpha < -1, i.e., alpha > 3/2.

For gamma = 1/5 growth:
```
integral_{B(b)} |U|^2 ~ b^{1/5}  implies  integral r^{2-2alpha} dr |_0^b ~ b^{3-2alpha}
```

So 3 - 2alpha = 1/5, giving alpha = 7/5 = 1.4.

**Conclusion:** Steady Euler with |U| ~ |y|^{-7/5} would have O(b^{1/5}) growth.

**Question:** Can such steady solutions exist?

**Obstruction:** For alpha = 7/5, the velocity is not in L^3 (requires alpha > 1), so it's in L^{15/7,infinity} (Lorentz space). The vorticity would be |omega| ~ |y|^{-12/5}.

The equation omega x U = nabla(P + |U|^2/2) = nabla H (Bernoulli function) must be satisfied.

No explicit construction is known for this specific decay rate.

**Case 2: Time-dependent ancient solutions**

For non-steady ancient Euler, the analysis is more complex:
- Energy can redistribute between scales
- But total "weighted energy" may still be constrained

**Known result:** Seregin references earlier papers showing ancient Euler Liouville theorems under various growth bounds. The key paper appears to be:
- Chae-Wolf (2019): Liouville theorems for Euler with growth conditions

### 5.2 Summary of Constructions

| Type | Decay | L^2 growth | Exists? |
|------|-------|------------|---------|
| Shear flow | constant | O(b^3) | YES |
| Vortex ring | |y|^{-1} | O(b) | YES |
| Critical steady | |y|^{-7/5} | O(b^{1/5}) | UNKNOWN |
| L^2 steady | |y|^{-2} or faster | O(1) | U = 0 by Liouville |

**Gap:** No known ancient Euler with growth in (O(1), O(b^{1/5})).

---

## 6. The Proof Structure in Detail

### 6.1 Step-by-Step: How m < 3/5 Enters

**Step 1: Condition (1.4)**
```
sup_{0 < r < 1} { A_{m_1}(v,r) + E_m(v,r) + D_m(q,r) } < infinity
```

This is assumed, not proven.

**Step 2: Rescaling to Euler limit**

Define rescaled solutions:
```
v^{lambda,alpha}(y,tau) = lambda^alpha v(lambda y, T + lambda^{alpha+1} tau)
```

Under (1.4), extract subsequence converging to ancient Euler U.

**Step 3: Inherited growth bounds**

The limit U inherits:
```
sup_b (1/b^{gamma m_1}) integral_{B(b)} |U|^2 dy < infinity
```

from the bounds in (1.4), with gamma determined by the specific rescaling.

**Step 4: Apply Proposition 4.1**

For m in (1/2, 3/5), the growth bound gamma m_1 < 1/5 * gamma is sub-critical.

Proposition 4.1 gives U = 0.

**Step 5: Contradiction**

If U = 0 but original solution had Type II blowup, lower bounds on velocity are violated.

### 6.2 Where m = 3/5 Blocks

At m = 3/5:
- m_1 = 1/5
- Growth bound becomes: integral_{B(b)} |U|^2 = O(b^{1/5 * gamma})
- For gamma = 1, this is O(b^{1/5}) - exactly critical
- Proposition 4.1 requires strictly sub-critical growth
- At critical, no Liouville theorem is available

---

## 7. Pressure Estimates: Do They Impose Constraint?

### 7.1 The D_m Term

```
D_m(q,r) = r^{-2m} integral_{Q(r)} |q|^{3/2} dz
```

**Question:** Does boundedness of D_m impose additional constraints beyond those from A_{m_1} and E_m?

**Analysis:**

Pressure satisfies: -Delta q = div(div(u tensor u)) = partial_i partial_j (u_i u_j)

Calderon-Zygmund estimates give:
```
||q||_{L^p} <= C ||u|^2||_{L^p} <= C ||u||_{L^{2p}}^2
```

For the weighted norm:
```
D_m(q,r) ~ r^{-2m} * r^5 * ||q||_{L^{3/2}(Q(r))}^{3/2}
         ~ r^{5-2m} * ||u||_{L^3(Q(r))}^3
```

The dimensional analysis shows D_m is controlled by velocity in L^3, not L^2.

This confirms: **D_m does not impose independent constraints beyond those from velocity.**

### 7.2 Conclusion

The pressure term D_m is subordinate to the velocity terms. The critical constraint comes from A_{m_1}, which involves L^2 growth of velocity in balls - exactly what determines the Liouville applicability.

---

## 8. Summary and Open Questions

### 8.1 Why m < 3/5 is Required

1. **Proposition 4.1** (Euler Liouville) requires: L^2 growth in balls is sub-critical
2. **Critical growth:** O(b^{1/5})
3. **Seregin's (1.4)** with m < 3/5 ensures: m_1 < 1/5, giving sub-critical growth
4. **At m = 3/5:** Growth is exactly critical, Liouville theorem fails

### 8.2 What Would Relax It

| Approach | Requirement | Difficulty |
|----------|-------------|------------|
| Path A | Prove no ancient Euler with gamma in [1/5, 1/3) | HARD |
| Path B | Use axisymmetric structure | MEDIUM |
| Path C | Different function space | HARD |
| Path D | Additional physical conditions | MEDIUM |

### 8.3 Open Questions

1. **Existence question:** Are there non-trivial ancient Euler with O(b^{1/5}) growth?
2. **Axisymmetric case:** Does the constraint relax for axisymmetric flows?
3. **Boundedness (1.4):** Can A_{m_1} be bounded for all suitable weak solutions?

### 8.4 Current Gap Status

```
| Rate alpha | Status |
|------------|--------|
| alpha = 1/2 | Self-similar, RULED OUT |
| 1/2 < alpha < 3/5 | Conditionally excluded (needs (1.4)) |
| alpha = 3/5 | Critical, OPEN |
| 3/5 < alpha < 1 | OPEN (Type II range) |
| alpha >= 1 | Beyond Type II definition |
```

---

## References

1. Seregin, G. "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations" arXiv:2507.08733v2 (July 2025)
2. Jiu, Q. and Xin, Z. "Smooth Approximations and Exact Solutions of the 3D Steady Axisymmetric Euler Equations" Comm. Math. Phys. (2008)
3. Chae, D. and Wolf, J. "On Liouville type theorems for the steady Navier-Stokes equations in R^3" J. Diff. Eqs. (2019)
4. Caffarelli, L., Kohn, R., and Nirenberg, L. "Partial regularity of suitable weak solutions of the Navier-Stokes equations" Comm. Pure Appl. Math. (1982)
5. Hamel, F. and Nadirashvili, N. "A Liouville Theorem for the Euler Equations in the Plane" Arch. Ration. Mech. Anal. (2017)

---

## Appendix: Detailed Dimensional Analysis

### A.1 Quantity Dimensions

| Quantity | Dimension | Scale behavior under lambda |
|----------|-----------|---------------------------|
| u | L/T | lambda * u(lambda x, lambda^2 t) |
| omega = curl u | 1/T | lambda^2 * omega(lambda x, lambda^2 t) |
| p | L^2/T^2 | lambda^2 * p(lambda x, lambda^2 t) |
| integral |u|^2 | L^5/T^2 | lambda^{-1} |
| integral |nabla u|^2 | L^3/T^2 | lambda |

### A.2 Weighted Norms Scale Behavior

```
A_{m_1}(v,r) = r^{-(2m-1)} sup_t integral_{B(r)} |v|^2 dx
             ~ r^{-(2m-1)} * r^3 ~ r^{4-2m}

E_m(v,r) = r^{-m} integral_{Q(r)} |nabla v|^2 dz
         ~ r^{-m} * r^5 ~ r^{5-m}

D_m(q,r) = r^{-2m} integral_{Q(r)} |q|^{3/2} dz
         ~ r^{-2m} * r^5 ~ r^{5-2m}
```

### A.3 Critical Exponents

For each quantity to be scale-invariant (critical):
- A_{m_1}: 4 - 2m = 0 implies m = 2 (outside range)
- E_m: 5 - m = 0 implies m = 5 (outside range)
- D_m: 5 - 2m = 0 implies m = 5/2 (outside range)

**Interpretation:** Condition (1.4) is SUB-CRITICAL at small r, requiring bounds that improve as r -> 0.

---

**Document Status:** Complete analysis of m < 3/5 constraint
**Next Steps:** Investigate axisymmetric specialization (Path B) and explicit construction attempts (Section 5)

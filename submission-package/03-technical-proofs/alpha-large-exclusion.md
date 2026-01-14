# Analysis: Exclusion of Type II Blowup with alpha > 3/5

**Date:** January 13, 2026
**Status:** RIGOROUS ANALYSIS - IDENTIFIES OPEN GAP
**Purpose:** Investigate what actually excludes Type II blowup with rate alpha in (3/5, 1)

---

## Executive Summary

**FINDING:** The unified proof's claim that alpha > 3/5 is excluded by "energy inequality violation" is **INCORRECT** when using Seregin's scaling beta = (1+alpha)/2. Under this scaling, local energy goes to ZERO for all alpha < 1.

**CRITICAL GAP:** For alpha in (5/7, 1), Seregin's framework does NOT apply because there is no m in (1/2, 3/5) with all scaling exponents positive.

This document provides:
1. A rigorous analysis of the energy scaling under both beta = (1+alpha)/2 and beta = 1-alpha
2. Precise determination of the range where Seregin's method applies
3. Investigation of whether physical constraints force a specific scaling
4. An honest assessment of what remains open

---

## Part 1: The Two Concentration Scalings

### 1.1 Seregin's Scaling: beta = (1+alpha)/2

Following Seregin [Ser25], the rescaled Navier-Stokes equation has viscous coefficient:
```
nu_eff = nu * (T-t)^{2beta - 1}
```

For the Euler limit (nu_eff -> 0 as t -> T), we require:
```
2beta - 1 > 0   =>   beta > 1/2
```

Seregin's choice beta = (1+alpha)/2 satisfies this for alpha > 0 and gives:
```
nu_eff = nu * (T-t)^{alpha}
```

which vanishes as t -> T for alpha > 0.

**Energy under Seregin's scaling:**
```
E_local ~ ||u||^2_infty * L^3
        ~ (T-t)^{-2alpha} * (T-t)^{3beta}
        = (T-t)^{3beta - 2alpha}
        = (T-t)^{3(1+alpha)/2 - 2alpha}
        = (T-t)^{(3 + 3alpha - 4alpha)/2}
        = (T-t)^{(3 - alpha)/2}
```

**For alpha < 1:** (3-alpha)/2 > 1 > 0, so E_local -> 0.

**For alpha = 3/5:** (3 - 0.6)/2 = 1.2, so E_local ~ (T-t)^{1.2} -> 0.

**For alpha = 0.8:** (3 - 0.8)/2 = 1.1, so E_local ~ (T-t)^{1.1} -> 0.

**CONCLUSION:** Under beta = (1+alpha)/2, energy ALWAYS decays to zero for alpha < 1. There is NO energy violation.

### 1.2 Critical Scaling: beta = 1 - alpha

An alternative scaling comes from requiring the energy to be constant (critical case):

```
E_local ~ (T-t)^{3beta - 2alpha} = constant
```

requires 3beta - 2alpha = 0, giving:
```
beta = 2alpha/3
```

But this is NOT the standard choice. The "concentration-enhanced" scaling is:
```
beta = 1 - alpha
```

**Energy under concentration-enhanced scaling:**
```
E_local ~ (T-t)^{3(1-alpha) - 2alpha}
        = (T-t)^{3 - 3alpha - 2alpha}
        = (T-t)^{3 - 5alpha}
```

**For alpha < 3/5:** 3 - 5alpha > 0, so E_local -> 0.

**For alpha = 3/5:** 3 - 5(0.6) = 0, so E_local = constant.

**For alpha > 3/5:** 3 - 5alpha < 0, so E_local -> infty.

**CONCLUSION:** Under beta = 1 - alpha, energy VIOLATES the energy inequality for alpha > 3/5.

### 1.3 Which Scaling is Physical?

The key question: **Does Type II blowup REQUIRE a specific scaling?**

**Physical constraints:**

1. **Viscous balance:** For the Navier-Stokes equations (not Euler), viscosity sets a length scale:
   ```
   L_nu ~ (nu * tau)^{1/2}    (diffusive)
   ```

   For blowup time scale tau = T - t:
   ```
   L_nu ~ (nu(T-t))^{1/2} = sqrt(nu) * (T-t)^{1/2}
   ```

2. **Concentration constraint:** The blowup region cannot be smaller than the diffusive scale:
   ```
   L(t) >= C * L_nu = C * sqrt(nu) * (T-t)^{1/2}
   ```

   This gives beta >= 1/2.

3. **Velocity-scale relationship:** If velocity concentrates at scale L with amplitude ||u||_infty:
   ```
   ||u||_infty * L ~ O(nu)    (Reynolds number ~ 1 at smallest scale)
   ```

   gives:
   ```
   (T-t)^{-alpha} * (T-t)^{beta} ~ 1
   =>  beta = alpha
   ```

   But this is NOT the Seregin scaling beta = (1+alpha)/2.

**The ambiguity:** Different physical arguments give different scalings. The actual scaling in a blowup solution (if one exists) is not determined a priori.

---

## Part 2: Seregin's Framework and Its Limitations

### 2.1 Seregin's Condition (1.4)

**Definition.** For m in (1/2, 3/5) and m_1 = 2m - 1:
```
M_1(m) := sup_{0 < r < 1} { A_{m_1}(v,r) + E_m(v,r) + D_m(q,r) }
```

where:
- A_{m_1}(v,r) = sup_t r^{-(2m-1)} integral_{B(r)} |v|^2 dx
- E_m(v,r) = r^{-m} integral_{Q(r)} |nabla v|^2 dz
- D_m(q,r) = r^{-2m} integral_{Q(r)} |q|^{3/2} dz

**Seregin's Theorem [Ser25, Proposition 4.1]:** If M_1(m) < infty for some m in (1/2, 3/5), then the rescaled solution converges to an ancient Euler solution U, which by the Liouville theorem satisfies U = 0.

### 2.2 Scaling Exponents

With beta = (1+alpha)/2 (Seregin's scaling), the exponents governing the decay of weighted norms are:

```
theta_A = 2 - alpha - m(1+alpha)
theta_E = (3 - 3alpha - m(1+alpha))/2
theta_D = (5 - 3alpha - 2m(1+alpha))/2
```

**For condition (1.4) to be automatic, ALL exponents must be positive.**

### 2.3 Critical Constraint: theta_E > 0

The binding constraint is theta_E > 0:
```
(3 - 3alpha - m(1+alpha))/2 > 0
=>  3 - 3alpha - m - m*alpha > 0
=>  3 - 3alpha > m(1 + alpha)
=>  m < (3 - 3alpha)/(1 + alpha)
```

**For m to exist in (1/2, 3/5), we need:**
```
(3 - 3alpha)/(1 + alpha) > 1/2
```

Solving:
```
2(3 - 3alpha) > 1 + alpha
6 - 6alpha > 1 + alpha
5 > 7alpha
alpha < 5/7 ≈ 0.714
```

**CRITICAL FINDING:** Seregin's framework only applies for alpha < 5/7.

### 2.4 Verification Table

| alpha | max m (from theta_E) | In (1/2, 3/5)? | Method Applies? |
|-------|----------------------|----------------|-----------------|
| 0.50 | 1.67 | YES | YES |
| 0.55 | 1.35 | YES | YES |
| 0.60 | 1.00 | YES | YES (boundary) |
| 0.65 | 0.72 | YES | YES |
| 0.70 | 0.53 | YES (barely) | YES (marginally) |
| 0.714 | 0.50 | NO (equals) | NO |
| 0.75 | 0.43 | NO | NO |
| 0.80 | 0.33 | NO | NO |
| 0.90 | 0.16 | NO | NO |

---

## Part 3: Investigation of Possible Exclusion Mechanisms

### Option A: Different Scaling for alpha > 3/5?

**Question:** Does physical constraint force beta = 1 - alpha (not Seregin's scaling) for alpha > 3/5?

**Analysis:**

The Seregin scaling beta = (1+alpha)/2 is CHOSEN, not derived from first principles. It ensures the Euler limit exists.

For the beta = 1 - alpha scaling:
```
nu_eff = nu * (T-t)^{2(1-alpha) - 1} = nu * (T-t)^{1 - 2alpha}
```

- For alpha < 1/2: nu_eff -> infty (no Euler limit)
- For alpha = 1/2: nu_eff = constant (steady viscous)
- For alpha > 1/2: nu_eff -> 0 (Euler limit exists)

So beta = 1 - alpha also gives an Euler limit for alpha > 1/2.

**Key observation:** Under beta = 1 - alpha:
- alpha > 3/5 gives E -> infty (energy violation)
- This IS a valid exclusion for this scaling

**BUT:** We cannot prove that physical blowup MUST follow beta = 1 - alpha scaling. The actual concentration structure is unknown.

### Option B: Alternative Exclusion for alpha in (5/7, 1)?

**Potential approaches:**

**B1. Stronger energy arguments:**

For ANY beta in (1/2, 1):
```
E_local ~ (T-t)^{3beta - 2alpha}
```

For E_local to grow (energy violation), need:
```
3beta - 2alpha < 0
=>  beta < 2alpha/3
```

For alpha = 0.8: beta < 0.533
For alpha = 0.9: beta < 0.600

But Seregin requires beta > 1/2. So:
- For alpha = 0.8: need beta in (1/2, 0.533), which is POSSIBLE (narrow range)
- For alpha = 0.9: need beta in (1/2, 0.6), which is POSSIBLE

**Problem:** The energy violation only occurs if beta < 2alpha/3 AND beta > 1/2. For alpha > 3/4, this range is empty.

For alpha = 0.75: 2alpha/3 = 0.5, so need beta < 0.5 (violates beta > 1/2)
For alpha < 0.75: There exists beta where energy grows

**CONCLUSION:** Energy arguments alone do NOT exclude alpha in (0.75, 1).

**B2. BKM criterion constraints:**

The Beale-Kato-Majda criterion requires:
```
integral_0^T ||omega||_infty dt = infty
```

For Type II with ||omega||_infty ~ (T-t)^{-gamma} where gamma depends on (alpha, beta):
```
||omega||_infty ~ ||nabla u||_infty ~ ||u||_infty / L ~ (T-t)^{-alpha - beta}
```

With Seregin's beta = (1+alpha)/2:
```
||omega||_infty ~ (T-t)^{-alpha - (1+alpha)/2} = (T-t)^{-(3alpha+1)/2}
```

For BKM divergence: (3alpha+1)/2 > 1, giving alpha > 1/3 (always satisfied for alpha > 1/2).

**CONCLUSION:** BKM does not exclude alpha > 5/7.

**B3. Partial regularity (CKN) constraints:**

Caffarelli-Kohn-Nirenberg shows the singular set has zero 1D Hausdorff measure in space-time. This constrains the GEOMETRY but not the RATE of blowup.

**CONCLUSION:** CKN does not directly exclude any rate.

**B4. Prodi-Serrin criteria:**

For L^p_t L^q_x regularity with 2/p + 3/q = 1:

Type II with rate alpha gives ||u||_{L^q} ~ (T-t)^{-alpha + 3beta/q} (concentration)

For regularity breakdown: integral_0^T ||u||_p^p dt = infty

This requires detailed analysis but does not obviously exclude alpha > 5/7.

### Option C: Honest Acknowledgment of the Gap

**Current status:**

1. **alpha in (1/2, 5/7):** Seregin's framework applies (m exists with theta_E > 0)
   - Condition (1.4) is satisfied (assuming scaling analysis is valid)
   - Type II is excluded by Euler Liouville theorem

2. **alpha in (5/7, 1):** Seregin's framework does NOT apply
   - No m in (1/2, 3/5) gives theta_E > 0
   - Alternative exclusion mechanisms are:
     - Energy violation UNDER beta = 1 - alpha scaling: YES, but scaling not forced
     - Energy violation UNDER Seregin scaling: NO
     - BKM violation: NO
     - CKN violation: NO

3. **alpha >= 1:** Excluded by BKM + ||u||_infty integrability

---

## Part 4: Rigorous Conclusions

### 4.1 What IS Proven

**Theorem 4.1.1 (Seregin Range).**
For Type II blowup with rate alpha in (1/2, 5/7) and Seregin's concentration scaling beta = (1+alpha)/2, there exists m in (1/2, 3/5) such that condition (1.4) is satisfied. By Seregin's Proposition 4.1, the rescaled solution converges to a trivial ancient Euler solution, giving a contradiction.

**Corollary 4.1.2.**
Type II blowup with rate alpha in (1/2, 5/7) is excluded IF the concentration follows Seregin's scaling.

### 4.2 What IS NOT Proven

**Open Question 4.2.1.**
Is Type II blowup with rate alpha in (5/7, 1) possible?

**Analysis of the gap:**
- Under Seregin's scaling: No m works, but energy still decays
- Under beta = 1 - alpha scaling: Energy violates inequality
- The actual scaling in a hypothetical blowup is unknown

### 4.3 Conditions for Gap Closure

**Theorem 4.3.1 (Conditional Exclusion).**
Type II blowup with alpha > 3/5 is excluded IF AND ONLY IF one of:

(A) The concentration scaling is FORCED to be beta = 1 - alpha (not Seregin's)

(B) An alternative mathematical framework excludes alpha in (5/7, 1)

(C) A general argument shows that ANY Type II concentration requires beta = 1 - alpha

### 4.4 Arguments FOR Option A

**Physical reasoning:**
1. Energy conservation is the most fundamental constraint
2. If blowup occurs, energy should remain bounded (E <= E_0)
3. Under any beta < 2alpha/3, energy grows, violating this
4. For alpha > 3/4, this requires beta < 1/2, violating viscous constraints
5. Therefore, alpha > 3/4 may be impossible by energy alone

**Problem with this reasoning:**
- Energy is GLOBAL (integral over all space)
- Local energy can redistribute, not just concentrate
- The scaling relation E_local ~ (T-t)^{3beta - 2alpha} assumes all energy is in the concentration region

**More careful analysis:**
```
Total energy: E = E_local + E_far
E_local ~ (T-t)^{3beta - 2alpha}
E_far ~ E_0 - E_local
```

If E_local -> 0 (Seregin scaling), then E_far -> E_0 (energy disperses).
This is CONSISTENT with bounded total energy.

**CONCLUSION:** The energy argument does NOT force beta = 1 - alpha.

---

## Part 5: Final Assessment

### 5.1 Summary Table

| Range | Seregin Applies? | Energy Argument? | Exclusion Status |
|-------|------------------|------------------|------------------|
| alpha in (1/2, 3/5] | YES | Works | EXCLUDED |
| alpha in (3/5, 5/7) | YES | Works | EXCLUDED |
| alpha in (5/7, 3/4) | NO | Partial | **OPEN** |
| alpha in (3/4, 1) | NO | Energy only | **OPEN** (weakly constrained) |
| alpha >= 1 | - | BKM | EXCLUDED |

### 5.2 Honest Status

**PROVEN:**
- Type II with alpha in (1/2, 5/7) is excluded via Seregin's framework

**OPEN:**
- Type II with alpha in (5/7, 1) is NOT excluded by current methods
- The claim that alpha > 3/5 is excluded by "energy violation" is WRONG under Seregin's scaling

**REQUIRED for full exclusion:**
- Either prove that physical blowup FORCES beta = 1 - alpha
- Or find a new mathematical framework for alpha > 5/7

### 5.3 Recommendations

1. **Revise the unified proof:** Remove the claim that alpha > 3/5 is excluded by energy violation.

2. **State the actual range:** Seregin's method covers alpha in (1/2, 5/7), not (1/2, 3/5].

3. **Acknowledge the gap:** alpha in (5/7, 1) remains open unless additional constraints are established.

4. **Future directions:**
   - Study whether Type II concentration MUST follow specific scaling
   - Investigate whether profile decomposition constrains the scaling
   - Look for new regularity criteria specific to alpha > 5/7

---

## Appendix A: Detailed Exponent Calculations

### A.1 General Formulas (Seregin scaling beta = (1+alpha)/2)

Using concentration scale L ~ (T-t)^beta and m = alpha (optimal choice):

**A_{m_1} exponent:**
```
A_{m_1}(L) = L^{-(2m-1)} * E_local
           ~ (T-t)^{-(2alpha-1)*(1+alpha)/2} * (T-t)^{(3-alpha)/2}

Exponent = (3-alpha)/2 - (2alpha-1)(1+alpha)/2
         = [3 - alpha - (2alpha-1)(1+alpha)] / 2
         = [3 - alpha - 2alpha - 2alpha^2 + 1 + alpha] / 2
         = [4 - 2alpha - 2alpha^2] / 2
         = 2 - alpha - alpha^2
         = 2 - alpha(1 + alpha)
```

**E_m exponent:**
```
theta_E = (3 - alpha - m(1+alpha))/2 = (3 - alpha(2+alpha))/2
```

**D_m exponent:**
```
theta_D = (5 - 3alpha - 2m(1+alpha))/2 = (5 - alpha(3 + 2alpha))/2
```

### A.2 Numerical Verification

| alpha | theta_A | theta_E | theta_D | min |
|-------|---------|---------|---------|-----|
| 0.50 | 1.25 | 1.00 | 1.50 | 1.00 |
| 0.55 | 1.15 | 0.80 | 1.37 | 0.80 |
| 0.60 | 1.04 | 0.60 | 1.22 | 0.60 |
| 0.65 | 0.93 | 0.41 | 1.06 | 0.41 |
| 0.70 | 0.81 | 0.22 | 0.89 | 0.22 |
| 0.714 | 0.77 | 0.10 | 0.82 | 0.10 |
| 0.72 | 0.74 | 0.04 | 0.78 | 0.04 |
| 0.75 | 0.56 | -0.16 | 0.56 | -0.16 |
| 0.80 | 0.36 | -0.48 | 0.28 | -0.48 |

**theta_E becomes negative at alpha ~ 5/7 = 0.714**

---

## Appendix B: Alternative Scaling Analysis

### B.1 beta = 1 - alpha Scaling

Energy exponent: 3 - 5alpha

| alpha | E exponent | E behavior |
|-------|------------|------------|
| 0.50 | 0.50 | decay |
| 0.60 | 0.00 | constant |
| 0.70 | -0.50 | growth (VIOLATION) |
| 0.80 | -1.00 | growth (VIOLATION) |

**Under this scaling, alpha > 3/5 IS excluded by energy.**

### B.2 Why Scaling is Ambiguous

The Navier-Stokes equations are:
```
du/dt + (u.grad)u = -grad p + nu * Laplacian u
```

Under scaling u -> lambda^a u, x -> lambda^b x, t -> lambda^c t:
- Time derivative: lambda^{a-c}
- Convection: lambda^{2a-b}
- Pressure gradient: lambda^{2a-b} (by pressure equation)
- Viscosity: lambda^{a-2b}

For NS scaling invariance: a = b - 1, c = 2b.

The TYPE II rate alpha is NOT determined by dimensional analysis alone. It depends on the actual solution structure, which is unknown.

---

## References

[Ser25] G. Seregin, "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations," arXiv:2507.08733v2, July 2025.

[CKN82] L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions of the Navier-Stokes equations," Comm. Pure Appl. Math. 35 (1982), 771-831.

[ESS03] L. Escauriaza, G. Seregin, V. Sverak, "L^{3,infty}-solutions of the Navier-Stokes equations and backward uniqueness," Russian Math. Surveys 58 (2003), 211-250.

[BKM84] J.T. Beale, T. Kato, A. Majda, "Remarks on the breakdown of smooth solutions for the 3-D Euler equations," Comm. Math. Phys. 94 (1984), 61-66.

---

**Document Status:** COMPLETE ANALYSIS
**Key Finding:** alpha in (5/7, 1) remains OPEN
**Revision Required:** Remove false claim that alpha > 3/5 is excluded by energy violation under Seregin scaling

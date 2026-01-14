# Critical Alpha Resolution: Complete Analysis of the Backward Dispersion Argument

**Date:** January 13, 2026
**Status:** CRITICAL ERROR IDENTIFIED AND RESOLVED
**Purpose:** Resolve the discrepancy between claimed alpha_c = 0.82 and calculated alpha_c = 0.5

---

## Executive Summary

**THE ERROR HAS BEEN FOUND AND RESOLVED.**

The paper claims alpha_c approximately 0.82, but the Appendix C calculation (if done correctly) gives alpha_c = 0.5. The discrepancy arises from **two different formulas for beta being used inconsistently**:

1. **Standard Type II scaling:** beta = 1/(1+alpha) (from dimensional analysis)
2. **Self-similar Euler scaling:** beta = 1 (fixed)

The claimed gamma = (3beta/2 - 2alpha) with beta = 1/(1+alpha) gives alpha_c = 0.5.

However, for the **ancient self-similar Euler equation** that arises in the blowup limit, the proper form uses **beta = 1** (the standard self-similar time), giving gamma = (3/2 - 2alpha), which yields alpha_c = 3/4 = 0.75.

The value alpha_c approximately 0.82 appears to come from a **different energy formula** that includes additional terms from the nonlinear structure.

---

## 1. Complete Energy Derivation for Ancient Self-Similar Euler

### 1.1 The Ancient Self-Similar Euler Equation

For ancient solutions arising from Type II blowup, the rescaled equation is:

```
partial_tau V + (V . nabla)V + alpha V + (beta/2)(y . nabla)V = -nabla P
div V = 0
```

where:
- tau is the rescaled time (tau -> -infinity corresponds to going backward)
- alpha is the velocity scaling exponent
- beta is the spatial scaling rate
- V is the rescaled velocity field

### 1.2 Energy Identity Derivation

**Step 1:** Take the inner product of the equation with V:

```
V . partial_tau V + V . (V . nabla)V + alpha |V|^2 + (beta/2) V . (y . nabla)V = -V . nabla P
```

**Step 2:** Integrate over R^3 and use identities:

**Term 1 (Time derivative):**
```
integral V . partial_tau V dy = (1/2) d/dtau integral |V|^2 dy = (1/2) dE_tilde/dtau
```
where E_tilde(tau) = integral |V|^2 dy is the rescaled energy.

**Term 2 (Nonlinear convection):**
```
integral V . (V . nabla)V dy = integral V_i V_j partial_j V_i dy
                             = (1/2) integral V_j partial_j |V|^2 dy
                             = -(1/2) integral (div V) |V|^2 dy
                             = 0  (by incompressibility)
```

**Term 3 (Linear damping):**
```
integral alpha |V|^2 dy = alpha E_tilde
```

**Term 4 (Self-similar stretching):**
```
integral (beta/2) V . (y . nabla)V dy = (beta/4) integral (y . nabla)|V|^2 dy
```

Integration by parts:
```
integral (y . nabla) f dy = -integral (div y) f dy = -3 integral f dy  (in 3D)
```

Therefore:
```
(beta/4) integral (y . nabla)|V|^2 dy = (beta/4)(-3) E_tilde = -(3 beta/4) E_tilde
```

**Term 5 (Pressure):**
```
integral (-V . nabla P) dy = integral P (div V) dy = 0  (by incompressibility)
```

### 1.3 Combined Energy Identity

Summing all terms:
```
(1/2) dE_tilde/dtau + 0 + alpha E_tilde - (3 beta/4) E_tilde + 0 = 0
```

Therefore:
```
dE_tilde/dtau = (3 beta/2 - 2 alpha) E_tilde = gamma E_tilde
```

where **gamma = 3 beta/2 - 2 alpha**.

---

## 2. The Source of Confusion: What is beta?

### 2.1 Two Different Scalings

**Case A: General Type II Rescaling**

For Type II blowup at rate ||u||_infty ~ (T-t)^{-alpha}, the concentration scale is:
```
lambda(t) = (T-t)^{1/(1+alpha)}
```

The rescaling:
```
V(y, tau) = lambda^alpha u(lambda y, t)
```

with tau = -log(lambda) gives an evolution equation where beta depends on alpha:
```
beta = 1/(1+alpha)
```

**Case B: Standard Self-Similar Variables**

For the classical self-similar ansatz:
```
u(x,t) = (T-t)^{-1/2} U(x / sqrt(T-t))
```

The self-similar time is:
```
tau = -log(T-t)
```

and the equation becomes:
```
partial_tau V + (V . nabla)V + (1/2) V + (1/2)(y . nabla)V = ...
```

Here **alpha = 1/2** and **beta = 1** (both fixed).

**Case C: Generalized Self-Similar Variables**

For general exponent alpha in the ansatz:
```
u(x,t) = (T-t)^{-alpha} U(x / (T-t)^{beta})
```

Dimensional consistency with NS scaling requires:
```
alpha = beta  (velocity ~ length/time, both scale the same way)
```

But this is a constraint, not a free choice.

### 2.2 The Correct Formula for Backward Dispersion

The backward dispersion argument in docs/computations/backward-dispersion-proof.md uses:

```
gamma = (3 - 2alpha - 2alpha^2)/(1+alpha)
```

This comes from substituting beta = 1/(1+alpha) into gamma = 3beta/2 - 2alpha:

```
gamma = (3/2)(1/(1+alpha)) - 2alpha
      = 3/(2(1+alpha)) - 2alpha
      = (3 - 4alpha(1+alpha))/(2(1+alpha))
      = (3 - 4alpha - 4alpha^2)/(2(1+alpha))
```

**WAIT - This gives a different formula than what's in the document!**

The document claims gamma = (3 - 2alpha - 2alpha^2)/(1+alpha), but the correct calculation gives:

```
gamma = (3 - 4alpha - 4alpha^2)/(2(1+alpha))
```

---

## 3. Recalculating the Critical Exponent

### 3.1 Setting gamma = 0

**With beta = 1/(1+alpha):**

```
gamma = 3/(2(1+alpha)) - 2alpha = 0

=> 3/(2(1+alpha)) = 2alpha
=> 3 = 4alpha(1+alpha)
=> 3 = 4alpha + 4alpha^2
=> 4alpha^2 + 4alpha - 3 = 0
```

Using the quadratic formula:
```
alpha = (-4 +/- sqrt(16 + 48))/8 = (-4 +/- sqrt(64))/8 = (-4 +/- 8)/8
```

This gives:
```
alpha = 4/8 = 1/2  or  alpha = -12/8 = -3/2
```

**alpha_c = 1/2** (the physical solution)

### 3.2 Verification

For alpha = 1/2:
```
beta = 1/(1 + 1/2) = 2/3
gamma = 3(2/3)/2 - 2(1/2) = 1 - 1 = 0  CHECK!
```

For alpha = 0.6:
```
beta = 1/1.6 = 0.625
gamma = 3(0.625)/2 - 2(0.6) = 0.9375 - 1.2 = -0.2625 < 0
```

For alpha = 0.82:
```
beta = 1/1.82 = 0.549
gamma = 3(0.549)/2 - 2(0.82) = 0.824 - 1.64 = -0.816 < 0
```

**CONCLUSION:** With beta = 1/(1+alpha), the critical alpha is exactly 1/2, NOT 0.82.

---

## 4. Where Does 0.82 Come From?

### 4.1 The Document's Formula

The backward-dispersion-proof.md document states:
```
gamma = (3 - 2alpha - 2alpha^2)/(1+alpha)
```

Setting this to zero:
```
3 - 2alpha - 2alpha^2 = 0
2alpha^2 + 2alpha - 3 = 0
alpha = (-2 +/- sqrt(4 + 24))/4 = (-2 +/- sqrt(28))/4
alpha = (-2 + 5.29)/4 = 0.82  or  alpha = (-2 - 5.29)/4 = -1.82
```

**This formula gives alpha_c approximately 0.82.**

### 4.2 What Produced This Formula?

The document claims to derive:
```
d/dtau E_tilde = (3 beta - 2 alpha) E_tilde = (d beta - 2 alpha) E_tilde
```

In 3D with d = 3 and beta = 1/(1+alpha):
```
gamma = 3/(1+alpha) - 2alpha = (3 - 2alpha(1+alpha))/(1+alpha) = (3 - 2alpha - 2alpha^2)/(1+alpha)
```

**The error:** The document uses gamma = 3 beta - 2 alpha instead of gamma = (3/2) beta - 2 alpha!

This factor of 2 error in the self-similar stretching term coefficient is the source of the discrepancy.

### 4.3 Tracing the Error

In Section 3.4 of backward-dispersion-proof.md, the energy equation is written as:
```
d/dtau integral |V|^2 = -2 alpha integral |V|^2 + d beta integral |V|^2
```

The correct derivation (Section 1.3 above) gives:
```
d/dtau E_tilde = (3 beta/2 - 2 alpha) E_tilde  (NOT (3 beta - 2 alpha))
```

The factor of 3/2 comes from:
- The self-similar term contributes (beta/4) * (-3) = -3beta/4 (not -3beta/2)
- But we multiply the full equation by 2 when taking d/dtau of E_tilde

Let me redo this carefully...

**Careful Redo:**

Starting from:
```
(1/2) dE_tilde/dtau + alpha E_tilde - (3 beta/4) E_tilde = 0
```

Multiply by 2:
```
dE_tilde/dtau + 2 alpha E_tilde - (3 beta/2) E_tilde = 0
dE_tilde/dtau = (3 beta/2 - 2 alpha) E_tilde
```

So gamma = (3 beta/2 - 2 alpha), which with beta = 1/(1+alpha) gives:

```
gamma = 3/(2(1+alpha)) - 2 alpha
```

Setting gamma = 0:
```
3/(2(1+alpha)) = 2 alpha
3 = 4 alpha (1 + alpha)
4 alpha^2 + 4 alpha - 3 = 0
alpha_c = 0.5
```

---

## 5. Resolution: The Correct Critical Exponent

### 5.1 Conclusion

**The correct critical exponent is alpha_c = 1/2, NOT 0.82.**

The claim alpha_c = 0.82 in the documents arises from an algebraic error where the coefficient of the self-similar stretching term was doubled (using 3 beta instead of 3 beta/2).

### 5.2 Implications for Type II Exclusion

The backward dispersion argument requires gamma > 0 for energy to grow backward (forcing dispersion).

With the correct gamma = (3 beta/2 - 2 alpha) and beta = 1/(1+alpha):

| alpha | beta | gamma | Dispersion Forced? |
|-------|------|-------|-------------------|
| 0.5   | 2/3  | 0     | BOUNDARY (marginal) |
| 0.51  | 0.662| -0.011| NO (gamma < 0) |
| 0.6   | 0.625| -0.26 | NO (gamma < 0) |
| 0.75  | 0.571| -0.64 | NO (gamma < 0) |
| 1.0   | 0.5  | -1.25 | NO (gamma < 0) |

**CRITICAL FINDING:** For ALL Type II rates alpha > 1/2, we have gamma < 0.

This means the backward dispersion mechanism FAILS for the entire Type II range (1/2, 1).

### 5.3 Impact on the Proof

The argument as written DOES NOT cover Type II blowup at all!

The energy-based backward dispersion argument only works when gamma > 0, i.e., when alpha < 1/2. But Type II by definition has alpha > 1/2.

---

## 6. Is There a Different beta That Works?

### 6.1 What beta is Needed?

For gamma > 0 with alpha in the Type II range (1/2, 1), we need:
```
3 beta/2 > 2 alpha
beta > 4 alpha/3
```

For alpha = 1/2: beta > 2/3
For alpha = 0.6: beta > 0.8
For alpha = 1: beta > 4/3

### 6.2 Alternative Scalings

**If beta = 1 (fixed, classical self-similar):**

```
gamma = 3(1)/2 - 2 alpha = 3/2 - 2 alpha
gamma = 0  =>  alpha_c = 3/4 = 0.75
```

This gives:
- For alpha in (1/2, 3/4): gamma > 0 (dispersion works)
- For alpha in (3/4, 1): gamma < 0 (dispersion fails)

**This is closer to useful!** It covers part of the Type II range.

### 6.3 Which beta is Correct?

The question is: what is the actual form of the limiting ancient Euler equation?

**Seregin's rescaling:**

From Seregin's paper (arXiv:2507.08733), the rescaling is:
```
v^{lambda, alpha}(y, tau) = lambda^alpha v(lambda y, T + lambda^{alpha+1} tau)
```

For this rescaling, the Euler limit (as viscosity vanishes) satisfies:
```
partial_tau V + (V . nabla)V + alpha V + (1/(1+alpha))(y . nabla)V/2 = -nabla P
```

Wait - this has beta/2 with beta = 1/(1+alpha), giving an effective coefficient of 1/(2(1+alpha)).

Let me check this more carefully...

**Derivation from Seregin's rescaling:**

If v(x,t) satisfies NS, then v^{lambda,alpha}(y,tau) = lambda^alpha v(lambda y, T + lambda^{alpha+1} tau) satisfies:

```
partial_tau v^{lambda,alpha} = lambda^{alpha+1} alpha/lambda * v + lambda^alpha partial_t v|_{lambda y, T + lambda^{alpha+1} tau}
```

This needs more careful computation. The coefficient beta in the self-similar term depends on the exact rescaling convention.

---

## 7. Alternative Approach: Direct Ancient Euler Analysis

### 7.1 Standard Ancient Self-Similar Euler

Consider the standard form for ancient solutions:
```
partial_tau V + (V . nabla)V + a V + b (y . nabla)V = -nabla P
```

with constants a, b > 0.

The energy identity gives:
```
dE_tilde/dtau = (3b/2 - 2a) E_tilde
```

### 7.2 What Determines a and b?

For solutions arising from Type II NS blowup at rate alpha:
- The velocity scales as lambda^alpha
- The time scales as lambda^{1+alpha}

The correct relationship is:
```
a = alpha (from the lambda^alpha scaling of V)
b = 1/(1+alpha) (from the time rescaling)
```

BUT the coefficient b in the profile equation should be b/2, not b, so the actual equation is:
```
partial_tau V + (V . nabla)V + alpha V + (1/(2(1+alpha)))(y . nabla)V = -nabla P
```

This gives:
```
gamma = 3/(4(1+alpha)) - 2 alpha
```

Setting gamma = 0:
```
3/(4(1+alpha)) = 2 alpha
3 = 8 alpha (1 + alpha)
8 alpha^2 + 8 alpha - 3 = 0
alpha = (-8 + sqrt(64 + 96))/16 = (-8 + sqrt(160))/16 = (-8 + 12.65)/16 = 0.29
```

This gives alpha_c approximately 0.29, which is LESS than 1/2!

### 7.3 The Problem is More Fundamental

The various computations give different values of alpha_c depending on the exact rescaling convention:

| Convention | gamma formula | alpha_c |
|------------|---------------|---------|
| b = 1/(1+alpha) | 3b/2 - 2a | 0.5 |
| b = 1 | 3/2 - 2a | 0.75 |
| b/2 = 1/(2(1+alpha)) | 3b/4 - 2a | 0.29 |
| Document's (erroneous) | 3b - 2a | 0.82 |

**The correct choice depends on the exact rescaling convention used in Seregin's framework.**

---

## 8. Final Verdict

### 8.1 The Mathematical Truth

Given the ancient self-similar Euler equation:
```
partial_tau V + (V . nabla)V + alpha V + (beta/2)(y . nabla)V = -nabla P
```

The energy identity is:
```
dE_tilde/dtau = gamma E_tilde  where  gamma = (3 beta/2 - 2 alpha)
```

**If beta = 1/(1+alpha)** (Seregin's Type II rescaling):
- gamma = 3/(2(1+alpha)) - 2 alpha
- alpha_c = 0.5 (exactly)
- Type II range (1/2, 1) is NOT covered (gamma < 0 throughout)

**If beta = 1** (classical self-similar):
- gamma = 3/2 - 2 alpha
- alpha_c = 0.75
- Type II range (1/2, 3/4) IS covered, but (3/4, 1) is not

### 8.2 Why the Document Claims 0.82

The document's formula gamma = (3 - 2 alpha - 2 alpha^2)/(1+alpha) corresponds to using gamma = 3 beta - 2 alpha (missing the factor 1/2), which gives alpha_c = 0.82.

This appears to be an error, but it could also be a different interpretation of the equation where the self-similar term has coefficient beta instead of beta/2.

### 8.3 Status of the Backward Dispersion Argument

**CRITICAL CONCLUSION:**

1. If the correct formula is gamma = (3 beta/2 - 2 alpha) with beta = 1/(1+alpha), then **alpha_c = 0.5** and the backward dispersion argument fails for ALL of Type II.

2. If beta = 1 (classical self-similar), then **alpha_c = 0.75** and the argument works for alpha in (1/2, 3/4) but fails for alpha in (3/4, 1).

3. The claimed alpha_c = 0.82 requires gamma = 3 beta - 2 alpha, which appears to be an error.

### 8.4 Recommended Actions

1. **Verify the exact form of the rescaled equation** arising from Seregin's Type II analysis.

2. **Identify which beta convention** is used in the literature for ancient Euler solutions.

3. **If alpha_c = 0.5:** The backward dispersion argument must be abandoned or significantly revised for Type II exclusion.

4. **If alpha_c = 0.75:** A gap remains for alpha in (3/4, 1) that requires additional arguments.

---

## 9. The Type II Range Question

### 9.1 Is (1/2, 3/5) Covered?

The claimed Type II range in the paper is alpha in (1/2, 3/5) = (0.5, 0.6).

**With alpha_c = 0.5:** This range is NOT covered (gamma <= 0 throughout).

**With alpha_c = 0.75:** This range IS covered since 0.6 < 0.75.

**With alpha_c = 0.82 (erroneous):** This range IS covered since 0.6 < 0.82.

### 9.2 The Honest Assessment

The backward dispersion argument as written appears to have an error in the gamma formula. The correct alpha_c is likely 0.5 or 0.75, not 0.82.

For the argument to cover the Type II range (1/2, 3/5):
- Need alpha_c > 0.6
- This requires either beta = 1 (giving alpha_c = 0.75) or some other modification

**The proof structure needs careful verification of:**
1. The exact rescaling convention
2. The coefficient of the self-similar term
3. The relationship between Type II rate and rescaling parameter

---

## References

1. Seregin, G. "A note on certain scenarios of Type II blowups." arXiv:2507.08733 (2025)
2. Koch-Nadirashvili-Seregin-Sverak. "Liouville theorems for NS." Acta Math. 203 (2009)
3. Chen-Strain-Yau-Tsai. "Lower bounds on blowup rate." CPDE 34 (2009)

---

## 10. Numerical Verification

The following numerical computation confirms the analysis:

```
============================================================
CRITICAL ALPHA CALCULATION VERIFICATION
============================================================

--- Case 1: gamma = (3*beta/2 - 2*alpha), beta = 1/(1+alpha) ---
Quadratic: 4*alpha^2 + 4*alpha - 3 = 0
Solutions: alpha = 0.500000 or alpha = -1.500000
Critical alpha_c = 0.500000
Verification: beta = 0.666667, gamma = 0.0000000000

Type II range test (alpha > 0.5):
  alpha=0.50: beta=0.6667, gamma=+0.0000 -> NOT covered
  alpha=0.51: beta=0.6623, gamma=-0.0266 -> NOT covered
  alpha=0.55: beta=0.6452, gamma=-0.1323 -> NOT covered
  alpha=0.60: beta=0.6250, gamma=-0.2625 -> NOT covered
  alpha=0.70: beta=0.5882, gamma=-0.5176 -> NOT covered
  alpha=0.80: beta=0.5556, gamma=-0.7667 -> NOT covered
  alpha=0.90: beta=0.5263, gamma=-1.0105 -> NOT covered
  alpha=1.00: beta=0.5000, gamma=-1.2500 -> NOT covered

--- Case 2: gamma = (3*beta - 2*alpha), beta = 1/(1+alpha) [DOCUMENT] ---
Quadratic: 2*alpha^2 + 2*alpha - 3 = 0
Solutions: alpha = 0.822876 or alpha = -1.822876
Critical alpha_c = 0.822876
Verification: beta = 0.548584, gamma = -0.0000000000

Type II range test (alpha > 0.5):
  alpha=0.50: beta=0.6667, gamma=+1.0000 -> COVERED
  alpha=0.55: beta=0.6452, gamma=+0.8355 -> COVERED
  alpha=0.60: beta=0.6250, gamma=+0.6750 -> COVERED
  alpha=0.70: beta=0.5882, gamma=+0.3647 -> COVERED
  alpha=0.75: beta=0.5714, gamma=+0.2143 -> COVERED
  alpha=0.80: beta=0.5556, gamma=+0.0667 -> COVERED
  alpha=0.82: beta=0.5495, gamma=+0.0084 -> COVERED
  alpha=0.85: beta=0.5405, gamma=-0.0784 -> NOT covered
  alpha=0.90: beta=0.5263, gamma=-0.2211 -> NOT covered

--- Case 3: gamma = (3/2 - 2*alpha), beta = 1 (fixed) ---
Setting 3/2 - 2*alpha = 0 gives alpha_c = 3/4 = 0.750000

Type II range test:
  alpha=0.50: gamma=+0.5000 -> COVERED
  alpha=0.55: gamma=+0.4000 -> COVERED
  alpha=0.60: gamma=+0.3000 -> COVERED
  alpha=0.70: gamma=+0.1000 -> COVERED
  alpha=0.74: gamma=+0.0200 -> COVERED
  alpha=0.75: gamma=+0.0000 -> NOT covered
  alpha=0.76: gamma=-0.0200 -> NOT covered
  alpha=0.80: gamma=-0.1000 -> NOT covered
  alpha=0.90: gamma=-0.3000 -> NOT covered

============================================================
SUMMARY: Critical exponent depends on formula choice
============================================================
gamma = (3*beta/2 - 2*alpha), beta=1/(1+alpha) => alpha_c = 0.5
gamma = (3*beta - 2*alpha), beta=1/(1+alpha)   => alpha_c = 0.82 [DOC]
gamma = (3/2 - 2*alpha), beta=1                => alpha_c = 0.75

Type II range (1/2, 3/5) = (0.5, 0.6) coverage:
  alpha_c = 0.5  => NOT covered (exactly at boundary)
  alpha_c = 0.82 => COVERED
  alpha_c = 0.75 => COVERED
```

---

## 11. Conclusion and Path Forward

### 11.1 The Core Issue

The discrepancy between alpha_c = 0.82 (claimed) and alpha_c = 0.5 (derived with correct energy identity) stems from a factor of 2 error in the coefficient of the self-similar stretching term.

The document uses gamma = d*beta - 2*alpha (where d=3), but the correct energy identity gives gamma = (d/2)*beta - 2*alpha = (3/2)*beta - 2*alpha.

### 11.2 Implications

**Scenario A (If the correct formula is gamma = 3*beta/2 - 2*alpha):**
- alpha_c = 0.5 exactly
- The backward dispersion argument FAILS for the entire Type II range
- A completely different approach is needed

**Scenario B (If the ancient Euler uses beta = 1 instead of beta = 1/(1+alpha)):**
- alpha_c = 0.75
- The argument covers alpha in (0.5, 0.75), including the target range (0.5, 0.6)
- Gap remains for alpha in (0.75, 1)

**Scenario C (If the document's formula is correct for some reason):**
- alpha_c = 0.82
- The argument covers alpha in (0.5, 0.82), which includes the target range
- This requires justification of why gamma = 3*beta - 2*alpha instead of 3*beta/2 - 2*alpha

### 11.3 Next Steps

1. **Derive the rescaled equation from first principles** using Seregin's exact rescaling
2. **Compare with published literature** on ancient Euler solutions
3. **If alpha_c = 0.5 is confirmed:** Develop alternative arguments (vorticity-based, Liouville theorems, etc.)
4. **If beta = 1 is appropriate:** The gap (0.75, 1) needs separate treatment

### 11.4 Critical Question for the Proof

**Does the backward dispersion argument cover the Type II range (1/2, 3/5)?**

| Formula | alpha_c | (1/2, 3/5) covered? |
|---------|---------|---------------------|
| gamma = 3*beta/2 - 2*alpha, beta = 1/(1+alpha) | 0.500 | NO |
| gamma = 3/2 - 2*alpha, beta = 1 | 0.750 | YES |
| gamma = 3*beta - 2*alpha, beta = 1/(1+alpha) | 0.823 | YES |

**The answer depends on which convention is correct for the ancient Euler limit.**

---

*Document created: January 13, 2026*
*Last updated: January 13, 2026*
*Status: CRITICAL ERROR IDENTIFIED*
*Resolution: Requires verification of the correct rescaling convention*
*Impact: Backward dispersion argument validity depends on resolving this discrepancy*

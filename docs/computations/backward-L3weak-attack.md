# Closing the Backward L^{3,∞} Gap

## The Problem

**Goal:** Prove that no backward self-similar profile exists in L^{3,∞}(ℝ³).

**Known:**
- Backward L² ruled out (Theorem E, velocity method)
- Backward L³ ruled out (NRŠ 1996)
- Forward L^{3,∞} ruled out (Theorem D, gradient decay)

**Gap:** L³ ⊂ L^{3,∞} but L^{3,∞} \ L³ is non-empty.

---

## 1. Review: Why Current Methods Fail

### 1.1 Velocity Method
For backward: -ν||∇U||² - (1/4)||U||² = 0

Requires ||U||² < ∞, which fails for U ∈ L^{3,∞} with |U| ~ r^{-1}.

### 1.2 Vorticity Method
For backward: -ν||∇Ω||² + (7/4)||Ω||² = 0

This is NOT definite sign (terms have opposite signs).

### 1.3 Forward Gradient Decay
For forward, we showed |∇U| = O(r^{-2}) even when |U| = O(r^{-1}).

**Question:** Does the same hold for backward?

---

## 2. Gradient Decay for Backward

### 2.1 Backward Asymptotic Structure

The backward profile equation:
```
ν∆U + (U·∇)U + U/2 + (y·∇)U/2 = ∇P
```

At large r with U ~ U₀(ŷ)/r:

**Self-similar terms:**
- U/2 ~ U₀/(2r)
- (y·∇)U/2 ~ (r∂_r)(U₀/r)/2 = -U₀/(2r)

These CANCEL (just like forward)!

**Key observation:** The leading-order cancellation is the SAME for forward
and backward. The difference is only in subleading terms.

### 2.2 Derivative Decay

If U = U₀(ŷ)/r + O(r^{-1-δ}) for backward (same expansion as forward), then:
```
∇U = O(r^{-2})
```

**This places Ω ∈ L² for backward as well!**

### 2.3 The Catch

For forward, Ω ∈ L² + vorticity identity → Ω = 0.

For backward, Ω ∈ L² but vorticity identity has WRONG sign:
```
-ν||∇Ω||² + (7/4)||Ω||² = 0
```

This gives ν||∇Ω||² = (7/4)||Ω||², a CONSTRAINT, not a contradiction.

---

## 3. New Approach: Mixed Velocity-Vorticity

### 3.1 Idea

Combine velocity and vorticity information to get definite sign.

For backward, define the combined functional:
```
F[U] = α||U||²_w + β||Ω||²
```

where α, β are constants and w is a weight.

### 3.2 Evolution Under the Equation

From velocity identity (weighted):
```
-ν∫|∇U|²w + (stuff)||U||²_w + cross terms = 0
```

From vorticity identity:
```
-ν||∇Ω||² + (7/4)||Ω||² = 0
```

Can we choose α, β, w such that the combination has definite sign?

### 3.3 The Constraint

We need:
```
α × (velocity coefficient) + β × (7/4) < 0
```

For velocity: coefficient depends on weight w.
For vorticity: coefficient is +7/4 > 0.

If we can make velocity coefficient negative enough with appropriate w,
and choose α/β correctly, we might get overall negative coefficient.

---

## 4. Weighted Velocity for Backward

### 4.1 Backward with Weight w = |y|^{-2α}

Multiply backward equation by U|y|^{-2α}:

**Viscous:** -ν∫|∇U|²|y|^{-2α} - ν∫∇U·U·∇(|y|^{-2α})

**Nonlinear:** 0 (by ∇·U = 0)

**Linear:** (1/2)∫|U|²|y|^{-2α}

**Self-similar:** (1/2)∫(y·∇)U·U|y|^{-2α}

Let me compute the self-similar term:
```
∫(y·∇)U·U|y|^{-2α} = (1/2)∫(y·∇)|U|²|y|^{-2α}
```

Integration by parts:
```
= -(1/2)∫|U|²∇·(y|y|^{-2α})
= -(1/2)∫|U|²[3|y|^{-2α} + y·(-2α)|y|^{-2α-2}y]
= -(1/2)∫|U|²|y|^{-2α}[3 - 2α]
= -(3-2α)/2 · ||U||²_w
```

where ||U||²_w = ∫|U|²|y|^{-2α}.

### 4.2 Combined Coefficient

The |U|²_w coefficient is:
```
1/2 + (1/2)·(-(3-2α)/2) = 1/2 - (3-2α)/4 = (2 - 3 + 2α)/4 = (2α-1)/4
```

For α > 1/2: coefficient is POSITIVE (bad)
For α < 1/2: coefficient is NEGATIVE (good!)
For α = 1/2: coefficient is ZERO

### 4.3 But There's a Problem

For α < 1/2, the weight |y|^{-2α} is GROWING at infinity.

The integral ||U||²_w = ∫|U|²|y|^{-2α} might not converge for U ∈ L^{3,∞}.

For |U| ~ r^{-1} and weight r^{-2α}:
```
∫|U|²|y|^{-2α} ~ ∫r^{-2}·r^{-2α}·r² dr = ∫r^{-2α} dr
```

This converges at infinity only for α > 1/2!

**Catch-22:** We need α < 1/2 for negative coefficient but α > 1/2 for convergence.

---

## 5. Different Approach: Interpolation

### 5.1 The Interpolation Idea

NRŠ works in L³. Our backward L² result works. Can we interpolate?

The space L^{3,∞} is "between" L³ and weaker spaces.

**Lorentz space interpolation:**
- (L², L³)_{θ,q} for appropriate θ, q
- Maybe we can interpolate the non-existence results?

### 5.2 The Issue

Non-existence is not a linear property that interpolates simply.

The argument structure is:
- L²: velocity energy identity
- L³: NRŠ integral identity

These are DIFFERENT methods. Interpolation of results is not straightforward.

---

## 6. Approach: Imitate NRŠ in Lorentz Spaces

### 6.1 The NRŠ Method

NRŠ derive an identity using multiplier y × U (or similar). The specific
structure of L³ (scale invariance: ||λU(λ·)||₃ = ||U||₃) is exploited.

### 6.2 L^{3,∞} Structure

The Lorentz space L^{3,∞} also has scaling properties:
```
||λU(λ·)||_{3,∞} = ||U||_{3,∞}
```

This is the SAME scaling! So the structural argument might adapt.

### 6.3 The Technical Issue

NRŠ use Hölder inequalities specific to L^p. For Lorentz spaces, the
analogous inequalities are:

For L^{p,q} × L^{p',q'} → L^{1,r}:
```
||fg||_{1,r} ≤ C||f||_{p,q}||g||_{p',q'}
```

with appropriate exponent relations.

The weak-L³ case (p=3, q=∞) has weaker product estimates.

---

## 7. Direct Attack: Vorticity + Biot-Savart

### 7.1 Idea

Even if vorticity identity doesn't force Ω = 0, we can analyze what
the constraint ν||∇Ω||² = (7/4)||Ω||² implies.

### 7.2 Spectral Interpretation

The constraint says Ω is an "eigenfunction" of:
```
ν∆Ω = (7/4)Ω  (in some generalized sense)
```

On ℝ³, the Laplacian has continuous spectrum [0, ∞). The "eigenvalue" 7/(4ν)
would need to be in the spectrum.

### 7.3 The Asymptotic Constraint

For Ω satisfying ν||∇Ω||² = (7/4)||Ω||² with Ω ∈ L²:

By the Poincaré-type inequality on ℝ³... wait, there's no Poincaré on ℝ³.

But there IS a constraint from the decay. For Ω ~ r^{-β} at infinity:
```
||∇Ω||² ~ ∫r^{-2β-2}r²dr = ∫r^{-2β}dr  (converges for β > 1/2)
||Ω||² ~ ∫r^{-2β}r²dr = ∫r^{2-2β}dr    (converges for β > 3/2)
```

The ratio ||∇Ω||²/||Ω||² depends on β:
```
ratio ~ ∫r^{-2β}dr / ∫r^{2-2β}dr
```

For β close to 2 (from our gradient decay): ratio → ∞ as cutoffs removed.

This suggests the constraint ν||∇Ω||² = (7/4)||Ω||² might not be satisfiable!

### 7.4 Making This Precise

**Claim:** For Ω ∈ L²(ℝ³) with |Ω| ~ r^{-2} at infinity, the ratio
||∇Ω||²/||Ω||² is unbounded (→ ∞).

**Argument:**
Take Ω with |Ω| = f(r) r^{-2} where f is a smooth cutoff (f=1 for r<R, f=0 for r>2R).

Then:
```
||Ω||² ~ ∫_1^R r^{-4}·r² dr = ∫_1^R r^{-2}dr ~ log R
||∇Ω||² ~ ∫_1^R r^{-6}·r² dr + boundary ~ ∫_1^R r^{-4}dr ~ R^{-3} + (stuff at R)
```

Hmm, this doesn't immediately give the right behavior. Let me reconsider.

Actually, for |Ω| ~ r^{-2} exactly:
```
|∇Ω| ~ r^{-3}
||∇Ω||² ~ ∫r^{-6}·r²dr = ∫r^{-4}dr ~ R^{-1} (as R → ∞, from r=1 to R)
||Ω||² ~ ∫r^{-4}·r²dr = ∫r^{-2}dr ~ log R
```

So ||∇Ω||²/||Ω||² ~ 1/(R log R) → 0 as R → ∞.

This is the OPPOSITE of what I claimed! The ratio goes to ZERO.

### 7.5 Reinterpretation

For Ω ~ r^{-2} with Ω ∈ L²:
```
||∇Ω||²/||Ω||² → 0  as we include larger domains
```

The backward constraint ν||∇Ω||² = (7/4)||Ω||² requires this ratio to be 7/(4ν).

For the ratio to be a FIXED positive constant, Ω cannot have pure r^{-2} decay.

**This might force specific structure on Ω!**

---

## 8. Structural Constraint on Backward Profiles

### 8.1 The Constraint Equation

For backward profiles with Ω ∈ L²:
```
ν||∇Ω||² = (7/4)||Ω||²
```

### 8.2 Scaling Analysis

Consider Ω_λ(y) = λ²Ω(λy). Then:
```
||Ω_λ||² = λ⁴ ∫|Ω(λy)|² dy = λ⁴ · λ^{-3} ||Ω||² = λ||Ω||²
||∇Ω_λ||² = λ⁴ · λ² ∫|∇Ω(λy)|² dy = λ³||∇Ω||²
```

So:
```
||∇Ω_λ||²/||Ω_λ||² = λ² · ||∇Ω||²/||Ω||²
```

The ratio SCALES with λ²!

### 8.3 Consequence

If Ω satisfies ν||∇Ω||² = (7/4)||Ω||², then Ω_λ satisfies:
```
ν||∇Ω_λ||² = λ² · (7/4)||Ω_λ||²
```

For the equation to be satisfied for ALL λ, we'd need the coefficient to
be independent of λ. But it's not!

**This means:** A non-trivial Ω satisfying the constraint cannot be
scale-invariant in the sense that rescalings also satisfy it.

### 8.4 But Wait...

The backward PROFILE is supposed to be a FIXED function U (not a family).
The constraint just needs to hold for that ONE Ω.

So the scaling argument doesn't immediately rule out existence.

---

## 9. Another Angle: Helicity

### 9.1 Helicity Definition

For velocity U with vorticity Ω:
```
H = ∫U·Ω dy
```

Helicity is conserved by ideal (inviscid) flow and is a topological invariant.

### 9.2 Helicity for Self-Similar

For self-similar profiles, compute H:

With U ~ r^{-1} and Ω ~ r^{-2}:
```
H = ∫U·Ω ~ ∫r^{-3}·r² dr = ∫r^{-1}dr = log divergent
```

Helicity is ILL-DEFINED for L^{3,∞} profiles!

### 9.3 Regularized Helicity

Consider H_R = ∫_{|y|<R} U·Ω.

For backward profiles:
```
H_R ~ log R → ∞
```

This growing helicity is a structural feature of profiles in L^{3,∞}.

### 9.4 Does This Help?

The helicity growth doesn't directly contradict anything, but it shows
L^{3,∞} profiles have unusual topological properties.

---

## 10. Summary of Attempts

| Approach | Status | Issue |
|----------|--------|-------|
| Weighted velocity | Failed | Need α > 1/2 for convergence, α < 1/2 for sign |
| Interpolation | Unclear | Non-linear problem, methods don't interpolate |
| NRŠ in Lorentz | Possible | Need weak-type product estimates |
| Rayleigh quotient | Inconclusive | Ratio → 0 for r^{-2} decay, not contradiction |
| Helicity | Structural | Divergent helicity, but not contradiction |

### The Core Difficulty

The backward case has "inward drift" (+(y·∇)U/2) that supports concentration.
This makes the energy structure work AGAINST us.

The only remaining path seems to be:
1. Adapt NRŠ integral identity to L^{3,∞} (technical)
2. Find a completely new multiplier
3. Use properties specific to NS (not just energy)

---

## 11. Attempt: The NRŠ Identity in Detail

Let me try to understand NRŠ more carefully and see if it adapts.

### 11.1 NRŠ Setup

NRŠ use the identity (for backward, their signs might differ):

Multiply profile equation by |U|U (or U|U|) and integrate.

The key is that ∫|U|³ appears, and they show it must equal zero.

### 11.2 Attempting for L^{3,∞}

For U ∈ L^{3,∞}:
- ∫|U|³ might not converge (|U| ~ r^{-1} gives ∫r^{-3}r² dr ~ log R)
- The NRŠ identity becomes R-dependent

### 11.3 Localized NRŠ

Consider ∫_{B_R} |U|³ and track the R-dependence.

The NRŠ identity would give:
```
∫_{B_R} |U|³ = [boundary terms at ∂B_R] + [lower order]
```

As R → ∞:
- LHS ~ log R (for |U| ~ r^{-1})
- RHS: boundary terms are O(R² · R^{-3}) = O(R^{-1}) → 0

**Contradiction!** LHS → ∞ but RHS → 0.

Wait, is this right? Let me check more carefully...

### 11.4 Detailed NRŠ Calculation

The NRŠ identity (schematically) is:
```
∫|U|³ = ν ∫ (∇U)·(something involving U)
```

The RHS involves ∫|∇U||U|² or similar.

For |U| ~ r^{-1} and |∇U| ~ r^{-2}:
```
∫|∇U||U|² ~ ∫r^{-2}·r^{-2}·r² dr = ∫r^{-2}dr < ∞
```

So RHS is FINITE while LHS (if we had ∫|U|³) would be log-divergent.

**But wait:** NRŠ work in L³ where ∫|U|³ < ∞.

For L^{3,∞}, we need to be more careful...

### 11.5 The Lorentz Space Integral

For U ∈ L^{3,∞}, the integral ∫|U|³ doesn't converge absolutely.

But we can define:
```
lim_{R→∞} ∫_{B_R} |U|³  (possibly with logs)
```

The NRŠ identity might give:
```
∫_{B_R} |U|³ = C (finite) + o(1) as R → ∞
```

If LHS grows like log R, we need RHS to also grow like log R.

**Key question:** Does the NRŠ RHS grow like log R for |U| ~ r^{-1}?

---

## 12. Computing the NRŠ Growth Rate

### 12.1 The NRŠ Right-Hand Side

From NRŠ (adapted to backward):
```
∫|U|³ = -ν ∫∇|U|·∇(|U|U) + (other terms)
```

The other terms involve the profile equation structure.

### 12.2 Growth Analysis

For |U| = f(r)/r with f bounded:
```
∇|U| ~ r^{-2}
∇(|U|U) ~ |U|∇U + U∇|U| ~ r^{-3}
∫∇|U|·∇(|U|U) ~ ∫r^{-5}·r² dr = ∫r^{-3}dr ~ R^{-2} → 0
```

So the NRŠ RHS → 0 as R → ∞!

But ∫_{B_R} |U|³ ~ log R → ∞.

### 12.3 Conclusion

**The NRŠ identity gives a contradiction for backward L^{3,∞}!**

The identity forces:
```
log R ~ 0  as R → ∞
```

This is impossible, so no backward profile in L^{3,∞} can exist.

---

## 13. Making This Rigorous

### 13.1 Theorem Statement

**Theorem F (Backward Non-Existence in L^{3,∞}):**
For any ν > 0, the only smooth backward self-similar profile
U ∈ L^{3,∞}(ℝ³) is U = 0.

### 13.2 Proof Outline

1. Establish gradient decay: |∇U| = O(r^{-2}) (same as forward)

2. Apply localized NRŠ identity on B_R

3. Show LHS ∫_{B_R} |U|³ ~ c log R for some c > 0

4. Show RHS → finite limit as R → ∞

5. Contradiction for non-trivial U.

### 13.3 Details Needed

- Verify the NRŠ identity applies to backward case
- Compute all terms carefully with correct signs
- Handle boundary terms

---

## 14. Verification

Let me verify the NRŠ identity structure more carefully...

[To be continued with detailed computation]

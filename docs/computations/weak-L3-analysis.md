# Weak-L³ Extension: Attacking the Critical Space

## Goal

Extend our non-existence result from L²(ℝ³) to the scale-critical space
L^{3,∞}(ℝ³) (weak-L³, Lorentz space).

**Why this matters:** L^{3,∞} is the largest space where self-similar profiles
make sense dimensionally. Success here would be a major advance.

---

## 1. The Critical Space

### 1.1 Definition of Weak-L³

A function f belongs to L^{3,∞}(ℝ³) if:
```
||f||_{L^{3,∞}} := sup_{λ>0} λ · |{x : |f(x)| > λ}|^{1/3} < ∞
```

Equivalently, the distribution function satisfies:
```
|{x : |f(x)| > λ}| ≤ C/λ³
```

### 1.2 Key Property: Power-Law Decay

For f ∈ L^{3,∞}(ℝ³), we can have:
```
|f(x)| ~ |x|^{-1}  as |x| → ∞
```

This is EXACTLY the self-similar scaling:
```
u(x,t) = (T-t)^{-1/2} U(x/√(T-t))
```

implies |U(y)| ~ |y|^{-1} at large |y| is dimensionally consistent.

### 1.3 Why L² Methods Fail

For U ~ |y|^{-1}:
```
∫|U|² dy ~ ∫ r^{-2} · r² dr = ∫ dr = ∞  (logarithmic divergence)
```

Our energy identity -ν||∇δΩ||² - (1/4)||δΩ||² = 0 requires finite L² norms.

---

## 2. Approach 1: Localized Energy

### 2.1 Energy on Balls

Define the localized energy on B_R:
```
E_R[U] := ∫_{B_R} |U|² dy
```

For U ∈ L^{3,∞} with |U| ~ |y|^{-1}:
```
E_R[U] ~ ∫_0^R r^{-2} · r² dr = R
```

So E_R grows linearly with R.

### 2.2 Localized Energy Identity

Multiply the profile equation by U · χ_R (where χ_R is a cutoff) and integrate:

```
ν∫ ∆U · U χ_R - ∫(U·∇)U · U χ_R - (1/2)∫|U|² χ_R
- (1/2)∫(y·∇)U · U χ_R - ∫∇P · U χ_R = 0
```

**Problems:**
1. Boundary terms from cutoff: ∫ ∇χ_R · ... appear
2. These boundary terms are O(R^{-1}) × (surface integral)
3. For |U| ~ R^{-1} on ∂B_R, boundary terms are O(1), not vanishing

### 2.3 Refined Cutoff Analysis

Let χ_R be smooth with χ_R = 1 on B_R, χ_R = 0 outside B_{2R}, |∇χ_R| ≤ C/R.

**Viscous term:**
```
∫ ν∆U · U χ_R = -ν∫|∇U|² χ_R - ν∫∇U · U · ∇χ_R
```

The boundary term:
```
|ν∫∇U · U · ∇χ_R| ≤ (ν/R) ∫_{R<|y|<2R} |∇U| |U| dy
```

For |U| ~ r^{-1} and |∇U| ~ r^{-2}:
```
~ (ν/R) ∫_R^{2R} r^{-3} · r² dr ~ ν log(2)
```

This is O(1), not vanishing as R → ∞!

**Conclusion:** Simple localization doesn't work.

---

## 3. Approach 2: Weighted Spaces

### 3.1 Weight Function

Define weight w(y) = (1 + |y|²)^{-α/2} for some α > 0.

Consider the weighted norm:
```
||U||²_w := ∫ |U|² w dy
```

For |U| ~ |y|^{-1}:
```
||U||²_w ~ ∫ r^{-2} · r^{-α} · r² dr = ∫ r^{-α} dr
```

This converges for α > 1.

### 3.2 Weighted Energy Identity

Multiply profile equation by U · w and integrate:

```
∫ [ν∆U - (U·∇)U - U/2 - (y·∇)U/2 - ∇P] · U w dy = 0
```

**Viscous term:**
```
∫ ν∆U · Uw = -ν∫|∇U|² w - ν∫∇U · U · ∇w
```

The cross term involves ∇w = -α y (1+|y|²)^{-α/2-1}:
```
∫ ∇U · U · ∇w ~ ∫ |y|^{-2} · |y|^{-1} · |y|^{-α} · |y| · r² dr
                ~ ∫ r^{-α} dr
```

This converges for α > 1 but introduces new terms.

**Self-similar term:**
```
∫ (y·∇)U · Uw = (1/2)∫ (y·∇)|U|² w = -(1/2)∫|U|² (3w + y·∇w)
```

Computing y·∇w = -α|y|² (1+|y|²)^{-α/2-1}:
```
3w + y·∇w = (1+|y|²)^{-α/2-1} [3(1+|y|²) - α|y|²]
          = (1+|y|²)^{-α/2-1} [3 + (3-α)|y|²]
```

For α = 3: this is 3(1+|y|²)^{-5/2}, giving positive coefficient.
For α > 3: the |y|² term is negative at large |y|.

### 3.3 Weighted Identity Structure

With α = 3, we get (after careful computation):

```
-ν∫|∇U|²w + [viscous cross terms] + c₁∫|U|²w + [nonlinear terms] = 0
```

**Challenge:** The nonlinear term ∫(U·∇)U · Uw doesn't vanish because the
weight breaks the divergence-free cancellation.

For incompressible U:
```
∫(U·∇)U · U = 0  (standard)
∫(U·∇)U · Uw ≠ 0  (weight breaks symmetry)
```

---

## 4. Approach 3: Vorticity in Weak Spaces

### 4.1 Vorticity Decay

If U ∈ L^{3,∞} with |U| ~ r^{-1}, then:
```
|Ω| = |∇ × U| ~ r^{-2}
```

So Ω ∈ L^{3/2,∞} (weaker space).

### 4.2 Vorticity Energy

For Ω ~ r^{-2}:
```
∫|Ω|² dy ~ ∫ r^{-4} · r² dr = ∫ r^{-2} dr
```

This CONVERGES! The vorticity is in L².

**Key Observation:** Even if U ∈ L^{3,∞} \ L², we might have Ω ∈ L².

### 4.3 Vorticity-Based Argument

If we can show Ω ∈ L² for any profile U ∈ L^{3,∞}, then our original
vorticity energy identity applies:

```
-ν||∇Ω||² - (1/4)||Ω||² = 0  ⟹  Ω = 0
```

**But:** Does Ω = 0 with U ∈ L^{3,∞} imply U = 0?

For U curl-free, div-free, and in L^{3,∞}:
- U = ∇φ with ∆φ = 0
- φ harmonic with |∇φ| ~ r^{-1}

**Liouville-type theorem:** A harmonic function on ℝ³ with |∇φ| ~ r^{-1}
must have φ ~ log r (in 3D, actually φ ~ r^{-1} or const).

Wait, let me reconsider. In 3D:
- Harmonic functions with |∇φ| ∈ L^{3,∞} exist (e.g., φ = c/|x|)
- These give ∇φ ~ r^{-2}, not r^{-1}

For |∇φ| ~ r^{-1}, we need φ ~ log r, but log is not harmonic in 3D.

**Conclusion:** Curl-free, div-free fields in L^{3,∞}(ℝ³) must decay faster
than r^{-1}, hence are actually in L^{3-ε} for some ε > 0, hence in L².

This suggests the Helmholtz argument might extend!

### 4.4 Refined Helmholtz for L^{3,∞}

**Claim:** If U ∈ L^{3,∞}(ℝ³) with ∇ × U = 0 and ∇ · U = 0, then U = 0.

**Proof attempt:**

1. U = ∇φ for some φ (curl-free)
2. ∆φ = 0 (div-free)
3. |∇φ| ∈ L^{3,∞} means |∇φ(x)| ≲ |x|^{-1}

For a harmonic function φ on ℝ³:
- If |∇φ| ≲ |x|^{-1}, then by gradient estimates for harmonic functions:
  |∇²φ(x)| ≲ |x|^{-2}

- By Liouville theorem: harmonic functions with polynomial growth are polynomials
- A polynomial with |∇p| ≲ |x|^{-1} must have ∇p = 0 (constants don't work,
  degree ≥ 1 gives |∇p| ~ |x|^{k} for some k ≥ 0)

Wait, this argument has a gap. Let me reconsider.

**Better approach:** Use the representation formula.

For harmonic φ with ∇φ ∈ L^{3,∞}:
```
φ(x) = ∫ K(x-y) f(y) dy  (for some source f)
```

But ∆φ = 0 means no source, so φ is determined by behavior at infinity.

In ℝ³, harmonic functions with |∇φ| → 0 at infinity must be constant.

**Why |∇φ| → 0:** If |∇φ| ~ c/|x| with c ≠ 0, then:
```
φ(x) = φ(0) + ∫_0^{|x|} (∂_r φ) dr ~ φ(0) + c log|x|
```

But log|x| is NOT harmonic in 3D (it's harmonic in 2D only).

In 3D, radial harmonic functions are φ = a + b/|x|, giving |∇φ| ~ |x|^{-2}.

**Conclusion:** No non-constant harmonic function in ℝ³ has |∇φ| ~ |x|^{-1}.

Therefore: ∇ × U = 0, ∇ · U = 0, U ∈ L^{3,∞} ⟹ U = 0. ✓

---

## 5. The Critical Argument

### 5.1 Strategy

1. Take U ∈ L^{3,∞} satisfying the profile equations
2. Show Ω = ∇ × U ∈ L² (vorticity has better integrability)
3. Apply our vorticity energy identity to get Ω = 0
4. Use Helmholtz for L^{3,∞} (Section 4.4) to get U = 0

### 5.2 Key Step: Ω ∈ L²

**Claim:** If U ∈ L^{3,∞}(ℝ³) satisfies the profile equations, then Ω ∈ L²(ℝ³).

**Attempt 1: Direct decay**

If |U(y)| ≤ C|y|^{-1}, then naively |Ω| ≤ C|y|^{-2}, giving:
```
∫|Ω|² ~ ∫ r^{-4} · r² dr = ∫ r^{-2} dr < ∞
```

But this assumes |∇U| ~ |U|/|y|, which isn't automatic.

**Attempt 2: Elliptic regularity**

The profile equation gives:
```
ν∆U = (U·∇)U + U/2 + (y·∇)U/2 + ∇P
```

For U ∈ L^{3,∞}, the RHS is in some Lebesgue space. By elliptic regularity:
```
U ∈ L^{3,∞} ⟹ ∆U ∈ L^{3/2,∞} ⟹ ∇²U ∈ L^{3/2,∞}
```

This gives Ω = ∇ × U with derivatives in L^{3/2,∞}.

**Attempt 3: Bootstrap regularity**

Use Sobolev embedding and bootstrap:
- U ∈ L^{3,∞} ⟹ (U·∇)U ∈ L^{3/2,∞}
- Elliptic regularity: ∆U ∈ L^{3/2,∞} ⟹ U ∈ W^{2,3/2,∞}
- Sobolev: ∇U ∈ L^{3,∞}

This doesn't immediately give Ω ∈ L².

### 5.3 The Gap

The key question: **Does U ∈ L^{3,∞} satisfying the profile equations
imply better integrability for Ω?**

**Obstacle:** The profile equation is NONLINEAR. The nonlinearity (U·∇)U
doesn't give us the needed boost.

**Possible resolution:** Use the STRUCTURE of the profile equation, not
just integrability.

---

## 6. Structure-Based Approach

### 6.1 The Profile Equation as a Fixed Point

Rewrite the profile equation:
```
U = (ν∆ - 1/2 - (y·∇)/2)^{-1} [(U·∇)U + ∇P]
```

The linear operator L = ν∆ - 1/2 - (y·∇)/2 has a specific structure.

### 6.2 Spectral Properties of L

Our linearization analysis showed:
- The operator L on vorticity has spectrum bounded away from 0
- Specifically: L_Ω = ν∆ - (y·∇)/2 - 1 satisfies the energy identity

The spectral gap is 1/4 (from the coefficient in the energy identity).

### 6.3 Implication for Weak-L³

Even if U ∈ L^{3,∞}, the profile equation implies:
```
L[U] = nonlinear terms + pressure
```

If the linear operator L has good mapping properties on L^{3,∞}, we might
bootstrap to better regularity.

**This requires careful analysis of L on Lorentz spaces.**

---

## 7. Alternative: Backward Uniqueness (ESS Approach)

### 7.1 The ESS Strategy

Escauriaza-Seregin-Šverák proved: L^∞_t L³_x bounds imply regularity.

Their method uses backward uniqueness for parabolic equations.

### 7.2 Adaptation to Self-Similar

For self-similar profiles, backward uniqueness becomes:
- The self-similar time evolution ∂v/∂τ = L[v] - (v·∇)v
- If v doesn't decay as τ → ∞, backward uniqueness says it was always non-zero
- But our linear stability shows perturbations MUST decay

This is essentially our Type I exclusion argument!

### 7.3 Connection

The ESS approach and our approach are DUAL:
- ESS: Uses backward uniqueness (forward in physical time)
- Ours: Uses forward stability (forward in self-similar time)

Both exploit the same underlying structure.

---

## 8. Current Status

### What we know:
1. Non-existence in L² (PROVEN)
2. Helmholtz decomposition works for L^{3,∞} (Section 4.4)
3. If Ω ∈ L² for profiles in L^{3,∞}, we're done

### The gap:
- Proving Ω ∈ L² for U ∈ L^{3,∞} requires additional argument
- Elliptic regularity alone doesn't suffice
- Need to exploit profile equation structure more carefully

### Promising directions:
1. **Localized vorticity estimates:** Show ||Ω||_{L²(B_R)} grows sub-linearly
2. **Spectral analysis of L on Lorentz spaces:** Map L^{3,∞} → better space
3. **Carleman estimates:** ESS-type backward uniqueness argument

---

## 9. A Partial Result

**Theorem (Conditional):**
If U ∈ L^{3,∞}(ℝ³) is a smooth self-similar profile with Ω = ∇ × U ∈ L²(ℝ³),
then U = 0.

**Proof:**
1. Apply our vorticity energy identity: -ν||∇Ω||² - (1/4)||Ω||² = 0
2. This forces Ω = 0
3. By Section 4.4, curl-free + div-free + L^{3,∞} implies U = 0. ∎

**Corollary:** Any profile in L^{3,∞} with |Ω| ≲ |y|^{-2+ε} for some ε > 0
must be trivial.

---

## 10. Summary

### Achievements:
- Identified that Helmholtz works for L^{3,∞}
- Showed that Ω ∈ L² is the key condition
- Connected to ESS backward uniqueness approach

### Remaining obstacle:
- Proving Ω ∈ L² for profiles U ∈ L^{3,∞} (without assuming extra decay)

### Assessment:
The weak-L³ extension is genuinely hard. Our L² result is likely the optimal
outcome using elementary energy methods. The critical space requires either:
- Lorentz-space elliptic regularity theory
- Carleman estimates (ESS style)
- Concentration-compactness methods

These are beyond the scope of elementary approaches.

# Backward Self-Similar Solutions (Leray Scenario)

## The Issue

Our theorems rule out **forward** self-similar blowup profiles. But Leray's
original 1934 paper considered **backward** self-similar solutions with
DIFFERENT structure. We need to analyze these separately.

---

## 1. Forward vs Backward Self-Similar

### 1.1 Forward Self-Similar (What We Proved)

For blowup at time T (approaching from below):
```
u(x,t) = (T-t)^{-1/2} U(x/√(T-t))  for t < T
```

The time derivative gives: ∂u/∂t ~ -U/(T-t) - (y·∇U)/(2(T-t))

Profile equation (after simplification):
```
ν∆U - (U·∇)U - U/2 - (y·∇)U/2 = ∇P          (Forward)
```

### 1.2 Backward Self-Similar (Leray)

For a solution defined for t > T, emanating FROM a singularity:
```
u(x,t) = (t-T)^{-1/2} U(x/√(t-T))  for t > T
```

The time derivative gives: ∂u/∂t ~ -U/(t-T) + (y·∇U)/(2(t-T))

Note the SIGN CHANGE in the (y·∇U) term!

Profile equation:
```
ν∆U + (U·∇)U + U/2 + (y·∇)U/2 = ∇P          (Backward)
```

### 1.3 Key Differences

| Term | Forward | Backward |
|------|---------|----------|
| Viscous | ν∆U | ν∆U |
| Nonlinear | -(U·∇)U | +(U·∇)U |
| Scaling | -U/2 - (y·∇)U/2 | +U/2 + (y·∇)U/2 |

The signs of nonlinear and scaling terms are REVERSED!

---

## 2. Vorticity Analysis for Backward Case

### 2.1 Backward Vorticity Equation

Taking curl of the backward profile equation:
```
ν∆Ω + (U·∇)Ω - (Ω·∇)U + (y·∇)Ω/2 + Ω = 0
```

Compare to forward:
```
ν∆Ω - (U·∇)Ω + (Ω·∇)U - (y·∇)Ω/2 - Ω = 0
```

### 2.2 Linearization at U = 0 (Backward)

Linearized backward vorticity equation:
```
ν∆δΩ + (y·∇)δΩ/2 + δΩ = 0
```

Compare to forward linearization:
```
ν∆δΩ - (y·∇)δΩ/2 - δΩ = 0
```

### 2.3 Energy Identity (Backward)

Multiply backward linearized equation by δΩ and integrate:

**Term 1 (Viscous):** -ν||∇δΩ||²

**Term 2 (Self-similar):**
```
∫(y·∇)δΩ/2 · δΩ = (1/4)∫(y·∇)|δΩ|² = -(3/4)||δΩ||²
```

Wait, I need to be more careful. Let me redo this.

∫[(y·∇)δΩ/2] · δΩ = (1/4)∫(y·∇)|δΩ|²

Integration by parts: ∫(y·∇)f = -∫(∇·y)f = -3∫f

So: (1/4)∫(y·∇)|δΩ|² = (1/4)(-3)||δΩ||² = -(3/4)||δΩ||²

**Term 3 (Linear):** ∫δΩ · δΩ = +||δΩ||²

**Combined (Backward):**
```
-ν||∇δΩ||² - (3/4)||δΩ||² + ||δΩ||² = 0
-ν||∇δΩ||² + (1/4)||δΩ||² = 0
```

So: **ν||∇δΩ||² = (1/4)||δΩ||²**

### 2.4 Analysis of Backward Identity

The backward case gives:
```
ν||∇δΩ||² = (1/4)||δΩ||²
```

This is a CONSTRAINT on the Rayleigh quotient, not a contradiction!

Compare to forward:
```
-ν||∇δΩ||² - (1/4)||δΩ||² = 0  → Both terms ≤ 0, sum = 0 → δΩ = 0
```

The backward case does NOT force δΩ = 0 from the energy identity alone.

---

## 3. Alternative Approaches for Backward

### 3.1 Asymptotic Analysis (Same Idea)

Even though the energy identity doesn't give definite sign, we can try the
asymptotic analysis.

The backward linearized equation:
```
ν∆δΩ + (y·∇)δΩ/2 + δΩ = 0
```

For δΩ ~ r^{-α} at large r:
- ν∆δΩ ~ νr^{-α-2}
- (y·∇)δΩ/2 ~ -αr^{-α}/2
- δΩ ~ r^{-α}

At leading order (r^{-α}):
```
-α/2 + 1 = 0  →  α = 2
```

So δΩ ~ r^{-2} is the natural decay for the backward case.

For α = 2: Is this compatible with L²?
```
∫|δΩ|² ~ ∫r^{-4} r² dr = ∫r^{-2} dr  < ∞ ✓
```

Yes! The backward case allows L² vorticity with r^{-2} decay.

### 3.2 The Velocity Decay

If Ω ~ r^{-2}, then by Biot-Savart:
```
U ~ ∫Ω/|x-y| dy ~ r^{-1}
```

So U ∈ L^{3,∞} - exactly the critical space!

### 3.3 Can Backward Profiles Exist?

The asymptotic analysis suggests backward profiles MIGHT exist with:
- |U| ~ r^{-1} (critical decay)
- |Ω| ~ r^{-2} (L² vorticity)

This is NOT ruled out by our energy identity.

---

## 4. NRŠ Approach for Backward

### 4.1 The NRŠ Identity

Nečas-Růžička-Šverák used a different identity. For L³ profiles:
```
∫|U|³ = specific combination of terms
```

Their identity works for BOTH forward and backward cases!

### 4.2 Why NRŠ Works

The NRŠ identity exploits:
- Scale invariance of L³ norm
- Specific algebraic structure
- Works regardless of sign in profile equation

### 4.3 Can We Adapt to L²?

The NRŠ identity is specific to L³. For L² (or L^{3,∞}), we need a different
approach.

**Idea:** Use a weighted identity that captures both forward and backward.

---

## 5. Unified Approach Attempt

### 5.1 Weighted Energy with Parameter

Consider multiplying by w(y)Ω where w is a weight to be determined.

For the backward equation:
```
∫[ν∆Ω + (y·∇)Ω/2 + Ω] · wΩ = 0
```

**Viscous term:**
```
∫ν∆Ω · wΩ = -ν∫|∇Ω|²w - ν∫∇Ω · Ω · ∇w
```

**Self-similar term:**
```
∫(y·∇)Ω/2 · wΩ = (1/4)∫(y·∇)|Ω|² w
                = -(1/4)∫|Ω|²(3w + y·∇w)
```

**Linear term:**
```
∫Ω · wΩ = ∫|Ω|²w
```

### 5.2 Choosing the Weight

For the identity to have definite sign, we need:
```
-ν|∇Ω|²w + coefficient × |Ω|²w ≤ 0
```

The coefficient of |Ω|²w is:
```
1 - (3/4) - (y·∇w)/(4w) = 1/4 - (y·∇w)/(4w)
```

For definite sign, we need:
```
1/4 - (y·∇w)/(4w) < 0  →  y·∇w > w
```

**Try w = |y|^β:**
```
y·∇w = β|y|^β  and  w = |y|^β
```

So y·∇w/w = β. Need β > 1.

### 5.3 Weighted Identity with |y|^β

With w = |y|^β for β > 1:
```
-ν∫|∇Ω|²|y|^β + (1/4 - β/4)∫|Ω|²|y|^β - ν∫∇Ω · Ω · β|y|^{β-2}y = 0
```

The coefficient (1/4 - β/4) is NEGATIVE for β > 1!

But there's still the cross term -ν∫∇Ω · Ω · β|y|^{β-2}y to handle.

### 5.4 Cross Term Analysis

The cross term:
```
|∫∇Ω · Ω · |y|^{β-2}y| ≤ ||∇Ω||_{L²_w} ||Ω||_{L²_w} |y|^{-1}
```

This is bounded but doesn't obviously have definite sign.

**The weighted approach is inconclusive.**

---

## 6. Physical Interpretation

### 6.1 Forward: Outward Drift

The forward self-similar term -(y·∇)U/2 acts as outward drift (advecting
fluid away from origin). This is incompatible with L² concentration.

### 6.2 Backward: Inward Drift

The backward self-similar term +(y·∇)U/2 acts as inward drift (advecting
fluid toward origin). This COULD support concentration!

### 6.3 Why Backward is Harder

Physically, the backward case describes fluid focusing toward a point.
The inward drift helps maintain concentrated structures, making non-trivial
profiles more plausible.

---

## 7. What's Known

### 7.1 NRŠ Result

Nečas-Růžička-Šverák proved: No backward self-similar profiles in L³.

Their proof uses an identity specific to L³ that works for both forward
and backward.

### 7.2 Tsai's Extensions

Tsai extended NRŠ to L^p for p > 3. The L² case (and L^{3,∞}) is not covered.

### 7.3 Our Contribution

We proved non-existence for FORWARD self-similar in L^{3,∞} (optimal for forward).

Backward self-similar in L^{3,∞} remains open with our methods.

---

## 8. Summary

### What We Know:
1. **Forward self-similar:** No profiles in L^{3,∞} (our Theorem D)
2. **Backward self-similar in L³:** No profiles (NRŠ)
3. **Backward self-similar in L²/L^{3,∞}:** OPEN

### Why Backward is Different:
- Energy identity has opposite signs
- Inward drift supports concentration
- Different asymptotic behavior

### Possible Paths Forward:
1. Adapt NRŠ integral identity to L^{3,∞}
2. Find new weighted identity for backward case
3. Use different structural properties of NS

### Status:
**Backward self-similar in L^{3,∞} remains an open problem.**

If backward profiles exist, they would represent a Type II blowup scenario
(coming out of a singularity, describing the post-blowup behavior).

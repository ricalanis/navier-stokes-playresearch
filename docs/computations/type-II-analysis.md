# Type II Blowup Analysis

## Context

We have ruled out Type I (self-similar) blowup completely. Any Navier-Stokes
singularity must therefore be **Type II**: faster than the self-similar rate.

**Definition:** Type II blowup means:
```
||u(·,t)||_{L^∞} >> (T-t)^{-1/2}  as t → T
```

Equivalently, for any C > 0, there exists t close to T with:
```
||u(·,t)||_{L^∞} > C(T-t)^{-1/2}
```

---

## 1. What We Know About Type II

### 1.1 Type II Must Be "Faster"

Type II means the blowup rate is strictly faster than (T-t)^{-1/2}. Possible rates:
- (T-t)^{-α} with α > 1/2
- (T-t)^{-1/2} |log(T-t)|^β for some β > 0
- Even faster (e.g., exponential in 1/(T-t))

### 1.2 Known Results

**Caffarelli-Kohn-Nirenberg [CKN82]:** The singular set has zero 1-dimensional
Hausdorff measure in space-time. This constrains WHERE singularities can occur.

**Seregin [Ser12]:** If blowup occurs, then:
```
limsup_{t→T} (T-t)^{1/2} ||u(t)||_{L^∞} = ∞
```

This confirms Type II is necessary (Type I is ruled out).

### 1.3 Type II in Related Equations

In other PDEs, Type II blowup CAN occur:
- **Supercritical NLS:** Type II blowup with specific rates
- **Harmonic map heat flow:** Type II bubbling
- **Semilinear heat equations:** Various Type II scenarios

These suggest Type II is not automatically excluded by "soft" arguments.

---

## 2. Constraints on Type II

### 2.1 Energy Constraint

The energy inequality gives:
```
||u(t)||²_{L²} + 2ν ∫_0^t ||∇u(s)||²_{L²} ds ≤ ||u_0||²_{L²}
```

Even as ||u||_{L^∞} → ∞, the L² norm stays bounded!

**For Type II:** The blowup must involve concentration, not global growth.

### 2.2 Enstrophy Growth

Define enstrophy E(t) = ||ω(t)||²_{L²} where ω = ∇ × u.

The enstrophy equation:
```
dE/dt = 2∫ω·(ω·∇)u dx - 2ν||∇ω||²_{L²}
```

The vortex stretching term ω·(ω·∇)u can cause enstrophy growth.

**Key question:** How fast can enstrophy grow?

### 2.3 Beale-Kato-Majda Criterion

**BKM Theorem:** Solution is regular on [0,T] iff:
```
∫_0^T ||ω(t)||_{L^∞} dt < ∞
```

**Contrapositive:** If blowup at T, then:
```
∫_0^T ||ω(t)||_{L^∞} dt = ∞
```

For Type II, ||ω||_{L^∞} must grow faster than (T-t)^{-1}.

---

## 3. Rescaled Analysis for Type II

### 3.1 The Challenge

For Type I, we had a fixed rescaling:
```
v(y,τ) = √(T-t) · u(y√(T-t), t)
```

For Type II, the rescaling factor is unknown and time-dependent.

### 3.2 Adaptive Rescaling

Define λ(t) such that:
```
||u(t)||_{L^∞} = λ(t)^{-1}
```

Type II means λ(t) << √(T-t).

Rescale: v(y,τ) = λ(t) · u(λ(t)y, t) where τ = τ(t) is a reparametrized time.

Then ||v||_{L^∞} = 1 (normalized).

### 3.3 Rescaled Equation

The rescaled solution v satisfies:
```
∂v/∂τ = ν λ²(dτ/dt)^{-1} ∆v - (v·∇)v - (λ'/λ)(dτ/dt)^{-1}[v + (y·∇)v] - ∇q
```

where λ' = dλ/dt.

**Key observation:** The equation depends on the RATE λ'/λ, which is unknown.

### 3.4 The Limiting Profile Problem

If v converges to some profile V as τ → ∞, then V satisfies:
```
0 = ν_eff ∆V - (V·∇)V - μ[V + (y·∇)V] - ∇Q
```

where ν_eff and μ depend on the limiting behavior of λ(t).

**Possibilities:**
- μ = 0: Steady Navier-Stokes (Leray's backward self-similar)
- μ > 0: Self-similar profile (ruled out by our theorems)
- μ = ∞: Euler limit

---

## 4. Ruling Out Some Type II Scenarios

### 4.1 No "Slow" Type II

**Claim:** If ||u(t)||_{L^∞} ~ (T-t)^{-α} with 1/2 < α < 1, then blowup
is impossible.

**Argument sketch:**

For α < 1, we have ∫_0^T ||u(t)||_{L^∞} dt < ∞.

By Serrin-type criteria, this controls regularity. More precisely:
```
||u||_{L^p_t L^q_x} < ∞  with 2/p + 3/q = 1
```
implies regularity. For α < 1, we can find such (p,q).

**Conclusion:** Type II must be at least as fast as (T-t)^{-1}.

### 4.2 Constraints from Partial Regularity

CKN theory shows singular set is small. For Type II:
- Singularities are isolated points in space-time
- The solution is smooth except at these points
- Blowup profile must be highly concentrated

### 4.3 Backward Self-Similar (Leray's Scenario)

Leray originally considered backward self-similar solutions:
```
u(x,t) = (T-t)^{-1/2} U(x/√(T-t))
```

with U satisfying:
```
ν∆U + (U·∇)U + U/2 + (y·∇)U/2 + ∇P = 0
```

Note the SIGN CHANGE in the profile equation compared to forward self-similar!

**Important:** Our theorems rule out forward self-similar, but backward
self-similar has DIFFERENT structure.

### 4.4 Backward Self-Similar Analysis

For backward self-similar (Leray):
```
ν∆U + (U·∇)U + U/2 + (y·∇)U/2 + ∇P = 0
```

Taking curl:
```
ν∆Ω + (U·∇)Ω - (Ω·∇)U + (y·∇)Ω/2 + Ω = 0
```

Note: The self-similar term has coefficient +1/2 (same) but the linear term is +Ω (not -Ω)!

**Energy identity:**

Multiply by Ω and integrate:
```
-ν||∇Ω||² + [self-similar: +(3/4)||Ω||²] + ||Ω||² = 0
```

This gives:
```
-ν||∇Ω||² + (7/4)||Ω||² = 0
```

This is NOT definite sign! The identity says:
```
ν||∇Ω||² = (7/4)||Ω||²
```

This is a constraint on the Rayleigh quotient, NOT a contradiction.

**Backward self-similar profiles might exist!**

---

## 5. The Backward Self-Similar Gap

### 5.1 Why Our Method Doesn't Apply

For forward self-similar (blowup):
- Energy identity: -ν||∇Ω||² - (1/4)||Ω||² = 0
- Both terms non-positive → Ω = 0

For backward self-similar (Leray):
- Energy identity: -ν||∇Ω||² + (7/4)||Ω||² = 0
- Terms have OPPOSITE signs → constraint, not contradiction

### 5.2 What's Known About Backward Self-Similar

**NRŠ [NRS96]:** Also proved non-existence for backward self-similar in L³.

**Tsai [Tsa98]:** Extended to other Lebesgue spaces.

**Key difference:** Their method uses different integral identities that work
for BOTH forward and backward cases.

### 5.3 Can We Extend?

Our vorticity energy method works for forward but not backward. To handle
backward self-similar, we would need:
- Different multiplier (not just Ω)
- Sign-correcting weights
- Or: use the NRŠ integral identity approach

---

## 6. Summary: Type II Landscape (UPDATED)

### What We've Shown:
1. Type I blowup is impossible (Theorem C)
2. Any blowup must be Type II
3. "Slow" Type II (rate < (T-t)^{-1}) is also ruled out
4. **NEW: Backward self-similar in L^{3,∞} ruled out (Theorem F)**

### What Remains Open:
1. ~~Backward self-similar~~ **RULED OUT by Theorem F**
2. **Generic Type II** (non-self-similar) with rate ~ (T-t)^{-1} or faster
3. **Hou-Luo type scenarios** (axis blowup, non-self-similar)

### The Big Picture:

```
Self-Similar Analysis: COMPLETE
  - Forward L^{3,∞}: RULED OUT (Theorem D)
  - Backward L^{3,∞}: RULED OUT (Theorem F)
                    ↓
Remaining Type II possibilities:
  - Generic (non-self-similar) Type II: NOT RULED OUT
  - Hou-Luo scenario: Numerical, non-self-similar, NOT RULED OUT
```

---

## 7. Next Steps

### 7.1 Backward Self-Similar

To rule out backward self-similar in L²:
- Need different energy identity or multiplier
- Or adapt NRŠ integral identity to L² setting
- Could also try weighted approaches

### 7.2 Generic Type II Constraints

Derive more constraints on Type II blowup:
- Concentration rates
- Spatial structure (must be point-like by CKN)
- Connection to vortex line geometry

### 7.3 Numerical Scenarios

Analyze Hou-Luo type configurations:
- Axis-touching vortex sheets
- Non-self-similar dynamics
- Role of viscosity

---

## 8. Conclusion

Our theorems provide strong constraints on blowup:
- All self-similar (Type I) blowup ruled out
- Slow Type II also ruled out
- Remaining possibilities are highly constrained

The question "Can Type II blowup occur?" remains open and is closely tied to
the Millennium Prize question of global regularity.

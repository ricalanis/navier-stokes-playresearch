# Backward Self-Similar Non-Existence in L²

## Verification of the Energy Identity

### The Backward Profile Equation

For backward self-similar solutions u(x,t) = (t-T)^{-1/2}U(x/√(t-T)) for t > T:

```
ν∆U + (U·∇)U + U/2 + (y·∇)U/2 = ∇P                    (B.1)
∇·U = 0                                                 (B.2)
```

### Velocity Energy Identity

Multiply (B.1) by U and integrate over ℝ³:

**Term 1: Viscous**
```
∫ν∆U·U dy = -ν∫|∇U|² dy = -ν||∇U||²
```
(integration by parts, boundary terms vanish for L² functions)

**Term 2: Nonlinear advection**
```
∫(U·∇)U·U dy = ∫U_j(∂_jU_i)U_i dy = (1/2)∫U_j∂_j|U|² dy
             = -(1/2)∫(∂_jU_j)|U|² dy = 0
```
(using ∇·U = 0)

**Term 3: Linear scaling**
```
∫(U/2)·U dy = (1/2)||U||²
```

**Term 4: Self-similar stretching**
```
∫[(y·∇)U/2]·U dy = (1/4)∫(y·∇)|U|² dy
```

Integration by parts: ∫(y·∇)f dy = -∫(∇·y)f dy = -3∫f dy

So: (1/4)∫(y·∇)|U|² dy = -(3/4)||U||²

**Term 5: Pressure**
```
∫∇P·U dy = -∫P(∇·U) dy = 0
```
(using ∇·U = 0)

### Combined Identity

Adding all terms:
```
-ν||∇U||² + 0 + (1/2)||U||² - (3/4)||U||² + 0 = 0
```

Simplifying:
```
-ν||∇U||² - (1/4)||U||² = 0                            (B.3)
```

### Analysis

Both terms in (B.3) are NON-POSITIVE:
- -ν||∇U||² ≤ 0
- -(1/4)||U||² ≤ 0

Their sum equals zero only if BOTH vanish:
```
||∇U||² = 0  AND  ||U||² = 0
```

Therefore U ≡ 0.

---

## Theorem (Backward Non-Existence in L²)

**Theorem E:** For any ν > 0, the only smooth backward self-similar profile
U ∈ L²(ℝ³) for the 3D Navier-Stokes equations is U = 0.

**Proof:** The velocity energy identity (B.3) gives:
```
-ν||∇U||² - (1/4)||U||² = 0
```
Both terms non-positive, so U = 0. ∎

---

## Comparison: Forward vs Backward in L²

### Forward Self-Similar (Theorem A)

Profile equation:
```
ν∆U - (U·∇)U - U/2 - (y·∇)U/2 = ∇P
```

Velocity energy: -ν||∇U||² + (1/4)||U||² = 0 (NOT definite sign!)

We used VORTICITY to get: -ν||∇Ω||² - (1/4)||Ω||² = 0 (definite sign ✓)

### Backward Self-Similar (Theorem E)

Profile equation:
```
ν∆U + (U·∇)U + U/2 + (y·∇)U/2 = ∇P
```

Velocity energy: -ν||∇U||² - (1/4)||U||² = 0 (definite sign ✓)

Vorticity energy: -ν||∇Ω||² + (7/4)||Ω||² = 0 (NOT definite sign!)

### Summary

| Case | Velocity Identity | Vorticity Identity | Method |
|------|-------------------|---------------------|--------|
| Forward | Indefinite | Definite negative | Vorticity |
| Backward | Definite negative | Indefinite | Velocity |

The two cases require DIFFERENT energy approaches!

---

## Implications

### For L² Theory

- **Forward:** No profiles (Theorem A, vorticity method)
- **Backward:** No profiles (Theorem E, velocity method)

Both directions are covered in L².

### For L^{3,∞} Theory

- **Forward:** No profiles (Theorem D, vorticity + gradient decay)
- **Backward:** OPEN (velocity method requires ||U||² < ∞)

The backward case in L^{3,∞} remains genuinely open.

---

## Physical Interpretation

### Why the Signs Differ

**Forward (approaching singularity):**
- Self-similar term -(y·∇)U/2 creates outward drift
- This fights concentration, helps vorticity decay

**Backward (emanating from singularity):**
- Self-similar term +(y·∇)U/2 creates inward drift
- This supports concentration but velocity still dissipates

The inward drift in backward case helps velocity decay (good for velocity identity)
but supports vorticity concentration (bad for vorticity identity).

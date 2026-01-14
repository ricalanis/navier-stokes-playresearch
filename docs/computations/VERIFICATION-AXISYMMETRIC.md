# Verification Checklist: Axisymmetric Navier-Stokes Global Regularity

**Date:** January 13, 2026
**Status:** FOR INDEPENDENT VERIFICATION
**Paper:** `docs/paper-axisymmetric-regularity.md`

---

## Purpose

This document provides a checklist for independent verification of the axisymmetric global regularity theorem.

---

## Claim Summary

**Main Theorem:** Smooth axisymmetric solutions to 3D incompressible Navier-Stokes remain smooth for all time.

**Proof Strategy:** Exhaustive exclusion of all blowup mechanisms:
1. Type I (self-similar): Profile non-existence
2. Type II α ∈ (1/2, 3/5): η conservation + sign control OR effective viscosity
3. Type II α ≥ 3/5: Energy inequality

---

## Verification Checklist

### Part A: Profile Non-Existence (Type I Exclusion)

| Claim | Status | Verification Method |
|-------|--------|---------------------|
| A.1 | Forward profiles don't exist in L^{3,∞} | Check NRŠ identity + Liouville |
| A.2 | Backward profiles don't exist in L^{3,∞} | Check KNSS extension |
| A.3 | Type I blowup implies profile existence | Standard ESS argument |

**Key References:**
- Nečas-Růžička-Šverák (1996)
- Koch-Nadirashvili-Seregin-Šverák (2009)
- Chae-Wolf (2016)

**Verification Steps:**
1. [ ] Confirm NRŠ identity derivation
2. [ ] Verify Liouville theorem conditions
3. [ ] Check profile equation derivation

---

### Part B: η Conservation (No-Swirl Case)

| Claim | Status | Verification Method |
|-------|--------|---------------------|
| B.1 | η = ω^θ/r is materially conserved for Euler | Direct calculation |
| B.2 | η satisfies parabolic equation for NS | Check diffusion operator |
| B.3 | Maximum principle holds for η | Standard parabolic theory |

**Key Calculation to Verify:**

Starting from vorticity equation:
```
∂_t ω^θ + u^r ∂_r ω^θ + u^z ∂_z ω^θ = (u^r/r) ω^θ + ν(Δω^θ - ω^θ/r²)
```

Dividing by r and computing D_t(ω^θ/r):
```
D_t η = (1/r)[∂_t ω^θ + u·∇ω^θ] - (ω^θ/r²)u^r
      = (1/r)[(u^r/r)ω^θ + viscous] - (ω^θ/r²)u^r
      = (ω^θ/r²)u^r - (ω^θ/r²)u^r + viscous/r
      = ν L[η]
```

**Verification Steps:**
1. [ ] Verify vorticity equation in cylindrical coordinates
2. [ ] Check stretching term cancellation
3. [ ] Confirm parabolic operator form
4. [ ] Verify maximum principle applicability

---

### Part C: Sign Control in Concentration Regions

| Claim | Status | Verification Method |
|-------|--------|---------------------|
| C.1 | Concentration toward axis requires u^r < 0 | Physical reasoning |
| C.2 | With u^r < 0, stretching is negative | Direct from enstrophy equation |
| C.3 | Negative stretching prevents blowup | Combined with viscous dissipation |

**Key Calculation to Verify:**

Enstrophy evolution:
```
d/dt ∫(ω^θ)² r dr dz = 2∫(ω^θ)²(u^r/r) r dr dz - 2ν∫|∇ω^θ|² r dr dz
                      = 2∫(ω^θ)² u^r dr dz - 2ν∫|∇ω^θ|² r dr dz
```

When u^r < 0: First term ≤ 0, second term ≤ 0 → enstrophy decreases.

**Verification Steps:**
1. [ ] Derive enstrophy evolution equation
2. [ ] Verify incompressibility constraint on concentration
3. [ ] Check sign of stretching contribution
4. [ ] Confirm both terms are non-positive

---

### Part D: η Bound Contradicts Type II

| Claim | Status | Verification Method |
|-------|--------|---------------------|
| D.1 | Type II requires ω^θ ~ (T-t)^{-2α} | Biot-Savart estimate |
| D.2 | η bounded gives ω^θ ≤ L·M ~ (T-t)^β | Direct from η bound |
| D.3 | These are incompatible for β > 0, α > 0 | Scaling comparison |

**Key Calculation to Verify:**

At concentration scale L ~ (T-t)^β with β = (1+α)/2:
- Type II requires: ω^θ ~ (T-t)^{-2α}
- η bound gives: ω^θ = r·η ≤ L·||η₀||_∞ ~ (T-t)^β

Compatibility requires: (T-t)^β ≥ (T-t)^{-2α}, i.e., β ≤ -2α.

Since β > 0 and -2α < 0, this is impossible.

**Verification Steps:**
1. [ ] Verify Biot-Savart scaling for vorticity
2. [ ] Check concentration scale formula
3. [ ] Confirm incompatibility of exponents

---

### Part E: Energy Constraint (α ≥ 3/5 Exclusion)

| Claim | Status | Verification Method |
|-------|--------|---------------------|
| E.1 | Energy scales as E ~ (T-t)^{3-5α} | Standard Type II scaling |
| E.2 | For α ≥ 3/5, energy doesn't decrease | Exponent check |
| E.3 | At α = 3/5, dissipation diverges | Direct calculation |

**Key Calculation to Verify:**

At α = 3/5:
- E(t) ~ (T-t)^{3-5(3/5)} = (T-t)^0 = constant
- ||∇u||² ~ (T-t)^{-4α/3} = (T-t)^{-4/5} → ∞
- dE/dt = -2ν||∇u||² → -∞

But E = constant requires dE/dt = 0. Contradiction.

**Verification Steps:**
1. [ ] Derive energy scaling formula
2. [ ] Check dissipation scaling
3. [ ] Verify contradiction at α = 3/5

---

### Part F: Effective Viscosity (With Swirl Case)

| Claim | Status | Verification Method |
|-------|--------|---------------------|
| F.1 | Type II rescaling gives ν_eff = ν λ^{1-2α} | Direct from rescaled equation |
| F.2 | For α > 1/2, ν_eff → ∞ as λ → 0 | Exponent sign check |
| F.3 | Diverging viscosity causes swirl decay | Energy estimate |

**Key Calculation to Verify:**

Rescaled equation:
```
∂_τ V + (V·∇)V = -∇P + ν_eff ΔV
```
where ν_eff = ν λ^{1-2α}.

For α > 1/2: 1 - 2α < 0, so λ^{1-2α} → ∞ as λ → 0.

Swirl energy satisfies:
```
dE_Γ/dτ ≤ -C·ν_eff·E_Γ
```
With ν_eff → ∞, E_Γ → 0 exponentially.

**Verification Steps:**
1. [ ] Derive rescaled NS equation
2. [ ] Verify effective viscosity formula
3. [ ] Check swirl energy decay estimate

---

### Part G: Backward Dispersion

| Claim | Status | Verification Method |
|-------|--------|---------------------|
| G.1 | Energy in trapped regions grows backward | Energy evolution calculation |
| G.2 | Growth contradicts finiteness | No bounded invariant regions |
| G.3 | All particles disperse backward | Corollary of G.2 |

**Key Calculation to Verify:**

For self-similar ancient Euler, the energy evolution gives:
```
dẼ/dτ = γ Ẽ where γ = (3 - 2α - 2α²)/(1+α)
```

For α < α_c ≈ 0.82: γ > 0.

In trapped regions: Ẽ(τ) ~ e^{γτ}.
As τ → -∞: Ẽ → ∞ (if γ > 0).

Type II requires α < 3/5 = 0.6 < 0.82, so γ > 0 always.

**Verification Steps:**
1. [ ] Derive energy evolution for self-similar Euler
2. [ ] Calculate critical α_c
3. [ ] Verify Type II range is covered

---

### Part H: Liouville Theorem

| Claim | Status | Verification Method |
|-------|--------|---------------------|
| H.1 | Material conservation: η(X(τ),τ) = const | From Part B |
| H.2 | Backward dispersion: |X(τ)| → ∞ | From Part G |
| H.3 | η → 0 at infinity | Decay assumption |
| H.4 | Therefore η ≡ 0 | Combination of H.1-H.3 |

**Verification Steps:**
1. [ ] Verify chain of implications
2. [ ] Check decay assumption is standard
3. [ ] Confirm ω^θ = 0 implies V = 0 for axisymmetric

---

## Summary Table

| Part | Description | Verified? |
|------|-------------|-----------|
| A | Profile non-existence | [ ] |
| B | η conservation | [ ] |
| C | Sign control | [ ] |
| D | η vs Type II contradiction | [ ] |
| E | Energy constraint | [ ] |
| F | Effective viscosity | [ ] |
| G | Backward dispersion | [ ] |
| H | Liouville theorem | [ ] |

---

## Key Literature to Consult

1. O.A. Ladyzhenskaya (1968) - Original η conservation proof
2. M.R. Ukhovskii, V.I. Yudovich (1968) - Independent proof
3. G. Seregin, V. Šverák (2009) - Type I exclusion methods
4. H. Koch et al. (2009) - KNSS Liouville theorems
5. G. Seregin (2025) - Type II analysis framework

---

## Potential Issues to Check

1. **Boundary behavior:** Verify all estimates are valid at r = 0 (axis)
2. **Decay at infinity:** Confirm η decay assumption is justified
3. **Rescaling limits:** Check convergence of rescaled solutions
4. **Trapped region definition:** Verify measure-theoretic arguments
5. **Energy evolution derivation:** Check self-similar Euler terms

---

## Recommended Verification Order

1. Part B (η conservation) - Foundation of argument
2. Part C (sign control) - Key innovation
3. Part D (contradiction) - Main no-swirl proof
4. Part E (energy) - Upper bound on α
5. Part F (viscosity) - With-swirl extension
6. Part G (dispersion) - Liouville preparation
7. Part H (Liouville) - Limit is trivial
8. Part A (profiles) - Type I exclusion

---

*Verification checklist created: January 13, 2026*
*For external review and independent verification*

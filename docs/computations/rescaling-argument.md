# Rescaling Argument: Type II Gap Closure Attempt

**Key Idea:** For α > 1/2, the rescaled Navier-Stokes has INFINITE effective viscosity, which should force rapid decay.

---

## Setup

### Original equation
```
∂u/∂t + (u·∇)u = -∇p + νΔu, div(u) = 0
```

### Type II ansatz
||u||_∞(t) ~ (T-t)^{-α} for α ∈ (1/2, 3/5)

### Rescaling
Define: U(τ,y) = (T-t)^α u(t, (T-t)^{1/2} y)
where τ = -log(T-t), y = x/(T-t)^{1/2}

As t → T: τ → ∞

---

## The Rescaled Equation

### Time derivative
∂u/∂t = (T-t)^{-α-1} [∂U/∂τ + αU + (1/2)y·∇U]

### Spatial derivative
∇_x u = (T-t)^{-α-1/2} ∇_y U
Δ_x u = (T-t)^{-α-1} Δ_y U

### Nonlinear term
(u·∇)u = (T-t)^{-2α-1/2} (U·∇_y)U
        = (T-t)^{-α-1} · (T-t)^{-α+1/2} (U·∇_y)U

### Putting together
```
(T-t)^{-α-1} [∂U/∂τ + αU + (1/2)y·∇U + (T-t)^{1/2-α}(U·∇)U]
    = -∇P + ν(T-t)^{-α-1} Δ_y U
```

Simplifying:
```
∂U/∂τ + αU + (1/2)y·∇U + (T-t)^{1/2-α}(U·∇)U = -∇P + νΔ_y U
```

Using τ = -log(T-t), so (T-t) = e^{-τ}:
```
∂U/∂τ + αU + (1/2)y·∇U + e^{(α-1/2)τ}(U·∇)U = -∇P + νΔ_y U
```

---

## Analysis of the Rescaled Equation

### For α > 1/2:
The coefficient e^{(α-1/2)τ} → ∞ as τ → ∞.

**The nonlinear term becomes DOMINANT!**

Wait, this is the opposite of what I expected. Let me recalculate.

### Recalculation
Actually, I think I made an error. Let me redo more carefully.

Original:
```
∂u/∂t + (u·∇)u = -∇p + νΔu
```

With u(t,x) = (T-t)^{-α} U(τ, (T-t)^{-1/2}x) and t = T - e^{-τ}:

dt = e^{-τ} dτ = (T-t) dτ
So ∂/∂t = (1/(T-t)) ∂/∂τ = (T-t)^{-1} ∂/∂τ

Also, x = (T-t)^{1/2} y, so:
∂u/∂t|_x = ∂[(T-t)^{-α} U(τ,y)]/∂t|_x

This involves:
- ∂(T-t)^{-α}/∂t = α(T-t)^{-α-1}
- ∂U/∂τ · ∂τ/∂t = ∂U/∂τ · (T-t)^{-1}
- ∂U/∂y · ∂y/∂t|_x = ∂U/∂y · (1/2)(T-t)^{-1/2}·(-1)·(T-t)^{-1/2}·x
                    = -(1/2)∂U/∂y · y · (T-t)^{-1}

So:
```
∂u/∂t = (T-t)^{-α-1} [αU + ∂U/∂τ - (1/2)y·∇U]
```

### Nonlinear term
u = (T-t)^{-α} U
∇_x = (T-t)^{-1/2} ∇_y

(u·∇)u = (T-t)^{-α} U · (T-t)^{-1/2} ∇_y [(T-t)^{-α} U]
       = (T-t)^{-2α-1/2} (U·∇_y)U

### Viscous term
Δ_x u = (T-t)^{-1} Δ_y [(T-t)^{-α} U]
      = (T-t)^{-α-1} Δ_y U

### Full equation
```
(T-t)^{-α-1} [αU + ∂U/∂τ - (1/2)y·∇U] + (T-t)^{-2α-1/2} (U·∇)U
    = -∇P + ν(T-t)^{-α-1} ΔU
```

Multiply by (T-t)^{α+1}:
```
αU + ∂U/∂τ - (1/2)y·∇U + (T-t)^{1/2-α} (U·∇)U = -∇P + νΔU
```

### Coefficient analysis
Nonlinear coefficient: (T-t)^{1/2-α} = e^{-(1/2-α)τ} = e^{(α-1/2)τ}

For α > 1/2: coefficient → ∞ as τ → ∞

For α < 1/2: coefficient → 0 as τ → ∞

**At α = 1/2:** coefficient = 1 (fixed, this is self-similar)

---

## Interpretation

### For α > 1/2:
The rescaled equation becomes:
```
∂U/∂τ + αU - (1/2)y·∇U + e^{(α-1/2)τ}(U·∇)U ≈ -∇P + νΔU
```

As τ → ∞, the nonlinear term e^{(α-1/2)τ}(U·∇)U BLOWS UP.

For the equation to remain balanced, either:
1. U → 0 (making nonlinear term small)
2. (U·∇)U → 0 in a very specific way
3. The equation becomes ill-posed

### What this means
If U remains O(1), then e^{(α-1/2)τ}(U·∇)U ~ e^{(α-1/2)τ} → ∞.

This term must be balanced by either:
- ∂U/∂τ ~ e^{(α-1/2)τ} (rapid growth/decay)
- -∇P ~ e^{(α-1/2)τ} (huge pressure)

Neither is consistent with a smooth limit.

**This suggests U → 0 as τ → ∞ for α > 1/2.**

---

## Formalizing the Constraint

### Claim
For α > 1/2, if U(τ,·) is a solution of the rescaled equation with ||U||_∞ ≤ M, then U → 0 as τ → ∞.

### Sketch of argument
1. The nonlinear term has coefficient e^{(α-1/2)τ} → ∞
2. For ||U||_∞ ~ O(1), this term dominates
3. The only way to balance is if (U·∇)U → 0
4. For incompressible flow, (U·∇)U = 0 implies U is a shear or potential flow
5. Combined with other constraints, this forces U → 0

### Gap in the argument
Step 4-5 are not rigorous. The pressure gradient could in principle balance the large nonlinear term.

---

## Alternative: Energy Estimate

### Rescaled energy
Ẽ(τ) = ∫ |U(τ,y)|² dy

### Evolution
dẼ/dτ = 2∫ U · ∂U/∂τ dy

From the rescaled equation:
```
∂U/∂τ = -αU + (1/2)y·∇U - e^{(α-1/2)τ}(U·∇)U - ∇P + νΔU
```

Taking the inner product with U:
```
dẼ/dτ = -2αẼ + ∫ U·(y·∇U) - e^{(α-1/2)τ}∫ U·(U·∇)U + 0 - 2ν∫|∇U|²
```

The terms:
1. -2αẼ: decay (for α > 0)
2. ∫ U·(y·∇U) = -(3/2)Ẽ (by integration by parts in R³)
3. -e^{(α-1/2)τ}∫ U·(U·∇)U = 0 (for div-free U)
4. -2ν∫|∇U|² ≤ 0

So:
```
dẼ/dτ = -(2α + 3/2)Ẽ - 2ν∫|∇U|² ≤ -(2α + 3/2)Ẽ
```

### Solution
Ẽ(τ) ≤ Ẽ(0) e^{-(2α + 3/2)τ}

For α > 0: Ẽ(τ) → 0 exponentially as τ → ∞.

**The rescaled energy decays!**

---

## What This Means for Type II

### Original energy
E(t) = ∫|u(t,x)|² dx

### Relation to rescaled energy
u(t,x) = (T-t)^{-α} U(τ, x/(T-t)^{1/2})

E(t) = ∫ (T-t)^{-2α} |U(τ, x/(T-t)^{1/2})|² dx
     = (T-t)^{-2α} (T-t)^{3/2} ∫ |U(τ, y)|² dy   [change of variables]
     = (T-t)^{3/2 - 2α} Ẽ(τ)

### Using Ẽ decay
Ẽ(τ) ≤ C e^{-(2α + 3/2)τ} = C (T-t)^{2α + 3/2}

So:
E(t) ≤ C (T-t)^{3/2 - 2α} (T-t)^{2α + 3/2} = C (T-t)^{3}

**E(t) ≤ C(T-t)³ regardless of α!**

### Consequence
For Type II with E(t) ~ (T-t)^{3-5α}:
- Need: 3 - 5α ≥ 3
- This requires: α ≤ 0

But α > 0 for blowup. **CONTRADICTION?**

Wait, this bound E ≤ C(T-t)³ seems too strong. Let me check.

---

## Checking the Energy Bound

The bound E ≤ C(T-t)³ would imply α ≤ 0, ruling out ALL blowup.

But we know blowup is not ruled out by known methods. Let me find the error.

### The issue
The rescaled energy estimate assumes U is defined for all τ ≥ 0.

But U is defined by:
U(τ,y) = (T-t)^α u(t, (T-t)^{1/2} y)

This requires u to exist up to time T.

If u blows up at T, then U may not be well-defined as τ → ∞.

### Resolution
The energy estimate shows:
**IF u extends smoothly to T, THEN Ẽ(τ) → 0 as τ → ∞.**

This doesn't prevent blowup; it says blowup is characterized by Ẽ not decaying.

### What goes wrong at blowup?
For blowup, ||U||_∞ ~ 1 is maintained despite Ẽ → 0 would suggest ||U||_{L²} → 0.

This means ||U||_∞ and ||U||_{L²} decouple: concentration!

---

## Refined Conclusion

The rescaled analysis shows:

1. **Energy estimate:** Ẽ(τ) ≤ Ẽ(0) e^{-(2α+3/2)τ} for smooth solutions
2. **Implication:** L² norm decays exponentially in rescaled time
3. **For blowup:** ||U||_∞ ~ 1 but ||U||_{L²} → 0, meaning concentration
4. **For α > 1/2:** Nonlinear term has growing coefficient, making balance delicate

### The gap persists because:
The energy estimate applies to L², not L^∞.

Concentration allows ||U||_∞ ~ 1 while ||U||_{L²} → 0.

**No contradiction for α ∈ (1/2, 3/5).**

---

## Final Assessment

The rescaling analysis provides strong HEURISTIC evidence that Type II in (1/2, 3/5) is delicate, but does not prove impossibility.

**The gap (1/2, 3/5) remains open.**

To close it would require:
1. An L^∞-based energy estimate (not just L²)
2. Proving concentration is impossible at these rates
3. Or constructing an explicit Type II solution

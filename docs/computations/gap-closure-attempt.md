# Attempt to Close the (1/2, 3/5) Gap

**Date:** 2026-01-13
**Goal:** Rule out non-self-similar Type II blowup with α ∈ (1/2, 3/5)

---

## The Gap

**Current bounds:**
- Lower: α ≥ 1/2 (BKM criterion)
- Upper: α ≤ 3/5 (energy decay)

**Gap:** (1/2, 3/5) = (0.5, 0.6), width 0.1

---

## Approach 1: Refined BKM via Biot-Savart

### Standard BKM
∫||ω||_∞ dt = ∞ for blowup. With ||ω||_∞ ~ (T-t)^{-2α}, need α ≥ 1/2.

### Refinement using Biot-Savart
From u = K * ω with Calderon-Zygmund estimates:
```
||u||_∞ ≤ C ||ω||_{L^{3,∞}} log(e + ||ω||_{BMO}/||ω||_{L^{3,∞}})
```

For concentration on scale L with ||ω||_∞ ~ (T-t)^{-2α}:
```
||ω||_{L^{3,∞}} ~ ||ω||_∞ L ~ (T-t)^{-2α + β}
```

If β = 2α/3 (from energy constraint):
```
||ω||_{L^{3,∞}} ~ (T-t)^{-2α + 2α/3} = (T-t)^{-4α/3}
```

For ||u||_∞ ~ (T-t)^{-α}:
```
(T-t)^{-α} ≤ C (T-t)^{-4α/3} log(...)
```

Ignoring log: -α ≤ -4α/3, i.e., 4α/3 ≤ α, i.e., 4 ≤ 3. FALSE!

**This is a contradiction for any α > 0!**

Wait, let me check the Biot-Savart estimate more carefully.

### Correct Biot-Savart estimate

Actually: ||u||_{L^∞} ≤ C ||ω||_{L^{3/2,∞}} (weak type)

For concentration: ||ω||_{L^{3/2,∞}} ~ ||ω||_∞ L^{2} ~ (T-t)^{-2α + 2β}

With β = 2α/3:
```
||ω||_{L^{3/2,∞}} ~ (T-t)^{-2α + 4α/3} = (T-t)^{-2α/3}
```

For ||u||_∞ ~ (T-t)^{-α}:
```
(T-t)^{-α} ≤ C (T-t)^{-2α/3}
```

Need: -α ≤ -2α/3, i.e., α ≥ 2α/3, i.e., 3α ≥ 2α. TRUE for α > 0.

So this doesn't give a contradiction. The estimates are consistent.

---

## Approach 2: Dissipation Integral

### Finite dissipation constraint
```
∫_0^T ||∇u||² dt ≤ E(0)/ν < ∞
```

### Scaling of ||∇u||²
```
||∇u||² ~ (||u||_∞ / L)² × L³ ~ ||u||²_∞ L
        ~ (T-t)^{-2α} (T-t)^β
        = (T-t)^{-2α + β}
```

With β = 2α/3:
```
||∇u||² ~ (T-t)^{-2α + 2α/3} = (T-t)^{-4α/3}
```

Integral: ∫(T-t)^{-4α/3} dt finite iff 4α/3 < 1, i.e., **α < 3/4**.

This is weaker than α ≤ 3/5. No improvement.

---

## Approach 3: Enstrophy Growth Bound

### Enstrophy equation
```
dΩ/dt = ∫ω·S·ω - ν||∇ω||²
```

The stretching term ∫ω·S·ω can be bounded:
```
|∫ω·S·ω| ≤ ||ω||²_∞ ||S||_{L^1} ≤ ||ω||²_∞ · C ||∇u||_{L^1}
```

For concentration:
```
||∇u||_{L^1} ~ ||∇u||_∞ L³ ~ (T-t)^{-α-β+3β} = (T-t)^{-α+2β}
```

With β = 2α/3:
```
||∇u||_{L^1} ~ (T-t)^{-α + 4α/3} = (T-t)^{α/3}
```

So stretching bound:
```
|∫ω·S·ω| ≤ C (T-t)^{-4α} (T-t)^{α/3} = C (T-t)^{-11α/3}
```

This blows up faster than ||ω||²_∞ ~ (T-t)^{-4α} for α > 0.

Hmm, the stretching is not controlled by enstrophy. This is the fundamental obstruction.

---

## Approach 4: Critical Sobolev - L³ Analysis

### Serrin criterion
If u ∈ L^∞_t L³_x, then regularity.

### Scaling of ||u||_{L³}
```
||u||³_{L³} ~ ||u||³_∞ L³ ~ (T-t)^{-3α + 3β}
```

With β = 2α/3:
```
||u||³_{L³} ~ (T-t)^{-3α + 2α} = (T-t)^{-α}
||u||_{L³} ~ (T-t)^{-α/3}
```

This blows up for α > 0, so u ∉ L^∞_t L³_x. Consistent with blowup, not a constraint.

---

## Approach 5: Energy-Enstrophy Interpolation

### Key observation
Energy E and enstrophy Ω are related by:
```
Ω = (1/2)||ω||²_{L²} = (1/2)||∇u||²_{L²} (for div-free u)
```

So enstrophy = dissipation rate / ν:
```
dE/dt = -2νΩ
```

### Interpolation inequality
Gagliardo-Nirenberg:
```
||u||_{L^∞} ≤ C ||u||^{1/2}_{L^2} ||∇²u||^{1/2}_{L^2}  (3D)
```

But we need ||∇²u||, not just ||∇u||.

Actually, better:
```
||u||_{L^∞} ≤ C ||u||^{1/4}_{L^2} ||∇u||^{3/4}_{H^1}
```

This involves ||∇²u||_{L²} which is related to ||∇ω||_{L²}.

### Chain of inequalities

From NS, we have the enstrophy equation:
```
dΩ/dt = stretching - ν||∇ω||²
```

If we could bound stretching by a function of E and Ω:
```
stretching ≤ f(E, Ω)
```

Then we'd have a closed system.

The problem: stretching ~ ||ω||²_∞ ||S||_{L^1}, involving ||ω||_∞ which is NOT controlled by Ω.

---

## Approach 6: Concentration-Compactness Argument

### Setup
Consider rescaled solutions U_λ(τ,y) = λ^α u(T-λ, λ^{1/2}y).

As λ → 0, by concentration-compactness:
1. Vanishing: ||U_λ||_∞ → 0 (contradicts blowup)
2. Concentration: U_λ → U_∞ in some sense

### The limiting equation
For α ∈ (1/2, 1), the limiting equation is:
```
αU + (1/2)y·∇U + (U·∇)U = -∇P + 0·ΔU
```
(Viscous term vanishes since ν λ^{1-2·1/2} = νλ^0 = ν → 0 in the scaling limit... wait, let me recalculate.)

Rescaling: τ = -log(T-t), y = x/(T-t)^{1/2}

Time derivative transforms as:
```
∂u/∂t = (T-t)^{-1} ∂u/∂τ - (1/2)(T-t)^{-1} y·∇_y u · (T-t)^{-1/2}
      = (T-t)^{-1} [∂u/∂τ - (1/2)y·∇u / (T-t)^{1/2} · (T-t)^{1/2}]
      = (T-t)^{-1} [∂u/∂τ + (1/2)y·∇u]
```

Hmm, getting complicated. The key point:

For α ≠ 1/2, the rescaled equation is NOT self-similar Navier-Stokes.

### Liouville theorems for limiting equation
Theorems N, O, P in our paper show:
- α-Euler Liouville: Only U = 0 in L² or L^{3,∞}

This means the weak limit U_∞ = 0.

But ||U_λ||_∞ ~ 1 (by scaling), so strong convergence fails.

This is exactly the definition of Type II: weak limit zero, strong limit doesn't exist.

**The Liouville theorems don't close the gap; they confirm Type II structure.**

---

## Approach 7: Forward-in-Time Propagation

### The backward uniqueness limitation
ESS and other methods work backward from T:
- At t = T: singularity
- Propagate regularity backward

This confirms the past is smooth but can't prevent future singularity.

### Can we propagate forward?
Consider the vorticity equation:
```
∂ω/∂t + (u·∇)ω = (ω·∇)u + νΔω
```

If we could show: ||ω||_∞(t) is controlled for t < T implies ||ω||_∞(t') controlled for t' > t...

But this is exactly what we can't show! The stretching term (ω·∇)u can cause explosive growth.

### Maximum principle?
The vorticity equation doesn't satisfy a maximum principle because of the stretching term.

If stretching = 0 (2D case): ||ω||_∞ is monotone decreasing. No blowup!
In 3D: stretching is indefinite. No such control.

---

## Approach 8: Combined Energy-BKM Constraint

### New idea
The BKM integral involves ||ω||_∞. The energy bound involves ||u||_{L²}.

Can we find a single quantity involving both?

### Try: Q = E^a · (∫||ω||_∞ dt)^b

For Type II approaching blowup:
- E ~ (T-t)^{3-5α} → (T-t)^{3-5α}
- ∫_t^T ||ω||_∞ ds ~ ∫(T-s)^{-2α} ds ~ (T-t)^{1-2α} / (2α-1)

So:
```
Q(t) ~ (T-t)^{a(3-5α)} · (T-t)^{b(1-2α)}
     = (T-t)^{3a - 5aα + b - 2bα}
     = (T-t)^{(3a+b) - (5a+2b)α}
```

For Q → 0 as t → T (blowup): need (3a+b) - (5a+2b)α < 0

For Q bounded (regularity): need (3a+b) - (5a+2b)α ≥ 0

Critical: (3a+b) = (5a+2b)α, i.e., α = (3a+b)/(5a+2b)

For different (a,b):
- (a,b) = (1,0): α_crit = 3/5 (energy bound)
- (a,b) = (0,1): α_crit = 1/2 (BKM bound)
- (a,b) = (1,1): α_crit = 4/7 ≈ 0.571

**Interesting!** With (a,b) = (1,1), we get α_crit = 4/7, which is BETWEEN 1/2 and 3/5!

### Does this close the gap?

If we could show Q = E · ∫||ω||_∞ dt must remain bounded (or have specific behavior), then α ≥ 4/7 would be required.

But can we prove Q is bounded?

dQ/dt = E' · ∫||ω||_∞ + E · ||ω||_∞
      = -ν||∇u||² · ∫||ω||_∞ + E · ||ω||_∞

This has mixed signs. Not obviously bounded.

### Refined attempt
What if we use Q = E + c · ∫||ω||_∞ dt for some constant c?

Then:
```
dQ/dt = -ν||∇u||² + c||ω||_∞
```

For Q decreasing: need c||ω||_∞ < ν||∇u||²

Is this ever true?

||ω||_∞ / ||∇u||² ~ (T-t)^{-2α} / (T-t)^{-4α/3} = (T-t)^{-2α/3}

For small (T-t), this → ∞. So ||ω||_∞ >> ||∇u||² near blowup.

Thus Q is NOT monotone. This approach fails.

---

## Approach 9: Refined Scaling Analysis

### Re-examine the energy constraint
We claimed: For E to decrease, need 3 - 5α ≥ 0, i.e., α ≤ 3/5.

But this assumed β = 1 - α (a specific concentration scaling).

### What if β is different?
From Biot-Savart: ||u||_∞ ≤ C ||ω||_{L^{3/2}}

||ω||_{L^{3/2}} ~ ||ω||_∞ L² ~ (T-t)^{-2α + 2β}

For ||u||_∞ ~ (T-t)^{-α}:
```
(T-t)^{-α} ~ (T-t)^{-2α + 2β}
-α = -2α + 2β
β = α/2
```

So the MINIMAL concentration scale is β = α/2, not β = 2α/3.

With β = α/2:
```
E ~ (T-t)^{-2α + 3(α/2)} = (T-t)^{-2α + 3α/2} = (T-t)^{-α/2}
```

E → 0 as t → T for α > 0. This is DECREASING energy!

Wait, but then what's the constraint?

### Dissipation with β = α/2
```
||∇u||² ~ (T-t)^{-2α + β} = (T-t)^{-2α + α/2} = (T-t)^{-3α/2}
```

∫||∇u||² dt finite iff 3α/2 < 1, i.e., α < 2/3.

### Combined with BKM
- BKM: α ≥ 1/2
- Dissipation: α < 2/3

**Gap: [1/2, 2/3)**

This is WIDER than (1/2, 3/5)! I must have made an error somewhere.

### Resolution
The issue is: β = α/2 is the MINIMAL concentration scale from Biot-Savart alone. But physical concentration may be larger (β > α/2).

The energy constraint E ~ (T-t)^{-2α + 3β} ≤ E(0) requires:
```
-2α + 3β ≥ 0, i.e., β ≥ 2α/3
```

So β ≥ max(α/2, 2α/3) = 2α/3 for α > 0.

With β = 2α/3:
- E ~ (T-t)^{-2α + 2α} = (T-t)^0 = const (borderline)
- ||∇u||² ~ (T-t)^{-4α/3}
- Dissipation integral finite iff 4α/3 < 1, i.e., α < 3/4

So: 1/2 ≤ α < 3/4 with E = const at upper bound β = 2α/3.

But E = const means dE/dt = 0, which requires ||∇u||² = 0. Contradiction!

So β > 2α/3 strictly, meaning E decreases strictly.

**But we can take β arbitrarily close to 2α/3.**

In that limit, E → const, and we hit the contradiction.

### The upshot
The constraint is: β > 2α/3 (strict).

This gives E → 0, which is fine. But how fast?

E ~ (T-t)^{-2α + 3β} with β > 2α/3, so exponent > 0, E → 0.

The limit β → 2α/3 is forbidden because E = const is inconsistent.

**This still doesn't close the gap (1/2, 3/5).** It just confirms β > 2α/3 strictly.

---

## Summary: The Gap Persists

After examining 9 approaches:

1. **Refined BKM:** Consistent, no improvement
2. **Dissipation integral:** Gives α < 3/4, weaker than energy
3. **Enstrophy growth:** Stretching uncontrolled
4. **Critical Sobolev:** Confirms blowup structure, not a constraint
5. **Energy-enstrophy interpolation:** Missing ||ω||_∞ control
6. **Concentration-compactness:** Confirms weak limit = 0, not exclusion
7. **Forward propagation:** Stretching prevents control
8. **Combined E-BKM:** Mixed signs, not monotone
9. **Refined scaling:** Confirms β > 2α/3, doesn't close gap

**Conclusion:** The gap (1/2, 3/5) appears to be ROBUST.

No combination of known estimates closes it. New mathematics required.

---

## What Would Close the Gap

### Option A: New monotone quantity
Find Q with dQ/dt ≤ 0 and scaling dimension 0 (critical).

Obstruction: Vortex stretching ω_i ω_j S_ij appears in all candidates.

### Option B: Forward unique continuation
Prove: if u smooth on [0,t], then u smooth on [0, t+ε].

Obstruction: NS is not parabolic in the usual sense; nonlinearity is too strong.

### Option C: Geometric constraint
Show that vortex geometry forbids concentration.

This would require understanding vortex tube/sheet dynamics near singularity.

### Option D: Construct counterexample
Build a Type II solution with α ∈ (1/2, 3/5).

This would show blowup exists (solving Millennium Problem negatively).

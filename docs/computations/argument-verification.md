# Verification of Scaling Argument for Type II Impossibility

**Date:** 2026-01-12
**Purpose:** Carefully verify the argument that Type II blowup is self-inconsistent

---

## The Argument Summary

1. **BKM lower bound:** α ≥ 3/5
2. **Energy upper bound:** α ≤ 3/5
3. **Combined:** α = 3/5 exactly
4. **Contradiction at α = 3/5:** E constant but dE/dt → -∞

**Claimed conclusion:** Type II blowup is impossible for unforced 3D NS

---

## Gap Analysis

### Gap 1: Is the BKM lower bound of 3/5 tight?

**The standard argument:**
- BKM criterion: ∫||ω||_∞ dt = ∞ for blowup at T
- For Type II: ||ω||_∞ ~ (T-t)^{-2α}
- Integral diverges iff 2α ≥ 1, i.e., α ≥ 1/2

But where does 3/5 come from?

**The tighter bound:**
Using Biot-Savart: ||u||_∞ ≤ C ||ω||_{L^∞}^{1/2} ||ω||_{L^1}^{1/2}

For self-similar concentration:
- ||ω||_∞ ~ (T-t)^{-2α}
- ||ω||_{L^1} ~ ||ω||_∞ L³ ~ (T-t)^{-2α + 3(1-α)} = (T-t)^{3-5α}

Then:
||u||_∞ ≤ C (T-t)^{-α} (T-t)^{(3-5α)/2}
       = C (T-t)^{-α + (3-5α)/2}
       = C (T-t)^{(3-7α)/2}

For ||u||_∞ ~ (T-t)^{-α} we need:
α ≥ (3-7α)/2  →  2α ≥ 3-7α  →  9α ≥ 3  →  **α ≥ 1/3**

**Gap identified:** The standard BKM only gives α ≥ 1/2, not 3/5!

**Where does 3/5 come from?**
The 3/5 bound is actually from ENERGY, not BKM. Let me recalculate.

### Recalculation: Energy Bound

Energy: E ~ u² L³ ~ (T-t)^{-2α} (T-t)^{3(1-α)} = (T-t)^{3-5α}

For E decreasing: 3-5α ≥ 0 → **α ≤ 3/5**

This is an UPPER bound from energy!

### What's the actual lower bound?

**From BKM:** α ≥ 1/2 (for ∫||ω||_∞ dt to diverge)

**So the actual window is:** [1/2, 3/5] not {3/5}!

Wait, this changes everything. Let me re-examine.

---

## Revised Analysis

### Window is [1/2, 3/5], not {3/5}

**Lower bound:** α ≥ 1/2 (BKM)
**Upper bound:** α ≤ 3/5 (energy decay)

This gives a window of width 0.1 (from 0.5 to 0.6), not a single point!

### At α = 1/2 (self-similar)

- E ~ (T-t)^{3-5(1/2)} = (T-t)^{1/2}
- Energy INCREASES (not constant)
- This is problematic: energy should decrease

**Wait:** For unforced NS, dE/dt = -ν||∇u||² ≤ 0 always.
So E cannot increase! This rules out α < 3/5 too!

### The real constraint

**Theorem:** For unforced NS, E(t) is monotonically decreasing.

If E ~ (T-t)^{3-5α}:
- For α < 3/5: exponent > 0, E → 0 as t → T (fine)
- For α = 3/5: exponent = 0, E = const (fine)
- For α > 3/5: exponent < 0, E → ∞ as t → T (impossible!)

Wait, I had the direction wrong. Let me recalculate.

E ~ (T-t)^{3-5α}

As t → T, (T-t) → 0.

- If 3-5α > 0 (α < 3/5): (T-t)^{3-5α} → 0. Energy decreases. OK.
- If 3-5α = 0 (α = 3/5): E = const. Energy constant. Marginal.
- If 3-5α < 0 (α > 3/5): (T-t)^{3-5α} → ∞. Energy increases. IMPOSSIBLE!

**Conclusion:** α ≤ 3/5 is required, confirmed.

**But BKM gives α ≥ 1/2.** So window is [1/2, 3/5], width 0.1.

---

## Re-examination of the Contradiction

At α = 3/5:
- E ~ const
- dE/dt = -ν||∇u||²

If E = const, then dE/dt = 0, which requires ||∇u||² = 0.
But for blowup, ||u||_∞ → ∞, which typically requires ||∇u|| → ∞ somewhere.

**The contradiction is:** ||∇u||² = 0 but ||u||_∞ → ∞

This is impossible in finite-dimensional approximation, but could it happen in the PDE?

### Analysis: Can ||∇u|| = 0 while ||u||_∞ → ∞?

For ||∇u|| = 0 globally: u must be constant in space.
But ||u||_∞ → ∞ means the constant value → ∞.
This is incompatible with conservation properties.

Actually, let's be more careful. dE/dt = -ν ∫|∇u|² dx = 0 means ∫|∇u|² = 0.
This means ∇u = 0 a.e., so u is constant.
A constant u has ||u||_∞ = constant, cannot blow up.

**Contradiction confirmed at α = 3/5.**

---

## The Window [1/2, 3/5)

For α ∈ [1/2, 3/5):
- E ~ (T-t)^{3-5α} with 3-5α > 0
- E → 0 as t → T
- dE/dt = -ν||∇u||² ≤ 0 (always true)

This is consistent! No contradiction for α < 3/5.

### But can such blowup occur?

At α = 1/2 (self-similar):
- E ~ (T-t)^{1/2} → 0
- ||u||_∞ ~ (T-t)^{-1/2} → ∞
- These are consistent with scaling

**Key question:** Do self-similar profiles exist?

**Answer:** NO. Theorems D, F, H, I rule out all profile-based blowup.

But what about non-self-similar Type II with α ∈ [1/2, 3/5)?

---

## Non-Self-Similar Type II in [1/2, 3/5)

For non-self-similar Type II:
- No profile equation to solve
- Just need ||u||_∞ ~ (T-t)^{-α} asymptotically
- Not ruled out by profile theorems

### What we know:

1. **Profile-based at α = 1/2:** Ruled out (Theorems D, F)
2. **Generalized profiles:** Ruled out (Theorems H, I)
3. **Non-profile Type II:** NOT directly ruled out

### The open question:

Can there be non-self-similar blowup with α ∈ [1/2, 3/5)?

This would have:
- E → 0 (consistent with decay)
- ||u||_∞ → ∞ (blowup)
- No self-similar structure

**This is the actual gap!**

---

## Revised Status

| Region | Status |
|--------|--------|
| α < 1/2 | RULED OUT (BKM) |
| α = 1/2 self-similar | RULED OUT (profiles) |
| α ∈ (1/2, 3/5) non-SS | **OPEN** |
| α = 3/5 | Self-inconsistent |
| α > 3/5 | RULED OUT (energy) |

**The actual gap is (1/2, 3/5), width 0.1, not [3/5, 3/4)!**

---

## Wait - Reconciling with Previous Analysis

The previous analysis had window [3/5, 3/4). Where did 3/4 come from?

**Upper bound 3/4:** From dissipation integral ∫||∇u||² dt

At α = 3/4: ||∇u||² ~ (T-t)^{-1.5}, integral diverges like (T-t)^{-0.5}
This is infinite, violating energy bound ∫||∇u||² dt < E(0)/ν.

So α < 3/4 from dissipation integral, not energy scaling.

### Reconciliation

**Energy scaling:** E ~ (T-t)^{3-5α}
- For E bounded below (E ≥ 0): need 3-5α ≥ 0, i.e., α ≤ 3/5

**Dissipation integral:** ∫||∇u||² dt < ∞
- ||∇u||² ~ (T-t)^{-2(α+(1-α))} = (T-t)^{-2α + 2α - 2} = (T-t)^{-2}...

Actually let me redo this more carefully.

For concentration on scale L ~ (T-t)^β:
- ||∇u||² ~ (u/L)² L³ ~ (T-t)^{-2α-2β+3β} = (T-t)^{-2α+β}

With β = 1-α:
||∇u||² ~ (T-t)^{-2α+(1-α)} = (T-t)^{1-3α}

Integral: ∫(T-t)^{1-3α} dt converges iff 1-3α > -1, i.e., 3α < 2, i.e., α < 2/3.

**So α < 2/3 from dissipation, not α < 3/4!**

### The correct bounds

1. **BKM:** α ≥ 1/2
2. **Energy scaling:** α ≤ 3/5
3. **Dissipation integral:** α < 2/3

Combined: α ∈ [1/2, 3/5]

At α = 3/5 = 0.6: dissipation integral ~ ∫(T-t)^{1-1.8} = ∫(T-t)^{-0.8}, diverges.

Wait, 1-3(3/5) = 1 - 9/5 = -4/5 = -0.8, which is < -1.
So integral DIVERGES at α = 3/5!

This is another constraint: α < 2/3 from dissipation, not α ≤ 3/5.

---

## Final Reconciliation

**The constraints:**
1. BKM: α ≥ 1/2
2. Energy scaling (E ≥ 0): α ≤ 3/5
3. Dissipation integral (finite): α < 2/3

The tightest combination is:
- Lower: 1/2
- Upper: min(3/5, 2/3) = 3/5

**Window: [1/2, 3/5]**

At α = 3/5: energy scaling says E = const, but this is edge case.

At α ∈ (1/2, 3/5): E → 0, dissipation integrable, BKM satisfied.

**This is the TRUE residual window, width 0.1.**

---

## Conclusion

The scaling argument has been REFINED:

1. **Old claim:** α = 3/5 is the only possible rate
2. **New finding:** Window is actually [1/2, 3/5], width 0.1

The profile theorems rule out α = 1/2 self-similar.
But non-self-similar α ∈ (1/2, 3/5) is NOT ruled out by our arguments.

**Status:** Gap narrowed from [3/5, 3/4) = 0.15 to (1/2, 3/5) = 0.1
But gap persists.

The TYPE_II_RULED_OUT promise CANNOT be output - there is still a gap!

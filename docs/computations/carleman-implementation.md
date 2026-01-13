# Carleman Approach Implementation: Attempt to Prove Condition (1.4)

**Date:** January 13, 2026
**Status:** PROOF ATTEMPT IN PROGRESS

---

## Goal

Prove that for suitable weak solutions near Type II blowup with rate α ∈ (1/2, 3/5):
```
sup_{0 < r < 1} A_{m₁}(v, r) < ∞
```

where A_{m₁}(v, r) = r^{-(2m-1)} sup_t ∫_{B(r)} |v|² dx and m ∈ (1/2, 3/5).

---

## Part 1: Carleman Inequality Setup

### 1.1 Standard Parabolic Carleman Inequality

For the heat equation ∂_t u - νΔu = f in a parabolic cylinder Q = B_R × (-T, 0):

**Theorem (Carleman for Heat):** There exist C > 0 and λ₀ > 0 such that for all λ > λ₀:
```
λ³ ∫_Q e^{2λφ} |u|² dx dt + λ ∫_Q e^{2λφ} |∇u|² dx dt
≤ C ∫_Q e^{2λφ} |∂_t u - νΔu|² dx dt + boundary terms
```

where φ(x,t) = |x|²/(4ν(T+t)) is the backward heat kernel weight.

### 1.2 Adaptation to Navier-Stokes

For NS: ∂_t u - νΔu = -u·∇u - ∇p

The source term is f = -u·∇u - ∇p.

**Key observation:** ||f||_{L²} ≤ ||u||_{L³} ||∇u||_{L²} + ||∇p||_{L²}

By pressure estimates: ||∇p||_{L^{3/2}} ≤ C ||u||²_{L³}

### 1.3 Localized Carleman Weight

Define for r > 0 and center at potential singularity (0, T):
```
φ_r(x,t) = exp(λ|x|²/r²) · η(|x|/r) · θ((T-t)/r²)
```

where:
- η is a smooth cutoff: η = 1 on [0, 1], η = 0 on [2, ∞)
- θ is a temporal cutoff: θ = 1 on [0, 1], θ = 0 on [2, ∞)
- λ > 0 is the Carleman parameter

---

## Part 2: Key Lemmas

### Lemma A (Local L² from Carleman)

**Statement:** For suitable weak solutions of NS with Type II rate α ∈ (1/2, 3/5), there exists β(α) > 0 such that:
```
||u||_{L²(B_r)}² ≤ C(α, E₀, ν) r^{2β(α)} ||∇u||_{L²(B_{2r})}²
```

for all r ∈ (0, r_*) where r_* = C(E₀/ν)³.

**Attempted Proof:**

Step 1: Apply Carleman inequality to NS in Q_r = B_r × (T-r², T):
```
λ³ ∫_{Q_r} e^{2λφ} |u|² ≤ C ∫_{Q_r} e^{2λφ} |u·∇u + ∇p|² + bdry
```

Step 2: Bound the RHS using Hölder:
```
∫_{Q_r} e^{2λφ} |u·∇u|² ≤ e^{2λ·4} ∫_{Q_r} |u|² |∇u|² dx dt
                        ≤ e^{8λ} ||u||²_{L^∞_t L³_x} ||∇u||²_{L²(Q_r)}
```

Step 3: Use Type II structure ||u||_{L³} ≤ C(T-t)^{-α+1/2}:
```
||u||²_{L^∞_t L³_x(Q_r)} ≤ C (T-T+r²)^{-2α+1} = C r^{2-4α}
```

Step 4: For α < 3/4: exponent 2-4α > -1, so this is bounded by r^{2-4α}.

**PROBLEM:** The exponential e^{8λ} on RHS grows faster than λ³ on LHS!

This is the **exponential loss** problem that arXiv:2510.20757 addresses via "careful bookkeeping."

---

### Lemma A - Revised Approach

**Key insight from Barker:** Use BACKWARD propagation with decreasing λ.

Step 1': Start at scale R and propagate to scale r < R.

Choose λ(r) = λ₀ (R/r)^{1/2} (decreasing as r → 0).

Step 2': At each scale, the gain from λ³ is:
```
gain = λ(r)³ = λ₀³ (R/r)^{3/2}
```

Step 3': The exponential factor becomes:
```
e^{2λφ} ≤ e^{2λ₀(R/r)^{1/2} · 4} = e^{8λ₀(R/r)^{1/2}}
```

Step 4': Compare: λ³ ~ (R/r)^{3/2} vs e^{Cλ} ~ exp(C(R/r)^{1/2})

**STILL PROBLEMATIC:** Exponential beats polynomial!

---

### Alternative: Iteration Without Carleman

Let me try a different approach using iteration of local energy inequalities.

**CKN Local Energy Inequality:**
```
sup_t ∫_{B(r/2)} |u|² η² + ν ∫∫_{Q(r)} |∇u|² η²
≤ ∫∫_{Q(r)} |u|² (∂_t η² + νΔη²) + ∫∫_{Q(r)} (|u|² + 2p)(u·∇η²)
```

**Iteration scheme:**

Let r_k = 2^{-k} R for k = 0, 1, 2, ...

Define A_k = sup_t ∫_{B(r_k)} |u|² dx

**Claim:** A_{k+1} ≤ (1/2) A_k + C r_k^{4-4α} E₀²

If true, this gives geometric decay!

**Proof attempt:**

From CKN with η supported in B(r_k):
```
A_{k+1} ≤ C/r_k² ∫∫_{Q(r_k)} |u|² + C/r_k ∫∫_{Q(r_k)} |u|³ + |p||u|
```

Term 1: ∫∫_{Q(r_k)} |u|² ≤ r_k² · A_k (time integral)

Term 2: ∫∫_{Q(r_k)} |u|³ ≤ r_k² · ||u||³_{L^∞_t L³} ≤ r_k² · (r_k^{(1-2α)})³ = r_k^{5-6α}

For α < 5/6: exponent > 0, this decays!

**BUT:** For α ∈ (1/2, 3/5), we have 5-6α ∈ (-1, 2).

At α = 3/5: 5 - 6(3/5) = 5 - 18/5 = 7/5 > 0. ✓

At α = 1/2: 5 - 6(1/2) = 5 - 3 = 2 > 0. ✓

**This looks promising!**

---

## Part 3: Rigorous Iteration

### Setup

Let (0, T) be a potential Type II singularity with rate α ∈ (1/2, 3/5).

Define:
- R = 1 (initial scale)
- r_k = 2^{-k} for k = 0, 1, 2, ...
- Q_k = B(r_k) × (T - r_k², T)
- A_k = r_k^{-(2m-1)} sup_{t ∈ (T-r_k², T)} ||u(t)||²_{L²(B(r_k))}

**Goal:** Show sup_k A_k < ∞.

### Type II Concentration Structure

By Type II definition:
```
||u(t)||_∞ ≤ M (T-t)^{-α}
```

Concentration scale: L(t) ~ (T-t)^{2α/3}

At time t = T - r_k²:
```
L(T - r_k²) ~ r_k^{4α/3}
```

For r_k >> L(t): flow is approximately smooth.
For r_k ~ L(t): this is the concentration scale.

### Case 1: r_k >> L(t) (Away from Concentration)

Here r_k >> r_k^{4α/3}, i.e., r_k^{1-4α/3} >> 1.

Since 1 - 4α/3 > 0 for α < 3/4, this holds for small r_k when α < 3/4.

**Wait, this is backwards.** For small r_k, r_k^{positive} → 0, not infinity.

Let me reconsider. r_k >> L means r_k >> r_k^{4α/3}.

For α < 3/4: 4α/3 < 1, so r_k^{4α/3} >> r_k for small r_k.

Therefore r_k << L(T - r_k²) for small r_k. We're INSIDE the concentration!

### Case 2: r_k << L(t) (Inside Concentration)

This is the hard case. The flow concentrates at scale L >> r_k.

In this regime, the L² mass in B(r_k) is a FRACTION of total:
```
||u||²_{L²(B(r_k))} ~ (r_k/L)³ ||u||²_{L²(B(L))} ~ (r_k/L)³ · E₀
```

This gives:
```
||u||²_{L²(B(r_k))} ≤ C E₀ (r_k/L)³ = C E₀ r_k³ / r_k^{4α} = C E₀ r_k^{3-4α}
```

Therefore:
```
A_k = r_k^{-(2m-1)} ||u||²_{L²(B(r_k))} ≤ C E₀ r_k^{3-4α-(2m-1)} = C E₀ r_k^{4-4α-2m}
```

**For boundedness:** Need 4 - 4α - 2m ≥ 0, i.e., α ≤ (4-2m)/4 = 1 - m/2.

For m = 0.55: need α ≤ 1 - 0.275 = 0.725.
For m = 0.5: need α ≤ 0.75.

**The condition α < 3/4 is EXACTLY what we need!**

But wait - this assumed ||u||²_{L²(B(L))} ~ E₀, which is the global energy.

**The key question:** Is the L² mass uniformly distributed or concentrated?

---

## Part 4: The Concentration Obstacle

### The Problem

Even with Type II structure, the L² mass could be VERY concentrated:
```
||u||²_{L²(B(r))} could be ~ ||u||²_{L²} for r ~ L
```

not ~ (r/L)³ ||u||²_{L²}.

### What Would Make It Work

**Hypothesis (H):** The rescaled solution at scale L has bounded shape:
```
u(x,t) ≈ (T-t)^{-α} U((x-x_0)/L(t))
```
where ||U||_{L²(B(1))} ~ ||U||_{L²} (no further concentration).

Under (H):
```
||u||²_{L²(B(r))} ~ (T-t)^{-2α} L³ (r/L)³ ||U||²_{L²(B(1))}
                 ~ (T-t)^{-2α+2α} r³ ||U||²
                 ~ r³ E₀
```

This gives A_k ~ r_k^{3-(2m-1)} = r_k^{4-2m} → 0 for m < 2. ✓

### Testing Hypothesis (H)

Hypothesis (H) says: after one level of rescaling, no further concentration.

**This is equivalent to:** The rescaled solution converges to a non-trivial limit.

**But we proved:** Rescaled Type II solutions have weak limit V ≡ 0!

**Contradiction?** Not quite. The weak limit being 0 means concentration happens at EVERY scale.

This is the **cascade scenario** - concentration at all scales simultaneously.

---

## Part 5: Cascade Analysis

### Multi-Scale Concentration

Suppose concentration happens at ALL scales r_k:

At each scale r_k, define the local energy fraction:
```
f_k = ||u||²_{L²(B(r_k))} / ||u||²_{L²(B(r_{k-1}))}
```

If concentration is self-similar: f_k ≈ f for all k.

Then:
```
||u||²_{L²(B(r_k))} = f^k ||u||²_{L²(B(1))} = f^k E₀
```

For f < 1:
```
A_k = r_k^{-(2m-1)} f^k E₀ = 2^{k(2m-1)} f^k E₀ = (2^{2m-1} f)^k E₀
```

**Bounded iff** 2^{2m-1} f < 1, i.e., f < 2^{-(2m-1)} = 2^{1-2m}.

For m = 0.55: need f < 2^{-0.1} ≈ 0.93.

**Question:** Is f < 0.93 automatic for Type II?

### Energy Conservation Constraint

Total energy: E = ||u||²_{L²} = constant.

If concentration factor is f at each scale:
```
Sum_k [energy at scale r_k but not r_{k+1}] = E
```

Energy in shell B(r_k) \ B(r_{k+1}):
```
||u||²_{L²(B(r_k) \ B(r_{k+1}))} = (1-f) ||u||²_{L²(B(r_k))} = (1-f) f^{k-1} E
```

Sum: E = Σ_k (1-f) f^{k-1} E = E. ✓ (automatic)

**Energy conservation doesn't constrain f!**

### Dissipation Constraint

Dissipation: D = ν ∫ ||∇u||² dt must be finite.

In the concentrating region:
```
||∇u||² ~ ||u||²/L² ~ (T-t)^{-2α} / (T-t)^{4α/3} = (T-t)^{-2α-4α/3} = (T-t)^{-10α/3}
```

Time integral:
```
∫_0^T (T-t)^{-10α/3} dt converges iff -10α/3 > -1, i.e., α < 3/10.
```

**But α > 1/2 > 3/10, so dissipation integral DIVERGES!**

Wait, this contradicts finite dissipation...

### Resolution: Refined Dissipation Analysis

The dissipation is:
```
D = ν ∫_0^T ||∇u(t)||²_{L²} dt
```

For Type II with ||u||_∞ ~ (T-t)^{-α}:
- ||∇u||_{L²} ~ ||∇u||_∞ · L^{3/2} ~ (T-t)^{-α-1} · (T-t)^α = (T-t)^{-1}

Actually need more care. Let me use scaling:
```
||∇u||²_{L²} ~ ||u||²_{L²} / L² = E₀ / (T-t)^{4α/3}
```

Time integral:
```
∫_0^T (T-t)^{-4α/3} dt converges iff -4α/3 > -1, i.e., α < 3/4.
```

**For α < 3/4:** Dissipation is finite! ✓

**For α ≥ 3/4:** Dissipation diverges → impossible.

This confirms α < 3/4 is necessary for Type II.

---

## Part 6: The Key Estimate

### Proposition (Local Energy Decay)

For Type II with α ∈ (1/2, 3/4), if the concentration is "regular" (Hypothesis H holds), then:
```
A_{m₁}(r) = r^{-(2m-1)} ||u||²_{L²(B(r))} ≤ C(α, E₀, ν) r^{4-2m-4α}
```

For m ∈ (1/2, 3/5) and α ∈ (1/2, 3/5):
- Exponent: 4 - 2m - 4α ∈ (4 - 1.2 - 2.4, 4 - 1 - 2) = (0.4, 1)

**The exponent is POSITIVE! A_{m₁} decays!**

### The Remaining Gap

**What's missing:** Proof that Hypothesis (H) holds.

Hypothesis (H) states that after rescaling to scale L, there's no further concentration.

**Equivalent to:** The profile decomposition has only ONE profile (plus decaying error).

**The obstruction:** We proved the profile is V ≡ 0. But maybe the ERROR term carries the energy?

---

## Part 7: Conclusion of Attempt

### What Was Achieved

1. **Identified the key estimate:** A_{m₁} ~ r^{4-2m-4α} under Hypothesis (H)
2. **Showed exponent is positive** for α, m ∈ (1/2, 3/5)
3. **Confirmed α < 3/4** from dissipation integral

### What Remains Unproven

**Hypothesis (H):** No concentration beyond scale L.

This is equivalent to proving that the rescaled solution converges STRONGLY (not just weakly) to something.

But we know:
- Weak limit = 0 (Liouville)
- Strong convergence fails (that's what Type II means!)

**The cascade scenario** - concentration at all scales - is NOT ruled out by our analysis.

### Status

**PROOF INCOMPLETE**

The Carleman/iteration approach reduces the problem to proving Hypothesis (H), which is essentially the same as ruling out multi-scale cascade concentration.

This is the SAME obstruction we encountered before, just reformulated.

---

## Part 8: What Would Complete the Proof

### Option A: Prove Hypothesis (H) Directly

Show that Type II concentration can only happen at ONE scale, not cascading.

**Possible approach:** Use the structure of NS nonlinearity to show cascades are unstable.

### Option B: Handle Cascade Directly

Show that even with f < 1 concentration at each scale:
```
A_k = (2^{2m-1} f)^k E₀ bounded requires f < 2^{1-2m}
```

**Need to prove:** f < 2^{1-2m} ≈ 0.93 for Type II with α ∈ (1/2, 3/5).

### Option C: Different Approach Entirely

The Carleman approach as attempted doesn't directly overcome the cascade obstacle.

Need fundamentally different mathematics - perhaps:
- Stochastic/probabilistic bounds on f
- Geometric constraints from vorticity direction
- Topological obstruction to cascades

---

## Summary

**The Carleman implementation attempt shows:**

1. Under Hypothesis (H) (no cascade), condition (1.4) IS satisfied
2. The cascade scenario is the TRUE remaining obstacle
3. Bounding the concentration factor f < 2^{1-2m} would complete the proof

**TYPE_II_RULED_OUT promise still CANNOT be output.**

The gap (1/2, 3/5) remains open due to the cascade obstruction.

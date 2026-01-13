# Blowup Construction Analysis: Exploiting the Gap

**Date:** January 13, 2026
**Status:** OFFENSIVE STRATEGY - CONSTRUCTING BLOWUP

---

## Paradigm Shift

Instead of proving regularity (defense), we now try to prove BLOWUP EXISTS (offense).

**Key vulnerabilities identified in the regularity proof:**
1. C(r) is NOT monotone - concentration can INCREASE
2. Energy is the ONLY monotone quantity - everything else is free
3. Dimensional gap gives "freedom" for concentration
4. No obstruction to cascades with variable f(k)

---

## Part 1: Exploiting C(r) Non-Monotonicity

### The Concentration Function

```
C(r) = sup_x ∫_{B(x,r)} |u|² dx / ∫ |u|² dx
```

**What we proved earlier:** dC/dt can have EITHER sign.

**For blowup:** We WANT dC/dt > 0 (concentration increasing).

### When Does C(r) Increase?

From entropy methods analysis:
```
dC/dt = [flux terms] - [dissipation redistribution]
```

C(r) INCREASES when:
1. Energy flows INTO the concentration region faster than it flows out
2. Dissipation preferentially depletes non-concentrated regions
3. Vortex stretching amplifies local velocity in concentration region

### Designing for Concentration Growth

**Optimal geometry for dC/dt > 0:**

Consider axisymmetric flow with concentration at origin:
- Swirl velocity u_θ = Γ/(2πr) (vortex)
- Axial strain: ∂u_z/∂z > 0 pulls fluid inward
- Combined: vortex intensifies as it's stretched

The strain-vorticity alignment ω·Sω > 0 gives:
```
d|ω|/dt = ω·Sω / |ω| > 0
```

This INCREASES local vorticity, hence local velocity, hence C(r).

---

## Part 2: Energy Budget Allows Local Concentration

### Global vs Local Energy

**Global:** dE/dt = -ν||∇u||² ≤ 0 (ALWAYS)

**Local:** d/dt ∫_{B(r)} |u|² = flux through ∂B(r) - local dissipation

The local energy can INCREASE even while global energy decreases!

### The Key Inequality

For blowup, we need:
```
||u||_{L²(B(r))} / ||u||_{L²} → ∞ as t → T
```

while
```
||u||_{L²} ≤ ||u_0||_{L²} (bounded)
```

This means ||u||_{L²(B(r))} must grow while ||u||_{L²} stays bounded.

**Is this possible?** YES, if energy concentrates spatially.

### Concentration Mechanism

Energy concentrates when:
1. Inward flux dominates outward flux through ∂B(r)
2. Local dissipation is weaker than flux differential
3. This requires specific velocity field geometry

---

## Part 3: The Variable Cascade

### Constant f Fails

Constant concentration factor f at each scale:
- Coherent cascade: needs f >> 1 (impossible since f ≤ 1)
- This ruled out CONSTANT f cascades

### Variable f(k) Can Work!

Let f_k vary with scale k = -log_2(r_k):

**Constraint 1 (Dissipation):**
```
∫_0^T ||∇u||² dt < ∞
```
requires the cascade to not accumulate too much gradient.

**Constraint 2 (Blowup):**
```
||u||_∞ → ∞
```
requires sufficient concentration at small scales.

### The Sweet Spot

Try f_k = c · k^{-γ} for some c, γ > 0:

**Dissipation integral:**
```
||∇u||² ~ Σ_k ||u||²_{L²(S_k)} / r_k²
        ~ Σ_k f_1·f_2·...·f_k · E_0 / r_k²
        = E_0 Σ_k (4^k) Π_{j≤k} f_j
        = E_0 Σ_k 4^k · c^k / (k!)^γ
```

For γ > 0: Σ_k 4^k / (k!)^γ < ∞ (converges!)

**L^∞ growth:**
```
||u||_∞ ~ max_k ||u||_{L²(B(r_k))} / r_k^{3/2}
        ~ max_k (Π_{j≤k} f_j)^{1/2} · E_0^{1/2} / r_k^{3/2}
        = max_k c^{k/2} / (k!)^{γ/2} · 2^{3k/2} · E_0^{1/2}
        = E_0^{1/2} max_k (c · 2^3)^{k/2} / (k!)^{γ/2}
```

For small γ and c·8 > 1: this can diverge as k_max → ∞!

### The Critical Exponent

**Dissipation converges if:** γ > 0
**||u||_∞ diverges if:** γ < 1 and c·8 > 1

**THERE EXISTS A WINDOW:** 0 < γ < 1 where BOTH:
- Dissipation is finite (NS constraint satisfied)
- ||u||_∞ → ∞ (blowup achieved!)

---

## Part 4: Modified Self-Similar Ansatz

### Pure Self-Similar is Ruled Out

u(x,t) = (T-t)^{-1/2} U(x/(T-t)^{1/2}) gives:
- Profile equation for U
- Liouville theorem: U ≡ 0

### Non-Self-Similar Modification

Try:
```
u(x,t) = (T-t)^{-α} V(x/(T-t)^β, τ)
```
where τ = -log(T-t) and α, β are to be determined.

**NS becomes:**
```
∂_τ V + [(β - α)V + β y·∇_y V] = -(V·∇_y)V - ∇_y P + ν(T-t)^{2β-1} Δ_y V
```

For α ∈ (1/2, 3/5) and β = (1+α)/2:
- The viscous term has coefficient (T-t)^{2β-1} = (T-t)^α → 0
- In the limit, V satisfies EULER (not NS)!

### Euler Limit

As t → T, the rescaled solution V approaches:
```
∂_τ V + [(β-α)V + β y·∇V] = -(V·∇)V - ∇P
```

This is α-Euler! Seregin's Liouville says: if V is in certain spaces, V ≡ 0.

**But:** The Liouville requires condition (1.4) - which is what we're trying to violate!

### The Loophole

**Seregin's theorem:** IF (1.4) holds, THEN Type II ruled out.

**Contrapositive:** IF Type II exists, THEN (1.4) fails.

So for blowup: we need V NOT in the Liouville class.

This means:
```
sup_r r^{-(2m-1)} ||V||²_{L²(B(r))} = ∞
```

**Question:** Does such V exist for α-Euler?

---

## Part 5: Candidate Blowup Structure

### Requirements for Type II

1. ||u||_∞ ~ (T-t)^{-α} with α ∈ (1/2, 3/5)
2. Global energy E bounded
3. Dissipation ∫||∇u||² dt finite
4. Seregin (1.4) FAILS: A_{m₁} → ∞

### Proposed Structure

**Geometry:** Axisymmetric with swirl, concentrating at a point.

**Velocity field:**
```
u_r = -α r f(r/(T-t)^β) / (T-t)
u_θ = Γ(t) / (2πr) · g(r/(T-t)^β)
u_z = 2α z f(r/(T-t)^β) / (T-t)
```

where f, g are profile functions with:
- f(0) = 1, f(∞) = 0 (localized)
- g(0) = 1, g(∞) = 0 (localized vortex)
- Γ(t) ~ (T-t)^{-α+1/2} (growing circulation)

**Checking NS:**
- Incompressibility: ∂(ru_r)/∂r + r ∂u_z/∂z = 0 ✓ (by construction)
- Swirl equation: ∂Γ/∂t + u_r ∂Γ/∂r = ν Δ_* Γ
  - LHS ~ (T-t)^{-α-1/2}
  - RHS ~ ν (T-t)^{-α+1/2} / (T-t)^{2β} ~ ν (T-t)^{-α-2β+1/2}
  - Balance requires: -α-1/2 = -α-2β+1/2, so β = 1/2

Wait, this gives β = 1/2, which is self-similar scaling!

### The Obstruction (Again)

Every attempt to construct blowup leads back to self-similar scaling, which is ruled out.

**The deep reason:** NS has a single length scale (ν t)^{1/2}, and any blowup must respect this.

---

## Part 6: Non-Self-Similar Escape

### Breaking Self-Similarity

To avoid the Liouville trap, we need structure that is NOT approximately self-similar even rescaled.

**Options:**
1. **Oscillatory:** V(y, τ) = V_0(y) cos(ω τ) - oscillating profile
2. **Cascade:** V(y, τ) builds fine structure as τ increases
3. **Multi-scale:** V has structure at MANY scales simultaneously

### The Cascade Option

Instead of single-scale concentration, try:
```
u(x,t) = Σ_k u_k(x,t)
```
where u_k is concentrated at scale r_k ~ 2^{-k} (T-t)^β.

Each u_k contributes:
- ||u_k||² ~ f_k · E_k (energy at scale k)
- ||∇u_k||² ~ f_k · E_k / r_k²

The cascade distributes energy across scales, avoiding single-scale Liouville.

### Compatibility Check

For cascade with f_k = c/k^γ, γ ∈ (0,1):

**Energy at each scale:**
```
E_k = Π_{j≤k} f_j · E_0 = c^k / (k!)^γ · E_0
```

**Dissipation:**
```
D = Σ_k E_k / r_k² = E_0 Σ_k c^k · 4^k / (k!)^γ
```

For γ > 0: D < ∞ ✓

**||u||_∞:**
```
||u||_∞ ≥ ||u_k||_{L^∞} ~ E_k^{1/2} / r_k^{3/2} ~ (c·8)^{k/2} / (k!)^{γ/2}
```

For small γ: can diverge ✓

**A_{m₁}:**
```
A_{m₁}(r_k) = r_k^{-(2m-1)} ||u||²_{L²(B(r_k))}
            ~ r_k^{-(2m-1)} · Σ_{j≤k} E_j
            ~ 2^{k(2m-1)} · c^k / (k!)^γ
            ~ (2^{2m-1} · c)^k / (k!)^γ
```

For 2^{2m-1} · c > 1 and small γ: can diverge ✓

### The Candidate

**Type II blowup might exist with:**
- Variable cascade: f_k ~ c/k^γ, γ ∈ (0, 1/2)
- c ~ 0.6 (so c·8 ~ 5 > 1)
- 2^{2m-1} · c ~ 0.6 · 1.07 ~ 0.64 < 1

Wait, 2^{2m-1} ~ 2^{0.1} ~ 1.07 for m = 0.55.
So 2^{2m-1} · c ~ 0.64 < 1.

**This means A_{m₁} CONVERGES, not diverges!**

Let me recalculate...

For A_{m₁} to diverge: need 2^{2m-1} · c > 1, so c > 2^{1-2m} ~ 0.93.

But for dissipation to converge with simple f_k = c: need c < 1/4 = 0.25.

**These constraints are INCOMPATIBLE!**

---

## Part 7: The Fundamental Obstruction (Revisited)

### Why Blowup Construction Fails

Every construction attempt hits the same wall:

1. **Dissipation constraint:** c < 1/4 (or f_k → 0)
2. **A_{m₁} divergence:** c > 0.93

These CANNOT be simultaneously satisfied with constant or simple variable f_k.

### What This Means

**The gap (1/2, 3/5) might be empty after all!**

The same dimensional mismatch that prevents us from PROVING regularity also prevents us from CONSTRUCTING blowup.

### The Either/Or

Either:
1. **Blowup exists** with very exotic structure (not cascade-like)
2. **Blowup doesn't exist** (regularity holds)

The analysis cannot determine which, but suggests:
- Simple constructions fail
- If blowup exists, it's very subtle
- Regularity is plausible

---

## Part 8: Conclusions

### What We Learned

1. C(r) non-monotonicity ALLOWS concentration but doesn't FORCE it
2. Variable cascade f_k can satisfy dissipation OR A_{m₁} divergence, NOT both
3. All simple blowup constructions fail
4. The gap (1/2, 3/5) may be genuinely empty

### Remaining Possibilities

**For blowup:**
- Non-cascade concentration (e.g., fractal)
- Oscillatory profiles evading Liouville
- Boundary-driven (Hou-Luo style)
- Multi-component (non-homogeneous)

**For regularity:**
- The construction failure suggests regularity
- New proof might exploit why constructions fail

### Status

**BLOWUP CONSTRUCTION: FAILED (so far)**

All attempted constructions hit incompatible constraints.
This provides indirect evidence for regularity.

**Neither TYPE_II_RULED_OUT nor BLOWUP_EXISTS can be claimed.**

# Energy Deconcentration for Ancient Euler Limits from Type II Blowup

**Date:** January 13, 2026
**Status:** CRITICAL ANALYSIS - Gap Identification

---

## 1. The Claim

For the ancient Euler limit V arising from Type II blowup rescaling:

$$E_R(\tau) = \int_{|y|<R} |V(y,\tau)|^2 \, dy \to 0 \quad \text{as } \tau \to -\infty$$

for any fixed R > 0.

**Goal:** Prove this backward dispersion, which combined with Euler energy conservation would force V = 0.

---

## 2. Setup and Rescaling Framework

### 2.1 Original Solution

Let u(x,t) be a hypothetical Type II blowup solution at (0,T) with rate α ∈ (1/2, 3/5):
- ||u(·,t)||_{L²} ≤ ||u₀||_{L²} (global energy bound)
- ||u(·,t)||_{L^∞} ~ C(T-t)^{-α} (Type II rate)
- Concentration at scale L(t) ~ (T-t)^β with β = (1+α)/2

### 2.2 The Rescaling

Following Seregin's framework, define:

$$V_\lambda(y, \tau) = \lambda^\alpha u(\lambda y, T + \lambda^{1+\alpha} \tau)$$

for λ > 0 and τ < 0 (so that T + λ^{1+α}τ < T).

The ancient Euler limit V is:

$$V(y,\tau) = \lim_{\lambda \to 0} V_\lambda(y,\tau)$$

where the limit exists (under appropriate conditions) and V solves the Euler equations for τ ∈ (-∞, 0).

### 2.3 Time Correspondence

For the rescaled solution V_λ at time τ < 0:
- Original time: t = T + λ^{1+α}τ
- Time to blowup: T - t = -λ^{1+α}τ = λ^{1+α}|τ|

As τ → -∞ with λ fixed: t → -∞ (far in the past of original solution).

But V is the **limit** as λ → 0. The key subtlety is understanding what τ → -∞ means for the limit V.

---

## 3. First Attempt: Direct Scaling

### 3.1 Energy Transformation

Consider:

$$E_R^\lambda(\tau) = \int_{|y|<R} |V_\lambda(y,\tau)|^2 \, dy$$

Substituting the definition:

$$E_R^\lambda(\tau) = \int_{|y|<R} \lambda^{2\alpha} |u(\lambda y, T + \lambda^{1+\alpha}\tau)|^2 \, dy$$

Change variables x = λy:

$$E_R^\lambda(\tau) = \lambda^{2\alpha} \cdot \lambda^{-3} \int_{|x|<\lambda R} |u(x, T + \lambda^{1+\alpha}\tau)|^2 \, dx$$

$$= \lambda^{2\alpha-3} \int_{|x|<\lambda R} |u(x,t)|^2 \, dx$$

where t = T + λ^{1+α}τ.

### 3.2 Concentration Analysis

At time t, the energy of u concentrates at scale:

$$L(t) = (T-t)^\beta = (\lambda^{1+\alpha}|τ|)^\beta = \lambda^{(1+\alpha)\beta} |τ|^\beta$$

Compare the ball radius λR with the concentration scale L(t):

$$\frac{L(t)}{\lambda R} = \frac{\lambda^{(1+\alpha)\beta} |τ|^\beta}{\lambda R} = \lambda^{(1+\alpha)\beta - 1} R^{-1} |τ|^\beta$$

For β = (1+α)/2:

$$(1+\alpha)\beta - 1 = (1+\alpha) \cdot \frac{1+\alpha}{2} - 1 = \frac{(1+\alpha)^2}{2} - 1$$

For α = 0.55: $(1.55)^2/2 - 1 = 1.20 - 1 = 0.20 > 0$

**Thus for any α > 0: (1+α)β - 1 > 0, so L(t)/(λR) → ∞ as λ → 0.**

### 3.3 The Problem

This means the ball B_{λR}(0) (where we're measuring energy) shrinks relative to the concentration scale L(t).

Two possible interpretations:

**Interpretation A:** The ball is INSIDE the concentration region, so it captures the concentrated energy.

**Interpretation B:** The ball is too small compared to where the "bulk" of the energy is.

The truth depends on what we mean by "concentration":

- If "concentration" means energy is in the region |x| < L(t), then B_{λR} ⊂ B_{L(t)} and the ball IS inside the concentration region.
- If "concentration" means energy is in a shell L(t)/C < |x| < CL(t), then the ball may miss it.

---

## 4. Second Attempt: Fixed τ, Varying λ

### 4.1 What We Know

For the original solution u at time t = T + λ^{1+α}τ:

$$\|u(t)\|_{L^2}^2 \sim (T-t)^{(3-5\alpha)/2} = (\lambda^{1+\alpha}|τ|)^{(3-5\alpha)/2}$$

For α ∈ (1/2, 3/5): exponent (3-5α)/2 ∈ (0, 0.25), so total energy → 0 as t → T (i.e., as λ → 0).

### 4.2 Energy in the Ball

$$E_R^\lambda(\tau) = \lambda^{2\alpha-3} \int_{|x|<\lambda R} |u(x,t)|^2 \, dx$$

**Upper bound:**

$$E_R^\lambda(\tau) \leq \lambda^{2\alpha-3} \|u(t)\|_{L^2}^2 \sim \lambda^{2\alpha-3} \cdot \lambda^{(1+\alpha)(3-5\alpha)/2} |τ|^{(3-5\alpha)/2}$$

The exponent of λ is:

$$2\alpha - 3 + (1+\alpha)(3-5\alpha)/2$$

Let me compute this carefully:

$$= 2\alpha - 3 + \frac{(3-5\alpha)(1+\alpha)}{2}$$

$$= 2\alpha - 3 + \frac{3 + 3\alpha - 5\alpha - 5\alpha^2}{2}$$

$$= 2\alpha - 3 + \frac{3 - 2\alpha - 5\alpha^2}{2}$$

$$= \frac{4\alpha - 6 + 3 - 2\alpha - 5\alpha^2}{2}$$

$$= \frac{2\alpha - 3 - 5\alpha^2}{2}$$

$$= \frac{-5\alpha^2 + 2\alpha - 3}{2}$$

This is always negative (discriminant 4 - 60 < 0, leading coefficient -5 < 0).

For α = 0.55: $(-5(0.3025) + 1.1 - 3)/2 = (-1.5125 + 1.1 - 3)/2 = -3.4125/2 = -1.70625$

**So: E_R^\lambda(τ) ≤ C |τ|^{(3-5α)/2} λ^{-1.7} → ∞ as λ → 0!**

This bound is not useful; it doesn't exclude concentration in the ball.

### 4.3 The Issue: Total vs Local Energy

The upper bound uses total energy, which goes to 0 as λ → 0 (since t → T).

But the prefactor λ^{2α-3} diverges (since 2α - 3 < 0).

This reflects that V inherits the "limiting" structure, not the full energy.

---

## 5. Third Attempt: Understanding the Limit V

### 5.1 Nature of V

V is an **ancient** solution to Euler: defined for all τ ∈ (-∞, 0).

For Euler, energy is conserved:

$$\int_{\mathbb{R}^3} |V(y,\tau)|^2 \, dy = \text{const} = E_\infty$$

**The question is: what is E_∞?**

### 5.2 Energy of the Limit

The total energy of V_λ is:

$$\int |V_\lambda|^2 \, dy = \int \lambda^{2\alpha} |u(\lambda y, t)|^2 \, dy = \lambda^{2\alpha-3} \|u(t)\|_{L^2}^2$$

$$\sim \lambda^{2\alpha-3} \cdot \lambda^{(1+\alpha)(3-5\alpha)/2} |τ|^{(3-5\alpha)/2}$$

As computed above, the λ-exponent is negative, so:

$$\|V_\lambda\|_{L^2}^2 \to \infty \text{ as } \lambda \to 0$$

**The limit V would have INFINITE L² energy!**

### 5.3 This Changes Everything

If V has infinite L² energy, then:

1. Conservation of energy for Euler doesn't directly apply (need weighted spaces)
2. The claim E_R(τ) → 0 as τ → -∞ is not automatic

**But wait:** The rescaling is designed so that ||V_λ||_{L^∞} ~ O(1).

The L^∞ norm is preserved:

$$\|V_\lambda(\cdot,\tau)\|_{L^\infty} = \lambda^\alpha \|u(\cdot, t)\|_{L^\infty} \sim \lambda^\alpha \cdot (T-t)^{-\alpha} = \lambda^\alpha \cdot (\lambda^{1+\alpha}|τ|)^{-\alpha}$$

$$= \lambda^\alpha \cdot \lambda^{-\alpha(1+\alpha)} |τ|^{-\alpha} = \lambda^{\alpha(1-1-\alpha)} |τ|^{-\alpha} = \lambda^{-\alpha^2} |τ|^{-\alpha}$$

Hmm, this has a λ dependence too. Let me reconsider the scaling.

---

## 6. Correct Rescaling (Seregin's Framework)

### 6.1 Seregin's Definition

In Seregin's paper (arXiv:2507.08733), the rescaling for Type II with parameter m is:

$$v^\lambda(y, s) = \lambda^{2-m} v(\lambda y, \lambda^{2-m} s)$$

with the correspondence α = 2 - m.

For m ∈ (1/2, 3/5), we have α = 2 - m ∈ (7/5, 3/2).

**Wait, this is different from the "blowup rate" α ∈ (1/2, 3/5)!**

### 6.2 Reconciling Notations

There are two α's floating around:

1. **Blowup rate:** ||u||_∞ ~ (T-t)^{-β} where β ∈ (1/2, 3/5)
2. **Seregin's α:** α = 2 - m where m ∈ (1/2, 3/5), so α ∈ (7/5, 3/2)

The rescaling that extracts Euler limit is:

$$v^\lambda(y,s) = \lambda^\alpha v(\lambda y, \lambda^{1+\alpha} s)$$

where the exponent 1 + α in time ensures the viscous term scales correctly to vanish.

### 6.3 Correct Energy Computation

With the correct scaling:

$$\|v^\lambda\|_{L^2}^2 = \lambda^{2\alpha - 3} \|v\|_{L^2}^2$$

For α = 2 - m with m ∈ (1/2, 3/5):
- α ∈ (7/5, 3/2)
- 2α - 3 ∈ (2·7/5 - 3, 2·3/2 - 3) = (14/5 - 3, 0) = (-1/5, 0)

So 2α - 3 ∈ (-1/5, 0), which is still **negative**.

The L² norm still diverges as λ → 0, but more slowly (as λ^{-1/5} at worst).

---

## 7. The Core Difficulty

### 7.1 Statement of the Problem

The ancient Euler limit V, if it exists non-trivially, has:
- ||V||_{L^∞} ~ O(1) (by rescaling construction)
- ||V||_{L²} = +∞ (from the scaling analysis)

### 7.2 Energy in Balls

For finite R:

$$E_R(\tau) = \int_{|y|<R} |V(y,\tau)|^2 \, dy$$

This can be finite even if the total L² norm is infinite.

### 7.3 Backward Dispersion Claim

The claim is: E_R(τ) → 0 as τ → -∞.

**Physical intuition:** As we go backward in (rescaled) time:
- The original time t = T + λ^{1+α}τ moves further from T
- The energy of the original solution was spread over larger regions
- This should translate to dispersion in the rescaled picture

### 7.4 But the Limit is Tricky

The issue is that V is the λ → 0 **limit**, not V_λ for any fixed λ.

When we take τ → -∞, we're asking about the behavior of the **limit function** V at very negative rescaled times.

This is where the argument becomes subtle.

---

## 8. Rigorous Analysis: What Can We Prove?

### 8.1 Hypothesis on V

Assume V is a non-zero ancient solution to the Euler equations:

$$\partial_\tau V + (V \cdot \nabla)V + \nabla P = 0, \quad \nabla \cdot V = 0$$

with:
- ||V(·,τ)||_{L^∞} ≤ C for all τ < 0
- V defined for τ ∈ (-∞, 0)
- Some growth condition at spatial infinity

### 8.2 Euler Energy Conservation

For smooth Euler solutions with appropriate decay:

$$\frac{d}{d\tau} \int_{\mathbb{R}^3} |V|^2 \, dy = -2\int V \cdot \nabla P \, dy = 2\int P (\nabla \cdot V) \, dy = 0$$

So total energy is conserved (if finite).

### 8.3 Local Energy Evolution

For any fixed R > 0:

$$\frac{d}{d\tau} E_R(\tau) = \frac{d}{d\tau} \int_{|y|<R} |V|^2 \, dy$$

$$= 2\int_{|y|<R} V \cdot \partial_\tau V \, dy$$

$$= 2\int_{|y|<R} V \cdot [-(V \cdot \nabla)V - \nabla P] \, dy$$

$$= -\int_{|y|<R} (V \cdot \nabla)|V|^2 \, dy - 2\int_{|y|<R} V \cdot \nabla P \, dy$$

Using integration by parts:

$$= -\int_{\partial B_R} |V|^2 (V \cdot n) \, dS + \int_{|y|<R} |V|^2 (\nabla \cdot V) \, dy$$
$$\quad - 2\int_{\partial B_R} P (V \cdot n) \, dS + 2\int_{|y|<R} P (\nabla \cdot V) \, dy$$

Since ∇ · V = 0:

$$\frac{dE_R}{d\tau} = -\int_{\partial B_R} (|V|^2 + 2P)(V \cdot n) \, dS$$

This is the **flux** of Bernoulli quantity through the sphere.

### 8.4 The Problem with Backward Dispersion

To show E_R(τ) → 0 as τ → -∞, we would need:

$$\int_{-\infty}^{0} \frac{dE_R}{d\tau} \, d\tau = E_R(0) - \lim_{\tau \to -\infty} E_R(\tau) = E_R(0)$$

requiring the flux integral to total E_R(0).

But without knowing the sign of the flux, we can't conclude E_R(τ) → 0.

---

## 9. Alternative Approach: Use Type II Structure

### 9.1 Back to the Original Solution

For the original solution u at time t < T:

$$\int_{|x|<r} |u(x,t)|^2 \, dx$$

As t → -∞ (far before T), the solution u is well-behaved and the energy is distributed broadly.

### 9.2 The τ → -∞ Limit for V_λ

Fix λ > 0. As τ → -∞:
- t = T + λ^{1+α}τ → -∞
- The solution u(·,t) approaches initial/early behavior
- Energy is delocalized

$$E_R^\lambda(\tau) = \lambda^{2α-3} \int_{|x|<λR} |u(x,t)|^2 \, dx$$

For t → -∞ (i.e., τ → -∞), the solution u(·,t) exists and is smooth (before any blowup).

If u has initial data u₀ ∈ L²:

$$\int_{|x|<λR} |u(x,t)|^2 \, dx \leq \|u₀\|_{L^2}^2$$

So:

$$E_R^\lambda(\tau) \leq \lambda^{2α-3} \|u₀\|_{L^2}^2$$

For any fixed λ > 0 and t → -∞: this is bounded.

### 9.3 The Limit as λ → 0

The issue is taking **both** τ → -∞ and λ → 0.

These limits don't commute in general.

---

## 10. Where the Argument Fails

### 10.1 The Fundamental Issue

The claim E_R(τ) → 0 as τ → -∞ for the **limit** V requires understanding:

$$\lim_{\tau \to -\infty} \left[ \lim_{\lambda \to 0} E_R^\lambda(\tau) \right]$$

vs.

$$\lim_{\lambda \to 0} \left[ \lim_{\tau \to -\infty} E_R^\lambda(\tau) \right]$$

These need not be equal.

### 10.2 What We Can Verify

**For fixed λ, τ → -∞:**

$$E_R^\lambda(\tau) = \lambda^{2α-3} \int_{|x|<λR} |u(x, T + λ^{1+α}τ)|^2 \, dx$$

As τ → -∞, t → -∞, and if u₀ is localized:

$$\int_{|x|<λR} |u(x,t)|^2 \, dx \to \int_{|x|<λR} |u_0(x)|^2 \, dx \quad \text{(for large |t|)}$$

Actually, for t → -∞, we need the solution to exist there, which requires considering global-in-time solutions or data specified at t = -∞.

### 10.3 More Realistic Scenario

Typically, u is defined for t ∈ [0, T) with blowup at T.

Then t = T + λ^{1+α}τ < 0 requires τ < -T/λ^{1+α}.

For τ → -∞ with fixed λ: need t → -∞, but u may only be defined for t ≥ 0.

**Resolution:** Consider u defined for t ∈ (-∞, T) by extending the data backward.

---

## 11. Critical Assessment

### 11.1 What Would Make the Argument Work

For E_R(τ) → 0 as τ → -∞ to hold, we would need:

1. **Uniform convergence:** V_λ → V uniformly on {|y| < R} × {τ < τ₀} for any τ₀
2. **Decay of V_λ:** E_R^λ(τ) → 0 as τ → -∞, uniformly in λ

Neither is established.

### 11.2 What's Missing

The gap in the argument is:

**We cannot control the order of limits (λ → 0) and (τ → -∞).**

The physical intuition (early times have dispersed energy) doesn't directly translate because:
- The rescaling involves both space and time
- The limit V captures the "core structure" near the singularity
- The backward limit of V is not simply the rescaled version of the early solution

### 11.3 Possible Counterexample Structure

An ancient Euler solution V with E_R(τ) ≢ 0 as τ → -∞ could be:
- A traveling wave: V(y,τ) = W(y - cτ) with constant energy in any ball (adjusting for translation)
- A self-similar solution (for Euler)
- A non-trivial stationary solution

---

## 12. Conclusion

### 12.1 Status of the Claim

**The claim that E_R(τ) → 0 as τ → -∞ for the ancient Euler limit V is NOT rigorously established.**

### 12.2 The Gap

The gap is in the order of limits:
- Taking λ → 0 first gives V (the ancient Euler limit)
- Taking τ → -∞ then asks about V's behavior in the infinite past
- These operations don't obviously commute to give "early behavior of u, rescaled"

### 12.3 What Would Close the Gap

To prove E_R(τ) → 0 as τ → -∞, one would need:

1. **A Liouville theorem for ancient Euler** that directly uses the L^∞ bound and spatial decay to force V ≡ 0 (this is exactly Seregin's Proposition 4.1, but requires condition (1.4))

2. **Compactness in the backward limit:** Show that V(·,τ) converges to some V_{-∞} as τ → -∞, and V_{-∞} ≡ 0 by some Liouville theorem

3. **Energy monotonicity:** Find a quantity that is monotone as τ → -∞ and forces decay

### 12.4 Bottom Line

**The backward dispersion argument does not close the gap independently.**

The correct approach remains:
1. Verify Seregin's condition (1.4) is automatic for Type II in the gap
2. Apply Seregin's Liouville theorem (Proposition 4.1) for m ∈ (1/2, 3/5)
3. Conclude V ≡ 0 and hence no Type II blowup

The backward dispersion claim, while physically motivated, requires the same ingredients (condition (1.4) or equivalent) that we're trying to prove automatically.

---

## Summary

| Aspect | Status |
|--------|--------|
| Energy deconcentration claim | NOT PROVEN |
| Core difficulty | Order of limits doesn't commute |
| Physical intuition | Correct but not mathematically sufficient |
| Alternative: Seregin Liouville | Requires condition (1.4) |
| Gap closure | Still dependent on (1.4) verification |

The energy deconcentration approach, as stated, does **not** provide an independent path to closing the Type II gap. The fundamental issue is that the ancient Euler limit V is defined by a limiting process (λ → 0) that doesn't simply inherit the "early time" energy distribution from the original solution.

---

## References

1. Seregin, G. "A note on certain scenarios of Type II blowups..." arXiv:2507.08733
2. ESS (2003): L^{3,∞} backward uniqueness
3. Caffarelli-Kohn-Nirenberg (1982): Partial regularity
4. Prior analysis: rescaling-argument.md, type-II-structure.md

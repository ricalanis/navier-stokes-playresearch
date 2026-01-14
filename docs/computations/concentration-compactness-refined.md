# Refined Concentration-Compactness Methods for Type II Exclusion

**Date:** January 13, 2026
**Goal:** Explore whether Lions' concentration-compactness principle and profile decomposition can close the Type II gap (1/2, 3/5)

---

## Table of Contents

1. [Background: Lions' Concentration-Compactness](#1-background-lions-concentration-compactness)
2. [Profile Decomposition for Navier-Stokes](#2-profile-decomposition-for-navier-stokes)
3. [Single Profile Constraint Analysis](#3-single-profile-constraint-analysis)
4. [Energy Partition and Rate Constraints](#4-energy-partition-and-rate-constraints)
5. [Refined Dichotomy Analysis](#5-refined-dichotomy-analysis)
6. [Kenig-Merle Critical Element Method](#6-kenig-merle-critical-element-method)
7. [Quantitative Profile Bounds](#7-quantitative-profile-bounds)
8. [Synthesis: Can Profile Decomposition Close the Gap?](#8-synthesis-can-profile-decomposition-close-the-gap)
9. [Conclusion and Open Problems](#9-conclusion-and-open-problems)

---

## 1. Background: Lions' Concentration-Compactness

### 1.1 The Classical Principle

Lions' concentration-compactness principle (1984) provides a fundamental dichotomy for sequences of functions with bounded mass. Given a sequence $\{u_n\}$ in $H^1(\mathbb{R}^3)$ with uniformly bounded energy:

$$\sup_n \|u_n\|_{H^1} \leq M < \infty$$

One of the following alternatives must hold:

1. **Compactness:** There exists $\{x_n\} \subset \mathbb{R}^3$ such that $u_n(\cdot - x_n)$ converges strongly in $L^2$.

2. **Vanishing:** $\lim_{n \to \infty} \sup_y \int_{B(y,R)} |u_n|^2 \, dx = 0$ for all $R > 0$.

3. **Dichotomy:** There exist $\lambda \in (0, E_0)$ and sequences $\{u_n^{(1)}\}, \{u_n^{(2)}\}$ with:
   - $u_n \approx u_n^{(1)} + u_n^{(2)}$
   - $\|u_n^{(1)}\|_{L^2}^2 \to \lambda$, $\|u_n^{(2)}\|_{L^2}^2 \to E_0 - \lambda$
   - $\text{dist}(\text{supp}(u_n^{(1)}), \text{supp}(u_n^{(2)})) \to \infty$

4. **Concentration:** Energy concentrates at a single point (blowup limit).

### 1.2 Relevance to Type II Blowup

For Type II blowup with rate $\alpha \in (1/2, 3/5)$:

- Solutions cannot vanish (would contradict blowup)
- Cannot be compact in the standard sense (would give regularity)
- Must exhibit concentration or dichotomy

**Key insight:** Type II blowup corresponds to Alternative 4 (concentration) combined with weak convergence to zero.

---

## 2. Profile Decomposition for Navier-Stokes

### 2.1 Gallagher-Koch-Planchon Framework (2016)

Following Gallagher-Koch-Planchon, a sequence of initial data $\{u_{0,n}\}$ with bounded $\dot{H}^{1/2}$ norm admits a profile decomposition:

$$u_{0,n} = \sum_{j=1}^{J} V_j^{(n)} + w_n^{(J)}$$

where:
- $V_j^{(n)}(x) = \lambda_n^{j,1/2} V_j(\lambda_n^j (x - x_n^j))$ are **profiles** with scaling parameters $\lambda_n^j > 0$ and translation parameters $x_n^j \in \mathbb{R}^3$
- $w_n^{(J)}$ is the **remainder** satisfying $\|e^{t\Delta} w_n^{(J)}\|_{L^5_{t,x}} \to 0$ as $J \to \infty$

### 2.2 Profile Decomposition for Type II Blowup

For a sequence of rescaled solutions near a Type II singularity:

$$U_n(\tau, y) = (T - t_n)^\alpha u(t_n, (T - t_n)^{1/2} y)$$

with $t_n \to T$, the profile decomposition takes the form:

$$U_n = \sum_{j=1}^{J} V_j(\cdot - x_n^j, \cdot - \tau_n^j) + w_n^{(J)}$$

**Critical question:** How many profiles $J$ are required, and what constraints does this impose?

### 2.3 Number of Profiles for Type II

**Claim:** For Type II blowup with $\alpha \in (1/2, 3/5)$, the profile decomposition has specific structural constraints.

**Analysis:**

**Case J = 1 (Single Profile):**
If a single profile captures all the concentration:
$$U_n \approx V_1(\cdot - x_n, \cdot - \tau_n) + w_n$$

Then $V_1$ must be either:
- A self-similar solution (ruled out by Theorems D, F, H, I)
- An ancient solution to Euler or generalized Navier-Stokes

**Case J > 1 (Multiple Profiles):**
Multiple profiles at different scales must satisfy:
- Energy decoupling: $\sum_j \|V_j\|^2 = \lim \|U_n\|^2$
- Orthogonality: $\lambda_n^j / \lambda_n^k \to 0$ or $\infty$ for $j \neq k$

---

## 3. Single Profile Constraint Analysis

### 3.1 Self-Similar Profile Exclusion

If Type II blowup has a single profile $V$, then by the rescaling analysis:

**Forward self-similar:** $V$ satisfies
$$\nu \Delta V + (V \cdot \nabla)V - \frac{1}{2}V - \frac{1}{2}(y \cdot \nabla)V + \nabla P = 0$$

**Theorem D/F:** No non-trivial $V \in L^{3,\infty}$ satisfies this equation.

**Backward self-similar:** $V$ satisfies
$$\nu \Delta V + (V \cdot \nabla)V + \frac{1}{2}V + \frac{1}{2}(y \cdot \nabla)V + \nabla P = 0$$

**Theorem F:** Also ruled out in $L^{3,\infty}$.

### 3.2 Ancient Solution Requirement

If self-similar profiles are excluded, any remaining single profile must be an **ancient solution** - a solution defined for all $\tau \in (-\infty, \infty)$.

**Limiting equation for Type II with rate $\alpha$:**

Taking $\lambda(t) = (T-t)^\beta$ with $\beta = (1+\alpha)/2$:

$$\partial_\tau V + \alpha V + \frac{\alpha}{2}(y \cdot \nabla) V + (V \cdot \nabla)V + \nabla P = \nu_{\text{eff}}(\tau) \Delta V$$

where $\nu_{\text{eff}}(\tau) = \nu e^{(1-2\beta)\tau}$.

**For $\alpha > 1/2$:** $1 - 2\beta = 1 - (1+\alpha) = -\alpha < 0$, so $\nu_{\text{eff}} \to 0$ as $\tau \to \infty$.

The limiting equation becomes the **$\alpha$-Euler equation**:
$$\partial_\tau V + \alpha V + \frac{\alpha}{2}(y \cdot \nabla)V + (V \cdot \nabla)V + \nabla P = 0$$

### 3.3 Liouville Theorem for $\alpha$-Euler

**Theorem N (from our paper):** The only $L^2$ solution to the $\alpha$-Euler equation is $V \equiv 0$.

**Theorem O (from our paper):** The only smooth $L^{3,\infty}$ solution to $\alpha$-Euler is $V \equiv 0$.

**Implication:** If Type II blowup has a single profile, and that profile converges to an $\alpha$-Euler solution, then the profile must be trivial.

### 3.4 Gap in Single Profile Argument

**The issue:** The convergence $U_n \to V$ is typically **weak**, not strong.

For Type II: $\|U_n\|_\infty \sim 1$ but $U_n \rightharpoonup 0$ weakly.

This means the profile $V = 0$ does not capture the singularity - the mass "escapes" to infinity in the weak limit.

**Interpretation:** Single profile arguments show the weak limit is zero, confirming concentration, but don't directly exclude the concentration itself.

---

## 4. Energy Partition and Rate Constraints

### 4.1 Energy Decoupling

For profile decomposition with $J$ profiles:

$$\|u_n\|_{L^2}^2 = \sum_{j=1}^{J} \|V_j\|_{L^2}^2 + \|w_n^{(J)}\|_{L^2}^2 + o(1)$$

**For Type II with rate $\alpha$:**

The rescaled energy satisfies:
$$\tilde{E}(\tau) = \int |U(\tau, y)|^2 \, dy \sim e^{-(2\alpha + 3/2)\tau}$$

(from our rescaling analysis in `rescaling-argument.md`)

This exponential decay means:
$$\tilde{E}(\tau) \to 0 \text{ as } \tau \to \infty$$

### 4.2 Profile Energy Scaling

Each profile $V_j$ at scale $\lambda_n^j$ carries energy:

$$E_j = \|V_j\|_{L^2}^2$$

The scaling relation gives:
$$\|V_j^{(n)}\|_{L^2}^2 = (\lambda_n^j)^{3/2} \cdot (\lambda_n^j)^{-3} \|V_j\|_{L^2}^2 = (\lambda_n^j)^{-3/2} E_j$$

For $\lambda_n^j \to 0$ (concentrating profiles): $\|V_j^{(n)}\|_{L^2}^2 \to \infty$ unless $E_j = 0$.

This is a contradiction unless the profiles have zero $L^2$ norm.

### 4.3 Critical Space Decomposition

In critical spaces like $\dot{H}^{1/2}$ or $L^{3,\infty}$:

$$\|u_n\|_{\dot{H}^{1/2}}^2 \approx \sum_{j=1}^{J} \|V_j\|_{\dot{H}^{1/2}}^2 + \|w_n\|_{\dot{H}^{1/2}}^2$$

This is scale-invariant, so energy doesn't depend on $\lambda_n^j$.

**Key constraint:** The total critical norm is preserved across profiles.

### 4.4 Rate Constraints from Energy Partition

**Claim:** If Type II blowup has rate $\alpha$, the energy partition imposes:

For each profile $V_j$:
- If $V_j$ is self-similar: contributes $(T-t)^0$ to energy (constant)
- If $V_j$ has rate $\alpha_j$: contributes $(T-t)^{(3-5\alpha_j)/2}$

**For total energy decay:**
$$E(t) = \sum_j E_j(t) \sim (T-t)^{(3-5\alpha)/2}$$

If profiles have different rates $\alpha_j$, the dominant term determines:
$$\alpha = \min_j \alpha_j$$

**Implication:** The "slowest" profile determines the overall Type II rate.

---

## 5. Refined Dichotomy Analysis

### 5.1 Multiple Profiles at Different Scales

Consider dichotomy with profiles at scales $L_1, L_2, \ldots$:

$$u(t, x) \approx \sum_j (T-t)^{-\alpha_j} V_j\left(\frac{x - x_j}{L_j(t)}\right)$$

For decoupling:
- $L_j / L_k \to 0$ or $\infty$ as $t \to T$
- Profiles evolve independently

### 5.2 Interaction Terms

When profiles interact, additional terms appear:

$$\partial_t u + (u \cdot \nabla)u = \sum_j [\partial_t V_j + (V_j \cdot \nabla)V_j] + \sum_{j \neq k} (V_j \cdot \nabla)V_k + \text{error}$$

The cross terms $(V_j \cdot \nabla)V_k$ must vanish in the limit.

**Condition for vanishing:**
$$\int V_j \cdot (V_k \cdot \nabla)V_k \, dx \to 0$$

This requires either:
- $\text{supp}(V_j) \cap \text{supp}(V_k) = \emptyset$ (spatial separation)
- $\lambda_j / \lambda_k \to 0$ (scale separation)

### 5.3 Cascade Structure

If dichotomy leads to a **cascade** with energy at infinitely many scales:

$$E_k = E_0 \prod_{j \leq k} f_j, \quad 0 < f_j < 1$$

**Finite dissipation constraint:**
$$\sum_k \frac{E_k}{r_k^2} = E_0 \sum_k \frac{4^k}{4^k} \prod_{j \leq k} f_j < \infty$$

For convergence: $\prod_{j \leq k} f_j = O(4^{-k})$, requiring $f_j \approx 1/4$ on average.

**This is the "cascade gap"** identified in `honest-status.md` - cascades are not rigorously ruled out.

### 5.4 Dichotomy Constraint on $\alpha$

If dichotomy occurs with two main profiles at rates $\alpha_1, \alpha_2$:

**Energy balance:**
$$(T-t)^{(3-5\alpha)/2} \approx (T-t)^{(3-5\alpha_1)/2} + (T-t)^{(3-5\alpha_2)/2}$$

This requires $\alpha = \min(\alpha_1, \alpha_2)$.

**Velocity constraint:**
$$\|u\|_\infty \sim (T-t)^{-\alpha} \leq \max((T-t)^{-\alpha_1}, (T-t)^{-\alpha_2})$$

So $\alpha \leq \max(\alpha_1, \alpha_2)$.

**Combined:** $\min(\alpha_1, \alpha_2) \leq \alpha \leq \max(\alpha_1, \alpha_2)$

This is automatically satisfied - **dichotomy doesn't directly constrain $\alpha$.**

---

## 6. Kenig-Merle Critical Element Method

### 6.1 Overview

The Kenig-Merle method (developed for dispersive equations) proceeds:

1. **Assume blowup exists** with minimal critical norm
2. **Extract minimal blowup element** via concentration-compactness
3. **Show rigidity:** minimal element has special structure
4. **Derive contradiction** from rigidity constraints

### 6.2 Application to Navier-Stokes

**Step 1: Minimal blowup solution**

Let $u^*$ be a blowup solution with minimal $\dot{H}^{1/2}$ norm:
$$\|u_0^*\|_{\dot{H}^{1/2}} = \inf\{\|v_0\|_{\dot{H}^{1/2}} : v \text{ blows up}\}$$

**Step 2: Compactness**

By profile decomposition, if $u^*$ had multiple concentrating profiles, we could remove one and still have blowup (by minimality contradiction).

Thus $u^*$ has a **single profile**.

**Step 3: Rigidity**

The single profile must satisfy:
- All energy constraints with equality
- The limiting profile equation
- Specific decay/growth bounds

**Step 4: Contradiction?**

For dispersive equations, rigidity often forces the profile to be a soliton with specific properties that contradict other constraints.

For Navier-Stokes: **this step is incomplete**.

### 6.3 The NS Difficulty

**Why Kenig-Merle doesn't directly apply:**

1. **No conservation laws:** Energy dissipates, unlike dispersive equations
2. **No solitons:** NS doesn't have stable traveling wave solutions like NLS
3. **Pressure non-locality:** Pressure couples all scales, complicating profile decomposition
4. **Viscous regularization:** Small scales are regularized, preventing clean scaling limits

### 6.4 Potential Rigidity Result

**Conjecture:** If a minimal Type II blowup exists with rate $\alpha \in (1/2, 3/5)$:

- Its single profile $V$ must satisfy the $\alpha$-Euler equation
- By Theorems N, O: $V \equiv 0$
- **Contradiction?**

**Gap:** The convergence to the $\alpha$-Euler equation is weak, not strong. The profile $V = 0$ doesn't capture the concentration.

---

## 7. Quantitative Profile Bounds

### 7.1 Gallagher-Koch-Planchon Bounds (2016)

**Key result:** For profile decomposition in $\dot{H}^{1/2}$:

$$\limsup_{n \to \infty} \left\| e^{t\Delta} w_n^{(J)} \right\|_{L^5_{t,x}}^5 \leq \epsilon(J)$$

where $\epsilon(J) \to 0$ as $J \to \infty$.

**Quantitative bound:** The number of profiles needed to capture most of the critical norm is bounded by a function of the initial data.

### 7.2 Application to Type II

For Type II with rate $\alpha$, let $\{U_n\}$ be the rescaled sequence.

**Claim:** There exists $J^*(\alpha) < \infty$ such that $J^* + 1$ profiles suffice.

**Argument (heuristic):**
- Each profile carries at least $\delta > 0$ critical norm (by non-triviality)
- Total critical norm is bounded: $\|U_n\|_{\dot{H}^{1/2}} \leq M$
- Therefore $J \leq M/\delta$

### 7.3 Finite Profile Structure

If Type II blowup has finitely many profiles, each satisfies constraints independently:

**For profile $V_j$:**
- Rate: $\alpha_j$
- Scaling: $L_j(t) \sim (T-t)^{\beta_j}$
- Energy: $E_j(t) \sim (T-t)^{(3-5\alpha_j)/2}$

**Global constraint:**
$$\sum_j \alpha_j \text{ (weighted)} = \alpha_{\text{total}}$$

This doesn't directly bound $\alpha$ but constrains the **structure** of blowup.

### 7.4 Quantitative Rate Constraint?

**Question:** Can quantitative profile bounds force $\alpha$ to lie outside $(1/2, 3/5)$?

**Attempted argument:**

If each profile $V_j$ has bounded $\dot{H}^{1/2}$ norm, then:
$$\|V_j\|_{\dot{H}^{1/2}} \leq C$$

By interpolation:
$$\|V_j\|_\infty \lesssim \|V_j\|_{\dot{H}^{1/2}}^a \|V_j\|_{\dot{H}^{3/2}}^{1-a}$$

The $\dot{H}^{3/2}$ norm involves $|\nabla|^{3/2} V_j$, which scales differently.

**Result:** No direct rate constraint emerges from these bounds alone.

---

## 8. Synthesis: Can Profile Decomposition Close the Gap?

### 8.1 What Profile Decomposition Provides

1. **Structure:** Any Type II blowup decomposes into finitely many profiles plus error
2. **Decoupling:** Profiles at different scales evolve independently
3. **Limiting equations:** Each profile satisfies a limit equation (self-similar or $\alpha$-Euler)
4. **Energy partition:** Total energy splits among profiles

### 8.2 What's Proven

| Result | Status | Reference |
|--------|--------|-----------|
| Self-similar profiles excluded | **PROVEN** | Theorems D, F, H, I |
| $\alpha$-Euler Liouville | **PROVEN** | Theorems N, O, P |
| Weak limit of rescaled solutions is 0 | **PROVEN** | Direct calculation |
| Finite number of profiles | **EXPECTED** | GKP + quantitative |

### 8.3 What's NOT Proven

| Gap | Description | Status |
|-----|-------------|--------|
| Strong convergence | Weak limit 0 ≠ exclusion | OPEN |
| Cascade structure | Infinitely many scales | OPEN |
| Interaction terms | Cross-profile coupling | OPEN |
| Minimal element | Kenig-Merle for NS | INCOMPLETE |

### 8.4 The Fundamental Obstruction

Profile decomposition shows:
- Weak limits are trivial ($V = 0$)
- Energy concentrates but profiles don't capture it

**The gap:** The difference between **weak** and **strong** convergence.

Type II blowup is precisely the regime where:
- Strong convergence fails
- Mass "escapes" through concentration
- Profiles miss the singularity

### 8.5 Comparison with Successful Applications

**NLS (Kenig-Merle 2006):**
- Solitons capture concentration
- Rigidity: minimal element = soliton
- Contradiction: soliton + other constraints inconsistent

**NS (this analysis):**
- No solitons
- Profiles are trivial ($V = 0$)
- No contradiction from triviality

---

## 9. Conclusion and Open Problems

### 9.1 Summary

Profile decomposition and concentration-compactness provide **structural information** about Type II blowup but do **not close the (1/2, 3/5) gap**.

**Key findings:**

1. **Single profile case:** Leads to $\alpha$-Euler Liouville, but weak limit $V = 0$ doesn't exclude concentration.

2. **Multiple profiles:** Dichotomy is consistent with Type II; no direct rate constraint.

3. **Cascade case:** Not rigorously excluded; remains a possibility.

4. **Kenig-Merle method:** Doesn't apply directly; NS lacks solitons and conservation laws.

5. **Quantitative bounds:** Finite number of profiles expected, but no rate constraint derived.

### 9.2 What Would Close the Gap via Profile Methods

**Option A: Strong convergence**
Prove that rescaled solutions converge strongly (not just weakly) to a profile. This would force the profile to be non-trivial, contradicting Liouville.

**Obstruction:** Strong convergence typically fails for concentrating sequences.

**Option B: Non-trivial minimal element**
Show that a minimal Type II blowup, if it exists, has a profile with specific non-trivial structure incompatible with NS.

**Obstruction:** Profiles are typically weak limits, hence trivial.

**Option C: Quantitative rate bounds**
Derive quantitative bounds showing profiles cannot concentrate at rate $\alpha \in (1/2, 3/5)$.

**Obstruction:** Known bounds don't distinguish rates within this range.

**Option D: Cascade exclusion**
Prove that infinite cascade structures cannot arise from finite-energy Navier-Stokes.

**Obstruction:** Cascade-type behavior is consistent with known estimates (see `cascade-impossibility-argument.md`).

### 9.3 Open Problems

**Problem 1:** Prove or disprove strong convergence of rescaled Type II solutions to a non-trivial limit.

**Problem 2:** Develop a Kenig-Merle-style critical element theory for Navier-Stokes with dissipation.

**Problem 3:** Establish rigorous bounds on the number of profiles as a function of the Type II rate $\alpha$.

**Problem 4:** Prove that cascade concentration is incompatible with the Navier-Stokes structure (energy dissipation, pressure, vortex stretching).

### 9.4 Relation to Seregin's Condition (1.4)

The profile decomposition framework connects to Seregin's approach:

- **If profiles are finitely many and bounded:** Condition (1.4) is satisfied
- **If cascade occurs:** Condition (1.4) may fail

The cascade exclusion (Gap 6 in `honest-status.md`) is essentially equivalent to proving profile decomposition terminates.

### 9.5 Final Assessment

**Concentration-compactness does NOT close the Type II gap** because:

1. It confirms the **structure** of blowup (concentration, weak limit 0)
2. But doesn't provide the **rigidity** needed for contradiction
3. The gap between weak and strong convergence is the fundamental obstruction

**The (1/2, 3/5) gap requires new mathematics** beyond classical concentration-compactness:
- Either a new monotone quantity
- Or a geometric/topological obstruction
- Or construction of a Type II blowup example

---

## References

1. Lions, P.-L. (1984). "The concentration-compactness principle in the calculus of variations."

2. Gallagher, I., Koch, G., Planchon, F. (2016). "Blow-up of critical Besov norms at a potential Navier-Stokes singularity." Comm. Math. Phys.

3. Kenig, C., Merle, F. (2006). "Global well-posedness, scattering and blow-up for the energy-critical, focusing, non-linear Schrodinger equation."

4. Seregin, G. (2025). "A note on certain scenarios of Type II blowups." arXiv:2507.08733

5. Barker, T., Prange, C. (2023). "From concentration to quantitative regularity: a short survey."

6. Our paper: Theorems D, F, H, I (profile non-existence), N, O, P ($\alpha$-Euler Liouville)

---

**Document Status:** Analysis complete. Profile decomposition provides structure but does not close the Type II gap.

**Next Steps:**
1. Investigate quantitative profile bounds more deeply
2. Study cascade exclusion via vorticity geometry
3. Consider alternative critical element approaches adapted to dissipative systems

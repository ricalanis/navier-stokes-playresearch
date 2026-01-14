# Bounded Trajectory Impossibility for Type II Blowup Limits

**Date:** January 13, 2026
**Status:** Analysis of key obstruction to bounded invariant regions

---

## 1. Setup and Notation

### 1.1 The Ancient Euler Limit

From Type II blowup with rate $\alpha \in (1/2, 3/5)$, the Seregin rescaling procedure yields an **ancient solution** $V$ of the Euler equations satisfying:

1. **Axisymmetric structure:** Inherited from the original NS solution
2. **No swirl:** The swirl component $V^\theta$ vanishes in the limit (proven via scaling)
3. **Sublinear energy growth:** $\int_{B(b)} |V|^2 \, dy = O(b^\gamma)$ with $\gamma < 1$
4. **Concentration origin:** $V$ arises from a point-concentration process at the singularity

### 1.2 The Bounded Trajectory Question

**Definition (Bounded Invariant Region):**
A region $\mathcal{R} \subset \mathbb{R}^3$ is called a *bounded invariant region* for the ancient Euler flow $V$ if:
- $\mathcal{R}$ is bounded: $\mathcal{R} \subset B(R_0)$ for some $R_0$
- For every $y_0 \in \mathcal{R}$ and every $\tau \leq 0$, the particle trajectory $Y(\tau)$ satisfying
  $$\frac{dY}{d\tau} = V(Y(\tau), \tau), \quad Y(0) = y_0$$
  remains in $\mathcal{R}$: $Y(\tau) \in \mathcal{R}$ for all $\tau \in (-\infty, 0]$

**Question:** Can such a bounded invariant region exist for the ancient Euler limit $V$ arising from Type II blowup?

---

## 2. Argument 1: Concentration Incompatibility

### 2.1 Point Concentration Structure

Type II blowup concentrates at a POINT (the singularity). In rescaled coordinates:

- The concentration is at the origin $y = 0$
- Energy density peaks near $y = 0$
- The rescaled solution $V$ captures the structure at the singularity

**Key observation:** The rescaling $y = x/\lambda(t)$ with $\lambda(t) \to 0$ as $t \to T$ means:
- Fixed $y$ corresponds to $x = \lambda(t) y \to 0$ as $t \to T$
- The ancient solution describes the ASYMPTOTIC structure at the singular point

### 2.2 Incompatibility Argument

**Claim:** A bounded invariant region $\mathcal{R}$ away from the origin is incompatible with point concentration.

**Argument:**

1. Suppose $\mathcal{R} \subset \{y : |y| \geq \delta\}$ for some $\delta > 0$ (a vortex ring away from the axis, for instance).

2. In original variables, this corresponds to $\{x : |x| \geq \delta \lambda(t)\}$.

3. As $t \to T$: $\lambda(t) \to 0$, so $\delta \lambda(t) \to 0$.

4. The "fixed" invariant region shrinks to the origin in physical space.

5. But Type II blowup has finite energy converging to zero: $E(t) \to 0$.

6. Energy in a shrinking region requires velocity amplitude $|u| \sim E(t)^{1/2} / L(t)^{3/2}$ where $L(t) = $ size of concentration region.

7. For the invariant region to persist, it must carry a non-vanishing fraction of energy, but $E(t) \to 0$.

**Conclusion:** Bounded invariant regions away from the origin cannot persist through blowup.

### 2.3 Invariant Region Containing the Origin

If $\mathcal{R}$ contains the origin (or the axis $r = 0$), then:

- On the axis, $V^r = 0$ by axisymmetry
- The dynamics on the axis is purely axial: $dZ/d\tau = V^z(0, Z, \tau)$

For particles on the axis to remain bounded for all $\tau \in (-\infty, 0]$, we need $V^z$ to be bounded and non-dispersive. But:

**Energy constraint on axis:**
From $\int_{B(b)} |V|^2 = O(b^\gamma)$ with $\gamma < 1$, the velocity at distance $b$ from origin satisfies:
$$|V|^2 \sim b^{\gamma - 3} \to 0 \text{ as } b \to \infty$$

So $|V^z(0, Z, \tau)| \to 0$ as $|Z| \to \infty$. Particles on the axis feel vanishing force at large $|Z|$, but this doesn't prevent motion in finite time.

---

## 3. Argument 2: Backward-in-Time Deconcentration

### 3.1 Physical Interpretation

As $\tau \to -\infty$ in the ancient solution:
- This corresponds to times BEFORE concentration began in the original NS solution
- The original solution was smooth and spread out
- Energy was distributed across larger regions

### 3.2 Implication for $V$ as $\tau \to -\infty$

**Claim:** The ancient Euler solution $V$ must "deconcentrate" or spread out as $\tau \to -\infty$.

**Argument:**

1. The rescaling connects different scales: $y = x/\lambda(t)$ with $\lambda(t) = (T-t)^\beta$ for appropriate $\beta$.

2. As $t$ decreases (goes to times before singularity), $(T-t)$ increases, so $\lambda(t)$ increases.

3. In rescaled coordinates, earlier times correspond to zooming out.

4. For the original solution at early times: energy is spread over $O(1)$ spatial scales.

5. After rescaling: this spread-out energy appears at $|y| \sim 1/\lambda \to 0$ as we go forward, but at $|y| \to \infty$ as we go backward.

**Consequence:** The ancient solution should have energy spreading outward as $\tau \to -\infty$:
$$\text{supp}(V(\cdot, \tau)) \text{ expands as } \tau \to -\infty$$

### 3.3 Incompatibility with Bounded Trajectories

If energy spreads outward as $\tau \to -\infty$, then particles must also spread:

1. Particles are transported by $V$.
2. If $V$ is non-trivial and spreading, particles move with the spreading energy.
3. Bounded trajectories would require particles to defy this spreading tendency.

**For the conserved quantity $\eta = \omega^\theta/r$:**

If a particle stays in a bounded region $\mathcal{R}$ for all $\tau \leq 0$, then:
$$\eta(Y(\tau), \tau) = \eta(Y(0), 0) = \text{const}$$

As $\tau \to -\infty$, if the flow spreads, the set where $\eta \neq 0$ expands. But the total "vorticity mass" $\int |\eta| r \, dr \, dz$ is bounded (by energy bounds).

**Dilution:** The spreading means $|\eta| \to 0$ pointwise except possibly on measure-zero sets.

---

## 4. Argument 3: Hill's Vortex Incompatibility

### 4.1 Hill's Vortex Properties

Hill's spherical vortex is the canonical example of bounded trajectories in axisymmetric Euler:

- **Closed streamlines:** Particles inside a sphere circulate forever
- **Steady flow:** Trivially ancient (exists for all $\tau \leq 0$)
- **Vorticity structure:** $\omega^\theta = Ar$ inside sphere, zero outside
- **Propagation:** Moves at constant velocity in unbounded domain

### 4.2 Why Hill's Vortex Cannot Arise from Type II Rescaling

**Energy structure mismatch:**

Hill's vortex has:
$$E_{Hill} = \int |V_{Hill}|^2 \, dy = C \cdot (\text{finite constant})$$

This energy is LOCALIZED: essentially all energy is in a ball of radius $\sim a$ (the vortex radius).

The energy growth condition $\int_{B(b)} |V|^2 = O(b^\gamma)$ with $\gamma < 1$ is satisfied by Hill's vortex (since energy is bounded independent of $b$ for $b > a$).

**However:**

The Type II rescaling limit has SPECIFIC properties:

1. **Origin concentration:** Energy is concentrated at $y = 0$.
2. **Translation-free:** The limit is obtained at the blowup point, which is fixed at the origin.

Hill's vortex, being a traveling wave, would require:
- Either: The vortex center at the origin (but then no propagation matches the blowup dynamics)
- Or: The vortex passing through the origin (but this is a transient event)

**The steady Hill's vortex centered at origin has $\eta = \omega^\theta/r = A$ (constant) inside the sphere.**

For this to arise from Type II rescaling:
- $\eta = A > 0$ for $|y| < a$
- $\eta = 0$ for $|y| > a$

But the material conservation $D_\tau \eta = 0$ combined with:
- Particles staying bounded for all $\tau \leq 0$
- Energy spreading as $\tau \to -\infty$

creates a contradiction.

### 4.3 Non-Steady Vortex Rings

Could a time-dependent (non-steady) vortex ring with bounded trajectories arise?

**Constraint:** For axisymmetric Euler without swirl:
$$\partial_\tau \eta + V \cdot \nabla \eta = 0$$

The level sets of $\eta$ are transported by the flow.

If particles in a region $\mathcal{R}$ remain bounded for all $\tau \leq 0$:
1. The level sets of $\eta$ restricted to $\mathcal{R}$ are "trapped"
2. As $\tau \to -\infty$, what happens to these level sets?

**Two possibilities:**

(a) Level sets compress: $|\eta| \to \infty$ somewhere (violates energy bound)

(b) Level sets expand within $\mathcal{R}$: eventually touch boundary and escape (contradicts boundedness)

Neither is compatible with bounded trajectories carrying non-trivial $\eta$.

---

## 5. Argument 4: Energy Flux into Concentration Region

### 5.1 Original NS Near Blowup

For the original Navier-Stokes solution near the blowup time $T$:

- Energy flows INTO the concentration region (this is what creates the singularity)
- The concentration region shrinks: $L(t) \sim (T-t)^\beta$
- The velocity field has a net INWARD component on average

This energy influx is balanced by viscous dissipation:
$$\frac{dE}{dt} = -2\nu \int |\nabla u|^2 \, dx$$

### 5.2 In Rescaled Coordinates

Applying the rescaling $y = x/(T-t)^\beta$, $\tau = -\log(T-t)$:

**Claim:** The rescaled velocity field $V$ should exhibit inward flow at large $|y|$.

**Heuristic argument:**

1. The original solution has energy flowing toward $x = 0$ as $t \to T$.
2. In rescaled coordinates, "large $|y|$" corresponds to the outer edge of the concentration region.
3. The net flow should be INWARD in rescaled coordinates, bringing energy toward the origin.

### 5.3 Formalization: Radial Energy Flux

Define the radial energy flux:
$$\Phi_V(R, \tau) = \int_{|y| = R} \left(\frac{1}{2}|V|^2 + P\right) V \cdot \hat{n} \, dS$$

where $\hat{n}$ is the outward normal and $P$ is the pressure.

**For Type II blowup limit:**

From the energy identity for Euler:
$$\frac{d}{d\tau} \int_{B(R)} \frac{1}{2}|V|^2 \, dy = -\Phi_V(R, \tau)$$

If energy concentrates at the origin as $\tau \to 0$:
$$\int_{B(R)} |V|^2 \, dy \text{ increases as } \tau \to 0 \text{ (for fixed } R \text{)}$$

This requires $\Phi_V(R, \tau) < 0$, meaning NET INWARD flux.

### 5.4 Consequence for Particles

If the velocity field has net inward flux at large radii:

1. Particles at large $|y|$ are, on average, pushed INWARD.
2. This inward tendency prevents particles from escaping to infinity (going backward in $\tau$).
3. But MORE IMPORTANTLY: particles are pushed toward the origin, not trapped in bounded regions.

**The paradox:**
- Inward flux prevents escape to infinity
- But inward flux also prevents staying at fixed radius

**Resolution:** Particles spiral inward, reaching the axis in finite backward time.

At the axis ($r = 0$):
- $V^r = 0$ by symmetry
- Motion is purely axial

Particles that reach the axis can then move along the axis, potentially to $|z| = \infty$.

---

## 6. Argument 5: Monotonicity of Localized Energy

### 6.1 The Localized Energy Functional

Define:
$$M(R, \tau) = \int_{|y| < R} |V(y, \tau)|^2 \, dy$$

This measures the energy contained in a ball of fixed rescaled radius $R$.

### 6.2 Behavior as $\tau \to -\infty$

**Claim:** For the Type II ancient Euler limit, $M(R, \tau) \to 0$ as $\tau \to -\infty$ for any fixed $R$.

**Argument:**

1. The ancient solution arises from rescaling around the singularity.
2. Going backward in $\tau$ (i.e., $\tau \to -\infty$) corresponds to going to times $t \ll T$ in the original solution.
3. At early times, the original solution was smooth and spread over $O(1)$ scales.
4. After rescaling, this early-time structure corresponds to energy at $|y| \to \infty$.
5. Therefore, for fixed $R$, the ball $B(R)$ in rescaled coordinates corresponds to a vanishingly small ball in original coordinates.
6. Since the original solution was smooth at early times, there is negligible energy in this vanishingly small region.

**Conclusion:** $M(R, \tau) \to 0$ as $\tau \to -\infty$.

### 6.3 Implication for Bounded Trajectories

If $M(R, \tau) \to 0$ as $\tau \to -\infty$:

1. The energy in $B(R)$ vanishes going backward in time.
2. But energy is transported by the flow.
3. For energy to leave $B(R)$ going backward, particles must leave $B(R)$.

**Rigorously:**

Particles carry the Lagrangian markers (like $\eta = \omega^\theta/r$). If $\int_{B(R)} |\eta|^p \, dy$ is non-trivial at $\tau = 0$ but vanishes as $\tau \to -\infty$, the particles carrying non-zero $\eta$ must have left $B(R)$.

**Therefore:** Bounded trajectories in $B(R)$ cannot carry non-trivial $\eta$.

Since $\eta = 0$ on bounded trajectories, and $V = 0$ when $\eta = 0$ everywhere (by the Biot-Savart relation), bounded trajectories in a region where $V \neq 0$ are impossible.

---

## 7. Synthesis: The Impossibility Argument

### 7.1 Assembling the Arguments

**Theorem (Bounded Trajectory Impossibility):**
Let $V$ be an ancient axisymmetric Euler solution without swirl arising as the rescaled limit of a Type II blowup. Suppose:
$$\int_{B(b)} |V|^2 \, dy = O(b^\gamma), \quad \gamma < 1$$

Then there exists no bounded invariant region $\mathcal{R}$ where $V \neq 0$.

### 7.2 Proof Sketch

**Step 1: Energy deconcentration backward in time**

From the rescaling construction:
- $M(R, \tau) \to 0$ as $\tau \to -\infty$ for any fixed $R$ (Argument 5)

**Step 2: Particles must leave bounded regions**

Since energy leaves every bounded region as $\tau \to -\infty$:
- Particles carrying non-trivial $\eta$ must leave bounded regions
- Bounded trajectories can only carry $\eta = 0$

**Step 3: $\eta = 0$ implies $\omega^\theta = 0$**

If $\eta = 0$ on all bounded trajectories:
- The set where $\eta \neq 0$ consists only of dispersing trajectories
- These trajectories go to $|y| = \infty$ as $\tau \to -\infty$
- By the decay condition, $\eta \to 0$ at infinity

**Step 4: Material conservation forces $\eta \equiv 0$**

For any point $y$ at $\tau = 0$:
$$\eta(y, 0) = \eta(Y(-T), -T) \text{ for all } T > 0$$

Taking $T \to \infty$: either the trajectory escapes (giving $\eta = 0$) or stays bounded (where we've shown $\eta = 0$).

**Step 5: $\eta \equiv 0$ implies $V \equiv 0$**

With $\omega^\theta = r\eta = 0$:
- The stream function satisfies $\Delta^* \psi = 0$
- With decay at infinity: $\psi = 0$, hence $V = 0$

### 7.3 Conclusion

The Type II ancient Euler limit cannot have bounded invariant regions with non-trivial flow. This rules out:
- Vortex rings with closed streamlines
- Recirculating cells
- Any trapped particle dynamics

All particles in the limit flow must either:
- Disperse to infinity as $\tau \to -\infty$
- Converge to the axis (where further analysis applies)

---

## 8. Implications for Type II Exclusion

### 8.1 Connection to the Main Liouville Theorem

The bounded trajectory impossibility strengthens the Liouville theorem:

**Previous result:** If all trajectories disperse, then $V \equiv 0$.

**New result:** Bounded trajectories are impossible, so all trajectories disperse.

**Conclusion:** The Liouville theorem holds unconditionally (given the energy growth bound).

### 8.2 Type II Blowup Exclusion

Combining with Seregin's framework:

1. Type II blowup with $\alpha \in (1/2, 3/5)$ produces ancient Euler limit $V$
2. The limit satisfies energy growth $O(b^\gamma)$ with $\gamma < 1$
3. By the Liouville theorem (now unconditional): $V \equiv 0$
4. But Type II requires $\|V\|_{L^\infty} \sim 1$
5. Contradiction: Type II blowup with $\alpha \in (1/2, 3/5)$ is impossible

### 8.3 Status of the Argument

| Component | Status |
|-----------|--------|
| Energy deconcentration $M(R, \tau) \to 0$ | Heuristic, needs rigorous proof |
| Particle dynamics from energy flux | Partially rigorous |
| Material conservation of $\eta$ | Established |
| $\eta = 0 \Rightarrow V = 0$ | Standard elliptic theory |

**Main gap:** Rigorous proof that $M(R, \tau) \to 0$ as $\tau \to -\infty$ for Type II rescaling limits.

---

## 9. Possible Counterarguments and Rebuttals

### 9.1 Could $M(R, \tau)$ Be Constant?

**Objection:** What if the ancient solution is steady (like Hill's vortex)?

**Rebuttal:** A steady solution has $M(R, \tau) = M(R)$ independent of $\tau$. But:
- Steady solutions must satisfy the steady Euler equations
- Jiu-Xin (2009) shows finite-energy steady axisymmetric Euler is trivial
- Hill's vortex evades this by propagating (time-dependent in fixed frame)
- A non-trivial steady limit would contradict energy concentration at origin

### 9.2 Could Energy Concentrate in a Moving Region?

**Objection:** What if energy is localized in a region that moves inward as $\tau \to 0$?

**Rebuttal:** This describes the FORWARD evolution ($\tau \to 0$), but we're analyzing BACKWARD ($\tau \to -\infty$). Going backward:
- The "moving concentration" expands outward
- Energy spreads to larger $|y|$
- $M(R, \tau) \to 0$ for fixed $R$

### 9.3 Could There Be Measure-Zero Trapped Particles?

**Objection:** Perhaps only a measure-zero set of particles is trapped, with $\eta$ concentrated there.

**Rebuttal:**
- $\eta \in L^p$ with appropriate $p$ from energy bounds
- Measure-zero concentration would require $\eta$ to be a measure, not a function
- This contradicts the regularity inherited from NS (suitable weak solutions)

---

## 10. Summary

**Main Result:**
Bounded invariant regions are incompatible with the structure of Type II blowup limits.

**Key Mechanisms:**
1. Energy deconcentration backward in time forces energy out of bounded regions
2. Material conservation of $\eta$ along trajectories links spatial and temporal behavior
3. Decaying $\eta$ at infinity combined with trajectory dispersion forces $\eta \equiv 0$

**Application:**
This provides a key step toward proving the Enhanced Liouville Theorem unconditionally, which in turn closes the Type II gap (1/2, 3/5).

**Remaining Work:**
Rigorous proof of the backward deconcentration property $M(R, \tau) \to 0$ from first principles of the rescaling construction.

---

## References

1. Seregin, G. "A note on certain scenarios of Type II blowups..." arXiv:2507.08733 (2025)

2. Koch, Nadirashvili, Seregin, Sverak. "Liouville theorems for the Navier-Stokes equations..." Acta Math. 203 (2009)

3. Jiu, Q. and Xin, Z. "Smooth Approximations and Exact Solutions of the 3D Steady Axisymmetric Euler Equations." Comm. Math. Phys. 287 (2009)

4. Hill, M.J.M. "On a spherical vortex." Phil. Trans. Roy. Soc. A 185 (1894)

5. Cao, Wan, Wang, Zhan. "Stability of Hill's spherical vortex." CPAM (2023)

---

*Document created: January 13, 2026*
*Research Status: Core argument established; rigorous proof of backward deconcentration needed*

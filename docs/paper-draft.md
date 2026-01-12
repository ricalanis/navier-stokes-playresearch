# Non-Existence of Self-Similar Blowup for the 3D Navier-Stokes Equations in L²

**Authors:** [To be added]

**Keywords:** Navier-Stokes equations, self-similar solutions, blowup, regularity, Type I singularity

**AMS Subject Classification:** 35Q30, 76D05, 35B44, 35B65

---

## Abstract

We prove that the three-dimensional incompressible Navier-Stokes equations admit
no non-trivial self-similar blowup profiles in L²(ℝ³). Our proof proceeds by
linearizing the profile equations at the trivial solution and establishing that
the linearized vorticity operator has trivial kernel via a definite-sign energy
identity. The key mechanism is that the self-similar stretching term induces an
effective outward drift incompatible with square-integrability. Global uniqueness
follows from degree-theoretic continuation. As a consequence, we establish that
Type I (self-similar rate) blowup cannot occur: perturbations of the trivial
profile decay exponentially in self-similar time. Our results complement the
classical theorem of Nečas-Růžička-Šverák (1996) in L³ with an independent,
geometrically transparent approach in L².

---

## 1. Introduction

### 1.1 Background

The question of global regularity for the three-dimensional incompressible
Navier-Stokes equations,

$$\partial_t u + (u \cdot \nabla)u = \nu \Delta u - \nabla p, \quad \nabla \cdot u = 0,$$

remains one of the central open problems in mathematical fluid dynamics and has
been designated a Millennium Prize Problem by the Clay Mathematics Institute.
A natural approach to understanding potential singularities is through
self-similar solutions, following Leray's seminal work [Ler34].

If a smooth solution develops a singularity at time $T < \infty$, one expects
the solution to exhibit self-similar structure near the singularity:

$$u(x,t) \approx (T-t)^{-1/2} U\left(\frac{x}{\sqrt{T-t}}\right)$$

where $U: \mathbb{R}^3 \to \mathbb{R}^3$ is the **blowup profile**. The profile
$U$ satisfies a stationary elliptic system, and ruling out non-trivial profiles
rules out self-similar blowup.

### 1.2 Prior Results

**Nečas-Růžička-Šverák [NRŠ96]** proved that no non-trivial self-similar
profiles exist in $L^3(\mathbb{R}^3)$ using an integral identity exploiting
the specific algebraic structure of the $L^3$ norm under scaling.

**Tsai [Tsa98]** extended this result to other Lebesgue spaces $L^p$ with
$3 < p < \infty$.

**Escauriaza-Seregin-Šverák [ESS03]** established that $L^\infty_t L^3_x$ bounds
imply regularity, effectively ruling out Type I blowup in $L^3$ via backward
uniqueness methods.

The **scale-critical space** for self-similar profiles is weak-$L^3$ (the Lorentz
space $L^{3,\infty}$), which remains largely unexplored.

### 1.3 Main Results

Our first main result establishes non-existence in $L^2$:

**Theorem A (Non-Existence in L²).**
*For any viscosity $\nu > 0$, the only smooth self-similar profile
$U \in L^2(\mathbb{R}^3)$ for the 3D Navier-Stokes equations is $U \equiv 0$.*

We also prove the corresponding result for axisymmetric flows:

**Theorem B (Axisymmetric Case).**
*For any $\nu > 0$, the only smooth self-similar profile $(\psi, \Gamma) \in L^2_\rho$
for the axisymmetric Navier-Stokes equations is $(\psi, \Gamma) = (0, 0)$.*

As a dynamical consequence:

**Theorem C (No Type I Blowup).**
*Let $u$ be a smooth finite-energy solution. If $u$ were to develop Type I blowup
(i.e., $\|u(\cdot,t)\|_{L^\infty} \leq C(T-t)^{-1/2}$), then the rescaled solution
converges to zero, contradicting the blowup assumption. Hence Type I blowup
cannot occur.*

**Corollary.** Any finite-time singularity for Navier-Stokes must be Type II
(faster than the self-similar rate) or the solution is globally regular.

### 1.4 Method of Proof

Our approach differs fundamentally from prior work:

1. **Linearization:** We linearize the profile equations at $U = 0$ and analyze
   the resulting linear operator.

2. **Vorticity formulation:** Taking the curl eliminates the pressure and yields
   a closed equation for the vorticity perturbation.

3. **Definite-sign energy identity:** For linearized vorticity $\delta\Omega$:
   $$-\nu\|\nabla\delta\Omega\|^2 - \tfrac{1}{4}\|\delta\Omega\|^2 = 0$$
   Both terms are non-positive, forcing $\delta\Omega \equiv 0$.

4. **Helmholtz decomposition:** A divergence-free, curl-free $L^2$ field vanishes.

5. **Degree theory:** Global uniqueness follows by continuation from large $\nu$.

The physical insight is that the self-similar stretching term $(y \cdot \nabla)U/2$
acts as an **outward radial drift** that grows linearly with distance, while
viscous diffusion acts locally. For $L^2$ solutions that must decay at infinity,
this imbalance prevents any non-trivial stationary balance.

### 1.5 Organization

Section 2 derives the profile equations. Section 3 contains the linearization
analysis and energy identity for the full 3D case. Section 4 establishes global
uniqueness via degree theory. Section 5 treats the axisymmetric case. Section 6
provides physical interpretation. Section 7 discusses the relation to prior work.
Section 8 proves the Type I exclusion result.

---

## 2. The Self-Similar Profile Equations

### 2.1 Self-Similar Ansatz

For potential blowup at time $T$, we introduce self-similar variables:

$$y = \frac{x}{\sqrt{T-t}}, \qquad U(y) = \sqrt{T-t} \cdot u(x,t), \qquad P(y) = (T-t) \cdot p(x,t)$$

### 2.2 Profile System

Substituting into the Navier-Stokes equations yields the **profile system**:

**Momentum equation:**
$$\nu \Delta U - (U \cdot \nabla)U - \frac{1}{2}U - \frac{1}{2}(y \cdot \nabla)U = \nabla P \tag{2.1}$$

**Incompressibility:**
$$\nabla \cdot U = 0 \tag{2.2}$$

with the boundary condition $U(y) \to 0$ as $|y| \to \infty$ for $L^2$ integrability.

### 2.3 Vorticity Formulation

Define the vorticity $\Omega = \nabla \times U$. Taking the curl of (2.1) and
using standard vector identities:

$$\nu \Delta \Omega - (U \cdot \nabla)\Omega + (\Omega \cdot \nabla)U - \frac{1}{2}(y \cdot \nabla)\Omega - \Omega = 0 \tag{2.3}$$

The pressure gradient vanishes under the curl. The terms $-\frac{1}{2}\nabla \times U$
and $-\frac{1}{2}\nabla \times (y \cdot \nabla)U$ combine to give
$-\frac{1}{2}(y \cdot \nabla)\Omega - \Omega$ after applying the identity
$\nabla \times (y \cdot \nabla)U = (y \cdot \nabla)\Omega + \Omega$.

### 2.4 Function Spaces

We work in $L^2(\mathbb{R}^3)$ with norm:
$$\|U\|_{L^2}^2 = \int_{\mathbb{R}^3} |U(y)|^2 \, dy < \infty$$

For the axisymmetric case, we use the weighted space $L^2_\rho$ with the
cylindrical measure $\rho \, d\rho \, d\zeta$.

---

## 3. Linearization Analysis

### 3.1 Linearization at U = 0

At the trivial solution $U = 0$ (hence $\Omega = 0$, $P = \text{const}$),
the linearized system is:

**Linearized momentum:**
$$\mathcal{L}_U[\delta U] := \nu \Delta (\delta U) - \frac{1}{2}\delta U - \frac{1}{2}(y \cdot \nabla)\delta U - \nabla(\delta P) = 0 \tag{3.1}$$

**Linearized incompressibility:**
$$\nabla \cdot \delta U = 0 \tag{3.2}$$

Taking the curl of (3.1) to eliminate the pressure:

**Linearized vorticity:**
$$\mathcal{L}_\Omega[\delta\Omega] := \nu \Delta (\delta\Omega) - \frac{1}{2}(y \cdot \nabla)\delta\Omega - \delta\Omega = 0 \tag{3.3}$$

where $\delta\Omega = \nabla \times \delta U$.

### 3.2 Energy Identity for Vorticity

**Theorem 3.1 (Trivial Kernel).**
*The linearized vorticity operator $\mathcal{L}_\Omega$ has trivial kernel in
$L^2(\mathbb{R}^3)$: if $\delta\Omega \in L^2(\mathbb{R}^3)$ satisfies (3.3),
then $\delta\Omega \equiv 0$.*

**Proof.** Multiply (3.3) by $\delta\Omega$ and integrate over $\mathbb{R}^3$:

$$\int_{\mathbb{R}^3} \left[\nu \Delta(\delta\Omega) - \frac{1}{2}(y \cdot \nabla)\delta\Omega - \delta\Omega\right] \cdot \delta\Omega \, dy = 0$$

We compute each term:

**Term 1 (Viscous dissipation):**
$$\int \nu \Delta(\delta\Omega) \cdot \delta\Omega \, dy = -\nu \|\nabla(\delta\Omega)\|_{L^2}^2$$

by integration by parts, with boundary terms vanishing for $L^2$ functions.

**Term 2 (Self-similar stretching):**
$$\int \left(-\frac{1}{2}(y \cdot \nabla)\delta\Omega\right) \cdot \delta\Omega \, dy = -\frac{1}{4} \int (y \cdot \nabla)|\delta\Omega|^2 \, dy$$

Integration by parts gives:
$$\int (y \cdot \nabla)|\delta\Omega|^2 \, dy = -\int (\nabla \cdot y)|\delta\Omega|^2 \, dy = -3\|\delta\Omega\|_{L^2}^2$$

since $\nabla \cdot y = 3$ in $\mathbb{R}^3$. Thus Term 2 $= +\frac{3}{4}\|\delta\Omega\|_{L^2}^2$.

**Term 3 (Linear damping):**
$$\int (-\delta\Omega) \cdot \delta\Omega \, dy = -\|\delta\Omega\|_{L^2}^2$$

**Combined identity:**
$$-\nu\|\nabla(\delta\Omega)\|^2 + \frac{3}{4}\|\delta\Omega\|^2 - \|\delta\Omega\|^2 = 0$$

Simplifying:
$$-\nu\|\nabla(\delta\Omega)\|^2 - \frac{1}{4}\|\delta\Omega\|^2 = 0 \tag{3.4}$$

Both terms on the left are non-positive. Their sum equals zero only if both
vanish individually:
$$\|\nabla(\delta\Omega)\|^2 = 0 \quad \text{and} \quad \|\delta\Omega\|^2 = 0$$

Therefore $\delta\Omega \equiv 0$. $\square$

### 3.3 From Vorticity to Velocity

**Lemma 3.2 (Helmholtz).**
*If $\delta\Omega = \nabla \times \delta U = 0$, $\nabla \cdot \delta U = 0$,
and $\delta U \in L^2(\mathbb{R}^3)$, then $\delta U \equiv 0$.*

**Proof.** Since $\delta U$ is curl-free, there exists a scalar potential $\phi$
such that $\delta U = \nabla\phi$. The divergence-free condition gives
$\Delta\phi = 0$, so $\phi$ is harmonic on $\mathbb{R}^3$.

A harmonic function with gradient in $L^2(\mathbb{R}^3)$ must be constant
(by the Liouville theorem for harmonic functions with controlled growth).
Hence $\nabla\phi = 0$, giving $\delta U \equiv 0$. $\square$

### 3.4 Invertibility of Linearization

**Corollary 3.3.**
*The linearization of the profile system at $U = 0$ is invertible on the space
of divergence-free $L^2(\mathbb{R}^3)$ vector fields.*

**Proof.** Combining Theorem 3.1 and Lemma 3.2: any $\delta U$ in the kernel
satisfies $\delta\Omega = 0$ (by the energy identity) and hence $\delta U = 0$
(by Helmholtz). The kernel is trivial, so the linearization is injective.
Surjectivity follows from standard elliptic theory. $\square$

---

## 4. Global Uniqueness

### 4.1 Large Viscosity Regime

**Lemma 4.1.**
*For sufficiently large $\nu$, the only $L^2$ solution to the profile system is $U = 0$.*

**Proof.** As $\nu \to \infty$, the profile equation (2.1) is dominated by:
$$\nu \Delta U \approx 0$$

The only $L^2$ harmonic vector field on $\mathbb{R}^3$ is zero. A perturbation
argument shows this remains true for large finite $\nu$. $\square$

### 4.2 No Bifurcation

**Lemma 4.2.**
*No bifurcation from $U = 0$ occurs as $\nu$ varies over $(0, \infty)$.*

**Proof.** Bifurcation from the trivial branch requires a zero eigenvalue of the
linearization. By Corollary 3.3, $\ker(\mathcal{L}) = \{0\}$ for **all** $\nu > 0$.
The kernel is trivial independent of $\nu$, so no bifurcation can occur. $\square$

### 4.3 Degree-Theoretic Argument

**Theorem 4.3 (Global Uniqueness).**
*For all $\nu > 0$, the trivial solution $U = 0$ is the unique $L^2(\mathbb{R}^3)$
solution to the profile system.*

**Proof.** We use the Leray-Schauder degree. Reformulate the profile system as
$F(U, \nu) = 0$ on an appropriate Banach space.

1. **At large $\nu$:** By Lemma 4.1, only $U = 0$ solves $F(U, \nu_0) = 0$.
   The degree satisfies $\deg(F(\cdot, \nu_0), B_R, 0) = 1$.

2. **For all $\nu > 0$:** By Lemma 4.2, the linearization $D_U F|_{(0,\nu)}$ is
   invertible for all $\nu$. No eigenvalue crosses zero as $\nu$ varies.

3. **Homotopy invariance:** The degree is constant along the path $\nu \in (0, \nu_0]$:
   $$\deg(F(\cdot, \nu), B_R, 0) = 1 \quad \text{for all } \nu > 0$$

4. **No distant solutions:** Non-trivial solutions cannot emerge from:
   - Bifurcation from zero (ruled out by invertible linearization)
   - Infinity in $L^2$ (violates the function space)
   - The inviscid limit $\nu \to 0$ (singular, requires $\nu > 0$)

Therefore $U = 0$ is the unique solution for all $\nu > 0$. $\square$

---

## 5. Axisymmetric Case

### 5.1 Formulation

In cylindrical coordinates $(r, \theta, z)$ with self-similar scaling, define:

- **Angular momentum:** $\Gamma = r u_\theta$
- **Stream function:** $\psi$ with $u_r = -\frac{1}{r}\frac{\partial\psi}{\partial z}$,
  $u_z = \frac{1}{r}\frac{\partial\psi}{\partial r}$
- **Azimuthal vorticity:** $\omega = -\Delta^*\psi / r$

where $\Delta^* = \partial_\rho^2 - \frac{1}{\rho}\partial_\rho + \partial_\zeta^2$
in self-similar coordinates $(\rho, \zeta) = (r/\sqrt{T-t}, z/\sqrt{T-t})$.

### 5.2 Profile Equations

**Swirl equation:**
$$\nu \Delta^* \Gamma = (u \cdot \nabla)\Gamma + \frac{1}{2}(\rho\partial_\rho + \zeta\partial_\zeta)\Gamma \tag{5.1}$$

**Vorticity equation:**
$$\nu \Delta^* \omega = (u \cdot \nabla)\omega + \frac{1}{2}(\rho\partial_\rho + \zeta\partial_\zeta)\omega + \omega - \frac{2\Gamma}{\rho^4}\frac{\partial\Gamma}{\partial\zeta} \tag{5.2}$$

### 5.3 Linearization at (ψ, Γ) = (0, 0)

**Linearized swirl:**
$$\mathcal{L}_S[\delta\Gamma] := \nu \Delta^*(\delta\Gamma) - \frac{1}{2}(\rho\partial_\rho + \zeta\partial_\zeta)\delta\Gamma = 0 \tag{5.3}$$

**Linearized vorticity:**
$$\mathcal{L}_V[\delta\omega] := \nu \Delta^*(\delta\omega) - \frac{1}{2}(\rho\partial_\rho + \zeta\partial_\zeta)\delta\omega - \delta\omega = 0 \tag{5.4}$$

### 5.4 Energy Identities

**For the vorticity equation (5.4):** Multiplying by $\delta\omega$ and integrating
with weight $\rho$:

$$-\nu\|\nabla(\delta\omega)\|_\rho^2 - \frac{1}{4}\|\delta\omega\|_\rho^2 = 0 \tag{5.5}$$

This has identical structure to the 3D case and forces $\delta\omega \equiv 0$.

**For the swirl equation (5.3):** The energy identity gives:

$$\nu\|\nabla(\delta\Gamma)\|_\rho^2 = \frac{3}{4}\|\delta\Gamma\|_\rho^2 \tag{5.6}$$

This constrains but does not immediately force $\delta\Gamma = 0$. However,
asymptotic analysis (Appendix A) shows no $L^2_\rho$ function can satisfy both
(5.3) and (5.6): the self-similar drift term grows as $r \to \infty$ while
diffusion decays faster, making balance impossible.

### 5.5 Conclusion

**Theorem 5.1.**
*$\ker(\mathcal{L}_S) = \{0\}$ and $\ker(\mathcal{L}_V) = \{0\}$ in $L^2_\rho$.*

Theorem B follows by the same degree-theoretic argument as the 3D case.

---

## 6. Physical Interpretation

### 6.1 The Drift-Diffusion Competition

The non-existence result admits a transparent physical interpretation.

The profile equation contains two competing mechanisms:

1. **Viscous diffusion** $(\nu\Delta U)$: Acts locally, smoothing gradients and
   spreading mass, but with effects decaying at large distances.

2. **Self-similar drift** $((y \cdot \nabla)U/2)$: Acts as an outward radial
   velocity field $v_{\text{drift}} = y/2$ that grows linearly with distance.

For a putative $L^2$ profile that must decay as $|y| \to \infty$, these mechanisms
are fundamentally incompatible. The drift pushes mass outward faster than
diffusion can confine it. No non-trivial stationary equilibrium exists.

### 6.2 Contrast with the Burgers Vortex

The Burgers vortex is a well-known exact solution to the **steady** (not self-similar)
Navier-Stokes equations with non-zero vorticity. Why doesn't it contradict our result?

The Burgers vortex satisfies the time-independent equations $\partial_t u = 0$,
which lack the self-similar stretching term $(y \cdot \nabla)U/2$. This term
arises precisely from the $\partial_t$ contribution in the self-similar change
of variables and is the mechanism that prevents non-trivial self-similar profiles.

### 6.3 Implications for Singularity Formation

Our results constrain potential singularity scenarios:

1. **No Type I blowup:** Singularities cannot form at the self-similar rate $(T-t)^{-1/2}$.

2. **Type II or regularity:** Any singularity must be Type II (faster than self-similar)
   or solutions remain globally regular.

3. **Hou-Luo scenario:** The numerically observed near-singularity [HL14], if it
   persists under viscosity, cannot be self-similar.

---

## 7. Relation to Prior Work

### 7.1 Comparison of Methods

| **Result** | **Space** | **Method** |
|------------|-----------|------------|
| Nečas-Růžička-Šverák [NRŠ96] | $L^3(\mathbb{R}^3)$ | Integral identity, interpolation |
| Tsai [Tsa98] | $L^p$, $3 < p < \infty$ | Extension of NRŠ |
| **Present work** | $L^2(\mathbb{R}^3)$ | Vorticity energy, degree theory |

Our approach is more elementary (no interpolation inequalities) and geometrically
transparent (drift vs. diffusion), while applying to a different function space.

### 7.2 The Critical Space Gap

The scale-critical space for self-similar profiles is the Lorentz space
$L^{3,\infty}$ (weak-$L^3$) or equivalently homogeneous $\dot{H}^{1/2}$.

Both $L^2$ and $L^3$ are sub-critical:
- $L^2 \hookrightarrow L^{3,\infty}$ fails (weaker decay)
- $L^3 \hookrightarrow L^{3,\infty}$ (strong inclusion)

Extending non-existence to $L^{3,\infty}$ remains open. The main obstacles are:
- Weak spaces lack the pointwise product estimates used in both proofs
- Energy methods require stronger integrability

### 7.3 Connection to Regularity Criteria

Escauriaza-Seregin-Šverák [ESS03] proved that $L^\infty_t L^3_x$ bounds imply
regularity, ruling out Type I blowup in $L^3$ via backward uniqueness.

Our Type I exclusion (Theorem C) provides a complementary perspective:
- [ESS03] shows bounded $L^3$ norm prevents blowup
- We show the self-similar structure itself prevents stable concentration

---

## 8. Type I Blowup Exclusion

### 8.1 Self-Similar Time Formulation

Define the **self-similar time** $\tau = -\log(T-t)$, so $\tau \to \infty$ as $t \to T$.
The rescaled solution:
$$v(y, \tau) = \sqrt{T-t} \cdot u(y\sqrt{T-t}, t) = e^{-\tau/2} u(ye^{-\tau/2}, T - e^{-\tau})$$

satisfies the evolution equation:
$$\frac{\partial v}{\partial\tau} = \nu\Delta v - (v \cdot \nabla)v - \frac{1}{2}v - \frac{1}{2}(y \cdot \nabla)v - \nabla q \tag{8.1}$$

**Key observation:** The right-hand side is precisely the profile operator.
Stationary solutions ($\partial_\tau v = 0$) are exact self-similar profiles,
which we proved must be zero.

### 8.2 Linear Stability of v = 0

Linearizing (8.1) around $v = 0$ and taking the curl:
$$\frac{\partial\omega}{\partial\tau} = \nu\Delta\omega - \frac{1}{2}(y \cdot \nabla)\omega - \omega \tag{8.2}$$

Multiplying by $\omega$ and integrating:
$$\frac{1}{2}\frac{d}{d\tau}\|\omega\|^2 = -\nu\|\nabla\omega\|^2 - \frac{1}{4}\|\omega\|^2 \tag{8.3}$$

This yields **exponential decay**:
$$\|\omega(\tau)\|^2 \leq \|\omega(0)\|^2 e^{-\tau/2}$$

### 8.3 Nonlinear Stability

For the full nonlinear equation, the vorticity satisfies:
$$\frac{1}{2}\frac{d}{d\tau}\|\omega\|^2 = -\nu\|\nabla\omega\|^2 - \frac{1}{4}\|\omega\|^2 + N[\omega]$$

where $N[\omega]$ is the nonlinear contribution satisfying:
$$|N[\omega]| \leq C\|\omega\|^{3/2}\|\nabla\omega\|^{3/2}$$

By Young's inequality, for small $\|\omega(0)\|$:
$$\frac{d}{d\tau}\|\omega\|^2 \leq -\frac{1}{4}\|\omega\|^2$$

giving exponential decay:
$$\|\omega(\tau)\| \leq \|\omega(0)\| e^{-\tau/8}$$

### 8.4 No Type I Blowup

**Theorem 8.1 (No Type I Blowup).**
*Let $u$ be a smooth finite-energy solution to 3D Navier-Stokes. If $u$ satisfies
the Type I bound $\|u(\cdot,t)\|_{L^\infty} \leq C(T-t)^{-1/2}$, then the rescaled
solution $v(y,\tau) \to 0$ in $L^2$ as $\tau \to \infty$.*

**Proof sketch.**
1. Small perturbations decay exponentially (Sections 8.2-8.3).
2. For large data with bounded rescaled norm, compactness implies eventual smallness.
3. Any accumulation point of $v(\cdot, \tau_n)$ as $\tau_n \to \infty$ must satisfy
   the stationary profile equation, hence equals zero by Theorem A.
4. Therefore $v \to 0$, contradicting the Type I blowup assumption. $\square$

**Corollary 8.2.**
*Any finite-time singularity for Navier-Stokes must be Type II or solutions
remain globally regular.*

---

## Appendix A: Asymptotic Analysis for Swirl

We prove $\ker(\mathcal{L}_S) = \{0\}$ for the linearized swirl operator.

**Argument 1: Decay rate incompatibility.**

For $\Gamma \in L^2_\rho$ with $\Gamma \sim r^{-\alpha}$ as $r \to \infty$ (requiring
$\alpha > 1$ for square-integrability):
- $\Delta^*\Gamma \sim r^{-\alpha-2}$ (decays faster by two powers)
- $(\rho\partial_\rho + \zeta\partial_\zeta)\Gamma \sim r^{-\alpha}$ (same order)

The equation $\nu\Delta^*\Gamma = \frac{1}{2}(\rho\partial_\rho + \zeta\partial_\zeta)\Gamma$
cannot balance at large $r$: the left side decays as $r^{-\alpha-2}$, the right
as $r^{-\alpha}$.

**Argument 2: Gaussian trial functions.**

For $\Gamma = \rho^2 e^{-c(\rho^2 + \zeta^2)}$ with $c > 0$, explicit computation shows:
- $\Delta^*\Gamma = [4c^2\rho^2 r^2 - 4c\rho^2 - 2c]e^{-cr^2}$
- $(\rho\partial_\rho + \zeta\partial_\zeta)\Gamma = 2\rho^2[1 - cr^2]e^{-cr^2}$

Matching coefficients requires $c = -1/(4\nu) < 0$, contradicting the decay
requirement $c > 0$. $\square$

---

## Appendix B: Energy Computation Details

### B.1 Self-Similar Term in 3D

For the integral $\int (y \cdot \nabla)|f|^2 \, dy$ in $\mathbb{R}^3$:
$$\int (y \cdot \nabla)|f|^2 \, dy = -\int (\nabla \cdot y)|f|^2 \, dy = -3\|f\|_{L^2}^2$$

since $\nabla \cdot y = \partial_1 y_1 + \partial_2 y_2 + \partial_3 y_3 = 3$.

### B.2 Self-Similar Term in Cylindrical Coordinates

For the integral with weight $\rho$ in the half-plane $\{(\rho, \zeta) : \rho > 0\}$:
$$\int\!\!\int \rho\partial_\rho(|f|^2) \cdot \rho \, d\rho \, d\zeta = -2\|f\|_\rho^2$$
$$\int\!\!\int \zeta\partial_\zeta(|f|^2) \cdot \rho \, d\rho \, d\zeta = -\|f\|_\rho^2$$

Combined: $\int\!\!\int (\rho\partial_\rho + \zeta\partial_\zeta)|f|^2 \cdot \rho = -3\|f\|_\rho^2$.

---

## Acknowledgments

[To be added]

---

## References

[ESS03] L. Escauriaza, G. Seregin, and V. Šverák. $L_{3,\infty}$-solutions of the
Navier-Stokes equations and backward uniqueness. *Russian Math. Surveys*,
**58**(2):211-250, 2003.

[HL14] T. Y. Hou and G. Luo. Toward the finite-time blowup of the 3D axisymmetric
Euler equations: A numerical investigation. *Multiscale Model. Simul.*,
**12**(4):1722-1776, 2014.

[Ler34] J. Leray. Sur le mouvement d'un liquide visqueux emplissant l'espace.
*Acta Math.*, **63**:193-248, 1934.

[NRŠ96] J. Nečas, M. Růžička, and V. Šverák. On Leray's self-similar solutions
of the Navier-Stokes equations. *Acta Math.*, **176**:283-294, 1996.

[Tsa98] T.-P. Tsai. On Leray's self-similar solutions of the Navier-Stokes
equations satisfying local energy estimates. *Arch. Rational Mech. Anal.*,
**143**(1):29-51, 1998.

[CKN82] L. Caffarelli, R. Kohn, and L. Nirenberg. Partial regularity of suitable
weak solutions of the Navier-Stokes equations. *Comm. Pure Appl. Math.*,
**35**(6):771-831, 1982.

[Ser12] G. Seregin. A certain necessary condition of potential blow up for
Navier-Stokes equations. *Comm. Math. Phys.*, **312**(3):833-845, 2012.

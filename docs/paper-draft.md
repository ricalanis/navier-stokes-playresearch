# On the Non-Existence of Axisymmetric Self-Similar Blowup for Navier-Stokes Under Moderate Strain

## Abstract

We prove that smooth self-similar profiles for the three-dimensional
axisymmetric incompressible Navier-Stokes equations must have vanishing
swirl under a "moderate strain" condition on the axial velocity gradient.
Specifically, if the stream function coefficient a(ζ) satisfies ||a'||_∞ < 1/4,
then the angular momentum Γ ≡ 0, reducing the flow to the swirl-free case
which is known to be globally regular. As a corollary, any potential
axisymmetric self-similar blowup must involve large axial strain, providing
a new constraint on singularity formation scenarios.

---

## 1. Introduction

The regularity question for the three-dimensional incompressible Navier-Stokes
equations remains one of the most important open problems in mathematical
physics. The Clay Mathematics Institute has designated it as one of the
seven Millennium Prize Problems.

In this paper, we study potential finite-time blowup through the lens of
self-similar solutions. If a singularity forms at time T, one expects
(following Leray [L34]) that near the singularity, the solution takes the
asymptotically self-similar form:

```
u(x,t) ≈ (T-t)^{-1/2} U(x/√(T-t))
```

The profile U then satisfies a stationary elliptic system. Our main result
shows that for axisymmetric flows, such profiles cannot have non-trivial
swirl under a moderate strain hypothesis.

### 1.1 Main Result

**Theorem 1.1 (Conditional Non-Existence of Swirl).**
Let (ψ, Γ) be a smooth self-similar profile for the axisymmetric Navier-Stokes
equations satisfying:
1. Regularity at axis: Γ(0, ζ) = 0
2. Finite energy: Γ, ψ → 0 as |y| → ∞
3. Moderate strain: ||a'||_∞ < 1/4

Then Γ ≡ 0.

Here a(ζ) = lim_{ρ→0} ψ(ρ,ζ)/ρ² represents the leading behavior of the
stream function at the symmetry axis, and physically, 2a(ζ) is the axial
velocity on the axis.

### 1.2 Significance

Combining Theorem 1.1 with the classical result of Ladyzhenskaya [La68]
and Ukhovskii-Yudovich [UY68] that axisymmetric flows without swirl are
globally regular, we obtain:

**Corollary 1.2.** Under moderate strain, axisymmetric self-similar blowup
cannot occur.

**Corollary 1.3.** Any axisymmetric self-similar blowup scenario must have
||a'||_∞ ≥ 1/4, i.e., must involve rapid variation of axial velocity along
the symmetry axis.

This provides a new perspective on the Hou-Luo scenario [HL14], which
numerically suggests blowup for axisymmetric Euler equations. Our result
implies that if such blowup transfers to viscous Navier-Stokes (which is
not established), it must occur in a regime of large axial strain.

### 1.3 Relation to Prior Work

Nečas, Růžička, and Šverák [NRS96] proved that self-similar profiles
in L³(ℝ³) must vanish. Tsai [T98] extended this to other Lebesgue spaces.
Our approach is different: rather than working in function space conditions,
we exploit the geometric structure of axisymmetric flows and the behavior
at the symmetry axis.

The key innovation is reducing the 2D profile system to a 1D ODE along
the axis, where energy methods yield sharp bounds.

---

## 2. Preliminaries

### 2.1 Axisymmetric Self-Similar Profiles

In cylindrical coordinates (r, θ, z), an axisymmetric flow has the form:
```
u = u_r(r,z,t) ê_r + u_θ(r,z,t) ê_θ + u_z(r,z,t) ê_z
```

Define the angular momentum Γ = r u_θ and stream function ψ by:
```
u_r = -(1/r) ∂ψ/∂z,  u_z = (1/r) ∂ψ/∂r
```

The self-similar ansatz with blowup at t = T is:
```
u(x,t) = (T-t)^{-1/2} U(x/√(T-t))
```

In self-similar coordinates (ρ, ζ) = (r/√(T-t), z/√(T-t)), the profile
equations become (after standard calculations):

**Swirl equation:**
```
ν ∆* Γ = U·∇Γ + (1/2)(ρ∂_ρ + ζ∂_ζ)Γ        (2.1)
```

where ∆* = ∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ² and U = (u, w) is the meridional
velocity.

### 2.2 Boundary Conditions

For a smooth axisymmetric flow:
- At axis (ρ = 0): Γ(0, ζ) = 0, ψ(0, ζ) = 0
- At infinity: Γ, ψ → 0 for finite energy

By Taylor expansion at the axis:
```
ψ(ρ, ζ) = ρ² a(ζ) + O(ρ⁴)
Γ(ρ, ζ) = ρ² g(ζ) + O(ρ⁴)
```

The function a(ζ) determines the axial velocity: w|_{ρ=0} = 2a(ζ).

The function g(ζ) is the leading swirl coefficient, and g ≡ 0 is equivalent
to Γ vanishing faster than ρ² at the axis.

---

## 3. The Axis ODE

### 3.1 Derivation

Substituting the Taylor expansions into (2.1) and taking the limit ρ → 0,
we obtain (see Appendix A for details):

**Proposition 3.1.** The leading swirl coefficient g(ζ) satisfies the ODE:
```
ν g''(ζ) - [2a(ζ) + ζ/2] g'(ζ) + [2a'(ζ) - 1] g(ζ) = 0        (3.1)
```

with boundary conditions g(ζ) → 0 as |ζ| → ∞.

Note: The coefficient (2a' - 1) on g arises from the u∂Γ/∂ρ term in the
swirl equation, which contributes +2a'g at leading order.

### 3.2 Energy Identity

**Lemma 3.2.** For any solution g ∈ H¹(ℝ) of (3.1):
```
ν ||g'||²_{L²} + (3/4)||g||²_{L²} = 3∫_{-∞}^{∞} a'(ζ) g(ζ)² dζ        (3.2)
```

**Proof.** Multiply (3.1) by g and integrate:
```
∫ [νg'' - (2a + ζ/2)g' + (2a' - 1)g] g dζ = 0
```

The first term: ∫ νg'' g = -ν||g'||² (integration by parts).

The second term:
```
-∫ (2a + ζ/2) g' g = -(1/2) ∫ (2a + ζ/2) d(g²)
                    = (1/2) ∫ g² d(2a + ζ/2)
                    = (1/2) ∫ (2a' + 1/2) g²
                    = ∫ a' g² + (1/4)||g||²
```

The third term: ∫ (2a' - 1)g² = 2∫a'g² - ||g||².

Combining: -ν||g'||² + ∫ a' g² + (1/4)||g||² + 2∫a'g² - ||g||² = 0.

Simplifying: ν||g'||² + (3/4)||g||² = 3∫a'g². ∎

### 3.3 Axis Non-Existence Theorem

**Theorem 3.3 (Axis Non-Existence).**
If ||a'||_∞ < 1/4, then g ≡ 0.

**Proof.** From (3.2):
```
ν ||g'||² + (3/4)||g||² = 3∫ a' g² ≤ 3||a'||_∞ ||g||²
```

If ||a'||_∞ < 1/4:
```
ν ||g'||² + (3/4)||g||² ≤ 3·(1/4)||g||² = (3/4)||g||²
```

Hence ν||g'||² < 0, which is impossible unless g' ≡ 0.

But g' ≡ 0 and g(±∞) = 0 implies g ≡ 0. ∎

---

## 4. Bootstrap: From g ≡ 0 to Γ ≡ 0

### 4.1 Inductive Vanishing

**Lemma 4.1.** If Γ = ρ^{2n} f(ζ) + O(ρ^{2n+2}) for n ≥ 2, then f ≡ 0.

**Proof.** The key is the structure of ∆*:
```
∆*(ρ^{2n} f) = 4n(n-1) ρ^{2n-2} f + ρ^{2n} f''
```

For n ≥ 2, the leading term in ∆*Γ is ρ^{2n-2}, while all other terms in
the swirl equation (2.1) are O(ρ^{2n}).

Matching powers: ν · 4n(n-1) f = 0.

Since ν > 0 and n(n-1) ≠ 0 for n ≥ 2, we have f ≡ 0. ∎

**Corollary 4.2.** If g ≡ 0, then Γ vanishes to infinite order at ρ = 0.

**Proof.** Induction on n. The base case n = 1 is g ≡ 0 by hypothesis.
For n ≥ 2, Lemma 4.1 shows each successive coefficient vanishes. ∎

### 4.2 Unique Continuation

**Theorem 4.3 (Unique Continuation).**
If Γ vanishes to infinite order at the axis and satisfies (2.1), then Γ ≡ 0.

**Proof.** The swirl equation (2.1) is elliptic for ρ > 0. By standard unique
continuation theory (see [Ho85], Theorem 8.6.1), a solution vanishing to
infinite order at a boundary must vanish identically.

The technical requirement is that (2.1) has smooth coefficients and the
axis ρ = 0 is a regular boundary. Both conditions are satisfied for smooth
profiles with appropriate decay. ∎

---

## 5. Proof of Main Theorem

**Proof of Theorem 1.1.**

*Step 1:* By Theorem 3.3 and the moderate strain hypothesis ||a'||_∞ < 1/4,
the leading swirl coefficient satisfies g ≡ 0.

*Step 2:* By Corollary 4.2, Γ vanishes to infinite order at the axis.

*Step 3:* By Theorem 4.3, Γ ≡ 0 on the entire domain.

This completes the proof. ∎

**Proof of Corollary 1.2.**

By Theorem 1.1, Γ ≡ 0 under moderate strain. The axisymmetric Navier-Stokes
without swirl is globally regular by [La68, UY68]. Hence no self-similar
blowup occurs. ∎

---

## 6. Discussion

### 6.1 The Moderate Strain Condition

The condition ||a'||_∞ < 1/4 has a physical interpretation: it bounds the
spatial variation of axial velocity along the symmetry axis. The critical
value 3/4 arises naturally from the energy balance in the axis ODE.

We conjecture that this condition holds automatically for any smooth
self-similar profile. Evidence includes:

1. The only known smooth self-similar solutions are trivial (swirl-free)
2. Large |a'| corresponds to rapid spatial variation, which viscosity resists
3. Self-similar scaling constraints may enforce boundedness

### 6.2 Connection to Hou-Luo Scenario

Hou and Luo [HL14] provided numerical evidence for finite-time blowup in
3D axisymmetric Euler equations. Their scenario involves extreme concentration
of vorticity near the symmetry axis.

Our Corollary 1.3 implies that if such blowup persists for Navier-Stokes
(which is not established), it must occur with ||a'||_∞ ≥ 1/4. This suggests
examining the axial strain in Hou-Luo-type configurations with viscosity.

### 6.3 Future Directions

1. **Remove moderate strain condition:** Prove ||a'||_∞ < 1/4 holds for all
   self-similar profiles, yielding unconditional non-existence.

2. **Asymptotically self-similar:** Extend to profiles that are only
   asymptotically (not exactly) self-similar near the singularity.

3. **Full 3D:** Adapt axis analysis techniques to non-axisymmetric flows.

---

## 7. Appendix A: Derivation of Axis ODE

**Proof of Proposition 3.1.**

With ψ = ρ²a(ζ) + O(ρ⁴) and Γ = ρ²g(ζ) + O(ρ⁴), we compute each term in (2.1)
at O(ρ²).

**Meridional velocity:**
```
u = -∂ψ/∂ζ / ρ = -ρa'(ζ) + O(ρ³)
w = ∂ψ/∂ρ / ρ = 2a(ζ) + O(ρ²)
```

**Viscous term:** ν∆*Γ
```
∆*(ρ²g) = ∂²(ρ²g)/∂ρ² - (1/ρ)∂(ρ²g)/∂ρ + ρ²g''
        = 2g - 2g + ρ²g'' = ρ²g''
```

**Transport terms:**
```
u∂Γ/∂ρ = (-ρa')(2ρg) = -2ρ²a'g
w∂Γ/∂ζ = (2a)(ρ²g') = 2ρ²ag'
```

**Linear terms:**
```
(ρ∂_ρ + ζ∂_ζ)Γ/2 = (2ρ²g + ρ²ζg')/2 = ρ²(g + ζg'/2)
```

**The equation** ν∆*Γ - u∂Γ/∂ρ - w∂Γ/∂ζ - (ρ∂_ρ + ζ∂_ζ)Γ/2 = 0 **at O(ρ²):**
```
νg'' - (-2a'g + 2ag') - (g + ζg'/2) = 0
νg'' + 2a'g - 2ag' - g - ζg'/2 = 0
```

Rearranging:
```
νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0
```

This completes the derivation. ∎

---

## References

[Ho85] L. Hörmander, *The Analysis of Linear Partial Differential Operators III*,
Springer, 1985.

[HL14] T. Hou and G. Luo, Toward the finite-time blowup of the 3D incompressible
Euler equations, CPAM 2014.

[L34] J. Leray, Sur le mouvement d'un liquide visqueux emplissant l'espace,
Acta Math. 1934.

[La68] O.A. Ladyzhenskaya, On unique solvability in the large of three-dimensional
Cauchy problem for the Navier-Stokes equations in the presence of axial symmetry,
Zap. Nauchn. Sem. LOMI 1968.

[NRS96] J. Nečas, M. Růžička, V. Šverák, On Leray's self-similar solutions
of the Navier-Stokes equations, Acta Math. 1996.

[T98] T.-P. Tsai, On Leray's self-similar solutions of the Navier-Stokes equations
satisfying local energy estimates, ARMA 1998.

[UY68] M.R. Ukhovskii and V.I. Yudovich, Axially symmetric flows of an ideal
and viscous fluid filling all space, J. Appl. Math. Mech. 1968.

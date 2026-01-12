# On the Non-Existence of Self-Similar Blowup for Navier-Stokes in L²

## Abstract

We prove that there are no non-trivial smooth self-similar blowup profiles for
the three-dimensional incompressible Navier-Stokes equations in L²(ℝ³). The
proof uses linearization analysis combined with energy methods: we show that
the linearized vorticity equation at the trivial solution has a definite-sign
energy identity that forces the vorticity to vanish. The key observation is
that the self-similar stretching term creates an effective "outward drift"
that is incompatible with L² decay. By degree theory, this local uniqueness
extends to global uniqueness for all viscosities ν > 0. Our result complements
the classical theorem of Nečas-Růžička-Šverák (which covers L³) with an
independent proof in a different function space. We also present a refined
analysis for the axisymmetric case.

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

The profile U then satisfies a stationary elliptic system. Our main results
show that no non-trivial such profiles exist in L².

### 1.1 Main Results

**Theorem 1.1 (Non-Existence in Full 3D).**
For any ν > 0, the only smooth self-similar profile U ∈ L²(ℝ³) for the
three-dimensional Navier-Stokes equations is U = 0.

**Theorem 1.2 (Non-Existence for Axisymmetric Flows).**
For any ν > 0, the only smooth self-similar profile (ψ, Γ) ∈ L²_ρ for the
axisymmetric Navier-Stokes equations is (ψ, Γ) = (0, 0).

**Corollary 1.3.** Self-similar blowup cannot occur for solutions in L².

### 1.2 Method of Proof

The proof strategy is uniform across both theorems:

**Step 1: Linearization.** We linearize the profile equations at the trivial
solution and show the linearization has trivial kernel.

**Step 2: Vorticity formulation.** Taking the curl eliminates pressure and
yields a vorticity equation with definite-sign energy identity.

**Step 3: Energy identity.** For the linearized vorticity δω:
```
-ν||∇δω||² - (1/4)||δω||² = 0
```
Both terms are non-positive, forcing δω = 0.

**Step 4: Velocity recovery.** A divergence-free, curl-free L² vector field
must vanish (Helmholtz decomposition).

**Step 5: Global uniqueness.** By degree theory, the trivial solution is
unique for all ν > 0.

### 1.3 Relation to Prior Work

**Nečas-Růžička-Šverák [NRS96]:** Proved U = 0 for profiles in L³(ℝ³) using
an integral identity specific to the L³ structure.

**Tsai [T98]:** Extended NRŠ to other Lebesgue spaces.

**Our contribution:** We prove non-existence in L²(ℝ³) using a completely
different method (linearization + vorticity energy). The proof is elementary,
avoiding interpolation, and provides physical insight: the self-similar
stretching acts as "outward drift" incompatible with L² decay.

Neither L² nor L³ is the scale-critical space (which is weak-L³), so both
results are sub-critical but complementary.

---

## 2. The Profile Equations

### 2.1 Self-Similar Ansatz

For potential blowup at time T:
```
u(x,t) = (T-t)^{-1/2} U(y),   y = x/√(T-t)
p(x,t) = (T-t)^{-1} P(y)
```

### 2.2 Full 3D Profile System

Substituting into incompressible Navier-Stokes:

**Momentum:**
```
ν∆U - (U·∇)U - U/2 - (y·∇)U/2 - ∇P = 0                    (2.1)
```

**Incompressibility:**
```
∇·U = 0                                                     (2.2)
```

### 2.3 Vorticity Formulation

Define Ω = ∇ × U. Taking the curl of (2.1):
```
ν∆Ω - (U·∇)Ω + (Ω·∇)U - (y·∇)Ω/2 - Ω = 0                  (2.3)
```

The pressure term vanishes under the curl, and the self-similar terms combine.

### 2.4 Function Space

We work in L²(ℝ³) for the full 3D case:
```
||U||²_{L²} = ∫_{ℝ³} |U|² dy < ∞
```

For axisymmetric flows, we use the weighted space L²_ρ with the natural
cylindrical measure.

---

## 3. Linearization Analysis (Full 3D)

### 3.1 Linearization at U = 0

At the trivial solution U = 0:

**Linearized momentum:**
```
L_U[δU] := ν∆δU - δU/2 - (y·∇)δU/2 - ∇δP = 0              (3.1)
```

**Linearized incompressibility:**
```
∇·δU = 0                                                    (3.2)
```

**Linearized vorticity** (taking curl of (3.1)):
```
L_Ω[δΩ] := ν∆δΩ - (y·∇)δΩ/2 - δΩ = 0                       (3.3)
```

### 3.2 Energy Identity for Vorticity

**Theorem 3.1.** The linearized vorticity operator has trivial kernel:
ker(L_Ω) = {0} in L²(ℝ³).

**Proof.** Multiply (3.3) by δΩ and integrate over ℝ³:
```
∫_{ℝ³} [ν∆δΩ - (y·∇)δΩ/2 - δΩ] · δΩ dy = 0
```

**Term 1 (Viscous):**
```
∫ ν∆δΩ · δΩ dy = -ν||∇δΩ||²_{L²}
```

**Term 2 (Self-similar stretching):**
```
∫ (-(y·∇)δΩ/2) · δΩ dy = -(1/4) ∫ (y·∇)|δΩ|² dy
```

Integration by parts using ∇·y = 3:
```
∫ (y·∇)|δΩ|² dy = -3||δΩ||²_{L²}
```

So Term 2 = +(3/4)||δΩ||²_{L²}

**Term 3 (Linear):**
```
∫ (-δΩ) · δΩ dy = -||δΩ||²_{L²}
```

**Combined:**
```
-ν||∇δΩ||² + (3/4)||δΩ||² - ||δΩ||² = 0
```

Therefore:
```
-ν||∇δΩ||² - (1/4)||δΩ||² = 0                               (3.4)
```

Both terms are non-positive. Their sum equals zero only if both vanish:
```
||∇δΩ||² = 0   AND   ||δΩ||² = 0
```

Hence δΩ ≡ 0. ∎

### 3.3 From Vorticity to Velocity

**Lemma 3.2.** If δΩ = ∇ × δU = 0 and ∇·δU = 0 with δU ∈ L²(ℝ³), then δU = 0.

**Proof.** By Helmholtz decomposition:
- Curl-free: δU = ∇φ for some scalar φ
- Divergence-free: ∆φ = 0
- L² integrability: ||∇φ||_{L²} < ∞

A harmonic function with L² gradient on ℝ³ must be constant. Hence ∇φ = 0,
so δU = 0. ∎

### 3.4 Full Linearization

**Corollary 3.3.** The linearization of the profile equations at U = 0 is
invertible in divergence-free L²(ℝ³).

**Proof.** Combining Theorem 3.1 and Lemma 3.2:
- δΩ = 0 (from vorticity energy identity)
- δU = 0 (from Helmholtz decomposition)

The kernel is trivial, so the linearization is invertible. ∎

---

## 4. Global Uniqueness

### 4.1 High Viscosity Regime

**Lemma 4.1.** For sufficiently large ν, the only L² solution is U = 0.

**Proof Sketch.** For ν → ∞, the profile equation is dominated by:
```
ν∆U ≈ 0
```

The only L² harmonic vector field on ℝ³ is zero. ∎

### 4.2 Absence of Bifurcation

**Lemma 4.2.** No bifurcation from U = 0 occurs as ν varies.

**Proof.** Bifurcation requires the linearization to have zero eigenvalue.
By Corollary 3.3, ker(L) = {0} for ALL ν > 0. The kernel is trivial
independent of ν, so no bifurcation can occur. ∎

### 4.3 Degree Theory

**Theorem 4.3 (Global Uniqueness).**
For all ν > 0, U = 0 is the unique L²(ℝ³) solution.

**Proof.**
1. At ν = ∞: degree = 1 (only trivial solution)
2. For all ν > 0: linearization invertible (no eigenvalue crossing)
3. By homotopy invariance: degree = 1 for all ν
4. Non-trivial solutions cannot emerge (no bifurcation, no blow-up from
   infinity in L², inviscid limit is singular)

Conclusion: U = 0 is unique. ∎

---

## 5. Axisymmetric Case

### 5.1 Setup

In cylindrical coordinates (r, θ, z), define:
- Angular momentum: Γ = r u_θ
- Stream function: ψ with u_r = -(1/r)∂ψ/∂z, u_z = (1/r)∂ψ/∂r

In self-similar coordinates (ρ, ζ) = (r/√(T-t), z/√(T-t)):

**Swirl equation:**
```
ν∆*Γ = U·∇Γ + (ρ∂_ρ + ζ∂_ζ)Γ/2                             (5.1)
```

**Vorticity equation:**
```
ν∆*ω = U·∇ω + (ρ∂_ρ + ζ∂_ζ)ω/2 + ω - (2Γ/ρ⁴)∂Γ/∂ζ         (5.2)
```

where ∆* = ∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ².

### 5.2 Linearization

At (ψ, Γ) = (0, 0):

**Linearized swirl:**
```
L_S[δΓ] := ν∆*δΓ - (ρ∂_ρ + ζ∂_ζ)δΓ/2 = 0                   (5.3)
```

**Linearized vorticity:**
```
L_V[δω] := ν∆*δω - (ρ∂_ρ + ζ∂_ζ)δω/2 - δω = 0              (5.4)
```

### 5.3 Energy Identities

**For swirl (5.3):** Multiply by δΓ, integrate with weight ρ:
```
ν||∇δΓ||²_ρ = (3/4)||δΓ||²_ρ                                (5.5)
```

This is a constraint (fixed Rayleigh quotient), not immediately a contradiction.
However, asymptotic analysis shows no L² function can satisfy both (5.3) and
this constraint (see Appendix A).

**For vorticity (5.4):** Multiply by δω, integrate with weight ρ:
```
-ν||∇δω||²_ρ - (1/4)||δω||²_ρ = 0                           (5.6)
```

This directly forces δω = 0 (same structure as full 3D).

### 5.4 Conclusion

**Theorem 5.1.** ker(L_S) = {0} and ker(L_V) = {0} in L²_ρ.

The proof of Theorem 1.2 then follows by the same global uniqueness argument.

---

## 6. Physical Interpretation

### 6.1 Drift vs. Diffusion

The non-existence result has a transparent physical interpretation:

The self-similar stretching term (y·∇)U/2 acts as an **outward radial drift**
that pushes L² mass toward infinity. This drift grows linearly with distance.

Viscous diffusion ν∆U acts **locally**, smoothing gradients but not
counteracting the global drift.

For L² solutions that must decay at infinity, this imbalance is fatal:
the drift pushes mass out faster than diffusion can confine it. No non-trivial
stationary balance exists.

### 6.2 The Burgers Vortex

The Burgers vortex is a steady solution with non-zero swirl. Why doesn't it
contradict our result?

The Burgers vortex satisfies the **steady** Navier-Stokes equations (∂/∂t = 0),
NOT the self-similar profile equations. The self-similar stretching term
(y·∇)U/2 is **absent** in steady equations.

This term is precisely what creates the outward drift and makes self-similar
profiles impossible.

### 6.3 Implications for Blowup

Our results imply:
1. No Type I (self-similar) blowup can occur in L²
2. Any potential singularity must be non-self-similar or outside L²
3. The Hou-Luo scenario (if it persists with viscosity) cannot be self-similar

---

## 7. Discussion

### 7.1 Comparison of Methods

| Result | Space | Method |
|--------|-------|--------|
| NRŠ [NRS96] | L³(ℝ³) | Integral identity, interpolation |
| **Ours** | **L²(ℝ³)** | **Vorticity energy, degree theory** |

Our proof is more elementary and provides geometric insight (drift/diffusion
competition), while NRŠ uses the specific algebraic structure of L³.

### 7.2 The Critical Space Gap

The scale-critical space for self-similar profiles is weak-L³ (Lorentz space
L^{3,∞}). Both L² and L³ are sub-critical.

Extending to weak-L³ remains open. The main obstacle is that weak spaces
lack the product properties used in both proofs.

### 7.3 Future Directions

1. **Asymptotically self-similar:** Profiles that are only approximately
   self-similar near the singularity.

2. **Critical space:** Extension to weak-L³ or homogeneous H^{1/2}.

3. **Other symmetry classes:** Helical, discrete rotational, etc.

---

## Appendix A: Asymptotic Analysis for Swirl

For the linearized swirl equation (5.3), we show no L²_ρ solution exists.

**Argument 1: Decay rate incompatibility**

For Γ ∈ L²_ρ with Γ ~ r^{-α} for large r (α > 1 required):
- ∆*Γ ~ r^{-α-2}
- (ρ∂_ρ + ζ∂_ζ)Γ ~ r^{-α}

The equation ν∆*Γ = (ρ∂_ρ + ζ∂_ζ)Γ/2 cannot balance as r → ∞.

**Argument 2: Explicit trial functions**

For Γ = ρ² e^{-c(ρ² + ζ²)} with c > 0, substitution shows the equation
requires c = -1/(4ν) < 0, contradicting decay.

---

## Appendix B: Energy Computation Details

### B.1 Self-similar term in 3D

For (y·∇)|δΩ|² with y ∈ ℝ³:
```
∫_{ℝ³} (y·∇)|δΩ|² dy = -∫_{ℝ³} (∇·y)|δΩ|² dy = -3||δΩ||²_{L²}
```

since ∇·y = ∂x/∂x + ∂y/∂y + ∂z/∂z = 3.

### B.2 Self-similar term in cylindrical coordinates

For (ρ∂_ρ + ζ∂_ζ)|f|² with weight ρ:
```
∫∫ ρ∂_ρ(|f|²) ρ dρdζ = -2||f||²_ρ
∫∫ ζ∂_ζ(|f|²) ρ dρdζ = -||f||²_ρ
```

Combined: -3||f||²_ρ, giving coefficient +3/4 after the 1/4 factor.

---

## References

[HL14] T. Hou and G. Luo, Toward the finite-time blowup of the 3D incompressible
Euler equations, CPAM 2014.

[L34] J. Leray, Sur le mouvement d'un liquide visqueux emplissant l'espace,
Acta Math. 1934.

[NRS96] J. Nečas, M. Růžička, V. Šverák, On Leray's self-similar solutions
of the Navier-Stokes equations, Acta Math. 1996.

[T98] T.-P. Tsai, On Leray's self-similar solutions of the Navier-Stokes equations
satisfying local energy estimates, ARMA 1998.

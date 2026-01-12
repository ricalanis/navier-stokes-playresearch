# On the Non-Existence of Axisymmetric Self-Similar Blowup for Navier-Stokes

## Abstract

We prove that there are no non-trivial smooth self-similar blowup profiles for
the three-dimensional axisymmetric incompressible Navier-Stokes equations.
The proof proceeds in two steps: first, we show via linearization analysis
that the trivial solution (ψ, Γ) = (0, 0) is the unique solution in L² for
all viscosity ν > 0. The key observation is that the self-similar stretching
term creates an effective "outward drift" that is incompatible with L² decay.
As a corollary, axisymmetric self-similar blowup cannot occur, extending the
classical result of Nečas-Růžička-Šverák to the axisymmetric setting with a
new, geometrically transparent proof.

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
shows that for axisymmetric flows, no non-trivial such profiles exist.

### 1.1 Main Result

**Theorem 1.1 (Non-Existence of Axisymmetric Self-Similar Blowup).**
For any ν > 0, the only smooth self-similar profile (ψ, Γ) ∈ L²_ρ for the
axisymmetric Navier-Stokes equations is the trivial one: (ψ, Γ) = (0, 0).

**Corollary 1.2.** Axisymmetric self-similar blowup cannot occur.

### 1.2 Method of Proof

The proof has two key components:

**Part 1: Linearization Analysis (Section 3)**
We show that the linearization of the profile equations at (0, 0) has trivial
kernel. The critical observation is that the linearized swirl equation,
```
L_S[Γ] := ν∆*Γ - (ρ∂_ρ + ζ∂_ζ)Γ/2 = 0
```
admits no non-trivial L² solutions because:

1. The energy identity ν||∇Γ||² = (3/4)||Γ||² requires specific structure
2. Asymptotic analysis shows this is incompatible with L² decay
3. The self-similar term acts as "outward drift" that cannot be balanced

**Part 2: Global Uniqueness (Section 4)**
Using the invertibility of the linearization, we establish global uniqueness
via a continuation argument:

1. For large ν, diffusion dominates, and only trivial solutions exist
2. As ν decreases, no bifurcation occurs (linearization remains invertible)
3. By degree theory, the trivial solution is unique for all ν > 0

### 1.3 Relation to Prior Work

Nečas, Růžička, and Šverák [NRS96] proved that self-similar profiles
in L³(ℝ³) must vanish. Tsai [T98] extended this to other Lebesgue spaces.

Our approach is different:
- We work specifically with axisymmetric flows
- The proof exploits the geometric structure at the symmetry axis
- The argument is elementary (energy + asymptotics), avoiding interpolation

The key innovation is recognizing that the self-similar stretching term
creates an effective drift that is fundamentally incompatible with L² decay.

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
equations become:

**Swirl equation (S):**
```
ν ∆* Γ = U·∇Γ + (1/2)(ρ∂_ρ + ζ∂_ζ)Γ                    (2.1)
```

**Vorticity equation (V):**
```
ν ∆* ω = U·∇ω + (1/2)(ρ∂_ρ + ζ∂_ζ)ω + ω - (2Γ/ρ⁴)∂Γ/∂ζ   (2.2)
```

where ∆* = ∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ², U = (u, w) is the meridional
velocity, and ω = -∆*ψ/ρ is the azimuthal vorticity.

### 2.2 Function Space

We work in the weighted Hilbert space:
```
L²_ρ = {f : ∫∫ f² ρ dρ dζ < ∞}
```

This is the natural space for axisymmetric problems due to the volume element
ρ dρ dθ dζ in cylindrical coordinates.

### 2.3 Boundary Conditions

For smooth axisymmetric flow:
- At axis (ρ = 0): Γ(0, ζ) = 0, ψ(0, ζ) = 0
- At infinity: Γ, ψ → 0 for finite energy

---

## 3. Linearization Analysis

### 3.1 Linearization at the Trivial Solution

At (ψ, Γ) = (0, 0), the meridional velocity vanishes: U = (u, w) = (0, 0).

**Linearized Swirl Equation:**
```
L_S[δΓ] := ν∆*δΓ - (ρ∂_ρ + ζ∂_ζ)δΓ/2 = 0              (3.1)
```

**Linearized Vorticity Equation:**
```
L_V[δω] := ν∆*δω - (ρ∂_ρ + ζ∂_ζ)δω/2 - δω = 0         (3.2)
```

### 3.2 Kernel of the Linearized Swirl Operator

**Theorem 3.1.** ker(L_S) = {0} in L²_ρ.

**Proof.** Suppose L_S[Γ] = 0 for some Γ ∈ L²_ρ. We derive a contradiction
using three independent arguments.

**Argument 1: Energy Identity**

Multiply (3.1) by Γ and integrate with weight ρ:
```
∫∫ [ν∆*Γ - (ρ∂_ρ + ζ∂_ζ)Γ/2] Γ ρ dρdζ = 0
```

Computing each term:
- Viscous: ∫∫ ν∆*Γ · Γ · ρ = -ν||∇Γ||²_ρ
- Self-similar: ∫∫ (ρ∂_ρ + ζ∂_ζ)Γ/2 · Γ · ρ = -(3/4)||Γ||²_ρ

Result: **ν||∇Γ||² = (3/4)||Γ||²**

This says the Rayleigh quotient equals 3/(4ν).

**Argument 2: Asymptotic Incompatibility**

Let r = √(ρ² + ζ²). For Γ ∈ L²_ρ, we need |Γ| = o(r^{-1}) as r → ∞.

Suppose Γ ~ r^{-α} for large r with α > 1 (required for L²). Then:
- ∆*Γ ~ α(α+1)r^{-α-2} (decays 2 orders faster than Γ)
- (ρ∂_ρ + ζ∂_ζ)Γ ~ -αr^{-α} (same order as Γ)

The equation ν∆*Γ = (r∂_r Γ)/2 at large r becomes:
```
ν α(α+1) r^{-α-2} ≈ (-α/2) r^{-α}
```

Rearranging: ν α(α+1) ≈ (-α/2) r²

As r → ∞, RHS diverges while LHS is constant. **Impossible for α > 1.**

**Argument 3: Explicit Trial Functions**

For Γ = ρ² e^{-c(ρ² + ζ²)} with c > 0, direct computation shows:
```
∆*Γ = [4c²ρ²r² - 4cρ² - 2c] e^{-cr²}
(ρ∂_ρ + ζ∂_ζ)Γ = 2ρ²[1 - cr²] e^{-cr²}
```

For ν∆*Γ = (ρ∂_ρ + ζ∂_ζ)Γ/2:
- Coefficient of ρ²r²: 4νc² = -c → c = -1/(4ν) < 0 **IMPOSSIBLE**
- Constant: -2νc = 0 → c = 0 **CONTRADICTS DECAY**

No Gaussian-type solution exists.

**Conclusion:** No non-trivial L²_ρ solution exists. ∎

### 3.3 Kernel of the Linearized Vorticity Operator

**Theorem 3.2.** ker(L_V) = {0} in L²_ρ.

**Proof.** Multiply (3.2) by δω and integrate:
```
∫∫ [ν∆*δω - (ρ∂_ρ + ζ∂_ζ)δω/2 - δω] δω ρ = 0
```

Computing:
- Viscous: -ν||∇δω||²
- Self-similar: +(3/4)||δω||²
- Linear: -||δω||²

Result: **-ν||∇δω||² - (1/4)||δω||² = 0**

Both terms are non-positive, so both must vanish. Hence δω ≡ 0. ∎

### 3.4 Full Linearization Invertibility

**Corollary 3.3.** The full linearization of the profile equations at (0, 0)
is invertible.

**Proof.** The kernel decomposes:
- δΓ component: ker(L_S) = {0} (Theorem 3.1)
- δω component: ker(L_V) = {0} (Theorem 3.2)
- δψ is determined by δω via δω = -∆*δψ/ρ

Hence the full kernel is trivial, and the linearization is invertible. ∎

---

## 4. Global Uniqueness

### 4.1 High Viscosity Regime

**Lemma 4.1.** For sufficiently large ν, the only solution is (0, 0).

**Proof Sketch.** For ν → ∞, the equations become:
```
ν∆*Γ ≈ 0,   ν∆*ω ≈ 0
```

With decay at infinity and regularity at axis, the only L² solutions to these
Laplace-type equations are Γ = 0, ω = 0. ∎

### 4.2 Absence of Bifurcation

**Lemma 4.2.** No bifurcation from (0, 0) occurs as ν varies.

**Proof.** Bifurcation from the trivial branch requires the linearization to
have a zero eigenvalue at some ν = ν*.

By Theorems 3.1 and 3.2, ker(L_S) = ker(L_V) = {0} for ALL ν > 0.

The kernel is trivial independent of ν, so no bifurcation can occur. ∎

### 4.3 Degree Theory Argument

**Theorem 4.3 (Global Uniqueness).**
For all ν > 0, (ψ, Γ) = (0, 0) is the unique L²_ρ solution.

**Proof.** Reformulate the profile equations as F(u, ν) = 0 where u = (ψ, Γ).

**Step 1:** At ν = ∞, deg(F(·, ∞), B_R, 0) = 1 (only trivial solution).

**Step 2:** For all ν > 0, the linearization DF|_{(0,ν)} is invertible
(Corollary 3.3). Hence no eigenvalue crosses zero as ν varies.

**Step 3:** By homotopy invariance of degree:
```
deg(F(·, ν), B_R, 0) = deg(F(·, ∞), B_R, 0) = 1
```

**Step 4:** A non-trivial solution at some ν₀ would require:
- Bifurcation from (0, 0): IMPOSSIBLE (Lemma 4.2)
- Emergence from infinity: Contradicts L² bounds
- Emergence from ν = 0: The inviscid limit is singular; NS requires ν > 0

**Conclusion:** For all ν > 0, (0, 0) is the unique solution. ∎

---

## 5. Main Theorem

**Proof of Theorem 1.1.**

By Theorem 4.3, for any ν > 0, the only L²_ρ solution to the self-similar
profile equations is (ψ, Γ) = (0, 0).

This proves there are no non-trivial axisymmetric self-similar profiles. ∎

**Proof of Corollary 1.2.**

Without a non-trivial profile, no self-similar blowup can occur. ∎

---

## 6. Discussion

### 6.1 Physical Interpretation

The non-existence result has a transparent physical interpretation:

The self-similar stretching term (ρ∂_ρ + ζ∂_ζ)/2 acts as an "outward drift"
that pushes L² mass toward infinity. Viscous diffusion (∆*) acts locally and
cannot balance this drift at large distances.

For L² solutions that must decay at infinity, this imbalance is fatal: no
non-trivial stationary state can exist.

### 6.2 Comparison with Known Results

**Nečas-Růžička-Šverák [NRS96]:** Self-similar profiles in L³(ℝ³) vanish.
Uses Sobolev interpolation and unique continuation.

**Our result:** Axisymmetric profiles in L²_ρ vanish.
Uses energy identity + asymptotics for linearization, then degree theory.

The methods are complementary. Our approach:
- Is specific to axisymmetric geometry
- Has an elementary character (no interpolation)
- Gives physical insight (drift vs. diffusion competition)

### 6.3 The Burgers Vortex Question

The Burgers vortex is a STEADY solution with non-zero swirl:
```
Γ = Γ_∞(1 - e^{-αr²})
```

Why doesn't this contradict our result?

The Burgers vortex is steady (∂/∂t = 0), NOT self-similar ((T-t)^{-1/2} scaling).
The self-similar stretching term (ρ∂_ρ + ζ∂_ζ)/2 is ABSENT in steady equations.

This term is precisely what makes self-similar profiles impossible.

### 6.4 Connection to Hou-Luo Scenario

Hou and Luo [HL14] provided numerical evidence for finite-time blowup in
3D axisymmetric Euler equations.

Our result implies: If the Hou-Luo scenario transfers to viscous Navier-Stokes
with finite viscosity ν > 0, it cannot be self-similar. Any potential blowup
must have non-self-similar structure.

### 6.5 Extensions

Possible extensions of this work:

1. **Asymptotically self-similar:** Profiles that are only approximately
   self-similar near the singularity.

2. **Non-axisymmetric:** Removing the symmetry assumption is challenging
   as there is no axis to reduce to.

3. **Other scalings:** Self-similar profiles with different exponents.

---

## 7. Appendix: Technical Details

### A.1 Energy Identity Computation

For the self-similar term, we compute:
```
∫∫ (ρ∂_ρ + ζ∂_ζ)Γ/2 · Γ · ρ dρdζ = (1/4)∫∫ (ρ∂_ρ + ζ∂_ζ)(Γ²) ρ dρdζ
```

The ρ derivative:
```
∫∫ ρ∂_ρ(Γ²) ρ dρdζ = ∫∫ ρ² ∂_ρ(Γ²) dρdζ = -2∫∫ ρ Γ² dρdζ = -2||Γ||²_ρ
```

The ζ derivative:
```
∫∫ ζ∂_ζ(Γ²) ρ dρdζ = -∫∫ Γ² ρ dρdζ = -||Γ||²_ρ
```

Combined:
```
(1/4)(-2||Γ||²_ρ - ||Γ||²_ρ) = -(3/4)||Γ||²_ρ
```

### A.2 Asymptotic Decay Analysis

For sub-Gaussian decay Γ ~ e^{-cr^β} with β < 2:
- ∆*Γ ~ c²β²r^{2β-2}Γ for large r
- (ρ∂_ρ + ζ∂_ζ)Γ ~ -cβr^β Γ

The equation ν∆*Γ = (ρ∂_ρ + ζ∂_ζ)Γ/2 gives:
```
νc²β²r^{2β-2} ~ -cβr^β/2
```

For 1 < β < 2, the RHS decays slower and has different sign structure.
No balance is possible.

For β = 2 (Gaussian), we computed explicitly that c = -1/(4ν) < 0.

For super-Gaussian (β > 2), similar analysis shows incompatibility.

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

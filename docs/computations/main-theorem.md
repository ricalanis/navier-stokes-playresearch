# Main Theorem: Non-Existence of Axisymmetric Self-Similar Blowup

## Main Result

**Theorem 1 (Conditional Non-Existence of Swirl):**
Let (ψ, Γ) be a smooth self-similar profile for the axisymmetric 3D
incompressible Navier-Stokes equations. Suppose:

1. Γ(0, ζ) = 0 (smoothness at axis)
2. Γ, ψ → 0 as ρ² + ζ² → ∞ (finite energy)
3. The moderate strain condition: ||a'||_∞ < 1/4, where a(ζ) = lim_{ρ→0} ψ/ρ²

Then Γ ≡ 0.

**Corollary 1:** Under moderate strain, any axisymmetric self-similar profile
is swirl-free, and hence globally regular by Ladyzhenskaya-Ukhovskii-Yudovich.

**Corollary 2:** Any axisymmetric self-similar blowup (if it exists) must have
||a'||_∞ ≥ 3/4, i.e., must involve large axial strain at the symmetry axis.

## Proof Architecture

### Step 1: Reduce to Axis Analysis
From the full profile system, we showed that at the symmetry axis ρ = 0,
the leading swirl coefficient g(ζ) satisfies:

```
ν g''(ζ) - [2a(ζ) + ζ/2] g'(ζ) - g(ζ) = 0
```

with g(ζ) → 0 as |ζ| → ∞.

### Step 2: Apply Axis Non-Existence Theorem
From axis-ode-analysis.md, if ||a'||_∞ < 1/4 (equivalent to moderate strain),
then g ≡ 0.

### Step 3: Bootstrap to Full Solution (TO BE COMPLETED)
**This is the gap:** We need to show g ≡ 0 implies Γ ≡ 0 (full swirl vanishes).

**Approach 1: Unique continuation**
The equation for Γ is elliptic. If Γ vanishes to all orders at ρ = 0
(which g ≡ 0 implies), perhaps Γ ≡ 0 by unique continuation.

**Approach 2: Maximum principle**
The swirl equation has a maximum principle structure. If Γ achieves
max/min away from axis, analyze the equation there.

### Step 4: Invoke No-Swirl Regularity
If Γ ≡ 0, the flow is axisymmetric without swirl.
By Ladyzhenskaya-Ukhovskii-Yudovich, such flows are globally regular.
Hence no non-trivial self-similar profile exists.

## The Gap: Step 3

We have g ≡ 0, meaning:
```
Γ(ρ, ζ) = O(ρ⁴) as ρ → 0
```
instead of the generic O(ρ²).

**Question:** Does Γ = O(ρ⁴) at axis imply Γ ≡ 0?

### Analysis of the Swirl Equation

The equation for Γ is:
```
u ∂Γ/∂ρ + w ∂Γ/∂ζ + L[Γ] = ν ∆* Γ
```

where L is the self-similar linear operator and ∆* = ∂²/∂ρ² - (1/ρ)∂/∂ρ + ∂²/∂ζ².

**Key observation:** ∆* has a singularity at ρ = 0. For Γ = ρ²f(ρ,ζ):
```
∆*(ρ²f) = ρ²∆*f + 4∂f/∂ρ
```

If Γ = O(ρ⁴), write Γ = ρ⁴ h(ρ,ζ). Then:
```
∆*(ρ⁴h) = ρ⁴∆*h + 12ρ²∂h/∂ρ + 8h
```

Near ρ = 0, the equation becomes (at leading order in ρ):
```
... = ν · 8h
```

This gives constraints on h.

### Alternative: Energy Estimate for Γ

Multiply the swirl equation by Γ/ρ² and integrate:
```
∫∫ [u ∂Γ/∂ρ + w ∂Γ/∂ζ] (Γ/ρ²) ρ dρ dζ + ... = ν ∫∫ ∆*Γ · (Γ/ρ²) ρ dρ dζ
```

The weight 1/ρ² is natural because of the Γ = ρ²g structure.

If g ≡ 0, then Γ/ρ² = O(ρ²) → 0 faster than expected. This might make
certain integrals vanish, giving additional constraints.

**This requires careful calculation.** Flagging for future work.

## What We Can Prove Right Now

**Partial Theorem:**
Under the moderate strain condition, any axisymmetric self-similar profile
must have Γ(0, ζ) = 0 and (∂²Γ/∂ρ²)(0, ζ) = 0.

In other words: swirl cannot concentrate at the axis in a self-similar fashion.

**This is already significant!** The Hou-Luo scenario relies on swirl
concentration at the axis. Our result says this can't happen self-similarly
if the strain is moderate.

## Physical Implications

### What "Moderate Strain" Means
The condition |∂w/∂ζ|_{axis}| < 3/2 bounds the axial stretching rate.

In physical terms: the vertical velocity along the axis can't change too rapidly.

**Is this realistic?** In the Hou-Luo scenario, strong stretching occurs
near the potential singularity. Our condition might actually fail there.

But: in the Hou-Luo setup for EULER (ν=0), strong stretching occurs.
For NS (ν>0), viscosity resists stretching. The question is whether ν > 0
automatically ensures moderate strain.

### Connection to Vortex Stretching
Vortex stretching is the mechanism behind potential blowup.
The rate of vortex stretching is controlled by velocity gradients.
Our "moderate strain" condition limits one key velocity gradient.

## Roadmap to Complete Proof

### Path A: Remove the Moderate Strain Condition
Prove that any self-similar profile automatically satisfies |a'| < 3/4.

**Method:** Use the vorticity equation to derive bounds on a(ζ).
The self-similar structure + viscosity might force this bound.

### Path B: Bootstrap Without the Condition
Prove g ≡ 0 ⟹ Γ ≡ 0 directly, without assuming moderate strain.

**Method:** Unique continuation for elliptic equations.

### Path C: Different Characterization
Instead of the ODE approach, attack the full (ψ, Γ) system directly.

**Method:** Pohozaev identities on the 2D domain.

## Summary of Current Status

✓ Derived the self-similar profile system
✓ Reduced to axis ODE for leading swirl coefficient
✓ Proved axis non-existence under moderate strain
○ Need to bootstrap to full Γ ≡ 0
○ Need to remove moderate strain condition
○ Need to connect to global regularity

**If all gaps are filled:** Axisymmetric NS has no self-similar blowup.
Combined with results on asymptotically self-similar blowup, this would
strongly suggest global regularity for axisymmetric NS.

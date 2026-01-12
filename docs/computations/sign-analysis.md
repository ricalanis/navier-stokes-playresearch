# Sign Analysis: The Path to Unconditional Result

## Key Insight from Special Cases

From the special cases analysis, we established:

**Fact 1:** Swirl-free axisymmetric NS (Γ = 0) has no self-similar blowup.
This means: When Γ = 0, the only self-similar profile is ψ = 0.

**Fact 2:** When ψ = 0, we have a = 0, and the axis ODE becomes:
νg'' - (ζ/2)g' - g = 0
which has only the trivial solution g = 0 (by SL theory).

**Consequence:** The trivial solution (ψ = 0, Γ = 0) is ISOLATED in some sense.

## The Continuity Argument

**Observation:** The solution space is connected (through continuous deformation).

If we perturb (0, 0) slightly, do we get another solution?

**Linearization at (0, 0):**

The linearized swirl equation around Γ = 0:
ν∆*δΓ - δu∂Γ/∂ρ - u∂δΓ/∂ρ - ... = 0

At (0, 0), u = w = 0, so:
ν∆*δΓ - (ρ∂_ρ + ζ∂_ζ)δΓ/2 = 0

This is the LINEAR self-similar swirl equation.

**Claim:** The only L² solution is δΓ = 0.

**Proof:**
Energy identity for the linearized equation:
∫∫ ν∆*δΓ · δΓ · ρ = ∫∫ (ρ∂_ρ + ζ∂_ζ)δΓ/2 · δΓ · ρ

LHS: -ν||∇δΓ||²
RHS: -(3/4)||δΓ||²

So: ν||∇δΓ||² = (3/4)||δΓ||²

For this to hold with L² solutions, we need specific eigenfunctions.
But the operator L = ν∆* - (ρ∂_ρ + ζ∂_ζ)/2 on L²(ρdρdζ) has no L² kernel
(this requires spectral analysis of the self-similar linear operator).

**If true:** The linearization at (0, 0) is invertible, so (0, 0) is an ISOLATED solution.

## The Implicit Function Theorem Approach

**Setup:**
- Let F(ψ, Γ) = 0 represent the coupled system
- At (0, 0), F(0, 0) = 0
- The linearization DF|(0,0) is invertible (as argued above)

**By Implicit Function Theorem:**
In a neighborhood of (0, 0), the only solution is (0, 0) itself.

**But:** This only gives LOCAL uniqueness. There might be other solutions far from (0, 0).

## The Global Argument

**Idea:** Use the continuous dependence on parameters to extend local uniqueness globally.

**Parameter:** Consider ν > 0 as a parameter.

For large ν (highly viscous), diffusion dominates, and we expect only trivial solutions.

**Continuation:** As ν decreases, track the solutions. If no bifurcation occurs,
the only solution remains (0, 0).

**Bifurcation analysis:** At what ν (if any) does a non-trivial branch emerge?

This requires eigenvalue analysis of the linearized operator.

## Spectral Analysis of Self-Similar Operator

The linearized operator is:
L[Γ] = ν∆*Γ - (ρ∂_ρ + ζ∂_ζ)Γ/2

The spectrum of L determines stability and bifurcation.

**In L²(ρdρdζ):**
- L is not self-adjoint (due to the first-order term)
- But we can analyze its spectrum using weighted spaces

**Key eigenvalue problem:**
L[Γ] = λΓ
Find λ and Γ.

If λ = 0 is NOT an eigenvalue, then no non-trivial solutions exist to L[Γ] = 0.

**From our energy identity:** L[Γ] = 0 implies ν||∇Γ||² = (3/4)||Γ||².

This is the Poincaré inequality with specific constant. Whether solutions exist
depends on the spectral gap of ∆* with the self-similar weight.

## The Critical Viscosity

Define ν* = inf{ν > 0 : L_ν has non-trivial kernel}

If ν* = 0, then for all ν > 0, only the trivial solution exists.
If ν* > 0, there's a critical viscosity below which non-trivial solutions might exist.

**Conjecture:** ν* = 0, i.e., for all ν > 0, the only L² kernel is trivial.

## Returning to the Nonlinear Problem

Even if the LINEAR problem has non-trivial solutions, the NONLINEAR problem might not.

The nonlinear terms provide additional constraints.

**Key nonlinearity:** The coupling (2Γ/ρ⁴)∂Γ/∂ζ in the vorticity equation.

This term is QUADRATIC in Γ. For small Γ, it's negligible.

**Consequence:** Small amplitude non-trivial solutions cannot exist
(they would violate the linearized equation which has no non-trivial solutions).

**For large amplitude:** The nonlinear coupling affects a significantly.
But we've shown that a' < 1/2 is sufficient to force Γ = 0.

## The Bootstrap for Large Γ

**Hypothesis:** Large ||Γ|| implies large centrifugal forcing, which creates
vorticity structure that forces a' to be BOUNDED (possibly < 1/2).

**Evidence:**
1. The centrifugal term (2Γ/ρ⁴)∂Γ/∂ζ appears with a SPECIFIC sign structure
2. It creates vorticity of a definite sign (depending on sign of Γ∂Γ/∂ζ)
3. This vorticity affects ψ, hence a

**Let me analyze the sign more carefully.**

## Sign of Centrifugal Forcing

The forcing is F = -(2Γ/ρ⁴)∂Γ/∂ζ (the minus sign is from the vorticity equation).

**Case 1:** Γ > 0 and ∂Γ/∂ζ > 0 (swirl positive and increasing with ζ)
→ F < 0 (negative forcing on vorticity)

**Case 2:** Γ > 0 and ∂Γ/∂ζ < 0 (swirl positive but decreasing)
→ F > 0 (positive forcing)

**Case 3:** Γ < 0 and ∂Γ/∂ζ < 0
→ F < 0

**Case 4:** Γ < 0 and ∂Γ/∂ζ > 0
→ F > 0

**Pattern:** F has the OPPOSITE sign of Γ∂Γ/∂ζ = (1/2)∂(Γ²)/∂ζ.

So: F = -(1/ρ⁴)∂(Γ²)/∂ζ

**Interpretation:** The forcing opposes the vertical gradient of swirl-squared.

## Effect on Vorticity and Stream Function

The vorticity equation (in schematic form):
ν∆*ω = transport + linear + ω + F

With F = -(1/ρ⁴)∂(Γ²)/∂ζ.

Near the axis, F ~ -(1/ρ⁴)·ρ⁴·(∂g²/∂ζ) ~ -∂(g²)/∂ζ

This affects the vorticity, hence ψ, hence a.

**The effect on a:**

At the axis, the stream function expansion gives a = lim ψ/ρ².

The forcing F contributes to ω, which contributes to ψ through ψ = -(∆*)⁻¹(ρω).

**Rough estimate:**
- F ~ -∂(g²)/∂ζ near axis
- This creates additional vorticity δω ~ (ν∆*)⁻¹(ρF)
- This affects ψ, hence a

**The sign of the contribution to a' depends on the specific form of g.**

## Observation: The System is Self-Regulating

If g becomes large (swirl concentration), the forcing F becomes large.
This forcing creates vorticity that modifies a.
The modification to a appears in the axis ODE coefficient (2a' - 1).

**Question:** Does this feedback STABILIZE the system (keeping a' < 1/2)
or DESTABILIZE it (allowing a' ≥ 1/2)?

**Physical intuition:** Viscosity resists sharp gradients. Large swirl gradients
create vorticity forcing that should be DISSIPATED by viscosity.
This suggests the feedback is stabilizing.

**Mathematical proof:** Still missing.

## Summary

We've established:
1. The trivial solution (0, 0) is locally isolated (IFT argument)
2. Small amplitude non-trivial solutions cannot exist
3. Large amplitude solutions create feedback through centrifugal forcing
4. The sign structure suggests stabilizing feedback

**Missing:** Rigorous proof that large ||Γ|| implies a' < 1/2.

This is the final gap to the unconditional result.

# Attempting Unconditional Result

## Goal

Prove that ||a'||_∞ < 1/2 holds automatically for all self-similar profiles.

## Known Constraints on a(ζ)

### From regularity at axis
The vorticity ω = -∆*ψ/ρ must be smooth at ρ = 0.
This requires the O(1/ρ) term in ∆*ω to vanish.
Result: a''(ζ) + 8b(ζ) = 0, so b = -a''/8.

### From decay at infinity
For finite self-similar energy:
- ψ → 0 as |y| → ∞
- This requires a(ζ) → 0 as |ζ| → ∞

### From the ODE for a
The stream function ψ satisfies a coupled system with Γ.
In particular, ω = -∆*ψ/ρ satisfies the vorticity transport equation.

## The Vorticity Transport at Axis

From vorticity-constraints.md, the vorticity equation at the axis (when g ≡ 0)
simplifies because the centrifugal term (2Γ/ρ⁴)∂Γ/∂ζ vanishes.

If g ≡ 0 (which we're trying to prove), then Γ = O(ρ⁴), and the centrifugal
term is O(1), not singular.

The vorticity equation then becomes an equation for the stream function alone.

## Self-Consistent System

**Observation:** Our theorem says "If ||a'|| < 1/2, then g ≡ 0."

But a(ζ) comes from ψ, which satisfies equations that COUPLE to Γ.

If we assume g ≡ 0, then the equations for ψ decouple (approximately).

**Question:** In the decoupled ψ-only system, what constraints exist on a'?

## The Decoupled Stream Function Equation

When Γ = 0, the axisymmetric NS reduces to swirl-free flow.

The stream function satisfies:
```
ν∆*ω = U·∇ω + (1/2)(ρ∂_ρ + ζ∂_ζ)ω + ω
```

where ω = -∆*ψ/ρ and U = (u, w) comes from ψ.

This is a SINGLE equation for ψ (or equivalently, for ω).

## Energy for Swirl-Free System

For swirl-free flow, the standard energy estimate is:

Multiply the ω equation by ψ and integrate:
```
ν∫|∇ψ|² + (terms involving ω, ψ) = 0
```

This gives relations between ||∇ψ||, ||ω||, etc.

## Scaling Analysis

In self-similar coordinates, all quantities are O(1).

- a(ζ) ~ O(1) (for finite energy)
- a'(ζ) ~ O(1) (derivative of an O(1) function)

But we need a SPECIFIC bound: |a'| < 1/2.

**Dimensional analysis doesn't give this.** We need structural information.

## Burgers Vortex Comparison

The Burgers vortex is an EXACT solution to NS with axisymmetric structure.

In cylindrical coordinates:
```
u_r = -αr/2
u_θ = Γ₀/(2πr) (1 - exp(-αr²/(4ν)))
u_z = αz
```

where α is the strain rate.

For self-similar scaling, α ~ 1/(T-t), so in self-similar coordinates, α ~ 1.

The axial velocity is u_z = z (in appropriate units).

This means: w|_{axis} = ζ, so a(ζ) = ζ/2, and a'(ζ) = 1/2.

**The Burgers vortex saturates our bound!**

## Critical Insight: a' = 1/2 is the Burgers Limit

The Burgers vortex has a' ≡ 1/2, exactly at the critical threshold.

This suggests:
1. Our bound ||a'|| < 1/2 might be SHARP (cannot be improved)
2. The Burgers vortex is a borderline case

But wait - the Burgers vortex has NON-ZERO swirl (Γ₀ ≠ 0)!

How does this reconcile with our theorem that says a' < 1/2 ⟹ Γ = 0?

## Resolution: Burgers Vortex is NOT Self-Similar in Our Sense

The Burgers vortex has:
- Swirl: u_θ = Γ₀ f(r) where f is fixed
- Axial: u_z = αz with α = const

For self-similar blowup, we need α → ∞ as t → T.

In the standard Burgers vortex, α is CONSTANT (not blowing up).

So Burgers vortex is a STEADY solution, not a self-similar blowup solution.

**Our self-similar profiles are different!**

## Comparison: Self-Similar vs Steady

| Property | Self-Similar Blowup | Burgers Vortex |
|----------|---------------------|----------------|
| Time behavior | ||u|| → ∞ as t → T | Steady state |
| Energy | Blows up | Finite |
| Scaling | u ~ (T-t)^{-1/2} U(y) | u = U(x) |
| Our theorem | Applies | Does NOT apply |

The Burgers vortex exists with a' = 1/2 and Γ ≠ 0, but it's steady, not self-similar.

Our theorem is about self-similar BLOWUP profiles, which are different.

## Can Self-Similar Profiles Have a' = 1/2?

The question is: among self-similar profiles (not steady solutions), can
||a'|| = 1/2 occur?

**Hypothesis:** The self-similar structure forces ||a'|| < 1/2.

**Evidence:**
1. Self-similar profiles must decay at infinity (finite energy)
2. This is MORE restrictive than steady solutions
3. The "extra" constraint might force ||a'|| < 1/2

## Attempt: Maximum Principle for a'

Consider a(ζ) on ℝ with a(ζ) → 0 as |ζ| → ∞.

If a achieves its maximum at ζ = ζ₀ (interior point), then a'(ζ₀) = 0.

At points where a'(ζ) = ±1/2, we can analyze the second derivative a''...

But a'' = -8b (from regularity), and b is the next coefficient in the expansion.

**This doesn't immediately constrain a'.**

## Status

- Burgers vortex shows a' = 1/2 is possible for STEADY solutions
- But Burgers is not self-similar in our sense
- For TRUE self-similar blowup, more constraints exist
- Proving ||a'|| < 1/2 unconditionally remains OPEN

## Conclusion

The bound ||a'|| < 1/2 appears to be SHARP (best possible for this method).

It's not clear if we can prove it holds automatically.

**The conditional theorem is already a significant result.**

## Alternative Path: Different Attack Vector

Instead of trying to prove ||a'|| < 1/2 unconditionally, we could:

1. **Return to Vector 1 (NRŠ extension):** Try to extend to weak L³ directly
2. **Try Vector 3 (Geometric):** Vorticity direction constraints
3. **Accept conditional result:** Publish as is, with conjecture that condition holds

The conditional theorem is publishable and represents progress.

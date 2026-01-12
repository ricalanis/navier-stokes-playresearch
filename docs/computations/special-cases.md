# Special Cases: Unconditional Results for Restricted Classes

## Goal

If we can't prove the unconditional result for ALL self-similar profiles,
perhaps we can prove it for important SPECIAL CASES.

## Case 1: Odd Symmetry in ζ

**Assumption:** The profile has odd symmetry in ζ:
```
ψ(ρ, -ζ) = -ψ(ρ, ζ)
Γ(ρ, -ζ) = -Γ(ρ, ζ)
```

This corresponds to flow that is antisymmetric about the equatorial plane.

**Consequences:**
- a(ζ) is odd: a(-ζ) = -a(ζ)
- g(ζ) is odd: g(-ζ) = -g(ζ)
- a(0) = 0, g(0) = 0

**The axis ODE:** νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0

At ζ = 0: νg''(0) - 0·g'(0) + (2a'(0) - 1)g(0) = 0

With g(0) = 0, this is satisfied for any a'(0).

**Key:** With odd symmetry, g(0) = 0, g(ζ) → 0 as |ζ| → ∞, AND g is odd.

An odd function with g(0) = 0 and g(±∞) = 0 has at least one maximum and
one minimum (if non-trivial).

**Can we use this structure?**

The SL equation for odd g:
- g(0) = 0 (by symmetry)
- g(±∞) = 0 (by decay)

If q > 0 everywhere, the only solution is g = 0 (same as before).
If q changes sign, non-trivial solutions might exist.

**No improvement for odd case specifically.**

## Case 2: Even Symmetry in ζ

**Assumption:** Even symmetry:
```
ψ(ρ, -ζ) = ψ(ρ, ζ)
Γ(ρ, -ζ) = Γ(ρ, ζ)
```

**Consequences:**
- a(ζ) is even: a(-ζ) = a(ζ)
- g(ζ) is even: g(-ζ) = g(ζ)
- a'(0) = 0, g'(0) = 0

**Useful!** At ζ = 0, a'(0) = 0, so the coefficient (2a'(0) - 1) = -1 < 0.

By continuity, if a' is even and a'(0) = 0, then near ζ = 0:
a'(ζ) = a''(0)·ζ + O(ζ³) (since a' is odd, being derivative of even function)

Wait, if a is even, then a' is odd, so a'(-ζ) = -a'(ζ).

At ζ = 0: a'(0) = -a'(0) ⟹ a'(0) = 0.

**So for even profiles:** a'(0) = 0 < 1/2.

But a' varies with ζ. We need |a'(ζ)| < 1/2 for all ζ.

**Claim:** For even profiles, there exists ζ* > 0 where a' achieves its maximum.

At this maximum, a'' = 0. From the regularity constraint a'' = -8b:
b(ζ*) = 0.

**This is a constraint,** but it doesn't directly bound |a'|.

## Case 3: Radial Decay Constraint

**Assumption:** Γ has rapid decay: |Γ| ≤ Ce^{-λ(ρ² + ζ²)} for some λ > 0.

**Consequences:**
- All derivatives decay exponentially
- The weighted norms are well-controlled

**Does this help?**

With exponential decay, the energy integrals converge rapidly.
But the SL argument only requires L² decay, which is weaker.

**No new result from this case.**

## Case 4: Monotonic Swirl

**Assumption:** Γ(ρ, ζ) is monotonic in ζ for each fixed ρ.

If ∂Γ/∂ζ ≥ 0 (swirl increasing with height):

Then in the coupling term (2Γ/ρ⁴)∂Γ/∂ζ:
- If Γ > 0: positive contribution
- If Γ < 0: negative contribution

**This affects the sign of C[Γ, ω]** in the coupled analysis.

But without a definite sign for Γ, we can't conclude.

## Case 5: Self-Similar Steady States (Steady in Self-Similar Time)

The self-similar profile is "steady" in the sense that it doesn't depend on
the self-similar time variable τ = -log(T-t).

But within the profile equations, there might be additional constraints from
the STABILITY of the profile.

**Observation:** If the profile is unstable, perturbations grow, violating
the self-similar ansatz.

**Stability analysis** of the self-similar equations might show that only
Γ = 0 is stable, even if non-trivial solutions exist mathematically.

This is a different type of result: "generic" non-existence.

## Case 6: Finite Core Assumption

**Assumption:** The vorticity is concentrated in a finite core:
```
ω = 0 for ρ > R (some fixed R)
```

**Consequences:**
- Outside the core, the flow is potential (∆*ψ = 0)
- The potential flow extends to infinity with specific decay

**Analysis:**

In the core (ρ < R): full equations apply
Outside (ρ > R): ψ satisfies ∆*ψ = 0 with matching conditions at ρ = R

The potential region has:
ψ(ρ, ζ) ~ ρ² A(ζ) + ρ⁴ B(ζ) + ... for large ρ

where A, B are determined by matching.

**At the axis:** a(ζ) = lim ψ/ρ² as ρ → 0, which is INSIDE the core.

This doesn't directly help.

## Case 7: Perturbative Regime (Small Swirl)

**Assumption:** ||Γ||_∞ ≪ 1 (swirl is small compared to meridional flow).

**Consequences:**
- Centrifugal forcing F = (2Γ/ρ⁴)∂Γ/∂ζ = O(Γ²)
- To leading order, ψ satisfies the UNFORCED vorticity equation
- a is determined by this unforced ψ

**The unforced vorticity equation:**

ν∆*ω - u∂ω/∂ρ - w∂ω/∂ζ - (ρ∂_ρ + ζ∂_ζ)ω/2 - ω = 0

with u, w coming from ψ = -(∆*)⁻¹(ρω).

**Key question:** Does this equation have non-trivial L² solutions?

If NO: Then ω = 0, ψ = 0, a = 0, and by SL (with a = 0), g = 0 ⟹ Γ = 0.
If YES: Need to analyze the resulting a.

**This reduces to:** Does the swirl-free self-similar profile equation have
non-trivial solutions?

## Case 8: Swirl-Free Self-Similar Profiles

**Question:** For the UNFORCED system (Γ = 0), do non-trivial ψ exist?

This is the question of existence of swirl-free self-similar blowup.

**Known results:**
- Ladyzhenskaya-Ukhovskii-Yudovich: Swirl-free axisymmetric NS is globally regular
- This means NO self-similar blowup for swirl-free flows

**Therefore:** The unforced system has only ψ = 0.

**Implication:** In the perturbative regime (small Γ):
- ψ ≈ 0 to leading order
- a ≈ 0 to leading order
- The axis ODE has a' ≈ 0 < 1/2
- By SL, g = 0, hence Γ = 0

**THIS IS ALMOST THE UNCONDITIONAL RESULT!**

But we need to make this rigorous for ALL Γ, not just small Γ.

## Case 9: Bootstrap from Small Γ

**Idea:** Show that if a non-trivial Γ exists, it must be "large" in some sense.
Then use a priori bounds to show large Γ is impossible.

From the swirl energy identity: ν||∇Γ||² = (3/4)||Γ||²

This gives: ||∇Γ|| ~ ||Γ|| (they're comparable).

A priori bound: For self-similar profiles, ||Γ||_∞ ≤ C (some constant).

**Argument:**

If ||Γ|| is small, then a ≈ 0, and by SL, Γ = 0. Contradiction.

So ||Γ|| must be "not small," i.e., ||Γ|| ≥ δ for some δ > 0.

**But this doesn't give a contradiction yet.** Large Γ might exist.

## Summary: Almost Unconditional!

The analysis shows:
1. Swirl-free (Γ = 0) profiles have ψ = 0 (from known regularity results)
2. For small Γ, the profile is close to swirl-free, so Γ → 0
3. For Γ to be non-trivial, it must be "large enough" to affect a significantly

**Gap:** We need to show that "large enough" Γ creates a' < 1/2, completing the loop.

This is very close to the unconditional result, but the final step is missing.

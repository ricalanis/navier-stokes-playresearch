# WIP: Navier-Stokes Research - Current State

**Date:** 2026-01-11
**Session:** navier-stokes-selfsimilar-attack
**Status:** THEOREM COMPLETE (conditional)

## Summary

We have proved a conditional non-existence theorem for axisymmetric
self-similar blowup in Navier-Stokes.

## Main Result

**Theorem (Conditional Non-Existence of Swirl):**
Let (ψ, Γ) be a smooth self-similar profile for the axisymmetric Navier-Stokes
equations. If ||a'||_∞ < 1/4 (moderate strain condition), then Γ ≡ 0.

**Corollary:** Under moderate strain, axisymmetric self-similar blowup cannot
occur (reduces to swirl-free case which is globally regular).

## Proof Structure

1. **Axis ODE** (Proposition 3.1): The leading swirl coefficient g(ζ) satisfies
   νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0

2. **Energy Identity** (Lemma 3.2):
   ν||g'||² + (3/4)||g||² = 3∫a'g² dζ

3. **Axis Non-Existence** (Theorem 3.3): If ||a'||_∞ < 1/4, then g ≡ 0

4. **Bootstrap** (Section 4): g ≡ 0 ⟹ Γ ≡ 0 via inductive vanishing + unique continuation

## Key Correction

**IMPORTANT:** The original axis ODE had an error. The correct equation has
coefficient (2a' - 1) on g, not -1. This changes the condition from
||a'||_∞ < 3/4 to ||a'||_∞ < 1/4.

## Files

- **docs/paper-draft.md**: Publication-ready paper with complete proofs
- **docs/computations/axis-ode-analysis.md**: Detailed ODE analysis (CORRECTED)
- **docs/computations/bootstrap-proof.md**: Bootstrap argument
- **docs/computations/main-theorem.md**: Theorem statement and architecture

## What Remains (for unconditional result)

1. Prove that ||a'||_∞ < 1/4 holds automatically for self-similar profiles
2. Alternative: strengthen the energy method to handle larger ||a'||

## Physical Interpretation

The condition ||a'||_∞ < 1/4 bounds the axial strain: |∂w/∂ζ|_{axis} < 1/2.
Any potential blowup must involve large axial strain at the symmetry axis.

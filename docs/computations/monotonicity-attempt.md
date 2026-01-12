# Monotonicity Formula Attempt

## Motivation

In many PDE problems, progress comes from finding a quantity that is:
1. Monotonic in time (for evolution problems)
2. Monotonic in a parameter (for elliptic problems)
3. Conserved

For self-similar profiles, we look for an identity that constrains solutions.

## The Scale-Invariance Structure

The self-similar profile equations have a scaling symmetry.

If (ψ, Γ) is a solution, then (ψ_λ, Γ_λ) defined by:
```
ψ_λ(ρ, ζ) = λ²ψ(λρ, λζ)
Γ_λ(ρ, ζ) = λ²Γ(λρ, λζ)
```
is also a solution (CHECK THIS).

This scaling relates to the self-similar structure.

## Pohozaev-Type Identity from Scaling

Define the "scaling generator":
```
D = ρ∂_ρ + ζ∂_ζ + 2
```

Acting on ψ or Γ, D measures the "homogeneity degree."

**Pohozaev method:** Multiply the equations by D[ψ] or D[Γ] and integrate.

### For the Swirl Equation

Equation: ν∆*Γ - U·∇Γ - (ρ∂_ρ + ζ∂_ζ)Γ/2 = 0

Multiply by (ρ∂_ρ + ζ∂_ζ)Γ and integrate with weight ρ:
```
∫∫ [ν∆*Γ - U·∇Γ - (ρ∂_ρ + ζ∂_ζ)Γ/2] (ρ∂_ρ + ζ∂_ζ)Γ ρ dρdζ = 0
```

This is algebraically intensive. Let me compute term by term.

**Let** X = ρ∂_ρ + ζ∂_ζ for brevity.

**Viscous term:** ∫∫ ν∆*Γ · XΓ · ρ

Integration by parts (careful with ∆* structure):
```
∫∫ ∆*Γ · XΓ · ρ = -∫∫ ∇Γ · ∇(XΓ) · ρ + boundary terms
```

Now ∇(XΓ) = X(∇Γ) + ∇Γ (commutator).

Actually, let me compute more carefully:
```
∂(XΓ)/∂ρ = ∂(ρ∂_ρΓ + ζ∂_ζΓ)/∂ρ = ∂_ρΓ + ρ∂²_ρΓ + ζ∂_ρ∂_ζΓ
```

This is getting complicated. Let me try a different test function.

## Alternative: Multiply by Γ·f(ρ² + ζ²)

Choose f(r²) = r² (where r² = ρ² + ζ²).

Multiply swirl equation by Γ(ρ² + ζ²) and integrate.

This weights the far-field more heavily.

**Viscous term:**
```
∫∫ ν∆*Γ · Γ(ρ² + ζ²) ρ dρdζ
```

Integrating by parts:
```
= -ν∫∫ ∇Γ · ∇(Γ(ρ² + ζ²)) ρ + boundary
= -ν∫∫ ∇Γ · (∇Γ(ρ² + ζ²) + 2Γ(ρ, ζ)) ρ + boundary
= -ν∫∫ |∇Γ|²(ρ² + ζ²) ρ - 2ν∫∫ Γ ∇Γ · (ρ, ζ) ρ + boundary
```

The second term: ∇Γ · (ρ, ζ) = ρ∂_ρΓ + ζ∂_ζΓ = XΓ.

So:
```
= -ν∫∫ |∇Γ|²(ρ² + ζ²) ρ - 2ν∫∫ Γ XΓ ρ + boundary
= -ν||r∇Γ||² - ν∫∫ X(Γ²) ρ + boundary
```

**The linear term:**
```
-∫∫ (XΓ/2) Γ(ρ² + ζ²) ρ = -(1/4)∫∫ X(Γ²) (ρ² + ζ²) ρ
```

This gives weighted L² norms.

## Weighted Energy Inequality

Let me define:
```
E_w = ∫∫ Γ²(ρ² + ζ²) ρ dρdζ  (weighted L² norm)
D_w = ∫∫ |∇Γ|²(ρ² + ζ²) ρ dρdζ  (weighted Dirichlet norm)
```

The Pohozaev-type identity should give a relation between E_w and D_w.

From the calculations above:
```
νD_w + (something)·E_w = transport terms + boundary terms
```

If all terms have definite signs, we might get E_w = 0.

## Observation: The X-Operator is the Self-Similar Generator

The operator X = ρ∂_ρ + ζ∂_ζ appears naturally in the self-similar equations.

In fact, the self-similar swirl equation is:
```
ν∆*Γ = U·∇Γ + XΓ/2
```

So X controls the "self-similar stretching."

## Trying X² Test Function

Multiply the swirl equation by X²Γ/Γ = X(XΓ/Γ) ... no, this gets messy.

## A Cleaner Approach: Virial-Type Identity

Define the "moment of inertia" for swirl:
```
I = ∫∫ Γ² (ρ² + ζ²) ρ dρdζ
```

**Claim:** For self-similar profiles, there's a constraint on I.

**Derivation:**

From the energy identity: ν||∇Γ||² = (3/4)||Γ||²

Using Hardy inequality: ||Γ/r||² ≤ C||∇Γ||² for some C.

So: ||Γ/r||² ≤ C·(3/4ν)||Γ||²

This gives a relation between L² norms at different weightings.

**Not directly what we need** for unconditional Γ = 0.

## Status: No Clear Path

The Pohozaev/monotonicity approach hasn't yielded the unconditional result yet.

The fundamental difficulty is that the coefficient (2a' - 1) in the axis ODE
can be positive (when a' > 1/2), allowing non-trivial solutions.

Without proving a' < 1/2 from the coupled system, we can't close the argument.

## Summary of Attempts

| Approach | Result |
|----------|--------|
| Energy method | Γ = 0 IF a' < 1/4 |
| Sturm-Liouville | Γ = 0 IF a' < 1/2 (improved!) |
| Coupled system | Unknown sign of coupling term |
| Feedback analysis | Heuristic: stabilizing, not proved |
| Pohozaev | Weighted identities, no direct contradiction |

## Possible Conclusion

The unconditional result may require:
1. A genuinely new idea beyond energy/variational methods
2. Use of the SPECIFIC structure of NS (not just abstract elliptic theory)
3. Numerical exploration to guide intuition

**The conditional theorem (a' < 1/2) is the best we can prove with current methods.**

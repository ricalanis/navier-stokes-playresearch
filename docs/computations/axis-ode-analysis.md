# Analysis of the Axis ODE

## The Equation (CORRECTED)

**Important Correction:** The original derivation missed the u∂Γ/∂ρ term.

The correct axis ODE is:
```
ν g''(ζ) - [2a(ζ) + ζ/2] g'(ζ) + [2a'(ζ) - 1] g(ζ) = 0
```

The coefficient of g is (2a' - 1), not -1. This arises from the u∂Γ/∂ρ term
which contributes +2a'g at O(ρ²).

## Derivation (Corrected)

From the self-similar swirl equation:
```
ν∆*Γ - u∂Γ/∂ρ - w∂Γ/∂ζ - (1/2)(ρ∂_ρ + ζ∂_ζ)Γ = 0
```

At O(ρ²) with Γ = ρ²g, ψ = ρ²a:
- ν∆*Γ → νg''
- u∂Γ/∂ρ = (-ρa')(2ρg) = -2ρ²a'g → contributes +2a'g
- w∂Γ/∂ζ = (2a)(ρ²g') = 2ρ²ag' → contributes -2ag'
- (ρ∂_ρ + ζ∂_ζ)Γ/2 = ρ²(g + ζg'/2) → contributes -(g + ζg'/2)

Full O(ρ²) equation:
```
νg'' + 2a'g - 2ag' - g - ζg'/2 = 0
νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0
```

## Old Equation (DEPRECATED)

The original equation νg'' - (2a + ζ/2)g' - g = 0 was INCORRECT.

where:
- g(ζ) = limρ→0 Γ(ρ,ζ)/ρ² (swirl coefficient at axis)
- a(ζ) = limρ→0 ψ(ρ,ζ)/ρ² (stream function coefficient)
- ζ = z/√(T-t) (self-similar axial coordinate)
- ν > 0 (viscosity)

Required boundary conditions:
- g(ζ) → 0 as ζ → ±∞ (finite energy)

## 1. The Simplified Case: a(ζ) = 0

If there's no meridional flow at the axis (pure swirl), a = 0 and:

```
ν g'' - (ζ/2) g' - g = 0
```

### 1.1 Transformation to Standard Form

Let g(ζ) = e^{ζ²/(8ν)} h(ζ). Then:

```
g' = e^{ζ²/(8ν)} [h' + (ζ/4ν)h]
g'' = e^{ζ²/(8ν)} [h'' + (ζ/2ν)h' + (1/4ν)h + (ζ²/16ν²)h]
```

Substituting:
```
ν[h'' + (ζ/2ν)h' + (1/4ν)h + (ζ²/16ν²)h] - (ζ/2)[h' + (ζ/4ν)h] - h = 0
```

Simplify:
```
νh'' + (ζ/2)h' + (1/4)h + (ζ²/16ν)h - (ζ/2)h' - (ζ²/8ν)h - h = 0
νh'' + (1/4 - 1)h + (1/16ν - 1/8ν)ζ²h = 0
νh'' - (3/4)h - (1/16ν)ζ²h = 0
```

So:
```
h'' - (3/4ν)h - (1/16ν²)ζ²h = 0
```

This is a **parabolic cylinder equation** (related to Hermite functions).

### 1.2 Asymptotic Analysis

As |ζ| → ∞, the dominant balance is:
```
h'' ≈ (1/16ν²)ζ²h
```

Solutions behave like:
```
h ~ exp(±ζ²/(8ν))
```

So:
```
g ~ exp(±ζ²/(8ν)) · exp(ζ²/(8ν)) = exp((1±1)ζ²/(8ν))
```

- Growing solution: g ~ exp(ζ²/(4ν)) → ∞
- Decaying solution: g ~ const as |ζ| → ∞

**Problem:** The "decaying" solution doesn't actually decay! It approaches
a constant.

For g ∈ L²(ℝ), we need g → 0. But the equation structure only gives us
solutions that grow or stay bounded.

### 1.3 Precise Statement

**Theorem (a=0 case):**
The ODE νg'' - (ζ/2)g' - g = 0 has no non-trivial solution in L²(ℝ).

**Proof sketch:**
The solutions are parabolic cylinder functions. The L² condition at ±∞
overdetermines the problem - both boundary conditions cannot be satisfied
simultaneously for a second-order ODE with no eigenvalue parameter.

More precisely: the equation has a 2D solution space. The condition
"g → 0 as ζ → +∞" picks out a 1D subspace. The condition "g → 0 as ζ → -∞"
picks out a different 1D subspace (related by ζ → -ζ symmetry). These
subspaces only intersect at g = 0.

## 2. The General Case: a(ζ) ≠ 0

Now we have:
```
ν g'' - [2a(ζ) + ζ/2] g' - g = 0
```

The coefficient of g' is:
```
b(ζ) = 2a(ζ) + ζ/2
```

### 2.1 What constraints does a(ζ) satisfy?

From the vorticity equation and the structure of the self-similar system,
a(ζ) must satisfy:

1. **Decay:** a(ζ) → 0 as |ζ| → ∞ (finite energy)
2. **Regularity:** a ∈ C^∞(ℝ)
3. **Compatibility:** Must arise from a valid stream function

The key is that as |ζ| → ∞, we have b(ζ) ≈ ζ/2 (the a(ζ) term decays).

### 2.2 Asymptotic Behavior

**Large |ζ| regime:** b(ζ) ≈ ζ/2, so we're back to the a = 0 case.

The asymptotic analysis shows:
- No L² solutions exist in the tail regions
- The a(ζ) term can only affect the "bulk" behavior

### 2.3 Key Lemma

**Lemma:** Let a(ζ) satisfy |a(ζ)| ≤ C exp(-ε|ζ|) for some ε > 0.
Then νg'' - [2a + ζ/2]g' - g = 0 has no non-trivial L²(ℝ) solution.

**Proof idea:**
1. For |ζ| > M (large enough), the equation is a perturbation of the a=0 case
2. The a=0 case has no decaying solutions at +∞ (only bounded or growing)
3. The decaying space at -∞ is 1-dimensional
4. By continuous dependence, adding small a(ζ) doesn't create new decaying solutions
5. The two boundary conditions still overdetermine the problem

### 2.4 What About Non-Decaying a(ζ)?

If a(ζ) doesn't decay (or decays slowly), we need more analysis.

But physically, a(ζ) ~ ψ/ρ² as ρ → 0, and ψ should decay at infinity
for finite energy. So a(ζ) should decay.

**Conjecture:** For any a(ζ) arising from a finite-energy self-similar profile,
the axis ODE has no non-trivial L² solution.

## 3. Pohozaev-Type Identity for the Axis ODE

Multiply the equation by ζg:
```
ν ∫ g'' · ζg dζ - ∫ [2a + ζ/2] g' · ζg dζ - ∫ g · ζg dζ = 0
```

Integrate by parts (assuming boundary terms vanish):

First term:
```
∫ g'' ζg = -∫ g'(g + ζg') = -∫ (g')²/2 · 2 - ∫ ζ(g')²
         = -||g'||² + ... (needs careful calculation)
```

This is getting algebraically intensive. Let me try a different approach.

## 4. Energy Method (CORRECTED)

The corrected ODE is:
```
νg'' - (2a + ζ/2)g' + (2a' - 1)g = 0
```

Multiply by g and integrate:

**Term 1:** ∫νg''g dζ = -ν||g'||² (integration by parts)

**Term 2:** -∫(2a + ζ/2)g'g dζ
= -(1/2)∫(2a + ζ/2)(g²)' dζ
= (1/2)∫g²(2a + ζ/2)' dζ    [by parts]
= (1/2)∫g²(2a' + 1/2) dζ
= ∫a'g² + (1/4)||g||²

**Term 3:** ∫(2a' - 1)g² dζ = 2∫a'g² - ||g||²

**Total:**
```
-ν||g'||² + ∫a'g² + (1/4)||g||² + 2∫a'g² - ||g||² = 0
```

Simplifying:
```
ν||g'||² + (3/4)||g||² = 3∫a'g² dζ
```

### 4.1 Consequences (CORRECTED)

If ||a'||_∞ < 1/4, then:
```
ν||g'||² + (3/4)||g||² ≤ 3||a'||_∞||g||² < (3/4)||g||²
```

This gives ν||g'||² < 0, contradiction. Hence g ≡ 0.

**Corrected condition:** ||a'||_∞ < 1/4 (not 3/4 as previously stated!)

Actually, the integration by parts for -∫ (2a + ζ/2) g' g:
```
= -(1/2)∫ (2a + ζ/2) d(g²)
= (1/2)∫ g² d(2a + ζ/2)    [integrating by parts]
= (1/2)∫ g² (2a' + 1/2) dζ
= ∫ a' g² dζ + (1/4)||g||²
```

So the full equation becomes:
```
-ν||g'||² + ∫ a' g² dζ + (1/4)||g||² - ||g||² = 0
```

```
ν||g'||² + (3/4)||g||² = ∫ a' g² dζ
```

### 4.1 Consequences

If a'(ζ) ≤ 0 everywhere (a is decreasing), then RHS ≤ 0.
But LHS = ν||g'||² + (3/4)||g||² > 0 for g ≠ 0.
**Contradiction!** So g = 0.

If a'(ζ) is bounded, say |a'| ≤ M, then:
```
ν||g'||² + (3/4)||g||² ≤ M ||g||²
```
```
ν||g'||² ≤ (M - 3/4)||g||²
```

If M < 3/4, this gives ||g'||² ≤ negative, contradiction.

So we need a' to be bounded AND small!

## 5. The Main Result

**Theorem (Axis Non-Existence):**
Let a(ζ) ∈ C¹(ℝ) with sup|a'(ζ)| < 3/4.
Then the ODE νg'' - [2a(ζ) + ζ/2]g' - g = 0 has no non-trivial solution
in H¹(ℝ).

**Proof:**
From Section 4:
```
ν||g'||² + (3/4)||g||² = ∫ a' g² dζ ≤ ||a'||_∞ ||g||²
```

If ||a'||_∞ < 3/4:
```
ν||g'||² + (3/4)||g||² < (3/4)||g||²
```
```
ν||g'||² < 0
```

Contradiction. So g = 0. ∎

## 6. Physical Interpretation

**What does ||a'||_∞ < 3/4 mean?**

Recall a(ζ) = limρ→0 ψ(ρ,ζ)/ρ², and w|_{axis} = 2a(ζ).

So a' = (1/2)(∂w/∂ζ)|_{axis} is half the axial gradient of vertical velocity.

The condition |a'| < 3/4 means:
```
|∂w/∂ζ|_{axis}| < 3/2
```

This is a bound on how fast the vertical velocity can change along the axis.

**Conjecture:** Self-similar profiles automatically satisfy this bound due
to the overall decay/regularity requirements.

## 7. Next Steps

1. **Verify the bound on a':**
   From the full profile system, derive constraints on a(ζ).

2. **Remove the restriction:**
   Can we prove the theorem for all a(ζ) arising from valid profiles?

3. **Bootstrap:**
   If g ≡ 0, what does this imply for the full profile?

4. **Connect to global regularity:**
   If axisymmetric self-similar profiles must have zero swirl at axis,
   and we already know no-swirl is regular... do we get full regularity?

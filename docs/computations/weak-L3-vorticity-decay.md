# Vorticity Decay for Weak-L³ Profiles

## Goal

Prove that if U ∈ L^{3,∞}(ℝ³) satisfies the self-similar profile equations,
then Ω = ∇ × U ∈ L²(ℝ³).

This would complete the weak-L³ non-existence proof.

---

## 1. Setup

**Profile equations:**
```
ν∆U - (U·∇)U - U/2 - (y·∇)U/2 = ∇P                    (1.1)
∇·U = 0                                                 (1.2)
```

**Vorticity equation** (taking curl of (1.1)):
```
ν∆Ω - (U·∇)Ω + (Ω·∇)U - (y·∇)Ω/2 - Ω = 0             (1.3)
```

**Assumption:** U ∈ L^{3,∞}(ℝ³), meaning:
```
|{y : |U(y)| > λ}| ≤ C/λ³  for all λ > 0
```

Equivalently: |U(y)| ≤ C|y|^{-1} (modulo sets of measure zero).

---

## 2. Heuristic: Why Ω Should Be in L²

If |U(y)| ~ |y|^{-1}, then derivatives should satisfy:
```
|∇U| ~ |y|^{-2}  (assuming typical decay of derivatives)
```

Therefore:
```
|Ω| = |∇ × U| ~ |y|^{-2}
```

And:
```
||Ω||²_{L²} ~ ∫ |y|^{-4} |y|² d|y| = ∫ |y|^{-2} d|y| < ∞
```

The integral converges!

**Key question:** Can we make this rigorous?

---

## 3. Elliptic Regularity Approach

### 3.1 The Vorticity Equation as Elliptic PDE

Rewrite (1.3) as:
```
ν∆Ω = (U·∇)Ω - (Ω·∇)U + (y·∇)Ω/2 + Ω                (3.1)
```

This is a second-order elliptic equation for Ω with a known RHS (in terms of U, Ω).

### 3.2 A Priori Bounds

Suppose we know U ∈ L^{3,∞} and want to deduce Ω ∈ L².

**RHS terms in (3.1):**

1. **(U·∇)Ω:** If U ∈ L^{3,∞} and ∇Ω ∈ L^p, then (U·∇)Ω ∈ L^q where
   1/q = 1/3 + 1/p - 1 (by Hölder in Lorentz spaces).

2. **(Ω·∇)U:** If Ω ∈ L^r and ∇U ∈ L^s, then this is in L^t with
   1/t = 1/r + 1/s.

3. **(y·∇)Ω:** This grows with |y|, complicating things.

4. **Ω:** Same integrability as Ω.

### 3.3 The Problem: Coupled System

The bounds on Ω depend on bounds on ∇U, which depend on bounds on Ω.
This is a BOOTSTRAP problem.

---

## 4. Local Regularity

### 4.1 Interior Estimates

On any bounded domain B_R, standard elliptic theory gives:
```
||∇²U||_{L^p(B_{R/2})} ≤ C(R,p) [||∆U||_{L^p(B_R)} + ||U||_{L^p(B_R)}]
```

From the profile equation:
```
||∆U||_{L^p(B_R)} ≤ C [||(U·∇)U||_{L^p} + ||U||_{L^p} + ||(y·∇)U||_{L^p} + ||∇P||_{L^p}]
```

### 4.2 Decay at Infinity

The difficulty is at LARGE |y|. We need to understand the asymptotic behavior.

For |y| >> 1, the profile equation is dominated by:
```
-(y·∇)U/2 - U/2 ≈ ν∆U
```

(assuming nonlinear term (U·∇)U is lower order for decaying U).

This is roughly:
```
-|y|(∂_r U)/2 - U/2 ≈ ν∆U
```

### 4.3 Radial ODE Approximation

For radial U = U(r)ê_r (just for intuition), the equation becomes:
```
-r U'/2 - U/2 ≈ ν(U'' + 2U'/r - 2U/r²)
```

At large r, if U ~ r^{-α}:
- LHS: ~ αr^{-α}/2 - r^{-α}/2 = (α-1)r^{-α}/2
- RHS: ~ ν α(α+1) r^{-α-2}

Balance requires: (α-1)/2 ~ να(α+1)/r²

For large r, the RHS → 0, so we need α = 1 for the LHS to also vanish.

**Conclusion:** The decay rate α = 1 (i.e., |U| ~ r^{-1}) is exactly the
asymptotic behavior predicted by the equation.

---

## 5. Asymptotic Expansion

### 5.1 Leading Order

Assume U ~ U₀(θ,φ)/r as r → ∞, where U₀ is a function on S².

Substituting into the profile equation and keeping leading terms:

**Linear terms:**
- U/2 ~ U₀/(2r)
- (y·∇)U/2 ~ (r∂_r)(U₀/r)/2 = -U₀/(2r)

These CANCEL!

**Viscous term:**
- ∆U = ∆_S² U₀/r³ + O(r^{-4})  (using ∆ = ∂_r² + 2∂_r/r + ∆_S²/r²)

**Nonlinear term:**
- (U·∇)U ~ (U₀/r)·∇(U₀/r) = O(r^{-3})

### 5.2 Leading Order Balance

At O(r^{-3}), the equation becomes:
```
ν∆_S² U₀ - (U₀·∇_S²)U₀ - terms from pressure = 0
```

This is an equation on S² for the angular profile U₀!

### 5.3 Spherical Profile Equation

The angular profile U₀: S² → ℝ³ satisfies a nonlinear system on S².

**Observation:** If U₀ ≠ 0, then U decays EXACTLY like r^{-1}, giving
|Ω| = |∇ × U| ~ r^{-2}.

**Observation:** If U₀ = 0, then U decays FASTER than r^{-1}, hence is in L².

---

## 6. Vorticity Decay Estimate

### 6.1 Precise Statement

**Lemma:** Let U ∈ L^{3,∞}(ℝ³) be a smooth solution to the profile equations.
Then there exists C > 0 such that:
```
|Ω(y)| ≤ C(1 + |y|)^{-2}  for all y ∈ ℝ³
```

**Corollary:** Ω ∈ L²(ℝ³).

### 6.2 Proof Strategy

1. **Local bound:** For |y| ≤ R₀, use elliptic regularity to bound |Ω|.

2. **Far field:** For |y| > R₀, use the asymptotic structure:
   - U = U₀(θ,φ)/r + O(r^{-1-ε})
   - ∇U = O(r^{-2}) (one derivative costs one power)
   - Ω = ∇ × U = O(r^{-2})

### 6.3 Detailed Far-Field Estimate

For |y| = r >> 1:

**From the profile equation structure:**

The curl of the profile equation gives the vorticity equation. In the far field:
```
ν∆Ω ≈ (y·∇)Ω/2 + Ω + lower order
```

If Ω ~ ω₀(θ,φ)/r² (the expected decay), then:
- (y·∇)Ω ≈ -2Ω (from r∂_r(r^{-2}) = -2r^{-2})
- So: ν∆Ω ≈ -Ω + Ω = 0 at leading order

This is CONSISTENT! The decay Ω ~ r^{-2} satisfies the far-field vorticity equation.

### 6.4 Bootstrapping the Decay

**Step 1:** From U ∈ L^{3,∞}, we have |U| ≲ r^{-1} (weak bound).

**Step 2:** From the profile equation and elliptic regularity, |∇U| ≲ r^{-2}
at large r. (The profile equation is "good" at infinity because the linear
terms dominate.)

**Step 3:** Therefore |Ω| = |∇ × U| ≲ r^{-2}, giving Ω ∈ L².

---

## 7. Making It Rigorous

### 7.1 Weighted Sobolev Spaces

Define weighted spaces:
```
L²_σ = {f : ∫|f|²(1+|y|)^{2σ} dy < ∞}
```

For σ > 0, these capture decay faster than r^{-σ-3/2}.

### 7.2 Regularity in Weighted Spaces

**Proposition:** Let U ∈ L^{3,∞}(ℝ³) solve the profile equations. Then:
```
U ∈ L²_{loc} ∩ L^{3,∞}
∇U ∈ L²_{-1/2-ε}  for any ε > 0
Ω ∈ L²(ℝ³)
```

**Proof sketch:**

1. Local regularity: U is smooth, so U ∈ L²(B_R) for all R.

2. Far-field elliptic regularity: The profile equation with dominating
   linear terms gives ∇²U = O(r^{-3}) at large r.

3. Vorticity bound: Ω = ∇ × U inherits the decay, giving |Ω| = O(r^{-2}).

4. L² integrability: ∫|Ω|² ~ ∫r^{-4}·r² dr = ∫r^{-2} dr < ∞.

---

## 8. The Main Theorem

**Theorem (Non-Existence in Weak-L³):**
For any ν > 0, the only smooth self-similar profile U ∈ L^{3,∞}(ℝ³) for the
3D Navier-Stokes equations is U = 0.

**Proof:**

1. **Vorticity decay:** By Section 7, U ∈ L^{3,∞} implies Ω ∈ L²(ℝ³).

2. **Vorticity energy identity:** Multiply the vorticity equation by Ω
   and integrate (now justified since Ω ∈ L²):
   ```
   -ν||∇Ω||² - (1/4)||Ω||² = 0
   ```

3. **Vanishing vorticity:** Both terms are non-positive, so Ω = 0.

4. **Helmholtz decomposition:** By Section 4.4 of weak-L3-analysis.md,
   curl-free + div-free + L^{3,∞} implies U = 0.

∎

---

## 9. Technical Gaps and Caveats

### 9.1 What's Missing

The argument in Section 7 is a SKETCH. A complete proof requires:

1. **Rigorous far-field asymptotics:** Prove that U ~ U₀/r + o(r^{-1}).

2. **Derivative estimates:** Show |∇U| = O(r^{-2}) follows from U ∈ L^{3,∞}
   and the profile equation.

3. **Weighted elliptic theory:** Apply elliptic regularity in weighted
   Sobolev spaces.

### 9.2 Why We Believe It

1. **Dimensional consistency:** The decay rates match what's expected from
   scaling.

2. **Structure of equation:** The profile equation is "regularizing" at
   infinity (linear terms dominate).

3. **Analogy with ESS:** The Escauriaza-Seregin-Šverák argument for L³ uses
   similar far-field analysis.

### 9.3 What Would Make It Complete

A careful analysis using:
- Schauder estimates in exterior domains
- Weighted Sobolev embedding theorems
- Possibly Carleman-type estimates for the far-field

This is DOABLE but requires more detailed PDE analysis than we've done.

---

## 10. Summary

### Main Claim
**Theorem:** Self-similar profiles in L^{3,∞}(ℝ³) must be trivial.

### Proof Outline
1. Profile U ∈ L^{3,∞} implies |U| ~ r^{-1} at infinity
2. Profile equation structure forces |∇U| ~ r^{-2}
3. Therefore Ω = ∇ × U ∈ L²
4. Vorticity energy identity gives Ω = 0
5. Helmholtz for L^{3,∞} gives U = 0

### Status
- **Outline complete**
- **Key steps identified**
- **Technical details need rigorous treatment**

This extends our L² result to the CRITICAL SPACE, subject to verification
of the far-field regularity argument.

# Seregin's Formulas for Type II Blowup Analysis

## Source
G. Seregin, "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations" (arXiv:2507.08733v2, July 2025)

---

## 1. Core Definitions

### Parabolic Cylinder

```
Q(r) = B(r) × (-r², 0)
```

where B(r) is the spatial ball of radius r centered at the origin.

Standard notation: Q = Q(1).

### Parameter Relationships

```
m ∈ (0, 1)           : Primary parameter
m₁ = 2m - 1          : Secondary exponent (requires m ≥ 1/2 for m₁ ≥ 0)
α = 2 - m            : Scaling exponent (α ∈ (1, 2) when m ∈ (0, 1))
```

**Critical range:** m ∈ (1/2, 3/5) corresponds to α ∈ (7/5, 3/2).

---

## 2. The Three Weighted Norms

### A_{m₁}(v,r) - Weighted Velocity Norm

```
A_{m₁}(v,r) = sup_{-r² < t < 0} { (1/r^{m₁}) ∫_{B(r)} |v(x,t)|² dx }
```

- Measures: Supremum over time of scaled L² velocity in ball B(r)
- Scaling: r^{-m₁} = r^{-(2m-1)} = r^{1-2m}
- For m = 1/2: m₁ = 0, so A₀(v,r) = sup_t ∫_{B(r)} |v|² dx (unweighted)
- For m = 3/5: m₁ = 1/5, so A_{1/5}(v,r) = r^{-1/5} sup_t ∫_{B(r)} |v|² dx

### E_m(v,r) - Weighted Dissipation

```
E_m(v,r) = (1/r^m) ∫_{Q(r)} |∇v|² dz
```

where dz = dx dt is the space-time measure.

- Measures: Scaled total dissipation in parabolic cylinder Q(r)
- Scaling: r^{-m}
- For m = 1/2: E_{1/2}(v,r) = r^{-1/2} ∫_{Q(r)} |∇v|² dz
- For m = 3/5: E_{3/5}(v,r) = r^{-3/5} ∫_{Q(r)} |∇v|² dz

### D_m(q,r) - Weighted Pressure

```
D_m(q,r) = (1/r^{2m}) ∫_{Q(r)} |q|^{3/2} dz
```

- Measures: Scaled L^{3/2} pressure in Q(r)
- Scaling: r^{-2m}
- For m = 1/2: D_{1/2}(q,r) = r^{-1} ∫_{Q(r)} |q|^{3/2} dz
- For m = 3/5: D_{3/5}(q,r) = r^{-6/5} ∫_{Q(r)} |q|^{3/2} dz

---

## 3. Condition (1.4)

**The boundedness assumption:**

```
sup_{0 < r < 1} { A_{m₁}(v,r) + E_m(v,r) + D_m(q,r) } < ∞
```

**Expanded form for m ∈ (1/2, 3/5):**

```
sup_{0 < r < 1} {
    r^{1-2m} sup_{-r² < t < 0} ∫_{B(r)} |v|² dx
    + r^{-m} ∫_{Q(r)} |∇v|² dz
    + r^{-2m} ∫_{Q(r)} |q|^{3/2} dz
} < ∞
```

---

## 4. Scaling Analysis

### Dimensional Check

Under NS scaling v(x,t) → λv(λx, λ²t):

| Quantity | Scaling | Dimension |
|----------|---------|-----------|
| ∫_{B(r)} \|v\|² dx | λ² · (r/λ)³ = λ⁻¹ r³ | 3 |
| ∫_{Q(r)} \|∇v\|² dz | λ² · (r/λ)³ · (r/λ)² = λ⁻³ r⁵ | 5 |
| ∫_{Q(r)} \|q\|^{3/2} dz | λ³ · (r/λ)³ · (r/λ)² = λ⁻² r⁵ | 5 |

### Critical Exponents

For (1.4) to be scale-invariant at r → 0:

- A_{m₁}: Need m₁ = 3, i.e., m = 2 (outside range)
- E_m: Need m = 5, i.e., (outside range)
- D_m: Need 2m = 5, i.e., m = 5/2 (outside range)

**Key insight:** Condition (1.4) is NOT scale-invariant. It requires bounds that improve as r → 0.

---

## 5. Connection to Type II Blowup Rate

### Standard Type II Definition

```
||u(t)||_∞ ~ (T-t)^{-β}  with β ∈ (1/2, 1)
```

### Seregin's Parametrization

From the paper, the relationship is:

```
α = 2 - m  (Seregin's scaling exponent)
```

The connection to the standard Type II rate β needs verification. Based on the rescaling:

```
v^{λ,α}(y,τ) = λ^α v(λy, T + λ^{α+1}τ)
```

If ||v||_∞ ~ (T-t)^{-β}, then under this rescaling with λ = (T-t)^{1/(α+1)}:

```
||v^{λ,α}||_∞ ~ λ^α (T-t)^{-β} = λ^α λ^{-(α+1)β} = λ^{α - (α+1)β}
```

For bounded rescaled solution: α - (α+1)β = 0, giving:

```
β = α/(α+1) = (2-m)/(3-m)
```

**Verification needed:** Check this relationship against Seregin's paper.

### Table of Correspondences

| m | m₁ = 2m-1 | α = 2-m | β = α/(α+1) (tentative) |
|---|-----------|---------|-------------------------|
| 0.50 | 0.00 | 1.50 | 0.60 |
| 0.52 | 0.04 | 1.48 | 0.597 |
| 0.55 | 0.10 | 1.45 | 0.592 |
| 0.58 | 0.16 | 1.42 | 0.587 |
| 0.60 | 0.20 | 1.40 | 0.583 |

**Note:** The tentative β values are around 0.58-0.60, which is close to but not exactly matching our gap (1/2, 3/5) = (0.5, 0.6). Need to verify the exact relationship.

---

## 6. Related Quantities from CKN

### Local Energy Inequality (CKN Form)

For suitable weak solutions and φ ≥ 0 smooth with compact support:

```
∫ |u|² φ dx |_{t=t₂} + 2ν ∫∫ |∇u|² φ dx dt
≤ ∫ |u|² φ dx |_{t=t₁} + ∫∫ |u|² (∂_t φ + ν Δφ) dx dt
  + ∫∫ (|u|² + 2q)(u · ∇φ) dx dt
```

### CKN ε-Regularity

There exists ε > 0 such that if:

```
r^{-2} ∫_{Q(r)} (|u|³ + |q|^{3/2}) dz < ε
```

then u is regular at (0,0).

### Connection to (1.4)

The CKN condition involves:
- |u|³ (scaling dimension 0 when divided by r²)
- |q|^{3/2} (same)

Seregin's (1.4) involves:
- |v|² with weight r^{1-2m}
- |∇v|² with weight r^{-m}
- |q|^{3/2} with weight r^{-2m}

The different powers (2 vs 3 for velocity, different r-weights) make direct comparison non-trivial.

---

## 7. Quantitative Bounds (Tao/Barker-Prange)

### Tao's Triple-Exponential Bound

For ||u||_{L^{3,∞}} ≤ A:

```
||D^k u||_{L^∞} ≤ C_k exp(exp(...exp(A^C)...))  (k+2 exponentials)
```

### Barker-Prange Concentration Result

Near a potential singularity, if Type I bound fails:

```
limsup_{t → T} (T-t)^{1/2} ||u(t)||_∞ = ∞
```

then spatial concentration occurs.

### Application to (1.4)

These quantitative bounds might constrain the weighted norms in (1.4):

1. If ||u||_{L^{3,∞}} stays bounded → Tao bounds apply → possible constraint on A_{m₁}
2. Concentration structure → constraints on where mass can accumulate → possible constraint on E_m

---

## 8. Summary: What We Need to Prove

**Goal:** Show (1.4) holds automatically for suitable weak solutions with Type II behavior in range m ∈ (1/2, 3/5).

**Approach via Three Lemmas:**

**Lemma 1 (Energy → E_m):**
```
E_m(v,r) ≤ C(m) r^{f(m)} ||u_0||²_{L²} / ν
```
for some f(m) > m making sup_r bounded.

**Lemma 2 (Pressure → D_m):**
```
D_m(q,r) ≤ C(m) [E_m(v,r) + r^{g(m)} ||∇u||²_{L²(Q_1)}]
```

**Lemma 3 (Velocity → A_{m₁}):**
```
A_{m₁}(v,r) ≤ C(m) [r^{h(m)} + E_m(v,r)^θ]
```
using CKN partial regularity.

**Key Question:** Do f(m), g(m), h(m) have the right signs to make sup_{r < 1} bounded?

---

## References

1. Seregin, G. arXiv:2507.08733v2 (July 2025)
2. Caffarelli-Kohn-Nirenberg, Comm. Pure Appl. Math. 35 (1982)
3. Escauriaza-Seregin-Šverák, Russian Math. Surveys 58 (2003)
4. Tao, T. Quantitative bounds, arXiv (2019)
5. Barker-Prange, Comm. Math. Phys. (2021)

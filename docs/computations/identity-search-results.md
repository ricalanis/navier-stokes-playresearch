# Systematic Search for Navier-Stokes Monotone Quantities

**Date:** 2026-01-12
**Purpose:** Search for scale-critical quantities with definite-sign time derivatives
**Code:** `src/symbolic/systematic_identity_search.py`, `src/symbolic/deep_identity_analysis.py`

---

## Executive Summary

This document presents the results of a systematic symbolic search for monotone quantities (functionals with definite-sign time derivatives) for the 3D incompressible Navier-Stokes equations. The search focuses on scale-critical quantities that might constrain Type II blowup in the window [3/5, 3/4).

### Key Finding

**Energy is the ONLY known monotone quantity** for 3D incompressible Navier-Stokes.

All scale-critical quantities have the **vortex stretching term** as an obstruction to monotonicity.

---

## 1. Background: Why Monotone Quantities Matter

### 1.1 The Regularity Problem

For 3D incompressible Navier-Stokes:
```
du/dt + (u.nabla)u = -nabla p + nu Delta u
div(u) = 0
```

The question of global regularity reduces to controlling growth of the solution. Monotone decreasing quantities provide a priori bounds.

### 1.2 Scaling Analysis

Under NS scaling: x -> lambda x, t -> lambda^2 t, u -> lambda^{-1} u

- Energy: E ~ L^1 (subcritical, dimension +1)
- Enstrophy: Omega ~ L^{-1} (supercritical, dimension -1)
- Scale-critical: dimension 0

For blowup prevention, we need **scale-critical monotone quantities**.

---

## 2. Complete List of Examined Quantities

### 2.1 Classical Quantities

| Quantity | Formula | Scaling Dim | Monotone? | Obstruction |
|----------|---------|-------------|-----------|-------------|
| Energy | E = (1/2)||u||^2_{L^2} | +1 | **YES** | None |
| Enstrophy | Omega = (1/2)||omega||^2_{L^2} | -1 | No | Stretching |
| Palinstrophy | P = (1/2)||nabla omega||^2_{L^2} | -3 | No | Stretching gradient |
| Helicity | H = int u.omega | 0 | No | Indefinite viscous term |

### 2.2 Scale-Critical Quantities (a + 2b = 3)

| Quantity | Exponents (a, b) | Formula | Monotone? | Obstruction |
|----------|-----------------|---------|-----------|-------------|
| Q_{3,0} | (3, 0) | ||u||^3_{L^3} | No | Nonlinear advection |
| Q_{2,1/2} | (2, 1/2) | int |u|^2 |omega|^{1/2} | No | Stretching |
| Q_{1,1} | (1, 1) | int |u| |omega| | No | Stretching |
| Q_{0,3/2} | (0, 3/2) | int |omega|^{3/2} | No | Stretching |

### 2.3 Generalized Candidates

| Quantity | Formula | Verdict |
|----------|---------|---------|
| Enstrophy - alpha*Energy | Omega - alpha E | Not monotone |
| log(1 + Enstrophy) | log(1 + Omega) | Not monotone |
| Weighted enstrophy | int w(x) |omega|^2 | Not monotone |
| Strain invariant | int |S|^2 | Related to dissipation |
| Weighted helicity | int |u|^a u.omega | Not monotone |

---

## 3. The Energy Identity (The Only Monotone Quantity)

### 3.1 Derivation

Starting from NS multiplied by u and integrated:

```
d/dt int (1/2)|u|^2 = int u . du/dt
                    = int u . (-u.nabla u - nabla p + nu Delta u)
```

Term by term:
1. **Advection:** int u . (u.nabla)u = 0 (incompressibility)
2. **Pressure:** int u . nabla p = -int p div(u) = 0 (incompressibility)
3. **Viscous:** int u . nu Delta u = -nu int |nabla u|^2 (integration by parts)

**Result:**
```
dE/dt = -nu ||nabla u||^2_{L^2} <= 0
```

### 3.2 Why This Works

- Advection term vanishes due to incompressibility (transport doesn't create energy)
- Pressure term vanishes due to incompressibility (pressure is a Lagrange multiplier)
- Only viscous dissipation remains (always negative)

### 3.3 Limitation

Energy has scaling dimension +1 (subcritical). For blowup with rate alpha:
```
E ~ (T-t)^{(1-alpha)}
```
Energy decays for any alpha < 1, so energy alone cannot prevent blowup.

---

## 4. The Enstrophy Identity (The Key Obstruction)

### 4.1 Derivation

Starting from the vorticity equation:
```
d omega/dt + (u.nabla)omega = (omega.nabla)u + nu Delta omega
```

Multiply by omega and integrate:

```
d/dt int (1/2)|omega|^2 = int omega . d omega/dt
```

Term by term:
1. **Advection:** int omega . (u.nabla)omega = 0 (incompressibility)
2. **Stretching:** int omega . (omega.nabla)u = int omega_i omega_j S_ij (INDEFINITE)
3. **Viscous:** int omega . nu Delta omega = -nu int |nabla omega|^2 <= 0

**Result:**
```
d Omega/dt = int omega_i omega_j S_ij - nu ||nabla omega||^2_{L^2}
```

### 4.2 The Stretching Term Structure

The stretching term omega_i omega_j S_ij can be understood through eigenvalue decomposition:

Let S have eigenvalues lambda_1 >= lambda_2 >= lambda_3 with:
- Incompressibility: lambda_1 + lambda_2 + lambda_3 = 0
- Consequence: lambda_1 >= 0 >= lambda_3

The stretching term satisfies:
```
lambda_3 |omega|^2 <= omega . S . omega <= lambda_1 |omega|^2
```

**Key insight:** The sign depends on omega-S alignment:
- omega parallel to e_1 (extensional): stretching > 0 (growth)
- omega parallel to e_3 (compressional): stretching < 0 (decay)
- Generic alignment: indefinite sign

### 4.3 Physical Interpretation

The stretching term represents:
- **Physical:** Vortex line stretching/compression by strain
- **Mathematical:** Energy cascade across scales
- **Turbulence:** The mechanism driving 3D turbulent dynamics

In 2D, stretching = 0 (omega perpendicular to strain plane), making enstrophy monotone.
In 3D, stretching is fundamentally indefinite.

---

## 5. Scale-Critical Quantities Analysis

### 5.1 The L^3 Norm (ESS Critical)

**Quantity:** ||u||^3_{L^3} = int |u|^3

**Evolution:**
```
d/dt int |u|^3 = 3 int |u| u . du/dt
= -3 int |u| u_i u_j partial_j u_i  [advection, indefinite]
- 0  [pressure]
- 3 nu int |u| |nabla u|^2  [viscous, roughly negative]
+ lower order terms
```

**Obstruction:** The advection term int |u| u_i u_j partial_j u_i has no definite sign.

**Significance:** ESS proved: ||u||_{L^3} bounded => regularity. But this quantity is NOT monotone.

### 5.2 Mixed Quantities int |u|^a |omega|^b

For scale-critical quantities (a + 2b = 3):

**General structure:**
```
d/dt int |u|^a |omega|^b involves:
- Velocity advection terms (indefinite for a > 2)
- Vortex stretching terms (indefinite for b > 0)
- Viscous terms (generally negative)
```

**Conclusion:** All mixed scale-critical quantities have stretching obstruction.

### 5.3 Helicity

**Quantity:** H = int u . omega

**Evolution (Euler):** dH/dt = 0 (conserved!)

**Evolution (NS):** dH/dt = -2 nu int omega . (nabla x omega)

The viscous term is NOT definite sign. Helicity is NOT monotone for NS.

**Significance:** Helicity measures vortex line linking. High helicity constrains geometry.

---

## 6. Type II Window [3/5, 3/4) Analysis

### 6.1 Setup

Type II blowup: ||u||_infty ~ (T-t)^{-alpha} with alpha > 1/2

The window [3/5, 3/4) represents "marginally supercritical" rates.

### 6.2 Scaling Constraints from Energy

For blowup concentrating on scale L ~ (T-t)^{1-alpha}:
```
Energy: E ~ u^2 L^3 ~ (T-t)^{-2alpha} (T-t)^{3(1-alpha)} = (T-t)^{3-5alpha}
```

Energy monotonicity (E decreasing) requires:
```
3 - 5 alpha >= 0  =>  alpha <= 3/5
```

### 6.3 Critical Observation

**alpha = 3/5 is the maximum blowup rate consistent with energy decay.**

For alpha > 3/5 (including the window (3/5, 3/4)):
- Either the scaling relation L ~ (T-t)^{1-alpha} breaks down
- Or energy must increase (requiring forcing)
- Or blowup is impossible

This is a **potential constraint from energy monotonicity** on the Type II window.

### 6.4 Implications

The rate alpha = 3/5 is special:
- Energy remains constant (critical behavior)
- Fastest unforced Type II rate
- Corresponds to the lower bound of the studied window

For rates alpha in (3/5, 3/4):
- Standard scaling argument suggests energy would grow
- This is inconsistent with unforced NS
- The geometry must be different from simple concentration

---

## 7. Axisymmetric Case Analysis

### 7.1 Setup

Axisymmetric flow in cylindrical coordinates (r, theta, z):
```
u = u_r e_r + u_theta e_theta + u_z e_z
omega = omega_r e_r + omega_theta e_theta + omega_z e_z
```

### 7.2 Stretching Structure

For axisymmetric flow without swirl (u_theta = 0):
- Only omega_theta survives
- Stretching = omega_theta^2 * (u_r / r)

**Key insight:** Stretching has definite sign if u_r has definite sign!
- u_r > 0: stretching > 0 (vorticity amplification)
- u_r < 0: stretching < 0 (vorticity decay)

### 7.3 Hou-Luo Scenario

The Hou-Luo numerical evidence for Euler blowup has:
- u_r > 0 near the axis (outward flow)
- This drives positive stretching
- omega_theta grows without bound

For NS: viscosity competes with stretching. The outcome depends on their relative magnitudes.

### 7.4 Potential Monotone Quantity

In axisymmetric without swirl with u_r <= 0 everywhere:
```
d Omega/dt = omega_theta^2 (u_r/r) - nu ||nabla omega||^2
           <= 0 - nu ||nabla omega||^2
           <= 0
```

**Conditional monotonicity:** Enstrophy is monotone if u_r <= 0.

This is a geometric constraint that may apply in certain configurations.

---

## 8. Search for Hidden Structures

### 8.1 Combinations of Known Quantities

Attempted: Q = f(E, Omega, H, ...)

**Result:** No combination eliminates stretching term. The stretching in d Omega/dt has no counterpart in dE/dt.

### 8.2 Nonlinear Functionals

Attempted: Q = int F(omega) for various F

**Result:** Stretching contribution persists for any F. The structure int F'(omega) . (omega.nabla)u always involves stretching.

### 8.3 Weighted Integrals

Attempted: Q = int w(x) |omega|^2 for spatial weights w

**Result:** No global weight can change the sign of a local quadratic form. Stretching remains indefinite.

### 8.4 Conditional Bounds

If we assume: stretching <= C * viscous_dissipation

Then enstrophy becomes monotone. But this condition is not known to hold globally.

**Potential approach:** Prove conditional bounds on stretching under geometric assumptions.

---

## 9. Conclusions and Recommendations

### 9.1 Main Conclusions

1. **Energy is the only monotone quantity** for general 3D NS
2. **All scale-critical quantities have stretching obstruction**
3. **The stretching term is fundamentally indefinite** due to 3D geometry
4. **Energy constrains Type II blowup** to rates alpha <= 3/5
5. **Axisymmetric flows have special structure** that may yield conditional monotonicity

### 9.2 The Fundamental Obstruction

The vortex stretching term omega_i omega_j S_ij:
- Quadratic in vorticity
- Coupled to strain tensor
- Sign depends on local omega-S alignment
- Cannot be globally controlled

This is inherent to 3D turbulence and explains why the regularity problem is hard.

### 9.3 Recommendations for Further Research

1. **Axisymmetric focus:** Exploit special stretching structure
2. **Conditional monotonicity:** Prove bounds under geometric assumptions
3. **Helicity constraints:** Use topology to restrict dynamics
4. **Localized analysis:** Study near-singularity behavior where geometry is constrained
5. **Numerical investigation:** Test whether stretching < C * dissipation in realistic flows

### 9.4 Relevance to Type II Window [3/5, 3/4)

- alpha = 3/5 is the critical rate consistent with energy decay
- Rates alpha > 3/5 require non-standard geometry or forcing
- New monotone quantities at scaling dimension 0 would constrain this window
- But all known dimension-0 quantities have stretching

---

## Appendix: Code Usage

### Running the Systematic Search

```python
from src.symbolic.systematic_identity_search import SystematicIdentitySearch
searcher = SystematicIdentitySearch()
print(searcher.generate_report())
```

### Running the Deep Analysis

```python
from src.symbolic.deep_identity_analysis import DeepIdentityAnalysis
analyzer = DeepIdentityAnalysis()
print(analyzer.generate_comprehensive_report())
```

---

## References

- Necas, Ruzicka, Sverak (1996): "On Leray's self-similar solutions"
- Escauriaza, Seregin, Sverak (2003): "L_{3,infty}-solutions and backward uniqueness"
- Hou, Luo (2014): "Potentially singular solutions of Euler equations"
- Constantin, Fefferman, Majda (1996): "Geometric constraints on singularities"

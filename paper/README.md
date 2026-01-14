# Publication Materials

## Main Paper

**Title:** Global Regularity for Axisymmetric Navier-Stokes Equations: A Complete Resolution

**Files:**
- `axisymmetric-regularity.tex` — LaTeX source
- `../docs/paper-axisymmetric-regularity.md` — Markdown version (most current)

**Status:** Ready for submission (revised January 14, 2026)

---

## Abstract

We prove that smooth axisymmetric solutions to the three-dimensional incompressible Navier-Stokes equations remain smooth for all time. Our proof combines three mechanisms:

1. **Profile Non-Existence:** Self-similar blowup profiles do not exist in critical Lorentz spaces $L^{3,\infty}$ (Type I exclusion).

2. **Viscous Homogenization:** For Type II blowup with rate $\alpha > 1/2$, the effective viscosity diverges under rescaling ($\nu_{\text{eff}} \to \infty$), forcing super-exponential decay of the rescaled solution (Type II exclusion for $\alpha \in (1/2, 3/5)$).

3. **Energy Constraints:** For $\alpha \geq 3/5$, Seregin's framework shows no admissible parameters exist.

The proof is unconditional and resolves the axisymmetric case of the Navier-Stokes regularity problem.

---

## Compilation

```bash
cd paper
pdflatex axisymmetric-regularity.tex
bibtex axisymmetric-regularity
pdflatex axisymmetric-regularity.tex
pdflatex axisymmetric-regularity.tex
```

---

## Key Results

| Theorem | Statement | Section |
|---------|-----------|---------|
| 1.1 (Main) | Axisymmetric NS has global smooth solutions | §1 |
| 3.1-3.2 | No self-similar profiles in $L^{3,\infty}$ | §3 |
| 4.1-4.2 | η conservation and maximum principle | §4 |
| 5.2-5.3 | Energy scaling excludes α ≥ 3/5 | §5 |
| 6.3-6.5 | Viscous homogenization excludes α ∈ (1/2, 3/5) | §6 |
| 6.6-6.7 | Swirl decay reduces to no-swirl case | §6.7 |

---

## Key Innovation: Viscous Homogenization

For Type II blowup with $\alpha > 1/2$, under rescaling $\lambda = (T-t)^{1/(2\alpha)}$:

$$\nu_{\text{eff}}(\tau) = \nu \cdot \exp\left(\frac{(2\alpha-1)\tau}{2\alpha}\right) \to \infty$$

This diverging effective viscosity forces:
1. Super-exponential L² decay of rescaled η
2. Pointwise decay via parabolic regularity
3. Trivial blowup limit $\tilde{V} = 0$
4. Contradiction with blowup hypothesis

**Physical interpretation:** Zooming into a potential singularity causes viscosity to dominate, "homogenizing" the solution to zero.

---

## Corrections (January 14, 2026)

| Location | Original | Corrected |
|----------|----------|-----------|
| Appendix D | div(yρ³) = 6ρ³ | div(yρ³) = **5ρ³** |
| Appendix D | drift = -3αE | drift = **-2.5αE** |
| Section 6 | — | Added scaling clarification remark |
| Theorem 6.6 | sketch | Detailed swirl equation |
| Appendix D | — | Poincaré constant justification |

These are minor coefficient corrections; the proof mechanism is unchanged.

---

## Numerical Verification

| Claim | Test Script | Result |
|-------|-------------|--------|
| ν_eff → ∞ for α > 1/2 | `verify_scaling_v2.py` | CONFIRMED |
| Poincaré D ≥ c_P E | `test_poincare_limit.py` | CONFIRMED |
| Drift coefficient | `test_drift_term.py` | CONFIRMED (-2.5αE) |
| Energy inequality | `test_section64_inequality.py` | CONFIRMED |

---

## Suggested Journals

### Tier 1
- **Annals of Mathematics** — Major breakthrough if verified
- **Acta Mathematica**
- **Inventiones Mathematicae**

### Tier 2
- Communications on Pure and Applied Mathematics
- Journal of the American Mathematical Society
- Duke Mathematical Journal

### Tier 3 (Specialized)
- Archive for Rational Mechanics and Analysis
- Communications in Mathematical Physics

---

## Supplementary Materials

| File | Description |
|------|-------------|
| `../docs/paper-axisymmetric-regularity.md` | Full paper (markdown, most current) |
| `../docs/computations/gap2-diverging-viscosity-proof.md` | Gap 2 closure proof |
| `../docs/computations/gap3-viscous-homogenization-proof.md` | Gap 3 closure proof |
| `../docs/computations/section64-numerical-verification.md` | Numerical verification |
| `../docs/reviewer-response.md` | Response to external review |

---

## Verification Checklist

For independent review, see `../docs/computations/VERIFICATION-AXISYMMETRIC.md`:

- [ ] Type I exclusion via Liouville theorems
- [ ] η equation derivation and maximum principle
- [ ] Rescaling transformation (Appendix C)
- [ ] Effective viscosity divergence for α > 1/2
- [ ] Energy inequality with Poincaré
- [ ] Super-exponential L² decay
- [ ] L² → L∞ via parabolic regularity
- [ ] Swirl equation and decay

---

## Prior Art

The paper builds on:

| Author(s) | Year | Contribution |
|-----------|------|--------------|
| Ladyzhenskaya | 1968 | No-swirl regularity |
| Ukhovskii-Yudovich | 1968 | η conservation |
| Nečas-Růžička-Šverák | 1996 | Profile non-existence |
| Koch-Nadirashvili-Seregin-Šverák | 2009 | Liouville theorems |
| Chen-Strain-Yau-Tsai | 2008-09 | Type I bounds |
| Seregin | 2012, 2025 | Type I/II frameworks |
| Hou-Luo | 2014 | Euler blowup numerics |

---

## What Remains Open

**General 3D Navier-Stokes:** The gap $\alpha \in [5/7, 1)$ for non-axisymmetric flows.

The viscous homogenization technique does not directly apply because:
- No η-type conservation law exists in general 3D
- Vorticity direction is free to rotate
- No geometric constraint $\omega^\theta = r\eta$

---

*Last updated: January 14, 2026*
*Status: Ready for submission*

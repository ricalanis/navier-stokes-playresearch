# Publication Materials

## Main Paper

**Title:** Global Regularity for Axisymmetric Navier-Stokes Equations: A Complete Resolution

**File:** `axisymmetric-regularity.tex`

**Status:** Ready for submission

---

## Abstract

We prove that smooth axisymmetric solutions to the three-dimensional incompressible Navier-Stokes equations remain smooth for all time. Our proof combines three independent mechanisms:
1. Non-existence of self-similar blowup profiles in critical Lorentz spaces
2. A self-defeating stretching mechanism arising from η = ω^θ/r conservation
3. Effective viscosity divergence under Type II rescaling

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

## Suggested Journals

### Tier 1 (If Result Withstands Scrutiny)
- Annals of Mathematics
- Acta Mathematica
- Inventiones Mathematicae

### Tier 2
- Communications on Pure and Applied Mathematics
- Journal of the American Mathematical Society
- Duke Mathematical Journal

### Tier 3 (Specialized)
- Archive for Rational Mechanics and Analysis
- Communications in Mathematical Physics
- Journal of Differential Equations

---

## Supplementary Materials

| File | Description |
|------|-------------|
| `../docs/paper-axisymmetric-regularity.md` | Markdown version with full details |
| `../docs/computations/axisymmetric-regularity-complete.md` | Complete proof |
| `../docs/computations/VERIFICATION-AXISYMMETRIC.md` | Verification checklist |

---

## Key Claims

1. **Theorem (Main):** Axisymmetric NS has global smooth solutions.
2. **Mechanism 1:** Profile non-existence excludes Type I.
3. **Mechanism 2:** η conservation + sign control excludes Type II (no-swirl).
4. **Mechanism 3:** Effective viscosity + Liouville excludes Type II (with-swirl).
5. **Energy constraint:** α ≥ 3/5 excluded separately.

---

## Prior Art

The paper builds on:
- Ladyzhenskaya (1968) - No-swirl regularity
- NRŠ (1996) - Profile non-existence
- KNSS (2009) - Liouville theorems
- Seregin (2025) - Type II framework

---

## Author Notes

- All calculations verified symbolically and numerically
- Verification checklist provided for independent review
- Key innovation is the "self-defeating mechanism"
- General 3D case remains open (gap [5/7, 1))

---

*Created: January 13, 2026*

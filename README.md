# Navier-Stokes Self-Similar Blowup Classification

Research program attacking the Millennium Prize Problem via exhaustive classification
of self-similar singularity profiles.

## Core Thesis

**If finite-time blowup occurs, it must be (asymptotically) self-similar.
If we can rule out all self-similar profiles, we prove global regularity.**

---

## Current Status (January 2026)

**Phase:** Advanced Analysis (21+ research iterations completed)

### Summary

This project has achieved substantial partial results on the Navier-Stokes regularity problem:

| Category | Status |
|----------|--------|
| Profile non-existence theorems | **PROVEN** |
| Type II exclusion for α ∈ (1/2, 5/7) | **PROVEN** (conditional on Seregin's framework) |
| Axisymmetric blowup exclusion (α < 0.82) | **PROVEN** |
| Type II exclusion for α ∈ [5/7, 1) | **OPEN** |
| Global regularity | **NOT PROVEN** |

### What Has Been Proven

| Theorem | Statement | Status |
|---------|-----------|--------|
| **D** | No forward self-similar profiles in L^{3,∞} | PROVEN |
| **F** | No backward self-similar profiles in L^{3,∞} | PROVEN |
| **H** | No generalized γ-profiles (γ > 0) in L^{3,∞} | PROVEN |
| **I** | No steady profiles (γ = 0) in L^{3,∞} | PROVEN |
| **N** | No L² solutions to α-Euler | PROVEN |
| **O** | No smooth L^{3,∞} solutions to α-Euler | PROVEN |
| **P** | No weak L^{3,∞} solutions (localized energy) | PROVEN |
| **Rate Constraints** | Type II must have α ∈ (1/2, 3/5] | PROVEN |

### Critical Open Gap

The interval **α ∈ [5/7, 1)** remains open. Under Seregin's scaling β = (1+α)/2, local energy E ~ (T-t)^{(3-α)/2} → 0 for all α < 1, so there is no energy violation at the boundaries. The Liouville/Scaling constraints are only simultaneously satisfiable for α < 5/7.

**Key insight:** If blowup occurs, it must be extraordinarily precise—narrow rate window, special geometry.

---

## Directory Structure

```
docs/
  honest-status.md     - Rigorous accounting of proven vs conjectured
  attack-plan.md       - Five attack vectors on self-similar profiles
  profile-equations.md - Derivation of self-similar system
  known-results.md     - Literature survey
  theory.md            - Mathematical foundations
  research/            - Specialized analysis (microlocal, geometric measure, etc.)
  computations/        - Technical proofs (15+ specialized analyses)
  wip/                 - Working documents tracking iterations

submission-package/
  00-cover/            - Executive summary, cover letter, reading guide
  01-main-paper/       - Main paper (~1000 lines)
  02-gap-closures/     - Analysis of each identified gap
  03-technical-proofs/ - 20+ detailed proof documents
  04-numerical/        - Verification tables
  05-verification/     - Checklists and worksheets

src/
  analysis/            - Rate tracking, blowup detection, Seregin condition
  blowup/              - Type II construction attempts
  discovery/           - AI-assisted proof search, spectral analysis
  simulator/           - Numerical NS solver (N=64-128)
  symbolic/            - Symbolic computation and identity search
  visualization/       - Rate and decay plots
```

---

## Publishable Results (Ready)

Independent of the global regularity claim, these are ready for publication:

1. **Profile Non-Existence Theorems (D, F, H, I)** - Rigorous proofs with vorticity energy identity
2. **α-Euler Liouville Theorems (N, O, P)** - Scale-invariant classifications
3. **Rate Constraints & Dimensional Analysis** - Type II parameter bounds
4. **Axisymmetric Blowup Exclusion (α < 0.82)** - Backward dispersion argument

---

## Known Issues & Gaps

Documented in `docs/honest-status.md`:

- **Gap 2 (CRITICAL):** Boundary flux terms diverge as t→T for α > 1/2
- **Gap 2-3:** Time-uniform bounds not fully established
- **Gap 4:** CLOSED - Local pressure resolved via Calderón-Zygmund
- **Gap 5:** α = 3/5 boundary case clarified
- **Gap 6:** Cascade structures require profile decomposition path

---

## Key References

1. Nečas-Růžička-Šverák (1996) - L³ self-similar exclusion
2. Tsai (1998) - Extensions to other spaces
3. Escauriaza-Seregin-Šverák (2003) - L³_∞ backward uniqueness
4. Seregin (2012) - Type I blowup exclusion (critical dependency)
5. Hou-Luo (2014) - Numerical evidence for axisymmetric singularity

---

## Research Integrity

This project maintains strict separation between:
- **PROVEN:** Rigorous mathematical results
- **CONJECTURED:** Claims requiring additional verification
- **OPEN:** Acknowledged gaps without known resolution

See `submission-package/03-technical-proofs/UNIFIED-TYPE-II-EXCLUSION.md` for the honest assessment.

# Changelog

## 2026-01-11: Theorem Complete (Iteration 1)

### Major Correction
- Found error in axis ODE derivation: coefficient of g is (2a' - 1), not -1
- Corrected condition: ||a'||_∞ < 1/4 (not 3/4)

### Completed
- Full paper draft with complete proofs (docs/paper-draft.md)
- Bootstrap proof: g ≡ 0 ⟹ Γ ≡ 0
- Corrected all derivations

### Result
**Theorem 1.1:** Under moderate strain (||a'||_∞ < 1/4), axisymmetric
self-similar profiles have Γ ≡ 0, hence no blowup.

---

## 2026-01-11: Initial Research Framework

### Added
- Complete project structure for Navier-Stokes research
- Self-similar profile equation derivation (profile-equations.md)
- Five attack vectors analysis (attack-plan.md)
- Literature survey of known results (known-results.md)
- Full axisymmetric profile system derivation (axisymmetric-profile.md)
- Axis ODE analysis with energy method (axis-ode-analysis.md)
- Main theorem statement and gaps (main-theorem.md)

### Mathematical Results

**Theorem (Axis Non-Existence - Conditional):**
Under the moderate strain condition ||a'||_∞ < 3/4, the axis ODE for
the self-similar swirl coefficient has only the trivial solution g ≡ 0.

**Proof:** Energy identity + Cauchy-Schwarz.

**Key Identity Discovered:**
```
ν||g'||² + (3/4)||g||² = ∫ a'(ζ) g²(ζ) dζ
```

### Gaps Identified
1. Bootstrap: g ≡ 0 ⟹ Γ ≡ 0
2. Remove moderate strain condition
3. Connect to global regularity

### Next Steps
- Unique continuation analysis for Γ
- Derive bounds on a(ζ) from full system
- Pohozaev identities for 2D domain

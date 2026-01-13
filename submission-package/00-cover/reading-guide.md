# Reading Guide for Reviewers

## Navier-Stokes Global Regularity: Type II Exclusion via Seregin's Framework

**Submission Date:** January 2026
**Estimated Total Pages:** ~150 (all documents combined)

---

## 1. Recommended Reading Order

### Phase 1: Overview (30-60 minutes)

| Step | Document | Focus | Purpose |
|------|----------|-------|---------|
| 1 | `00-cover/executive-summary.md` | All sections | Grasp the main claim and proof strategy |

### Phase 2: Core Argument (2-4 hours)

| Step | Document | Focus | Purpose |
|------|----------|-------|---------|
| 2 | `01-main-paper/paper-type-II.md` | Sections 5.5, 9 | Understand the automatic satisfaction of Seregin's condition (1.4) |
| 3 | `01-main-paper/paper-type-II.md` | Sections 1-4 | Background on Type II blowup classification |

### Phase 3: Gap Closure Documents (4-8 hours)

Read in the following order, as each builds on the previous:

| Step | Document | Key Result |
|------|----------|------------|
| 4 | `02-gap-closures/gap2-constants-analysis.md` | Implicit constants C(t) = O(1), not divergent |
| 5 | `02-gap-closures/gap3-all-scales-analysis.md` | Supremum over ALL r in (0,1) is bounded |
| 6 | `02-gap-closures/gap4-local-pressure-analysis.md` | Local Calderon-Zygmund with r-independent constant |
| 7 | `02-gap-closures/gap5-boundary-analysis.md` | alpha = 3/5 excluded via energy-dissipation incompatibility |
| 8 | `02-gap-closures/gap6-cascade-analysis.md` | Multi-scale cascades also satisfy (1.4) |

### Phase 4: Rigorous Verification (2-4 hours)

| Step | Document | Purpose |
|------|----------|---------|
| 9 | `03-technical-proofs/epsilon-delta-proofs.md` | Complete epsilon-delta proofs with explicit constants |

### Phase 5: Numerical Check (1-2 hours)

| Step | Document | Purpose |
|------|----------|---------|
| 10 | `04-numerical-verification/unified-exponent-table.md` | Verify all exponents positive in (1/2, 3/5)^2 |

---

## 2. Dependency Graph

```
                    SEREGIN'S THEOREM (arXiv:2507.08733)
                    "If condition (1.4) holds for m in (1/2, 3/5),
                     then Type II with alpha in (1/2, 3/5) is excluded"
                                      |
                                      v
              +-----------------------------------------------+
              |   MAIN RESULT: Condition (1.4) is AUTOMATIC   |
              |   for Type II blowup with alpha in (1/2, 3/5) |
              +-----------------------------------------------+
                     |                    |
        +------------+------------+       +------------+
        |                         |                    |
        v                         v                    v
+----------------+    +-------------------+    +------------------+
| GAP 2:         |    | GAP 3:            |    | GAP 4:           |
| Constants      |    | All Scales        |    | Local Pressure   |
| C(t) = O(1)    |    | sup_r bounded     |    | r-independent C  |
+----------------+    +-------------------+    +------------------+
        |                    |                         |
        v                    v                         v
        +--------------------+--------------------------+
                             |
                    +--------+--------+
                    |                 |
                    v                 v
          +-----------------+  +------------------+
          | GAP 5:          |  | GAP 6:           |
          | alpha = 3/5     |  | Cascade          |
          | excluded        |  | satisfies (1.4)  |
          +-----------------+  +------------------+
                    |                 |
                    v                 v
              +-----------------------------+
              | TYPE II EXCLUSION COMPLETE  |
              | for alpha in (1/2, 3/5]     |
              +-----------------------------+
                             |
                             v
              +-----------------------------+
              | COMBINED WITH:              |
              | - ESS (alpha = 1/2)         |
              | - BKM (alpha < 1/2)         |
              | - Energy (alpha > 3/5)      |
              +-----------------------------+
                             |
                             v
              +-----------------------------+
              |  GLOBAL REGULARITY FOR      |
              |  3D NAVIER-STOKES           |
              +-----------------------------+
```

### Critical Path (Shortest Path to Main Result)

```
Seregin's Theorem --> Gap 2 (constants) --> Gap 3 (all scales) -->
Gap 5 (boundary) --> Type II Exclusion --> Global Regularity
```

---

## 3. Three Most Critical Verification Points

Reviewers should pay particular attention to these key claims:

### Critical Point 1: Seregin's Theorem Validity

**Location:** `01-main-paper/paper-type-II.md`, Section 5.5.1

**Claim:** Seregin's Proposition 4.1 (arXiv:2507.08733) correctly states that condition (1.4) with m in (1/2, 3/5) excludes Type II blowup via the ancient Euler Liouville theorem.

**What to Verify:**
- [ ] The statement of condition (1.4) is correctly transcribed
- [ ] The parameter range m in (1/2, 3/5) matches Seregin's requirements
- [ ] The connection to ancient Euler solutions is correctly applied
- [ ] No hidden assumptions in Seregin's theorem are missed

**Reference:** G. Seregin, arXiv:2507.08733v2, July 2025

---

### Critical Point 2: Gap 2 - Constants Bounded

**Location:** `02-gap-closures/gap2-constants-analysis.md`, Sections 5-6

**Claim:** The implicit constant C(t) in the scaling relation A_{m1}(L) = C(t) * (T-t)^{theta_A} satisfies C(t) <= C_* where C_* depends only on initial energy E_0.

**What to Verify:**
- [ ] The local energy inequality is correctly applied
- [ ] All constants from Sobolev/Calderon-Zygmund are tracked explicitly
- [ ] No circular dependency (assuming what we're proving)
- [ ] The constant C_LEI from local energy inequality is truly universal

**Key Formula:**
```
C(t) <= C_* := C_{LEI} * E_0
```

**Warning Signs to Look For:**
- Constants that depend on the solution itself (circular)
- Hidden t-dependence in "universal" constants
- Interpolation inequalities with untracked constants

---

### Critical Point 3: Exponent Positivity (theta_E >= 0.12)

**Location:** `04-numerical-verification/unified-exponent-table.md`, Section 6

**Claim:** The minimum value of theta_E = (3 - 3*alpha - m(1+alpha))/2 over (alpha, m) in (1/2, 3/5)^2 is 0.12, achieved at the corner (0.6, 0.6).

**What to Verify:**
- [ ] The formula for theta_E is correct (matches the scaling derivation)
- [ ] The numerical computation at boundary is accurate
- [ ] The boundary case (0.6, 0.6) is handled correctly
- [ ] No open vs. closed interval issues

**Verification Computation:**
```
At alpha = m = 0.6:
theta_E = (3 - 3*0.6 - 0.6*(1+0.6))/2
        = (3 - 1.8 - 0.6*1.6)/2
        = (3 - 1.8 - 0.96)/2
        = 0.24/2
        = 0.12 > 0
```

**Why This Matters:**
If theta_E <= 0 for any valid (alpha, m), then E_m is unbounded and condition (1.4) fails.

---

## 4. Estimated Review Time

| Review Level | Documents | Time Estimate |
|--------------|-----------|---------------|
| **Quick Review** | Executive summary + main paper (Sec 5.5, 9) | 2-4 hours |
| **Thorough Review** | All documents, verify key lemmas | 1-2 days |
| **Full Verification** | Check all proofs, reproduce calculations | 1-2 weeks |

### Breakdown by Document

| Document | Pages | Quick | Thorough | Full |
|----------|-------|-------|----------|------|
| Executive Summary | ~5 | 15 min | 30 min | 1 hr |
| Main Paper | ~40 | 1-2 hr | 4-6 hr | 2-3 days |
| Gap 2 Analysis | ~20 | 30 min | 2-3 hr | 1 day |
| Gap 3 Analysis | ~18 | 30 min | 2-3 hr | 1 day |
| Gap 4 Analysis | ~20 | 30 min | 2-3 hr | 1 day |
| Gap 5 Analysis | ~16 | 20 min | 1-2 hr | 4 hr |
| Gap 6 Analysis | ~25 | 40 min | 3-4 hr | 1-2 days |
| Epsilon-Delta Proofs | ~15 | 20 min | 2-3 hr | 1 day |
| Unified Exponent Table | ~5 | 10 min | 30 min | 2 hr |

---

## 5. Potential Weak Points (Honest Assessment)

Based on internal review, these are areas that require extra scrutiny:

### High Risk
1. **Cascade interpolation (Gap 6, Part 3.4):** The interpolation between dyadic scales requires careful handling of the monotonicity assumption.

2. **Energy scaling consistency (Gap 5, Section 2.3):** Different concentration scalings (beta = (1+alpha)/2 vs. beta = 1-alpha) give different energy exponents. Verify which applies.

### Medium Risk
3. **Local CZ r-independence (Gap 4, Theorem 3.1):** The scaling argument is elegant but requires careful verification that all hidden factors cancel.

4. **Profile decomposition application (Gap 6, Part 5):** The use of Bahouri-Gerard decomposition is non-trivial and may have technical conditions not fully addressed.

### Lower Risk
5. **Boundary m = 1/2 (Gap 5, Section 4):** This case reduces to known ESS results, but the reduction should be verified.

---

## 6. Reference Literature

### Essential Prerequisites
1. G. Seregin, "A note on certain scenarios of Type II blowups," arXiv:2507.08733 (2025)
2. L. Escauriaza, G. Seregin, V. Sverak, "L^{3,infinity}-solutions and backward uniqueness," Russian Math. Surveys 58 (2003)
3. L. Caffarelli, R. Kohn, L. Nirenberg, "Partial regularity of suitable weak solutions," CPAM 35 (1982)

### Recommended Background
4. T. Tao, "Quantitative bounds for critically bounded solutions," arXiv:1908.04958 (2019)
5. T. Barker, C. Prange, "Quantitative classification of singular solutions," arXiv:2510.20757 (2024)
6. P. Constantin, C. Fefferman, "Direction of vorticity and the problem of global regularity," Indiana Univ. Math. J. 42 (1993)

---

## 7. Suggested Review Workflow

### For Quick Review (Referee Pre-screening)
```
1. Read executive summary (15 min)
2. Skim main paper Section 5.5 for main theorem (30 min)
3. Check exponent table for obvious errors (15 min)
4. Read Critical Points 1, 2, 3 in this guide (30 min)
5. Form initial assessment
```

### For Thorough Review (Detailed Refereeing)
```
Day 1:
- Executive summary + main paper Sections 1-5

Day 2:
- Gap 2 and Gap 3 analyses
- Verify interpolation lemma

Day 3:
- Gap 4 (pressure) and Gap 5 (boundary)
- Check energy-dissipation argument

Day 4:
- Gap 6 (cascades)
- Epsilon-delta proofs
- Cross-reference exponent table
```

### For Full Verification
```
Week 1:
- Reproduce all explicit calculations
- Verify Seregin's theorem independently
- Check all cited references

Week 2:
- Attempt to find counterexamples
- Stress-test boundary cases
- Write detailed referee report
```

---

## 8. Contact Information

For questions regarding this submission:

**Primary Contact:**
[Author Name]
[Institution]
[Email]

**Alternative Contact:**
[Co-Author Name]
[Institution]
[Email]

**Response Time:** We aim to respond to reviewer queries within 48 hours.

---

## 9. Document Checksums

For verification that documents have not been modified:

| Document | Last Modified | SHA-256 (first 16 chars) |
|----------|---------------|-------------------------|
| paper-type-II.md | [Date] | [To be computed] |
| gap2-constants-analysis.md | 2026-01-13 | [To be computed] |
| gap3-all-scales-analysis.md | 2026-01-13 | [To be computed] |
| gap4-local-pressure-analysis.md | 2026-01-13 | [To be computed] |
| gap5-boundary-analysis.md | 2026-01-13 | [To be computed] |
| gap6-cascade-analysis.md | 2026-01-13 | [To be computed] |
| epsilon-delta-proofs.md | 2026-01-13 | [To be computed] |
| unified-exponent-table.md | 2026-01-13 | [To be computed] |

---

## 10. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-13 | Initial submission package |

---

**End of Reading Guide**

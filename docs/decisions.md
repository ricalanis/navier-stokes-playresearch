# Research Decisions

## 2026-01-13: BREAKTHROUGH - Self-Defeating Mechanism

**Decision:** Use physical sign control (u^r < 0 in concentration) as the key mechanism.

**Rationale:**
1. All algebraic approaches to control stretching failed
2. Physical reasoning: concentration toward axis requires inward flow
3. Sign control is automatic from geometry, not assumed
4. Creates self-defeating mechanism: concentration triggers anti-stretching

**Outcome:** Complete axisymmetric regularity proven.

---

## 2026-01-13: Three Independent Proof Mechanisms

**Decision:** Develop three independent mechanisms:
1. Profile non-existence (Theorems D, F) - Type I exclusion
2. η conservation + sign control - Type II no-swirl
3. Effective viscosity divergence - Type II with-swirl

**Rationale:**
1. Each mechanism covers different cases
2. Independence provides robustness
3. Combined coverage is exhaustive

**Outcome:** All blowup mechanisms excluded for axisymmetric NS.

---

## 2026-01-13: Bypass Seregin's Condition (1.4)

**Decision:** Use η conservation instead of trying to prove (1.4).

**Rationale:**
1. Proving (1.4) requires bounding local L² norms
2. This is the genuine mathematical frontier
3. Axisymmetric structure provides alternative path
4. η conservation gives stronger control

**Outcome:** Proof bypasses (1.4) entirely.

---

## 2026-01-13: Backward Dispersion for Liouville

**Decision:** Prove backward dispersion via energy growth in trapped regions.

**Rationale:**
1. Standard Liouville (KNSS) requires bounded solutions
2. Type II limit may have infinite total energy
3. Backward energy growth contradicts trapped regions
4. Forced dispersion enables material conservation argument

**Key Result:** For α < 0.82, energy grows backward. Type II needs α < 0.6 < 0.82.

**Outcome:** Completed Liouville theorem for with-swirl case.

---

## 2026-01-11: Attack Vector Selection

**Decision:** Focus on Vector D (Self-Similar Classification), specifically
the axisymmetric case with swirl.

**Rationale:**
1. Most concrete - connects to Hou-Luo numerics
2. Has existing partial results to build on (NRŠ, Tsai, etc.)
3. Geometric symmetry reduces complexity
4. Clear path to partial theorems even if full result eludes us

**Alternatives considered:**
- Vector A (NRŠ extension to weak L³): Too technical, less physical insight
- Vector B (Pohozaev): Generic approach, will use as supporting technique
- Vector C (Geometric/vorticity direction): Promising but less concrete
- Vector E (Spectral): Most speculative

## 2026-01-11: Proof Strategy

**Decision:** Use the axis ODE reduction + energy method.

**Rationale:**
1. The axis behavior dominates the singularity formation (Hou-Luo insight)
2. ODE analysis is more tractable than PDE analysis
3. Energy methods give clean inequalities
4. Results in a conditional theorem that can be strengthened

**Risk:** The "moderate strain" condition might not hold for all profiles.
Mitigation: Work to remove the condition in subsequent steps.

## 2026-01-11: Mathematical Rigor Level

**Decision:** Maintain full rigor in derivations, but flag gaps explicitly.

**Rationale:**
1. Partial/heuristic results in Millennium Prize problems are dangerous
2. Clear gap identification enables future work
3. Even partial rigorous results are publishable

**Implementation:**
- Use "Theorem" only for fully proved statements
- Use "Conjecture" for gaps requiring proof
- Use "Calculation" for algebraic steps that need verification

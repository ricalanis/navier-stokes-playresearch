# Research Decisions

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

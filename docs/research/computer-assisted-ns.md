# Computer-Assisted Proof Methods for Navier-Stokes Equations

*Research Survey - January 2026*

## Executive Summary

This report surveys computer-assisted proof methods applicable to the Navier-Stokes regularity problem, with focus on interval arithmetic, validated numerics, and machine learning approaches. The central question remains whether computational methods can rigorously close the "scaling gap" between what analysis can prove and what is needed to resolve the Millennium Prize Problem.

---

## 1. Foundations of Computer-Assisted Proofs in PDEs

### 1.1 Interval Arithmetic for Rigorous Bounds

**Core Principle**: Interval arithmetic replaces real numbers with intervals [a, b] that contain the true value. All operations propagate these bounds rigorously, producing guaranteed enclosures of results.

**Key Properties**:
- Controls rounding errors from floating-point arithmetic
- Provides rigorous upper and lower bounds on computed quantities
- Enables mathematically certified numerical results

**Major Software Libraries**:

| Library | Language | Features | Source |
|---------|----------|----------|--------|
| [CAPD](http://capd.ii.uj.edu.pl/) | C++ | ODE/PDE solvers, automatic differentiation | Jagiellonian University |
| [IntervalArithmetic.jl](https://github.com/JuliaIntervals/IntervalArithmetic.jl) | Julia | IEEE 1788-2015 compliant intervals | JuliaIntervals |
| [Arb](https://arblib.org/) | C | Arbitrary-precision ball arithmetic | Fredrik Johansson |
| [MPFI](http://perso.ens-lyon.fr/nathalie.revol/software.html) | C | Multiple-precision interval arithmetic | INRIA |
| [CoqInterval](https://coqinterval.gitlabpages.inria.fr/) | Coq | Formally verified intervals | INRIA |

### 1.2 Validated Numerics Framework

Validated numerics combines:
1. **Interval arithmetic** for error propagation
2. **A posteriori error estimates** for discretization control
3. **Fixed-point theorems** (Banach, Schauder) for existence proofs
4. **Symbolic manipulation** for exact computations where needed

**The Nakao-Plum-Watanabe School**:

Pioneering work by M.T. Nakao, M. Plum, and Y. Watanabe established rigorous methods for PDEs:

- **Nakao (1988)**: "A numerical approach to the proof of existence of solutions for elliptic problems"
- **Nakao, Hashimoto, Watanabe (2005)**: "A numerical method to verify the invertibility of linear elliptic operators"
- **Nakao, Hashimoto, Kobayashi (2007)**: "Verified numerical computation of solutions for the stationary Navier-Stokes equation in nonconvex polygonal domains" (Hokkaido Math. J.)
- **Watanabe (2009)**: "A computer-assisted proof for the Kolmogorov flows of incompressible viscous fluid" (J. Comput. Appl. Math.)
- **Watanabe, Plum, Nakao**: "A computer-assisted instability proof for the Orr-Sommerfeld problem"

**Key Result**: Computer-assisted proofs have verified existence of solutions for **stationary** Navier-Stokes equations in specific domains (L-shaped, 3D nonconvex polygonal) using:
- Infinite-dimensional Newton-type formulations
- Finite element method with constructive error estimates
- Radii polynomial approach for contraction arguments

---

## 2. Tucker-Style Rigorous ODE/PDE Solvers

### 2.1 The Lorenz Attractor Proof (2002)

Warwick Tucker's landmark work solved Smale's 14th problem by proving the Lorenz equations support a strange attractor.

**Methodology**:
- Rigorous ODE integration using interval arithmetic
- Directed rounding for controlled error propagation
- Partitioning process for trajectory tracking
- Poincare section analysis with rigorous bounds

**Significance for Navier-Stokes**: The Lorenz system is a truncation of Navier-Stokes equations, providing a simplified model for turbulence. The methodology demonstrates:
- Computer-assisted proofs can handle chaotic dynamics
- Rigorous error control is achievable for nonlinear systems
- Formal verification (later done in Isabelle/HOL) can certify such computations

### 2.2 The CAPD Library

[CAPD (Computer Assisted Proofs in Dynamics)](http://capd.ii.uj.edu.pl/) provides:

**Capabilities**:
- Rigorous ODE integration with automatic step control
- Lohner representation for set propagation
- Arbitrary precision via MPFR
- Support for differential inclusions
- Bifurcation analysis tools

**Applications**:
- Verified chaos in Kuramoto-Sivashinsky PDE
- Hyperchaos in Rossler-4D system
- Work in progress: 2D Navier-Stokes bifurcation analysis

**PDE Extension**: A dedicated solver for dissipative PDEs with periodic boundary conditions, using:
- FILIB interval arithmetic
- Rigorous integration guaranteeing solution enclosure
- Plans for 2D Navier-Stokes systems

---

## 3. The Chen-Hou Computer-Assisted Proof (2022)

### 3.1 Breakthrough Result

Thomas Hou (Caltech) and Jiajie Chen proved **finite-time singularity formation** for:
- 2D Boussinesq equations
- 3D axisymmetric Euler equations with boundary

This resolved the 2013 Hou-Luo numerical conjecture with rigorous mathematics.

### 3.2 Methodology

**Key Innovation**: Self-similar blowup profile analysis

1. **Dynamic Rescaling Formulation**: Transform to coordinates that "zoom in" at the blowup rate
2. **Approximate Steady State**: Construct numerical approximation to self-similar profile
3. **Nonlinear Stability Analysis**: Prove perturbations from approximate profile remain controlled
4. **Weighted Energy Estimates**: Establish bounds via carefully chosen Sobolev-type norms
5. **Rigorous Error Control**: Track all numerical errors to maintain mathematical validity

**Computer-Assisted Components**:
- Construction of approximate space-time solutions with rigorous error control
- Sharp stability estimates for linearized operators
- Numerical integration with certified bounds
- Verification of inequalities for energy estimate constants
- Computation performed on Caltech IMSS High Performance Computing

**Publications**:
- Chen-Hou arXiv:2210.07191 (2022): "Stable nearly self-similar blowup"
- SIAM Multiscale Modeling & Simulation (2023): Part II - Rigorous Numerics
- Annals of PDE: "Asymptotically self-similar blowup of the Hou-Luo model"

### 3.3 Implications for Navier-Stokes

**What was proven**: Blowup for Euler equations **with boundary** in a cylinder.

**What remains open**:
- Euler equations without boundary
- Navier-Stokes equations (viscosity present)

**Hou's Assessment**: "I see a path forward, a way to maybe even eventually resolve the full Millennium problem."

---

## 4. DeepMind's Discovery of Unstable Singularities (2025)

### 4.1 Machine Learning Approach

Google DeepMind, in collaboration with NYU and Stanford, discovered new families of **unstable singularities** using Physics-Informed Neural Networks (PINNs).

**Paper**: "Discovery of Unstable Singularities" (arXiv:2509.14185, September 2025)

**Authors**: Yongji Wang (NYU), Ray Jiang (DeepMind), Ching-Yao Lai (Stanford)

### 4.2 Technical Methodology

**Key Innovations**:
1. **High-Precision PINNs**: Trained to satisfy PDE residuals to unprecedented accuracy
2. **Gauss-Newton Optimizer**: Second-order optimization for extreme precision
3. **GPU Hardware-Limited Accuracy**: Achieved near double-float machine precision (constrained only by round-off errors)

**Discovered Singularities**:
- New families in 3D Euler equation with boundary
- Singularities in incompressible porous media equation
- Singularities in Boussinesq equation

### 4.3 Significance

**Unstable vs Stable Singularities**:
- **Stable**: Form robustly under perturbations
- **Unstable**: Require infinitely precise initial conditions (collapse under infinitesimal disturbance)

**Why This Matters**: Mathematicians believe no **stable** singularities exist for boundary-free 3D Euler and Navier-Stokes. Therefore, if singularities exist, they must be **unstable** - exactly what DeepMind discovered.

**Connection to Rigorous Proofs**: The precision achieved "meets the requirements for rigorous mathematical validation via computer-assisted proofs."

---

## 5. Type I and Type II Singularity Analysis

### 5.1 Definitions

**Type I Singularity**: Satisfies the natural scaling bound
$$\|u(\cdot, t)\|_{L^\infty} \leq \frac{C}{\sqrt{T-t}}$$

**Type II Singularity**: Violates Type I bounds; more severe concentration of vorticity.

### 5.2 Current Knowledge

**Axisymmetric Solutions**:
- **Type I blowup ruled out** for suitable weak solutions (Seregin 2006)
- Type II analysis is the frontier of research

**ε-Regularity Theory** (Caffarelli-Kohn-Nirenberg 1982):
- Singular set has zero 1D Hausdorff measure
- Smallness of scaled energy quantities implies regularity

### 5.3 Computer-Assisted Analysis Questions

**Q1: Can we rigorously verify solutions don't enter Type II window?**

Current Status: **Partially addressable**
- Quantitative bounds have been established for axisymmetric initial data
- These bounds are "in principle amenable to numerical testing"
- Full verification requires tracking all possible concentration mechanisms

**Challenges**:
- Type II blowup involves extreme concentration at potentially unknown locations
- Requires global-in-space-time error control
- Current methods work best for self-similar scenarios

---

## 6. The Scaling Gap Problem

### 6.1 The Fundamental Obstacle

The Navier-Stokes regularity problem is **supercritical**: there is a mismatch between:
- What can be bounded rigorously (energy, enstrophy)
- What is needed to rule out singularities (pointwise control)

**The Gap**: Energy is conserved globally but can concentrate locally. A finite amount of energy concentrating at a point could produce a singularity.

### 6.2 Critical Exponents

**Hyperdissipative NS**: Global regularity proven for dissipation exponent α ≥ 5/4 (energy-critical)

**Standard NS**: α = 1 (supercritical)

**The (1/2, 3/5) Question**: This likely refers to Holder exponents in regularity criteria. The classical result (Prodi-Serrin-Ladyzhenskaya) gives:
$$u \in L^p_t L^q_x \quad \text{with} \quad \frac{2}{p} + \frac{3}{q} \leq 1, \quad q \geq 3$$

**Q2: Can interval arithmetic close the gap numerically?**

Current Assessment: **Very challenging**
- The gap is infinite-dimensional (function space vs. pointwise control)
- Interval arithmetic can verify specific numerical inequalities
- Cannot directly "close" an analytical gap

**What IS possible**:
- Verify specific solutions remain regular on finite time intervals
- Bound energy concentration for specific initial data
- Check numerical stability of computed solutions

---

## 7. Verified Bounds on Blowup Rates

### 7.1 What Is Known Rigorously

**For averaged/modified equations** (Tao 2014):
- Finite-time blowup proven for averaged Navier-Stokes
- Demonstrates any positive resolution must use fine structure beyond energy methods

**For Euler with boundary** (Chen-Hou 2022):
- Self-similar blowup rate: $(T-t)^{-1}$ for vorticity
- Profile is asymptotically self-similar

### 7.2 Q3: Are there verified bounds on blowup rates?

**For actual 3D Navier-Stokes**: **NO verified blowup exists**

**Conditional Results**:
- IF blowup occurs, then $\|u\|_{L^3}$ must become unbounded (Escauriaza-Seregin-Sverak)
- IF blowup occurs with specific structure, rate bounds follow from scaling

**Computer-Assisted Potential**:
- Could potentially verify specific candidate blowup scenarios fail
- Could bound rates assuming specific concentration profiles
- Cannot yet prove or disprove general blowup

---

## 8. Formal Verification (Hales-Style Approach)

### 8.1 The Flyspeck Precedent

Thomas Hales' proof of the Kepler conjecture was formally verified in HOL Light and Isabelle (completed 2014).

**Key Features**:
- ~1000 nonlinear inequalities verified by computer
- Taylor interval approximations for rigorous bounds
- Multiple proof assistants for cross-validation
- 21 collaborators, ~11 years of work

### 8.2 Formal Verification of PDEs

**Current State**: No formal proof of Navier-Stokes solutions exists in Lean, Coq, or Isabelle.

**Challenges**:
- Need mathematical proof first (open problem!)
- PDE formalization is inherently harder than algebraic/combinatorial
- Requires formalizing functional analysis in proof assistants

**Related Work**:
- Tucker's Lorenz attractor proof formalized in Isabelle/HOL
- Interval arithmetic formalized in CoqInterval
- ODE existence theorems in mathlib (Lean)

### 8.3 What Would Be Needed

For a Flyspeck-style verification of Navier-Stokes:

1. **Complete Mathematical Proof**: Must exist first
2. **Formalized Functional Analysis**: Sobolev spaces, weak solutions, energy estimates
3. **Verified Numerical Components**: All computer calculations certified
4. **Proof Assistant Infrastructure**: Adequate libraries for PDEs

**Estimated Effort**: If a proof existed today, formal verification would likely require 10-20 person-years.

---

## 9. Machine Learning for Conjecture Generation

### 9.1 Current Approaches

**Physics-Informed Neural Networks (PINNs)**:
- Train networks to satisfy PDE residuals
- Discover solutions without traditional discretization
- Can explore parameter space for interesting behavior

**Reinforcement Learning**:
- Generate mathematical constructions
- Find counterexamples to conjectures
- Optimize search in proof spaces

**Transformer-Based Systems**:
- PatternBoost: Combines transformers with local search
- AlphaProof: Autoformalization of mathematical problems
- Aristotle: IMO-level theorem proving

### 9.2 Applications to PDEs

**Demonstrated Capabilities**:
- Discovery of new singularities (DeepMind 2025)
- Pattern recognition in numerical solutions
- Conjecture generation for graph theory, combinatorics

**Limitations**:
- Cannot produce rigorous proofs directly
- Require human mathematicians to verify insights
- Prone to "hallucinating" false patterns

### 9.3 Future Potential

**For Navier-Stokes**:
- Identify candidate blowup scenarios for rigorous analysis
- Suggest functional inequalities to investigate
- Explore high-dimensional parameter spaces
- Guide human intuition toward productive directions

---

## 10. Computational Infrastructure Requirements

### 10.1 For Rigorous Numerical Proofs

**Hardware Requirements**:
- High-precision arithmetic (quadruple or arbitrary precision)
- Large memory for interval propagation (intervals have 2x storage)
- Parallel computing for exhaustive case analysis
- GPU capabilities for neural network components

**Software Stack**:
- Interval arithmetic libraries (MPFI, Arb, IntervalArithmetic.jl)
- ODE/PDE solvers with rigorous error control (CAPD, custom)
- Proof assistants for formal verification (Lean, Isabelle, Coq)
- High-performance linear algebra (BLAS, LAPACK with error bounds)

### 10.2 Estimated Requirements for "Closing the Gap"

**If a computer-assisted proof strategy existed**, infrastructure would need:

| Component | Requirement | Justification |
|-----------|-------------|---------------|
| Precision | 128-bit or arbitrary | Error accumulation over long times |
| Memory | 100+ GB per node | Full interval representations |
| Compute | 10,000+ CPU hours | Exhaustive case verification |
| Storage | 10+ TB | Intermediate certified computations |
| Verification | Formal proof assistant | Mathematical certification |

### 10.3 Current Gaps in Infrastructure

1. **No PDE-specific rigorous solver at NS scale**: Current tools handle simpler systems
2. **No 3D turbulence-scale interval arithmetic**: Computational cost prohibitive
3. **No formal verification of time-dependent NS**: Even basic theorems not formalized
4. **No ML-to-proof pipeline**: Discoveries need manual translation

---

## 11. Research Roadmap

### 11.1 Near-Term (1-3 years)

- [ ] Extend Chen-Hou methodology to Euler without boundary
- [ ] Develop formal verification of stationary NS proofs
- [ ] Create PDE-specific interval arithmetic libraries
- [ ] Apply ML to discover new candidate blowup scenarios

### 11.2 Medium-Term (3-7 years)

- [ ] Computer-assisted analysis of NS with small viscosity
- [ ] Rigorous verification of Type II exclusion for specific data
- [ ] Formal verification of Hou-Chen Euler proof
- [ ] ML-guided conjecture generation for regularity criteria

### 11.3 Long-Term (7+ years)

- [ ] Full computer-assisted proof of NS blowup or regularity
- [ ] Formal verification in proof assistant
- [ ] Unified framework for rigorous PDE analysis
- [ ] Resolution of Millennium Prize Problem

---

## 12. Key References

### Foundational Works

1. Tucker, W. (2002). "A Rigorous ODE Solver and Smale's 14th Problem." *Foundations of Computational Mathematics*, 2, 53-117. [Link](https://link.springer.com/article/10.1007/s002080010018)

2. Nakao, M.T., Hashimoto, K., Kobayashi, K. (2007). "Verified numerical computation of solutions for the stationary Navier-Stokes equation in nonconvex polygonal domains." *Hokkaido Math. J.*, 36(4), 777-799.

3. Hales, T. et al. (2017). "A formal proof of the Kepler conjecture." *Forum of Mathematics, Pi*, 5, e2. [arXiv:1501.02155](https://arxiv.org/abs/1501.02155)

### Recent Breakthroughs

4. Chen, J., Hou, T.Y. (2022). "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data." [arXiv:2210.07191](https://arxiv.org/abs/2210.07191)

5. Wang, Y., Jiang, R., Lai, C.-Y. et al. (2025). "Discovery of Unstable Singularities." [arXiv:2509.14185](https://arxiv.org/abs/2509.14185)

### Survey Papers

6. Gomez-Serrano, J. (2019). "Computer-assisted proofs in PDE: a survey." *SeMA Journal*, 76, 459-484. [Link](https://link.springer.com/article/10.1007/s40324-019-00186-x)

7. Li, Z. et al. (2024). "A Survey on Deep Learning for Theorem Proving." [arXiv:2404.09939](https://arxiv.org/abs/2404.09939)

### Software and Tools

8. CAPD Library: [http://capd.ii.uj.edu.pl/](http://capd.ii.uj.edu.pl/)

9. IntervalArithmetic.jl: [GitHub](https://github.com/JuliaIntervals/IntervalArithmetic.jl)

10. Flyspeck Project: [GitHub](https://github.com/flyspeck/flyspeck)

---

## 13. Conclusions

### 13.1 What Computer-Assisted Methods CAN Do

1. **Verify specific numerical inequalities** rigorously
2. **Prove existence** of solutions for stationary NS in bounded domains
3. **Establish blowup** for modified/simplified equations (Euler with boundary)
4. **Discover candidate singularities** for further analysis
5. **Track errors** in numerical simulations to machine precision

### 13.2 What Remains Beyond Current Reach

1. **General blowup/regularity** for 3D Navier-Stokes
2. **Closing the scaling gap** purely numerically
3. **Formal verification** of time-dependent NS theory
4. **Automated proof** of PDE regularity theorems

### 13.3 Assessment of Specific Questions

**Q1: Can we RIGOROUSLY verify that solutions don't enter Type II window?**
> **Partially.** For specific initial data with quantitative assumptions, yes. Generally, no.

**Q2: Can interval arithmetic close the (1/2, 3/5) gap numerically?**
> **No.** The gap is analytical, not numerical. Interval arithmetic verifies computations but cannot bridge infinite-dimensional analytical gaps.

**Q3: Are there verified bounds on blowup rates?**
> **For Euler with boundary:** Yes (Chen-Hou).
> **For Navier-Stokes:** No blowup proven, so no rates to bound.

### 13.4 Path Forward

The most promising near-term approach combines:
1. **Chen-Hou methodology** extended to NS with small viscosity
2. **ML-guided discovery** of critical scenarios
3. **Rigorous verification** of discovered phenomena
4. **Incremental formalization** in proof assistants

The Millennium Prize Problem remains open, but computer-assisted methods are now serious contenders in the mathematical toolkit for its eventual resolution.

---

*Report compiled from web searches and literature review, January 2026.*

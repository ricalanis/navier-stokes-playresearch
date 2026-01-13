# Recent Breakthroughs in Navier-Stokes Regularity Theory (2023-2026)

**Last Updated:** January 13, 2026

This document summarizes the most significant recent developments in Navier-Stokes regularity theory, with particular focus on results relevant to the Millennium Prize Problem and Type II blowup analysis.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [New Regularity Criteria Beyond Prodi-Serrin-Ladyzhenskaya](#new-regularity-criteria-beyond-prodi-serrin-ladyzhenskaya)
3. [Type II Blowup: Recent Progress](#type-ii-blowup-recent-progress)
4. [Major Results from Leading Researchers](#major-results-from-leading-researchers)
5. [AI and Machine Learning Breakthroughs](#ai-and-machine-learning-breakthroughs)
6. [Partial Results on Critical Gaps](#partial-results-on-critical-gaps)
7. [Open Problems and Future Directions](#open-problems-and-future-directions)
8. [Key References](#key-references)

---

## Executive Summary

The period 2023-2026 has seen remarkable progress in understanding the Navier-Stokes equations, though the Millennium Prize Problem remains officially unsolved. Key developments include:

- **Thomas Hou's group** provided the first rigorous computer-assisted proof of Leray-Hopf nonuniqueness for unforced 3D Navier-Stokes (September 2025)
- **Google DeepMind** discovered new families of unstable singularities using Physics-Informed Neural Networks (September 2025)
- **Multi-level logarithmic criteria** have been developed extending Prodi-Serrin-Ladyzhenskaya conditions (March 2025)
- **Type II blowup scenarios** have been systematically ruled out under specific conditions using Liouville theorems for ancient Euler solutions (July 2025)
- **Non-uniqueness from critical data** has been demonstrated, showing sharpness of Koch-Tataru results (December 2025)

---

## New Regularity Criteria Beyond Prodi-Serrin-Ladyzhenskaya

### Classical Background

The Prodi-Serrin-Ladyzhenskaya condition states that if a weak solution u satisfies:
```
u in L^s(0,T; L^r(R^3))  with  2/s + 3/r <= 1,  r >= 3
```
then u is smooth. The critical case (s=infinity, r=3) was resolved by Escauriaza-Seregin-Sverak (2003) using backward uniqueness.

### Recent Extensions (2024-2025)

#### 1. Multi-Level Logarithmic Criteria (March 2025)

**Paper:** [Global Well-Posedness of the 3D Navier-Stokes Equations under Multi-Level Logarithmically Improved Criteria](https://arxiv.org/abs/2503.24029)

**Key Result:** Extends logarithmically improved regularity criteria with a comprehensive framework involving j-fold nested logarithms.

**Main Theorem:** If initial data satisfies a nested logarithmically weakened condition involving multiple layers of logarithmic corrections, then global existence and uniqueness hold.

**Technical Innovation:** Novel sequence of increasingly precise commutator estimates with multiple layers of logarithmic corrections. Establishes existence of a critical threshold function characterizing the boundary between global regularity and potential singularity.

**Relevance to Type II:** These criteria provide finer tools for analyzing borderline cases where standard scaling arguments fail.

#### 2. Regularity in Critical Anisotropic Spaces (July 2025)

**Paper:** [On the Regularity of Navier-Stokes Equations in Critical Space](https://arxiv.org/abs/2507.03881)

**Key Result:** Proves that if u(x,t) is in the scaling-invariant spaces:
```
L_t^infinity L_{x_3}^{p_1} L_{x_h}^{p_2}(Q_T)  where  1/p_1 + 2/p_2 = 1,  p_1 >= 2
```
then u is smooth and doesn't blow up at t=0.

**Special Case:** If u(x,t) in L_t^infinity L_{x_3}^infinity L_{x_h}^2, then u is smooth.

#### 3. New Criteria in Besov and Lorentz Spaces (2024-2025)

**Paper:** [New regularity criteria for Navier-Stokes and SQG equations in critical spaces](https://www.aimsciences.org/article/doi/10.3934/dcds.2024123)

**Key Result:** Demonstrates that Leray-Hopf solutions are regular under new conditions in Besov spaces B^{-1}_{infinity,infinity} and Lorentz spaces. Extends Gallagher-Koch-Planchon (2016) results to the largest critical space.

#### 4. Epsilon Regularity via Weak-Strong Uniqueness (2023)

**Paper:** [Epsilon Regularity for the Navier-Stokes Equations via Weak-Strong Uniqueness](https://link.springer.com/article/10.1007/s00021-023-00780-0)

**Key Result:** New concise proof of one-scale epsilon regularity criterion using weak-strong uniqueness for solutions with non-zero boundary conditions.

---

## Type II Blowup: Recent Progress

Type II blowup refers to singularities where the blowup rate is slower than the self-similar rate |u(t)| ~ (T-t)^{-1/2}.

### Key 2025 Results

#### 1. Ruling Out Type II Scenarios via Liouville Theorems (July 2025)

**Paper:** [A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations](https://arxiv.org/abs/2507.08733)

**Main Results:**
- Studies various Type II blowup scenarios for suitable weak solutions
- Proves that under certain assumptions, such blowups **cannot happen**
- Uses Euler scaling combined with Liouville-type theorems for ancient Euler solutions
- The necessary condition for Type II blowup is existence of a non-trivial ancient solution to Euler in a specific class

**Technical Approach:** Connects Type II blowup to the structure of ancient solutions of the Euler equations, exploiting the Liouville property of these ancient solutions.

**Implication:** Type II blowup can only occur if specific exotic ancient Euler solutions exist, significantly constraining the possibilities.

#### 2. Seregin's Type II Remarks (2024)

**Paper:** G. A. Seregin, "Remarks on type II blowups of solutions to the Navier-Stokes equations," Comm. Pure Appl. Anal. 23(10):1389-1406, 2024.

**Key Result:** Establishes boundedness conditions that rule out Type II singularities for MHD equations, providing a natural starting point for NS analysis.

#### 3. Time-Global Regularity with Super-Level Set Analysis (2025)

**Paper:** [Time-Global Regularity of the Navier-Stokes...](https://d-nb.info/1366489675/34) (Annals of PDE)

**Key Result:** Shows a region in parameter space where singularity formation cannot be ruled out classically, but the sparseness of super-level sets of higher-order derivatives rules out approximately self-similar blow-up when beta > 1.

---

## Major Results from Leading Researchers

### Thomas Hou (Caltech)

#### Nearly Self-Similar Blowup (May 2024, revised June 2025)

**Paper:** [Nearly self-similar blowup of generalized axisymmetric Navier-Stokes equations](https://arxiv.org/abs/2405.10916)

**Key Contributions:**
- First rigorous derivation of axisymmetric NS with swirl in dimensions > 3
- Novel two-scale dynamic rescaling formulation using dimension as degree of freedom
- Numerical evidence: rescaled NS model with two constant viscosity coefficients exhibits nearly self-similar blowup with max vorticity growth O(10^30)
- "Tornado-type" traveling wave singularity at the origin

**Methodology:** Counter-intuitive approach with relatively high viscosity leads to 10^7-fold enhancement of maximum vorticity.

#### Leray-Hopf Nonuniqueness (September 2025)

**Paper:** [Nonuniqueness of Leray-Hopf solutions to the unforced incompressible 3D Navier-Stokes Equation](https://arxiv.org/abs/2509.25116)

**Major Breakthrough:** First rigorous computer-assisted proof of Leray-Hopf nonuniqueness for **unforced** 3D NS.

**Key Result:** Constructs Leray-Hopf solution in self-similar setting and establishes second solution by analyzing stability of linearized operator. Shows existence of unstable perturbation yielding infinitely many Leray-Hopf solutions.

**Historical Context:** Prior work (Albritton-Brue-Colombo 2022) showed nonuniqueness for *forced* NS; this extends to the unforced case.

### Seregin & Sverak

#### Supercritical Extension (August 2025)

**Paper:** [Time asymptotics, time regularity and separation rates for Navier-Stokes flows in supercritical solution classes](https://arxiv.org/abs/2508.00714) by Zachary Bradshaw

**Key Result:** Extends Barker-Seregin-Sverak weak solution theory from critical to supercritical setting.

**Includes:**
- Useful a priori energy bound
- Statement about stability under weak-star convergence
- Spatially local, short-time asymptotic expansion
- Upper bound on separation rate for hypothetical non-unique solutions
- Higher-order time regularity at singular time for points away from singularity

### Barker & Prange: Concentration to Quantitative Regularity

**Survey:** [From concentration to quantitative regularity: a short survey of recent developments for the Navier-Stokes equations](https://arxiv.org/abs/2211.16215) (Vietnam J. Math., December 2023)

**Key Questions Addressed:**
1. Are norms accumulating/concentrating on small scales near potential blow-up?
2. At what speed do scale-invariant norms blow up?
3. Can one prove explicit quantitative regularity estimates?
4. Can one break the criticality barrier, even slightly?

**Main Insight:** These questions are closely linked. Methods from nonlinear dispersive equations inspire recent NS advances.

**Technical Tools:**
- Local-in-space smoothing results (Jia-Sverak 2014)
- Quantitative arguments using Carleman inequalities (Tao 2019)
- Profile decomposition techniques

---

## AI and Machine Learning Breakthroughs

### Google DeepMind: Discovery of Unstable Singularities (September 2025)

**Paper:** [Discovery of Unstable Singularities](https://arxiv.org/abs/2509.14185)

**Significance:** First systematic discovery of new families of unstable singularities using AI-enhanced methods.

**Key Findings:**
- New singularity families discovered in:
  - 3D Euler equations
  - Incompressible porous media equation
  - Boussinesq equation
- Observed linear relationship between lambda (blowup speed) and instability order, suggesting additional undiscovered solutions

**Methodology:**
- Enhanced Physics-Informed Neural Networks (PINNs)
- Second-order optimizers for neural network training
- Achieved extreme precision (errors equivalent to predicting Earth's diameter within centimeters)
- Embedded mathematical insights directly into training

**Implications for NS:** Demonstrates that AI can find "unstable" blowups that are nearly impossible to find analytically. These are the types most likely to occur in Navier-Stokes if blowup exists.

**Coverage:** [Quanta Magazine (January 2026)](https://www.quantamagazine.org/using-ai-mathematicians-find-hidden-glitches-in-fluid-equations-20260109/)

### David Budden's AI-Assisted Proof Attempt (December 2025)

**Context:** $10,000 bet between DeepMind engineers Marcus Hutter and David Budden.

**Claim:** Budden (who left DeepMind to work on math proof with LLMs) claims to have a proof of Navier-Stokes existence and smoothness formalized in Lean.

**Status:** Under review. First version published in Lean; community can find holes that may be patched before arXiv submission.

**Note:** This claim has NOT been verified and should be treated with extreme caution.

### Physics-Informed Neural Networks for NS (2024-2025)

**Paper:** [Using Physics-Informed neural networks for solving Navier-Stokes equations in fluid dynamic complex scenarios](https://www.sciencedirect.com/science/article/pii/S0952197625003471)

**Key Advance:** PINNs embed physical laws directly into training process, offering promising approach for solving NS in practical scenarios where analytical solutions don't exist.

### Turing Completeness Result (July 2025)

**Paper:** "Turing complete Navier-Stokes steady states via cosymplectic geometry" by Dyhr, Gonzalez-Prieto, Miranda, and Peralta-Salas

**Result:** Constructed steady solutions of full Navier-Stokes equations that are Turing-complete.

**Implication:** May provide fundamental limits on what can be predicted about NS solutions algorithmically.

---

## Partial Results on Critical Gaps

### The (1/2, 3/5) Gap and Related Questions

The gap between the critical Sobolev exponent s=1/2 (where local well-posedness is known) and the energy regularity s=1 remains a major open question.

#### Relevant 2024-2025 Progress:

##### 1. Global Regularity from H^{1/2} Data (August 2025)

**Paper:** [Global regularity of Leray-Hopf weak solutions to 3D Navier-Stokes equations](https://arxiv.org/abs/2508.19590)

**Claim:** Any Leray-Hopf weak solution with initial data in H^{1/2}(R^3) belongs to L^infinity(0,infinity; H^{1/2}(R^3)) and is thus regular.

**Method:** Constructs supercritical space whose norm is compared to H^{1/2}-norm, featuring inverse logarithmic weight sparsely in frequency domain.

**Status:** Preprint; requires verification.

##### 2. Non-uniqueness at Critical Regularity (December 2025)

**Paper:** [Non-uniqueness of smooth solutions of the Navier-Stokes equations from critical data](https://www.researchgate.net/publication/398638086)

**Key Result:** Demonstrates sharpness of Koch-Tataru small data global well-posedness result. First example of non-uniqueness for NS with data at critical regularity.

**Implication:** Any proof of global regularity cannot rely solely on critical space arguments.

##### 3. Quantitative Partial Regularity (April 2024)

**Paper:** [Quantitative partial regularity of the Navier-Stokes equations and applications](https://www.sciencedirect.com/science/article/abs/pii/S0001870824001695)

**Key Result:** Logarithmic improvement of Caffarelli-Kohn-Nirenberg partial regularity theorem.

**Method:** Quantitative counterpart for absolute continuity of dissipation energy using pigeonholing argument.

---

## Open Problems and Future Directions

### Still Open as of January 2026:

1. **Millennium Prize Problem:** Global existence and smoothness of 3D NS from smooth data remains unsolved.

2. **Type II Blowup:** While many scenarios have been ruled out, complete exclusion of Type II blowup remains open.

3. **Axisymmetric with Swirl:** Global regularity for general axisymmetric data with non-trivial swirl is wide open.

4. **Uniqueness:** While non-uniqueness has been proven in various settings (forced, critical data), uniqueness for smooth data remains unresolved.

### Promising Research Directions:

1. **AI-Assisted Discovery:** DeepMind's success suggests further AI methods could identify blowup candidates or prove their impossibility.

2. **Liouville Theorems for Ancient Solutions:** Connection between Type II blowup and ancient Euler solutions suggests this as a key research area.

3. **Computer-Assisted Proofs:** Hou's work demonstrates rigorous computer-assisted methods can tackle problems previously considered intractable.

4. **Profile Decomposition:** Techniques from dispersive equations continue to yield new insights (Barker-Prange survey).

5. **Anisotropic Spaces:** New regularity criteria in anisotropic spaces may provide alternative routes to closing gaps.

---

## Key References

### Survey Papers

1. Barker, T. & Prange, C. (2023). "From concentration to quantitative regularity: a short survey of recent developments for the Navier-Stokes equations." Vietnam J. Math. [arXiv:2211.16215](https://arxiv.org/abs/2211.16215)

### Type II Blowup

2. Seregin, G. A. (2024). "Remarks on type II blowups of solutions to the Navier-Stokes equations." Comm. Pure Appl. Anal. 23(10):1389-1406.

3. Anonymous (2025). "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations." [arXiv:2507.08733](https://arxiv.org/abs/2507.08733)

### Hou's Group

4. Hou, T. Y. (2024). "Nearly self-similar blowup of generalized axisymmetric Navier-Stokes equations." [arXiv:2405.10916](https://arxiv.org/abs/2405.10916)

5. Hou, T. Y., Wang, Y., & Yang, C. (2025). "Nonuniqueness of Leray-Hopf solutions to the unforced incompressible 3D Navier-Stokes Equation." [arXiv:2509.25116](https://arxiv.org/abs/2509.25116)

### AI/ML Approaches

6. DeepMind et al. (2025). "Discovery of Unstable Singularities." [arXiv:2509.14185](https://arxiv.org/abs/2509.14185)

7. Wood, C. (2026). "Using AI, Mathematicians Find Hidden Glitches in Fluid Equations." [Quanta Magazine](https://www.quantamagazine.org/using-ai-mathematicians-find-hidden-glitches-in-fluid-equations-20260109/)

### Regularity Criteria

8. Anonymous (2025). "Global Well-Posedness of the 3D Navier-Stokes Equations under Multi-Level Logarithmically Improved Criteria." [arXiv:2503.24029](https://arxiv.org/abs/2503.24029)

9. Anonymous (2025). "On the Regularity of Navier-Stokes Equations in Critical Space." [arXiv:2507.03881](https://arxiv.org/abs/2507.03881)

### Critical Space Results

10. Anonymous (2025). "Non-uniqueness of smooth solutions of the Navier-Stokes equations from critical data." ResearchGate.

### Clay Mathematics Institute

11. Clay Mathematics Institute. "Navier-Stokes Equation." [Official Problem Statement](https://www.claymath.org/millennium/navier-stokes-equation/)

---

## Notes for Type II Analysis

### Key Observations for Current Project:

1. **Liouville Connection:** Type II blowup requires existence of non-trivial ancient Euler solutions in specific classes. This provides a concrete obstruction to ruling out Type II.

2. **Quantitative Methods:** Barker-Prange-type quantitative regularity estimates may provide tools for analyzing borderline cases in the (1/2, 3/5) gap.

3. **Computer-Assisted Approaches:** Hou's success with computer-assisted proofs suggests this methodology could be applied to Type II exclusion arguments.

4. **DeepMind's Unstable Singularities:** The discovery of unstable singularities in related equations suggests that if NS blowup exists, it may be highly unstable and require AI-assisted discovery methods.

5. **Anisotropic Criteria:** New regularity criteria in anisotropic spaces may be particularly relevant for axisymmetric configurations relevant to Type II analysis.

---

*This document will be updated as new results emerge.*

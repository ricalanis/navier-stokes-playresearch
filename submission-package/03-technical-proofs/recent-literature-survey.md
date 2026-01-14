# Recent Literature Survey: Type II Navier-Stokes Blowup and the Gap alpha in [5/7, 1)

## Survey Overview

**Date:** January 13, 2026
**Focus:** Mathematical literature from 2020-2026 on Type II Navier-Stokes blowup exclusion
**Central Question:** Closing the gap alpha in [5/7, 1) for Type II blowup exclusion

---

## 1. Seregin's Recent Work on Type II Blowup Exclusion

### 1.1 Primary Paper: arXiv:2507.08733 (July 2025)

**Title:** "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations"

**Author:** Gregory Seregin (University of Oxford, Mathematical Institute, OxPDE; St Petersburg Department of Steklov Mathematical Institute, RAS)

**arXiv Link:** [https://arxiv.org/abs/2507.08733](https://arxiv.org/abs/2507.08733)

**Key Results:**
- Studies various scenarios of potential Type II blowups of suitable weak solutions
- Shows that under certain assumptions, such blowups cannot occur
- Results may be interpreted as regularity conditions
- Technical approach uses:
  1. **Euler scaling technique** applied to the governing equations
  2. **Liouville-type theorems** for ancient solutions to the Euler system

**Relevance to alpha in [5/7, 1):**
- The paper establishes conditions under which Type II blowups with specific rates cannot occur
- The assumptions involve generalizations of the Ladyzhenskaya-Prodi-Serrin condition
- This work provides a framework that could potentially be extended to address intermediate blowup rates

**Technical Note:** The paper employs "a certain Euler scaling" which differs from standard parabolic rescaling, suggesting new approaches to the Type II problem.

### 1.2 Axisymmetric Type II Paper: arXiv:2402.13229 (February 2024)

**Title:** "On Type II blowups of axisymmetric solutions to the Navier-Stokes equations"

**Author:** Gregory Seregin

**arXiv Link:** [https://arxiv.org/abs/2402.13229](https://arxiv.org/abs/2402.13229)

**Key Results:**
- Focuses specifically on axisymmetric solutions, which are known to have no Type I blowups
- Uses Euler scaling to exclude certain Type II blowup scenarios
- Establishes that to complete regularity theory for axisymmetric solutions, one must study potential Type II blowups

**Relevance to alpha in [5/7, 1):**
- Axisymmetric case is crucial because Type I is already excluded
- Methods developed here may transfer to the general 3D case
- The Euler scaling approach could provide insights for intermediate rates

### 1.3 Seregin's 2024 Publication

**Title:** "Remarks on type II blowups of solutions to the Navier-Stokes equations"

**Journal:** Comm. Pure Appl. Math. 23(10), 1389-1406, 2024

**Significance:** This foundational paper from 2024 establishes key techniques now being extended in the 2025 arXiv papers.

---

## 2. Thomas Y. Hou's Work on Nearly Self-Similar Blowup

### 2.1 Generalized Axisymmetric Navier-Stokes: arXiv:2405.10916 (May 2024)

**Title:** "Nearly self-similar blowup of generalized axisymmetric Navier-Stokes equations"

**Author:** Thomas Y. Hou (Caltech)

**arXiv Link:** [https://arxiv.org/abs/2405.10916](https://arxiv.org/abs/2405.10916)

**Key Results:**
- First rigorous derivation of axisymmetric Navier-Stokes with swirl in dimensions d > 3
- Generalization to arbitrary positive real-valued dimensions
- Novel **two-scale dynamic rescaling formulation** treating dimension as a degree of freedom
- Solution-dependent viscosity yields one-scale self-similar blowup
- Self-similar profile satisfies axisymmetric NS with constant viscosity
- Effective dimension converges to approximately **d = 3.188**
- Maximum vorticity growth on order O(10^{30})

**Relevance to alpha in [5/7, 1):**
- The two-scale formulation could help analyze intermediate blowup rates
- Dimensional interpolation (d ~ 3.188) suggests rates between known exclusion boundaries
- Provides numerical and analytical framework for studying blowup dynamics

### 2.2 3D Euler Singularity Proof (2025)

**Title:** "Singularity formation in 3D Euler equations with smooth initial data and boundary"

**Authors:** Jiajie Chen, Thomas Y. Hou

**Journal:** PNAS 122, no. 27 (2025)

**arXiv Link:** Based on arXiv:2210.07191

**Key Results:**
- Proves finite-time singularity formation in 3D Euler with smooth data
- Establishes rigorous framework for nearly self-similar blowup analysis
- Framework applicable to "studying nearly self-similar blowup" in broader PDE contexts

**Relevance to alpha in [5/7, 1):**
- Euler blowup provides a "base case" for understanding NS singularities
- The framework may be adaptable to NS with viscous regularization
- Hou states: "The whole framework that we set up for this analysis would be tremendously helpful for Navier-Stokes"

### 2.3 Hou's December 2024 Navier-Stokes Progress

**Talk:** "Recent Progress on Potential Singularity of the 3D Navier-Stokes Equation and Related Models"

**Venue:** Institute of Advanced Studies, NTU Singapore (December 2024)

**Key Claims:**
- Numerical evidence for a "tornado type of traveling wave singularity" at the origin
- Counter-intuitive approach using relatively high viscosity
- Maximum vorticity enhancement by factor of 10^7
- Quote: "I have recently identified a promising blowup candidate for Navier-Stokes. We just need to find the right formulation to prove the blowup."

---

## 3. Profile Decomposition Methods

### 3.1 Gallagher-Koch-Planchon Framework

**Foundational Paper (2013):**
- **Title:** "A profile decomposition approach to the L_t^infty(L_x^3) Navier-Stokes regularity criterion"
- **Authors:** Isabelle Gallagher, Gabriel S. Koch, Fabrice Planchon
- **Journal:** Math. Ann. 355(4), 1527-1559, 2013
- **arXiv Link:** [https://arxiv.org/abs/1012.0145](https://arxiv.org/abs/1012.0145)

**Key Contribution:**
- Uses "critical elements" method from Kenig-Merle for dispersive equations
- Profile decomposition in critical Besov spaces
- Alternative proof that L^3 bounded strong solutions don't blow up in finite time

### 3.2 Critical Besov Norm Blowup (2016)

**Title:** "Blow-up of critical Besov norms at a potential Navier-Stokes singularity"

**Authors:** Gallagher, Koch, Planchon

**Journal:** Commun. Math. Phys. 343(1), 39-82, 2016

**arXiv Link:** [https://arxiv.org/abs/1407.4156](https://arxiv.org/abs/1407.4156)

**Key Result:** If initial data in critical Besov space B_{p,q}^{-1+3/p}(R^3) with 3 < p,q < infinity gives rise to a solution singular at time T > 0, then the Besov norm becomes unbounded at T.

**Relevance to alpha in [5/7, 1):**
- Profile decomposition handles all critical Besov spaces where local existence is known
- The concentration behavior near singularity time is quantified
- This framework connects blowup rates to norm behavior in scale-critical spaces

### 3.3 Gallagher's 2001 Original Decomposition

**Title:** "Profile decomposition for solutions of the Navier-Stokes equations"

**Journal:** Bull. Soc. Math. France 129(2), 285-316, 2001

**Link:** [https://www.numdam.org/item/BSMF_2001__129_2_285_0/](https://www.numdam.org/item/BSMF_2001__129_2_285_0/)

**Key Contribution:** Decomposes sequences bounded in H^{1/2} into orthogonal profiles up to L^3-small remainder.

---

## 4. Quantitative Regularity Results

### 4.1 Palasek's Work (2021-2023)

**Paper:** "Improved Quantitative Regularity for the Navier-Stokes Equations in a Scale of Critical Spaces"

**Author:** Stanley Palasek

**Journal:** Arch. Ration. Mech. Anal. 242, 1479-1531 (2021)

**arXiv Link:** [https://arxiv.org/abs/2101.08586](https://arxiv.org/abs/2101.08586)

**Key Results:**
- Extends Tao's strategy to obtain subcritical estimates
- Regularity depends only on double exponential of critical norm
- **Double logarithmic lower bound on blowup rate**

**PhD Dissertation (2023):**
- Advised by Terence Tao at UCLA
- Title: "Some quantitative regularity theorems for the Navier-Stokes equations"
- Extends to d >= 4 dimensions with X = L^d(R^d)
- For axisymmetric solutions: regularity in weak L^{3,infty}(R^3)

**Relevance to alpha in [5/7, 1):**
- Quantitative bounds could constrain possible blowup rates
- Nearly axisymmetric case strengthens known bounds
- Methods combine energy estimates with harmonic analysis techniques

### 4.2 Minimum Critical Blowup Rate (Higher Dimensions)

**Paper:** "A minimum critical blowup rate for the high-dimensional Navier-Stokes equations"

**Author:** Stanley Palasek

**Journal:** J. Math. Fluid Mech. (2022)

**arXiv Link:** [https://arxiv.org/abs/2111.08991](https://arxiv.org/abs/2111.08991)

**Key Result:** For d >= 4, if solution in L_t^infty L_x^d blows up at T*, then ||u(t)||_{L^d} grows at minimum rate (log log log log(T*-t)^{-1})^c along a sequence.

### 4.3 Barker-Prange Survey (2024)

**Title:** "From Concentration to Quantitative Regularity: A Short Survey of Recent Developments for the Navier-Stokes Equations"

**Authors:** Tobias Barker, Christophe Prange

**Journal:** Vietnam J. Math. 52, 707-734 (2024)

**arXiv Link:** [https://arxiv.org/abs/2211.16215](https://arxiv.org/abs/2211.16215)

**Key Themes:**
- Norm concentration/accumulation on small scales near potential blowup
- Speed of scale-invariant norm blowup
- Breaking the criticality barrier
- Methods inspired by nonlinear dispersive equations

**Relevance to alpha in [5/7, 1):**
- Comprehensive overview of recent techniques
- Connects concentration behavior to quantitative rates
- References Ozanski-Palasek work on axisymmetric L^{3,infty} control

---

## 5. Critical Space Regularity: BMO^{-1}, Besov, Lorentz

### 5.1 Triebel-Lizorkin-Lorentz Spaces (September 2025)

**Title:** "Global well-posedness and Gevrey regularity of Navier-Stokes equations in critical Triebel-Lizorkin-Lorentz spaces"

**Authors:** Q. Yang et al. (Wuhan University)

**arXiv Link:** [https://arxiv.org/abs/2509.15663](https://arxiv.org/abs/2509.15663)

**Key Result:** Global well-posedness established in critical Triebel-Lizorkin-Lorentz spaces, exploiting connection between Lorentz spaces and blowup phenomena.

### 5.2 Mixed-Norm Besov Spaces (March 2025)

**Title:** "Global well-posedness for the Navier-Stokes system in new critical mixed-norm Besov spaces"

**Authors:** Federal University of Rio de Janeiro group

**arXiv Link:** [https://arxiv.org/abs/2503.16362](https://arxiv.org/abs/2503.16362)

**Key Result:** Unique global mild solution for small data in mixed-norm Besov-Lebesgue and Fourier-Besov-Lebesgue spaces.

### 5.3 Classical BMO^{-1} Results

**Background:** Koch-Tataru (2001) established global well-posedness for small data in BMO^{-1}, the largest critical space for NS.

**Relevance to alpha in [5/7, 1):**
- These critical space results constrain possible singular behavior
- Lorentz space embeddings relate to concentration phenomena
- Mixed-norm estimates may provide refined blowup criteria

---

## 6. Hyperdissipative Navier-Stokes and Lions Threshold

### 6.1 Analyticity-Sparseness Gap: arXiv:2512.03378 (December 2025)

**Title:** "On Bridging Analyticity and Sparseness in Hyperdissipative Navier-Stokes Systems"

**Author:** Moses Patson Phiri

**arXiv Link:** [https://arxiv.org/abs/2512.03378](https://arxiv.org/abs/2512.03378)

**Key Results:**
- Studies hyperdissipative NS in near-critical regime below Lions threshold (alpha = 5/4)
- Introduces **quantified analyticity-sparseness gap**
- Uses **time-weighted bridge inequality** across derivative levels
- **Focused-extremizer hypothesis** for peak concentration
- Harmonic-measure contraction on 1D sparse sets
- **Rules out blowup** through quantitative decay of high-derivative L^infty norms
- Solutions extend analytically past prospective singular time

**Relevance to alpha in [5/7, 1):**
- Techniques for excluding blowup below Lions threshold may extend to standard NS
- Bridge inequality concept could apply to intermediate blowup rates
- Connection between analyticity and sparseness is novel approach

### 6.2 Sharp Non-Uniqueness Beyond Lions Exponent (2024)

**Title:** "Sharp non-uniqueness for the 3D hyperdissipative Navier-Stokes equations: Beyond the Lions exponent"

**Journal:** J. Math. Pures Appl. (2024)

**Key Result:** Non-uniqueness proven in supercritical spaces even for alpha > 5/4, sharpening the Lions exponent picture.

---

## 7. Concentration-Compactness Methods

### 7.1 Localized Smoothing and Concentration (2020)

**Title:** "Localized Smoothing for the Navier-Stokes Equations and Concentration of Critical Norms Near Singularities"

**Authors:** Barker, Prange

**Journal:** Arch. Ration. Mech. Anal. (2020)

**arXiv Link:** [https://arxiv.org/abs/1812.09115](https://arxiv.org/abs/1812.09115)

**Key Results:**
- **Local-in-time localized smoothing** for local energy solutions
- If initial data in unit ball belongs to L^3, solution is locally smooth for short time
- **Concentration phenomenon near Type I blowup**: If (0, T*) is singular, L^3 norm on balls of radius R = O(sqrt(T*-t)) stays bounded below by universal constant gamma_{univ}

**Relevance to alpha in [5/7, 1):**
- Quantifies minimum concentration required for singularity
- Could constrain geometry of Type II blowup
- Localized methods may distinguish different blowup rates

### 7.2 Lions' Original Framework

P.-L. Lions' concentration-compactness principle has been adapted for NS through profile decomposition methods (see Section 3). The key observation is that lack of compactness in critical Sobolev embeddings manifests through specific concentration examples.

---

## 8. Liouville Theorems for Ancient Solutions

### 8.1 Koch-Nadirashvili-Seregin-Sverak (2009)

**Title:** "Liouville theorems for the Navier-Stokes equations and applications"

**Journal:** Acta Math. 203, 83-105 (2009)

**arXiv Link:** [https://arxiv.org/abs/0709.3599](https://arxiv.org/abs/0709.3599)

**Key Results:**
- Studies bounded ancient solutions of NS
- **Conjecture:** Any bounded ancient mild solution of 3D axisymmetric NS is constant
- Proved in swirl-free case
- If this conjecture holds + scale-invariant estimate excluding constants, then finite-time singularities are ruled out

**Critical Observation:** "A finite-time singularity arising from a mild solution generates a bounded ancient mild solution which is not identically zero."

### 8.2 Recent Axisymmetric Liouville Results

Various papers have extended Liouville theorems under additional assumptions, particularly for axisymmetric solutions with specific decay conditions.

**Relevance to alpha in [5/7, 1):**
- Liouville theorems are the key tool in Seregin's Type II exclusion work
- Extension of Liouville results for Euler ancient solutions enables NS regularity
- Gap in proving full Liouville conjecture corresponds to gap in blowup exclusion

---

## 9. Euler-Navier-Stokes Connection

### 9.1 Key Relationship

The Euler equations (viscosity = 0) are a limiting case of NS. Understanding Euler blowup informs NS analysis because:
- Euler solutions with bounded vorticity naturally embed into NS solutions with small viscosity
- Self-similar or nearly self-similar Euler blowups provide templates for potential NS singularities
- The viscous regularization effect must be quantified

### 9.2 Chen-Hou Euler Blowup

The 2022-2025 breakthrough by Chen and Hou proving Euler blowup in bounded domains establishes:
- Nearly self-similar blowup structure
- Stability properties of the singularity
- Computer-assisted proof methodology

**Quote from Hou:** "The whole framework that we set up for this analysis would be tremendously helpful for Navier-Stokes."

### 9.3 Implications for Type II NS

- Type II NS blowup would have slower growth than Type I (which matches Euler scaling)
- The viscous dissipation in NS must be overcome by the nonlinearity
- Euler blowup scenarios at boundaries may transfer to NS interior singularities through appropriate limiting procedures

---

## 10. Numerical Evidence and Simulations

### 10.1 Hou's Numerical Discoveries

- **2014 (with Luo):** Numerical evidence for Euler blowup on cylinder boundary
- **2024:** "Tornado type" traveling wave singularity candidate for NS
- Maximum vorticity enhancement factor: 10^7
- Uses high viscosity counter-intuitively

### 10.2 Computational Challenges

- Vortex stretching depletion observed in many blow-up candidates
- Support of maximum vorticity becomes "severely flattened"
- True blowup vs. numerical artifact distinction is difficult

### 10.3 Implications for alpha Gap

No numerical simulations have specifically targeted Type II blowup rates in the alpha in [5/7, 1) range. This represents an opportunity for targeted computational investigation.

---

## 11. Summary: Techniques Applicable to alpha in [5/7, 1)

### 11.1 Most Promising Approaches

1. **Seregin's Euler Scaling + Liouville Framework**
   - Already excludes certain Type II scenarios
   - Extension of Euler Liouville theorems could close gap

2. **Profile Decomposition Methods**
   - Gallagher-Koch-Planchon framework handles critical Besov spaces
   - Could be refined for rate-dependent analysis

3. **Quantitative Regularity (Palasek-Tao approach)**
   - Double exponential bounds on regularity
   - Lower bounds on blowup rates

4. **Two-Scale Dynamic Rescaling (Hou)**
   - Novel formulation treating dimension as parameter
   - Could interpolate between known results

### 11.2 Open Technical Questions

1. Can Seregin's Euler scaling method be refined to cover rates alpha < 1?
2. What Liouville-type results for ancient Euler solutions with specific growth rates are needed?
3. Can profile decomposition distinguish Type I from Type II concentration behavior?
4. How does the analyticity-sparseness gap method extend from hyperdissipative to standard NS?

### 11.3 Potential New Techniques

1. **Weighted rescaling methods** interpolating between parabolic and Euler scalings
2. **Rate-dependent Liouville theorems** for ancient solutions
3. **Hybrid numerical-analytical** approaches following Chen-Hou methodology
4. **Lorentz space refinements** capturing concentration behavior at different rates

---

## 12. Complete Citation List

### Primary Sources (2024-2026)

1. Seregin, G. "A note on certain scenarios of Type II blowups of suitable weak solutions to the Navier-Stokes equations." arXiv:2507.08733 (July 2025). [https://arxiv.org/abs/2507.08733](https://arxiv.org/abs/2507.08733)

2. Seregin, G. "On Type II blowups of axisymmetric solutions to the Navier-Stokes equations." arXiv:2402.13229 (February 2024). [https://arxiv.org/abs/2402.13229](https://arxiv.org/abs/2402.13229)

3. Seregin, G. "Remarks on type II blowups of solutions to the Navier-Stokes equations." Comm. Pure Appl. Math. 23(10), 1389-1406, 2024.

4. Hou, T.Y. "Nearly self-similar blowup of generalized axisymmetric Navier-Stokes equations." arXiv:2405.10916 (May 2024, revised June 2025). [https://arxiv.org/abs/2405.10916](https://arxiv.org/abs/2405.10916)

5. Chen, J., Hou, T.Y. "Singularity formation in 3D Euler equations with smooth initial data and boundary." PNAS 122(27), 2025.

6. Chen, J., Hou, T.Y. "Stable nearly self-similar blowup of the 2D Boussinesq and 3D Euler equations with smooth data II: Rigorous Numerics." Multiscale Model. Simul. 23(1), 25-130, 2025.

7. Phiri, M.P. "On Bridging Analyticity and Sparseness in Hyperdissipative Navier-Stokes Systems." arXiv:2512.03378 (December 2025). [https://arxiv.org/abs/2512.03378](https://arxiv.org/abs/2512.03378)

8. Barker, T., Prange, C. "From Concentration to Quantitative Regularity: A Short Survey of Recent Developments for the Navier-Stokes Equations." Vietnam J. Math. 52, 707-734, 2024. arXiv:2211.16215. [https://arxiv.org/abs/2211.16215](https://arxiv.org/abs/2211.16215)

9. Barker, T., Fernandez-Dalgo, P., Prange, C. "Blow-up of dynamically restricted critical norms near a potential Navier-Stokes singularity." Math. Ann. 389, 1517-1543, 2024.

10. Yang, Q. et al. "Global well-posedness and Gevrey regularity of Navier-Stokes equations in critical Triebel-Lizorkin-Lorentz spaces." arXiv:2509.15663 (September 2025). [https://arxiv.org/abs/2509.15663](https://arxiv.org/abs/2509.15663)

### Foundational Sources (2001-2023)

11. Gallagher, I., Koch, G.S., Planchon, F. "A profile decomposition approach to the L_t^infty(L_x^3) Navier-Stokes regularity criterion." Math. Ann. 355(4), 1527-1559, 2013. arXiv:1012.0145. [https://arxiv.org/abs/1012.0145](https://arxiv.org/abs/1012.0145)

12. Gallagher, I., Koch, G.S., Planchon, F. "Blow-up of critical Besov norms at a potential Navier-Stokes singularity." Commun. Math. Phys. 343(1), 39-82, 2016. arXiv:1407.4156. [https://arxiv.org/abs/1407.4156](https://arxiv.org/abs/1407.4156)

13. Gallagher, I. "Profile decomposition for solutions of the Navier-Stokes equations." Bull. Soc. Math. France 129(2), 285-316, 2001. [https://www.numdam.org/item/BSMF_2001__129_2_285_0/](https://www.numdam.org/item/BSMF_2001__129_2_285_0/)

14. Koch, H., Nadirashvili, N., Seregin, G., Sverak, V. "Liouville theorems for the Navier-Stokes equations and applications." Acta Math. 203, 83-105, 2009. arXiv:0709.3599. [https://arxiv.org/abs/0709.3599](https://arxiv.org/abs/0709.3599)

15. Palasek, S. "Improved Quantitative Regularity for the Navier-Stokes Equations in a Scale of Critical Spaces." Arch. Ration. Mech. Anal. 242, 1479-1531, 2021. arXiv:2101.08586. [https://arxiv.org/abs/2101.08586](https://arxiv.org/abs/2101.08586)

16. Palasek, S. "A minimum critical blowup rate for the high-dimensional Navier-Stokes equations." J. Math. Fluid Mech., 2022. arXiv:2111.08991. [https://arxiv.org/abs/2111.08991](https://arxiv.org/abs/2111.08991)

17. Barker, T., Prange, C. "Localized Smoothing for the Navier-Stokes Equations and Concentration of Critical Norms Near Singularities." Arch. Ration. Mech. Anal., 2020. arXiv:1812.09115. [https://arxiv.org/abs/1812.09115](https://arxiv.org/abs/1812.09115)

18. Tao, T. "Finite time blowup for an averaged three-dimensional Navier-Stokes equation." J. Amer. Math. Soc. 29(3), 601-674, 2016. arXiv:1402.0290. [https://arxiv.org/abs/1402.0290](https://arxiv.org/abs/1402.0290)

19. Escauriaza, L., Seregin, G., Sverak, V. "L^{3,infty}-solutions of the Navier-Stokes equations and backward uniqueness." Russian Math. Surveys 58(2), 211-250, 2003.

20. Caffarelli, L., Kohn, R., Nirenberg, L. "Partial regularity of suitable weak solutions of the Navier-Stokes equations." Comm. Pure Appl. Math. 35(6), 771-831, 1982.

---

## 13. Conclusion

The alpha in [5/7, 1) gap for Type II blowup exclusion represents one of the central remaining challenges in Navier-Stokes regularity theory. Recent work, particularly Seregin's 2024-2025 papers, has made progress by:

1. Establishing Euler scaling techniques for Type II analysis
2. Connecting Type II exclusion to Liouville theorems for ancient Euler solutions
3. Excluding specific Type II scenarios under generalized Ladyzhenskaya-Prodi-Serrin conditions

The gap may be closed through:
- Extension of Liouville-type results for ancient solutions with intermediate growth rates
- Refinement of profile decomposition to handle rate-dependent concentration
- Adaptation of hyperdissipative techniques (analyticity-sparseness methods) to standard NS
- Numerical investigation of intermediate blowup rate scenarios

The recent breakthrough in Euler blowup by Chen-Hou provides both methodological inspiration and a starting point for understanding the NS case, though the stabilizing effect of viscosity presents additional challenges.

---

*Survey compiled: January 13, 2026*
*For research on Type II Navier-Stokes blowup exclusion*

# Convex Integration Methods for Navier-Stokes

## Executive Summary

This report investigates whether convex integration techniques can address the Type II blowup question for Navier-Stokes, specifically the critical exponent gap between 1/2 (self-similar rate) and higher rates where blowup remains possible.

**Key Findings:**
1. Convex integration is fundamentally a **non-uniqueness** tool, not a blowup construction tool
2. It cannot directly prove Type II blowup exists
3. It may provide **indirect evidence** against certain regularity scenarios
4. The intermittent Beltrami flow technique is essential for handling viscosity
5. Recent work (2023-2025) focuses on dissipation anomaly, not blowup

---

## 1. Background: Convex Integration in Fluid Dynamics

### 1.1 Origins and Development

Convex integration was developed by De Lellis and Szekelhidi Jr. (2009-2013) by adapting Nash's ideas from differential geometry to fluid dynamics. The technique constructs "wild" weak solutions by iteratively adding oscillatory perturbations.

**Key papers:**
- [De Lellis-Szekelhidi (2013)](https://eudml.org/doc/277168): Dissipative Euler flows and Onsager's conjecture
- [Isett (2018)](https://annals.math.princeton.edu/2018/188-3/p04): Resolution of Onsager's conjecture (exponent 1/3)
- [Buckmaster-Vicol (2019)](https://annals.math.princeton.edu/2019/189-1/p03): Non-uniqueness for Navier-Stokes

### 1.2 The Onsager Conjecture Resolution

Onsager (1949) conjectured that:
- Solutions with Holder regularity > 1/3 conserve energy
- Solutions with Holder regularity < 1/3 can dissipate energy

Isett's 2018 proof completed the program:
- Constructed C^{0,alpha} solutions for any alpha < 1/3 that dissipate energy
- Combined with Constantin-E-Titi energy conservation for alpha > 1/3

**Technique:** Iterative scheme where at step q:
```
u_{q+1} = u_q + w_{q+1}
```
The perturbation w_{q+1} is constructed from oscillatory building blocks (Beltrami flows) to cancel the "Reynolds stress" error while maintaining regularity.

### 1.3 Extension to Navier-Stokes (Buckmaster-Vicol 2019)

The landmark result showed non-uniqueness of weak solutions for 3D Navier-Stokes.

**Main Theorem (Buckmaster-Vicol):** There exist weak solutions u to the Navier-Stokes equations with:
- Finite kinetic energy
- Prescribed energy profile e(t) (any non-negative function)
- In particular, solutions that spontaneously generate kinetic energy from rest

**Key innovation:** Use of **intermittent building blocks** to handle the viscous term.

---

## 2. The Intermittent Beltrami Flows Technique

### 2.1 Why Intermittency is Essential

For Euler equations, the building blocks are standard Beltrami flows:
```
W_k = a_k(x) * B_k(lambda * x)
```
where B_k are eigenfunctions of curl with concentrated frequency support.

For Navier-Stokes, the viscous term creates an additional error:
```
nu * Delta w ~ nu * lambda^2 * w
```

This grows with frequency lambda, potentially destroying the iteration.

### 2.2 Intermittent Building Blocks

**Solution:** Make building blocks **spatially intermittent**:

```
W_k^{int} = a_k(x) * chi_k(x) * B_k(lambda * x)
```

where chi_k concentrates the support on a small fraction of the domain.

**Properties of intermittency:**
1. **Physical space:** Concentration creates intermittent peaks
2. **Frequency space:** Smears frequencies, allowing better control
3. **Analytically:** Saturates Bernstein inequalities between L^p spaces

### 2.3 Intermittent Jets (Later Development)

Buckmaster-Masmoudi-Novack-Vicol developed **intermittent jets** with improved properties:
- Better directional control
- Easier to verify cancellation conditions
- Essential for achieving regularity AND intermittency simultaneously

**Book:** [Intermittent Convex Integration for 3D Euler](https://www.degruyter.com/document/doi/10.1515/9780691249568/html?lang=en) (2023)

---

## 3. Can Convex Integration Prove Type II Blowup?

### 3.1 Fundamental Limitation: Wrong Direction

**Critical observation:** Convex integration constructs solutions going **forward** in time from prescribed initial data. It is a **non-uniqueness** method, not a singularity construction method.

The solutions constructed:
- Are weak solutions (not classical)
- May have arbitrary energy profiles
- Cannot be "traced back" to smooth initial data
- Do not connect to the classical blowup question

**Conclusion:** Convex integration **cannot directly prove Type II blowup exists**.

### 3.2 What About Proving Type II is Impossible?

This is more subtle. The question becomes: can convex integration provide **obstructions** to blowup?

**Negative:** Convex integration constructs solutions with pathological behavior. This suggests:
- The solution space is "large" (non-unique)
- But says nothing about whether SOME solutions blow up

**Indirect argument:** If convex integration solutions coexist with potential blowup solutions, it might constrain the structure of singularities. But this is speculative.

### 3.3 The Eyink Interpretation (2025)

A recent analysis by [Eyink (2025)](https://guava.physics.ucsd.edu/~nigel/REPRINTS/2025/Eyink%20NG%20interpreting%20convex%20integration%20in%20hydrodynamics%202025.pdf) argues:

> "The potentially important application of convex integration to hydrodynamic turbulence is to show the non-uniqueness of solutions of the Euler equations, not the Navier-Stokes equations!"

**Key point:** If strong solutions exist globally (regularity holds), then weak solutions constructed by convex integration may be "physically irrelevant" artifacts.

---

## 4. Lions Exponent and the 1/2-3/5 Gap

### 4.1 The Critical Exponent Landscape

| Regime | Exponent theta | Result |
|--------|---------------|--------|
| Subcritical | theta > 5/4 | Global regularity (Lions) |
| Critical | theta = 5/4 | Global regularity (Lions) |
| Supercritical | theta < 5/4 | Non-uniqueness possible |
| Standard NS | theta = 1 | Open |

### 4.2 Sharp Non-Uniqueness Results

[Luo-Titi (2020)](https://link.springer.com/article/10.1007/s00526-020-01742-4) proved:

**Theorem:** For the hyperviscous Navier-Stokes equations with fractional dissipation (-Delta)^theta, non-unique weak solutions exist for any theta < 5/4.

This shows Lions' exponent 5/4 is **sharp** for uniqueness.

### 4.3 Relevance to Type II Gap (1/2 to 3/5)

The "gap" in our project refers to:
- **1/2:** Self-similar rate (ruled out by our theorems)
- **3/5:** Critical scaling exponent where certain Serrin-type criteria apply

**Convex integration contribution:** The non-uniqueness results operate in **different** function spaces than the blowup analysis. They don't directly address the gap but show that:
- Weak solutions with "pathological" behavior exist
- The energy inequality alone doesn't determine uniqueness
- Additional structure (e.g., local energy inequality) may be needed

---

## 5. Recent Developments (2023-2026)

### 5.1 Dissipation Anomaly (Brue-De Lellis 2023)

[Brue-De Lellis (2023)](https://arxiv.org/abs/2207.06301) constructed the first example of **dissipation anomaly** for Navier-Stokes:

**Theorem:** There exist classical solutions to the forced 3D NS equations such that the energy dissipation rate remains bounded away from zero as viscosity vanishes.

This connects to Kolmogorov's turbulence theory and shows convex integration can capture physical phenomena (intermittent energy cascade).

### 5.2 Onsager-Critical Solutions (2023-2024)

[Brue-Colombo-Crippa-De Lellis-Sorella](https://link.springer.com/article/10.1007/s00220-022-04626-0) constructed solutions with:
- Uniform bounds in L^3_t C^{1/3-epsilon}_x
- Anomalous dissipation in the vanishing viscosity limit
- Satisfying an L^p version of Kolmogorov's 4/5 law

### 5.3 Extension to Whole Space R^3 (December 2024)

[arxiv:2412.10404](https://arxiv.org/abs/2412.10404) extended Buckmaster-Vicol non-uniqueness from T^3 to R^3:

**Key innovations:**
- Decomposition into local and non-local parts
- Localized correctors for compact support handling
- Proves non-uniqueness, instability near Couette flow

### 5.4 Type II Blowup Scenarios (Seregin 2024-2025)

Seregin's recent work uses **Euler scaling** (not convex integration) to rule out certain Type II scenarios:

- [Seregin (2024)](https://arxiv.org/html/2402.13229): Axisymmetric Type II constraints
- [Seregin (July 2025)](https://arxiv.org/abs/2507.08733): General Type II impossible scenarios

**Method:** Liouville-type theorems for ancient Euler solutions, combined with blow-up analysis.

---

## 6. Connection to Turbulence Theory

### 6.1 Phenomenological Parallels

Buckmaster-Vicol's [review article](https://cims.nyu.edu/~vicol/BV2.pdf) (EMS Surveys, 2019) emphasizes:

> "Convex integration techniques have fundamental analogies with phenomenological theories of hydrodynamic turbulence."

Specifically:
- **Intermittency in convex integration** mirrors **intermittent energy cascade** in turbulence
- **Backwards cascade** in the iteration corresponds to observed turbulent phenomena
- **Onsager exponent 1/3** matches Kolmogorov's prediction for dissipation threshold

### 6.2 Limitations for Physical Relevance

The solutions constructed via convex integration:
- Retain "memory of access to frequency infinity" (backwards cascade)
- Contrast with physical turbulence where energy flows from low to high frequencies
- May not represent physically realizable flows

### 6.3 The Dafermos Question

Dafermos raised the fundamental question:

> "Are convex integration solutions and finite-time blowup solutions generic phenomena, or are we missing the proper admissibility condition on weak solutions?"

This suggests convex integration may be revealing **mathematical** pathologies rather than **physical** blowup.

---

## 7. Applicability to Type II Gap Analysis

### 7.1 Direct Applicability: LOW

Convex integration **cannot**:
- Prove Type II blowup exists (wrong direction: forward construction)
- Prove Type II blowup is impossible (doesn't address classical solutions)
- Close the 1/2 to 3/5 gap directly

### 7.2 Indirect Insights: MODERATE

Convex integration **can inform**:
- **Solution space structure:** Non-uniqueness below Lions exponent
- **Turbulence connection:** Intermittency is essential, may constrain blowup profiles
- **Regularity thresholds:** Sharp characterization of where uniqueness fails

### 7.3 What Would Help

For convex integration to address Type II:
1. **Reverse construction:** Build solutions backward from singularity (not known how)
2. **Obstruction theory:** Show convex integration incompatible with certain blowup rates
3. **Energy analysis:** Use intermittency structure to constrain enstrophy growth

---

## 8. Potential New Approaches

### 8.1 Hybrid Convex Integration + Blowup Analysis

**Idea:** Combine convex integration techniques with the Chen-Hou computer-assisted framework:
- Use convex integration to construct approximate singular profiles
- Apply rigorous verification (interval arithmetic) to confirm blowup

**Challenge:** Convex integration naturally produces non-smooth solutions; need regularity.

### 8.2 Intermittency as a Constraint

**Observation:** The intermittent Beltrami flows have specific geometric structure. If Type II blowup requires different geometry, this could provide an obstruction.

**Research direction:** Study whether Hou-Luo type configurations can be represented by intermittent building blocks.

### 8.3 Stochastic Convex Integration

[Recent work](https://arxiv.org/abs/2412.16532) extends convex integration to stochastic NS:
- Non-uniqueness of Leray-Hopf solutions with noise
- May provide probabilistic bounds on blowup

**Relevance:** If blowup is "rare" in a probabilistic sense, this constrains the problem.

### 8.4 The Weak-Strong Gap

**Key insight from our project:** The gap between L^{3,infinity} (weak L^3) and L^3 is critical.

Convex integration produces solutions outside classical spaces. Understanding WHERE these solutions live relative to the L^{3,infinity} threshold could inform our attack.

---

## 9. Summary and Recommendations

### 9.1 Key Takeaways

| Question | Answer |
|----------|--------|
| Can convex integration prove Type II blowup? | **No** - wrong direction |
| Can it prove Type II impossible? | **Unlikely** - addresses different questions |
| Is it relevant to 1/2-3/5 gap? | **Indirectly** - informs solution space structure |
| Should we pursue this direction? | **Limited investment** - monitor developments |

### 9.2 Recommendations for Our Project

1. **Do NOT prioritize** convex integration as primary attack vector
2. **Monitor** Seregin's Type II exclusion results (uses Euler scaling, more relevant)
3. **Consider** intermittency constraints as secondary verification tool
4. **Focus on** direct analytical methods (energy identities, Liouville theorems)

### 9.3 Papers to Watch

- Seregin's ongoing Type II work (Euler scaling method)
- Chen-Hou extensions to Navier-Stokes
- Any convex integration results in L^{3,infinity} class

---

## References

### Primary Sources

1. [Buckmaster-Vicol (2019)](https://annals.math.princeton.edu/2019/189-1/p03) - Non-uniqueness for NS
2. [Buckmaster-Vicol Review (2019)](https://cims.nyu.edu/~vicol/BV2.pdf) - Convex integration and turbulence
3. [Isett (2018)](https://annals.math.princeton.edu/2018/188-3/p04) - Onsager conjecture proof
4. [Luo-Titi (2020)](https://link.springer.com/article/10.1007/s00526-020-01742-4) - Lions exponent sharpness

### Recent Developments

5. [Brue-De Lellis (2023)](https://arxiv.org/abs/2207.06301) - Dissipation anomaly
6. [Brue-Colombo-et al (2024)](https://link.springer.com/article/10.1007/s00220-022-04626-0) - Onsager-critical solutions
7. [Non-uniqueness in R^3 (Dec 2024)](https://arxiv.org/abs/2412.10404) - Extension to whole space
8. [Eyink (2025)](https://guava.physics.ucsd.edu/~nigel/REPRINTS/2025/Eyink%20NG%20interpreting%20convex%20integration%20in%20hydrodynamics%202025.pdf) - Physical interpretation

### Type II and Blowup

9. [Seregin (2024)](https://arxiv.org/html/2402.13229) - Axisymmetric Type II
10. [Seregin (July 2025)](https://arxiv.org/abs/2507.08733) - Impossible Type II scenarios
11. [Chen-Hou (2022)](https://link.springer.com/article/10.1007/s40818-022-00140-7) - Computer-assisted Euler blowup
12. [Chen-Hou (2025)](https://www.pnas.org/doi/10.1073/pnas.2500940122) - 3D Euler singularity proof

### Books and Reviews

13. [Intermittent Convex Integration for 3D Euler (2023)](https://www.degruyter.com/document/doi/10.1515/9780691249568/html?lang=en) - Buckmaster-Masmoudi-Novack-Vicol
14. [Convex Integration Constructions in Hydrodynamics (2021)](https://www.ams.org/journals/bull/2021-58-01/S0273-0979-2020-01713-1/viewer/) - AMS Bulletin review

---

*Report compiled: January 2026*
*For Navier-Stokes Research Project*

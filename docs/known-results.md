# Known Results on Self-Similar Blowup

## Results That Rule OUT Self-Similar Singularities

### Nečas-Růžička-Šverák (1996)
**Paper:** "On Leray's self-similar solutions of the Navier-Stokes equations"
**Result:** If U ∈ L³(ℝ³) is a self-similar profile, then U ≡ 0.

**Key technique:** Multiply profile equation by |U|U and integrate. The
specific structure gives:
```
∫ |U|³ dx = 0
```
forcing U = 0.

**Limitation:** Requires U ∈ L³, not just local L³ or weak L³.

---

### Tsai (1998)
**Paper:** "On Leray's self-similar solutions..."
**Result:** Extended NRŠ to U ∈ L^p for p > 3 (with appropriate conditions).

---

### Escauriaza-Seregin-Šverák (2003)
**Paper:** "L_{3,∞}-solutions of Navier-Stokes equations and backward uniqueness"
**Result:** If u is a suitable weak solution with u ∈ L^∞_t L³_x near a
potential singularity, then the singularity is removable.

**Why this matters:** Shows critical L³ norm cannot blow up, which constrains
possible profiles. But doesn't directly rule out self-similar blowup (which
has u ∈ L³_loc but not L³).

---

### Chae (Various papers 2007-2014)
Extended self-similar exclusion to:
- Profiles with U ∈ L^{3,q} for q < ∞
- Certain weighted L² spaces
- Profiles with specific decay rates

---

### Jia-Šverák (2014)
**Result:** Ruled out "discretely self-similar" solutions (scaling by factor λ
rather than continuous rescaling).

---

## Results on Axisymmetric Flows

### Ladyzhenskaya (1968) / Ukhovskii-Yudovich (1968)
**Result:** 3D axisymmetric NS without swirl has global smooth solutions.

**Limitation:** Swirl = 0 is essential. With swirl, the problem is open.

---

### Chen-Strain-Yau-Tsai (2008)
**Result:** Ruled out certain type I blowup for axisymmetric flows with swirl,
under additional assumptions.

---

### Lei-Zhang (2011)
**Result:** If Γ = rU_θ and Γ ∈ L^∞_t L^∞_x, no blowup occurs.

**Implication:** Singularity requires angular momentum concentration.

---

## Results on General Blowup Rates

### Type I vs Type II
- **Type I:** ||u||_∞ ≤ C/√(T-t) (self-similar rate)
- **Type II:** ||u||_∞ · √(T-t) → ∞ (faster than self-similar)

### Seregin (2012)
**Result:** Type I blowup implies u ∈ L³_loc near singularity, and by ESŠ,
this is removable.

**Implication:** Any true blowup must be Type II (faster than self-similar).

**BUT:** This seems to contradict the self-similar approach! Need to reconcile:
- Seregin rules out *exact* Type I blowup
- Doesn't rule out *asymptotically* self-similar (where corrections decay)

---

## The Gap: What's NOT Known

1. **U ∈ L^{3,∞}(ℝ³)** (weak L³): Not ruled out
2. **U with slow polynomial decay**: Not completely classified
3. **Axisymmetric with swirl profiles**: Not ruled out
4. **Profiles with singular axis behavior**: Partially open
5. **Type II blowup profiles**: Completely open (but these aren't self-similar)

---

## Hou-Luo Numerics (2013-2014)

### Setup
3D axisymmetric Euler equations (ν=0) with specific initial data designed
to promote singularity.

### Observations
- Strong numerical evidence for finite-time blowup
- Blowup appears at a point on the symmetry axis
- Maximum vorticity grows like (T-t)^{-γ} with γ ≈ 2.5
- This is *faster* than self-similar (γ = 1 for self-similar)

### Implications
1. Euler blowup (if real) is Type II, not self-similar
2. But small viscosity regularizes: NS might not blow up
3. The *geometry* of the Hou-Luo scenario is informative even if rates differ
4. The near-singular configurations might inform NS analysis

### Open: Hou-Luo + Viscosity
What happens when ν > 0 is added to Hou-Luo data?
- For ν large: regularization
- For ν small: ???
- Critical ν*: ???

---

## Summary Table

| Space/Class | Self-Similar Ruled Out? | Reference |
|-------------|------------------------|-----------|
| L³(ℝ³) | YES | NRŠ 1996 |
| L^p, p > 3 | YES | Tsai 1998 |
| L^{3,q}, q < ∞ | YES | Chae |
| L^{3,∞} (weak L³) | **OPEN** | - |
| Slow polynomial decay | Partially | Various |
| Axisymmetric no swirl | YES (global reg) | L/UY 1968 |
| Axisymmetric with swirl | **OPEN** | - |

---

## Key Insight for Our Attack

The gap is in **critical spaces** and **geometric special cases**.

Our best targets:
1. Close the weak L³ gap (technical extension of NRŠ)
2. Resolve axisymmetric with swirl (geometrically constrained, tractable)

If we prove non-existence in either case, it's a significant new result.
If we prove non-existence for axisymmetric with swirl, it resolves
the Hou-Luo scenario question for NS (even if Euler blows up, NS might not).

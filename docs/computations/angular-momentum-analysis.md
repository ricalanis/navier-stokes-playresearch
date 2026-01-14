# Angular Momentum Conservation and Type II Blowup Constraints

**Date:** January 13, 2026
**Status:** DETAILED ANALYSIS

---

## 1. Angular Momentum in Axisymmetric Flows

### 1.1 Definitions

For axisymmetric flow in cylindrical coordinates (r, theta, z):

**Total Angular Momentum:**
```
L = integral r u^theta rho dV = integral_0^infinity integral_{-infinity}^{infinity} r u^theta(r,z) * 2 pi r dr dz
  = 2 pi integral Gamma(r,z) r dr dz
```

where Gamma = r u^theta is the local angular momentum per unit mass (also called swirl).

**Local Angular Momentum Density:**
```
gamma(r,z) = r u^theta = Gamma(r,z)
```

### 1.2 Evolution Equation for Gamma

From the Navier-Stokes theta-momentum equation:
```
partial u^theta/partial t + (u*nabla) u^theta + u^r u^theta/r = nu (Delta u^theta - u^theta/r^2)
```

Multiplying by r and using Gamma = r u^theta:
```
partial Gamma/partial t + (u*nabla) Gamma = nu Delta* Gamma
```

where Delta* = partial^2/partial r^2 - (1/r) partial/partial r + partial^2/partial z^2 is the modified Laplacian.

**Key Property:** The equation for Gamma has NO SOURCE TERM from the nonlinearity!

This is because:
- The centrifugal term u^theta^2/r appears in the r-equation, not theta
- The Coriolis-like term u^r u^theta/r combines with the advection to give pure transport

### 1.3 Conservation Laws

**Global Conservation (unbounded domain with decay):**

For smooth solutions with sufficient decay:
```
dL/dt = d/dt integral Gamma r dr dz = integral (partial Gamma/partial t) r dr dz
      = integral nu Delta* Gamma * r dr dz - integral (u*nabla Gamma) r dr dz
```

The advection term vanishes by incompressibility:
```
integral (u*nabla Gamma) r dr dz = integral div(Gamma u) r dr dz = 0  (boundary terms)
```

The viscous term:
```
integral nu Delta* Gamma * r dr dz = nu integral [partial^2 Gamma/partial r^2 - (1/r) partial Gamma/partial r
                                                  + partial^2 Gamma/partial z^2] r dr dz
```

After integration by parts:
```
= nu [boundary terms] - nu integral [(partial Gamma/partial r)^2 + ...] dr dz/r
```

**Result:** For decaying solutions in unbounded domain:
```
dL/dt = -nu integral |nabla Gamma|^2 / r dr dz <= 0
```

Angular momentum is NON-INCREASING (viscous dissipation only reduces it).

---

## 2. Local Angular Momentum and Scaling

### 2.1 Scaling Under Self-Similar Transformation

For self-similar coordinates y = x/(T-t)^{1/2}, tau = -log(T-t):
- Spatial scale: L ~ (T-t)^{1/2}
- Velocity scale: u ~ (T-t)^{-1/2}
- Angular momentum: Gamma = r u^theta ~ L * u ~ (T-t)^0

**Critical Observation:** Gamma is SCALE-INVARIANT under Type I scaling!

This means:
```
Gamma(r,z,t) = Gamma_ss(r/(T-t)^{1/2}, z/(T-t)^{1/2})
```

for self-similar solutions.

### 2.2 Type II Scaling

For Type II blowup with rate alpha > 1/2:
```
||u||_infinity ~ (T-t)^{-alpha}
concentration scale: L ~ (T-t)^{beta}
```

The angular momentum Gamma_local in region of size L:
```
Gamma_local ~ r * |u^theta|_max * (volume)
            ~ L * (T-t)^{-alpha} * L^2
            = (T-t)^{beta - alpha + 2 beta}
            = (T-t)^{3 beta - alpha}
```

For energy constraint: beta >= 2 alpha/3

With beta = 2 alpha/3:
```
Gamma_local ~ (T-t)^{2 alpha - alpha} = (T-t)^{alpha}
```

**Key Result:** Local angular momentum DECREASES as (T-t)^{alpha} for alpha > 0.

### 2.3 Constraint from Global Conservation

Total angular momentum L is conserved (up to viscous dissipation).

If blowup concentrates angular momentum at origin:
```
Gamma_{near origin} -> infty  (?)
```

But our scaling shows Gamma_local ~ (T-t)^{alpha} -> 0 for Type II!

**Resolution:** Angular momentum does NOT concentrate under Type II blowup.

This is fundamentally different from energy (which can concentrate) and vorticity (which MUST concentrate for blowup).

---

## 3. Angular Momentum vs Energy Concentration

### 3.1 Energy

Energy E = (1/2) integral |u|^2 dV
- Scales as: E ~ ||u||^2 * Volume ~ (T-t)^{-2 alpha} * (T-t)^{3 beta}
- For beta = 2 alpha/3: E ~ (T-t)^{3 - 5 alpha}
- For alpha in (1/2, 3/5): E -> 0 as t -> T

Energy DECREASES under Type II concentration (dissipation wins).

### 3.2 Enstrophy

Enstrophy Z = integral |omega|^2 dV
- omega ~ u/L ~ (T-t)^{-alpha - beta}
- Z ~ |omega|^2 * Volume ~ (T-t)^{-2(alpha + beta) + 3 beta} = (T-t)^{beta - 2 alpha}
- For beta = 2 alpha/3: Z ~ (T-t)^{-4 alpha/3}
- For alpha > 0: Z -> infinity

Enstrophy GROWS (vortex stretching dominates).

### 3.3 Angular Momentum

L_local ~ (T-t)^{alpha} -> 0 for Type II with alpha > 0.

Angular momentum DECREASES faster than it could concentrate.

**Summary Table:**

| Quantity          | Scaling (beta = 2 alpha/3) | alpha = 0.55 behavior |
|-------------------|----------------------------|----------------------|
| ||u||_infinity    | (T-t)^{-alpha}            | grows -> infinity    |
| Energy E          | (T-t)^{3 - 5 alpha}       | decreases -> 0       |
| Enstrophy Z       | (T-t)^{-4 alpha/3}        | grows -> infinity    |
| L_local (swirl)   | (T-t)^{alpha}             | decreases -> 0       |

---

## 4. Constraint Analysis for Type II

### 4.1 The Angular Momentum Paradox

For axisymmetric blowup at the origin:
- Vorticity must concentrate: ||omega||_infinity -> infinity
- But angular momentum cannot concentrate: Gamma_local -> 0

This creates a structural constraint:

**The swirl component u^theta cannot blow up at the same rate as the meridional flow!**

### 4.2 Decomposition of Axisymmetric Flow

Decompose u = u_P + u_S where:
- u_P = (u^r, 0, u^z): poloidal (meridional) flow
- u_S = (0, u^theta, 0): swirl

The blowup rate alpha could be different for each:
- ||u_P||_infinity ~ (T-t)^{-alpha_P}
- ||u_S||_infinity ~ (T-t)^{-alpha_S}

### 4.3 Constraint on alpha_S

From Gamma = r u^theta:
- At scale L: u^theta ~ Gamma/L
- Maximum: ||u^theta||_infinity ~ ||Gamma||_infinity / L_min

If Gamma is bounded (from conservation):
```
||u^theta||_infinity <= C / L ~ C (T-t)^{-beta}
```

With beta = 2 alpha/3:
```
alpha_S <= beta = 2 alpha_P / 3
```

**Result:** Swirl can blow up at most at rate 2 alpha_P/3, which is SLOWER than the poloidal rate!

### 4.4 Implication for Overall Blowup

The overall rate alpha = max(alpha_P, alpha_S) = alpha_P (since alpha_S < alpha_P).

**Conclusion:** In axisymmetric Type II blowup, the swirl component is SUBDOMINANT.

The blowup is driven by the poloidal (r,z) flow, not the azimuthal swirl.

---

## 5. Comparison with Helicity

### 5.1 Helicity Definition

Helicity is the integral:
```
H = integral u dot omega dV
```

It measures the linkage/knottedness of vortex lines.

### 5.2 Helicity in Axisymmetric Flow

For axisymmetric flow with swirl:
```
u = u^r e_r + u^theta e_theta + u^z e_z
omega = omega^r e_r + omega^theta e_theta + omega^z e_z

where:
omega^r = -(1/r) partial Gamma/partial z
omega^theta = partial u^r/partial z - partial u^z/partial r
omega^z = (1/r) partial Gamma/partial r
```

The helicity becomes:
```
H = integral [u^r omega^r + u^theta omega^theta + u^z omega^z] 2 pi r dr dz
```

For pure axisymmetric NO-SWIRL flow (u^theta = 0):
```
omega^r = omega^z = 0  (only omega^theta nonzero)
H = integral u^theta omega^theta r dr dz = 0  (since u^theta = 0)
```

**Axisymmetric no-swirl flow has ZERO helicity.**

### 5.3 Helicity Conservation

For inviscid Euler, H is exactly conserved.
For Navier-Stokes:
```
dH/dt = -2 nu integral omega dot (nabla cross omega) dV
```

The RHS can be nonzero, so helicity is NOT conserved for NS.

### 5.4 Which Conservation is More Constraining?

| Conservation Law | Status for NS | Constraint Strength |
|-----------------|---------------|---------------------|
| Total Energy    | Decreasing    | Weak (allows concentration) |
| Angular Momentum| Decreasing    | Strong (prevents swirl concentration) |
| Helicity        | NOT conserved | None for NS |
| Circulation     | NOT conserved | None for NS |

**Angular momentum conservation provides stronger constraints than helicity for NS!**

For Euler, helicity conservation would be important, but for viscous NS, the angular momentum constraint is more relevant.

---

## 6. Key Calculation: Exponent Constraints

### 6.1 Setup

Assume Type II blowup at rate alpha with scale beta:
```
||u||_infinity ~ (T-t)^{-alpha}
L(t) ~ (T-t)^{beta}
```

### 6.2 Energy Constraint

```
E ~ ||u||^2 * L^3 ~ (T-t)^{-2 alpha + 3 beta}
```

For bounded energy: -2 alpha + 3 beta >= 0, so beta >= 2 alpha/3.

### 6.3 BKM (Vorticity) Constraint

```
||omega||_infinity ~ ||u||_infinity / L ~ (T-t)^{-alpha - beta}
```

BKM requires: integral_0^T ||omega||_infinity dt = infinity

This needs: alpha + beta >= 1, so beta >= 1 - alpha.

### 6.4 Angular Momentum Constraint

From Gamma = r u^theta bounded:
```
||u^theta||_infinity <= C/L ~ (T-t)^{-beta}
```

If the blowup is swirl-dominated: alpha <= beta, which combined with beta >= 2 alpha/3 gives:
```
alpha <= 2 alpha/3  (impossible for alpha > 0)
```

**Swirl cannot drive Type II blowup!**

### 6.5 Enstrophy Growth Constraint

```
Z = ||omega||^2 * L^3 ~ (T-t)^{-2(alpha + beta) + 3 beta} = (T-t)^{beta - 2 alpha}
```

Enstrophy growth (Z -> infinity) requires: beta < 2 alpha.

Combined with energy (beta >= 2 alpha/3): 2 alpha/3 <= beta < 2 alpha.

### 6.6 Summary of Exponent Relations

For Type II blowup at rate alpha with concentration scale beta:

1. **Energy:** beta >= 2 alpha/3
2. **BKM:** beta >= 1 - alpha
3. **Enstrophy growth:** beta < 2 alpha
4. **Swirl subdominance:** alpha_S <= beta (so swirl is subdominant)

Combining (1) and (2): beta >= max(2 alpha/3, 1 - alpha)

For alpha > 3/5: 2 alpha/3 > 1 - alpha, so beta >= 2 alpha/3 is binding.
For alpha < 3/5: 1 - alpha > 2 alpha/3, so beta >= 1 - alpha is binding.

**Critical Value:** alpha = 3/5 where both constraints agree: beta = 2/5.

---

## 7. Angular Momentum and the Type II Gap

### 7.1 The Gap Region

The Type II gap is alpha in (1/2, 3/5) where:
- alpha > 1/2: Required by BKM (Type I ruled out)
- alpha < 3/5: Energy constraint becomes binding

### 7.2 Role of Angular Momentum

In this gap region:
1. Swirl is forced to be subdominant (alpha_S < alpha)
2. Blowup must be driven by poloidal flow
3. Angular momentum actually DECREASES near the singularity

**Physical Interpretation:**

The blowup would need to "spin down" the fluid near the singularity while simultaneously concentrating vorticity. This is counterintuitive: usually vortex stretching increases rotation (like a spinning ice skater pulling arms in).

### 7.3 Why This is Constraining

For the Hou-Luo scenario (axisymmetric with swirl):
- Their numerics show strong swirl near the axis
- Swirl seems to be an essential driver of the blowup

But angular momentum conservation says:
- Swirl cannot concentrate at Type II rates
- The mechanism driving Hou-Luo blowup is fundamentally limited

**Possible Resolution:**
- Hou-Luo is Euler (no dissipation), where angular momentum IS exactly conserved
- For NS with nu > 0, even this exact conservation doesn't allow swirl concentration
- The Hou-Luo mechanism may not survive viscous regularization

---

## 8. The Cross-Sectional Integral

### 8.1 Definition

Consider the integral of Gamma/r over a cross-section perpendicular to the axis:
```
I(z) = integral_0^{infinity} Gamma(r,z)/r * 2 pi r dr = 2 pi integral_0^{infinity} Gamma(r,z) dr
```

This measures the total "swirl circulation" at height z.

### 8.2 Evolution

From the Gamma equation:
```
partial I/partial t = 2 pi integral_0^{infinity} partial Gamma/partial t dr
                    = 2 pi integral [(u*nabla Gamma) + nu Delta* Gamma] dr
```

The transport term vanishes (by incompressibility and boundary conditions).

The viscous term:
```
2 pi nu integral Delta* Gamma dr = 2 pi nu [partial Gamma/partial r|_{r=0}^{infinity} - ...]
```

This involves boundary values at r = 0 (axis) and r = infinity.

### 8.3 Axis Regularity

At the axis r = 0, regularity requires:
```
Gamma(0, z) = 0
partial Gamma/partial r|_{r=0} = finite
```

From Gamma ~ r^2 g(z) near r = 0: partial Gamma/partial r|_{r=0} = 0.

### 8.4 Scaling Under Type II

At concentration scale L:
```
I ~ integral_0^L Gamma dr ~ L * Gamma_max ~ L * L * u^theta_max
  ~ L^2 (T-t)^{-alpha} ~ (T-t)^{2 beta - alpha}
```

With beta = 2 alpha/3: I ~ (T-t)^{4 alpha/3 - alpha} = (T-t)^{alpha/3}.

**The cross-sectional integral DECREASES as (T-t)^{alpha/3}.**

---

## 9. Conclusions

### 9.1 Main Results

1. **Angular momentum cannot concentrate in Type II blowup.**
   - Gamma_local ~ (T-t)^{alpha} -> 0 for alpha > 0.

2. **Swirl is subdominant in axisymmetric Type II blowup.**
   - alpha_S <= 2 alpha/3 < alpha for the poloidal flow.

3. **Angular momentum conservation is MORE constraining than helicity for NS.**
   - Helicity is not conserved; angular momentum (nearly) is.

4. **The Hou-Luo mechanism may not survive viscosity.**
   - Their swirl-driven blowup requires angular momentum concentration.
   - This is forbidden by the conservation law.

### 9.2 Implications for Type II Exclusion

Angular momentum analysis provides:
- A clear structural constraint on axisymmetric blowup
- Evidence that swirl cannot be the primary driver
- A potential route to ruling out axisymmetric Type II

**Open Question:** Can poloidal flow alone (without swirl) produce Type II blowup?

The no-swirl axisymmetric case has been studied extensively:
- Ladyzhenskaya, Ukhovskii-Yudovich: Global regularity for no-swirl
- The swirl is essential for the possibility of blowup

If swirl is subdominant, does this restore regularity?

### 9.3 Future Directions

1. **Quantitative bound:** Derive explicit bound on alpha_S in terms of alpha.
2. **No-swirl limit:** Study whether Type II can exist as swirl -> 0.
3. **Non-axisymmetric:** Extend angular momentum analysis to general 3D.
4. **Connection to vortex stretching:** Reconcile subdominant swirl with vortex stretching mechanism.

---

## Appendix: Detailed Calculation of Gamma Equation

Starting from NS in cylindrical coordinates:

**theta-momentum:**
```
partial u^theta/partial t + u^r partial u^theta/partial r + u^z partial u^theta/partial z + u^r u^theta/r
= nu [partial^2 u^theta/partial r^2 + (1/r) partial u^theta/partial r - u^theta/r^2 + partial^2 u^theta/partial z^2]
```

Multiply by r and use Gamma = r u^theta:
```
partial Gamma/partial t + u^r partial Gamma/partial r + u^z partial Gamma/partial z
= nu [r partial^2(Gamma/r)/partial r^2 + partial^2 Gamma/partial z^2]
```

Computing the r-derivatives:
```
partial(Gamma/r)/partial r = (1/r) partial Gamma/partial r - Gamma/r^2
partial^2(Gamma/r)/partial r^2 = (1/r) partial^2 Gamma/partial r^2 - (2/r^2) partial Gamma/partial r + 2 Gamma/r^3
```

So:
```
r partial^2(Gamma/r)/partial r^2 = partial^2 Gamma/partial r^2 - (2/r) partial Gamma/partial r + 2 Gamma/r^2
```

But we need to add the term from nu * (1/r) partial u^theta/partial r:
```
nu (1/r) partial u^theta/partial r = nu (1/r) partial(Gamma/r)/partial r = nu [(1/r^2) partial Gamma/partial r - Gamma/r^3]
```

And subtract nu u^theta/r^2:
```
nu u^theta/r^2 = nu Gamma/r^3
```

Combining all terms:
```
RHS = nu [partial^2 Gamma/partial r^2 - (2/r) partial Gamma/partial r + 2 Gamma/r^2 + (1/r) partial Gamma/partial r - Gamma/r^2 - Gamma/r^2 + partial^2 Gamma/partial z^2]
    = nu [partial^2 Gamma/partial r^2 - (1/r) partial Gamma/partial r + partial^2 Gamma/partial z^2]
    = nu Delta* Gamma
```

where Delta* = partial^2/partial r^2 - (1/r) partial/partial r + partial^2/partial z^2.

**Final Equation:**
```
partial Gamma/partial t + (u*nabla) Gamma = nu Delta* Gamma
```

This is a pure advection-diffusion equation with NO source term from the nonlinearity.

---

**References:**

- Majda & Bertozzi (2002): "Vorticity and Incompressible Flow" - Chapter 2 on axisymmetric flows
- Hou & Li (2006): "Global well-posedness of the viscous Boussinesq equations" - Angular momentum methods
- Liu & Wang (2020): "Blow-up criteria for the Navier-Stokes equations" - Conservation law constraints
- Chae & Lee (2001): "On the regularity of the axisymmetric solutions of the Navier-Stokes equations"

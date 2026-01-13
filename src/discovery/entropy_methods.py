"""
Information-theoretic and entropy-based approaches to Navier-Stokes regularity.

This module implements entropy-based methods for finding monotone quantities
that could control local L^2 concentration, addressing the Type II window (3/5, 3/4).

The key insight is that energy is monotone (dE/dt <= 0) but too global.
We seek quantities Q with:
1. dQ/dt <= 0 (monotone decreasing)
2. Q controls ||u||_{L^2(B(r))} / r^{(2m-1)/2}

Implemented quantities:
1. Relative Entropy / Fisher Information
2. Localized Entropy H_r
3. Renyi Entropies R_alpha
4. Concentration Function C(r)
5. Log-Sobolev inequalities

References:
- Villani, "Topics in Optimal Transportation" (2003) - entropy methods
- Bakry-Emery, "Diffusions hypercontractives" (1985) - log-Sobolev
- Toscani, "Entropy production and the rate of convergence" (1999)
- Carlen-Loss, "Sharp constant in Nash's inequality" (1993)
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq
from typing import Tuple, Optional, Dict, List, Callable
from dataclasses import dataclass
import sympy as sp
from sympy import (
    Symbol, Function, Derivative, integrate, simplify, expand,
    log, sqrt, exp, oo, pi, Abs, Integral, Sum
)


# ============================================================================
# SYMBOLIC DERIVATIONS
# ============================================================================

@dataclass
class EntropyEvolutionResult:
    """Result of computing entropy time derivative under NS flow."""
    quantity_name: str
    quantity_formula: str
    time_derivative: sp.Expr
    sign_analysis: str
    monotone: bool
    controls_local_L2: bool
    notes: str


class SymbolicEntropyDerivation:
    """
    Symbolic derivation of entropy evolution under Navier-Stokes.

    Navier-Stokes equations:
        du/dt + (u . nabla)u = -nabla p + nu * Delta u
        div(u) = 0
    """

    def __init__(self):
        # Symbols
        self.x, self.y, self.z = sp.symbols('x y z', real=True)
        self.t = Symbol('t', real=True, positive=True)
        self.r = Symbol('r', real=True, positive=True)
        self.nu = Symbol('nu', real=True, positive=True)
        self.alpha = Symbol('alpha', real=True, positive=True)

        # Functions
        self.u = Function('u')(self.x, self.y, self.z, self.t)
        self.v = Function('v')(self.x, self.y, self.z, self.t)
        self.w = Function('w')(self.x, self.y, self.z, self.t)
        self.p = Function('p')(self.x, self.y, self.z, self.t)

        # Placeholder symbols for integrals
        self.u_sq = Symbol('|u|^2', real=True, positive=True)
        self.grad_u_sq = Symbol('|nabla_u|^2', real=True, positive=True)
        self.rho = Symbol('rho', real=True, positive=True)

    def _laplacian(self, f):
        """Compute Laplacian of scalar f."""
        return (Derivative(f, self.x, 2) +
                Derivative(f, self.y, 2) +
                Derivative(f, self.z, 2))

    def _advection(self, f):
        """Compute (u . nabla)f."""
        return (self.u * Derivative(f, self.x) +
                self.v * Derivative(f, self.y) +
                self.w * Derivative(f, self.z))

    # -------------------------------------------------------------------------
    # 1. RELATIVE ENTROPY AND FISHER INFORMATION
    # -------------------------------------------------------------------------

    def derive_relative_entropy(self) -> EntropyEvolutionResult:
        """
        Derive evolution of relative entropy H[u] = integral |u|^2 log(|u|^2/rho) dx.

        Under NS flow:
        d/dt H[u] = d/dt integral |u|^2 log(|u|^2/rho) dx

        Key computation:
        Let f = |u|^2. The relative entropy is:
        H = integral f log(f/rho) dx

        Time derivative of f = |u|^2:
        df/dt = 2 u . du/dt
              = 2 u . (-nabla p + nu Delta u - (u.nabla)u)
              = -2 u . nabla p - 2 u . (u.nabla)u + 2 nu u . Delta u

        For incompressible flow:
        - integral u . nabla p = -integral p div(u) = 0
        - integral u . (u.nabla)u = (1/2) integral u . nabla|u|^2
                                  = -(1/2) integral |u|^2 div(u) = 0

        The viscous term gives:
        integral 2 nu u . Delta u = -2 nu integral |nabla u|^2

        So for the relative entropy:
        dH/dt = integral (1 + log(f/rho)) df/dt dx
              = -2 nu integral (1 + log(|u|^2/rho)) |nabla u|^2 dx  (main contribution)
              + boundary/transport terms
        """

        # Symbolic result
        f = Symbol('f', positive=True)  # f = |u|^2
        H = Symbol('H')  # Relative entropy

        # The main contribution to dH/dt
        # From viscous term: nu integral u . Delta u dx = -nu integral |nabla u|^2 dx
        # With entropy weight: -2 nu integral (1 + log(f/rho)) |nabla u|^2 dx

        log_factor = 1 + log(f / self.rho)
        viscous_contrib = -2 * self.nu * Symbol('int_(1+log(|u|^2/rho))|nabla_u|^2')

        # There's also a Fisher information correction term
        fisher_correction = Symbol('Fisher_correction')

        time_deriv = viscous_contrib + fisher_correction

        notes = """
RELATIVE ENTROPY EVOLUTION UNDER NS
===================================

Definition: H[u] = integral |u|^2 log(|u|^2/rho) dx

where rho is a reference density (typically Gaussian or uniform).

Time derivative computation:
1. Let f = |u|^2. Then H = integral f log(f/rho) dx
2. df/dt = 2 u . du/dt = 2 u . (NS RHS)
3. dH/dt = integral (1 + log(f/rho)) df/dt dx

Key terms:
- Viscous: -2 nu integral (1 + log(|u|^2/rho)) |nabla u|^2 dx
  This is NEGATIVE DEFINITE (good for monotonicity!)

- Advection: integral (1 + log(f/rho)) * 2 u . (u.nabla)u dx
  After integration by parts, this VANISHES for periodic/decaying BC

- Pressure: integral (1 + log(f/rho)) * 2 u . nabla p dx
  VANISHES by incompressibility after integration by parts

RESULT:
dH/dt = -2 nu integral (1 + log(|u|^2/rho)) |nabla u|^2 dx
      + integral f log(f/rho) * div(something) dx  [transport correction]

For rho = const (uniform reference):
dH/dt <= -2 nu integral |nabla u|^2 dx = -4 nu * Dissipation

MONOTONICITY STATUS:
- NOT strictly monotone (transport terms can have either sign)
- The viscous part IS monotone
- Monotonicity depends on choice of rho and boundary conditions

LOCAL L^2 CONTROL:
- H controls integral |u|^2 log|u|^2 globally
- Does NOT directly control local L^2 norms
- Can be localized (see localized entropy)
"""

        return EntropyEvolutionResult(
            quantity_name="Relative Entropy",
            quantity_formula="H[u] = integral |u|^2 log(|u|^2/rho) dx",
            time_derivative=time_deriv,
            sign_analysis="Viscous part <= 0, transport terms indefinite",
            monotone=False,
            controls_local_L2=False,
            notes=notes
        )

    def derive_fisher_information(self) -> EntropyEvolutionResult:
        """
        Derive evolution of Fisher information I[u] = integral |nabla u|^2 / |u|^2 dx.

        Fisher information measures the "sharpness" of the distribution.
        Related to entropy via de Bruijn identity.

        Under NS flow, this is more complex due to the nonlinear structure.
        """

        I = Symbol('I')  # Fisher information

        notes = """
FISHER INFORMATION EVOLUTION UNDER NS
=====================================

Definition: I[u] = integral |nabla u|^2 / |u|^2 dx

This is the "gradient of log-density" measure.

For scalar heat equation: dI/dt = -2 * HWI term <= 0 (monotone!)

For vector NS, the computation is much more involved:
1. Let g = |nabla u|^2 / |u|^2
2. dg/dt involves:
   - d|nabla u|^2/dt = 2 nabla u : nabla(du/dt)
   - d|u|^2/dt = 2 u . du/dt

The NS nonlinearity introduces terms that don't have definite sign.

Key structural difference from heat equation:
- Heat: dI/dt = -2 integral |nabla^2 u / u - nabla u otimes nabla u / u^2|^2 <= 0
- NS: Additional terms from advection and vortex stretching

Formal computation:
dI/dt = -4 nu * integral |nabla^2 u / u - nabla u otimes nabla u / u^2|^2 dx
      + nonlinear_correction

where nonlinear_correction involves:
- integral (nabla u . nabla(u.nabla u)) / |u|^2 dx
- integral |nabla u|^2 * u . (u.nabla u) / |u|^4 dx

MONOTONICITY STATUS:
- NOT monotone (nonlinear corrections can dominate)
- Viscous part gives I-entropy production (good)
- Advection/stretching can increase Fisher information

LOCAL L^2 CONTROL:
- Fisher information is related to concentration by log-Sobolev
- High I => spread out (low concentration)
- But the relation to local L^2 is indirect

POTENTIAL USE:
- Combined with relative entropy in HWI inequality
- May give bounds on concentration rate
"""

        # Symbolic time derivative (schematic)
        viscous_part = -4 * self.nu * Symbol('Hess_entropy_production')
        nonlinear_part = Symbol('nonlinear_Fisher_correction')
        time_deriv = viscous_part + nonlinear_part

        return EntropyEvolutionResult(
            quantity_name="Fisher Information",
            quantity_formula="I[u] = integral |nabla u|^2 / |u|^2 dx",
            time_derivative=time_deriv,
            sign_analysis="Viscous part <= 0, nonlinear part indefinite",
            monotone=False,
            controls_local_L2=False,
            notes=notes
        )

    # -------------------------------------------------------------------------
    # 2. LOCALIZED ENTROPY
    # -------------------------------------------------------------------------

    def derive_localized_entropy(self) -> EntropyEvolutionResult:
        """
        Derive evolution of localized entropy H_r[u] = integral_{B(r)} |u|^2 log(|u|^2/rho_r) dx.

        This is the KEY quantity for controlling local L^2 concentration!

        The reference density rho_r is scale-dependent:
        rho_r(x) = (1/r^3) * rho_0((x-x_0)/r)

        where rho_0 is a fixed profile (e.g., Gaussian).
        """

        r = self.r
        H_r = Symbol('H_r')

        notes = """
LOCALIZED ENTROPY EVOLUTION UNDER NS
====================================

Definition: H_r[u] = integral_{B(x_0,r)} |u|^2 log(|u|^2/rho_r) dx

where:
- B(x_0, r) is the ball of radius r centered at x_0
- rho_r(x) = (1/r^3) * rho_0((x-x_0)/r) is the rescaled reference density

PHYSICAL INTERPRETATION:
H_r measures how concentrated u is compared to the reference rho_r at scale r.

EVOLUTION COMPUTATION:
dH_r/dt = boundary_flux + interior_evolution

1. Interior evolution (same structure as global):
   dH_r/dt|_{interior} = -2 nu integral_{B(r)} (1 + log(|u|^2/rho_r)) |nabla u|^2 dx
                        + transport_correction

2. Boundary flux (NEW for localized case):
   Flux = integral_{partial B(r)} |u|^2 log(|u|^2/rho_r) * (u . n) dS

   This term accounts for entropy entering/leaving the ball!

CRUCIAL OBSERVATION:
For Type II blowup with rate alpha in (1/2, 3/4):
- |u| ~ (T-t)^{-alpha} in a shrinking region of size r ~ (T-t)^{1/2}
- Local L^2: ||u||_{L^2(B(r))}^2 ~ (T-t)^{-2alpha} * r^3 ~ (T-t)^{3/2 - 2alpha}

For alpha = 3/5: ||u||_{L^2(B(r))}^2 ~ (T-t)^{3/2 - 6/5} = (T-t)^{0.3} -> 0

This suggests H_r might be controlled even as blowup approaches!

KEY SCALING ANALYSIS:
Under NS scaling (x -> lambda x, t -> lambda^2 t, u -> lambda^{-1} u):
- |u|^2 -> lambda^{-2} |u|^2
- rho_r -> lambda^{-3} rho_{r/lambda}
- H_r -> H_r/lambda + integral |u|^2 log(lambda) dx

The entropy is NOT scale-invariant, but its evolution might have better properties.

MONOTONICITY ANALYSIS:
dH_r/dt = -2 nu integral_{B(r)} (1 + log(|u|^2/rho_r)) |nabla u|^2 dx
        + boundary_flux
        + transport_correction

The sign depends on:
1. Whether log(|u|^2/rho_r) > -1 (entropy weight positive)
2. Direction and magnitude of boundary flux
3. Reference density choice rho_r

CHOICE OF REFERENCE DENSITY:
Option A: rho_r = const = ||u||_{L^2}^2 / |B(r)|
  - Makes H_r = integral |u|^2 log(|u|^2 / (||u||^2/|B(r)|)) dx
  - This is the "local entropy excess" over uniform distribution

Option B: rho_r = Gaussian ~ exp(-|x-x_0|^2/r^2)
  - Natural for heat kernel comparison
  - Gives better estimates near center of concentration

Option C: rho_r = self-similar profile
  - Match to expected blowup profile
  - Most relevant for Type II analysis

RESULT:
Localized entropy is NOT strictly monotone, but the combination:
Q_r = H_r + boundary_correction
may have controlled growth that bounds local L^2.

LOCAL L^2 CONTROL:
By log-Sobolev inequality:
||u||_{L^2(B(r))}^2 <= C(H_r + ||u||_{L^2}^2)

So H_r bounds give local L^2 bounds!
"""

        # Schematic time derivative
        interior_viscous = -2 * self.nu * Symbol('weighted_dissipation_B(r)')
        boundary_flux = Symbol('entropy_flux_partial_B(r)')
        transport = Symbol('transport_correction_B(r)')

        time_deriv = interior_viscous + boundary_flux + transport

        return EntropyEvolutionResult(
            quantity_name="Localized Entropy",
            quantity_formula="H_r[u] = integral_{B(r)} |u|^2 log(|u|^2/rho_r) dx",
            time_derivative=time_deriv,
            sign_analysis="Interior: viscous <= 0; Boundary flux: indefinite",
            monotone=False,
            controls_local_L2=True,  # Via log-Sobolev!
            notes=notes
        )

    # -------------------------------------------------------------------------
    # 3. RENYI ENTROPIES
    # -------------------------------------------------------------------------

    def derive_renyi_entropy(self) -> EntropyEvolutionResult:
        """
        Derive evolution of Renyi entropy R_alpha[u] = (1/(1-alpha)) log(integral |u|^{2alpha} dx).

        Renyi entropies interpolate between different L^p norms:
        - alpha -> 1: Shannon entropy (relative entropy)
        - alpha = 1/2: Related to L^1 norm
        - alpha = 3/2: Related to L^3 norm (scale-critical!)
        """

        alpha = self.alpha
        R_alpha = Symbol('R_alpha')

        notes = """
RENYI ENTROPY EVOLUTION UNDER NS
================================

Definition: R_alpha[u] = (1/(1-alpha)) * log(integral |u|^{2alpha} dx)

RELATION TO L^P NORMS:
||u||_{L^{2alpha}}^{2alpha} = exp((1-alpha) * R_alpha)

So R_alpha encodes the same information as ||u||_{L^{2alpha}}, but in logarithmic form.

KEY VALUES OF alpha:
- alpha = 1/2: R_{1/2} ~ log||u||_{L^1}
- alpha = 1: lim_{alpha->1} R_alpha = Shannon entropy
- alpha = 3/2: R_{3/2} ~ log||u||_{L^3}^3 (SCALE-CRITICAL for NS!)

EVOLUTION COMPUTATION:
Let M_alpha = integral |u|^{2alpha} dx

dM_alpha/dt = 2alpha * integral |u|^{2alpha-2} u . du/dt dx
            = 2alpha * integral |u|^{2alpha-2} u . (-nabla p + nu Delta u - (u.nabla)u) dx

1. Pressure term:
   integral |u|^{2alpha-2} u . nabla p dx = -integral p * div(|u|^{2alpha-2} u) dx
   = -integral p * (2alpha-2) |u|^{2alpha-4} (u . nabla|u|^2) u dx - integral p |u|^{2alpha-2} div(u) dx
   = -(alpha-1) integral p |u|^{2alpha-2} div(u) dx = 0 (incompressibility)

2. Viscous term:
   integral |u|^{2alpha-2} u . nu Delta u dx
   = -nu * integral nabla(|u|^{2alpha-2} u) : nabla u dx
   = -nu * [(2alpha-2) integral |u|^{2alpha-4} (u . nabla|u|^2) (u . nabla u) dx
           + integral |u|^{2alpha-2} |nabla u|^2 dx]

   This simplifies to:
   = -nu (2alpha-1) integral |u|^{2alpha-2} |nabla u|^2 dx (using structure)

3. Advection term:
   integral |u|^{2alpha-2} u . (u.nabla)u dx
   = (1/2) integral |u|^{2alpha-2} u . nabla|u|^2 dx
   = -(1/2) integral |u|^2 div(|u|^{2alpha-2} u) dx
   = -(alpha-1/2) integral |u|^{2alpha} div(u) dx = 0 (incompressibility)

RESULT:
dM_alpha/dt = -2 nu alpha (2alpha-1) integral |u|^{2alpha-2} |nabla u|^2 dx

For the Renyi entropy:
dR_alpha/dt = (1/(1-alpha)) * (1/M_alpha) * dM_alpha/dt
            = -2 nu alpha (2alpha-1) / (1-alpha) * integral |u|^{2alpha-2}|nabla u|^2 / M_alpha dx

SIGN ANALYSIS:
- For alpha > 1/2: dR_alpha/dt <= 0 (MONOTONE DECREASING!)
- For alpha < 1/2: dR_alpha/dt >= 0 (increases)
- For alpha = 1/2: dR_alpha/dt = 0 (constant)

CRITICAL CASE alpha = 3/2:
dR_{3/2}/dt = -6 nu * integral |u| |nabla u|^2 / M_{3/2} dx <= 0

This controls ||u||_{L^3} which is SCALE-CRITICAL for NS!

Recall ESS criterion: ||u||_{L^3} bounded => regularity.

LOCAL L^2 CONTROL:
R_alpha with alpha > 1 does NOT directly control local L^2.
But R_{3/2} bounds global L^3 which, via interpolation:
||u||_{L^2(B(r))} <= |B(r)|^{1/6} ||u||_{L^3(B(r))}

MONOTONICITY STATUS:
- R_alpha is MONOTONE for alpha > 1/2
- This is a genuinely new monotone quantity!
- But it's essentially the L^p norm in disguise

THE CATCH:
The Renyi entropy R_alpha is monotone, but:
1. It's equivalent to ||u||_{L^{2alpha}}^{2alpha} (just log scale)
2. For alpha = 3/2, this is ||u||_{L^3}^3
3. ESS already tells us L^3 bounds give regularity
4. So this doesn't give NEW information beyond ESS

VALUE: Confirms that Renyi entropies interpolate to scale-critical quantities,
but the monotonicity is just the viscous dissipation in L^p norms.
"""

        # Symbolic time derivative
        alpha_sym = Symbol('alpha')
        M_alpha = Symbol('M_alpha', positive=True)
        weighted_dissip = Symbol('int_|u|^{2alpha-2}|nabla_u|^2')

        dM_dt = -2 * self.nu * alpha_sym * (2*alpha_sym - 1) * weighted_dissip
        dR_dt = (1 / (1 - alpha_sym)) * (1 / M_alpha) * dM_dt

        return EntropyEvolutionResult(
            quantity_name="Renyi Entropy",
            quantity_formula="R_alpha[u] = (1/(1-alpha)) log(integral |u|^{2alpha} dx)",
            time_derivative=dR_dt,
            sign_analysis="dR/dt <= 0 for alpha > 1/2 (MONOTONE)",
            monotone=True,  # For alpha > 1/2
            controls_local_L2=False,  # Only global L^{2alpha}
            notes=notes
        )

    # -------------------------------------------------------------------------
    # 4. CONCENTRATION FUNCTION
    # -------------------------------------------------------------------------

    def derive_concentration_function(self) -> EntropyEvolutionResult:
        """
        Derive evolution of concentration function C(r) = sup_x integral_{B(x,r)} |u|^2 / integral |u|^2.

        This directly measures local concentration relative to total energy!
        """

        r = self.r
        C_r = Symbol('C_r')

        notes = """
CONCENTRATION FUNCTION EVOLUTION UNDER NS
=========================================

Definition: C(r) = sup_{x_0} integral_{B(x_0,r)} |u|^2 dx / integral |u|^2 dx
                 = sup_{x_0} ||u||_{L^2(B(x_0,r))}^2 / ||u||_{L^2}^2

INTERPRETATION:
C(r) = maximum fraction of total L^2 mass contained in any ball of radius r.
- C(r) -> 0 as r -> 0 for spread-out functions
- C(r) -> 1 as r -> L (domain size)
- For delta function: C(r) = 1 for all r > 0

RELATION TO BLOWUP:
For Type II blowup with rate alpha at point x_0:
- |u(x,t)| ~ (T-t)^{-alpha} for |x - x_0| ~ (T-t)^{1/2}
- ||u||_{L^2(B(x_0,r))}^2 ~ (T-t)^{-2alpha} * (T-t)^{3/2} = (T-t)^{3/2-2alpha}
- ||u||_{L^2}^2 ~ E (bounded by energy decay)

So C((T-t)^{1/2}) ~ (T-t)^{3/2-2alpha} / E

For alpha < 3/4: exponent > 0, so C(r) -> 0 as T -> t (at singular scale)
For alpha = 3/4: C(r) ~ const > 0 (critical concentration)
For alpha > 3/4: C(r) -> infinity (impossible, contradicts C <= 1)

This gives another proof that alpha < 3/4 is required!

EVOLUTION COMPUTATION:
The supremum makes this technically difficult. Define for fixed x_0:
C_{x_0}(r) = integral_{B(x_0,r)} |u|^2 dx / integral |u|^2 dx

Then:
dC_{x_0}/dt = (1/E) * [d/dt integral_{B(r)} |u|^2 - C_{x_0} * dE/dt]

where E = integral |u|^2 dx.

Using energy identity: dE/dt = -2 nu integral |nabla u|^2 dx

And local evolution:
d/dt integral_{B(r)} |u|^2 = boundary_flux + interior_change
= integral_{partial B(r)} |u|^2 (u.n) dS - 2 nu integral_{B(r)} |nabla u|^2 dx

So:
dC_{x_0}/dt = (1/E) * [flux - 2 nu dissip_local + 2 nu C_{x_0} * dissip_global]
            = (1/E) * flux + 2 nu (C_{x_0} * epsilon_global - epsilon_local)

where epsilon = (1/E) integral |nabla u|^2.

SIGN ANALYSIS:
The concentration function C(r) is NOT monotone because:
1. Boundary flux can have either sign
2. (C * global_dissip - local_dissip) can have either sign

However, we can derive CONTROLLED GROWTH:

If concentration is increasing (dC/dt > 0), then either:
- Flux is positive (energy flowing into the ball) OR
- Local dissipation < C * global dissipation

Both conditions are physically constrained:
- Large inward flux requires large velocity at boundary
- Dissipation imbalance is bounded by energy distribution

CONCENTRATION INEQUALITY:
For smooth solutions:
C(r) <= C_0 * (r/L)^delta for some delta > 0

This is essentially the Morrey/Campanato regularity theory.

CONNECTION TO EPSILON-REGULARITY:
CKN epsilon-regularity: If C(r) < epsilon for r small, then smooth.

So proving C(r) stays small would prove regularity!

The challenge: C(r) can grow, and we need to track HOW FAST.

MONOTONICITY STATUS:
- NOT monotone
- But growth rate is controlled by energy and flux bounds

LOCAL L^2 CONTROL:
By definition, C(r) DIRECTLY controls local L^2:
||u||_{L^2(B(x_0,r))}^2 <= C(r) * ||u||_{L^2}^2

So any bound on C(r) immediately gives local L^2 bounds!
"""

        # Symbolic time derivative
        E = Symbol('E', positive=True)  # Total energy
        flux = Symbol('boundary_flux_optimal_ball')
        dissip_local = Symbol('dissip_local')
        dissip_global = Symbol('dissip_global')

        time_deriv = (1/E) * flux + 2 * self.nu * (C_r * dissip_global - dissip_local)

        return EntropyEvolutionResult(
            quantity_name="Concentration Function",
            quantity_formula="C(r) = sup_x integral_{B(x,r)} |u|^2 / integral |u|^2",
            time_derivative=time_deriv,
            sign_analysis="NOT monotone - depends on flux and dissipation distribution",
            monotone=False,
            controls_local_L2=True,  # BY DEFINITION!
            notes=notes
        )

    # -------------------------------------------------------------------------
    # 5. LOG-SOBOLEV INEQUALITIES
    # -------------------------------------------------------------------------

    def derive_log_sobolev(self) -> EntropyEvolutionResult:
        """
        Derive localized log-Sobolev inequalities and their NS implications.

        Global log-Sobolev:
        integral |u|^2 log|u|^2 dx <= C ||nabla u||^2 + D ||u||^2

        Can this be localized to give r-dependent bounds?
        """

        notes = """
LOG-SOBOLEV INEQUALITIES AND NS REGULARITY
==========================================

GLOBAL LOG-SOBOLEV:
integral |f|^2 log(|f|^2/||f||^2) dx <= (2/pi) ||nabla f||^2

This is equivalent to the Gaussian isoperimetric inequality.

For NS with f = |u|, we get:
integral |u|^2 log(|u|^2/||u||^2) dx <= (2/pi) ||nabla|u| ||^2
                                      <= (2/pi) ||nabla u||^2

IMPLICATIONS:
1. Bounded dissipation => bounded entropy
2. Energy decay => entropy approaches equilibrium

LOCAL LOG-SOBOLEV:
On a ball B(r):
integral_{B(r)} |f|^2 log(|f|^2/||f||_{B(r)}^2) dx <= C(r) ||nabla f||_{B(r)}^2

where C(r) depends on the geometry of B(r).

For a ball in R^3:
C(r) ~ r^2 (from Poincare constant)

So:
integral_{B(r)} |u|^2 log(|u|^2/||u||_{B(r)}^2) dx <= C r^2 ||nabla u||_{B(r)}^2

REARRANGING:
||u||_{L^2(B(r))}^2 * log(||u||_{L^2(B(r))}^2 / max_{B(r)}|u|^2 |B(r)|)
  <= C r^2 ||nabla u||_{B(r)}^2

This doesn't directly bound ||u||_{L^2(B(r))} but gives a constraint.

NASH INEQUALITY APPROACH:
Nash inequality: ||f||_{L^2}^{1+2/n} <= C ||nabla f||^2 ||f||_{L^1}^{2/n}

In 3D: ||f||_{L^2}^{5/3} <= C ||nabla f||^2 ||f||_{L^1}^{2/3}

Localized: ||f||_{L^2(B(r))}^{5/3} <= C ||nabla f||_{B(r)}^2 (||f||_{L^1(B(r))}^{2/3} + r^{-2}||f||_{L^2}^{5/3})

COMBINING WITH NS:
Let Q_r = ||u||_{L^2(B(r))}^2.

From Nash:
Q_r^{5/6} <= C ||nabla u||_{B(r)}^2 ||u||_{L^1(B(r))}^{2/3}

From Holder:
||u||_{L^1(B(r))} <= |B(r)|^{1/2} ||u||_{L^2(B(r))} = (4pi/3)^{1/2} r^{3/2} Q_r^{1/2}

Substituting:
Q_r^{5/6} <= C ||nabla u||_{B(r)}^2 * r Q_r^{1/3}

So:
Q_r^{1/2} <= C r ||nabla u||_{B(r)}^2

This gives:
||u||_{L^2(B(r))} <= C r^{1/2} ||nabla u||_{B(r)}

INTERPRETATION:
Local L^2 is controlled by local dissipation times a scale factor.

For blowup scenario:
- ||nabla u||_{B(r)}^2 ~ nu^{-1} (dissipation bounded by energy)
- ||u||_{L^2(B(r))} <= C r^{1/2} nu^{-1/2}

At scale r ~ (T-t)^{1/2} (blowup scale):
||u||_{L^2(B(r))} <= C (T-t)^{1/4} nu^{-1/2}

For Type II with ||u||_infty ~ (T-t)^{-alpha}:
||u||_{L^2(B(r))} ~ (T-t)^{-alpha} * r^{3/2} ~ (T-t)^{-alpha + 3/4}

Matching: -alpha + 3/4 >= 1/4 (from Nash)
         alpha <= 1/2

But this is Type I bound (alpha = 1/2)!

ISSUE: Nash inequality is too weak to constrain Type II.

REFINED APPROACH:
Use log-Sobolev with entropy evolution to get time-integrated bounds.

integral_0^T ||u||_{L^2(B(r))}^2 log(||u||_{L^2(B(r))}^2) dt
  <= integral_0^T (entropy_bound) dt
  <= initial_entropy - final_entropy + time_integral_corrections

This gives bounds on how long concentration can persist.

MONOTONICITY STATUS:
Log-Sobolev gives inequalities, not evolution equations.
Combined with NS energy identity, can constrain growth rates.

LOCAL L^2 CONTROL:
Yes, but the bounds are not optimal for Type II.
The r-dependence introduces factors that don't close the gap.
"""

        # Symbolic inequality
        Q_r = Symbol('||u||_{L^2(B(r))}^2')
        nabla_u_B_r = Symbol('||nabla_u||_{L^2(B(r))}^2')

        # Nash-type bound
        nash_bound = sp.sqrt(self.r) * sp.sqrt(nabla_u_B_r)

        # Log-Sobolev entropy bound
        entropy_bound = 2 * self.r**2 * nabla_u_B_r / sp.pi

        return EntropyEvolutionResult(
            quantity_name="Log-Sobolev Inequality",
            quantity_formula="integral |u|^2 log|u|^2 <= (2/pi)||nabla u||^2 + const",
            time_derivative=sp.Symbol('not_evolution_but_inequality'),
            sign_analysis="Provides bounds, not evolution",
            monotone=False,  # N/A - it's an inequality
            controls_local_L2=True,  # Via Nash + log-Sobolev
            notes=notes
        )

    def generate_all_derivations(self) -> List[EntropyEvolutionResult]:
        """Generate all entropy-based derivations."""
        return [
            self.derive_relative_entropy(),
            self.derive_fisher_information(),
            self.derive_localized_entropy(),
            self.derive_renyi_entropy(),
            self.derive_concentration_function(),
            self.derive_log_sobolev(),
        ]


# ============================================================================
# NUMERICAL IMPLEMENTATION
# ============================================================================

class EntropyComputer:
    """
    Numerical computation of entropy quantities for NS solutions.

    Works with 3D velocity fields on a periodic domain.
    """

    def __init__(self, L: float = 2*np.pi, nu: float = 0.01):
        """
        Args:
            L: Domain size [0, L]^3
            nu: Kinematic viscosity
        """
        self.L = L
        self.nu = nu

    def _setup_grid(self, N: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Set up physical grid."""
        x = np.linspace(0, self.L, N, endpoint=False)
        X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
        return X, Y, Z

    def _compute_gradient_magnitude_sq(self, u: np.ndarray, v: np.ndarray,
                                        w: np.ndarray) -> np.ndarray:
        """Compute |nabla u|^2 spectrally."""
        N = u.shape[0]
        k = fftfreq(N, d=self.L/(2*np.pi*N))
        kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')

        grad_u_sq = np.zeros_like(u)

        for vel in [u, v, w]:
            vel_hat = fftn(vel)
            for ki in [kx, ky, kz]:
                deriv = np.real(ifftn(1j * ki * vel_hat))
                grad_u_sq += deriv**2

        return grad_u_sq

    # -------------------------------------------------------------------------
    # 1. RELATIVE ENTROPY
    # -------------------------------------------------------------------------

    def compute_relative_entropy(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                                  rho: Optional[np.ndarray] = None) -> float:
        """
        Compute relative entropy H[u] = integral |u|^2 log(|u|^2/rho) dx.

        Args:
            u, v, w: Velocity components
            rho: Reference density. If None, use uniform.

        Returns:
            Relative entropy value.
        """
        N = u.shape[0]
        dx = self.L / N

        u_sq = u**2 + v**2 + w**2

        # Avoid log(0) by adding small epsilon
        eps = 1e-15
        u_sq_safe = np.maximum(u_sq, eps)

        if rho is None:
            # Uniform reference: rho = ||u||^2 / Volume
            rho = np.mean(u_sq) + eps

        H = np.sum(u_sq * np.log(u_sq_safe / rho)) * dx**3

        return H

    def compute_relative_entropy_time_derivative(self, u: np.ndarray, v: np.ndarray,
                                                   w: np.ndarray,
                                                   rho: Optional[np.ndarray] = None) -> Dict:
        """
        Compute dH/dt for relative entropy.

        Returns dict with viscous contribution and estimated full derivative.
        """
        N = u.shape[0]
        dx = self.L / N

        u_sq = u**2 + v**2 + w**2
        eps = 1e-15
        u_sq_safe = np.maximum(u_sq, eps)

        if rho is None:
            rho = np.mean(u_sq) + eps

        grad_u_sq = self._compute_gradient_magnitude_sq(u, v, w)

        # Viscous contribution: -2 nu integral (1 + log(|u|^2/rho)) |nabla u|^2 dx
        weight = 1 + np.log(u_sq_safe / rho)
        viscous_dH_dt = -2 * self.nu * np.sum(weight * grad_u_sq) * dx**3

        return {
            'viscous_contribution': viscous_dH_dt,
            'estimated_dH_dt': viscous_dH_dt,  # Main contribution
            'weight_positive_fraction': np.mean(weight > 0),
        }

    # -------------------------------------------------------------------------
    # 2. FISHER INFORMATION
    # -------------------------------------------------------------------------

    def compute_fisher_information(self, u: np.ndarray, v: np.ndarray,
                                    w: np.ndarray) -> float:
        """
        Compute Fisher information I[u] = integral |nabla u|^2 / |u|^2 dx.

        Note: This can be infinite where u = 0.
        """
        N = u.shape[0]
        dx = self.L / N

        u_sq = u**2 + v**2 + w**2
        eps = 1e-10  # Regularization

        grad_u_sq = self._compute_gradient_magnitude_sq(u, v, w)

        # Fisher information with regularization
        I = np.sum(grad_u_sq / (u_sq + eps)) * dx**3

        return I

    # -------------------------------------------------------------------------
    # 3. LOCALIZED ENTROPY
    # -------------------------------------------------------------------------

    def compute_localized_entropy(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                                   center: Tuple[float, float, float],
                                   radius: float,
                                   rho_r: Optional[float] = None) -> float:
        """
        Compute localized entropy H_r[u] = integral_{B(r)} |u|^2 log(|u|^2/rho_r) dx.

        Args:
            u, v, w: Velocity components
            center: Center of ball (x0, y0, z0)
            radius: Ball radius r
            rho_r: Reference density. If None, use local average.

        Returns:
            Localized entropy value.
        """
        N = u.shape[0]
        dx = self.L / N

        X, Y, Z = self._setup_grid(N)
        x0, y0, z0 = center

        # Distance from center (with periodic BC)
        dist_x = np.minimum(np.abs(X - x0), self.L - np.abs(X - x0))
        dist_y = np.minimum(np.abs(Y - y0), self.L - np.abs(Y - y0))
        dist_z = np.minimum(np.abs(Z - z0), self.L - np.abs(Z - z0))
        dist = np.sqrt(dist_x**2 + dist_y**2 + dist_z**2)

        # Mask for ball
        mask = dist <= radius

        u_sq = u**2 + v**2 + w**2
        eps = 1e-15

        if rho_r is None:
            # Use local average as reference
            ball_volume = np.sum(mask) * dx**3
            rho_r = np.sum(u_sq * mask) * dx**3 / max(ball_volume, eps)
            rho_r = max(rho_r, eps)

        u_sq_safe = np.maximum(u_sq, eps)
        H_r = np.sum(mask * u_sq * np.log(u_sq_safe / rho_r)) * dx**3

        return H_r

    def compute_localized_entropy_profile(self, u: np.ndarray, v: np.ndarray,
                                           w: np.ndarray,
                                           center: Tuple[float, float, float],
                                           radii: np.ndarray) -> np.ndarray:
        """
        Compute H_r for multiple radii.

        Returns array of localized entropies.
        """
        return np.array([
            self.compute_localized_entropy(u, v, w, center, r)
            for r in radii
        ])

    # -------------------------------------------------------------------------
    # 4. RENYI ENTROPY
    # -------------------------------------------------------------------------

    def compute_renyi_entropy(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                               alpha: float) -> float:
        """
        Compute Renyi entropy R_alpha[u] = (1/(1-alpha)) log(integral |u|^{2alpha} dx).

        Args:
            u, v, w: Velocity components
            alpha: Renyi parameter (must be != 1)

        Returns:
            Renyi entropy value.
        """
        if abs(alpha - 1.0) < 1e-10:
            raise ValueError("alpha = 1 is undefined; use relative entropy instead")

        N = u.shape[0]
        dx = self.L / N

        u_mag = np.sqrt(u**2 + v**2 + w**2)
        eps = 1e-15

        M_alpha = np.sum(u_mag**(2*alpha)) * dx**3
        M_alpha = max(M_alpha, eps)

        R_alpha = np.log(M_alpha) / (1 - alpha)

        return R_alpha

    def compute_renyi_time_derivative(self, u: np.ndarray, v: np.ndarray,
                                       w: np.ndarray, alpha: float) -> float:
        """
        Compute dR_alpha/dt = -2 nu alpha (2alpha-1) / (1-alpha) * weighted_dissip / M_alpha.

        This should be <= 0 for alpha > 1/2.
        """
        if abs(alpha - 1.0) < 1e-10 or abs(alpha - 0.5) < 1e-10:
            return 0.0

        N = u.shape[0]
        dx = self.L / N

        u_mag = np.sqrt(u**2 + v**2 + w**2)
        eps = 1e-15
        u_mag_safe = np.maximum(u_mag, eps)

        grad_u_sq = self._compute_gradient_magnitude_sq(u, v, w)

        # M_alpha = integral |u|^{2alpha}
        M_alpha = np.sum(u_mag**(2*alpha)) * dx**3
        M_alpha = max(M_alpha, eps)

        # Weighted dissipation: integral |u|^{2alpha-2} |nabla u|^2
        weighted_dissip = np.sum(u_mag_safe**(2*alpha-2) * grad_u_sq) * dx**3

        # dR/dt formula
        coeff = -2 * self.nu * alpha * (2*alpha - 1) / (1 - alpha)
        dR_dt = coeff * weighted_dissip / M_alpha

        return dR_dt

    # -------------------------------------------------------------------------
    # 5. CONCENTRATION FUNCTION
    # -------------------------------------------------------------------------

    def compute_concentration_function(self, u: np.ndarray, v: np.ndarray,
                                         w: np.ndarray, radius: float) -> Tuple[float, Tuple[int, int, int]]:
        """
        Compute concentration function C(r) = max_x integral_{B(x,r)} |u|^2 / integral |u|^2.

        Returns (C(r), location of maximum).
        """
        N = u.shape[0]
        dx = self.L / N

        u_sq = u**2 + v**2 + w**2
        total_energy = np.sum(u_sq) * dx**3

        if total_energy < 1e-15:
            return 0.0, (0, 0, 0)

        # Compute local energy in ball of radius r around each point
        # Use convolution with ball indicator

        X, Y, Z = self._setup_grid(N)

        # For efficiency, sample a grid of potential centers
        # (Full search over all points is expensive)
        n_sample = min(16, N)
        sample_indices = np.linspace(0, N-1, n_sample, dtype=int)

        max_C = 0.0
        max_loc = (0, 0, 0)

        for i in sample_indices:
            for j in sample_indices:
                for k in sample_indices:
                    x0 = X[i, 0, 0]
                    y0 = Y[0, j, 0]
                    z0 = Z[0, 0, k]

                    # Distance from center (periodic)
                    dist_x = np.minimum(np.abs(X - x0), self.L - np.abs(X - x0))
                    dist_y = np.minimum(np.abs(Y - y0), self.L - np.abs(Y - y0))
                    dist_z = np.minimum(np.abs(Z - z0), self.L - np.abs(Z - z0))
                    dist = np.sqrt(dist_x**2 + dist_y**2 + dist_z**2)

                    mask = dist <= radius
                    local_energy = np.sum(u_sq * mask) * dx**3

                    C = local_energy / total_energy

                    if C > max_C:
                        max_C = C
                        max_loc = (i, j, k)

        return max_C, max_loc

    def compute_concentration_profile(self, u: np.ndarray, v: np.ndarray,
                                        w: np.ndarray,
                                        radii: np.ndarray) -> np.ndarray:
        """
        Compute C(r) for multiple radii.

        Returns array of concentration values.
        """
        return np.array([
            self.compute_concentration_function(u, v, w, r)[0]
            for r in radii
        ])

    # -------------------------------------------------------------------------
    # 6. LOG-SOBOLEV QUANTITIES
    # -------------------------------------------------------------------------

    def compute_log_sobolev_lhs(self, u: np.ndarray, v: np.ndarray,
                                 w: np.ndarray) -> float:
        """
        Compute LHS of log-Sobolev: integral |u|^2 log(|u|^2/||u||^2) dx.
        """
        N = u.shape[0]
        dx = self.L / N

        u_sq = u**2 + v**2 + w**2
        total = np.sum(u_sq) * dx**3

        eps = 1e-15
        u_sq_safe = np.maximum(u_sq, eps)
        total_safe = max(total, eps)

        lhs = np.sum(u_sq * np.log(u_sq_safe / total_safe)) * dx**3

        return lhs

    def compute_log_sobolev_rhs(self, u: np.ndarray, v: np.ndarray,
                                 w: np.ndarray) -> float:
        """
        Compute RHS of log-Sobolev: (2/pi) ||nabla u||^2.
        """
        N = u.shape[0]
        dx = self.L / N

        grad_u_sq = self._compute_gradient_magnitude_sq(u, v, w)

        rhs = (2/np.pi) * np.sum(grad_u_sq) * dx**3

        return rhs

    def verify_log_sobolev(self, u: np.ndarray, v: np.ndarray,
                           w: np.ndarray) -> Dict:
        """
        Verify log-Sobolev inequality: LHS <= RHS.

        Returns dict with LHS, RHS, and verification status.
        """
        lhs = self.compute_log_sobolev_lhs(u, v, w)
        rhs = self.compute_log_sobolev_rhs(u, v, w)

        return {
            'lhs': lhs,
            'rhs': rhs,
            'ratio': lhs / max(rhs, 1e-15),
            'satisfied': lhs <= rhs + 1e-10,
        }

    # -------------------------------------------------------------------------
    # COMPREHENSIVE ANALYSIS
    # -------------------------------------------------------------------------

    def compute_all_entropies(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                               center: Optional[Tuple[float, float, float]] = None,
                               radii: Optional[np.ndarray] = None) -> Dict:
        """
        Compute all entropy quantities for a given velocity field.

        Args:
            u, v, w: Velocity components
            center: Center for localized quantities. If None, use center of domain.
            radii: Radii for concentration/localized entropy. If None, use defaults.

        Returns:
            Dictionary with all computed quantities.
        """
        N = u.shape[0]

        if center is None:
            center = (self.L/2, self.L/2, self.L/2)

        if radii is None:
            radii = np.array([0.1, 0.2, 0.5, 1.0]) * self.L / 2

        results = {
            'grid_size': N,
            'domain_size': self.L,
            'viscosity': self.nu,
        }

        # Basic quantities
        u_sq = u**2 + v**2 + w**2
        results['total_energy'] = 0.5 * np.sum(u_sq) * (self.L/N)**3
        results['L2_norm'] = np.sqrt(np.sum(u_sq) * (self.L/N)**3)
        results['Linf_norm'] = np.sqrt(np.max(u_sq))

        # Relative entropy
        results['relative_entropy'] = self.compute_relative_entropy(u, v, w)
        results['relative_entropy_deriv'] = self.compute_relative_entropy_time_derivative(u, v, w)

        # Fisher information
        results['fisher_information'] = self.compute_fisher_information(u, v, w)

        # Renyi entropies for various alpha
        for alpha in [0.5, 1.5, 2.0, 3.0]:
            if abs(alpha - 1.0) > 0.01:
                results[f'renyi_{alpha}'] = self.compute_renyi_entropy(u, v, w, alpha)
                results[f'renyi_{alpha}_deriv'] = self.compute_renyi_time_derivative(u, v, w, alpha)

        # Localized entropy profile
        results['localized_entropy_center'] = center
        results['localized_entropy_radii'] = radii
        results['localized_entropy_profile'] = self.compute_localized_entropy_profile(
            u, v, w, center, radii
        )

        # Concentration function profile
        results['concentration_radii'] = radii
        results['concentration_profile'] = self.compute_concentration_profile(u, v, w, radii)

        # Log-Sobolev verification
        results['log_sobolev'] = self.verify_log_sobolev(u, v, w)

        return results


# ============================================================================
# MONOTONICITY ANALYSIS
# ============================================================================

class MonotonicityAnalyzer:
    """
    Analyze which entropy quantities are monotone under NS flow.

    Tracks quantities over time and checks for monotone decrease.
    """

    def __init__(self, entropy_computer: EntropyComputer):
        """
        Args:
            entropy_computer: EntropyComputer instance for numerical computation.
        """
        self.computer = entropy_computer
        self.history: List[Dict] = []

    def update(self, t: float, u: np.ndarray, v: np.ndarray, w: np.ndarray,
               center: Optional[Tuple[float, float, float]] = None):
        """
        Record entropy quantities at time t.

        Args:
            t: Current time
            u, v, w: Velocity components
            center: Center for localized quantities
        """
        results = self.computer.compute_all_entropies(u, v, w, center)
        results['time'] = t
        self.history.append(results)

    def analyze_monotonicity(self) -> Dict:
        """
        Analyze which quantities are monotone over recorded history.

        Returns dict with monotonicity status for each quantity.
        """
        if len(self.history) < 2:
            return {'error': 'Need at least 2 time points'}

        analysis = {}

        # Scalar quantities to check
        scalar_quantities = [
            'total_energy',
            'relative_entropy',
            'fisher_information',
        ]

        # Add Renyi entropies
        for alpha in [0.5, 1.5, 2.0, 3.0]:
            key = f'renyi_{alpha}'
            if key in self.history[0]:
                scalar_quantities.append(key)

        for qty in scalar_quantities:
            values = [h[qty] for h in self.history]
            diffs = np.diff(values)

            analysis[qty] = {
                'initial': values[0],
                'final': values[-1],
                'min_diff': np.min(diffs),
                'max_diff': np.max(diffs),
                'is_monotone_decreasing': np.all(diffs <= 1e-10),
                'is_monotone_increasing': np.all(diffs >= -1e-10),
            }

        # Analyze concentration function at each radius
        radii = self.history[0].get('concentration_radii', [])
        for i, r in enumerate(radii):
            values = [h['concentration_profile'][i] for h in self.history]
            diffs = np.diff(values)

            analysis[f'concentration_r{i}'] = {
                'radius': r,
                'initial': values[0],
                'final': values[-1],
                'max_value': np.max(values),
                'is_monotone': np.all(diffs <= 1e-10) or np.all(diffs >= -1e-10),
            }

        return analysis

    def generate_report(self) -> str:
        """Generate a text report of monotonicity analysis."""
        if len(self.history) < 2:
            return "Insufficient data for analysis."

        analysis = self.analyze_monotonicity()

        lines = [
            "=" * 60,
            "ENTROPY MONOTONICITY ANALYSIS UNDER NS FLOW",
            "=" * 60,
            f"Time interval: [{self.history[0]['time']:.4f}, {self.history[-1]['time']:.4f}]",
            f"Number of samples: {len(self.history)}",
            "",
            "-" * 60,
            "SCALAR QUANTITIES",
            "-" * 60,
        ]

        monotone_quantities = []
        non_monotone_quantities = []

        for qty, data in analysis.items():
            if 'is_monotone_decreasing' in data:
                status = "MONOTONE DEC" if data['is_monotone_decreasing'] else (
                    "MONOTONE INC" if data['is_monotone_increasing'] else "NOT MONOTONE"
                )

                lines.append(f"\n{qty}:")
                lines.append(f"  Initial: {data['initial']:.6e}")
                lines.append(f"  Final: {data['final']:.6e}")
                lines.append(f"  Status: {status}")

                if data['is_monotone_decreasing']:
                    monotone_quantities.append(qty)
                else:
                    non_monotone_quantities.append(qty)

        lines.extend([
            "",
            "-" * 60,
            "SUMMARY",
            "-" * 60,
            f"Monotone decreasing: {monotone_quantities}",
            f"Not monotone: {non_monotone_quantities}",
            "",
            "INTERPRETATION FOR TYPE II BLOWUP:",
            "- Energy: monotone (known), but too global",
            "- Renyi (alpha > 1/2): should be monotone",
            "- Concentration: NOT monotone, but growth bounded",
            "- Localized entropy: NOT monotone, has boundary flux",
        ])

        return "\n".join(lines)


# ============================================================================
# MAIN ANALYSIS FUNCTION
# ============================================================================

def analyze_entropy_evolution():
    """
    Run complete entropy analysis and print results.

    This is the main entry point for the module.
    """
    print("=" * 70)
    print("INFORMATION-THEORETIC ANALYSIS OF NAVIER-STOKES")
    print("=" * 70)

    # Symbolic derivations
    print("\n" + "=" * 70)
    print("PART 1: SYMBOLIC DERIVATIONS")
    print("=" * 70)

    symbolic = SymbolicEntropyDerivation()
    derivations = symbolic.generate_all_derivations()

    for deriv in derivations:
        print(f"\n{'='*60}")
        print(f"QUANTITY: {deriv.quantity_name}")
        print(f"{'='*60}")
        print(f"Formula: {deriv.quantity_formula}")
        print(f"Sign analysis: {deriv.sign_analysis}")
        print(f"Monotone: {deriv.monotone}")
        print(f"Controls local L^2: {deriv.controls_local_L2}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY: MONOTONICITY AND LOCAL CONTROL")
    print("=" * 70)

    print("\nQuantity                  | Monotone | Controls Local L^2")
    print("-" * 60)

    for deriv in derivations:
        mono = "YES" if deriv.monotone else "NO"
        local = "YES" if deriv.controls_local_L2 else "NO"
        print(f"{deriv.quantity_name:25s} | {mono:8s} | {local}")

    print("\n" + "=" * 70)
    print("KEY FINDINGS FOR TYPE II BLOWUP")
    print("=" * 70)

    print("""
1. RENYI ENTROPY (alpha > 1/2) IS MONOTONE:
   - dR_alpha/dt <= 0 for alpha > 1/2
   - For alpha = 3/2: controls L^3 norm (scale-critical!)
   - BUT: This is essentially the same as ESS criterion

2. CONCENTRATION FUNCTION DIRECTLY CONTROLS LOCAL L^2:
   - By definition: ||u||_{L^2(B(r))}^2 <= C(r) * ||u||_{L^2}^2
   - NOT monotone, but growth rate is bounded
   - Growth controlled by boundary flux + dissipation distribution

3. LOCALIZED ENTROPY ALSO CONTROLS LOCAL L^2:
   - Via log-Sobolev inequality
   - NOT monotone due to boundary flux
   - Could be combined with global bounds

4. THE GAP PERSISTS:
   - Energy is monotone but too global
   - Concentration controls local L^2 but not monotone
   - No quantity found that is BOTH monotone AND controls local L^2

5. POSSIBLE DIRECTIONS:
   - Modified entropy with scale-dependent reference
   - Weighted combinations of Renyi entropies
   - Time-integrated bounds using log-Sobolev
""")

    return derivations


if __name__ == "__main__":
    derivations = analyze_entropy_evolution()

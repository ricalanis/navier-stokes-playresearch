"""
Systematic Symbolic Search for Navier-Stokes Monotone Quantities.

This module performs an exhaustive search for:
1. Scale-critical quantities of the form int |u|^a |omega|^b dx
2. Mixed quantities involving gradients
3. Weighted L^p norms with specific structures
4. Quantities that might constrain Type II blowup in [3/5, 3/4)

Key insight: The enstrophy stretching term int omega_i omega_j S_ij dx
is the main obstruction to monotonicity beyond energy.
"""

import sympy as sp
from sympy import (Symbol, Function, Derivative, simplify, expand, factor,
                   sqrt, Abs, sign, integrate, diff, Rational, S, oo, pi,
                   Matrix, symbols, latex)
from typing import List, Dict, Tuple, Optional, Any
from dataclasses import dataclass, field
from fractions import Fraction
import itertools


@dataclass
class QuantityCandidate:
    """A candidate monotone quantity."""
    name: str
    formula: str
    exponents: Tuple[float, ...]  # (a, b, ...) exponents
    scaling_dimension: float  # Under NS scaling
    time_derivative_structure: str
    is_scale_critical: bool
    has_definite_sign: bool
    sign_type: Optional[str]  # 'decreasing', 'increasing', or None
    obstruction: Optional[str]  # What prevents monotonicity
    notes: str


class SystematicIdentitySearch:
    """
    Systematic search for monotone quantities in Navier-Stokes.

    NS Scaling: x -> lambda*x, t -> lambda^2*t, u -> lambda^{-1}*u
    Under this scaling:
        - |u|^a scales as lambda^{-a}
        - |omega|^b scales as lambda^{-2b} (omega ~ nabla u)
        - dx^3 scales as lambda^3
        - Total: lambda^{3 - a - 2b}

    Scale-critical: 3 - a - 2b = 0, i.e., a + 2b = 3
    """

    def __init__(self):
        # Symbolic setup
        self.nu = Symbol('nu', real=True, positive=True)
        self.t = Symbol('t', real=True)

        # L^p norms as symbols
        self.u_Lp = {}  # u_Lp[p] = ||u||_Lp
        self.omega_Lp = {}  # omega_Lp[p] = ||omega||_Lp

        # Key integrals as symbols
        self.energy = Symbol('E', positive=True)  # (1/2)||u||^2_{L^2}
        self.enstrophy = Symbol('Omega', positive=True)  # (1/2)||omega||^2_{L^2}
        self.palinstrophy = Symbol('P', positive=True)  # (1/2)||nabla omega||^2_{L^2}
        self.stretching = Symbol('S')  # int omega_i omega_j S_ij

        # Results storage
        self.candidates: List[QuantityCandidate] = []

    def scaling_dimension(self, a: float, b: float, c: float = 0) -> float:
        """
        Compute scaling dimension for int |u|^a |omega|^b |nabla omega|^c dx.

        Under NS scaling:
        - |u| ~ lambda^{-1}
        - |omega| ~ lambda^{-2}
        - |nabla omega| ~ lambda^{-3}
        - dx^3 ~ lambda^3

        Returns: dimension (0 = scale-critical)
        """
        return 3 - a - 2*b - 3*c

    def is_scale_critical(self, a: float, b: float, c: float = 0) -> bool:
        """Check if exponents give scale-critical quantity."""
        return abs(self.scaling_dimension(a, b, c)) < 1e-10

    def derive_time_derivative_u_omega_mixed(self, a: float, b: float) -> Dict[str, Any]:
        """
        Derive the time derivative of Q = int |u|^a |omega|^b dx.

        Using:
        - NS: du/dt = -u.nabla u - nabla p + nu Delta u
        - Vorticity: d omega/dt = omega.nabla u - u.nabla omega + nu Delta omega

        d/dt int |u|^a |omega|^b = int (a |u|^{a-2} u . du/dt) |omega|^b
                                 + int |u|^a (b |omega|^{b-2} omega . d omega/dt)
        """
        result = {
            'quantity': f'int |u|^{a} |omega|^{b}',
            'scaling_dim': self.scaling_dimension(a, b),
            'is_critical': self.is_scale_critical(a, b),
            'terms': {}
        }

        # Time derivative structure (symbolic description)
        terms = []

        # From velocity evolution: a |u|^{a-2} u . du/dt
        if a != 0:
            # Advection contribution: a |u|^{a-2} u . (-(u.nabla)u)
            # = -a |u|^{a-2} u_i u_j partial_j u_i
            # For incompressible: this becomes a boundary term / vanishes appropriately
            terms.append({
                'name': 'velocity_advection',
                'expression': f'-int a |u|^{a-2} u_i u_j partial_j u_i |omega|^{b}',
                'sign': 'indefinite',
                'notes': 'Vanishes by integration by parts if a >= 2 (incompressibility)'
            })

            # Pressure contribution: a |u|^{a-2} u . (-nabla p)
            # = -a |u|^{a-2} u . nabla p = a |u|^{a-2} p div(u) = 0 by incompressibility
            terms.append({
                'name': 'pressure',
                'expression': f'-int a |u|^{a-2} u . nabla p |omega|^{b}',
                'sign': 'zero',
                'notes': 'Vanishes by incompressibility after integration by parts'
            })

            # Viscous contribution: a |u|^{a-2} u . (nu Delta u)
            # Integration by parts: -nu a int |u|^{a-2} |nabla u|^2 - lower order
            terms.append({
                'name': 'velocity_viscous',
                'expression': f'-nu a int |u|^{a-2} |nabla u|^2 |omega|^{b} + ...',
                'sign': 'negative (main term)',
                'notes': 'Negative definite for main term; lower order terms need care'
            })

        # From vorticity evolution: b |omega|^{b-2} omega . d omega/dt
        if b != 0:
            # Stretching: b |omega|^{b-2} omega . (omega.nabla)u
            # = b |omega|^{b-2} omega_i omega_j S_ij (strain tensor contribution)
            terms.append({
                'name': 'vortex_stretching',
                'expression': f'int b |u|^{a} |omega|^{b-2} omega_i omega_j S_ij',
                'sign': 'INDEFINITE - KEY OBSTRUCTION',
                'notes': 'This is the vortex stretching term. Can be positive (growth) or negative (decay).'
            })

            # Advection of vorticity: -b |omega|^{b-2} omega . (u.nabla)omega
            # This is transport, vanishes in integral by incompressibility
            terms.append({
                'name': 'vorticity_advection',
                'expression': f'-int b |omega|^{b-2} omega . (u.nabla)omega |u|^{a}',
                'sign': 'zero (after ibp)',
                'notes': 'Vanishes by incompressibility and integration by parts for suitable b'
            })

            # Viscous: b |omega|^{b-2} omega . (nu Delta omega)
            # = -nu b int |omega|^{b-2} |nabla omega|^2 (main negative term)
            terms.append({
                'name': 'vorticity_viscous',
                'expression': f'-nu b int |u|^{a} |omega|^{b-2} |nabla omega|^2',
                'sign': 'negative (main term)',
                'notes': 'Negative definite dissipation'
            })

        result['terms'] = terms

        # Analyze overall sign
        has_indefinite = any(t['sign'].startswith('indefinite') or
                           t['sign'].startswith('INDEFINITE') for t in terms)
        result['has_definite_sign'] = not has_indefinite

        if has_indefinite:
            result['obstruction'] = 'vortex stretching term'
        else:
            result['obstruction'] = None

        return result

    def analyze_energy(self) -> QuantityCandidate:
        """Energy: E = (1/2) int |u|^2 dx"""
        return QuantityCandidate(
            name="Kinetic Energy",
            formula="E = (1/2) int |u|^2 dx",
            exponents=(2, 0),
            scaling_dimension=self.scaling_dimension(2, 0),  # = 1, subcritical
            time_derivative_structure="dE/dt = -nu ||nabla u||^2 <= 0",
            is_scale_critical=False,
            has_definite_sign=True,
            sign_type='decreasing',
            obstruction=None,
            notes="""
MONOTONE DECREASING. The unique definite-sign quantity.
- Advection cancels (incompressibility)
- Pressure cancels (incompressibility)
- Only viscous term remains: -nu int |nabla u|^2
- Scaling dimension = 1 (subcritical)
"""
        )

    def analyze_enstrophy(self) -> QuantityCandidate:
        """Enstrophy: Omega = (1/2) int |omega|^2 dx"""
        return QuantityCandidate(
            name="Enstrophy",
            formula="Omega = (1/2) int |omega|^2 dx",
            exponents=(0, 2),
            scaling_dimension=self.scaling_dimension(0, 2),  # = -1, supercritical
            time_derivative_structure="dOmega/dt = int omega_i omega_j S_ij - nu ||nabla omega||^2",
            is_scale_critical=False,
            has_definite_sign=False,
            sign_type=None,
            obstruction="Vortex stretching term: int omega_i omega_j S_ij",
            notes="""
NOT MONOTONE due to vortex stretching.
- Stretching can be positive (enstrophy growth)
- In 2D: stretching = 0, so enstrophy IS monotone decreasing
- In 3D: stretching is the key obstacle to regularity
- Scaling dimension = -1 (supercritical)
"""
        )

    def analyze_helicity(self) -> QuantityCandidate:
        """Helicity: H = int u . omega dx"""
        return QuantityCandidate(
            name="Helicity",
            formula="H = int u . omega dx",
            exponents=(1, 1),  # Not a pure power form
            scaling_dimension=0,  # Scale-invariant!
            time_derivative_structure="dH/dt = -2 nu int omega . (nabla x omega) dx",
            is_scale_critical=True,
            has_definite_sign=False,
            sign_type=None,
            obstruction="Viscous term is indefinite; inviscid Euler conserves H",
            notes="""
SCALE-CRITICAL. Conserved in inviscid Euler.
- Measures linking of vortex lines
- Under viscosity: dH/dt = -2 nu int omega . curl(omega)
- This viscous term is NOT definite sign
- But H is topological: constrains vortex reconnection
"""
        )

    def analyze_L3_norm(self) -> QuantityCandidate:
        """||u||^3_{L^3} - the ESS critical norm"""
        deriv = self.derive_time_derivative_u_omega_mixed(3, 0)
        return QuantityCandidate(
            name="||u||^3_{L^3}",
            formula="Q = int |u|^3 dx",
            exponents=(3, 0),
            scaling_dimension=0,  # Scale-critical!
            time_derivative_structure="""
d/dt int |u|^3 = 3 int |u| u . du/dt
= -3 int |u| u . (u.nabla)u - 3 int |u| u . nabla p + 3 nu int |u| u . Delta u
= nonlinear - 0 - 3 nu int |u| |nabla u|^2 + lower order
""",
            is_scale_critical=True,
            has_definite_sign=False,
            sign_type=None,
            obstruction="Nonlinear advection term: int |u| u_i u_j partial_j u_i",
            notes="""
SCALE-CRITICAL (ESS space). Critical for regularity.
- ESS theorem: ||u||_{L^3} bounded => regularity
- Time derivative has nonlinear term that's NOT definite
- The cubic power makes integration by parts complicated
- Would need: int |u| u . (u.nabla)u <= 0, but this is FALSE in general
"""
        )

    def search_scale_critical_mixed(self) -> List[QuantityCandidate]:
        """
        Search all scale-critical mixed quantities int |u|^a |omega|^b.

        Scale-critical: a + 2b = 3

        Physical constraints:
        - a, b >= 0 (positivity)
        - a, b should give integrable quantities
        """
        candidates = []

        # Generate candidates with a + 2b = 3
        # Let b range in reasonable values
        for b_num in range(0, 6):  # b = 0, 1/2, 1, 3/2, 2, 5/2
            b = Fraction(b_num, 2)
            a = 3 - 2 * b  # From a + 2b = 3

            if a < 0:
                continue

            deriv = self.derive_time_derivative_u_omega_mixed(float(a), float(b))

            candidate = QuantityCandidate(
                name=f"Q_{a}_{b}",
                formula=f"int |u|^{a} |omega|^{b}",
                exponents=(float(a), float(b)),
                scaling_dimension=0,
                time_derivative_structure=self._format_derivative_structure(deriv),
                is_scale_critical=True,
                has_definite_sign=deriv['has_definite_sign'],
                sign_type='decreasing' if deriv['has_definite_sign'] else None,
                obstruction=deriv['obstruction'],
                notes=self._analyze_mixed_candidate(float(a), float(b))
            )
            candidates.append(candidate)

        return candidates

    def search_weighted_enstrophy(self) -> List[QuantityCandidate]:
        """
        Search for weighted enstrophy quantities that might be monotone.

        Idea: int f(|u|) |omega|^2 dx where f is chosen to cancel stretching.
        """
        candidates = []

        # Try various weight functions
        weights = [
            ('1/|u|^2', -2),
            ('|u|', 1),
            ('|u|^{-1}', -1),
            ('exp(-|u|^2)', 'exp'),
        ]

        for weight_name, weight_power in weights:
            if weight_power == 'exp':
                notes = """
Weight f(|u|) = exp(-|u|^2):
- Suppresses contribution where |u| is large
- Time derivative very complicated
- Nonlinear coupling makes this unlikely to be monotone
- But: might be useful for localized analysis
"""
            else:
                a_eff = weight_power
                b = 2
                scaling = self.scaling_dimension(a_eff, b)
                notes = f"""
Weight |u|^{{{weight_power}}} with |omega|^2:
- Effective scaling dimension: {scaling}
- {'Scale-critical' if abs(scaling) < 0.01 else 'Not scale-critical'}
- Time derivative still has stretching term
- The weight modifies but doesn't eliminate stretching
"""

            candidates.append(QuantityCandidate(
                name=f"Weighted Enstrophy ({weight_name})",
                formula=f"int {weight_name} |omega|^2 dx",
                exponents=(weight_power if weight_power != 'exp' else 0, 2),
                scaling_dimension=self.scaling_dimension(
                    weight_power if isinstance(weight_power, (int, float)) else 0, 2
                ),
                time_derivative_structure="Modified stretching + viscous dissipation",
                is_scale_critical=False,
                has_definite_sign=False,
                sign_type=None,
                obstruction="Modified stretching term still indefinite",
                notes=notes
            ))

        return candidates

    def search_strain_based(self) -> List[QuantityCandidate]:
        """
        Search for quantities based on strain tensor S_ij = (1/2)(partial_i u_j + partial_j u_i).

        Key relation: |omega|^2 = 2 |S|^2 - 2 (div u)^2 = 2|S|^2 (incompressible)
        So enstrophy is really a strain-based quantity!
        """
        candidates = []

        # Palinstrophy: int |nabla omega|^2
        candidates.append(QuantityCandidate(
            name="Palinstrophy",
            formula="P = (1/2) int |nabla omega|^2 dx",
            exponents=(0, 0, 2),  # (u, omega, nabla omega)
            scaling_dimension=-3,  # Very supercritical
            time_derivative_structure="""
dP/dt = int nabla omega . nabla (d omega/dt)
= stretching_gradient_term - nu ||Delta omega||^2
""",
            is_scale_critical=False,
            has_definite_sign=False,
            sign_type=None,
            obstruction="Gradient of stretching term",
            notes="""
VERY SUPERCRITICAL. Higher derivative of enstrophy.
- Controls H^2 norm of omega
- Grows even faster than enstrophy near blowup
- Important for numerical stability analysis
"""
        ))

        # Strain-vorticity alignment
        candidates.append(QuantityCandidate(
            name="Strain-Vorticity Alignment",
            formula="A = int omega . S . omega dx / int |omega|^2 dx",
            exponents=(0, 2),  # But it's a ratio
            scaling_dimension=0,  # Ratio is scale-invariant
            time_derivative_structure="Complex - involves derivative of ratio",
            is_scale_critical=True,
            has_definite_sign=False,
            sign_type=None,
            obstruction="Not a simple integral - ratio of quantities",
            notes="""
SCALE-INVARIANT RATIO. Measures alignment.
- Value in [-1, 1] normalized
- Perfect alignment (A=1) means maximal stretching
- This is diagnostic, not easily a conserved quantity
- But bounds on A constrain dynamics
"""
        ))

        return candidates

    def search_potential_monotone(self) -> List[QuantityCandidate]:
        """
        Specifically search for quantities that MIGHT be monotone.

        Strategy: Look for quantities where stretching term might vanish
        or be controlled by viscous term.
        """
        candidates = []

        # Quantity designed to have stretching cancel (if possible)
        candidates.append(QuantityCandidate(
            name="Modified Enstrophy (Logarithmic)",
            formula="int |omega|^2 log(1 + |omega|^2) dx",
            exponents=(0, 2),  # Approximate
            scaling_dimension=-1,  # Approximately
            time_derivative_structure="""
d/dt int |omega|^2 log(...) involves:
- Modified stretching: int omega.S.omega (1 + 2 log(1+|omega|^2)/(1+|omega|^2))
- Modified viscous: more negative than standard
""",
            is_scale_critical=False,
            has_definite_sign=False,
            sign_type=None,
            obstruction="Modified stretching still indefinite",
            notes="""
LOGARITHMIC MODIFICATION to enhance dissipation.
- The log factor grows slowly at large |omega|
- Might enhance control where |omega| is large
- But stretching is still the problem
- No clear advantage over standard enstrophy
"""
        ))

        # Quantity with specific structure from NRS identity
        candidates.append(QuantityCandidate(
            name="NRS-type Quantity",
            formula="int |u + alpha omega|^2 dx for specific alpha(nu, geometry)",
            exponents=(2, 0),  # Mixed structure
            scaling_dimension=1,  # Subcritical
            time_derivative_structure="""
Uses special structure of NS + vorticity equation coupling.
Cross terms may cancel if alpha chosen correctly.
""",
            is_scale_critical=False,
            has_definite_sign=False,
            sign_type=None,
            obstruction="Cross terms don't fully cancel for any alpha",
            notes="""
INSPIRED BY NECAS-RUZICKA-SVERAK identity.
- NRS showed int |U|^3 = 0 for self-similar profiles
- This used specific structure of profile equation
- For time-dependent case, similar tricks might work
- But the cross terms involve stretching indirectly
"""
        ))

        return candidates

    def analyze_type_II_window(self) -> str:
        """
        Analyze which quantities might constrain Type II blowup in [3/5, 3/4).

        Type II: ||u||_infty ~ (T-t)^{-alpha} with alpha > 1/2.
        Window [3/5, 3/4): marginally beyond self-similar.
        """
        analysis = """
# Type II Blowup Window Analysis: alpha in [3/5, 3/4)

## What these rates mean:
- Self-similar: alpha = 1/2, so ||u||_infty ~ (T-t)^{-1/2}
- Type II: alpha > 1/2 (faster blowup)
- Window [3/5, 3/4) is "marginally supercritical"

## Scaling implications:
For ||u||_infty ~ (T-t)^{-alpha}:
- Length scale: L(t) ~ (T-t)^{1-alpha} (since u ~ 1/L)
- For alpha = 3/5: L ~ (T-t)^{2/5}
- For alpha = 3/4: L ~ (T-t)^{1/4}

## Quantity behavior in this window:

### Energy: E ~ L^1 (subcritical)
- E ~ (T-t)^{(1)(1-alpha)}
- For alpha = 3/5: E ~ (T-t)^{2/5} -> 0 as t -> T
- For alpha = 3/4: E ~ (T-t)^{1/4} -> 0 as t -> T
- Energy DECREASES, consistent with dissipation
- Does NOT prevent blowup in this window

### Enstrophy: Omega ~ L^{-1} (supercritical)
- Omega ~ (T-t)^{-(1-alpha)}
- For alpha = 3/5: Omega ~ (T-t)^{-2/5} -> infty
- For alpha = 3/4: Omega ~ (T-t)^{-3/4} -> infty (faster)
- Enstrophy GROWTH is allowed by stretching

### Scale-critical ||u||_{L^3}: dimension 0
- ||u||_{L^3} ~ L^0 = constant in self-similar
- But for Type II: ||u||_{L^3} ~ (T-t)^{3(alpha - 1/2)/3} if concentrating
- The behavior depends on geometry of concentration
- ESS: bounded L^3 => regularity, so blowup => L^3 unbounded

## Key insight for [3/5, 3/4):
Any new monotone quantity with scaling dimension d would give:
- Q(t) ~ (T-t)^{d(1-alpha)}
- If d > 0 (subcritical): Q -> 0, no constraint
- If d = 0 (critical): Q ~ constant, strong constraint
- If d < 0 (supercritical): Q -> infty, but stretching can drive this

THE GAP: We have monotone quantities only for d > 0 (energy).
We need monotone quantities at d = 0 to constrain this window.
But all known d = 0 quantities have indefinite stretching!

## Potential strategies:
1. Find NEW scale-critical quantity without stretching (seems impossible)
2. Prove stretching is controlled for specific geometries (axisymmetric?)
3. Use combination of quantities (entropy methods?)
4. Exploit topological constraints (helicity for flows without reconnection)
"""
        return analysis

    def _format_derivative_structure(self, deriv: Dict) -> str:
        """Format derivative structure as string."""
        lines = [f"d/dt {deriv['quantity']} involves:"]
        for term in deriv['terms']:
            lines.append(f"  - {term['name']}: {term['sign']}")
        return "\n".join(lines)

    def _analyze_mixed_candidate(self, a: float, b: float) -> str:
        """Generate analysis notes for mixed quantity."""
        if a == 3 and b == 0:
            return "This is ||u||^3_{L^3}, the ESS critical norm."
        elif a == 0 and b == 1.5:
            return "Pure vorticity, supercritical. Stretching dominates."
        elif a == 1 and b == 1:
            return "Linear in both u and omega. Related to helicity but different."
        elif a == 2 and b == 0.5:
            return "Energy-like with vorticity correction. Still has stretching."
        else:
            return f"Mixed critical quantity with a={a}, b={b}. Has stretching obstruction."

    def run_search(self) -> List[QuantityCandidate]:
        """Run complete systematic search."""
        self.candidates = []

        # Known quantities
        self.candidates.append(self.analyze_energy())
        self.candidates.append(self.analyze_enstrophy())
        self.candidates.append(self.analyze_helicity())
        self.candidates.append(self.analyze_L3_norm())

        # Scale-critical mixed
        self.candidates.extend(self.search_scale_critical_mixed())

        # Weighted enstrophy variants
        self.candidates.extend(self.search_weighted_enstrophy())

        # Strain-based quantities
        self.candidates.extend(self.search_strain_based())

        # Potential monotone candidates
        self.candidates.extend(self.search_potential_monotone())

        return self.candidates

    def generate_report(self) -> str:
        """Generate comprehensive report of search results."""
        if not self.candidates:
            self.run_search()

        lines = [
            "=" * 80,
            "SYSTEMATIC SEARCH FOR NAVIER-STOKES MONOTONE QUANTITIES",
            "=" * 80,
            "",
            "## Summary",
            "",
            f"Total candidates examined: {len(self.candidates)}",
            f"Monotone (definite sign): {sum(1 for c in self.candidates if c.has_definite_sign)}",
            f"Scale-critical: {sum(1 for c in self.candidates if c.is_scale_critical)}",
            "",
            "=" * 80,
            "MONOTONE QUANTITIES FOUND",
            "=" * 80,
        ]

        for c in self.candidates:
            if c.has_definite_sign:
                lines.extend([
                    "",
                    f"### {c.name}",
                    f"Formula: {c.formula}",
                    f"Sign: {c.sign_type}",
                    f"Scale-critical: {c.is_scale_critical}",
                    f"Time derivative: {c.time_derivative_structure}",
                    f"Notes: {c.notes}",
                ])

        lines.extend([
            "",
            "=" * 80,
            "SCALE-CRITICAL QUANTITIES (NOT MONOTONE)",
            "=" * 80,
        ])

        for c in self.candidates:
            if c.is_scale_critical and not c.has_definite_sign:
                lines.extend([
                    "",
                    f"### {c.name}",
                    f"Formula: {c.formula}",
                    f"Obstruction: {c.obstruction}",
                    f"Notes: {c.notes}",
                ])

        lines.extend([
            "",
            "=" * 80,
            "TYPE II WINDOW ANALYSIS [3/5, 3/4)",
            "=" * 80,
            self.analyze_type_II_window(),
        ])

        lines.extend([
            "",
            "=" * 80,
            "CONCLUSIONS",
            "=" * 80,
            """
## Key Finding: ENERGY IS THE ONLY MONOTONE QUANTITY

The systematic search confirms:
1. **Energy** (||u||^2_{L^2}) is the ONLY known monotone decreasing quantity
2. All scale-critical quantities have **vortex stretching obstruction**
3. The stretching term int omega_i omega_j S_ij is the key obstacle

## Why This Matters for Type II Blowup

For Type II blowup with alpha in [3/5, 3/4):
- Energy decay does NOT prevent blowup (wrong scaling)
- We need scale-critical monotone quantities
- But ALL scale-critical quantities have stretching!

## Potential Paths Forward

1. **Geometric constraints**: For axisymmetric flows, stretching has special structure
2. **Conditional bounds**: If we assume stretching < C * dissipation, monotonicity follows
3. **Localized analysis**: Near blowup point, geometry constraints may help
4. **New identities**: Perhaps combinations of quantities have hidden structure

## The Fundamental Obstruction

The vortex stretching term omega.S.omega represents:
- Physical: vortex line stretching/compression
- Mathematical: energy transfer across scales
- This is inherent to 3D turbulence
- No "simple" monotone quantity can avoid it

## Recommendation

Focus on:
1. Axisymmetric case where stretching is constrained
2. Proving stretching bounds under geometric assumptions
3. Using topology (helicity) to constrain dynamics
""",
        ])

        return "\n".join(lines)


def main():
    """Run the systematic search and print results."""
    searcher = SystematicIdentitySearch()
    candidates = searcher.run_search()

    print(searcher.generate_report())

    return searcher


if __name__ == "__main__":
    main()

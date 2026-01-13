"""
Blowup construction and analysis for 3D Navier-Stokes.

This module attempts to construct Type II blowup solutions
exploiting the theoretical gaps:
- Type II blowup with alpha in (1/2, 3/5) is NOT ruled out
- The concentration function C(r) is NOT monotone
- Energy is the ONLY monotone quantity
- The dimensional gap (0.9) gives "freedom" for concentration

Key Components:
- Type II construction: Self-similar ansatz and profile equations
- Cascade design: Variable cascade factors for Type II blowup
- Concentration analysis: Track energy concentration across scales
"""

from .type_ii_construction import (
    TypeIIBlowupConstructor,
    ModifiedSelfSimilarAnsatz,
    ProfileEquation,
    ConcentrationAnalyzer,
    CascadeConstructor,
    NumericalVerifier,
    TypeIIParameters,
    demonstrate_type_ii_construction,
)

__all__ = [
    # Type II construction
    'TypeIIBlowupConstructor',
    'ModifiedSelfSimilarAnsatz',
    'ProfileEquation',
    'ConcentrationAnalyzer',
    'CascadeConstructor',
    'NumericalVerifier',
    'TypeIIParameters',
    'demonstrate_type_ii_construction',
]

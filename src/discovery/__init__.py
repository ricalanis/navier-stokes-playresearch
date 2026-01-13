"""
Discovery module for Navier-Stokes inequality discovery.

This module contains tools for discovering new functional inequalities
using genetic algorithms and other optimization techniques.

Key tools:
- genetic_inequality: Genetic algorithm for finding functional inequalities
- entropy_methods: Information-theoretic and entropy-based approaches
- spectral_concentration: Spectral analysis of concentration operators
- proof_search: Symbolic proof search engine for NS regularity
- constructive_bounds: Explicit constant computation with rigorous verification
- category_theory: Categorical structures in PDE analysis
- dynamical_systems: Flow analysis in function space
- renormalization: Multi-scale renormalization group methods
"""

from .proof_search import (
    KnowledgeBase,
    Statement,
    StatementType,
    InferenceRule,
    ProofSearchEngine,
    ProofResult,
    ProofVisualizer,
    GapDetector,
    run_proof_search,
    run_gap_analysis,
    export_knowledge_base,
)

from .genetic_inequality import (
    GeneticInequalityDiscovery,
    ExpressionTree,
    ExpressionNode,
    InequalityCandidate,
    Dimension,
    StandardDimensions,
    FitnessEvaluator,
    GeneticOperator,
    InequalityValidator,
    ExpressionGenerator,
    run_discovery,
)

from .constructive_bounds import (
    ConstructiveBounds,
    ExplicitSobolevConstants,
    ExplicitCKNConstants,
    ExplicitGagliardoNirenberg,
    IterativeBoundsComputer,
    CriticalCalculation,
    IntervalVerifiedComputation,
    SobolevConstantResult,
    CKNResult,
    GNResult,
    IterationResult,
    IntervalResult,
    CriticalResult,
)

__all__ = [
    # Proof search
    'KnowledgeBase',
    'Statement',
    'StatementType',
    'InferenceRule',
    'ProofSearchEngine',
    'ProofResult',
    'ProofVisualizer',
    'GapDetector',
    'run_proof_search',
    'run_gap_analysis',
    'export_knowledge_base',
    # Genetic inequality discovery
    'GeneticInequalityDiscovery',
    'ExpressionTree',
    'ExpressionNode',
    'InequalityCandidate',
    'Dimension',
    'StandardDimensions',
    'FitnessEvaluator',
    'GeneticOperator',
    'InequalityValidator',
    'ExpressionGenerator',
    'run_discovery',
    # Constructive bounds
    'ConstructiveBounds',
    'ExplicitSobolevConstants',
    'ExplicitCKNConstants',
    'ExplicitGagliardoNirenberg',
    'IterativeBoundsComputer',
    'CriticalCalculation',
    'IntervalVerifiedComputation',
    'SobolevConstantResult',
    'CKNResult',
    'GNResult',
    'IterationResult',
    'IntervalResult',
    'CriticalResult',
]

"""
MCTS-based Proof Explorer for Navier-Stokes Regularity.

This module implements Monte Carlo Tree Search for systematically
exploring and validating the axisymmetric Navier-Stokes regularity proof.

Main components:
- state: Proof state representation
- actions: Proof tactics and actions
- rewards: Multi-objective reward functions
- tree: MCTS tree structure
- search: Main MCTS algorithm
- oracles: Numerical and symbolic verification
"""

from .state import ProofState, LemmaStatus, ProofContext
from .actions import Action, ActionType, get_legal_actions
from .rewards import RewardFunction, RewardComponents
from .tree import MCTSNode
from .search import ProofMCTS, ParallelProofMCTS

__all__ = [
    'ProofState',
    'LemmaStatus',
    'ProofContext',
    'Action',
    'ActionType',
    'get_legal_actions',
    'RewardFunction',
    'RewardComponents',
    'MCTSNode',
    'ProofMCTS',
    'ParallelProofMCTS'
]

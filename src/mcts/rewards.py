"""
Reward function design for MCTS proof exploration.

Multi-objective rewards balancing:
- Proof progress and goal completion
- Logical soundness (no gaps or circular reasoning)
- Numerical consistency
- Proof elegance (shorter, simpler proofs preferred)
- Novelty (exploring new paths)
"""

from dataclasses import dataclass, field
from typing import Dict, Set, List, Optional, Any
import numpy as np

from .state import ProofState, LemmaStatus
from .actions import Action, ActionType


@dataclass
class RewardComponents:
    """Components of the reward function."""

    # Primary: Proof progress
    goal_completion: float = 0.0        # 0-1 for partial, 1.0 for complete
    subgoal_progress: float = 0.0       # Fraction of subgoals resolved

    # Logical soundness
    gap_penalty: float = 0.0            # Penalty for logical gaps
    circular_penalty: float = 0.0       # Penalty for circular reasoning

    # Numerical consistency
    numerical_agreement: float = 1.0    # Agreement with numerical experiments

    # Elegance metrics
    proof_length_penalty: float = 0.0   # Shorter proofs preferred
    complexity_penalty: float = 0.0     # Simpler arguments preferred

    # Novelty bonus
    new_path_bonus: float = 0.0         # Bonus for unexplored strategies

    def total(self, weights: Optional[Dict[str, float]] = None) -> float:
        """Weighted sum of components."""
        if weights is None:
            weights = DEFAULT_WEIGHTS

        return (
            weights.get("goal", 10.0) * self.goal_completion +
            weights.get("subgoal", 3.0) * self.subgoal_progress +
            weights.get("gap", -5.0) * self.gap_penalty +
            weights.get("circular", -10.0) * self.circular_penalty +
            weights.get("numerical", 2.0) * self.numerical_agreement +
            weights.get("length", -0.1) * self.proof_length_penalty +
            weights.get("complexity", -0.2) * self.complexity_penalty +
            weights.get("novelty", 1.0) * self.new_path_bonus
        )


# Default reward weights
DEFAULT_WEIGHTS = {
    "goal": 10.0,
    "subgoal": 3.0,
    "gap": -5.0,
    "circular": -10.0,
    "numerical": 2.0,
    "length": -0.1,
    "complexity": -0.2,
    "novelty": 1.0
}


# Special rewards for domain-specific achievements
SPECIAL_REWARDS = {
    # Closing known gaps
    "spectral_gap_lemma": 5.0,          # Key lemma for viscous homogenization
    "swirl_decay": 3.0,                 # Extension to flows with swirl
    "type_ii_exclusion_gap": 10.0,      # Main gap region proof

    # Finding edge cases
    "alpha_boundary_analysis": 2.0,     # What happens at alpha = 1/2

    # Optimal constants
    "improved_constants": 1.5,          # Finding tighter bounds

    # Alternative proofs
    "alternative_spectral_gap": 3.0,    # New approach to key lemma
    "direct_linfty_decay": 4.0,         # Bypass L2 -> Linfty
}


class RewardFunction:
    """Compute rewards for proof states."""

    def __init__(self, numerical_oracle: Optional[Any] = None,
                 weights: Optional[Dict[str, float]] = None):
        self.numerical = numerical_oracle
        self.weights = weights or DEFAULT_WEIGHTS
        self.visited_states: Set[str] = set()

    def compute(self, state: ProofState, action: Action,
                next_state: ProofState) -> RewardComponents:
        """Compute reward for state transition."""

        # Goal completion
        goal_completion = self._compute_goal_completion(next_state)

        # Subgoal progress
        subgoal_progress = self._compute_subgoal_progress(state, next_state)

        # Gap penalty
        gaps = self._detect_gaps(next_state)
        gap_penalty = len(gaps) / max(len(next_state.lemma_status), 1)

        # Circular dependency check
        circular = next_state.dependencies.check_circular()
        circular_penalty = 1.0 if circular else 0.0

        # Numerical verification
        numerical_agreement = self._check_numerical_consistency(next_state, action)

        # Proof complexity metrics
        proof_length_penalty = len(next_state.history) / 100.0
        complexity_penalty = self._compute_complexity(next_state)

        # Novelty
        state_hash = next_state.hash_state()
        new_path_bonus = 1.0 if state_hash not in self.visited_states else 0.0
        self.visited_states.add(state_hash)

        return RewardComponents(
            goal_completion=goal_completion,
            subgoal_progress=subgoal_progress,
            gap_penalty=gap_penalty,
            circular_penalty=circular_penalty,
            numerical_agreement=numerical_agreement,
            proof_length_penalty=proof_length_penalty,
            complexity_penalty=complexity_penalty,
            new_path_bonus=new_path_bonus
        )

    def _compute_goal_completion(self, state: ProofState) -> float:
        """Check if main theorem is proven."""
        if state.target_theorem.status == LemmaStatus.PROVEN:
            return 1.0
        elif state.target_theorem.status == LemmaStatus.BLOCKED:
            return 0.0
        else:
            # Partial credit for progress
            deps = state.target_theorem.dependencies
            proven = sum(1 for d in deps
                        if state.lemma_status.get(d) in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED])
            return proven / max(len(deps), 1) * 0.9

    def _compute_subgoal_progress(self, old_state: ProofState,
                                   new_state: ProofState) -> float:
        """Compute progress on subgoals."""
        proven_before = sum(1 for s in old_state.lemma_status.values()
                          if s == LemmaStatus.PROVEN)
        proven_after = sum(1 for s in new_state.lemma_status.values()
                         if s == LemmaStatus.PROVEN)
        total_goals = len(new_state.lemma_status)
        return (proven_after - proven_before) / max(total_goals, 1)

    def _detect_gaps(self, state: ProofState) -> List[str]:
        """Detect logical gaps in the proof."""
        gaps = []
        for lemma_id, status in state.lemma_status.items():
            if status == LemmaStatus.OPEN:
                # Check if this blocks the main theorem
                if self._blocks_main_theorem(lemma_id, state):
                    gaps.append(lemma_id)
        return gaps

    def _blocks_main_theorem(self, lemma_id: str, state: ProofState) -> bool:
        """Check if a lemma blocks the main theorem."""
        # Simple check: is it in the dependency path?
        visited = set()
        queue = [lemma_id]

        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)

            dependents = state.dependencies.get_dependents(current)
            if "main_theorem" in dependents:
                return True
            queue.extend(dependents)

        return False

    def _check_numerical_consistency(self, state: ProofState,
                                     action: Action) -> float:
        """Check if proof claims are numerically consistent."""
        if self.numerical is None:
            return 1.0  # No oracle, assume consistent

        if action.type == ActionType.APPLY_INEQUALITY:
            # Verify the inequality numerically
            return self.numerical.verify_inequality(
                action.target, state.context
            )
        elif action.type == ActionType.CHECK_NUMERICALLY:
            # Get numerical evidence
            if action.target in state.numerical_evidence:
                return state.numerical_evidence[action.target].success_rate
            return 1.0

        return 1.0  # No numerical check applicable

    def _compute_complexity(self, state: ProofState) -> float:
        """Compute proof complexity metric."""
        complexity = 0.0

        # Penalize many case splits
        case_splits = sum(1 for step in state.history
                         if step.action_type == ActionType.CASE_SPLIT.value)
        complexity += case_splits * 0.5

        # Penalize deep dependency chains
        if state.dependencies:
            depths = []
            for node in state.dependencies.nodes:
                depth = self._compute_depth(node, state.dependencies)
                depths.append(depth)
            if depths:
                complexity += max(depths) * 0.1

        # Penalize many hypotheses
        complexity += len(state.context.hypotheses) * 0.05

        return complexity

    def _compute_depth(self, node: str, deps) -> int:
        """Compute depth of a node in dependency graph."""
        predecessors = deps.get_dependencies(node)
        if not predecessors:
            return 0
        return 1 + max(self._compute_depth(p, deps) for p in predecessors)

    def compute_special_rewards(self, state: ProofState,
                                 action: Action) -> float:
        """Compute special domain-specific rewards."""
        special = 0.0

        # Check for newly proven key lemmas
        if action.type == ActionType.APPLY_LEMMA:
            target = action.target
            if target in SPECIAL_REWARDS:
                if state.lemma_status.get(target) == LemmaStatus.PROVEN:
                    special += SPECIAL_REWARDS[target]

        # Bonus for proving main gap region theorem
        if state.lemma_status.get("type_ii_exclusion_gap") == LemmaStatus.PROVEN:
            special += SPECIAL_REWARDS["type_ii_exclusion_gap"]

        return special


class AdaptiveRewardFunction(RewardFunction):
    """Reward function that adapts weights based on exploration progress."""

    def __init__(self, numerical_oracle: Optional[Any] = None,
                 initial_weights: Optional[Dict[str, float]] = None):
        super().__init__(numerical_oracle, initial_weights)
        self.iteration_count = 0
        self.success_history: List[bool] = []

    def adapt_weights(self, recent_success_rate: float):
        """Adapt weights based on exploration success."""
        self.iteration_count += 1

        # If making progress, maintain current weights
        if recent_success_rate > 0.3:
            return

        # If stuck, increase exploration bonuses
        if recent_success_rate < 0.1:
            self.weights["novelty"] *= 1.2
            self.weights["gap"] *= 0.9  # Reduce gap penalty slightly

        # Periodically reset to avoid weight explosion
        if self.iteration_count % 1000 == 0:
            self._reset_weights()

    def _reset_weights(self):
        """Reset weights to defaults."""
        self.weights = DEFAULT_WEIGHTS.copy()


class HierarchicalRewardFunction(RewardFunction):
    """Reward function with hierarchical goal structure."""

    def __init__(self, numerical_oracle: Optional[Any] = None):
        super().__init__(numerical_oracle)

        # Define goal hierarchy
        self.goal_hierarchy = {
            "main_theorem": 1.0,         # Top priority
            "type_ii_exclusion_gap": 0.9,
            "spectral_gap_lemma": 0.8,
            "l2_decay_theorem": 0.7,
            "effective_viscosity_divergence": 0.6,
            "swirl_decay": 0.5
        }

    def compute_hierarchical_reward(self, state: ProofState,
                                    action: Action,
                                    next_state: ProofState) -> float:
        """Compute reward with hierarchical weighting."""
        base_reward = self.compute(state, action, next_state)

        # Add hierarchical bonus for progress on high-priority goals
        hierarchical_bonus = 0.0

        for goal, priority in self.goal_hierarchy.items():
            old_status = state.lemma_status.get(goal, LemmaStatus.OPEN)
            new_status = next_state.lemma_status.get(goal, LemmaStatus.OPEN)

            if old_status != LemmaStatus.PROVEN and new_status == LemmaStatus.PROVEN:
                hierarchical_bonus += priority * 5.0

        return base_reward.total(self.weights) + hierarchical_bonus


def create_reward_function(oracle: Optional[Any] = None,
                          adaptive: bool = False,
                          hierarchical: bool = False) -> RewardFunction:
    """Factory function to create reward functions."""
    if hierarchical:
        return HierarchicalRewardFunction(oracle)
    elif adaptive:
        return AdaptiveRewardFunction(oracle)
    else:
        return RewardFunction(oracle)

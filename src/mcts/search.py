"""
Main MCTS search algorithm for proof exploration.

Implements:
- Standard MCTS with UCB1 selection
- Parallel MCTS for faster exploration
- Domain-specific heuristics for proof search
"""

import copy
import random
import time
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import numpy as np

from .state import (
    ProofState, LemmaStatus, create_initial_proof_state,
    create_ns_theorem_registry, create_dependency_graph
)
from .actions import Action, ActionType, get_legal_actions, apply_action, create_ns_proof_actions
from .rewards import RewardFunction, RewardComponents, create_reward_function, DEFAULT_WEIGHTS
from .tree import MCTSNode, MCTSTree, determine_branch_type


@dataclass
class MCTSConfig:
    """Configuration for MCTS search."""
    exploration_constant: float = 1.414
    max_iterations: int = 10000
    max_depth: int = 50
    rollout_depth: int = 10
    reward_weights: Dict[str, float] = field(default_factory=lambda: DEFAULT_WEIGHTS.copy())
    use_domain_heuristics: bool = True
    random_seed: Optional[int] = None


@dataclass
class SearchStats:
    """Statistics from MCTS search."""
    iterations: int = 0
    max_depth_reached: int = 0
    proofs_found: int = 0
    gaps_detected: List[str] = field(default_factory=list)
    time_elapsed: float = 0.0
    nodes_expanded: int = 0
    rollouts_performed: int = 0


class ProofMCTS:
    """Monte Carlo Tree Search for proof exploration."""

    def __init__(self, config: Optional[MCTSConfig] = None,
                 numerical_oracle: Optional[Any] = None):
        self.config = config or MCTSConfig()

        # Set random seed if specified
        if self.config.random_seed is not None:
            random.seed(self.config.random_seed)
            np.random.seed(self.config.random_seed)

        # Initialize reward function
        self.reward_fn = create_reward_function(numerical_oracle)
        self.numerical_oracle = numerical_oracle

        # Root node and tree
        self.root: Optional[MCTSNode] = None
        self.tree: Optional[MCTSTree] = None

        # Statistics
        self.stats = SearchStats()

        # Action library
        self.actions = create_ns_proof_actions()

    def initialize(self, initial_state: Optional[ProofState] = None):
        """Initialize the tree with initial proof state."""
        if initial_state is None:
            initial_state = create_initial_proof_state()

        self.root = MCTSNode(
            state=initial_state,
            parent=None,
            proof_depth=0,
            branch_type="root"
        )
        self.tree = MCTSTree(self.root)

    def search(self, iterations: Optional[int] = None) -> List[MCTSNode]:
        """Run MCTS search and return best path."""
        if self.root is None:
            self.initialize()

        iterations = iterations or self.config.max_iterations
        start_time = time.time()

        for i in range(iterations):
            self.stats.iterations = i + 1

            # 1. Selection
            node = self._select(self.root)

            # 2. Expansion
            if not node.is_fully_expanded() and node.proof_depth < self.config.max_depth:
                node = self._expand(node)
                self.stats.nodes_expanded += 1

            # 3. Simulation (rollout)
            reward = self._simulate(node)
            self.stats.rollouts_performed += 1

            # 4. Backpropagation
            self._backpropagate(node, reward)

            # Check for proof completion
            if self.root.state.target_theorem.status == LemmaStatus.PROVEN:
                self.stats.proofs_found += 1
                print(f"Proof found after {i+1} iterations!")
                break

            # Periodic progress report
            if (i + 1) % 100 == 0:
                self._report_progress(i + 1)

        self.stats.time_elapsed = time.time() - start_time
        return self.tree.get_best_path()

    def _select(self, node: MCTSNode) -> MCTSNode:
        """Select a node to expand using UCB1."""
        while not node.is_terminal():
            if not node.is_fully_expanded():
                return node
            else:
                node = node.best_child(self.config.exploration_constant)
                self.stats.max_depth_reached = max(
                    self.stats.max_depth_reached,
                    node.proof_depth
                )
        return node

    def _expand(self, node: MCTSNode) -> MCTSNode:
        """Expand node with an untried action."""
        untried = node.get_untried_actions()

        if not untried:
            return node

        # Select action (with domain-specific heuristics if enabled)
        if self.config.use_domain_heuristics:
            action = self._select_action_with_heuristics(untried, node)
        else:
            action = random.choice(untried)

        return node.expand(action)

    def _simulate(self, node: MCTSNode) -> float:
        """Simulate a rollout from the node."""
        state = node.state.clone()
        total_reward = 0.0

        for _ in range(self.config.rollout_depth):
            if state.is_terminal():
                break

            actions = get_legal_actions(state)
            if not actions:
                break

            # Random action selection (could use policy network here)
            action = random.choice(actions)
            next_state = apply_action(state, action)

            # Compute reward
            reward_components = self.reward_fn.compute(state, action, next_state)
            total_reward += reward_components.total(self.config.reward_weights)

            state = next_state

        return total_reward

    def _backpropagate(self, node: MCTSNode, reward: float):
        """Backpropagate reward up the tree."""
        while node is not None:
            node.visits += 1
            node.total_reward += reward
            node = node.parent

    def _select_action_with_heuristics(self, actions: List[Action],
                                        node: MCTSNode) -> Action:
        """Select action using domain-specific heuristics."""
        scored_actions = []

        for action in actions:
            score = 0.0

            # Prefer numerical verification when available
            if action.type == ActionType.CHECK_NUMERICALLY:
                score += 2.0

            # Prefer applying proven lemmas
            if action.type == ActionType.APPLY_LEMMA:
                status = node.state.lemma_status.get(action.target)
                if status in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED]:
                    score += 1.5
                elif status == LemmaStatus.OPEN:
                    # Bonus for deriving open lemmas
                    score += 2.0

            # Prioritize actions related to spectral gap (key lemma)
            if action.target and "spectral_gap" in str(action.target).lower():
                score += 3.0

            # Prioritize actions for the gap region
            if node.branch_type == "type_ii_gap":
                if "viscosity" in str(action.target).lower():
                    score += 1.5
                if "decay" in str(action.target).lower():
                    score += 1.5

            # Penalize expensive actions slightly
            score -= action.cost * 0.2

            scored_actions.append((score, action))

        # Softmax selection based on scores
        scores = np.array([s for s, _ in scored_actions])
        # Temperature for exploration
        temperature = 1.0
        probs = np.exp(scores / temperature)
        probs = probs / np.sum(probs)

        idx = np.random.choice(len(actions), p=probs)
        return scored_actions[idx][1]

    def _report_progress(self, iteration: int):
        """Report search progress."""
        tree_stats = self.tree.statistics()

        print(f"\n=== MCTS Progress (iteration {iteration}) ===")
        print(f"Max depth reached: {self.stats.max_depth_reached}")
        print(f"Root visits: {self.root.visits}")
        print(f"Best average reward: {self.root.average_reward:.4f}")
        print(f"Total nodes: {tree_stats['total_nodes']}")
        print(f"Proofs found: {self.stats.proofs_found}")

        # Key lemma status
        print("\nKey lemma status:")
        key_lemmas = [
            "type_ii_exclusion_gap",
            "spectral_gap_lemma",
            "l2_decay_theorem",
            "effective_viscosity_divergence"
        ]
        for lemma in key_lemmas:
            status = self.root.state.lemma_status.get(lemma, LemmaStatus.OPEN)
            print(f"  {lemma}: {status.value}")

    def get_best_proof_path(self) -> Tuple[List[MCTSNode], float]:
        """Get the best proof path and its total reward."""
        path = self.tree.get_best_path()
        total_reward = sum(n.average_reward for n in path)
        return path, total_reward

    def get_alternative_proofs(self, top_k: int = 5) -> List[List[MCTSNode]]:
        """Get alternative proof paths."""
        proven_paths = self.tree.get_proven_paths()
        if not proven_paths:
            # Return top-k paths by reward even if not complete
            all_leaves = self.tree.get_leaves()
            sorted_leaves = sorted(all_leaves, key=lambda n: n.average_reward, reverse=True)
            return [leaf.get_path_from_root() for leaf in sorted_leaves[:top_k]]

        return proven_paths[:top_k]

    def analyze_gaps(self) -> List[str]:
        """Analyze proof for gaps and blocking lemmas."""
        gaps = []
        state = self.root.state

        for lemma_id, status in state.lemma_status.items():
            if status == LemmaStatus.OPEN:
                # Check dependencies
                deps = state.dependencies.get_dependencies(lemma_id)
                all_deps_proven = all(
                    state.lemma_status.get(d) in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED]
                    for d in deps
                )
                if all_deps_proven:
                    gaps.append(f"{lemma_id}: ready to prove (deps satisfied)")
                else:
                    missing = [d for d in deps
                              if state.lemma_status.get(d) not in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED]]
                    gaps.append(f"{lemma_id}: blocked by {missing}")

        return gaps

    def export_results(self, filepath: str):
        """Export search results to JSON."""
        results = {
            "stats": {
                "iterations": self.stats.iterations,
                "max_depth": self.stats.max_depth_reached,
                "proofs_found": self.stats.proofs_found,
                "time_elapsed": self.stats.time_elapsed,
                "nodes_expanded": self.stats.nodes_expanded,
                "rollouts": self.stats.rollouts_performed
            },
            "tree_stats": self.tree.statistics(),
            "best_path": [
                {
                    "action": str(n.action.target) if n.action else "ROOT",
                    "reward": n.average_reward,
                    "visits": n.visits,
                    "branch_type": n.branch_type
                }
                for n in self.tree.get_best_path()
            ],
            "lemma_status": {
                k: v.value for k, v in self.root.state.lemma_status.items()
            },
            "gaps": self.analyze_gaps()
        }

        with open(filepath, 'w') as f:
            json.dump(results, f, indent=2)


class ParallelProofMCTS(ProofMCTS):
    """Parallelized MCTS for faster exploration."""

    def __init__(self, config: Optional[MCTSConfig] = None,
                 num_workers: int = 4,
                 numerical_oracle: Optional[Any] = None):
        super().__init__(config, numerical_oracle)
        self.num_workers = num_workers

    def search_parallel(self, iterations: int) -> List[MCTSNode]:
        """Run parallel MCTS with tree parallelization."""
        if self.root is None:
            self.initialize()

        iterations_per_worker = iterations // self.num_workers
        start_time = time.time()

        # Use ThreadPoolExecutor for simplicity (ProcessPool needs serialization)
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            futures = []
            for worker_id in range(self.num_workers):
                future = executor.submit(
                    self._worker_search,
                    iterations_per_worker,
                    worker_id
                )
                futures.append(future)

            # Collect and merge results
            for future in futures:
                worker_stats = future.result()
                self._merge_stats(worker_stats)

        self.stats.time_elapsed = time.time() - start_time
        return self.tree.get_best_path()

    def _worker_search(self, iterations: int, worker_id: int) -> SearchStats:
        """Worker search function."""
        # Set different random seed for each worker
        np.random.seed(worker_id * 1000 + int(time.time()) % 1000)
        random.seed(worker_id * 1000 + int(time.time()) % 1000)

        local_stats = SearchStats()

        for i in range(iterations):
            local_stats.iterations = i + 1

            node = self._select(self.root)
            if not node.is_fully_expanded():
                node = self._expand(node)
                local_stats.nodes_expanded += 1

            reward = self._simulate(node)
            local_stats.rollouts_performed += 1

            self._backpropagate(node, reward)

            if self.root.state.target_theorem.status == LemmaStatus.PROVEN:
                local_stats.proofs_found += 1
                break

        return local_stats

    def _merge_stats(self, worker_stats: SearchStats):
        """Merge worker statistics into main stats."""
        self.stats.iterations += worker_stats.iterations
        self.stats.nodes_expanded += worker_stats.nodes_expanded
        self.stats.rollouts_performed += worker_stats.rollouts_performed
        self.stats.proofs_found += worker_stats.proofs_found
        self.stats.max_depth_reached = max(
            self.stats.max_depth_reached,
            worker_stats.max_depth_reached
        )


def run_proof_search(config: Optional[Dict] = None,
                    parallel: bool = False,
                    num_workers: int = 4) -> Tuple[List[MCTSNode], SearchStats]:
    """
    Convenience function to run proof search.

    Args:
        config: Configuration dictionary
        parallel: Whether to use parallel search
        num_workers: Number of parallel workers

    Returns:
        Tuple of (best path, search statistics)
    """
    mcts_config = MCTSConfig(**config) if config else MCTSConfig()

    if parallel:
        mcts = ParallelProofMCTS(mcts_config, num_workers)
    else:
        mcts = ProofMCTS(mcts_config)

    mcts.initialize()
    best_path = mcts.search() if not parallel else mcts.search_parallel(mcts_config.max_iterations)

    return best_path, mcts.stats


def main():
    """Main entry point for proof exploration."""
    print("=" * 60)
    print("MCTS Proof Explorer for Axisymmetric NS Regularity")
    print("=" * 60)

    # Configuration
    config = MCTSConfig(
        exploration_constant=1.414,
        max_iterations=1000,
        max_depth=30,
        rollout_depth=5,
        use_domain_heuristics=True,
        random_seed=42
    )

    # Initialize and run search
    mcts = ProofMCTS(config)
    mcts.initialize()

    print("\nStarting MCTS search...")
    best_path = mcts.search()

    # Report results
    print("\n" + "=" * 60)
    print("SEARCH COMPLETE")
    print("=" * 60)

    print(f"\nStatistics:")
    print(f"  Total iterations: {mcts.stats.iterations}")
    print(f"  Max depth reached: {mcts.stats.max_depth_reached}")
    print(f"  Proofs found: {mcts.stats.proofs_found}")
    print(f"  Time elapsed: {mcts.stats.time_elapsed:.2f}s")

    print(f"\nBest proof path:")
    for i, node in enumerate(best_path):
        action_str = str(node.action.target) if node.action else "ROOT"
        print(f"  {i}. {action_str} (visits={node.visits}, reward={node.average_reward:.3f})")

    print(f"\nFinal lemma status:")
    final_state = best_path[-1].state
    for lemma_id, status in final_state.lemma_status.items():
        if status != LemmaStatus.ASSUMED:
            print(f"  {lemma_id}: {status.value}")

    print(f"\nGap analysis:")
    gaps = mcts.analyze_gaps()
    for gap in gaps[:10]:  # Limit output
        print(f"  - {gap}")

    # Export results
    mcts.export_results("mcts_proof_results.json")
    print(f"\nResults exported to mcts_proof_results.json")

    # Visualize tree
    print(f"\nTree structure:")
    print(mcts.tree.visualize(max_depth=3))


if __name__ == "__main__":
    main()

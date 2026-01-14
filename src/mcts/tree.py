"""
MCTS tree structure for proof exploration.

Implements the tree nodes with UCB-based selection,
expansion, and backpropagation support.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import numpy as np
import copy

from .state import ProofState, LemmaStatus
from .actions import Action, get_legal_actions, apply_action


@dataclass
class MCTSNode:
    """Node in the Monte Carlo Tree Search."""

    state: ProofState
    parent: Optional['MCTSNode'] = None
    children: Dict[Action, 'MCTSNode'] = field(default_factory=dict)

    # UCB statistics
    visits: int = 0
    total_reward: float = 0.0

    # Action that led to this state
    action: Optional[Action] = None

    # Proof-specific metadata
    proof_depth: int = 0
    branch_type: str = ""  # "type_i", "type_ii_gap", "type_ii_high", etc.

    @property
    def average_reward(self) -> float:
        """Average reward across all visits."""
        return self.total_reward / max(self.visits, 1)

    def ucb_score(self, c: float = 1.414) -> float:
        """Upper Confidence Bound score for selection."""
        if self.visits == 0:
            return float('inf')

        exploitation = self.average_reward
        parent_visits = self.parent.visits if self.parent else 1
        exploration = c * np.sqrt(np.log(parent_visits) / self.visits)

        return exploitation + exploration

    def is_fully_expanded(self) -> bool:
        """Check if all legal actions have been tried."""
        legal_actions = get_legal_actions(self.state)
        return len(self.children) >= len(legal_actions)

    def is_terminal(self) -> bool:
        """Check if this is a terminal state."""
        return self.state.is_terminal()

    def best_child(self, c: float = 1.414) -> 'MCTSNode':
        """Select best child by UCB."""
        if not self.children:
            return self

        return max(self.children.values(), key=lambda n: n.ucb_score(c))

    def most_visited_child(self) -> 'MCTSNode':
        """Select child with most visits (for final selection)."""
        if not self.children:
            return self

        return max(self.children.values(), key=lambda n: n.visits)

    def highest_reward_child(self) -> 'MCTSNode':
        """Select child with highest average reward."""
        if not self.children:
            return self

        return max(self.children.values(), key=lambda n: n.average_reward)

    def expand(self, action: Action) -> 'MCTSNode':
        """Expand with new action, creating child node."""
        if action in self.children:
            return self.children[action]

        next_state = apply_action(self.state, action)
        child = MCTSNode(
            state=next_state,
            parent=self,
            action=action,
            proof_depth=self.proof_depth + 1,
            branch_type=determine_branch_type(next_state)
        )
        self.children[action] = child
        return child

    def get_untried_actions(self) -> List[Action]:
        """Get actions that haven't been tried yet."""
        legal_actions = get_legal_actions(self.state)
        tried_actions = set(self.children.keys())
        return [a for a in legal_actions if a not in tried_actions]

    def get_path_from_root(self) -> List['MCTSNode']:
        """Get the path from root to this node."""
        path = []
        node = self
        while node is not None:
            path.append(node)
            node = node.parent
        return list(reversed(path))

    def get_depth(self) -> int:
        """Get depth from root."""
        depth = 0
        node = self.parent
        while node is not None:
            depth += 1
            node = node.parent
        return depth

    def clone(self) -> 'MCTSNode':
        """Create a deep copy of this node (without parent/children)."""
        return MCTSNode(
            state=self.state.clone(),
            parent=None,
            children={},
            visits=self.visits,
            total_reward=self.total_reward,
            action=self.action,
            proof_depth=self.proof_depth,
            branch_type=self.branch_type
        )

    def __repr__(self) -> str:
        action_str = str(self.action.type.value) if self.action else "ROOT"
        return f"MCTSNode({action_str}, visits={self.visits}, reward={self.average_reward:.3f})"


def determine_branch_type(state: ProofState) -> str:
    """Determine the branch type based on state constraints."""
    # Check alpha constraints
    for constraint in state.context.constraints:
        expr = constraint.expression.lower()

        if "alpha == 1/2" in expr or "alpha = 0.5" in expr:
            return "type_i"
        elif "1/2 < alpha < 3/5" in expr or "0.5 < alpha < 0.6" in expr:
            return "type_ii_gap"
        elif "alpha >= 3/5" in expr or "alpha > 0.6" in expr:
            return "type_ii_high"

    # Check which theorems are being worked on
    if state.lemma_status.get("type_ii_exclusion_gap") == LemmaStatus.IN_PROGRESS:
        return "type_ii_gap"
    elif state.lemma_status.get("swirl_decay") == LemmaStatus.IN_PROGRESS:
        return "swirl_extension"

    return "general"


class MCTSTree:
    """Container for the MCTS tree with utility methods."""

    def __init__(self, root: MCTSNode):
        self.root = root

    def get_all_nodes(self) -> List[MCTSNode]:
        """Get all nodes in the tree."""
        nodes = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            nodes.append(node)
            queue.extend(node.children.values())

        return nodes

    def get_leaves(self) -> List[MCTSNode]:
        """Get all leaf nodes."""
        return [n for n in self.get_all_nodes() if not n.children]

    def get_proven_paths(self) -> List[List[MCTSNode]]:
        """Get all paths that lead to proven states."""
        paths = []

        for leaf in self.get_leaves():
            if leaf.state.target_theorem.status == LemmaStatus.PROVEN:
                paths.append(leaf.get_path_from_root())

        return paths

    def get_best_path(self) -> List[MCTSNode]:
        """Get the path with highest cumulative reward."""
        best_path = [self.root]
        node = self.root

        while node.children:
            node = node.highest_reward_child()
            best_path.append(node)

        return best_path

    def get_most_visited_path(self) -> List[MCTSNode]:
        """Get the path following most visited children."""
        path = [self.root]
        node = self.root

        while node.children:
            node = node.most_visited_child()
            path.append(node)

        return path

    def statistics(self) -> Dict:
        """Compute tree statistics."""
        nodes = self.get_all_nodes()
        leaves = self.get_leaves()

        depths = [n.get_depth() for n in nodes]
        rewards = [n.average_reward for n in nodes if n.visits > 0]

        return {
            "total_nodes": len(nodes),
            "leaf_nodes": len(leaves),
            "max_depth": max(depths) if depths else 0,
            "avg_depth": np.mean(depths) if depths else 0,
            "max_reward": max(rewards) if rewards else 0,
            "avg_reward": np.mean(rewards) if rewards else 0,
            "proven_paths": len(self.get_proven_paths()),
            "root_visits": self.root.visits,
            "branch_distribution": self._branch_distribution()
        }

    def _branch_distribution(self) -> Dict[str, int]:
        """Count nodes by branch type."""
        distribution = {}
        for node in self.get_all_nodes():
            bt = node.branch_type or "unknown"
            distribution[bt] = distribution.get(bt, 0) + 1
        return distribution

    def prune_low_value_branches(self, threshold: float = 0.1):
        """Prune branches with low average reward."""
        self._prune_recursive(self.root, threshold)

    def _prune_recursive(self, node: MCTSNode, threshold: float):
        """Recursive pruning helper."""
        to_remove = []

        for action, child in node.children.items():
            if child.visits > 10 and child.average_reward < threshold:
                to_remove.append(action)
            else:
                self._prune_recursive(child, threshold)

        for action in to_remove:
            del node.children[action]

    def visualize(self, max_depth: int = 5) -> str:
        """Generate text visualization of tree."""
        lines = []
        self._visualize_recursive(self.root, "", lines, max_depth)
        return "\n".join(lines)

    def _visualize_recursive(self, node: MCTSNode, prefix: str,
                             lines: List[str], max_depth: int):
        """Recursive visualization helper."""
        if node.get_depth() > max_depth:
            return

        action_str = str(node.action.target) if node.action else "ROOT"
        status = "PROVEN" if node.state.target_theorem.status == LemmaStatus.PROVEN else ""
        line = f"{prefix}{action_str} (v={node.visits}, r={node.average_reward:.2f}) {status}"
        lines.append(line)

        children = list(node.children.values())
        for i, child in enumerate(children[:5]):  # Limit children shown
            new_prefix = prefix + ("    " if i == len(children) - 1 else "    ")
            self._visualize_recursive(child, new_prefix, lines, max_depth)

        if len(children) > 5:
            lines.append(f"{prefix}    ... ({len(children) - 5} more children)")

    def to_dot(self, max_depth: int = 10) -> str:
        """Export tree to DOT format for GraphViz."""
        lines = ["digraph MCTSTree {"]
        lines.append("  rankdir=TB;")

        self._to_dot_recursive(self.root, lines, max_depth, 0)

        lines.append("}")
        return "\n".join(lines)

    def _to_dot_recursive(self, node: MCTSNode, lines: List[str],
                          max_depth: int, node_id: int) -> int:
        """Recursive DOT export helper."""
        if node.get_depth() > max_depth:
            return node_id

        # Node label
        action_str = str(node.action.target)[:20] if node.action else "ROOT"
        color = "green" if node.state.target_theorem.status == LemmaStatus.PROVEN else "white"
        label = f"{action_str}\\nv={node.visits}, r={node.average_reward:.2f}"
        lines.append(f'  n{node_id} [label="{label}", style=filled, fillcolor={color}];')

        parent_id = node_id
        current_id = node_id

        for child in node.children.values():
            current_id += 1
            child_id = current_id
            lines.append(f'  n{parent_id} -> n{child_id};')
            current_id = self._to_dot_recursive(child, lines, max_depth, child_id)

        return current_id

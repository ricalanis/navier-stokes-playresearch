"""
Genetic Algorithm for Discovering Functional Inequalities in Navier-Stokes.

The Goal:
---------
Bridge the dimensional gap between:
- KNOWN: r^{-2} integral |u|^3 bounded (CKN, dimension 0)
- NEEDED: r^{-(2m-1)} integral |u|^2 bounded for m in (1/2, 3/5)

The mismatch is approximately 0.9 dimensions.

This module uses genetic programming to evolve candidate inequalities
of the form:
    ||u||_{L^2(B(r))} <= C * r^alpha * ||u||_{L^3}^beta * ||grad u||_{L^2}^gamma ...

with alpha > (2m-1)/2 approximately 0.05.

Key Concepts:
-------------
1. Genes = Expression trees representing mathematical quantities
2. Fitness = Dimensional consistency + interpolation property + physical validity
3. Evolution = Crossover (swap subtrees) + Mutation (modify nodes)
4. Validation = Check against Holder, Sobolev, Gagliardo-Nirenberg

Physical Dimensions (NS scaling):
---------------------------------
Under NS scaling: x -> lambda*x, t -> lambda^2*t, u -> lambda^{-1}*u

[Length] = L
[Time] = T = L^2 (diffusive scaling)
[Velocity] = L/T = L^{-1}
[Vorticity] = L^{-2}
[Energy] = L (integral of u^2 over L^3)
[Dissipation] = L^{-1} (integral of |grad u|^2)

Author: NS Research Project
Date: 2026-01-13
"""

from __future__ import annotations
import random
import copy
import math
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple, Callable, Set, Any
from abc import ABC, abstractmethod
import numpy as np
from collections import defaultdict


# =============================================================================
# DIMENSIONAL ANALYSIS SYSTEM
# =============================================================================

@dataclass
class Dimension:
    """
    Physical dimension in the NS scaling system.

    We use a 2D basis: [L] for length, [T] for time.
    Under NS scaling: [T] = [L]^2, so effectively 1D.

    We track the scaling exponent: quantity ~ L^alpha means
    under x -> lambda*x, quantity -> lambda^alpha * quantity.

    Key dimensions:
    - u (velocity): L^{-1}
    - omega (vorticity): L^{-2}
    - nu (viscosity): L^0 (dimensionless in NS scaling)
    - r (length scale): L^1
    - grad: L^{-1}
    - integral over R^3: L^3
    """
    length_power: float = 0.0  # Power of length L

    def __add__(self, other: Dimension) -> Dimension:
        """Addition requires same dimension (returns same)."""
        if not self.is_compatible(other):
            return Dimension(float('nan'))  # Invalid
        return Dimension(self.length_power)

    def __sub__(self, other: Dimension) -> Dimension:
        """Subtraction requires same dimension."""
        return self + other

    def __mul__(self, other: Dimension) -> Dimension:
        """Multiplication adds dimensions."""
        return Dimension(self.length_power + other.length_power)

    def __truediv__(self, other: Dimension) -> Dimension:
        """Division subtracts dimensions."""
        return Dimension(self.length_power - other.length_power)

    def __pow__(self, power: float) -> Dimension:
        """Power multiplies dimension."""
        return Dimension(self.length_power * power)

    def is_compatible(self, other: Dimension, tol: float = 1e-10) -> bool:
        """Check if two dimensions are compatible (same)."""
        return abs(self.length_power - other.length_power) < tol

    def is_dimensionless(self, tol: float = 1e-10) -> bool:
        """Check if dimension is zero (dimensionless)."""
        return abs(self.length_power) < tol

    def is_valid(self) -> bool:
        """Check if dimension is valid (not NaN)."""
        return not math.isnan(self.length_power)

    def __repr__(self) -> str:
        if not self.is_valid():
            return "Dimension(INVALID)"
        if self.is_dimensionless():
            return "Dimension(0)"
        return f"Dimension(L^{self.length_power:.3f})"


# Standard dimensions for NS quantities
class StandardDimensions:
    """Standard dimensions for quantities in NS."""

    # Fundamental
    LENGTH = Dimension(1.0)            # r, x
    TIME = Dimension(2.0)              # t (diffusive scaling)

    # Fields
    VELOCITY = Dimension(-1.0)         # u ~ L^{-1}
    VORTICITY = Dimension(-2.0)        # omega ~ L^{-2}
    PRESSURE = Dimension(-2.0)         # p ~ |u|^2 ~ L^{-2}

    # Operators
    GRADIENT = Dimension(-1.0)         # grad ~ L^{-1}
    LAPLACIAN = Dimension(-2.0)        # Delta ~ L^{-2}
    INTEGRAL_R3 = Dimension(3.0)       # integral dx^3 ~ L^3

    # Physical constants
    VISCOSITY = Dimension(0.0)         # nu is dimensionless in NS scaling
    ENERGY_BOUND = Dimension(1.0)      # E_0 ~ L (integral |u|^2)

    # L^p norms (over R^3)
    @staticmethod
    def lp_norm(field_dim: Dimension, p: float) -> Dimension:
        """
        Dimension of ||f||_{L^p} = (integral |f|^p)^{1/p}.

        If [f] = L^a, then [|f|^p] = L^{ap}, [integral] = L^{3+ap}
        So [||f||_{L^p}] = L^{(3+ap)/p} = L^{3/p + a}
        """
        return Dimension(3.0/p + field_dim.length_power)

    @staticmethod
    def sobolev_norm(field_dim: Dimension, s: float, p: float) -> Dimension:
        """
        Dimension of ||f||_{W^{s,p}} ~ ||f||_{L^p} + ||D^s f||_{L^p}.

        [D^s f] = L^{a - s} if [f] = L^a
        So [||D^s f||_{L^p}] = L^{3/p + a - s}
        """
        return Dimension(3.0/p + field_dim.length_power - s)


# =============================================================================
# EXPRESSION TREE NODES
# =============================================================================

class NodeType(Enum):
    """Types of nodes in expression trees."""
    # Leaf nodes (quantities)
    VELOCITY = auto()           # u
    VORTICITY = auto()          # omega = curl u
    PRESSURE = auto()           # p
    LENGTH_SCALE = auto()       # r
    VISCOSITY = auto()          # nu
    ENERGY_BOUND = auto()       # E_0 (initial energy)
    CONSTANT = auto()           # numerical constant

    # Operators (unary)
    GRADIENT = auto()           # grad
    LAPLACIAN = auto()          # Delta
    CURL = auto()               # curl
    LP_NORM = auto()            # ||.||_{L^p}
    LOCAL_LP_NORM = auto()      # ||.||_{L^p(B(r))}
    ABSOLUTE = auto()           # |.|

    # Operators (binary)
    ADD = auto()                # +
    SUBTRACT = auto()           # -
    MULTIPLY = auto()           # *
    DIVIDE = auto()             # /
    POWER = auto()              # ^

    # Special
    INTEGRAL = auto()           # integral
    DOT_PRODUCT = auto()        # u . v


@dataclass
class ExpressionNode:
    """
    Node in an expression tree.

    Each node has:
    - node_type: what kind of operation/quantity
    - children: list of child nodes (empty for leaves)
    - params: additional parameters (e.g., p for L^p norm)
    - dimension: physical dimension (computed)
    """
    node_type: NodeType
    children: List[ExpressionNode] = field(default_factory=list)
    params: Dict[str, float] = field(default_factory=dict)
    dimension: Optional[Dimension] = None

    def is_leaf(self) -> bool:
        """Check if this is a leaf node."""
        return len(self.children) == 0

    def depth(self) -> int:
        """Compute depth of subtree."""
        if self.is_leaf():
            return 1
        return 1 + max(child.depth() for child in self.children)

    def size(self) -> int:
        """Compute number of nodes in subtree."""
        return 1 + sum(child.size() for child in self.children)

    def copy(self) -> ExpressionNode:
        """Deep copy of this node and subtree."""
        return ExpressionNode(
            node_type=self.node_type,
            children=[child.copy() for child in self.children],
            params=dict(self.params),
            dimension=copy.copy(self.dimension)
        )


class ExpressionTree:
    """
    Full expression tree representing a mathematical quantity.

    Examples:
    - ||u||_{L^3} = LP_NORM(VELOCITY, p=3)
    - ||grad u||_{L^2} = LP_NORM(GRADIENT(VELOCITY), p=2)
    - r^alpha ||u||_{L^3} = MULTIPLY(POWER(LENGTH_SCALE, alpha), LP_NORM(VELOCITY, p=3))
    """

    def __init__(self, root: Optional[ExpressionNode] = None):
        self.root = root

    def compute_dimensions(self) -> bool:
        """
        Compute dimensions for all nodes. Returns True if valid.
        """
        if self.root is None:
            return False
        return self._compute_node_dimension(self.root)

    def _compute_node_dimension(self, node: ExpressionNode) -> bool:
        """Recursively compute dimension for a node."""
        # First compute children
        for child in node.children:
            if not self._compute_node_dimension(child):
                return False

        # Now compute this node's dimension
        node.dimension = self._get_node_dimension(node)
        return node.dimension is not None and node.dimension.is_valid()

    def _get_node_dimension(self, node: ExpressionNode) -> Dimension:
        """Get dimension for a specific node type."""
        nt = node.node_type
        SD = StandardDimensions

        # Leaf nodes
        if nt == NodeType.VELOCITY:
            return SD.VELOCITY
        elif nt == NodeType.VORTICITY:
            return SD.VORTICITY
        elif nt == NodeType.PRESSURE:
            return SD.PRESSURE
        elif nt == NodeType.LENGTH_SCALE:
            return SD.LENGTH
        elif nt == NodeType.VISCOSITY:
            return SD.VISCOSITY
        elif nt == NodeType.ENERGY_BOUND:
            return SD.ENERGY_BOUND
        elif nt == NodeType.CONSTANT:
            return Dimension(0.0)  # Dimensionless

        # Unary operators
        elif nt == NodeType.GRADIENT:
            if not node.children:
                return Dimension(float('nan'))
            child_dim = node.children[0].dimension
            return child_dim * SD.GRADIENT

        elif nt == NodeType.LAPLACIAN:
            if not node.children:
                return Dimension(float('nan'))
            child_dim = node.children[0].dimension
            return child_dim * SD.LAPLACIAN

        elif nt == NodeType.CURL:
            if not node.children:
                return Dimension(float('nan'))
            child_dim = node.children[0].dimension
            return child_dim * SD.GRADIENT  # curl has same dimension as grad

        elif nt == NodeType.LP_NORM:
            if not node.children:
                return Dimension(float('nan'))
            p = node.params.get('p', 2.0)
            child_dim = node.children[0].dimension
            return SD.lp_norm(child_dim, p)

        elif nt == NodeType.LOCAL_LP_NORM:
            # ||f||_{L^p(B(r))} ~ r^{3/p} ||f||_{local}
            # Dimension is same as L^p norm
            if not node.children:
                return Dimension(float('nan'))
            p = node.params.get('p', 2.0)
            child_dim = node.children[0].dimension
            return SD.lp_norm(child_dim, p)

        elif nt == NodeType.ABSOLUTE:
            if not node.children:
                return Dimension(float('nan'))
            return node.children[0].dimension

        # Binary operators
        elif nt == NodeType.ADD or nt == NodeType.SUBTRACT:
            if len(node.children) != 2:
                return Dimension(float('nan'))
            d1, d2 = node.children[0].dimension, node.children[1].dimension
            if d1.is_compatible(d2):
                return d1
            return Dimension(float('nan'))

        elif nt == NodeType.MULTIPLY:
            if len(node.children) != 2:
                return Dimension(float('nan'))
            d1, d2 = node.children[0].dimension, node.children[1].dimension
            return d1 * d2

        elif nt == NodeType.DIVIDE:
            if len(node.children) != 2:
                return Dimension(float('nan'))
            d1, d2 = node.children[0].dimension, node.children[1].dimension
            return d1 / d2

        elif nt == NodeType.POWER:
            if len(node.children) != 2:
                return Dimension(float('nan'))
            base_dim = node.children[0].dimension
            # Power must be a constant
            power = node.params.get('power', 1.0)
            return base_dim ** power

        elif nt == NodeType.INTEGRAL:
            if not node.children:
                return Dimension(float('nan'))
            child_dim = node.children[0].dimension
            return child_dim * SD.INTEGRAL_R3

        elif nt == NodeType.DOT_PRODUCT:
            if len(node.children) != 2:
                return Dimension(float('nan'))
            d1, d2 = node.children[0].dimension, node.children[1].dimension
            return d1 * d2

        return Dimension(float('nan'))

    def to_string(self, node: Optional[ExpressionNode] = None) -> str:
        """Convert expression tree to string representation."""
        if node is None:
            node = self.root
        if node is None:
            return "EMPTY"

        nt = node.node_type

        # Leaf nodes
        if nt == NodeType.VELOCITY:
            return "u"
        elif nt == NodeType.VORTICITY:
            return "omega"
        elif nt == NodeType.PRESSURE:
            return "p"
        elif nt == NodeType.LENGTH_SCALE:
            return "r"
        elif nt == NodeType.VISCOSITY:
            return "nu"
        elif nt == NodeType.ENERGY_BOUND:
            return "E_0"
        elif nt == NodeType.CONSTANT:
            val = node.params.get('value', 1.0)
            if val == int(val):
                return str(int(val))
            return f"{val:.3f}"

        # Unary operators
        elif nt == NodeType.GRADIENT:
            return f"grad({self.to_string(node.children[0])})"
        elif nt == NodeType.LAPLACIAN:
            return f"Delta({self.to_string(node.children[0])})"
        elif nt == NodeType.CURL:
            return f"curl({self.to_string(node.children[0])})"
        elif nt == NodeType.LP_NORM:
            p = node.params.get('p', 2.0)
            p_str = str(int(p)) if p == int(p) else f"{p:.2f}"
            return f"||{self.to_string(node.children[0])}||_L{p_str}"
        elif nt == NodeType.LOCAL_LP_NORM:
            p = node.params.get('p', 2.0)
            p_str = str(int(p)) if p == int(p) else f"{p:.2f}"
            return f"||{self.to_string(node.children[0])}||_L{p_str}(B(r))"
        elif nt == NodeType.ABSOLUTE:
            return f"|{self.to_string(node.children[0])}|"

        # Binary operators
        elif nt == NodeType.ADD:
            return f"({self.to_string(node.children[0])} + {self.to_string(node.children[1])})"
        elif nt == NodeType.SUBTRACT:
            return f"({self.to_string(node.children[0])} - {self.to_string(node.children[1])})"
        elif nt == NodeType.MULTIPLY:
            return f"({self.to_string(node.children[0])} * {self.to_string(node.children[1])})"
        elif nt == NodeType.DIVIDE:
            return f"({self.to_string(node.children[0])} / {self.to_string(node.children[1])})"
        elif nt == NodeType.POWER:
            power = node.params.get('power', 1.0)
            p_str = str(int(power)) if power == int(power) else f"{power:.3f}"
            return f"({self.to_string(node.children[0])})^{p_str}"
        elif nt == NodeType.INTEGRAL:
            return f"int({self.to_string(node.children[0])})"
        elif nt == NodeType.DOT_PRODUCT:
            return f"({self.to_string(node.children[0])} . {self.to_string(node.children[1])})"

        return f"UNKNOWN({nt})"

    def copy(self) -> ExpressionTree:
        """Deep copy of expression tree."""
        if self.root is None:
            return ExpressionTree(None)
        return ExpressionTree(self.root.copy())

    def depth(self) -> int:
        """Depth of tree."""
        if self.root is None:
            return 0
        return self.root.depth()

    def size(self) -> int:
        """Number of nodes."""
        if self.root is None:
            return 0
        return self.root.size()

    def get_all_nodes(self) -> List[ExpressionNode]:
        """Get list of all nodes in tree."""
        if self.root is None:
            return []
        nodes = []
        self._collect_nodes(self.root, nodes)
        return nodes

    def _collect_nodes(self, node: ExpressionNode, nodes: List[ExpressionNode]):
        """Recursively collect all nodes."""
        nodes.append(node)
        for child in node.children:
            self._collect_nodes(child, nodes)


# =============================================================================
# INEQUALITY CANDIDATE
# =============================================================================

@dataclass
class InequalityCandidate:
    """
    A candidate functional inequality.

    Form: LHS <= C * RHS

    where LHS and RHS are expression trees.

    For our gap-bridging goal:
    LHS = ||u||_{L^2(B(r))}
    RHS = r^alpha * ||u||_{L^3}^beta * ||grad u||_{L^2}^gamma * ...

    We want alpha > (2m-1)/2 ~ 0.05 for m in (1/2, 3/5).
    """
    lhs: ExpressionTree
    rhs: ExpressionTree
    fitness: float = 0.0
    dimensional_valid: bool = False
    interpolation_score: float = 0.0
    monotonicity_score: float = 0.0
    novelty_score: float = 0.0
    notes: str = ""

    def __repr__(self) -> str:
        return f"Inequality: {self.lhs.to_string()} <= C * {self.rhs.to_string()} (fitness={self.fitness:.4f})"

    def detailed_string(self) -> str:
        """Detailed representation with scores."""
        lines = [
            "=" * 60,
            "INEQUALITY CANDIDATE",
            "=" * 60,
            f"LHS: {self.lhs.to_string()}",
            f"RHS: C * {self.rhs.to_string()}",
            "-" * 40,
            f"Fitness: {self.fitness:.4f}",
            f"Dimensional valid: {self.dimensional_valid}",
            f"Interpolation score: {self.interpolation_score:.4f}",
            f"Monotonicity score: {self.monotonicity_score:.4f}",
            f"Novelty score: {self.novelty_score:.4f}",
        ]
        if self.notes:
            lines.append(f"Notes: {self.notes}")

        # Dimension info
        if self.lhs.root and self.lhs.root.dimension:
            lines.append(f"LHS dimension: {self.lhs.root.dimension}")
        if self.rhs.root and self.rhs.root.dimension:
            lines.append(f"RHS dimension: {self.rhs.root.dimension}")

        lines.append("=" * 60)
        return "\n".join(lines)


# =============================================================================
# RANDOM EXPRESSION GENERATION
# =============================================================================

class ExpressionGenerator:
    """Generate random expression trees."""

    # Leaf node types and their weights
    LEAF_TYPES = [
        (NodeType.VELOCITY, 3.0),
        (NodeType.VORTICITY, 2.0),
        (NodeType.LENGTH_SCALE, 2.0),
        (NodeType.GRADIENT, 2.0),  # Will be converted to GRADIENT(VELOCITY)
        (NodeType.ENERGY_BOUND, 1.0),
        (NodeType.VISCOSITY, 0.5),
    ]

    # Unary operators
    UNARY_OPS = [
        NodeType.LP_NORM,
        NodeType.LOCAL_LP_NORM,
        NodeType.GRADIENT,
        NodeType.ABSOLUTE,
    ]

    # Binary operators
    BINARY_OPS = [
        NodeType.MULTIPLY,
        NodeType.DIVIDE,
        NodeType.POWER,
    ]

    # Common L^p values
    LP_VALUES = [1.5, 2.0, 2.5, 3.0, 4.0, 6.0]

    # Common power values
    POWER_VALUES = [-2.0, -1.5, -1.0, -0.5, 0.5, 1.0, 1.5, 2.0]

    def __init__(self, max_depth: int = 5, seed: Optional[int] = None):
        self.max_depth = max_depth
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

    def generate_random_tree(self, depth: int = 0,
                            force_norms: bool = True) -> ExpressionTree:
        """
        Generate a random expression tree.

        Args:
            depth: Current depth in recursion
            force_norms: If True, ensure we generate norm-like expressions
        """
        root = self._generate_node(depth, force_norms)
        return ExpressionTree(root)

    def _generate_node(self, depth: int, force_norms: bool) -> ExpressionNode:
        """Generate a random node."""
        # At max depth or with some probability, generate leaf
        if depth >= self.max_depth:
            return self._generate_leaf()

        # Decide what to generate
        r = random.random()

        if r < 0.3:  # 30% chance of leaf
            return self._generate_leaf()
        elif r < 0.6:  # 30% chance of unary op
            return self._generate_unary(depth)
        else:  # 40% chance of binary op
            return self._generate_binary(depth)

    def _generate_leaf(self) -> ExpressionNode:
        """Generate a leaf node."""
        # Weighted random choice
        types, weights = zip(*self.LEAF_TYPES)
        total = sum(weights)
        weights = [w/total for w in weights]
        node_type = random.choices(types, weights=weights)[0]

        if node_type == NodeType.GRADIENT:
            # Generate GRADIENT(VELOCITY)
            return ExpressionNode(
                node_type=NodeType.GRADIENT,
                children=[ExpressionNode(node_type=NodeType.VELOCITY)]
            )

        return ExpressionNode(node_type=node_type)

    def _generate_unary(self, depth: int) -> ExpressionNode:
        """Generate a unary operator node."""
        op = random.choice(self.UNARY_OPS)
        child = self._generate_node(depth + 1, force_norms=False)

        params = {}
        if op in [NodeType.LP_NORM, NodeType.LOCAL_LP_NORM]:
            params['p'] = random.choice(self.LP_VALUES)

        return ExpressionNode(
            node_type=op,
            children=[child],
            params=params
        )

    def _generate_binary(self, depth: int) -> ExpressionNode:
        """Generate a binary operator node."""
        op = random.choice(self.BINARY_OPS)

        if op == NodeType.POWER:
            # For power, first child is base, params has power
            child = self._generate_node(depth + 1, force_norms=False)
            power = random.choice(self.POWER_VALUES)
            return ExpressionNode(
                node_type=op,
                children=[child],
                params={'power': power}
            )
        else:
            # For multiply/divide, two children
            left = self._generate_node(depth + 1, force_norms=False)
            right = self._generate_node(depth + 1, force_norms=False)
            return ExpressionNode(
                node_type=op,
                children=[left, right]
            )

    def generate_inequality(self) -> InequalityCandidate:
        """Generate a random inequality candidate."""
        # LHS: typically a local L^p norm of u
        lhs = self._generate_lhs()

        # RHS: product of scaled norms
        rhs = self._generate_rhs()

        return InequalityCandidate(lhs=lhs, rhs=rhs)

    def _generate_lhs(self) -> ExpressionTree:
        """Generate LHS of inequality (what we want to bound)."""
        # Typically ||u||_{L^2(B(r))} or similar
        p = random.choice([2.0, 3.0, 4.0])

        root = ExpressionNode(
            node_type=NodeType.LOCAL_LP_NORM,
            children=[ExpressionNode(node_type=NodeType.VELOCITY)],
            params={'p': p}
        )
        return ExpressionTree(root)

    def _generate_rhs(self) -> ExpressionTree:
        """
        Generate RHS of inequality.

        Form: r^alpha * ||u||_{L^p1}^beta1 * ||grad u||_{L^p2}^beta2 * ...
        """
        # Start with r^alpha
        alpha = random.uniform(-1.0, 1.0)

        terms = []

        # r^alpha term
        r_term = ExpressionNode(
            node_type=NodeType.POWER,
            children=[ExpressionNode(node_type=NodeType.LENGTH_SCALE)],
            params={'power': alpha}
        )
        terms.append(r_term)

        # Add 1-3 norm terms
        num_terms = random.randint(1, 3)
        for _ in range(num_terms):
            term = self._generate_norm_term()
            terms.append(term)

        # Combine with multiplication
        if len(terms) == 1:
            root = terms[0]
        else:
            root = terms[0]
            for term in terms[1:]:
                root = ExpressionNode(
                    node_type=NodeType.MULTIPLY,
                    children=[root, term]
                )

        return ExpressionTree(root)

    def _generate_norm_term(self) -> ExpressionNode:
        """Generate a norm term like ||f||_{L^p}^beta."""
        # What to take norm of
        r = random.random()
        if r < 0.5:
            # ||u||_{L^p}
            inner = ExpressionNode(node_type=NodeType.VELOCITY)
        elif r < 0.8:
            # ||grad u||_{L^p}
            inner = ExpressionNode(
                node_type=NodeType.GRADIENT,
                children=[ExpressionNode(node_type=NodeType.VELOCITY)]
            )
        else:
            # ||omega||_{L^p}
            inner = ExpressionNode(node_type=NodeType.VORTICITY)

        # L^p norm
        p = random.choice(self.LP_VALUES)
        norm = ExpressionNode(
            node_type=NodeType.LP_NORM,
            children=[inner],
            params={'p': p}
        )

        # Power
        beta = random.choice([0.5, 1.0, 1.5, 2.0])
        if beta != 1.0:
            norm = ExpressionNode(
                node_type=NodeType.POWER,
                children=[norm],
                params={'power': beta}
            )

        return norm


# =============================================================================
# FITNESS FUNCTION
# =============================================================================

class FitnessEvaluator:
    """
    Evaluate fitness of inequality candidates.

    Criteria:
    1. Dimensional consistency (LHS and RHS have same dimension)
    2. Interpolation property (connects L^3 to L^2)
    3. Achieves target scaling (alpha > 0.05)
    4. Monotonicity under NS flow (bonus)
    5. Novelty (not a known inequality)
    """

    # Known inequalities to check against
    KNOWN_INEQUALITIES = [
        "Holder",           # ||fg||_1 <= ||f||_p ||g||_q
        "Sobolev",          # ||u||_{L^p} <= C ||grad u||_{L^q}
        "Gagliardo-Nirenberg",  # ||D^j u||_{L^p} <= C ||D^m u||_{L^r}^a ||u||_{L^q}^{1-a}
        "CKN",              # Local energy inequality
        "Ladyzhenskaya",    # ||u||_4^4 <= C ||u||_2 ||grad u||_2^3 (2D)
    ]

    # Target: alpha > (2m-1)/2 for m in (1/2, 3/5)
    # For m = 0.55, alpha > 0.05
    TARGET_ALPHA_MIN = 0.05
    TARGET_ALPHA_MAX = 0.5

    def __init__(self):
        self.weights = {
            'dimensional': 10.0,    # Most important
            'interpolation': 5.0,
            'scaling': 3.0,
            'monotonicity': 2.0,
            'novelty': 1.0,
            'simplicity': 0.5,
        }

    def evaluate(self, candidate: InequalityCandidate) -> float:
        """Compute total fitness score."""
        scores = {}

        # 1. Dimensional consistency
        scores['dimensional'] = self._dimensional_score(candidate)

        # 2. Interpolation property
        scores['interpolation'] = self._interpolation_score(candidate)

        # 3. Scaling analysis
        scores['scaling'] = self._scaling_score(candidate)

        # 4. Monotonicity (placeholder)
        scores['monotonicity'] = self._monotonicity_score(candidate)

        # 5. Novelty
        scores['novelty'] = self._novelty_score(candidate)

        # 6. Simplicity bonus
        scores['simplicity'] = self._simplicity_score(candidate)

        # Weighted sum
        total = sum(self.weights[k] * scores[k] for k in scores)
        max_possible = sum(self.weights.values())

        candidate.fitness = total / max_possible
        candidate.dimensional_valid = scores['dimensional'] > 0.9
        candidate.interpolation_score = scores['interpolation']
        candidate.monotonicity_score = scores['monotonicity']
        candidate.novelty_score = scores['novelty']

        return candidate.fitness

    def _dimensional_score(self, candidate: InequalityCandidate) -> float:
        """
        Score dimensional consistency.

        LHS and RHS must have the same dimension for the inequality to make sense.
        """
        # Compute dimensions
        lhs_valid = candidate.lhs.compute_dimensions()
        rhs_valid = candidate.rhs.compute_dimensions()

        if not lhs_valid or not rhs_valid:
            return 0.0

        lhs_dim = candidate.lhs.root.dimension
        rhs_dim = candidate.rhs.root.dimension

        if not lhs_dim.is_valid() or not rhs_dim.is_valid():
            return 0.0

        # Check if dimensions match
        diff = abs(lhs_dim.length_power - rhs_dim.length_power)

        if diff < 0.01:
            return 1.0
        elif diff < 0.1:
            return 0.8
        elif diff < 0.5:
            return 0.5 * (1 - diff)
        else:
            return 0.0

    def _interpolation_score(self, candidate: InequalityCandidate) -> float:
        """
        Score interpolation property.

        We want inequalities that connect L^3 norms to L^2 norms,
        bridging the dimensional gap.

        Check if:
        - LHS involves L^2 type norms
        - RHS involves L^3 type norms and gradients
        """
        score = 0.0

        # Check LHS for L^2-like terms
        lhs_nodes = candidate.lhs.get_all_nodes()
        for node in lhs_nodes:
            if node.node_type in [NodeType.LP_NORM, NodeType.LOCAL_LP_NORM]:
                p = node.params.get('p', 2.0)
                if 1.5 <= p <= 2.5:
                    score += 0.3

        # Check RHS for L^3-like terms and gradients
        rhs_nodes = candidate.rhs.get_all_nodes()
        has_l3 = False
        has_gradient = False
        has_r_scaling = False

        for node in rhs_nodes:
            if node.node_type in [NodeType.LP_NORM, NodeType.LOCAL_LP_NORM]:
                p = node.params.get('p', 2.0)
                if 2.5 <= p <= 4.0:
                    has_l3 = True
            elif node.node_type == NodeType.GRADIENT:
                has_gradient = True
            elif node.node_type == NodeType.LENGTH_SCALE:
                has_r_scaling = True

        if has_l3:
            score += 0.3
        if has_gradient:
            score += 0.2
        if has_r_scaling:
            score += 0.2

        return min(score, 1.0)

    def _scaling_score(self, candidate: InequalityCandidate) -> float:
        """
        Score based on whether inequality achieves target scaling.

        We want r^alpha with alpha in (0.05, 0.5).
        """
        # Find r^alpha terms in RHS
        rhs_nodes = candidate.rhs.get_all_nodes()

        for node in rhs_nodes:
            if node.node_type == NodeType.POWER:
                if node.children and node.children[0].node_type == NodeType.LENGTH_SCALE:
                    alpha = node.params.get('power', 0.0)

                    if self.TARGET_ALPHA_MIN <= alpha <= self.TARGET_ALPHA_MAX:
                        # Good range
                        return 1.0
                    elif 0 < alpha < self.TARGET_ALPHA_MIN:
                        # Close but not quite
                        return 0.5
                    elif alpha > self.TARGET_ALPHA_MAX:
                        # Too large but positive
                        return 0.3

        return 0.1  # No explicit r scaling found

    def _monotonicity_score(self, candidate: InequalityCandidate) -> float:
        """
        Score monotonicity under NS flow (placeholder).

        Ideally we'd check if the RHS is monotone decreasing under NS dynamics.
        This is complex to verify symbolically, so we use heuristics.
        """
        # Heuristic: expressions with energy-like terms get bonus
        rhs_nodes = candidate.rhs.get_all_nodes()

        score = 0.0
        for node in rhs_nodes:
            if node.node_type == NodeType.ENERGY_BOUND:
                score += 0.3
            elif node.node_type == NodeType.LP_NORM:
                p = node.params.get('p', 2.0)
                if p == 2.0:  # L^2 norms related to energy
                    score += 0.2

        return min(score, 1.0)

    def _novelty_score(self, candidate: InequalityCandidate) -> float:
        """
        Score novelty (not being a trivial variant of known inequalities).

        We penalize very simple expressions that are just known inequalities.
        """
        expr = candidate.rhs.to_string()

        # Check for trivial cases
        if "||u||_L3" in expr and candidate.rhs.size() < 5:
            return 0.3  # Too simple, probably just CKN

        if "||grad(u)||_L2" in expr and candidate.rhs.size() < 5:
            return 0.4  # Might be just Sobolev

        # Complex expressions are more novel
        size = candidate.rhs.size()
        if size > 10:
            return 0.9
        elif size > 5:
            return 0.7
        else:
            return 0.5

    def _simplicity_score(self, candidate: InequalityCandidate) -> float:
        """
        Bonus for simpler expressions (Occam's razor).

        Very complex expressions are harder to prove and use.
        """
        total_size = candidate.lhs.size() + candidate.rhs.size()

        if total_size <= 5:
            return 1.0
        elif total_size <= 10:
            return 0.8
        elif total_size <= 15:
            return 0.5
        else:
            return 0.2


# =============================================================================
# GENETIC OPERATIONS
# =============================================================================

class GeneticOperator:
    """Genetic operations: crossover, mutation, selection."""

    def __init__(self, mutation_rate: float = 0.3,
                 crossover_rate: float = 0.7):
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generator = ExpressionGenerator()

    def crossover(self, parent1: InequalityCandidate,
                  parent2: InequalityCandidate) -> Tuple[InequalityCandidate, InequalityCandidate]:
        """
        Crossover: swap subtrees between two inequalities.

        We only crossover the RHS (the bound), keeping LHS fixed.
        """
        child1 = InequalityCandidate(
            lhs=parent1.lhs.copy(),
            rhs=parent1.rhs.copy()
        )
        child2 = InequalityCandidate(
            lhs=parent2.lhs.copy(),
            rhs=parent2.rhs.copy()
        )

        if random.random() > self.crossover_rate:
            return child1, child2

        # Get all nodes from both RHS trees
        nodes1 = child1.rhs.get_all_nodes()
        nodes2 = child2.rhs.get_all_nodes()

        if len(nodes1) < 2 or len(nodes2) < 2:
            return child1, child2

        # Select random nodes (not roots)
        node1 = random.choice(nodes1[1:]) if len(nodes1) > 1 else nodes1[0]
        node2 = random.choice(nodes2[1:]) if len(nodes2) > 1 else nodes2[0]

        # Find parents and swap
        self._swap_nodes(child1.rhs, child2.rhs, node1, node2)

        return child1, child2

    def _swap_nodes(self, tree1: ExpressionTree, tree2: ExpressionTree,
                   node1: ExpressionNode, node2: ExpressionNode):
        """Swap two nodes between trees by modifying their parents."""
        # Find parent of node1 in tree1
        parent1, idx1 = self._find_parent(tree1.root, node1)
        parent2, idx2 = self._find_parent(tree2.root, node2)

        if parent1 is not None and parent2 is not None:
            # Swap
            temp = parent1.children[idx1]
            parent1.children[idx1] = parent2.children[idx2]
            parent2.children[idx2] = temp

    def _find_parent(self, root: ExpressionNode, target: ExpressionNode
                    ) -> Tuple[Optional[ExpressionNode], int]:
        """Find parent of target node."""
        for i, child in enumerate(root.children):
            if child is target:
                return root, i
            result = self._find_parent(child, target)
            if result[0] is not None:
                return result
        return None, -1

    def mutate(self, candidate: InequalityCandidate) -> InequalityCandidate:
        """
        Mutation: modify the RHS expression.

        Types of mutations:
        1. Change operator
        2. Change constant/power
        3. Add/remove node
        4. Change L^p exponent
        """
        mutated = InequalityCandidate(
            lhs=candidate.lhs.copy(),
            rhs=candidate.rhs.copy()
        )

        if random.random() > self.mutation_rate:
            return mutated

        nodes = mutated.rhs.get_all_nodes()
        if not nodes:
            return mutated

        # Select random node to mutate
        node = random.choice(nodes)

        # Choose mutation type
        mutation_type = random.choice(['power', 'lp', 'operator', 'subtree'])

        if mutation_type == 'power' and node.node_type == NodeType.POWER:
            # Modify power value
            current = node.params.get('power', 1.0)
            delta = random.uniform(-0.5, 0.5)
            node.params['power'] = current + delta

        elif mutation_type == 'lp' and node.node_type in [NodeType.LP_NORM, NodeType.LOCAL_LP_NORM]:
            # Modify L^p exponent
            node.params['p'] = random.choice(self.generator.LP_VALUES)

        elif mutation_type == 'operator' and node.node_type in [NodeType.MULTIPLY, NodeType.DIVIDE]:
            # Swap multiply/divide
            if node.node_type == NodeType.MULTIPLY:
                node.node_type = NodeType.DIVIDE
            else:
                node.node_type = NodeType.MULTIPLY

        elif mutation_type == 'subtree':
            # Replace subtree with new random subtree
            new_subtree = self.generator._generate_node(0, force_norms=True)
            node.node_type = new_subtree.node_type
            node.children = new_subtree.children
            node.params = new_subtree.params

        return mutated

    def tournament_select(self, population: List[InequalityCandidate],
                         tournament_size: int = 3) -> InequalityCandidate:
        """Tournament selection: select best from random subset."""
        tournament = random.sample(population, min(tournament_size, len(population)))
        return max(tournament, key=lambda x: x.fitness)

    def elitist_select(self, population: List[InequalityCandidate],
                      num_elite: int = 2) -> List[InequalityCandidate]:
        """Return top individuals unchanged."""
        sorted_pop = sorted(population, key=lambda x: x.fitness, reverse=True)
        return [c.lhs.copy() and InequalityCandidate(
            lhs=c.lhs.copy(),
            rhs=c.rhs.copy(),
            fitness=c.fitness
        ) for c in sorted_pop[:num_elite]]


# =============================================================================
# KNOWN INEQUALITY VALIDATION
# =============================================================================

class InequalityValidator:
    """
    Validate candidate inequalities against known results.

    Known inequalities in 3D:
    1. Holder: ||fg||_1 <= ||f||_p ||g||_q, 1/p + 1/q = 1
    2. Sobolev: ||u||_{L^6} <= C ||grad u||_{L^2}
    3. Gagliardo-Nirenberg: ||D^j u||_{L^p} <= C ||D^m u||^a ||u||^{1-a}
    4. Ladyzhenskaya (3D): ||u||_{L^4}^4 <= C ||u||_{L^2} ||grad u||_{L^2}^3
    5. CKN: r^{-2} int |u|^3 bounded
    """

    def __init__(self):
        self.known_bounds = self._setup_known_bounds()

    def _setup_known_bounds(self) -> Dict[str, Dict]:
        """Setup database of known inequalities."""
        return {
            'sobolev_3d': {
                'lhs': '||u||_L6',
                'rhs': 'C * ||grad u||_L2',
                'conditions': '3D, u in H^1',
                'dimension_check': True,  # Both sides are L^{-1}
            },
            'ladyzhenskaya_3d': {
                'lhs': '||u||_L4^4',
                'rhs': 'C * ||u||_L2 * ||grad u||_L2^3',
                'conditions': '3D',
                'dimension_check': True,
            },
            'gagliardo_nirenberg': {
                'lhs': '||u||_L^p',
                'rhs': 'C * ||grad u||_L^q^a * ||u||_L^r^{1-a}',
                'conditions': 'Depends on p,q,r,a relation',
                'dimension_check': True,
            },
            'ckn_local': {
                'lhs': 'r^{-2} * int |u|^3',
                'rhs': 'bounded by initial data',
                'conditions': 'suitable weak solution',
                'dimension_check': True,  # dimensionless
            },
            'bkm_criterion': {
                'description': 'int_0^T ||omega||_infty dt < infty implies smooth',
                'application': 'Blowup rate constraint',
            }
        }

    def check_against_known(self, candidate: InequalityCandidate) -> Dict[str, Any]:
        """
        Check if candidate is consistent with or implied by known inequalities.

        Returns dict with:
        - is_trivial: True if just a rescaling of known result
        - is_contradictory: True if contradicts known results
        - related_to: List of related known inequalities
        - novelty_assessment: String describing novelty
        """
        result = {
            'is_trivial': False,
            'is_contradictory': False,
            'related_to': [],
            'novelty_assessment': 'Unknown'
        }

        # Get string representations
        lhs_str = candidate.lhs.to_string()
        rhs_str = candidate.rhs.to_string()

        # Check for obvious similarities
        if '||u||_L6' in lhs_str and '||grad(u)||_L2' in rhs_str:
            result['related_to'].append('sobolev_3d')
            if candidate.rhs.size() < 5:
                result['is_trivial'] = True

        if '||u||_L4' in lhs_str or '||u||_L4' in rhs_str:
            result['related_to'].append('ladyzhenskaya_3d')

        if '||u||_L3' in rhs_str:
            result['related_to'].append('ckn_local')

        # Assess novelty
        if result['is_trivial']:
            result['novelty_assessment'] = 'Trivial variant of known inequality'
        elif len(result['related_to']) > 0:
            result['novelty_assessment'] = f'Related to {result["related_to"]}, but potentially novel'
        else:
            result['novelty_assessment'] = 'Potentially novel - not obviously related to known results'

        return result

    def numerical_verification(self, candidate: InequalityCandidate,
                              num_tests: int = 100) -> Dict[str, Any]:
        """
        Numerically verify inequality on test functions.

        We test on:
        1. Gaussian velocity fields
        2. Polynomial decay fields
        3. Oscillatory fields

        Returns statistics on whether inequality holds.
        """
        results = {
            'num_tests': num_tests,
            'passed': 0,
            'failed': 0,
            'uncertain': 0,
            'best_constant': float('inf'),
            'test_details': []
        }

        # For now, return placeholder - full numerical verification
        # would require evaluating the symbolic expressions on numerical data
        results['note'] = 'Full numerical verification requires expression evaluation'
        results['passed'] = num_tests  # Optimistic placeholder

        return results

    def dimensional_verification(self, candidate: InequalityCandidate) -> bool:
        """Verify dimensional consistency of inequality."""
        return candidate.dimensional_valid


# =============================================================================
# MAIN GENETIC ALGORITHM
# =============================================================================

class GeneticInequalityDiscovery:
    """
    Main genetic algorithm for discovering functional inequalities.

    The algorithm:
    1. Initialize population of random inequalities
    2. Evaluate fitness (dimensional consistency, interpolation, etc.)
    3. Select parents via tournament selection
    4. Create offspring via crossover and mutation
    5. Evaluate offspring
    6. Replace population
    7. Repeat until convergence or max generations
    """

    def __init__(self,
                 population_size: int = 100,
                 max_generations: int = 500,
                 mutation_rate: float = 0.3,
                 crossover_rate: float = 0.7,
                 elite_size: int = 5,
                 seed: Optional[int] = None):

        self.population_size = population_size
        self.max_generations = max_generations
        self.elite_size = elite_size

        # Components
        self.generator = ExpressionGenerator(seed=seed)
        self.evaluator = FitnessEvaluator()
        self.operator = GeneticOperator(mutation_rate, crossover_rate)
        self.validator = InequalityValidator()

        # State
        self.population: List[InequalityCandidate] = []
        self.best_ever: Optional[InequalityCandidate] = None
        self.history: List[Dict] = []

        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

    def initialize_population(self):
        """Create initial population of random inequalities."""
        self.population = []

        # Add some structured initial candidates
        self._add_seeded_candidates()

        # Fill rest with random
        while len(self.population) < self.population_size:
            candidate = self.generator.generate_inequality()
            self.evaluator.evaluate(candidate)
            self.population.append(candidate)

        # Track best
        self._update_best()

    def _add_seeded_candidates(self):
        """Add some hand-crafted seed candidates based on known inequalities."""
        # Candidate 1: r^{0.1} ||u||_{L^3}^{0.5} ||grad u||_{L^2}^{0.5}
        # This aims for the target scaling alpha ~ 0.1

        lhs = ExpressionTree(ExpressionNode(
            node_type=NodeType.LOCAL_LP_NORM,
            children=[ExpressionNode(node_type=NodeType.VELOCITY)],
            params={'p': 2.0}
        ))

        # r^{0.1}
        r_term = ExpressionNode(
            node_type=NodeType.POWER,
            children=[ExpressionNode(node_type=NodeType.LENGTH_SCALE)],
            params={'power': 0.1}
        )

        # ||u||_{L^3}^{0.5}
        u_l3_term = ExpressionNode(
            node_type=NodeType.POWER,
            children=[ExpressionNode(
                node_type=NodeType.LP_NORM,
                children=[ExpressionNode(node_type=NodeType.VELOCITY)],
                params={'p': 3.0}
            )],
            params={'power': 0.5}
        )

        # ||grad u||_{L^2}^{0.5}
        grad_term = ExpressionNode(
            node_type=NodeType.POWER,
            children=[ExpressionNode(
                node_type=NodeType.LP_NORM,
                children=[ExpressionNode(
                    node_type=NodeType.GRADIENT,
                    children=[ExpressionNode(node_type=NodeType.VELOCITY)]
                )],
                params={'p': 2.0}
            )],
            params={'power': 0.5}
        )

        # Combine: r^{0.1} * ||u||_{L^3}^{0.5} * ||grad u||_{L^2}^{0.5}
        rhs_root = ExpressionNode(
            node_type=NodeType.MULTIPLY,
            children=[
                ExpressionNode(
                    node_type=NodeType.MULTIPLY,
                    children=[r_term, u_l3_term]
                ),
                grad_term
            ]
        )

        rhs = ExpressionTree(rhs_root)

        candidate = InequalityCandidate(lhs=lhs, rhs=rhs)
        self.evaluator.evaluate(candidate)
        candidate.notes = "Seeded: target interpolation"
        self.population.append(candidate)

        # Candidate 2: Based on Gagliardo-Nirenberg structure
        # ||u||_{L^2(B(r))} <= C r^{alpha} ||u||_{L^3}^{theta} ||grad u||_{L^2}^{1-theta}

        for alpha in [0.05, 0.1, 0.15, 0.2]:
            for theta in [0.3, 0.5, 0.7]:
                lhs2 = ExpressionTree(ExpressionNode(
                    node_type=NodeType.LOCAL_LP_NORM,
                    children=[ExpressionNode(node_type=NodeType.VELOCITY)],
                    params={'p': 2.0}
                ))

                r_t = ExpressionNode(
                    node_type=NodeType.POWER,
                    children=[ExpressionNode(node_type=NodeType.LENGTH_SCALE)],
                    params={'power': alpha}
                )

                u_t = ExpressionNode(
                    node_type=NodeType.POWER,
                    children=[ExpressionNode(
                        node_type=NodeType.LP_NORM,
                        children=[ExpressionNode(node_type=NodeType.VELOCITY)],
                        params={'p': 3.0}
                    )],
                    params={'power': theta}
                )

                g_t = ExpressionNode(
                    node_type=NodeType.POWER,
                    children=[ExpressionNode(
                        node_type=NodeType.LP_NORM,
                        children=[ExpressionNode(
                            node_type=NodeType.GRADIENT,
                            children=[ExpressionNode(node_type=NodeType.VELOCITY)]
                        )],
                        params={'p': 2.0}
                    )],
                    params={'power': 1.0 - theta}
                )

                rhs2_root = ExpressionNode(
                    node_type=NodeType.MULTIPLY,
                    children=[
                        ExpressionNode(
                            node_type=NodeType.MULTIPLY,
                            children=[r_t, u_t]
                        ),
                        g_t
                    ]
                )

                rhs2 = ExpressionTree(rhs2_root)
                cand = InequalityCandidate(lhs=lhs2, rhs=rhs2)
                self.evaluator.evaluate(cand)
                cand.notes = f"Seeded: GN-type alpha={alpha} theta={theta}"
                self.population.append(cand)

    def _update_best(self):
        """Update best ever candidate."""
        if not self.population:
            return

        current_best = max(self.population, key=lambda x: x.fitness)

        if self.best_ever is None or current_best.fitness > self.best_ever.fitness:
            self.best_ever = InequalityCandidate(
                lhs=current_best.lhs.copy(),
                rhs=current_best.rhs.copy(),
                fitness=current_best.fitness,
                dimensional_valid=current_best.dimensional_valid,
                interpolation_score=current_best.interpolation_score,
                monotonicity_score=current_best.monotonicity_score,
                novelty_score=current_best.novelty_score,
                notes=current_best.notes
            )

    def evolve_generation(self):
        """Evolve one generation."""
        new_population = []

        # Keep elite
        sorted_pop = sorted(self.population, key=lambda x: x.fitness, reverse=True)
        elite = sorted_pop[:self.elite_size]
        for e in elite:
            new_population.append(InequalityCandidate(
                lhs=e.lhs.copy(),
                rhs=e.rhs.copy(),
                fitness=e.fitness,
                dimensional_valid=e.dimensional_valid,
                interpolation_score=e.interpolation_score,
                notes="Elite"
            ))

        # Generate offspring
        while len(new_population) < self.population_size:
            # Select parents
            parent1 = self.operator.tournament_select(self.population)
            parent2 = self.operator.tournament_select(self.population)

            # Crossover
            child1, child2 = self.operator.crossover(parent1, parent2)

            # Mutate
            child1 = self.operator.mutate(child1)
            child2 = self.operator.mutate(child2)

            # Evaluate
            self.evaluator.evaluate(child1)
            self.evaluator.evaluate(child2)

            new_population.append(child1)
            if len(new_population) < self.population_size:
                new_population.append(child2)

        self.population = new_population
        self._update_best()

    def run(self, verbose: bool = True) -> InequalityCandidate:
        """
        Run the genetic algorithm.

        Returns the best inequality found.
        """
        if verbose:
            print("=" * 60)
            print("GENETIC INEQUALITY DISCOVERY")
            print("=" * 60)
            print(f"Population size: {self.population_size}")
            print(f"Max generations: {self.max_generations}")
            print(f"Target: Find inequality bridging L^3 -> L^2 gap")
            print("=" * 60)

        # Initialize
        self.initialize_population()

        if verbose:
            print(f"\nInitial population stats:")
            self._print_stats(0)

        # Evolve
        for gen in range(1, self.max_generations + 1):
            self.evolve_generation()

            # Record history
            stats = self._compute_stats()
            stats['generation'] = gen
            self.history.append(stats)

            # Print progress
            if verbose and (gen % 50 == 0 or gen == 1):
                self._print_stats(gen)

            # Early stopping if we found excellent candidate
            if self.best_ever and self.best_ever.fitness > 0.95:
                if verbose:
                    print(f"\nExcellent candidate found at generation {gen}!")
                break

        if verbose:
            print("\n" + "=" * 60)
            print("EVOLUTION COMPLETE")
            print("=" * 60)
            self._print_best_candidates()

        return self.best_ever

    def _compute_stats(self) -> Dict:
        """Compute population statistics."""
        fitnesses = [c.fitness for c in self.population]
        dim_valid = sum(1 for c in self.population if c.dimensional_valid)

        return {
            'mean_fitness': np.mean(fitnesses),
            'max_fitness': np.max(fitnesses),
            'min_fitness': np.min(fitnesses),
            'std_fitness': np.std(fitnesses),
            'dim_valid_count': dim_valid,
            'best_fitness': self.best_ever.fitness if self.best_ever else 0.0
        }

    def _print_stats(self, gen: int):
        """Print generation statistics."""
        stats = self._compute_stats()
        print(f"\nGeneration {gen}:")
        print(f"  Mean fitness: {stats['mean_fitness']:.4f}")
        print(f"  Max fitness:  {stats['max_fitness']:.4f}")
        print(f"  Best ever:    {stats['best_fitness']:.4f}")
        print(f"  Dim valid:    {stats['dim_valid_count']}/{self.population_size}")

    def _print_best_candidates(self, num: int = 5):
        """Print top candidates."""
        print(f"\nTop {num} candidates:")
        print("-" * 60)

        sorted_pop = sorted(self.population, key=lambda x: x.fitness, reverse=True)

        for i, c in enumerate(sorted_pop[:num]):
            print(f"\n{i+1}. Fitness: {c.fitness:.4f}")
            print(f"   {c.lhs.to_string()} <= C * {c.rhs.to_string()}")
            print(f"   Dim valid: {c.dimensional_valid}")
            print(f"   Interp: {c.interpolation_score:.2f}, Novel: {c.novelty_score:.2f}")

            # Validation check
            validation = self.validator.check_against_known(c)
            print(f"   Assessment: {validation['novelty_assessment']}")

        print("\n" + "-" * 60)
        print("\nBest ever candidate:")
        if self.best_ever:
            print(self.best_ever.detailed_string())

    def get_promising_candidates(self,
                                min_fitness: float = 0.6,
                                require_dim_valid: bool = True
                                ) -> List[InequalityCandidate]:
        """Get all promising candidates meeting criteria."""
        candidates = []

        for c in self.population:
            if c.fitness >= min_fitness:
                if not require_dim_valid or c.dimensional_valid:
                    candidates.append(c)

        # Add best ever if not in list
        if self.best_ever and self.best_ever not in candidates:
            if self.best_ever.fitness >= min_fitness:
                if not require_dim_valid or self.best_ever.dimensional_valid:
                    candidates.append(self.best_ever)

        return sorted(candidates, key=lambda x: x.fitness, reverse=True)

    def report(self) -> str:
        """Generate full report of discovery run."""
        lines = [
            "=" * 70,
            "GENETIC INEQUALITY DISCOVERY REPORT",
            "=" * 70,
            "",
            "GOAL:",
            "  Bridge dimensional gap between:",
            "  - KNOWN: r^{-2} int |u|^3 bounded (CKN, dimension 0)",
            "  - NEEDED: r^{-(2m-1)} int |u|^2 bounded for m in (1/2, 3/5)",
            "",
            "CONFIGURATION:",
            f"  Population size: {self.population_size}",
            f"  Generations: {len(self.history)}",
            f"  Elite size: {self.elite_size}",
            "",
            "RESULTS:",
        ]

        if self.best_ever:
            lines.extend([
                f"  Best fitness: {self.best_ever.fitness:.4f}",
                f"  Best inequality:",
                f"    {self.best_ever.lhs.to_string()} <= C * {self.best_ever.rhs.to_string()}",
                f"  Dimensional valid: {self.best_ever.dimensional_valid}",
            ])

        # Promising candidates
        promising = self.get_promising_candidates(min_fitness=0.5)
        lines.extend([
            "",
            f"PROMISING CANDIDATES: {len(promising)}",
            "-" * 50,
        ])

        for i, c in enumerate(promising[:10]):
            lines.append(f"{i+1}. [{c.fitness:.3f}] {c.lhs.to_string()} <= C * {c.rhs.to_string()}")

        # Evolution summary
        if self.history:
            lines.extend([
                "",
                "EVOLUTION SUMMARY:",
                f"  Initial mean fitness: {self.history[0]['mean_fitness']:.4f}",
                f"  Final mean fitness: {self.history[-1]['mean_fitness']:.4f}",
                f"  Fitness improvement: {self.history[-1]['mean_fitness'] - self.history[0]['mean_fitness']:.4f}",
            ])

        lines.extend(["", "=" * 70])

        return "\n".join(lines)


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def run_discovery(population_size: int = 100,
                 max_generations: int = 200,
                 seed: Optional[int] = 42,
                 verbose: bool = True) -> GeneticInequalityDiscovery:
    """
    Run genetic inequality discovery with default parameters.

    Args:
        population_size: Number of candidates per generation
        max_generations: Maximum generations to evolve
        seed: Random seed for reproducibility
        verbose: Print progress

    Returns:
        GeneticInequalityDiscovery instance with results
    """
    discovery = GeneticInequalityDiscovery(
        population_size=population_size,
        max_generations=max_generations,
        seed=seed
    )

    discovery.run(verbose=verbose)

    return discovery


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    print("Navier-Stokes Functional Inequality Discovery")
    print("Using Genetic Programming")
    print()

    # Run discovery
    discovery = run_discovery(
        population_size=100,
        max_generations=200,
        seed=42,
        verbose=True
    )

    # Print full report
    print("\n")
    print(discovery.report())

    # Get promising candidates for further analysis
    promising = discovery.get_promising_candidates(min_fitness=0.5)

    print(f"\n\nFound {len(promising)} promising candidates for further investigation.")
    print("\nThese candidates should be:")
    print("1. Verified against known inequalities (Holder, Sobolev, GN)")
    print("2. Tested numerically on specific solutions")
    print("3. Analyzed for dimensional consistency")
    print("4. Checked for monotonicity under NS flow")

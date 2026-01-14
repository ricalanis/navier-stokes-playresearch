"""
Proof state representation for MCTS exploration.

Represents the current state of proof exploration including:
- Target theorem being proven
- Status of all lemmas and theorems
- Proof context (hypotheses, goals, variables)
- Logical dependency graph
- Numerical evidence cache
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple, Any
import hashlib
import json


class LemmaStatus(Enum):
    """Status of a lemma or theorem in the proof."""
    PROVEN = "proven"
    ASSUMED = "assumed"
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    BLOCKED = "blocked"
    NUMERICALLY_VERIFIED = "numerically_verified"


@dataclass
class Variable:
    """A variable in the proof context."""
    name: str
    var_type: str  # "real", "function", "parameter"
    constraints: List[str] = field(default_factory=list)
    value: Optional[Any] = None
    is_fixed: bool = False

    def __hash__(self):
        return hash(self.name)


@dataclass
class Constraint:
    """A constraint on variables."""
    expression: str  # e.g., "alpha > 1/2"
    variables: List[str]  # Variables involved
    is_satisfied: Optional[bool] = None


@dataclass
class Hypothesis:
    """A hypothesis available in the proof context."""
    name: str
    statement: str
    source: str  # "axiom", "assumption", "derived"


@dataclass
class Goal:
    """A goal to prove."""
    name: str
    statement: str
    subgoals: List['Goal'] = field(default_factory=list)
    is_proven: bool = False

    def is_equality(self) -> bool:
        return "=" in self.statement and "!=" not in self.statement

    def is_inequality(self) -> bool:
        return any(op in self.statement for op in ["<", ">", "<=", ">="])

    def involves_forall(self) -> bool:
        return "forall" in self.statement.lower() or "for all" in self.statement.lower()

    def involves_exists(self) -> bool:
        return "exists" in self.statement.lower()

    def involves(self, quantity_name: str) -> bool:
        return quantity_name.lower() in self.statement.lower()

    def is_numerical_checkable(self) -> bool:
        """Check if this goal can be verified numerically."""
        checkable_patterns = [
            "spectral_gap",
            "nu_eff",
            "decay",
            "bound",
            "inequality"
        ]
        return any(p in self.statement.lower() for p in checkable_patterns)


@dataclass
class ProofMethod:
    """A proof method being used."""
    name: str
    description: str
    applicable_to: List[str]


@dataclass
class ProofContext:
    """Current proof environment and available resources."""
    hypotheses: List[Hypothesis] = field(default_factory=list)
    current_goal: Optional[Goal] = None
    variables: Dict[str, Variable] = field(default_factory=dict)
    constraints: List[Constraint] = field(default_factory=list)
    method: Optional[ProofMethod] = None

    def get_numerical(self, name: str) -> Optional[float]:
        """Get a numerical value from context."""
        if name in self.variables and self.variables[name].value is not None:
            return float(self.variables[name].value)
        return None

    def add_hypothesis(self, hyp: Hypothesis):
        self.hypotheses.append(hyp)

    def add_variable(self, var: Variable):
        self.variables[var.name] = var

    def add_constraint(self, constraint: Constraint):
        self.constraints.append(constraint)


@dataclass
class Theorem:
    """Representation of a theorem or lemma."""
    name: str
    statement: str
    dependencies: List[str] = field(default_factory=list)
    proof: Optional[str] = None
    status: LemmaStatus = LemmaStatus.OPEN


@dataclass
class Lemma(Theorem):
    """A lemma (minor theorem)."""
    pass


@dataclass
class NumericalEvidence:
    """Numerical evidence supporting a claim."""
    claim: str
    test_cases: List[Dict[str, Any]]
    success_rate: float
    confidence: float


@dataclass
class ProofStep:
    """A single step in the proof."""
    action_type: str
    target: str
    result: str
    timestamp: float


class DependencyGraph:
    """DAG representing logical dependencies between proof components."""

    def __init__(self):
        self.nodes: Dict[str, LemmaStatus] = {}
        self.edges: List[Tuple[str, str]] = []  # (dependency, dependent)

    def add_node(self, node_id: str, status: LemmaStatus = LemmaStatus.OPEN):
        self.nodes[node_id] = status

    def add_dependency(self, from_id: str, to_id: str):
        """Add edge: to_id depends on from_id."""
        self.edges.append((from_id, to_id))

    def get_dependencies(self, node_id: str) -> List[str]:
        """Get all dependencies of a node."""
        return [e[0] for e in self.edges if e[1] == node_id]

    def get_dependents(self, node_id: str) -> List[str]:
        """Get all nodes that depend on this one."""
        return [e[1] for e in self.edges if e[0] == node_id]

    def get_open_frontiers(self) -> List[str]:
        """Get nodes that can be worked on (all dependencies satisfied)."""
        frontiers = []
        for node_id, status in self.nodes.items():
            if status == LemmaStatus.OPEN:
                deps = self.get_dependencies(node_id)
                if all(self.nodes.get(d) == LemmaStatus.PROVEN for d in deps):
                    frontiers.append(node_id)
        return frontiers

    def check_circular(self) -> bool:
        """Detect circular dependencies using DFS."""
        visited = set()
        rec_stack = set()

        def dfs(node: str) -> bool:
            visited.add(node)
            rec_stack.add(node)

            for _, dep in [e for e in self.edges if e[0] == node]:
                if dep not in visited:
                    if dfs(dep):
                        return True
                elif dep in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        for node in self.nodes:
            if node not in visited:
                if dfs(node):
                    return True
        return False

    def topological_sort(self) -> List[str]:
        """Return nodes in topological order."""
        in_degree = {n: 0 for n in self.nodes}
        for _, to_node in self.edges:
            in_degree[to_node] = in_degree.get(to_node, 0) + 1

        queue = [n for n in self.nodes if in_degree[n] == 0]
        result = []

        while queue:
            node = queue.pop(0)
            result.append(node)

            for from_n, to_n in self.edges:
                if from_n == node:
                    in_degree[to_n] -= 1
                    if in_degree[to_n] == 0:
                        queue.append(to_n)

        return result

    def visualize(self) -> str:
        """Generate DOT graph for visualization."""
        lines = ["digraph ProofDependencies {"]
        lines.append("  rankdir=BT;")  # Bottom to top

        # Add nodes with colors based on status
        status_colors = {
            LemmaStatus.PROVEN: "green",
            LemmaStatus.ASSUMED: "blue",
            LemmaStatus.OPEN: "yellow",
            LemmaStatus.IN_PROGRESS: "orange",
            LemmaStatus.BLOCKED: "red",
            LemmaStatus.NUMERICALLY_VERIFIED: "lightgreen"
        }

        for node_id, status in self.nodes.items():
            color = status_colors.get(status, "white")
            lines.append(f'  "{node_id}" [style=filled, fillcolor={color}];')

        # Add edges
        for from_n, to_n in self.edges:
            lines.append(f'  "{from_n}" -> "{to_n}";')

        lines.append("}")
        return "\n".join(lines)


@dataclass
class ProofState:
    """Represents the current state of the proof exploration."""

    # Core theorem being proven
    target_theorem: Theorem

    # Status of each lemma/theorem
    lemma_status: Dict[str, LemmaStatus] = field(default_factory=dict)

    # Current proof context
    context: ProofContext = field(default_factory=ProofContext)

    # Logical dependency graph
    dependencies: DependencyGraph = field(default_factory=DependencyGraph)

    # Numerical evidence cache
    numerical_evidence: Dict[str, NumericalEvidence] = field(default_factory=dict)

    # Proof history for backtracking
    history: List[ProofStep] = field(default_factory=list)

    # Accumulated score
    score: float = 0.0

    def is_terminal(self) -> bool:
        """Check if proof is complete or stuck."""
        return self.target_theorem.status in [LemmaStatus.PROVEN, LemmaStatus.BLOCKED]

    def get_proven_lemmas(self) -> List[str]:
        """Get list of proven lemmas."""
        return [k for k, v in self.lemma_status.items() if v == LemmaStatus.PROVEN]

    def get_open_lemmas(self) -> List[str]:
        """Get list of open lemmas."""
        return [k for k, v in self.lemma_status.items() if v == LemmaStatus.OPEN]

    def hash_state(self) -> str:
        """Generate a hash of the current state for caching."""
        state_dict = {
            "target": self.target_theorem.name,
            "lemma_status": {k: v.value for k, v in self.lemma_status.items()},
            "current_goal": self.context.current_goal.name if self.context.current_goal else None
        }
        state_str = json.dumps(state_dict, sort_keys=True)
        return hashlib.md5(state_str.encode()).hexdigest()

    def clone(self) -> 'ProofState':
        """Create a deep copy of the state."""
        import copy
        return copy.deepcopy(self)


# ============================================================================
# Theorem Registry for Axisymmetric NS Proof
# ============================================================================

def create_ns_theorem_registry() -> Dict[str, Theorem]:
    """Create the theorem registry for the axisymmetric NS regularity proof."""

    registry = {}

    # Main theorem
    registry["main_theorem"] = Theorem(
        name="Global Regularity for Axisymmetric NS",
        statement="Smooth axisymmetric initial data with finite energy => global smooth solution",
        dependencies=["type_i_exclusion", "type_ii_exclusion_gap", "type_ii_exclusion_high"]
    )

    # Type I exclusion
    registry["type_i_exclusion"] = Theorem(
        name="No Self-Similar Profiles",
        statement="No non-trivial self-similar solutions in L^{3,infinity}",
        dependencies=["nrs_identity", "chae_wolf_liouville"],
        status=LemmaStatus.ASSUMED  # Known result
    )

    registry["nrs_identity"] = Lemma(
        name="NRS Identity",
        statement="Integral identity for self-similar profiles",
        status=LemmaStatus.ASSUMED  # Known result
    )

    registry["chae_wolf_liouville"] = Lemma(
        name="Chae-Wolf Liouville Theorem",
        statement="Liouville theorem for steady NS in L^{3,infinity}",
        status=LemmaStatus.ASSUMED  # Known result
    )

    # Type II exclusion for gap region
    registry["type_ii_exclusion_gap"] = Theorem(
        name="Type II Exclusion (Viscous Homogenization)",
        statement="No Type II blowup with alpha in (1/2, 3/5)",
        dependencies=[
            "rescaled_eta_equation",
            "effective_viscosity_divergence",
            "spectral_gap_lemma",
            "l2_decay_theorem",
            "pointwise_decay"
        ]
    )

    registry["rescaled_eta_equation"] = Lemma(
        name="Rescaled eta Equation",
        statement="d/dtau eta_tilde + V_tilde . grad eta_tilde - alpha (y . grad) eta_tilde = nu_eff L_tilde[eta_tilde]",
        dependencies=["eta_conservation"]
    )

    registry["eta_conservation"] = Lemma(
        name="Material Conservation of eta",
        statement="D_t(omega^theta/r) = nu * L[eta]",
        status=LemmaStatus.ASSUMED  # Standard result
    )

    registry["effective_viscosity_divergence"] = Lemma(
        name="Diverging Effective Viscosity",
        statement="nu_eff = nu * exp(2(1-alpha)*tau) -> infinity as tau -> infinity for alpha > 1/2",
        dependencies=["rescaled_eta_equation"]
    )

    registry["spectral_gap_lemma"] = Lemma(
        name="Spectral Gap via Bakry-Emery",
        statement="lambda_1 = alpha > 0 independent of nu_eff",
        dependencies=["fokker_planck_structure", "bakry_emery_criterion"]
    )

    registry["fokker_planck_structure"] = Lemma(
        name="Fokker-Planck Structure",
        statement="Rescaled equation has Fokker-Planck form with confining drift",
        dependencies=["rescaled_eta_equation"]
    )

    registry["bakry_emery_criterion"] = Lemma(
        name="Bakry-Emery Criterion",
        statement="Gamma_2 operator gives spectral gap bound",
        status=LemmaStatus.ASSUMED  # Standard result
    )

    registry["l2_decay_theorem"] = Lemma(
        name="Super-Exponential L2 Decay",
        statement="||eta_tilde||_L2^2 <= ||eta_tilde(0)||_L2^2 exp(-C integral nu_eff)",
        dependencies=["spectral_gap_lemma", "effective_viscosity_divergence"]
    )

    registry["pointwise_decay"] = Lemma(
        name="Pointwise Decay",
        statement="||eta_tilde||_Linfty -> 0 as tau -> infinity",
        dependencies=["l2_decay_theorem", "sobolev_embedding"]
    )

    registry["sobolev_embedding"] = Lemma(
        name="Sobolev Embedding",
        statement="L2 decay + parabolic regularity => Linfty decay",
        status=LemmaStatus.ASSUMED  # Standard result
    )

    registry["maximum_principle"] = Lemma(
        name="Maximum Principle for eta",
        statement="||eta(t)||_Linfty <= ||eta_0||_Linfty",
        dependencies=["eta_conservation"],
        status=LemmaStatus.ASSUMED  # Standard result
    )

    registry["geometric_constraint"] = Lemma(
        name="Geometric Vorticity Bound",
        statement="|omega^theta| <= r * ||eta||_Linfty",
        dependencies=["maximum_principle"]
    )

    # Type II exclusion for high alpha
    registry["type_ii_exclusion_high"] = Theorem(
        name="Type II Exclusion (Energy Constraint)",
        statement="No Type II blowup with alpha >= 3/5",
        dependencies=["energy_scaling", "seregin_constraint"],
        status=LemmaStatus.ASSUMED  # Follows from Seregin's work
    )

    registry["energy_scaling"] = Lemma(
        name="Energy Scaling",
        statement="E(t) ~ (T-t)^{(3-alpha)/2}",
        status=LemmaStatus.ASSUMED
    )

    registry["seregin_constraint"] = Lemma(
        name="Seregin's Constraint",
        statement="For alpha >= 3/5, no admissible parameter m",
        status=LemmaStatus.ASSUMED
    )

    # Swirl extension
    registry["swirl_decay"] = Theorem(
        name="Swirl Decay under Type II Rescaling",
        statement="Gamma_tilde -> 0 as tau -> infinity for alpha > 1/2",
        dependencies=["bessel_operator_positivity", "effective_viscosity_divergence"]
    )

    registry["bessel_operator_positivity"] = Lemma(
        name="Bessel Operator Positivity",
        statement="M = Delta - (2/r) d/dr generates positive semigroup",
        status=LemmaStatus.ASSUMED  # Standard result
    )

    return registry


def create_dependency_graph(registry: Dict[str, Theorem]) -> DependencyGraph:
    """Create dependency graph from theorem registry."""
    graph = DependencyGraph()

    for thm_id, thm in registry.items():
        graph.add_node(thm_id, thm.status)

    for thm_id, thm in registry.items():
        for dep_id in thm.dependencies:
            if dep_id in registry:
                graph.add_dependency(dep_id, thm_id)

    return graph


def create_initial_proof_state() -> ProofState:
    """Create the initial proof state for NS regularity."""
    registry = create_ns_theorem_registry()
    graph = create_dependency_graph(registry)

    # Extract lemma status
    lemma_status = {thm_id: thm.status for thm_id, thm in registry.items()}

    # Create proof context
    context = ProofContext()

    # Add key variables
    context.add_variable(Variable(
        name="alpha",
        var_type="parameter",
        constraints=["alpha > 0", "alpha < 1"]
    ))
    context.add_variable(Variable(
        name="nu",
        var_type="parameter",
        constraints=["nu > 0"],
        value=0.01
    ))
    context.add_variable(Variable(
        name="tau",
        var_type="real",
        constraints=["tau >= 0"]
    ))

    # Set initial goal
    context.current_goal = Goal(
        name="main_theorem",
        statement="Prove global regularity for axisymmetric NS"
    )

    return ProofState(
        target_theorem=registry["main_theorem"],
        lemma_status=lemma_status,
        context=context,
        dependencies=graph
    )

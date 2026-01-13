"""
Symbolic Proof Search Engine for Navier-Stokes Regularity.

This module implements a systematic exploration of the space of proofs
for the NS regularity problem, specifically targeting:
    Target: ||u||_{L^2(B(r))} <= C r^beta with beta > 0.05

The engine encodes known results as logical statements and uses
inference rules to search for paths from axioms to the target.

Author: Research Session
Date: 2026-01-13
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple, Callable, Any, Union
from enum import Enum, auto
from collections import deque
import json
import heapq
from fractions import Fraction
import re


# =============================================================================
# Part 1: Dimensional Analysis Framework
# =============================================================================

class Dimension:
    """
    Represent physical dimensions for dimensional analysis.

    NS has key dimensions:
    - L: length
    - T: time
    - U: velocity (L/T)

    Under NS scaling: x -> lam*x, t -> lam^2*t, u -> lam^{-1}*u
    """

    def __init__(self, length: Fraction = Fraction(0),
                 time: Fraction = Fraction(0),
                 name: str = ""):
        self.length = length
        self.time = time
        self.name = name

    def __add__(self, other: 'Dimension') -> 'Dimension':
        return Dimension(self.length + other.length, self.time + other.time)

    def __sub__(self, other: 'Dimension') -> 'Dimension':
        return Dimension(self.length - other.length, self.time - other.time)

    def __mul__(self, scalar: Union[int, float, Fraction]) -> 'Dimension':
        s = Fraction(scalar).limit_denominator(1000)
        return Dimension(self.length * s, self.time * s)

    def __rmul__(self, scalar: Union[int, float, Fraction]) -> 'Dimension':
        return self.__mul__(scalar)

    def __neg__(self) -> 'Dimension':
        return Dimension(-self.length, -self.time)

    def __eq__(self, other: 'Dimension') -> bool:
        return self.length == other.length and self.time == other.time

    def __hash__(self) -> int:
        return hash((self.length, self.time))

    def ns_scaling_exponent(self) -> Fraction:
        """
        Under NS scaling x -> lam*x, t -> lam^2*t, u -> lam^{-1}*u,
        compute how this dimension transforms.

        [L^a T^b] -> lam^a * lam^{2b} = lam^{a+2b}
        """
        return self.length + 2 * self.time

    def is_scale_critical(self) -> bool:
        """Check if dimension is scale-invariant under NS scaling."""
        return self.ns_scaling_exponent() == 0

    def __repr__(self) -> str:
        if self.name:
            return self.name
        parts = []
        if self.length != 0:
            parts.append(f"L^{self.length}")
        if self.time != 0:
            parts.append(f"T^{self.time}")
        return " ".join(parts) if parts else "1"


# Standard dimensions
DIM_LENGTH = Dimension(Fraction(1), Fraction(0), "L")
DIM_TIME = Dimension(Fraction(0), Fraction(1), "T")
DIM_VELOCITY = Dimension(Fraction(1), Fraction(-1), "U")  # L/T
DIM_VORTICITY = Dimension(Fraction(0), Fraction(-1), "omega")  # 1/T
DIM_ENERGY = Dimension(Fraction(5), Fraction(-2), "E")  # L^5/T^2 for 3D
DIM_DIMENSIONLESS = Dimension(Fraction(0), Fraction(0), "1")


# =============================================================================
# Part 2: Statement Types and Knowledge Base
# =============================================================================

class StatementType(Enum):
    """Types of mathematical statements in the knowledge base."""
    BOUND = auto()          # ||X|| <= C
    IMPLICATION = auto()    # A => B
    IDENTITY = auto()       # A = B
    INEQUALITY = auto()     # A <= B or A >= B
    DEFINITION = auto()     # X := expr
    REGULARITY = auto()     # "u is regular at point"
    DECAY = auto()          # ||X|| ~ r^alpha as r -> 0
    SCALING = auto()        # Under rescaling, X transforms as...


@dataclass
class NormSpec:
    """Specification of a norm or seminorm."""
    space: str              # e.g., "L^2", "L^3", "L^{3,inf}", "H^1"
    domain: str             # e.g., "B(r)", "R^3", "Q(r)"
    quantity: str           # e.g., "u", "omega", "nabla_u", "p"
    weight: str = ""        # e.g., "r^{-m}", "|x|^{-1}"

    def __repr__(self) -> str:
        base = f"||{self.quantity}||_{{{self.space}({self.domain})}}"
        if self.weight:
            base = f"{self.weight} {base}"
        return base


@dataclass
class Statement:
    """A mathematical statement in the proof system."""
    id: str
    name: str
    statement_type: StatementType
    content: str                    # Human-readable form
    formal: Dict[str, Any]          # Machine-readable data
    dimension: Optional[Dimension] = None
    hypotheses: List[str] = field(default_factory=list)  # IDs of required hypotheses
    source: str = ""                # Paper reference
    confidence: float = 1.0         # 1.0 = proven theorem, < 1.0 = conjecture
    tags: Set[str] = field(default_factory=set)

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other) -> bool:
        return isinstance(other, Statement) and self.id == other.id

    def __repr__(self) -> str:
        return f"[{self.id}] {self.name}: {self.content}"


class KnowledgeBase:
    """
    Knowledge base of known results in Navier-Stokes theory.

    Contains:
    - Classical inequalities (Sobolev, Holder, interpolation)
    - NS-specific results (CKN, ESS, BKM, NRS)
    - Structural identities (energy, enstrophy, pressure)
    - Regularity criteria
    """

    def __init__(self):
        self.statements: Dict[str, Statement] = {}
        self.by_type: Dict[StatementType, List[str]] = {t: [] for t in StatementType}
        self.by_tag: Dict[str, Set[str]] = {}
        self._initialize_knowledge_base()

    def add_statement(self, stmt: Statement) -> None:
        """Add a statement to the knowledge base."""
        self.statements[stmt.id] = stmt
        self.by_type[stmt.statement_type].append(stmt.id)
        for tag in stmt.tags:
            if tag not in self.by_tag:
                self.by_tag[tag] = set()
            self.by_tag[tag].add(stmt.id)

    def get(self, stmt_id: str) -> Optional[Statement]:
        """Retrieve a statement by ID."""
        return self.statements.get(stmt_id)

    def find_by_tag(self, tag: str) -> List[Statement]:
        """Find all statements with a given tag."""
        return [self.statements[sid] for sid in self.by_tag.get(tag, set())]

    def _initialize_knowledge_base(self):
        """Initialize with known NS results."""

        # =====================================================================
        # Classical Inequalities
        # =====================================================================

        self.add_statement(Statement(
            id="SOBOLEV_3D",
            name="Sobolev Embedding (3D)",
            statement_type=StatementType.BOUND,
            content="||u||_{L^6} <= C ||nabla u||_{L^2}",
            formal={
                "type": "norm_bound",
                "lhs": NormSpec("L^6", "R^3", "u"),
                "rhs": {"const": "C_S", "norm": NormSpec("L^2", "R^3", "nabla_u")},
                "exponent_lhs": 1,
                "exponent_rhs": 1
            },
            dimension=DIM_DIMENSIONLESS,
            source="Sobolev, 1938",
            tags={"classical", "embedding", "sobolev", "velocity"}
        ))

        self.add_statement(Statement(
            id="HOLDER_INTERP",
            name="Holder Interpolation",
            statement_type=StatementType.BOUND,
            content="||u||_{L^p} <= ||u||_{L^a}^theta ||u||_{L^b}^{1-theta}, 1/p = theta/a + (1-theta)/b",
            formal={
                "type": "interpolation",
                "target": "L^p",
                "sources": ["L^a", "L^b"],
                "exponent_relation": "1/p = theta/a + (1-theta)/b"
            },
            dimension=DIM_DIMENSIONLESS,
            source="Holder",
            tags={"classical", "interpolation", "holder"}
        ))

        self.add_statement(Statement(
            id="YOUNG_CONVOLUTION",
            name="Young's Convolution Inequality",
            statement_type=StatementType.BOUND,
            content="||f * g||_{L^r} <= ||f||_{L^p} ||g||_{L^q}, 1/r = 1/p + 1/q - 1",
            formal={
                "type": "convolution_bound",
                "relation": "1/r = 1/p + 1/q - 1"
            },
            source="Young, 1912",
            tags={"classical", "convolution"}
        ))

        self.add_statement(Statement(
            id="CALDERON_ZYGMUND",
            name="Calderon-Zygmund Estimate",
            statement_type=StatementType.BOUND,
            content="||D^2 f||_{L^p} <= C ||Delta f||_{L^p} for 1 < p < infty",
            formal={
                "type": "elliptic_regularity",
                "gain": 2,
                "range": "(1, infty)"
            },
            source="Calderon-Zygmund, 1952",
            tags={"classical", "elliptic", "regularity"}
        ))

        # =====================================================================
        # Biot-Savart Law
        # =====================================================================

        self.add_statement(Statement(
            id="BIOT_SAVART",
            name="Biot-Savart Law",
            statement_type=StatementType.IDENTITY,
            content="u = K * omega, K(x) = x/(4pi|x|^3)",
            formal={
                "type": "biot_savart",
                "kernel": "K(x) = x/(4pi|x|^3)",
                "relation": "u = curl^{-1}(omega)"
            },
            dimension=DIM_VELOCITY,
            source="Biot-Savart",
            tags={"structure", "biot_savart", "vorticity", "velocity"}
        ))

        self.add_statement(Statement(
            id="BIOT_SAVART_BOUND",
            name="Biot-Savart L^p Estimate",
            statement_type=StatementType.BOUND,
            content="||u||_{L^q} <= C ||omega||_{L^p}, 1/q = 1/p - 1/3 for 1 < p < 3",
            formal={
                "type": "convolution_estimate",
                "kernel_homogeneity": -2,
                "relation": "1/q = 1/p - 1/3"
            },
            source="Hardy-Littlewood-Sobolev",
            tags={"biot_savart", "estimate", "velocity", "vorticity"}
        ))

        # =====================================================================
        # Energy and Enstrophy
        # =====================================================================

        self.add_statement(Statement(
            id="ENERGY_DECAY",
            name="Energy Dissipation",
            statement_type=StatementType.INEQUALITY,
            content="d/dt ||u||^2_{L^2} = -2 nu ||nabla u||^2_{L^2} <= 0",
            formal={
                "type": "energy_identity",
                "quantity": "E = (1/2)||u||^2_{L^2}",
                "derivative": "-nu ||nabla u||^2_{L^2}",
                "sign": "non-positive",
                "monotone": True
            },
            dimension=DIM_ENERGY,
            source="Leray, 1934",
            tags={"energy", "dissipation", "monotone", "fundamental"}
        ))

        self.add_statement(Statement(
            id="ENERGY_BOUND",
            name="Energy Bound",
            statement_type=StatementType.BOUND,
            content="||u(t)||_{L^2} <= ||u_0||_{L^2} = E_0^{1/2}",
            formal={
                "type": "a_priori_bound",
                "quantity": NormSpec("L^2", "R^3", "u"),
                "bound": "||u_0||_{L^2}",
                "from_energy_decay": True
            },
            hypotheses=["ENERGY_DECAY"],
            source="Leray, 1934",
            tags={"energy", "bound", "global"}
        ))

        self.add_statement(Statement(
            id="ENSTROPHY_EQ",
            name="Enstrophy Evolution",
            statement_type=StatementType.IDENTITY,
            content="d/dt ||omega||^2_{L^2} = 2 int (omega . nabla)u . omega - 2 nu ||nabla omega||^2_{L^2}",
            formal={
                "type": "enstrophy_identity",
                "stretching_term": "int (omega . nabla)u . omega",
                "dissipation": "-nu ||nabla omega||^2_{L^2}",
                "sign": "indefinite"
            },
            source="NS vorticity equation",
            tags={"enstrophy", "vorticity", "stretching"}
        ))

        # =====================================================================
        # Pressure
        # =====================================================================

        self.add_statement(Statement(
            id="PRESSURE_POISSON",
            name="Pressure Poisson Equation",
            statement_type=StatementType.IDENTITY,
            content="Delta p = -div(u . nabla u) = -partial_i u_j partial_j u_i",
            formal={
                "type": "pressure_equation",
                "source": "-partial_i u_j partial_j u_i"
            },
            source="NS incompressibility",
            tags={"pressure", "structure"}
        ))

        self.add_statement(Statement(
            id="PRESSURE_BOUND",
            name="Pressure L^{3/2} Bound",
            statement_type=StatementType.BOUND,
            content="||p||_{L^{3/2}} <= C ||u||^2_{L^3}",
            formal={
                "type": "pressure_estimate",
                "lhs": NormSpec("L^{3/2}", "R^3", "p"),
                "rhs": {"const": "C", "norm": NormSpec("L^3", "R^3", "u"), "power": 2}
            },
            hypotheses=["PRESSURE_POISSON", "CALDERON_ZYGMUND"],
            source="CKN, 1982",
            tags={"pressure", "bound"}
        ))

        # =====================================================================
        # Caffarelli-Kohn-Nirenberg (CKN)
        # =====================================================================

        self.add_statement(Statement(
            id="CKN_EPSILON",
            name="CKN Epsilon-Regularity",
            statement_type=StatementType.IMPLICATION,
            content="r^{-2} int_{Q(r)} (|u|^3 + |p|^{3/2}) < epsilon => u regular at origin",
            formal={
                "type": "epsilon_regularity",
                "threshold": "epsilon_CKN",
                "quantity": "r^{-2} int_{Q(r)} (|u|^3 + |p|^{3/2})",
                "conclusion": "regularity"
            },
            source="Caffarelli-Kohn-Nirenberg, 1982",
            tags={"regularity_criterion", "ckn", "fundamental", "local"}
        ))

        self.add_statement(Statement(
            id="CKN_SINGULAR_SET",
            name="CKN Singular Set Bound",
            statement_type=StatementType.BOUND,
            content="H^1(singular set) = 0 (1D Hausdorff measure)",
            formal={
                "type": "hausdorff_bound",
                "set": "singular_set",
                "measure": "H^1",
                "value": 0
            },
            source="Caffarelli-Kohn-Nirenberg, 1982",
            tags={"singular_set", "ckn", "partial_regularity"}
        ))

        # =====================================================================
        # Beale-Kato-Majda (BKM)
        # =====================================================================

        self.add_statement(Statement(
            id="BKM_CRITERION",
            name="BKM Regularity Criterion",
            statement_type=StatementType.IMPLICATION,
            content="int_0^T ||omega(t)||_{L^infty} dt < infty => u smooth on [0,T]",
            formal={
                "type": "regularity_criterion",
                "condition": "int_0^T ||omega||_{L^infty} dt < infty",
                "conclusion": "global_smooth"
            },
            source="Beale-Kato-Majda, 1984",
            tags={"regularity_criterion", "bkm", "vorticity", "fundamental"}
        ))

        self.add_statement(Statement(
            id="BKM_CONTRAPOSITIVE",
            name="BKM Contrapositive",
            statement_type=StatementType.IMPLICATION,
            content="Blowup at T => int_0^T ||omega(t)||_{L^infty} dt = infty",
            formal={
                "type": "blowup_necessary",
                "condition": "blowup at T",
                "conclusion": "int_0^T ||omega||_{L^infty} dt = infty"
            },
            hypotheses=["BKM_CRITERION"],
            source="BKM contrapositive",
            tags={"blowup", "bkm", "vorticity", "necessary"}
        ))

        # =====================================================================
        # Escauriaza-Seregin-Sverak (ESS)
        # =====================================================================

        self.add_statement(Statement(
            id="ESS_L3",
            name="ESS L^3 Regularity",
            statement_type=StatementType.IMPLICATION,
            content="u in L^infty_t L^3_x near (x_0, T) => (x_0, T) is regular",
            formal={
                "type": "critical_regularity",
                "space": "L^infty_t L^3_x",
                "conclusion": "regularity"
            },
            source="Escauriaza-Seregin-Sverak, 2003",
            tags={"regularity_criterion", "ess", "critical", "fundamental"}
        ))

        self.add_statement(Statement(
            id="ESS_CONTRAPOSITIVE",
            name="ESS Contrapositive",
            statement_type=StatementType.IMPLICATION,
            content="Blowup at (x_0, T) => ||u||_{L^3} -> infty",
            formal={
                "type": "blowup_necessary",
                "conclusion": "L^3 norm blows up"
            },
            hypotheses=["ESS_L3"],
            source="ESS contrapositive",
            tags={"blowup", "ess", "necessary"}
        ))

        # =====================================================================
        # Necas-Ruzicka-Sverak (NRS)
        # =====================================================================

        self.add_statement(Statement(
            id="NRS_L3",
            name="NRS Self-Similar Exclusion",
            statement_type=StatementType.IMPLICATION,
            content="U in L^3(R^3) self-similar profile => U = 0",
            formal={
                "type": "liouville",
                "space": "L^3",
                "object": "self-similar profile",
                "conclusion": "trivial"
            },
            source="Necas-Ruzicka-Sverak, 1996",
            tags={"liouville", "self_similar", "nrs", "fundamental"}
        ))

        self.add_statement(Statement(
            id="NRS_WEAK_L3_OPEN",
            name="NRS Weak L^3 Gap",
            statement_type=StatementType.BOUND,
            content="U in L^{3,infty}(R^3) self-similar: STATUS OPEN",
            formal={
                "type": "open_problem",
                "space": "L^{3,infty}",
                "status": "open"
            },
            confidence=0.0,  # Open problem
            source="Open problem",
            tags={"open", "self_similar", "weak_L3", "gap"}
        ))

        # =====================================================================
        # Type I/II Classification
        # =====================================================================

        self.add_statement(Statement(
            id="TYPE_I_DEF",
            name="Type I Blowup Definition",
            statement_type=StatementType.DEFINITION,
            content="||u||_infty <= C/(T-t)^{1/2} (self-similar rate)",
            formal={
                "type": "blowup_rate",
                "rate": "1/2",
                "classification": "Type I"
            },
            tags={"type_I", "definition", "blowup_rate"}
        ))

        self.add_statement(Statement(
            id="TYPE_II_DEF",
            name="Type II Blowup Definition",
            statement_type=StatementType.DEFINITION,
            content="||u||_infty * (T-t)^{1/2} -> infty (faster than self-similar)",
            formal={
                "type": "blowup_rate",
                "classification": "Type II"
            },
            tags={"type_II", "definition", "blowup_rate"}
        ))

        self.add_statement(Statement(
            id="TYPE_I_RULED_OUT",
            name="Type I Ruled Out",
            statement_type=StatementType.IMPLICATION,
            content="Type I blowup => contradiction (Seregin 2012)",
            formal={
                "type": "exclusion",
                "excluded": "Type I blowup",
                "reason": "implies u in L^3_loc, then ESS applies"
            },
            hypotheses=["ESS_L3"],
            source="Seregin, 2012",
            tags={"type_I", "ruled_out", "seregin"}
        ))

        self.add_statement(Statement(
            id="TYPE_II_WINDOW",
            name="Type II Window",
            statement_type=StatementType.BOUND,
            content="If blowup exists, rate alpha in [1/2, 3/4) with ||u||_infty ~ (T-t)^{-alpha}",
            formal={
                "type": "rate_constraint",
                "lower": "1/2",
                "upper": "3/4",
                "reason_lower": "BKM",
                "reason_upper": "energy dissipation"
            },
            hypotheses=["BKM_CRITERION", "ENERGY_DECAY"],
            source="Analysis synthesis",
            tags={"type_II", "window", "blowup_rate", "gap"}
        ))

        # =====================================================================
        # Seregin's Condition (1.4)
        # =====================================================================

        self.add_statement(Statement(
            id="SEREGIN_14",
            name="Seregin Condition (1.4)",
            statement_type=StatementType.IMPLICATION,
            content="If A_{m_1}(r) + E_m(r) + D_m(r) bounded for m in (1/2, 3/5) => regularity",
            formal={
                "type": "regularity_criterion",
                "quantities": ["A_{m_1}", "E_m", "D_m"],
                "range": "(1/2, 3/5)",
                "conclusion": "regularity"
            },
            source="Seregin, 2025 (arXiv:2507.08733)",
            tags={"seregin", "regularity_criterion", "type_II"}
        ))

        self.add_statement(Statement(
            id="SEREGIN_Am1",
            name="Weighted Velocity Norm A_{m_1}",
            statement_type=StatementType.DEFINITION,
            content="A_{m_1}(r) = r^{1-2m} sup_t int_{B(r)} |u|^2 dx",
            formal={
                "type": "weighted_norm",
                "weight": "r^{1-2m}",
                "base_norm": "sup_t L^2(B(r))"
            },
            tags={"seregin", "definition", "weighted"}
        ))

        self.add_statement(Statement(
            id="SEREGIN_Em",
            name="Weighted Dissipation E_m",
            statement_type=StatementType.DEFINITION,
            content="E_m(r) = r^{-m} int_{Q(r)} |nabla u|^2 dz",
            formal={
                "type": "weighted_dissipation",
                "weight": "r^{-m}",
                "base": "L^2_t,x(Q(r)) of nabla u"
            },
            tags={"seregin", "definition", "dissipation", "weighted"}
        ))

        # =====================================================================
        # Target Statement
        # =====================================================================

        self.add_statement(Statement(
            id="TARGET_LOCAL_DECAY",
            name="Target: Local L^2 Decay",
            statement_type=StatementType.DECAY,
            content="||u||_{L^2(B(r))} <= C r^beta with beta > 0.05",
            formal={
                "type": "decay_estimate",
                "norm": NormSpec("L^2", "B(r)", "u"),
                "decay_rate": "beta",
                "threshold": 0.05
            },
            confidence=0.0,  # Target to prove
            tags={"target", "local", "decay"}
        ))

        # =====================================================================
        # Scaling Relations
        # =====================================================================

        self.add_statement(Statement(
            id="SCALING_NS",
            name="NS Scaling Symmetry",
            statement_type=StatementType.SCALING,
            content="u_lambda(x,t) = lambda u(lambda x, lambda^2 t) is a solution if u is",
            formal={
                "type": "scaling_symmetry",
                "transformations": {
                    "x": "lambda x",
                    "t": "lambda^2 t",
                    "u": "lambda^{-1} u",
                    "p": "lambda^{-2} p",
                    "omega": "lambda^{-2} omega"
                }
            },
            source="NS structure",
            tags={"scaling", "symmetry", "fundamental"}
        ))

        self.add_statement(Statement(
            id="SCALE_CRITICAL_L3",
            name="L^3 is Scale-Critical",
            statement_type=StatementType.SCALING,
            content="||u||_{L^3} is invariant under NS scaling",
            formal={
                "type": "scale_critical_norm",
                "space": "L^3",
                "scaling_dimension": 0
            },
            hypotheses=["SCALING_NS"],
            tags={"scaling", "critical", "L3"}
        ))

        # =====================================================================
        # Local Energy Inequality
        # =====================================================================

        self.add_statement(Statement(
            id="LOCAL_ENERGY_INEQ",
            name="Local Energy Inequality",
            statement_type=StatementType.INEQUALITY,
            content="int |u|^2 phi dx |_{t2} + 2nu int int |nabla u|^2 phi <= int |u|^2 phi |_{t1} + transport terms",
            formal={
                "type": "local_energy",
                "form": "integral_inequality",
                "test_function": "phi >= 0"
            },
            source="CKN, 1982",
            tags={"energy", "local", "ckn"}
        ))

        # =====================================================================
        # Interpolation Results
        # =====================================================================

        self.add_statement(Statement(
            id="INTERP_L2_LINF",
            name="L^2-L^infty Interpolation for Velocity",
            statement_type=StatementType.BOUND,
            content="||u||_{L^3} <= ||u||_{L^2}^{2/3} ||u||_{L^infty}^{1/3}",
            formal={
                "type": "interpolation",
                "target": "L^3",
                "sources": ["L^2", "L^infty"],
                "exponents": [2/3, 1/3]
            },
            hypotheses=["HOLDER_INTERP"],
            tags={"interpolation", "velocity"}
        ))

        self.add_statement(Statement(
            id="INTERP_GRADIENT_HOLDER",
            name="Gradient Interpolation",
            statement_type=StatementType.BOUND,
            content="||nabla u||_{L^2}^2 >= c ||u||_{L^infty}^{4/3} ||u||_{L^2}^{2/3}",
            formal={
                "type": "nash_inequality",
                "lower_bound": True
            },
            source="Nash inequality variant",
            tags={"interpolation", "gradient", "nash"}
        ))

    def export_to_dict(self) -> Dict:
        """Export knowledge base to dictionary for serialization."""
        return {
            "statements": [
                {
                    "id": s.id,
                    "name": s.name,
                    "type": s.statement_type.name,
                    "content": s.content,
                    "hypotheses": s.hypotheses,
                    "source": s.source,
                    "confidence": s.confidence,
                    "tags": list(s.tags)
                }
                for s in self.statements.values()
            ]
        }

    def summary(self) -> str:
        """Generate summary of knowledge base."""
        lines = ["=" * 70]
        lines.append("NAVIER-STOKES KNOWLEDGE BASE")
        lines.append("=" * 70)

        for stype in StatementType:
            stmts = self.by_type[stype]
            if stmts:
                lines.append(f"\n{stype.name} ({len(stmts)} statements):")
                lines.append("-" * 40)
                for sid in stmts[:5]:  # Show first 5
                    s = self.statements[sid]
                    lines.append(f"  [{s.id}] {s.name}")
                if len(stmts) > 5:
                    lines.append(f"  ... and {len(stmts) - 5} more")

        lines.append(f"\nTotal statements: {len(self.statements)}")
        lines.append(f"Tags: {sorted(self.by_tag.keys())}")

        return "\n".join(lines)


# =============================================================================
# Part 3: Inference Rules
# =============================================================================

@dataclass
class InferenceStep:
    """A single step in a proof."""
    rule_name: str
    inputs: List[str]       # Statement IDs used
    output: Statement       # New statement produced
    justification: str

    def __repr__(self) -> str:
        return f"{self.rule_name}: {self.inputs} => {self.output.id}"


class InferenceRule:
    """Base class for inference rules."""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def applicable(self, kb: KnowledgeBase, current: Set[str]) -> List[Tuple[List[str], Statement]]:
        """
        Find all ways this rule can be applied given current statements.

        Returns: List of (input_ids, new_statement) pairs
        """
        raise NotImplementedError

    def apply(self, inputs: List[Statement]) -> Optional[Statement]:
        """Apply the rule to given inputs, return new statement if applicable."""
        raise NotImplementedError


class SubstitutionRule(InferenceRule):
    """
    Substitute an identity into another statement.

    If we have A = B and C(A), derive C(B).
    """

    def __init__(self):
        super().__init__(
            "Substitution",
            "Replace equals with equals in a statement"
        )

    def applicable(self, kb: KnowledgeBase, current: Set[str]) -> List[Tuple[List[str], Statement]]:
        results = []

        # Find identities
        identities = [kb.get(sid) for sid in current
                     if kb.get(sid).statement_type == StatementType.IDENTITY]

        for identity in identities:
            # Try substituting into other statements
            for sid in current:
                stmt = kb.get(sid)
                if stmt.id == identity.id:
                    continue

                # Check if identity's LHS appears in statement
                # Simplified check - in real system would do proper term matching
                if identity.formal.get("type") == "biot_savart":
                    # Can substitute u = K * omega
                    if "velocity" in stmt.tags or "u" in stmt.content:
                        new_stmt = self._substitute_biot_savart(stmt, identity)
                        if new_stmt:
                            results.append(([identity.id, stmt.id], new_stmt))

        return results

    def _substitute_biot_savart(self, stmt: Statement, bs: Statement) -> Optional[Statement]:
        """Substitute Biot-Savart into a statement."""
        if "velocity" not in stmt.tags:
            return None

        new_id = f"{stmt.id}_BS_SUB"
        new_content = stmt.content.replace("u", "(K * omega)")

        return Statement(
            id=new_id,
            name=f"{stmt.name} (Biot-Savart form)",
            statement_type=stmt.statement_type,
            content=new_content,
            formal={**stmt.formal, "biot_savart_applied": True},
            hypotheses=stmt.hypotheses + [bs.id],
            source="Substitution",
            tags=stmt.tags | {"biot_savart_form"}
        )


class InequalityChainRule(InferenceRule):
    """
    Chain inequalities: A <= B and B <= C implies A <= C.
    """

    def __init__(self):
        super().__init__(
            "Inequality Chain",
            "Combine inequalities transitively"
        )

    def applicable(self, kb: KnowledgeBase, current: Set[str]) -> List[Tuple[List[str], Statement]]:
        results = []

        bounds = [kb.get(sid) for sid in current
                 if kb.get(sid).statement_type in [StatementType.BOUND, StatementType.INEQUALITY]]

        for b1 in bounds:
            for b2 in bounds:
                if b1.id == b2.id:
                    continue

                # Check if they can be chained
                chained = self._try_chain(b1, b2)
                if chained:
                    results.append(([b1.id, b2.id], chained))

        return results

    def _try_chain(self, b1: Statement, b2: Statement) -> Optional[Statement]:
        """Try to chain two bounds."""
        f1 = b1.formal
        f2 = b2.formal

        # Check if b1's RHS matches b2's LHS
        if f1.get("type") == "norm_bound" and f2.get("type") == "norm_bound":
            # e.g., ||u||_6 <= C||nabla u||_2 and ||nabla u||_2 <= ...
            rhs1 = f1.get("rhs", {})
            lhs2 = f2.get("lhs")

            if isinstance(rhs1, dict) and isinstance(lhs2, NormSpec):
                if rhs1.get("norm") == lhs2:
                    # Can chain!
                    new_id = f"CHAIN_{b1.id}_{b2.id}"
                    return Statement(
                        id=new_id,
                        name=f"Chained: {b1.name} + {b2.name}",
                        statement_type=StatementType.BOUND,
                        content=f"{b1.content} AND {b2.content}",
                        formal={"type": "chained_bound", "from": [b1.id, b2.id]},
                        hypotheses=[b1.id, b2.id],
                        source="Inequality chaining",
                        tags=b1.tags | b2.tags | {"derived", "chained"}
                    )

        return None


class ScalingAnalysisRule(InferenceRule):
    """
    Apply scaling analysis to derive dimensionally consistent bounds.
    """

    def __init__(self):
        super().__init__(
            "Scaling Analysis",
            "Use NS scaling to derive dimension constraints"
        )

    def applicable(self, kb: KnowledgeBase, current: Set[str]) -> List[Tuple[List[str], Statement]]:
        results = []

        scaling = kb.get("SCALING_NS")
        if scaling is None or "SCALING_NS" not in current:
            return results

        for sid in current:
            stmt = kb.get(sid)
            if stmt.statement_type in [StatementType.BOUND, StatementType.DECAY]:
                scaled = self._apply_scaling(stmt, scaling)
                if scaled:
                    results.append(([stmt.id, "SCALING_NS"], scaled))

        return results

    def _apply_scaling(self, stmt: Statement, scaling: Statement) -> Optional[Statement]:
        """Apply scaling to a statement."""
        f = stmt.formal

        if f.get("type") == "decay_estimate":
            # For decay estimates, scaling gives constraints on exponents
            rate = f.get("decay_rate")
            if rate:
                new_id = f"{stmt.id}_SCALED"
                return Statement(
                    id=new_id,
                    name=f"{stmt.name} (scaling constraint)",
                    statement_type=StatementType.BOUND,
                    content=f"Scaling requires: {stmt.content}",
                    formal={**f, "scaling_analyzed": True},
                    hypotheses=[stmt.id, scaling.id],
                    source="Scaling analysis",
                    tags=stmt.tags | {"scaling_derived"}
                )

        return None


class LocalizationRule(InferenceRule):
    """
    Localize global estimates to balls B(r).
    """

    def __init__(self):
        super().__init__(
            "Localization",
            "Restrict estimates to ball B(r)"
        )

    def applicable(self, kb: KnowledgeBase, current: Set[str]) -> List[Tuple[List[str], Statement]]:
        results = []

        for sid in current:
            stmt = kb.get(sid)
            if stmt.statement_type == StatementType.BOUND:
                f = stmt.formal
                if f.get("type") == "norm_bound":
                    lhs = f.get("lhs")
                    if isinstance(lhs, NormSpec) and lhs.domain == "R^3":
                        localized = self._localize(stmt)
                        if localized:
                            results.append(([stmt.id], localized))

        return results

    def _localize(self, stmt: Statement) -> Optional[Statement]:
        """Localize a global bound to B(r)."""
        new_id = f"{stmt.id}_LOCAL"

        return Statement(
            id=new_id,
            name=f"{stmt.name} (localized to B(r))",
            statement_type=StatementType.BOUND,
            content=stmt.content.replace("R^3", "B(r)"),
            formal={**stmt.formal, "localized": True, "domain": "B(r)"},
            hypotheses=[stmt.id],
            source="Localization",
            tags=stmt.tags | {"local", "localized"}
        )


class ImplicationChainRule(InferenceRule):
    """
    Chain implications: A => B and B => C implies A => C.
    """

    def __init__(self):
        super().__init__(
            "Implication Chain",
            "Chain logical implications"
        )

    def applicable(self, kb: KnowledgeBase, current: Set[str]) -> List[Tuple[List[str], Statement]]:
        results = []

        implications = [kb.get(sid) for sid in current
                       if kb.get(sid).statement_type == StatementType.IMPLICATION]

        for i1 in implications:
            for i2 in implications:
                if i1.id == i2.id:
                    continue

                f1 = i1.formal
                f2 = i2.formal

                # Check if i1's conclusion matches i2's condition
                c1 = f1.get("conclusion", "")
                c2 = f2.get("condition", f2.get("excluded", ""))

                if c1 and c2 and (c1 in c2 or c2 in c1):
                    new_id = f"IMPL_CHAIN_{i1.id}_{i2.id}"
                    new_stmt = Statement(
                        id=new_id,
                        name=f"Chained: {i1.name} + {i2.name}",
                        statement_type=StatementType.IMPLICATION,
                        content=f"{f1.get('condition', i1.content)} => {f2.get('conclusion', i2.content)}",
                        formal={
                            "type": "implication",
                            "condition": f1.get("condition"),
                            "conclusion": f2.get("conclusion")
                        },
                        hypotheses=[i1.id, i2.id],
                        source="Implication chaining",
                        tags=i1.tags | i2.tags | {"derived", "chained"}
                    )
                    results.append(([i1.id, i2.id], new_stmt))

        return results


class InterpolationRule(InferenceRule):
    """
    Apply Holder/interpolation between known bounds.
    """

    def __init__(self):
        super().__init__(
            "Interpolation",
            "Interpolate between norms"
        )

    def applicable(self, kb: KnowledgeBase, current: Set[str]) -> List[Tuple[List[str], Statement]]:
        results = []

        # Find bounds that could be interpolated
        bounds = [kb.get(sid) for sid in current
                 if kb.get(sid).statement_type == StatementType.BOUND]

        # Check for L^2 and L^infty bounds to get L^3
        l2_bounds = [b for b in bounds if "L^2" in b.content or "L^2" in str(b.formal)]
        linf_bounds = [b for b in bounds if "L^infty" in b.content or "infty" in str(b.formal)]

        for l2 in l2_bounds:
            for linf in linf_bounds:
                if l2.id == linf.id:
                    continue

                new_id = f"INTERP_{l2.id}_{linf.id}"
                new_stmt = Statement(
                    id=new_id,
                    name=f"Interpolated L^3 from {l2.name} and {linf.name}",
                    statement_type=StatementType.BOUND,
                    content=f"||u||_{{L^3}} <= ||u||_{{L^2}}^{{2/3}} ||u||_{{L^infty}}^{{1/3}} using {l2.name}, {linf.name}",
                    formal={
                        "type": "interpolated_bound",
                        "target": "L^3",
                        "sources": [l2.id, linf.id]
                    },
                    hypotheses=[l2.id, linf.id, "HOLDER_INTERP"],
                    source="Holder interpolation",
                    tags={"interpolation", "derived", "L3"}
                )
                results.append(([l2.id, linf.id], new_stmt))

        return results


# =============================================================================
# Part 4: Proof Search Algorithm
# =============================================================================

@dataclass
class ProofNode:
    """A node in the proof search tree."""
    statements: Set[str]        # Current set of statement IDs
    depth: int
    history: List[InferenceStep]
    score: float                # Heuristic score (lower = better)

    def __lt__(self, other: 'ProofNode') -> bool:
        return self.score < other.score

    def __hash__(self) -> int:
        return hash(frozenset(self.statements))

    def __eq__(self, other) -> bool:
        return isinstance(other, ProofNode) and self.statements == other.statements


@dataclass
class ProofResult:
    """Result of a proof search."""
    success: bool
    target_id: str
    proof_tree: List[InferenceStep]
    explored_nodes: int
    max_depth_reached: int
    missing_lemmas: List[str]
    gap_analysis: str


class ProofSearchEngine:
    """
    Main proof search engine using BFS with heuristics.

    Searches for a path from known lemmas to the target statement.
    """

    def __init__(self, knowledge_base: Optional[KnowledgeBase] = None):
        self.kb = knowledge_base or KnowledgeBase()
        self.rules: List[InferenceRule] = [
            SubstitutionRule(),
            InequalityChainRule(),
            ScalingAnalysisRule(),
            LocalizationRule(),
            ImplicationChainRule(),
            InterpolationRule(),
        ]

        self.explored: Set[frozenset] = set()
        self.target_keywords = {"target", "local", "decay", "regularity"}

    def _compute_heuristic(self, node: ProofNode, target: Statement) -> float:
        """
        Compute heuristic score for a node.

        Lower score = more promising.

        Heuristics:
        1. Tag overlap with target
        2. Dimensional similarity
        3. Presence of key intermediate results
        """
        score = node.depth * 0.1  # Slight preference for shorter proofs

        # Tag overlap
        current_tags = set()
        for sid in node.statements:
            stmt = self.kb.get(sid)
            if stmt:
                current_tags |= stmt.tags

        target_tags = target.tags
        overlap = len(current_tags & target_tags)
        score -= overlap * 0.5  # Reward tag overlap

        # Presence of key results
        key_results = {"CKN_EPSILON", "ESS_L3", "SEREGIN_14", "LOCAL_ENERGY_INEQ"}
        key_present = len(node.statements & key_results)
        score -= key_present * 0.3

        # Has local bounds
        local_count = sum(1 for sid in node.statements
                        if "local" in (self.kb.get(sid).tags if self.kb.get(sid) else set()))
        score -= local_count * 0.2

        return score

    def _is_target_reached(self, node: ProofNode, target: Statement) -> bool:
        """Check if the target has been derived."""
        # Direct check
        if target.id in node.statements:
            return True

        # Check if we have a statement that implies the target
        for sid in node.statements:
            stmt = self.kb.get(sid)
            if stmt and stmt.statement_type == StatementType.IMPLICATION:
                f = stmt.formal
                if f.get("conclusion") == "regularity":
                    # We have a regularity criterion - check if conditions are met
                    condition = f.get("condition", "")
                    if "bounded" in condition.lower():
                        # Need to verify the bound
                        pass

        # Check for decay estimates that match target
        for sid in node.statements:
            stmt = self.kb.get(sid)
            if stmt and stmt.statement_type == StatementType.DECAY:
                f = stmt.formal
                if f.get("type") == "decay_estimate":
                    rate = f.get("decay_rate")
                    threshold = f.get("threshold")
                    if rate and threshold and float(threshold) >= 0.05:
                        return True

        return False

    def _dimension_filter(self, stmt: Statement) -> bool:
        """Filter out dimensionally inconsistent statements."""
        dim = stmt.dimension
        if dim is None:
            return True  # Allow if dimension not specified

        # Check for obvious inconsistencies
        # e.g., bounds should be dimensionless
        if stmt.statement_type == StatementType.BOUND:
            return dim.is_scale_critical() or dim == DIM_DIMENSIONLESS

        return True

    def search(self, target_id: str = "TARGET_LOCAL_DECAY",
               max_depth: int = 10,
               beam_width: int = 100,
               max_nodes: int = 10000) -> ProofResult:
        """
        Search for a proof of the target statement.

        Uses beam search with heuristics.
        """
        target = self.kb.get(target_id)
        if target is None:
            return ProofResult(
                success=False,
                target_id=target_id,
                proof_tree=[],
                explored_nodes=0,
                max_depth_reached=0,
                missing_lemmas=[f"Target {target_id} not in knowledge base"],
                gap_analysis="Target not found"
            )

        # Initialize with all confident statements (theorems, not conjectures)
        initial_statements = {
            sid for sid, stmt in self.kb.statements.items()
            if stmt.confidence == 1.0
        }

        initial_node = ProofNode(
            statements=initial_statements,
            depth=0,
            history=[],
            score=self._compute_heuristic(
                ProofNode(initial_statements, 0, [], 0), target
            )
        )

        # Priority queue for beam search
        frontier = [initial_node]
        heapq.heapify(frontier)

        self.explored = set()
        nodes_explored = 0
        max_depth_seen = 0

        while frontier and nodes_explored < max_nodes:
            # Get best node
            current = heapq.heappop(frontier)
            nodes_explored += 1
            max_depth_seen = max(max_depth_seen, current.depth)

            # Check if target reached
            if self._is_target_reached(current, target):
                return ProofResult(
                    success=True,
                    target_id=target_id,
                    proof_tree=current.history,
                    explored_nodes=nodes_explored,
                    max_depth_reached=max_depth_seen,
                    missing_lemmas=[],
                    gap_analysis="Proof found!"
                )

            # Check depth limit
            if current.depth >= max_depth:
                continue

            # Mark as explored
            state_key = frozenset(current.statements)
            if state_key in self.explored:
                continue
            self.explored.add(state_key)

            # Expand node by applying all rules
            new_nodes = self._expand(current, target)

            # Beam search: keep top-k
            for node in new_nodes:
                if frozenset(node.statements) not in self.explored:
                    heapq.heappush(frontier, node)

            # Prune to beam width
            if len(frontier) > beam_width:
                frontier = heapq.nsmallest(beam_width, frontier)
                heapq.heapify(frontier)

        # Search failed - analyze gaps
        gap_analysis, missing = self._analyze_gap(target)

        return ProofResult(
            success=False,
            target_id=target_id,
            proof_tree=[],
            explored_nodes=nodes_explored,
            max_depth_reached=max_depth_seen,
            missing_lemmas=missing,
            gap_analysis=gap_analysis
        )

    def _expand(self, node: ProofNode, target: Statement) -> List[ProofNode]:
        """Expand a node by applying all applicable rules."""
        new_nodes = []

        for rule in self.rules:
            try:
                applications = rule.applicable(self.kb, node.statements)

                for input_ids, new_stmt in applications:
                    # Add new statement to knowledge base if not present
                    if new_stmt.id not in self.kb.statements:
                        # Filter dimensionally inconsistent
                        if not self._dimension_filter(new_stmt):
                            continue
                        self.kb.add_statement(new_stmt)

                    # Create new node
                    new_statements = node.statements | {new_stmt.id}
                    step = InferenceStep(
                        rule_name=rule.name,
                        inputs=input_ids,
                        output=new_stmt,
                        justification=rule.description
                    )

                    new_node = ProofNode(
                        statements=new_statements,
                        depth=node.depth + 1,
                        history=node.history + [step],
                        score=0  # Will be computed below
                    )
                    new_node.score = self._compute_heuristic(new_node, target)

                    new_nodes.append(new_node)

            except Exception as e:
                # Skip failed rule applications
                continue

        return new_nodes

    def _analyze_gap(self, target: Statement) -> Tuple[str, List[str]]:
        """
        Analyze why the search failed and identify missing lemmas.
        """
        lines = []
        missing = []

        lines.append("=" * 70)
        lines.append("GAP ANALYSIS: Why Proof Search Failed")
        lines.append("=" * 70)

        # What we're trying to prove
        lines.append(f"\nTARGET: {target.content}")
        lines.append(f"Type: {target.statement_type.name}")

        # What would be needed
        lines.append("\nWHAT WOULD BE NEEDED:")

        target_formal = target.formal
        if target_formal.get("type") == "decay_estimate":
            rate = target_formal.get("decay_rate", "beta")
            threshold = target_formal.get("threshold", 0.05)

            lines.append(f"  1. A decay estimate ||u||_{{L^2(B(r))}} <= C r^{{{rate}}}")
            lines.append(f"     with {rate} > {threshold}")
            lines.append("")
            lines.append("  POSSIBLE PATHS:")

            # Path 1: Through CKN
            lines.append("  [Path A] CKN epsilon-regularity:")
            lines.append("    - Need: r^{-2} int_{Q(r)} (|u|^3 + |p|^{3/2}) < epsilon")
            lines.append("    - Have: Energy bound ||u||_{L^2} <= E_0^{1/2}")
            lines.append("    - GAP: Cannot control L^3 from L^2 without L^infty bound")
            missing.append("L^infty bound to interpolate L^2 -> L^3")

            # Path 2: Through Seregin
            lines.append("\n  [Path B] Seregin condition (1.4):")
            lines.append("    - Need: A_{m_1}(r) + E_m(r) + D_m(r) bounded for m in (1/2, 3/5)")
            lines.append("    - Have: Energy dissipation integral")
            lines.append("    - GAP: Weighted norms require more than energy")
            missing.append("Proof that Type II implies Seregin (1.4)")

            # Path 3: Through ESS
            lines.append("\n  [Path C] ESS backward uniqueness:")
            lines.append("    - Need: ||u||_{L^3} bounded near singularity")
            lines.append("    - Have: Energy bound gives ||u||_{L^2} bounded")
            lines.append("    - GAP: L^3 is critical, not controlled by subcritical L^2")
            missing.append("L^3 boundedness from Type II structure")

            # Path 4: Direct scaling
            lines.append("\n  [Path D] Direct scaling argument:")
            lines.append("    - Need: Rescaled solution converges strongly")
            lines.append("    - Have: Rescaled solution bounded in L^2")
            lines.append("    - GAP: Concentration allows weak but not strong convergence")
            missing.append("Exclusion of concentration (cascade prevention)")

        lines.append("\n" + "=" * 70)
        lines.append("MINIMAL MISSING LEMMA")
        lines.append("=" * 70)

        # Identify the minimal gap
        lines.append("\nThe MINIMAL statement that would complete a proof:")
        lines.append("")
        lines.append("  CONJECTURE (Gap-Closing Lemma):")
        lines.append("  For suitable weak solutions with Type II rate alpha in (1/2, 3/5):")
        lines.append("  ")
        lines.append("    limsup_{r -> 0} r^{-epsilon} ||u||_{L^2(B(r))} < infty")
        lines.append("    ")
        lines.append("  for some epsilon > 0.")
        lines.append("")
        lines.append("  WHY THIS SUFFICES:")
        lines.append("  - Gives decay ||u||_{L^2(B(r))} <= C r^epsilon")
        lines.append("  - Combined with dissipation: ||nabla u||_{L^2(B(r))} bounded")
        lines.append("  - Then CKN/Seregin conditions become verifiable")

        missing.append("epsilon-decay of local L^2 norm for Type II")

        lines.append("\n" + "=" * 70)
        lines.append("WHAT BLOCKS PROVING THE MISSING LEMMA")
        lines.append("=" * 70)
        lines.append("")
        lines.append("1. CONCENTRATION: Energy can concentrate at a point while")
        lines.append("   staying bounded in L^2 - no decay follows from energy alone")
        lines.append("")
        lines.append("2. DIMENSIONAL GAP: Energy and vorticity have different")
        lines.append("   dimensions. The gap alpha in (1/2, 3/5) is exactly where")
        lines.append("   neither energy nor vorticity arguments apply directly.")
        lines.append("")
        lines.append("3. NO MONOTONE QUANTITY: There is no known scale-critical")
        lines.append("   monotone quantity that would prevent concentration.")
        lines.append("")
        lines.append("4. BACKWARD METHODS: All known regularity arguments work")
        lines.append("   backward in time (uniqueness), not forward (prevention).")

        return "\n".join(lines), missing


# =============================================================================
# Part 5: Proof Tree Visualization
# =============================================================================

class ProofVisualizer:
    """Visualize proof trees and search results."""

    @staticmethod
    def format_proof_tree(steps: List[InferenceStep]) -> str:
        """Format a proof as a readable tree."""
        if not steps:
            return "Empty proof"

        lines = ["PROOF TREE", "=" * 50]

        for i, step in enumerate(steps, 1):
            lines.append(f"\nStep {i}: {step.rule_name}")
            lines.append(f"  Inputs: {step.inputs}")
            lines.append(f"  Output: {step.output.name}")
            lines.append(f"  Statement: {step.output.content}")
            if step.justification:
                lines.append(f"  Justification: {step.justification}")

        return "\n".join(lines)

    @staticmethod
    def format_search_result(result: ProofResult) -> str:
        """Format a search result for display."""
        lines = []

        lines.append("=" * 70)
        lines.append("PROOF SEARCH RESULT")
        lines.append("=" * 70)

        if result.success:
            lines.append("\nSTATUS: SUCCESS - Proof Found!")
        else:
            lines.append("\nSTATUS: FAILED - No Proof Found")

        lines.append(f"\nTarget: {result.target_id}")
        lines.append(f"Nodes explored: {result.explored_nodes}")
        lines.append(f"Max depth reached: {result.max_depth_reached}")

        if result.success:
            lines.append("\n" + ProofVisualizer.format_proof_tree(result.proof_tree))
        else:
            lines.append(f"\nMissing lemmas ({len(result.missing_lemmas)}):")
            for i, lemma in enumerate(result.missing_lemmas, 1):
                lines.append(f"  {i}. {lemma}")

        lines.append("\n" + result.gap_analysis)

        return "\n".join(lines)

    @staticmethod
    def export_dot(steps: List[InferenceStep], filename: str) -> str:
        """Export proof tree to DOT format for GraphViz."""
        lines = ["digraph ProofTree {"]
        lines.append("  rankdir=TB;")
        lines.append("  node [shape=box];")

        for i, step in enumerate(steps):
            node_id = f"step{i}"
            label = f"{step.rule_name}\\n{step.output.name}"
            lines.append(f'  {node_id} [label="{label}"];')

            for inp in step.inputs:
                inp_id = inp.replace("-", "_").replace(".", "_")
                lines.append(f"  {inp_id} -> {node_id};")

        lines.append("}")

        dot_content = "\n".join(lines)

        # Write to file
        with open(filename, 'w') as f:
            f.write(dot_content)

        return dot_content


# =============================================================================
# Part 6: Advanced Gap Detection
# =============================================================================

class GapDetector:
    """
    Detect and analyze gaps in the proof space.

    Identifies:
    1. Which lemmas are "almost" connected
    2. What type of statement would bridge gaps
    3. Structural reasons for gaps
    """

    def __init__(self, kb: KnowledgeBase):
        self.kb = kb

    def find_minimal_gap(self, source_tags: Set[str], target_tags: Set[str]) -> Dict:
        """Find the minimal lemma that would connect source to target."""

        # Find statements with source tags
        source_stmts = set()
        for tag in source_tags:
            source_stmts |= set(self.kb.by_tag.get(tag, []))

        # Find statements with target tags
        target_stmts = set()
        for tag in target_tags:
            target_stmts |= set(self.kb.by_tag.get(tag, []))

        # Find what's missing
        analysis = {
            "source_statements": list(source_stmts),
            "target_statements": list(target_stmts),
            "overlap": list(source_stmts & target_stmts),
            "missing_connection": []
        }

        # Identify bridging needs
        if not analysis["overlap"]:
            # Need a bridge
            source_types = set()
            target_types = set()

            for sid in source_stmts:
                s = self.kb.get(sid)
                if s:
                    source_types.add(s.statement_type)

            for sid in target_stmts:
                s = self.kb.get(sid)
                if s:
                    target_types.add(s.statement_type)

            if StatementType.BOUND in source_types and StatementType.IMPLICATION in target_types:
                analysis["missing_connection"].append(
                    "Need: Bound -> Implication connector (show bound implies condition)"
                )

            if StatementType.DECAY in target_types and StatementType.BOUND in source_types:
                analysis["missing_connection"].append(
                    "Need: Bound -> Decay converter (extract decay rate from bound)"
                )

        return analysis

    def structural_gap_analysis(self) -> str:
        """
        Analyze structural gaps in the knowledge base.

        Identifies fundamental mathematical obstacles.
        """
        lines = []

        lines.append("=" * 70)
        lines.append("STRUCTURAL GAP ANALYSIS")
        lines.append("=" * 70)

        # Gap 1: L^2 to L^3
        lines.append("\nGAP 1: L^2 -> L^3 Upgrade")
        lines.append("-" * 40)
        lines.append("We have: ||u||_{L^2} bounded (energy)")
        lines.append("We need: ||u||_{L^3} bounded (ESS critical)")
        lines.append("Obstacle: Interpolation requires L^infty, which is the blowup!")
        lines.append("Status: FUNDAMENTAL - cannot be closed by known methods")

        # Gap 2: Global to local
        lines.append("\nGAP 2: Global -> Local Decay")
        lines.append("-" * 40)
        lines.append("We have: ||u||_{L^2(R^3)} bounded")
        lines.append("We need: ||u||_{L^2(B(r))} <= C r^beta")
        lines.append("Obstacle: Concentration allows mass to pile up at origin")
        lines.append("Status: FUNDAMENTAL - energy conservation doesn't prevent concentration")

        # Gap 3: Type II window
        lines.append("\nGAP 3: Type II Window (1/2, 3/5)")
        lines.append("-" * 40)
        lines.append("Upper bound (1/2): BKM requires ||omega||_{L^1_t L^infty_x} = infty")
        lines.append("Lower bound (3/5): Energy scaling E ~ (T-t)^{3-5alpha} increasing for alpha > 3/5")
        lines.append("Obstacle: Different dimensions - vorticity vs energy")
        lines.append("Status: FUNDAMENTAL - requires new mathematics")

        # Gap 4: Cascade
        lines.append("\nGAP 4: Cascade Exclusion")
        lines.append("-" * 40)
        lines.append("We need: Prove energy cannot cascade infinitely to smaller scales")
        lines.append("We have: Energy decreases globally, but can redistribute locally")
        lines.append("Obstacle: No monotone local quantity")
        lines.append("Status: FUNDAMENTAL - touches essence of turbulence")

        return "\n".join(lines)


# =============================================================================
# Part 7: Main Interface
# =============================================================================

def run_proof_search(verbose: bool = True) -> ProofResult:
    """
    Run the proof search engine.

    Returns the search result with proof tree or gap analysis.
    """
    # Initialize
    kb = KnowledgeBase()
    engine = ProofSearchEngine(kb)

    if verbose:
        print(kb.summary())
        print("\n" + "=" * 70)
        print("STARTING PROOF SEARCH")
        print("=" * 70)
        print(f"Target: ||u||_{{L^2(B(r))}} <= C r^beta with beta > 0.05")
        print("=" * 70 + "\n")

    # Run search
    result = engine.search(
        target_id="TARGET_LOCAL_DECAY",
        max_depth=8,
        beam_width=50,
        max_nodes=5000
    )

    if verbose:
        print(ProofVisualizer.format_search_result(result))

    return result


def run_gap_analysis(verbose: bool = True) -> str:
    """Run comprehensive gap analysis."""
    kb = KnowledgeBase()
    detector = GapDetector(kb)

    analysis = detector.structural_gap_analysis()

    if verbose:
        print(analysis)

    return analysis


def export_knowledge_base(filename: str = "ns_knowledge_base.json") -> None:
    """Export knowledge base to JSON."""
    kb = KnowledgeBase()
    data = kb.export_to_dict()

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Exported {len(data['statements'])} statements to {filename}")


# =============================================================================
# Main Entry Point
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("NAVIER-STOKES PROOF SEARCH ENGINE")
    print("Symbolic exploration of the regularity problem")
    print("=" * 70)
    print()

    # Run the search
    result = run_proof_search(verbose=True)

    print("\n\n")

    # Run gap analysis
    run_gap_analysis(verbose=True)

    print("\n" + "=" * 70)
    print("SEARCH COMPLETE")
    print("=" * 70)
    print(f"Proof found: {result.success}")
    print(f"Nodes explored: {result.explored_nodes}")
    print(f"Max depth: {result.max_depth_reached}")
    print(f"Missing lemmas: {len(result.missing_lemmas)}")

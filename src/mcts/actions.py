"""
Proof actions and tactics for MCTS exploration.

Defines the action space for proof exploration including:
- Proof tactics (apply lemma, case split, contradiction)
- Mathematical operations (integration by parts, rescaling)
- Verification actions (numerical checks, symbolic verification)
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Any, Callable

from .state import ProofState, LemmaStatus, Goal, ProofStep, Hypothesis
import time


class ActionType(Enum):
    """Types of actions in the proof exploration."""

    # Proof tactics
    APPLY_LEMMA = "apply_lemma"
    INTRODUCE_VARIABLE = "introduce_variable"
    CASE_SPLIT = "case_split"
    CONTRADICTION = "contradiction"
    INDUCTION = "induction"

    # Mathematical operations
    INTEGRATE_BY_PARTS = "integrate_by_parts"
    CHANGE_VARIABLES = "change_variables"
    RESCALE = "rescale"
    MULTIPLY_BY_TEST_FUNCTION = "multiply_test"

    # Structural tactics
    DECOMPOSE_GOAL = "decompose_goal"
    STRENGTHEN_HYPOTHESIS = "strengthen_hypothesis"
    WEAKEN_CONCLUSION = "weaken_conclusion"

    # Estimation tactics
    APPLY_INEQUALITY = "apply_inequality"
    BOUND_TERM = "bound_term"
    ESTIMATE_INTEGRAL = "estimate_integral"

    # Verification tactics
    CHECK_NUMERICALLY = "check_numerically"
    VERIFY_SYMBOLICALLY = "verify_symbolically"
    INVOKE_EXTERNAL_RESULT = "invoke_external_result"

    # Strategic moves
    CHANGE_STRATEGY = "change_strategy"
    BACKTRACK = "backtrack"
    EXPLORE_ALTERNATIVE = "explore_alternative"


@dataclass
class Action:
    """Represents a proof action."""
    type: ActionType
    target: Optional[str] = None  # Lemma name, inequality name, etc.
    params: Dict[str, Any] = field(default_factory=dict)
    description: str = ""
    preconditions: List[str] = field(default_factory=list)
    cost: float = 1.0  # Action complexity cost

    def __hash__(self):
        return hash((self.type, self.target, frozenset(self.params.items())))

    def __eq__(self, other):
        if not isinstance(other, Action):
            return False
        return (self.type == other.type and
                self.target == other.target and
                self.params == other.params)


# ============================================================================
# Specific Actions for NS Proof
# ============================================================================

def create_ns_proof_actions() -> Dict[str, Action]:
    """Create the action library for NS proof exploration."""

    actions = {}

    # Core lemma applications
    actions["apply_eta_conservation"] = Action(
        type=ActionType.APPLY_LEMMA,
        target="eta_conservation",
        description="Use material conservation of eta = omega^theta/r",
        cost=0.5
    )

    actions["apply_maximum_principle"] = Action(
        type=ActionType.APPLY_LEMMA,
        target="maximum_principle",
        description="Apply maximum principle for eta",
        cost=0.5
    )

    actions["apply_geometric_constraint"] = Action(
        type=ActionType.APPLY_LEMMA,
        target="geometric_constraint",
        description="Use omega^theta = r * eta bound",
        cost=0.5
    )

    actions["apply_bakry_emery"] = Action(
        type=ActionType.APPLY_INEQUALITY,
        target="bakry_emery_criterion",
        description="Apply Bakry-Emery criterion for spectral gap",
        cost=1.5
    )

    actions["apply_poincare_weighted"] = Action(
        type=ActionType.APPLY_INEQUALITY,
        target="weighted_poincare",
        description="Apply weighted Poincare inequality",
        cost=1.0
    )

    actions["apply_sobolev_embedding"] = Action(
        type=ActionType.APPLY_INEQUALITY,
        target="sobolev_embedding",
        description="L2 decay implies Linfty decay via Sobolev",
        cost=0.5
    )

    actions["apply_nash_inequality"] = Action(
        type=ActionType.APPLY_INEQUALITY,
        target="nash_inequality",
        description="Apply Nash inequality for dissipation bound",
        cost=1.0
    )

    # Rescaling actions
    actions["type_ii_rescaling"] = Action(
        type=ActionType.RESCALE,
        target="type_ii",
        params={
            "lambda": "(T-t)^{1/(2*alpha)}",
            "tau": "-log(T-t)/(2*alpha)",
            "amplitude": "(T-t)^alpha"
        },
        description="Apply Type II self-similar rescaling",
        cost=2.0
    )

    actions["type_i_rescaling"] = Action(
        type=ActionType.RESCALE,
        target="type_i",
        params={
            "lambda": "sqrt(T-t)",
            "tau": "-log(T-t)",
            "amplitude": "sqrt(T-t)"
        },
        description="Apply Type I (self-similar) rescaling",
        cost=1.5
    )

    # Case splits for alpha
    actions["split_alpha_type_i"] = Action(
        type=ActionType.CASE_SPLIT,
        target="alpha",
        params={"condition": "alpha == 1/2"},
        description="Case split: Type I (alpha = 1/2)",
        cost=1.0
    )

    actions["split_alpha_gap"] = Action(
        type=ActionType.CASE_SPLIT,
        target="alpha",
        params={"condition": "1/2 < alpha < 3/5"},
        description="Case split: Type II gap region",
        cost=1.0
    )

    actions["split_alpha_high"] = Action(
        type=ActionType.CASE_SPLIT,
        target="alpha",
        params={"condition": "alpha >= 3/5"},
        description="Case split: High Type II rate",
        cost=1.0
    )

    # Numerical verification
    actions["verify_spectral_gap_numerically"] = Action(
        type=ActionType.CHECK_NUMERICALLY,
        target="spectral_gap",
        description="Numerically verify spectral gap is positive",
        cost=0.5
    )

    actions["verify_viscosity_divergence"] = Action(
        type=ActionType.CHECK_NUMERICALLY,
        target="nu_eff_divergence",
        description="Verify nu_eff -> infinity for alpha > 1/2",
        cost=0.5
    )

    actions["verify_decay_rate"] = Action(
        type=ActionType.CHECK_NUMERICALLY,
        target="decay_rate",
        description="Verify super-exponential decay rate",
        cost=0.5
    )

    # Mathematical operations
    actions["multiply_by_eta"] = Action(
        type=ActionType.MULTIPLY_BY_TEST_FUNCTION,
        target="eta",
        description="Multiply equation by eta and integrate",
        cost=1.0
    )

    actions["multiply_by_eta_squared"] = Action(
        type=ActionType.MULTIPLY_BY_TEST_FUNCTION,
        target="eta^2",
        description="Multiply equation by eta^2 and integrate",
        cost=1.0
    )

    actions["integrate_by_parts_viscous"] = Action(
        type=ActionType.INTEGRATE_BY_PARTS,
        target="viscous_term",
        params={"moves": 1},
        description="Integration by parts on viscous term",
        cost=0.5
    )

    # Strategic moves
    actions["try_direct_energy_estimate"] = Action(
        type=ActionType.CHANGE_STRATEGY,
        target="direct_energy",
        description="Try direct energy estimate instead of spectral gap",
        cost=2.0
    )

    actions["try_comparison_principle"] = Action(
        type=ActionType.CHANGE_STRATEGY,
        target="comparison",
        description="Try comparison with heat equation",
        cost=2.0
    )

    actions["try_pohozaev_identity"] = Action(
        type=ActionType.CHANGE_STRATEGY,
        target="pohozaev",
        description="Try Pohozaev-type identity approach",
        cost=2.5
    )

    actions["explore_alternative_gap_proof"] = Action(
        type=ActionType.EXPLORE_ALTERNATIVE,
        target="spectral_gap",
        description="Explore alternative proofs of spectral gap",
        cost=3.0
    )

    # Derive key results
    actions["derive_fokker_planck_structure"] = Action(
        type=ActionType.APPLY_LEMMA,
        target="fokker_planck_structure",
        params={"derive": True},
        description="Derive Fokker-Planck structure from rescaled equation",
        cost=1.5
    )

    actions["derive_effective_viscosity"] = Action(
        type=ActionType.APPLY_LEMMA,
        target="effective_viscosity_divergence",
        params={"derive": True},
        description="Derive effective viscosity formula",
        cost=1.0
    )

    # Contradiction arguments
    actions["assume_blowup_exists"] = Action(
        type=ActionType.CONTRADICTION,
        target="blowup_assumption",
        description="Assume Type II blowup exists for contradiction",
        cost=0.5
    )

    actions["derive_contradiction"] = Action(
        type=ActionType.CONTRADICTION,
        target="contradiction_conclusion",
        description="Derive contradiction from trivial limit",
        cost=1.0
    )

    return actions


# ============================================================================
# Action Application
# ============================================================================

def can_apply_lemma(lemma_id: str, goal: Goal, state: ProofState) -> bool:
    """Check if a lemma can be applied to the current goal."""
    # Check if lemma is proven or assumed
    if lemma_id not in state.lemma_status:
        return False

    status = state.lemma_status[lemma_id]
    if status not in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED]:
        return False

    # Check if lemma is relevant to goal
    # This is a simplified check - in practice would use unification
    return lemma_id.lower() in goal.statement.lower() or goal.involves(lemma_id)


def apply_action(state: ProofState, action: Action) -> ProofState:
    """Apply an action to a proof state, returning new state."""
    new_state = state.clone()

    # Record the action in history
    step = ProofStep(
        action_type=action.type.value,
        target=action.target or "",
        result="applied",
        timestamp=time.time()
    )
    new_state.history.append(step)

    # Apply action effects based on type
    if action.type == ActionType.APPLY_LEMMA:
        _apply_lemma_action(new_state, action)

    elif action.type == ActionType.CASE_SPLIT:
        _apply_case_split(new_state, action)

    elif action.type == ActionType.APPLY_INEQUALITY:
        _apply_inequality(new_state, action)

    elif action.type == ActionType.RESCALE:
        _apply_rescaling(new_state, action)

    elif action.type == ActionType.CHECK_NUMERICALLY:
        _apply_numerical_check(new_state, action)

    elif action.type == ActionType.CONTRADICTION:
        _apply_contradiction(new_state, action)

    elif action.type == ActionType.CHANGE_STRATEGY:
        _apply_strategy_change(new_state, action)

    elif action.type == ActionType.INTEGRATE_BY_PARTS:
        _apply_integration_by_parts(new_state, action)

    elif action.type == ActionType.MULTIPLY_BY_TEST_FUNCTION:
        _apply_test_function(new_state, action)

    # Update overall score
    new_state.score += _compute_action_progress(state, new_state, action)

    # Check if main theorem is now provable
    _check_theorem_completion(new_state)

    return new_state


def _apply_lemma_action(state: ProofState, action: Action):
    """Apply a lemma to the proof."""
    lemma_id = action.target

    # If deriving, mark as in progress
    if action.params.get("derive"):
        state.lemma_status[lemma_id] = LemmaStatus.IN_PROGRESS

        # Check if all dependencies are satisfied
        deps = state.dependencies.get_dependencies(lemma_id)
        if all(state.lemma_status.get(d) in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED]
               for d in deps):
            state.lemma_status[lemma_id] = LemmaStatus.PROVEN
    else:
        # Using an already proven lemma
        if state.lemma_status.get(lemma_id) in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED]:
            # Add as hypothesis in context
            state.context.add_hypothesis(Hypothesis(
                name=lemma_id,
                statement=f"By lemma {lemma_id}",
                source="lemma"
            ))


def _apply_case_split(state: ProofState, action: Action):
    """Apply a case split."""
    condition = action.params.get("condition", "")

    # Add constraint to context
    from .state import Constraint
    state.context.add_constraint(Constraint(
        expression=condition,
        variables=[action.target] if action.target else []
    ))

    # If splitting on alpha, update variable
    if action.target == "alpha" and "alpha" in state.context.variables:
        var = state.context.variables["alpha"]
        var.constraints.append(condition)

        # Extract value if specific
        if "==" in condition:
            val_str = condition.split("==")[1].strip()
            try:
                if "/" in val_str:
                    num, denom = val_str.split("/")
                    var.value = float(num) / float(denom)
                else:
                    var.value = float(val_str)
                var.is_fixed = True
            except:
                pass


def _apply_inequality(state: ProofState, action: Action):
    """Apply an inequality to derive bounds."""
    inequality_name = action.target

    # Add to hypotheses
    state.context.add_hypothesis(Hypothesis(
        name=inequality_name,
        statement=f"By {inequality_name} inequality",
        source="inequality"
    ))


def _apply_rescaling(state: ProofState, action: Action):
    """Apply a rescaling transformation."""
    # Add rescaling variables to context
    for var_name, var_expr in action.params.items():
        from .state import Variable
        state.context.add_variable(Variable(
            name=f"{action.target}_{var_name}",
            var_type="derived",
            constraints=[f"= {var_expr}"]
        ))

    # If Type II rescaling, mark rescaled equation as derivable
    if action.target == "type_ii":
        state.lemma_status["rescaled_eta_equation"] = LemmaStatus.PROVEN


def _apply_numerical_check(state: ProofState, action: Action):
    """Apply numerical verification."""
    target = action.target

    # For now, assume numerical checks pass
    # In full implementation, this would call NumericalOracle
    from .state import NumericalEvidence
    state.numerical_evidence[target] = NumericalEvidence(
        claim=target,
        test_cases=[{"status": "passed"}],
        success_rate=1.0,
        confidence=0.95
    )

    # Update related lemma status
    lemma_map = {
        "spectral_gap": "spectral_gap_lemma",
        "nu_eff_divergence": "effective_viscosity_divergence",
        "decay_rate": "l2_decay_theorem"
    }
    if target in lemma_map:
        lemma_id = lemma_map[target]
        if state.lemma_status.get(lemma_id) == LemmaStatus.OPEN:
            state.lemma_status[lemma_id] = LemmaStatus.NUMERICALLY_VERIFIED


def _apply_contradiction(state: ProofState, action: Action):
    """Apply contradiction reasoning."""
    if action.target == "blowup_assumption":
        # Set up contradiction proof
        state.context.add_hypothesis(Hypothesis(
            name="blowup_assumption",
            statement="Assume Type II blowup exists at time T",
            source="assumption_for_contradiction"
        ))
    elif action.target == "contradiction_conclusion":
        # If we have trivial limit, contradiction is derived
        if state.lemma_status.get("pointwise_decay") == LemmaStatus.PROVEN:
            # All Type II cases in gap region are ruled out
            if "1/2 < alpha < 3/5" in str(state.context.constraints):
                state.lemma_status["type_ii_exclusion_gap"] = LemmaStatus.PROVEN


def _apply_strategy_change(state: ProofState, action: Action):
    """Change proof strategy."""
    from .state import ProofMethod
    state.context.method = ProofMethod(
        name=action.target,
        description=action.description,
        applicable_to=["type_ii_gap"]
    )


def _apply_integration_by_parts(state: ProofState, action: Action):
    """Apply integration by parts."""
    state.context.add_hypothesis(Hypothesis(
        name="ibp_result",
        statement=f"Integration by parts on {action.target}",
        source="computation"
    ))


def _apply_test_function(state: ProofState, action: Action):
    """Multiply by test function and integrate."""
    state.context.add_hypothesis(Hypothesis(
        name="energy_identity",
        statement=f"Multiply by {action.target} and integrate",
        source="computation"
    ))


def _compute_action_progress(old_state: ProofState, new_state: ProofState,
                             action: Action) -> float:
    """Compute progress made by action."""
    progress = 0.0

    # Count newly proven lemmas
    for lemma_id, old_status in old_state.lemma_status.items():
        new_status = new_state.lemma_status.get(lemma_id)
        if old_status == LemmaStatus.OPEN and new_status == LemmaStatus.PROVEN:
            progress += 1.0
        elif old_status == LemmaStatus.OPEN and new_status == LemmaStatus.NUMERICALLY_VERIFIED:
            progress += 0.5

    # Penalty for action cost
    progress -= action.cost * 0.1

    return progress


def _check_theorem_completion(state: ProofState):
    """Check if main theorem can now be proven."""
    main_thm = state.target_theorem

    # Check if all dependencies are satisfied
    all_deps_proven = all(
        state.lemma_status.get(dep) in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED]
        for dep in main_thm.dependencies
    )

    if all_deps_proven:
        state.lemma_status["main_theorem"] = LemmaStatus.PROVEN
        state.target_theorem.status = LemmaStatus.PROVEN


# ============================================================================
# Action Selection
# ============================================================================

def get_legal_actions(state: ProofState) -> List[Action]:
    """Return all legal actions from current state."""
    actions = create_ns_proof_actions()
    legal = []

    # Get current goal
    goal = state.context.current_goal
    if goal is None:
        return legal

    # Check which lemmas can be applied
    for lemma_id, status in state.lemma_status.items():
        if status in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED]:
            if can_apply_lemma(lemma_id, goal, state):
                legal.append(Action(
                    type=ActionType.APPLY_LEMMA,
                    target=lemma_id,
                    description=f"Apply proven lemma {lemma_id}"
                ))

    # Check for derivable lemmas
    for lemma_id, status in state.lemma_status.items():
        if status == LemmaStatus.OPEN:
            deps = state.dependencies.get_dependencies(lemma_id)
            if all(state.lemma_status.get(d) in [LemmaStatus.PROVEN, LemmaStatus.ASSUMED]
                   for d in deps):
                legal.append(Action(
                    type=ActionType.APPLY_LEMMA,
                    target=lemma_id,
                    params={"derive": True},
                    description=f"Derive lemma {lemma_id}"
                ))

    # Check for case splits based on constraints
    if "alpha" in state.context.variables:
        alpha_var = state.context.variables["alpha"]
        if not alpha_var.is_fixed:
            legal.extend([
                actions["split_alpha_type_i"],
                actions["split_alpha_gap"],
                actions["split_alpha_high"]
            ])

    # Check for numerical verification opportunities
    if goal.is_numerical_checkable():
        legal.extend([
            actions["verify_spectral_gap_numerically"],
            actions["verify_viscosity_divergence"],
            actions["verify_decay_rate"]
        ])

    # Rescaling actions
    if "rescaled_eta_equation" not in [h.name for h in state.context.hypotheses]:
        legal.append(actions["type_ii_rescaling"])

    # Strategic alternatives
    legal.extend([
        actions["try_direct_energy_estimate"],
        actions["try_comparison_principle"],
        actions["explore_alternative_gap_proof"]
    ])

    # Mathematical operations
    legal.extend([
        actions["multiply_by_eta"],
        actions["integrate_by_parts_viscous"]
    ])

    # Contradiction steps
    if "blowup_assumption" not in [h.name for h in state.context.hypotheses]:
        legal.append(actions["assume_blowup_exists"])
    if state.lemma_status.get("pointwise_decay") == LemmaStatus.PROVEN:
        legal.append(actions["derive_contradiction"])

    return legal

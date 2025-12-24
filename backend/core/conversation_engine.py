from backend.core.decision_engine import Decision, DecisionEngine
from backend.core.state_manager import StateManager
from backend.domain.conversation import ConversationState


class ConversationEngine:
    def __init__(self, decision_engine: DecisionEngine, state_manager: StateManager) -> None:
        self.decision_engine = decision_engine
        self.state_manager = state_manager

    def evaluate(self, conversation_id: str) -> tuple[ConversationState, Decision]:
        state = self.state_manager.load(conversation_id)
        decision = self.decision_engine.decide(state)
        return state, decision

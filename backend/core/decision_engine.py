from dataclasses import dataclass

from backend.core.silence_policy import SilencePolicyProvider
from backend.domain.agent_role import AgentRole
from backend.domain.conversation import ConversationState, ConversationStatus


@dataclass(frozen=True)
class Decision:
    should_respond: bool
    agent_role: AgentRole | None
    next_status: ConversationStatus
    reason: str


class DecisionEngine:
    max_attempts_without_reply = 2

    def __init__(self, silence_policy_provider: SilencePolicyProvider | None = None) -> None:
        self.silence_policy_provider = silence_policy_provider or SilencePolicyProvider()

    def decide(self, state: ConversationState) -> Decision:
        silence_policy = self.silence_policy_provider.get()

        if state.status == ConversationStatus.CLOSED:
            return Decision(False, None, ConversationStatus.CLOSED, "conversation_closed")

        if state.attempts >= self.max_attempts_without_reply:
            return Decision(False, None, ConversationStatus.CLOSED, "max_attempts_reached")

        if state.detected_intent == "negative":
            return Decision(False, None, ConversationStatus.CLOSED, "negative_intent")

        if state.detected_intent in silence_policy.when_to_not_reply:
            reason = "silence_policy_final" if silence_policy.silence_is_final else "silence_policy"
            next_status = ConversationStatus.CLOSED if silence_policy.silence_is_final else state.status
            return Decision(False, None, next_status, reason)

        if state.detected_intent == "schedule":
            return Decision(True, AgentRole.SCHEDULING, ConversationStatus.ACTIVE, "schedule_intent")

        return Decision(True, AgentRole.QUALIFICATION, ConversationStatus.ACTIVE, "default_route")

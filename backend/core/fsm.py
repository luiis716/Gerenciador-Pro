from dataclasses import dataclass

from backend.domain.conversation import ConversationStatus


@dataclass(frozen=True)
class TransitionResult:
    allowed: bool
    reason: str


class ConversationStateMachine:
    allowed_transitions: dict[ConversationStatus, tuple[ConversationStatus, ...]] = {
        ConversationStatus.NEW: (ConversationStatus.ACTIVE,),
        ConversationStatus.ACTIVE: (ConversationStatus.WAITING, ConversationStatus.CLOSED),
        ConversationStatus.WAITING: (ConversationStatus.ACTIVE, ConversationStatus.CLOSED),
        ConversationStatus.CLOSED: (),
    }

    def can_transition(
        self, current: ConversationStatus, target: ConversationStatus
    ) -> TransitionResult:
        if target in self.allowed_transitions.get(current, ()): 
            return TransitionResult(True, "allowed")
        return TransitionResult(False, "transition_not_allowed")

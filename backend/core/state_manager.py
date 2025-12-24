from datetime import datetime

from backend.domain.conversation import ConversationState, ConversationStatus


class StateManager:
    def load(self, conversation_id: str) -> ConversationState:
        return ConversationState(
            id=conversation_id,
            contact_id="contact-id",
            status=ConversationStatus.NEW,
            last_agent=None,
            last_message_at=datetime.utcnow(),
            attempts=0,
            detected_intent=None,
        )

    def save(self, state: ConversationState) -> None:
        return None

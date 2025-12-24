from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ConversationStatus(str, Enum):
    NEW = "new"
    ACTIVE = "active"
    WAITING = "waiting"
    CLOSED = "closed"


@dataclass(frozen=True)
class ConversationState:
    id: str
    contact_id: str
    status: ConversationStatus
    last_agent: str | None
    last_message_at: datetime | None
    attempts: int
    detected_intent: str | None

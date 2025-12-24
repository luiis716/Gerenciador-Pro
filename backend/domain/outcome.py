from enum import Enum


class ConversationOutcome(str, Enum):
    CONVERTED = "converted"
    SCHEDULED = "scheduled"
    REJECTED = "rejected"
    ABANDONED = "abandoned"
    HUMAN_HANDOFF = "human_handoff"

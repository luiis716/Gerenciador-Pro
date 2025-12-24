from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EventType(str, Enum):
    INCOMING_MESSAGE = "incoming_message"
    NEW_CONTACT = "new_contact"
    MANUAL_TRIGGER = "manual_trigger"
    TIMEOUT = "timeout"


@dataclass(frozen=True)
class Event:
    type: EventType
    contact_id: str
    payload: dict
    source: str
    timestamp: datetime

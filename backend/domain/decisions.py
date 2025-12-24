from dataclasses import dataclass
from enum import Enum

from backend.domain.conversation import ConversationStatus


class AgentAction(str, Enum):
    REPLY = "reply"
    ASK_TOOL = "ask_tool"
    END = "end"
    SILENCE = "silence"


@dataclass(frozen=True)
class ToolRequest:
    name: str
    payload: dict


@dataclass(frozen=True)
class AgentResult:
    action: AgentAction
    message: str | None
    tool_request: ToolRequest | None
    next_state: ConversationStatus

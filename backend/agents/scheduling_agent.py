from backend.agents.base_agent import AgentProfile, BaseAgent
from backend.domain.conversation import ConversationStatus
from backend.domain.decisions import AgentAction, AgentResult, ToolRequest


class SchedulingAgent(BaseAgent):
    role = "scheduling"
    profile = AgentProfile(
        goal="book a calendar slot",
        max_messages=2,
        can_use_tools=True,
    )

    def run(self, prompt: str) -> AgentResult:
        return AgentResult(
            action=AgentAction.ASK_TOOL,
            message=None,
            tool_request=ToolRequest(name="google_calendar.create_event", payload={}),
            next_state=ConversationStatus.WAITING,
        )

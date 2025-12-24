from backend.agents.base_agent import AgentProfile, BaseAgent
from backend.domain.conversation import ConversationStatus
from backend.domain.decisions import AgentAction, AgentResult


class ReactivationAgent(BaseAgent):
    role = "reactivation"
    profile = AgentProfile(
        goal="restart stalled conversation",
        max_messages=1,
        can_use_tools=False,
    )

    def run(self, prompt: str) -> AgentResult:
        return AgentResult(
            action=AgentAction.REPLY,
            message=prompt,
            tool_request=None,
            next_state=ConversationStatus.WAITING,
        )

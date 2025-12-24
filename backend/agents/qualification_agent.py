from backend.agents.base_agent import AgentProfile, BaseAgent
from backend.domain.conversation import ConversationStatus
from backend.domain.decisions import AgentAction, AgentResult


class QualificationAgent(BaseAgent):
    role = "qualification"
    profile = AgentProfile(
        goal="discover intent and fit",
        max_messages=2,
        can_use_tools=False,
    )

    def run(self, prompt: str) -> AgentResult:
        return AgentResult(
            action=AgentAction.REPLY,
            message=prompt,
            tool_request=None,
            next_state=ConversationStatus.WAITING,
        )

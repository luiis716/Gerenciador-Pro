from backend.agents.base_agent import AgentProfile, BaseAgent
from backend.domain.conversation import ConversationStatus
from backend.domain.decisions import AgentAction, AgentResult


class OrchestratorAgent(BaseAgent):
    role = "orchestrator"
    profile = AgentProfile(
        goal="routing and summarization",
        max_messages=1,
        can_use_tools=False,
    )

    def run(self, prompt: str) -> AgentResult:
        return AgentResult(
            action=AgentAction.SILENCE,
            message=None,
            tool_request=None,
            next_state=ConversationStatus.ACTIVE,
        )


if __name__ == "__main__":
    agent = OrchestratorAgent()
    response = agent.run("orchestrator ready")
    print(response.action)

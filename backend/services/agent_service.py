from backend.agents.closing_agent import ClosingAgent
from backend.agents.qualification_agent import QualificationAgent
from backend.agents.reactivation_agent import ReactivationAgent
from backend.agents.sales_agent import SalesAgent
from backend.agents.scheduling_agent import SchedulingAgent
from backend.domain.agent_role import AgentRole
from backend.domain.decisions import AgentResult


class AgentService:
    def __init__(self) -> None:
        self._agents = {
            AgentRole.QUALIFICATION: QualificationAgent(),
            AgentRole.SALES: SalesAgent(),
            AgentRole.SCHEDULING: SchedulingAgent(),
            AgentRole.REACTIVATION: ReactivationAgent(),
            AgentRole.CLOSING: ClosingAgent(),
        }

    def dispatch(self, agent_role: AgentRole, prompt: str) -> AgentResult:
        agent = self._agents[agent_role]
        return agent.run(prompt)

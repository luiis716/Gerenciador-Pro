from dataclasses import dataclass

from backend.domain.decisions import AgentResult


@dataclass(frozen=True)
class AgentProfile:
    goal: str
    max_messages: int
    can_use_tools: bool


class BaseAgent:
    role: str = "base"
    profile: AgentProfile

    def run(self, prompt: str) -> AgentResult:
        raise NotImplementedError

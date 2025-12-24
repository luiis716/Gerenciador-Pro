from enum import Enum


class AgentRole(str, Enum):
    ORCHESTRATOR = "orchestrator"
    QUALIFICATION = "qualification"
    SALES = "sales"
    SCHEDULING = "scheduling"
    REACTIVATION = "reactivation"
    CLOSING = "closing"

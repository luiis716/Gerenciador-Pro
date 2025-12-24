from dataclasses import dataclass


@dataclass(frozen=True)
class GuardrailLimits:
    max_active_contacts_per_day: int
    max_messages_per_contact: int
    max_agents_per_conversation: int


class Guardrails:
    def __init__(self, limits: GuardrailLimits) -> None:
        self.limits = limits

    def allow_contact(self, active_contacts_today: int) -> bool:
        return active_contacts_today < self.limits.max_active_contacts_per_day

    def allow_message(self, messages_sent: int) -> bool:
        return messages_sent < self.limits.max_messages_per_contact

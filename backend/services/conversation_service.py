from dataclasses import replace
from datetime import datetime

from backend.core.conversation_engine import ConversationEngine
from backend.core.fsm import ConversationStateMachine
from backend.core.guardrails import Guardrails
from backend.core.message_builder import MessageBuilder
from backend.core.state_manager import StateManager
from backend.domain.decisions import AgentAction
from backend.domain.event import Event
from backend.infra.channel.whatsapp_gateway import WhatsAppGateway
from backend.infra.metrics import Metrics
from backend.services.agent_service import AgentService


class ConversationService:
    def __init__(
        self,
        engine: ConversationEngine,
        agent_service: AgentService,
        message_builder: MessageBuilder,
        gateway: WhatsAppGateway,
        state_manager: StateManager,
        state_machine: ConversationStateMachine,
        guardrails: Guardrails,
        metrics: Metrics,
    ) -> None:
        self.engine = engine
        self.agent_service = agent_service
        self.message_builder = message_builder
        self.gateway = gateway
        self.state_manager = state_manager
        self.state_machine = state_machine
        self.guardrails = guardrails
        self.metrics = metrics

    def handle(self, event: Event, prompt: str) -> dict:
        state, decision = self.engine.evaluate(event.contact_id)

        if not self.guardrails.allow_message(state.attempts):
            self.metrics.increment("guardrail_blocked")
            return {"decision": "guardrail_blocked", "sent": False}

        if not decision.should_respond or decision.agent_role is None:
            self.metrics.increment("silence_rate")
            return {"decision": decision.reason, "sent": False}

        result = self.agent_service.dispatch(decision.agent_role, prompt)

        transition = self.state_machine.can_transition(state.status, result.next_state)
        if not transition.allowed:
            self.metrics.increment("invalid_transition")
            return {"decision": transition.reason, "sent": False}

        if result.action == AgentAction.REPLY and result.message:
            message = self.message_builder.build(result.message)
            self.gateway.send_message(state.contact_id, message)
            self.metrics.increment("messages_sent")

        if result.action == AgentAction.END:
            self.gateway.send_message(state.contact_id, result.message or "")
            self.metrics.increment("conversations_closed")

        next_attempts = state.attempts + 1 if result.action in {AgentAction.REPLY, AgentAction.END} else state.attempts
        next_state = replace(
            state,
            status=result.next_state,
            last_agent=decision.agent_role.value,
            last_message_at=datetime.utcnow(),
            attempts=next_attempts,
        )
        self.state_manager.save(next_state)
        return {"decision": decision.reason, "sent": True, "action": result.action}

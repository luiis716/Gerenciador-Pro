from backend.core.conversation_engine import ConversationEngine
from backend.core.decision_engine import DecisionEngine
from backend.core.fsm import ConversationStateMachine
from backend.core.guardrails import Guardrails, GuardrailLimits
from backend.core.message_builder import MessageBuilder
from backend.core.state_manager import StateManager
from backend.infra.channel.whatsapp_gateway import WhatsAppGateway
from backend.infra.metrics import Metrics
from backend.services.agent_service import AgentService
from backend.services.conversation_service import ConversationService


def get_conversation_service() -> ConversationService:
    decision_engine = DecisionEngine()
    state_manager = StateManager()
    engine = ConversationEngine(decision_engine, state_manager)
    agent_service = AgentService()
    message_builder = MessageBuilder()
    gateway = WhatsAppGateway()
    state_machine = ConversationStateMachine()
    guardrails = Guardrails(
        GuardrailLimits(
            max_active_contacts_per_day=100,
            max_messages_per_contact=5,
            max_agents_per_conversation=3,
        )
    )
    metrics = Metrics()
    return ConversationService(
        engine,
        agent_service,
        message_builder,
        gateway,
        state_manager,
        state_machine,
        guardrails,
        metrics,
    )

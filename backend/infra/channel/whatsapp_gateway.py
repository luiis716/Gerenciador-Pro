class WhatsAppGateway:
    def send_message(self, contact_id: str, text: str) -> None:
        return None

    def receive_message(self, payload: dict) -> dict:
        return payload

class ContactService:
    def get(self, contact_id: str) -> dict:
        return {"id": contact_id}

from fastapi import APIRouter

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/{contact_id}")
def get_contact(contact_id: str) -> dict:
    return {"id": contact_id}

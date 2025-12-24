from fastapi import APIRouter

router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.get("/{conversation_id}")
def get_conversation(conversation_id: str) -> dict:
    return {"id": conversation_id}

from fastapi import APIRouter

router = APIRouter(prefix="/campaigns", tags=["campaigns"])


@router.get("/")
def list_campaigns() -> dict:
    return {"campaigns": []}

from fastapi import APIRouter

router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("/")
def get_settings() -> dict:
    return {"version": "0.1.0"}

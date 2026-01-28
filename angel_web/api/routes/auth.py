"""Auth API routes."""
from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
def login() -> dict[str, str]:
    """Login endpoint stub."""
    return {"status": "ok"}

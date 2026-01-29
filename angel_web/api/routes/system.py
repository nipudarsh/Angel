"""System API routes."""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    """Health check stub."""
    return {"status": "ok"}

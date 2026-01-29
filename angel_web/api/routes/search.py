"""Search API routes."""
from fastapi import APIRouter

router = APIRouter()


@router.get("")
def search(q: str) -> dict[str, str]:
    """Search stub."""
    return {"query": q}

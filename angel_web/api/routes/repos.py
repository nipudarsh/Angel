"""Repository API routes."""
from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_repos() -> list[dict[str, str]]:
    """List repositories stub."""
    return []

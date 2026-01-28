"""Tool API routes."""
from fastapi import APIRouter

router = APIRouter()


@router.get("")
def list_tools() -> list[dict[str, str]]:
    """List tools stub."""
    return []

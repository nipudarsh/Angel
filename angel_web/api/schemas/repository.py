"""Repository schemas."""
from pydantic import BaseModel


class RepositoryOut(BaseModel):
    """Repository output schema."""

    id: str
    name: str
    url: str

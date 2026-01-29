"""User schemas."""
from pydantic import BaseModel


class UserOut(BaseModel):
    """User output schema."""

    id: str
    username: str

"""Tool schemas."""
from pydantic import BaseModel


class ToolOut(BaseModel):
    """Tool output schema."""

    id: str
    name: str
    version: str

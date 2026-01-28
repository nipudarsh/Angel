"""Repository service layer."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RepoMetadata:
    """Repository metadata container."""

    name: str
    url: str

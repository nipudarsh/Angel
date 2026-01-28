"""Utility functions."""
from __future__ import annotations

from pathlib import Path


def ensure_directory(path: Path) -> None:
    """Ensure a directory exists."""
    path.mkdir(parents=True, exist_ok=True)

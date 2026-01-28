"""Tool service layer."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from angel_cli.core.storage import calculate_sha256


@dataclass
class ToolMetadata:
    """Simple tool metadata container."""

    name: str
    version: str
    file_path: Path
    file_hash: str


def build_metadata(path: Path, name: str, version: str) -> ToolMetadata:
    """Build metadata for a tool file."""
    return ToolMetadata(
        name=name,
        version=version,
        file_path=path,
        file_hash=calculate_sha256(path),
    )

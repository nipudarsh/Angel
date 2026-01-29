"""File storage utilities."""
from __future__ import annotations

from pathlib import Path
import hashlib


def calculate_sha256(file_path: Path) -> str:
    """Calculate SHA-256 hash for a file."""
    hash_obj = hashlib.sha256()
    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

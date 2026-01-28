"""Backup service layer."""
from __future__ import annotations

from pathlib import Path


def create_backup(destination: Path) -> Path:
    """Create a backup archive (stub)."""
    destination.mkdir(parents=True, exist_ok=True)
    backup_file = destination / "backup.zip"
    backup_file.write_text("backup placeholder")
    return backup_file

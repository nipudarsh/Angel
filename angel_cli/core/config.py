"""Configuration management for ANGEL."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class AngelConfig:
    """Runtime configuration settings."""

    storage_path: Path
    database_path: Path
    log_level: str = "INFO"


def default_config_path() -> Path:
    """Return the default config path for the current platform."""
    if os.name == "nt":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    else:
        base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    return base / "angel" / "config.toml"


def load_config(config_path: Path | None = None) -> AngelConfig:
    """Load configuration with defaults."""
    if config_path is None:
        config_path = default_config_path()
    storage_path = Path.home() / ".angel" / "storage"
    database_path = storage_path / "angel.db"
    return AngelConfig(storage_path=storage_path, database_path=database_path)

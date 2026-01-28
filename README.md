# ANGEL

ANGEL (Automated Navigator for Gathering and Executing Local tools) is a cross-platform CLI + web console for storing and managing your personal toolkit and repositories.

## Features
- CLI for tool and repository management
- Local FastAPI web console
- SQLite-backed metadata storage
- Configurable storage paths and settings

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
angel init
angel web
```

## Configuration
Configuration is stored in `~/.config/angel/config.toml` (Linux/macOS) or `%APPDATA%\angel\config.toml` (Windows). Use `angel config` to manage settings.

## Development
```bash
pip install -r requirements-dev.txt
pre-commit install
pytest
```

## License
MIT

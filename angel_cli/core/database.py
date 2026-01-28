"""Database session management."""
from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from angel_cli.core.config import AngelConfig


def create_session_factory(config: AngelConfig) -> sessionmaker:
    """Create a SQLAlchemy session factory."""
    engine = create_engine(f"sqlite:///{config.database_path}")
    return sessionmaker(bind=engine)

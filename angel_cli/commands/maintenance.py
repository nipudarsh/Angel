"""Maintenance commands."""
import click



@click.group(name="maintenance", help="Maintenance tasks.")
def group() -> None:
    """Maintenance command group."""


@group.command("doctor")
def doctor() -> None:
    """Run a health check."""


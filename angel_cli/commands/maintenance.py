"""Maintenance commands."""
import click
from rich.console import Console

console = Console()


@click.group(name="maintenance", help="Maintenance tasks.")
def group() -> None:
    """Maintenance command group."""


@group.command("doctor")
def doctor() -> None:
    """Run a health check."""
    console.print("[green]All checks passed (stub).[/green]")

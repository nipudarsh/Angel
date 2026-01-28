"""Repository commands."""
import click
from rich.console import Console

console = Console()


@click.group(name="repos", help="Manage repositories.")
def group() -> None:
    """Repos command group."""


@group.command("list")
def list_repos() -> None:
    """List tracked repositories."""
    console.print("[green]No repositories available (stub).[/green]")

"""Tool management commands."""
import click
from rich.console import Console

console = Console()


@click.group(name="tools", help="Manage tools.")
def group() -> None:
    """Tools command group."""


@group.command("list")
def list_tools() -> None:
    """List stored tools."""
    console.print("[green]No tools available (stub).[/green]")


@group.command("add")
@click.argument("path", required=False)
def add_tool(path: str | None) -> None:
    """Add a tool from a file path."""
    console.print(f"[green]Add tool stub: {path}[/green]")

"""Tool management commands."""
import click


@click.group(name="tools", help="Manage tools.")
def group() -> None:
    """Tools command group."""


@group.command("list")
def list_tools() -> None:
    """List stored tools."""
    click.echo("No tools available (stub).")


@group.command("add")
@click.argument("path", required=False)
def add_tool(path: str | None) -> None:
    """Add a tool from a file path."""
    click.echo(f"Add tool stub: {path}")

"""Configuration commands."""
import click
from rich.console import Console

console = Console()


@click.group(name="config", help="Configuration management.")
def group() -> None:
    """Config command group."""


@group.command("show")
def show_config() -> None:
    """Show current configuration."""
    console.print("[green]Config display not yet implemented.[/green]")

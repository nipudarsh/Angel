"""Configuration commands."""
import click



@click.group(name="config", help="Configuration management.")
def group() -> None:
    """Config command group."""


@group.command("show")
def show_config() -> None:
    """Show current configuration."""
 


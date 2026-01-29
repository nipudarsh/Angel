"""Repository commands."""
import click



@click.group(name="repos", help="Manage repositories.")
def group() -> None:
    """Repos command group."""


@group.command("list")
def list_repos() -> None:
    """List tracked repositories."""


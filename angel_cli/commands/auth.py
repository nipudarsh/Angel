"""Authentication commands."""
import click
from rich.console import Console

console = Console()


@click.group(name="auth", help="Authentication commands.")
def group() -> None:
    """Auth command group."""


@group.command("login")
def login() -> None:
    """Login to the local instance."""
    console.print("[green]Login flow not yet implemented.[/green]")


@group.command("logout")
def logout() -> None:
    """Logout from the local instance."""
    console.print("[green]Logout flow not yet implemented.[/green]")


@group.command("change-password")
def change_password() -> None:
    """Change the current user's password."""
    console.print("[yellow]Password change not yet implemented.[/yellow]")

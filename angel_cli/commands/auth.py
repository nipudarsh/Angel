"""Authentication commands."""
import click



@click.group(name="auth", help="Authentication commands.")
def group() -> None:
    """Auth command group."""


@group.command("login")
def login() -> None:
    """Login to the local instance."""



@group.command("logout")
def logout() -> None:
    """Logout from the local instance."""



@group.command("change-password")
def change_password() -> None:
    """Change the current user's password."""


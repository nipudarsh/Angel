"""Authentication commands."""
import click


@click.group(name="auth", help="Authentication commands.")
def group() -> None:
    """Auth command group."""


@group.command("login")
def login() -> None:
    """Login to the local instance."""
    click.echo("Login flow not yet implemented.")


@group.command("logout")
def logout() -> None:
    """Logout from the local instance."""
    click.echo("Logout flow not yet implemented.")


@group.command("change-password")
def change_password() -> None:
    """Change the current user's password."""
    click.echo("Password change not yet implemented.")

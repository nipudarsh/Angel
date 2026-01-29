"""Main CLI entry point for ANGEL."""
from __future__ import annotations

import click

@click.group(help="ANGEL CLI - manage tools and repositories.")
@click.option("--config-path", type=click.Path(), help="Custom config path.")
@click.pass_context
def main(ctx: click.Context, config_path: str | None) -> None:
    """Root command group."""
    ctx.ensure_object(dict)
    ctx.obj["config_path"] = config_path


main.add_command(auth.group)
main.add_command(tools.group)
main.add_command(repos.group)
main.add_command(maintenance.group)
main.add_command(config.group)

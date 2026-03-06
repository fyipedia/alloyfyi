"""Command-line interface for alloyfyi."""

from __future__ import annotations

import json

import typer

from alloyfyi.api import AlloyFYI

app = typer.Typer(help="AlloyFYI — Metal alloys and materials science API client.")


@app.command()
def search(query: str) -> None:
    """Search alloyfyi.com."""
    with AlloyFYI() as api:
        result = api.search(query)
        typer.echo(json.dumps(result, indent=2))

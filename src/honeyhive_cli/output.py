"""Output formatting utilities."""

import json
import sys
from typing import Any, Optional, Sequence

import click
from rich.console import Console
from rich.table import Table


def print_json(data: Any) -> None:
    """Pretty-print JSON data to stdout."""
    click.echo(json.dumps(data, indent=2, default=str))


def print_table(rows: Sequence[dict], columns: Optional[Sequence[str]] = None) -> None:
    """Render a list of dicts as a rich table."""
    if not rows:
        click.echo("No results.")
        return

    if columns is None:
        columns = list(rows[0].keys())

    console = Console(file=sys.stdout)
    table = Table(show_header=True, header_style="bold")
    for col in columns:
        table.add_column(col)

    for row in rows:
        table.add_row(*[_format_cell(row.get(col)) for col in columns])

    console.print(table)


def _format_cell(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, default=str)
    return str(value)


def output(data: Any, fmt: str, columns: Optional[Sequence[str]] = None) -> None:
    """Dispatch output to the right formatter."""
    if fmt == "table":
        if isinstance(data, list):
            print_table(data, columns)
        elif isinstance(data, dict):
            print_table([data], columns)
        else:
            print_json(data)
    else:
        print_json(data)

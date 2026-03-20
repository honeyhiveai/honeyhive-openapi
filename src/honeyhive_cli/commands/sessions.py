"""Session commands."""

import json

import click

from honeyhive_cli.cli import State, pass_state
from honeyhive_cli.output import output


@click.group()
def sessions() -> None:
    """Manage sessions."""


@sessions.command()
@click.argument("session_id")
@pass_state
def get(state: State, session_id: str) -> None:
    """Get a session tree by session ID."""
    resp = state.client.get(f"/v1/sessions/{session_id}")
    output(resp.json(), state.output)


@sessions.command()
@click.option("--session", "session_data", required=True, help="JSON-encoded session object.")
@pass_state
def start(state: State, session_data: str) -> None:
    """Start a new session."""
    try:
        json.loads(session_data)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"Invalid JSON for --session: {exc}") from exc

    resp = state.client.post("/session/start", json={"session": session_data})
    output(resp.json(), state.output)


@sessions.command()
@click.argument("session_id")
@click.confirmation_option(prompt="Are you sure you want to delete this session?")
@pass_state
def delete(state: State, session_id: str) -> None:
    """Delete all events for a session."""
    resp = state.client.delete(f"/v1/sessions/{session_id}")
    output(resp.json(), state.output)

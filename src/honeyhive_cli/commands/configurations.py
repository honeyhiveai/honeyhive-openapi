"""Configuration commands."""

import json
from typing import Optional

import click

from honeyhive_cli.cli import State, pass_state
from honeyhive_cli.output import output


@click.group()
def configurations() -> None:
    """Manage prompt/model configurations."""


@configurations.command("list")
@click.option("--name", default=None, help="Filter by configuration name.")
@click.option("--env", default=None, help="Filter by environment (dev, staging, prod).")
@click.option("--tags", default=None, help="Filter by tags.")
@pass_state
def list_configurations(
    state: State, name: Optional[str], env: Optional[str], tags: Optional[str]
) -> None:
    """List configurations."""
    params: dict = {}
    if name:
        params["name"] = name
    if env:
        params["env"] = env
    if tags:
        params["tags"] = tags

    resp = state.client.get("/v1/configurations", params=params)
    data = resp.json()
    if state.output == "table" and isinstance(data, list):
        output(data, state.output, columns=["id", "name", "type", "provider", "created_at"])
    else:
        output(data, state.output)


@configurations.command()
@click.option("--name", required=True, help="Configuration name.")
@click.option("--provider", required=True, help="Provider (e.g. openai, anthropic).")
@click.option("--parameters", required=True, help="JSON-encoded parameters object.")
@click.option(
    "--type",
    "config_type",
    type=click.Choice(["LLM", "pipeline"]),
    default="LLM",
    help="Configuration type.",
)
@click.option("--env", default=None, help="Comma-separated environments (dev,staging,prod).")
@click.option("--tags", default=None, help="Comma-separated tags.")
@pass_state
def create(
    state: State,
    name: str,
    provider: str,
    parameters: str,
    config_type: str,
    env: Optional[str],
    tags: Optional[str],
) -> None:
    """Create a new configuration."""
    try:
        params_parsed = json.loads(parameters)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"Invalid JSON for --parameters: {exc}") from exc

    body: dict = {
        "name": name,
        "provider": provider,
        "parameters": params_parsed,
        "type": config_type,
    }
    if env:
        body["env"] = [e.strip() for e in env.split(",")]
    if tags:
        body["tags"] = [t.strip() for t in tags.split(",")]

    resp = state.client.post("/v1/configurations", json=body)
    output(resp.json(), state.output)


@configurations.command()
@click.argument("config_id")
@click.option("--name", required=True, help="Configuration name.")
@click.option("--provider", default=None, help="New provider.")
@click.option("--parameters", default=None, help="JSON-encoded parameters.")
@click.option("--env", default=None, help="Comma-separated environments.")
@click.option("--tags", default=None, help="Comma-separated tags.")
@pass_state
def update(
    state: State,
    config_id: str,
    name: str,
    provider: Optional[str],
    parameters: Optional[str],
    env: Optional[str],
    tags: Optional[str],
) -> None:
    """Update a configuration by ID."""
    body: dict = {"name": name}
    if provider:
        body["provider"] = provider
    if parameters:
        try:
            body["parameters"] = json.loads(parameters)
        except json.JSONDecodeError as exc:
            raise click.ClickException(f"Invalid JSON for --parameters: {exc}") from exc
    if env:
        body["env"] = [e.strip() for e in env.split(",")]
    if tags:
        body["tags"] = [t.strip() for t in tags.split(",")]

    resp = state.client.put(f"/v1/configurations/{config_id}", json=body)
    output(resp.json(), state.output)


@configurations.command()
@click.argument("config_id")
@click.confirmation_option(prompt="Are you sure you want to delete this configuration?")
@pass_state
def delete(state: State, config_id: str) -> None:
    """Delete a configuration by ID."""
    resp = state.client.delete(f"/v1/configurations/{config_id}")
    output(resp.json(), state.output)

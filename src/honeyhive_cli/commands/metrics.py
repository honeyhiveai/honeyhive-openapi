"""Metric commands."""

import json
from typing import Optional

import click

from honeyhive_cli.cli import State, pass_state
from honeyhive_cli.output import output


@click.group()
def metrics() -> None:
    """Manage metrics."""


@metrics.command("list")
@click.option("--type", "metric_type", default=None, help="Filter by metric type.")
@click.option("--id", "metric_id", default=None, help="Filter by metric ID.")
@pass_state
def list_metrics(state: State, metric_type: Optional[str], metric_id: Optional[str]) -> None:
    """List all metrics."""
    params: dict = {}
    if metric_type:
        params["type"] = metric_type
    if metric_id:
        params["id"] = metric_id

    resp = state.client.get("/v1/metrics", params=params)
    data = resp.json()
    if state.output == "table" and isinstance(data, list):
        output(data, state.output, columns=["id", "name", "type", "return_type", "created_at"])
    else:
        output(data, state.output)


@metrics.command()
@click.option("--name", required=True, help="Metric name.")
@click.option(
    "--type",
    "metric_type",
    required=True,
    type=click.Choice(["PYTHON", "LLM", "HUMAN", "COMPOSITE"]),
    help="Metric type.",
)
@click.option("--criteria", required=True, help="Metric criteria/code.")
@click.option("--description", default="", help="Metric description.")
@click.option(
    "--return-type",
    type=click.Choice(["float", "boolean", "string", "categorical"]),
    default="float",
    help="Return type.",
)
@click.option("--enabled-in-prod", is_flag=True, default=False, help="Enable in production.")
@pass_state
def create(
    state: State,
    name: str,
    metric_type: str,
    criteria: str,
    description: str,
    return_type: str,
    enabled_in_prod: bool,
) -> None:
    """Create a new metric."""
    body: dict = {
        "name": name,
        "type": metric_type,
        "criteria": criteria,
        "description": description,
        "return_type": return_type,
        "enabled_in_prod": enabled_in_prod,
    }
    resp = state.client.post("/v1/metrics", json=body)
    output(resp.json(), state.output)


@metrics.command()
@click.option("--id", "metric_id", required=True, help="Metric ID to update.")
@click.option("--name", default=None, help="New name.")
@click.option("--criteria", default=None, help="New criteria.")
@click.option("--description", default=None, help="New description.")
@pass_state
def update(
    state: State,
    metric_id: str,
    name: Optional[str],
    criteria: Optional[str],
    description: Optional[str],
) -> None:
    """Update an existing metric."""
    body: dict = {"id": metric_id}
    if name:
        body["name"] = name
    if criteria:
        body["criteria"] = criteria
    if description is not None:
        body["description"] = description

    resp = state.client.put("/v1/metrics", json=body)
    output(resp.json(), state.output)


@metrics.command()
@click.option("--id", "metric_id", required=True, help="Metric ID to delete.")
@click.confirmation_option(prompt="Are you sure you want to delete this metric?")
@pass_state
def delete(state: State, metric_id: str) -> None:
    """Delete a metric."""
    resp = state.client.delete("/v1/metrics", params={"metric_id": metric_id})
    output(resp.json(), state.output)


@metrics.command()
@click.option("--metric", required=True, help="JSON-encoded metric definition.")
@click.option("--event", "event_data", required=True, help="JSON-encoded event data.")
@pass_state
def run(state: State, metric: str, event_data: str) -> None:
    """Run a metric evaluation on an event."""
    try:
        metric_parsed = json.loads(metric)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"Invalid JSON for --metric: {exc}") from exc
    try:
        event_parsed = json.loads(event_data)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"Invalid JSON for --event: {exc}") from exc

    resp = state.client.post(
        "/v1/metrics/run_metric", json={"metric": metric_parsed, "event": event_parsed}
    )
    output(resp.json(), state.output)

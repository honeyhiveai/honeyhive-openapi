"""Datapoint commands."""

import json
from typing import Optional

import click

from honeyhive_cli.cli import State, pass_state
from honeyhive_cli.output import output


@click.group()
def datapoints() -> None:
    """Manage datapoints."""


@datapoints.command("list")
@click.option("--dataset-name", default=None, help="Filter by dataset name.")
@click.option("--ids", default=None, help="Comma-separated datapoint IDs.")
@pass_state
def list_datapoints(state: State, dataset_name: Optional[str], ids: Optional[str]) -> None:
    """List datapoints, optionally filtered by dataset name or IDs."""
    params: dict = {}
    if dataset_name:
        params["dataset_name"] = dataset_name
    if ids:
        params["datapoint_ids"] = [i.strip() for i in ids.split(",")]

    resp = state.client.get("/v1/datapoints", params=params)
    output(resp.json(), state.output)


@datapoints.command()
@click.argument("datapoint_id")
@pass_state
def get(state: State, datapoint_id: str) -> None:
    """Get a specific datapoint by ID."""
    resp = state.client.get(f"/v1/datapoints/{datapoint_id}")
    output(resp.json(), state.output)


@datapoints.command()
@click.option("--inputs", default=None, help="JSON-encoded inputs object.")
@click.option("--history", default=None, help="JSON-encoded history array.")
@click.option("--ground-truth", default=None, help="JSON-encoded ground truth object.")
@click.option("--metadata", default=None, help="JSON-encoded metadata object.")
@click.option("--linked-event", default=None, help="Linked event ID.")
@click.option("--linked-datasets", default=None, help="Comma-separated dataset IDs.")
@pass_state
def create(
    state: State,
    inputs: Optional[str],
    history: Optional[str],
    ground_truth: Optional[str],
    metadata: Optional[str],
    linked_event: Optional[str],
    linked_datasets: Optional[str],
) -> None:
    """Create a new datapoint."""
    body: dict = {}
    for key, raw in [
        ("inputs", inputs),
        ("history", history),
        ("ground_truth", ground_truth),
        ("metadata", metadata),
    ]:
        if raw:
            try:
                body[key] = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise click.ClickException(f"Invalid JSON for --{key}: {exc}") from exc
    if linked_event:
        body["linked_event"] = linked_event
    if linked_datasets:
        body["linked_datasets"] = [d.strip() for d in linked_datasets.split(",")]

    resp = state.client.post("/v1/datapoints", json=body)
    output(resp.json(), state.output)


@datapoints.command()
@click.argument("datapoint_id")
@click.option("--inputs", default=None, help="JSON-encoded inputs object.")
@click.option("--history", default=None, help="JSON-encoded history array.")
@click.option("--ground-truth", default=None, help="JSON-encoded ground truth object.")
@click.option("--metadata", default=None, help="JSON-encoded metadata object.")
@pass_state
def update(
    state: State,
    datapoint_id: str,
    inputs: Optional[str],
    history: Optional[str],
    ground_truth: Optional[str],
    metadata: Optional[str],
) -> None:
    """Update a datapoint by ID."""
    body: dict = {}
    for key, raw in [
        ("inputs", inputs),
        ("history", history),
        ("ground_truth", ground_truth),
        ("metadata", metadata),
    ]:
        if raw:
            try:
                body[key] = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise click.ClickException(f"Invalid JSON for --{key}: {exc}") from exc

    resp = state.client.put(f"/v1/datapoints/{datapoint_id}", json=body)
    output(resp.json(), state.output)


@datapoints.command()
@click.argument("datapoint_id")
@click.confirmation_option(prompt="Are you sure you want to delete this datapoint?")
@pass_state
def delete(state: State, datapoint_id: str) -> None:
    """Delete a datapoint by ID."""
    resp = state.client.delete(f"/v1/datapoints/{datapoint_id}")
    output(resp.json(), state.output)

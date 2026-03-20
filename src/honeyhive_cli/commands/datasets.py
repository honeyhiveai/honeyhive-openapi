"""Dataset commands."""

import json
from typing import Optional

import click

from honeyhive_cli.cli import State, pass_state
from honeyhive_cli.output import output


@click.group()
def datasets() -> None:
    """Manage datasets."""


@datasets.command("list")
@click.option("--id", "dataset_id", default=None, help="Filter by dataset ID.")
@click.option("--name", default=None, help="Filter by dataset name.")
@click.option("--include-datapoints", is_flag=True, default=False, help="Include datapoints.")
@pass_state
def list_datasets(
    state: State,
    dataset_id: Optional[str],
    name: Optional[str],
    include_datapoints: bool,
) -> None:
    """List datasets."""
    params: dict = {}
    if dataset_id:
        params["dataset_id"] = dataset_id
    if name:
        params["name"] = name
    if include_datapoints:
        params["include_datapoints"] = "true"

    resp = state.client.get("/v1/datasets", params=params)
    data = resp.json()
    if state.output == "table":
        items = data.get("datasets", data) if isinstance(data, dict) else data
        output(items, state.output, columns=["id", "name", "description", "created_at"])
    else:
        output(data, state.output)


@datasets.command()
@click.option("--name", default="Untitled Dataset", help="Dataset name.")
@click.option("--description", default=None, help="Dataset description.")
@pass_state
def create(state: State, name: str, description: Optional[str]) -> None:
    """Create a new dataset."""
    body: dict = {"name": name}
    if description:
        body["description"] = description

    resp = state.client.post("/v1/datasets", json=body)
    output(resp.json(), state.output)


@datasets.command()
@click.option("--id", "dataset_id", required=True, help="Dataset ID to update.")
@click.option("--name", default=None, help="New dataset name.")
@click.option("--description", default=None, help="New description.")
@pass_state
def update(state: State, dataset_id: str, name: Optional[str], description: Optional[str]) -> None:
    """Update a dataset."""
    body: dict = {"dataset_id": dataset_id}
    if name:
        body["name"] = name
    if description is not None:
        body["description"] = description

    resp = state.client.put("/v1/datasets", json=body)
    output(resp.json(), state.output)


@datasets.command()
@click.option("--id", "dataset_id", required=True, help="Dataset ID to delete.")
@click.confirmation_option(prompt="Are you sure you want to delete this dataset?")
@pass_state
def delete(state: State, dataset_id: str) -> None:
    """Delete a dataset."""
    resp = state.client.delete("/v1/datasets", params={"dataset_id": dataset_id})
    output(resp.json(), state.output)


@datasets.command("add-datapoints")
@click.argument("dataset_id")
@click.option("--data", required=True, help="JSON-encoded array of data objects.")
@click.option(
    "--mapping",
    required=True,
    help="JSON-encoded mapping {inputs, history, ground_truth}.",
)
@pass_state
def add_datapoints(state: State, dataset_id: str, data: str, mapping: str) -> None:
    """Add datapoints to a dataset."""
    try:
        data_parsed = json.loads(data)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"Invalid JSON for --data: {exc}") from exc
    try:
        mapping_parsed = json.loads(mapping)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"Invalid JSON for --mapping: {exc}") from exc

    resp = state.client.post(
        f"/v1/datasets/{dataset_id}/datapoints",
        json={"data": data_parsed, "mapping": mapping_parsed},
    )
    output(resp.json(), state.output)


@datasets.command("remove-datapoint")
@click.argument("dataset_id")
@click.argument("datapoint_id")
@click.confirmation_option(prompt="Remove this datapoint from the dataset?")
@pass_state
def remove_datapoint(state: State, dataset_id: str, datapoint_id: str) -> None:
    """Remove a datapoint from a dataset."""
    resp = state.client.delete(f"/v1/datasets/{dataset_id}/datapoints/{datapoint_id}")
    output(resp.json(), state.output)

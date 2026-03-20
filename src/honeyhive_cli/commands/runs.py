"""Experiment run commands."""

import json
from typing import Optional

import click

from honeyhive_cli.cli import State, pass_state
from honeyhive_cli.output import output


@click.group()
def runs() -> None:
    """Manage experiment runs (evaluations)."""


@runs.command("list")
@click.option("--dataset-id", default=None, help="Filter by dataset ID.")
@click.option("--name", default=None, help="Filter by run name.")
@click.option(
    "--status",
    type=click.Choice(["pending", "completed", "failed", "cancelled", "running"]),
    default=None,
    help="Filter by status.",
)
@click.option("--page", type=int, default=None, help="Page number.")
@click.option("--limit", type=int, default=None, help="Results per page (max 100).")
@click.option(
    "--sort-by",
    type=click.Choice(["created_at", "updated_at", "name", "status"]),
    default=None,
    help="Sort field.",
)
@click.option(
    "--sort-order",
    type=click.Choice(["asc", "desc"]),
    default=None,
    help="Sort order.",
)
@pass_state
def list_runs(
    state: State,
    dataset_id: Optional[str],
    name: Optional[str],
    status: Optional[str],
    page: Optional[int],
    limit: Optional[int],
    sort_by: Optional[str],
    sort_order: Optional[str],
) -> None:
    """List evaluation runs."""
    params: dict = {}
    if dataset_id:
        params["dataset_id"] = dataset_id
    if name:
        params["name"] = name
    if status:
        params["status"] = status
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if sort_by:
        params["sort_by"] = sort_by
    if sort_order:
        params["sort_order"] = sort_order

    resp = state.client.get("/v1/runs", params=params)
    output(resp.json(), state.output)


@runs.command()
@click.argument("run_id")
@pass_state
def get(state: State, run_id: str) -> None:
    """Get details of an evaluation run."""
    resp = state.client.get(f"/v1/runs/{run_id}")
    output(resp.json(), state.output)


@runs.command()
@click.option("--name", default=None, help="Run name.")
@click.option("--description", default=None, help="Run description.")
@click.option("--dataset-id", default=None, help="Associated dataset ID.")
@click.option(
    "--status",
    type=click.Choice(["pending", "completed", "failed", "cancelled", "running"]),
    default="pending",
    help="Initial status.",
)
@click.option("--metadata", default=None, help="JSON-encoded metadata.")
@click.option("--configuration", default=None, help="JSON-encoded configuration.")
@pass_state
def create(
    state: State,
    name: Optional[str],
    description: Optional[str],
    dataset_id: Optional[str],
    status: str,
    metadata: Optional[str],
    configuration: Optional[str],
) -> None:
    """Create a new evaluation run."""
    body: dict = {"status": status}
    if name:
        body["name"] = name
    if description:
        body["description"] = description
    if dataset_id:
        body["dataset_id"] = dataset_id
    for key, raw in [("metadata", metadata), ("configuration", configuration)]:
        if raw:
            try:
                body[key] = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise click.ClickException(f"Invalid JSON for --{key}: {exc}") from exc

    resp = state.client.post("/v1/runs", json=body)
    output(resp.json(), state.output)


@runs.command()
@click.argument("run_id")
@click.option("--name", default=None, help="New run name.")
@click.option("--description", default=None, help="New description.")
@click.option(
    "--status",
    type=click.Choice(["pending", "completed", "failed", "cancelled", "running"]),
    default=None,
    help="New status.",
)
@click.option("--metadata", default=None, help="JSON-encoded metadata.")
@pass_state
def update(
    state: State,
    run_id: str,
    name: Optional[str],
    description: Optional[str],
    status: Optional[str],
    metadata: Optional[str],
) -> None:
    """Update an evaluation run."""
    body: dict = {}
    if name:
        body["name"] = name
    if description:
        body["description"] = description
    if status:
        body["status"] = status
    if metadata:
        try:
            body["metadata"] = json.loads(metadata)
        except json.JSONDecodeError as exc:
            raise click.ClickException(f"Invalid JSON for --metadata: {exc}") from exc

    resp = state.client.put(f"/v1/runs/{run_id}", json=body)
    output(resp.json(), state.output)


@runs.command()
@click.argument("run_id")
@click.confirmation_option(prompt="Are you sure you want to delete this run?")
@pass_state
def delete(state: State, run_id: str) -> None:
    """Delete an evaluation run."""
    resp = state.client.delete(f"/v1/runs/{run_id}")
    output(resp.json(), state.output)


@runs.command("metrics")
@click.argument("run_id")
@click.option("--date-range", default=None, help="JSON-encoded date range filter.")
@click.option("--filters", default=None, help="JSON-encoded filters.")
@pass_state
def run_metrics(
    state: State, run_id: str, date_range: Optional[str], filters: Optional[str]
) -> None:
    """Get event metrics for an experiment run."""
    params: dict = {}
    if date_range:
        params["dateRange"] = date_range
    if filters:
        params["filters"] = filters

    resp = state.client.get(f"/v1/runs/{run_id}/metrics", params=params)
    output(resp.json(), state.output)


@runs.command()
@click.argument("run_id")
@click.option(
    "--aggregate-function",
    type=click.Choice(["average", "min", "max", "median", "p90", "p95", "p99", "sum", "count"]),
    default=None,
    help="Aggregation function.",
)
@click.option("--filters", default=None, help="JSON-encoded filters.")
@pass_state
def result(
    state: State, run_id: str, aggregate_function: Optional[str], filters: Optional[str]
) -> None:
    """Get the evaluation result for a run."""
    params: dict = {}
    if aggregate_function:
        params["aggregate_function"] = aggregate_function
    if filters:
        params["filters"] = filters

    resp = state.client.get(f"/v1/runs/{run_id}/result", params=params)
    output(resp.json(), state.output)


@runs.command()
@click.argument("new_run_id")
@click.argument("old_run_id")
@click.option(
    "--aggregate-function",
    type=click.Choice(["average", "min", "max", "median", "p90", "p95", "p99", "sum", "count"]),
    default=None,
    help="Aggregation function.",
)
@click.option("--filters", default=None, help="JSON-encoded filters.")
@pass_state
def compare(
    state: State,
    new_run_id: str,
    old_run_id: str,
    aggregate_function: Optional[str],
    filters: Optional[str],
) -> None:
    """Compare two experiment runs."""
    params: dict = {}
    if aggregate_function:
        params["aggregate_function"] = aggregate_function
    if filters:
        params["filters"] = filters

    resp = state.client.get(f"/v1/runs/{new_run_id}/compare-with/{old_run_id}", params=params)
    output(resp.json(), state.output)


@runs.command("compare-events")
@click.option("--run-id-1", required=True, help="First run ID.")
@click.option("--run-id-2", required=True, help="Second run ID.")
@click.option("--event-name", default=None, help="Filter by event name.")
@click.option("--event-type", default=None, help="Filter by event type.")
@click.option("--limit", type=int, default=None, help="Max results.")
@click.option("--page", type=int, default=None, help="Page number.")
@pass_state
def compare_events(
    state: State,
    run_id_1: str,
    run_id_2: str,
    event_name: Optional[str],
    event_type: Optional[str],
    limit: Optional[int],
    page: Optional[int],
) -> None:
    """Compare events between two experiment runs."""
    params: dict = {"run_id_1": run_id_1, "run_id_2": run_id_2}
    if event_name:
        params["event_name"] = event_name
    if event_type:
        params["event_type"] = event_type
    if limit is not None:
        params["limit"] = limit
    if page is not None:
        params["page"] = page

    resp = state.client.get("/v1/runs/compare/events", params=params)
    output(resp.json(), state.output)


@runs.command()
@click.option("--date-range", default=None, help="JSON-encoded date range.")
@click.option("--evaluation-id", default=None, help="Filter by evaluation ID.")
@pass_state
def schema(state: State, date_range: Optional[str], evaluation_id: Optional[str]) -> None:
    """Get experiment runs schema."""
    params: dict = {}
    if date_range:
        params["dateRange"] = date_range
    if evaluation_id:
        params["evaluation_id"] = evaluation_id

    resp = state.client.get("/v1/runs/schema", params=params)
    output(resp.json(), state.output)

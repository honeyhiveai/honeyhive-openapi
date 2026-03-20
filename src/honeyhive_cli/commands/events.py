"""Event commands."""

import json
from typing import Optional

import click

from honeyhive_cli.cli import State, pass_state
from honeyhive_cli.output import output


@click.group()
def events() -> None:
    """Manage events."""


@events.command("list")
@click.option("--limit", type=int, default=None, help="Max results (default 1000).")
@click.option("--page", type=int, default=None, help="Page number (default 1).")
@click.option("--filters", default=None, help="JSON-encoded filter array.")
@click.option("--date-range", default=None, help="JSON-encoded date range.")
@click.option("--projections", default=None, help="Comma-separated fields to include.")
@click.option("--evaluation-id", default=None, help="Filter by evaluation ID.")
@pass_state
def list_events(
    state: State,
    limit: Optional[int],
    page: Optional[int],
    filters: Optional[str],
    date_range: Optional[str],
    projections: Optional[str],
    evaluation_id: Optional[str],
) -> None:
    """Query events with filters and projections."""
    params: dict = {}
    if limit is not None:
        params["limit"] = limit
    if page is not None:
        params["page"] = page
    if filters:
        params["filters"] = filters
    if date_range:
        params["dateRange"] = date_range
    if projections:
        params["projections"] = projections
    if evaluation_id:
        params["evaluation_id"] = evaluation_id

    resp = state.client.get("/events", params=params)
    output(resp.json(), state.output)


@events.command()
@click.option("--event", "event_data", required=True, help="JSON-encoded event object.")
@pass_state
def create(state: State, event_data: str) -> None:
    """Create a new event."""
    try:
        json.loads(event_data)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"Invalid JSON for --event: {exc}") from exc

    resp = state.client.post("/events", json={"event": event_data})
    output(resp.json(), state.output)


@events.command()
@click.argument("event_id")
@click.option("--metadata", default=None, help="JSON-encoded metadata.")
@click.option("--feedback", default=None, help="JSON-encoded feedback.")
@click.option("--metrics", "metrics_data", default=None, help="JSON-encoded metrics.")
@click.option("--outputs", default=None, help="JSON-encoded outputs.")
@click.option("--config", "config_data", default=None, help="JSON-encoded config.")
@click.option("--user-properties", default=None, help="JSON-encoded user properties.")
@click.option("--duration", type=float, default=None, help="Duration in ms.")
@pass_state
def update(
    state: State,
    event_id: str,
    metadata: Optional[str],
    feedback: Optional[str],
    metrics_data: Optional[str],
    outputs: Optional[str],
    config_data: Optional[str],
    user_properties: Optional[str],
    duration: Optional[float],
) -> None:
    """Update an existing event."""
    body: dict = {"event_id": event_id}
    for key, raw in [
        ("metadata", metadata),
        ("feedback", feedback),
        ("metrics", metrics_data),
        ("outputs", outputs),
        ("config", config_data),
        ("user_properties", user_properties),
    ]:
        if raw:
            try:
                body[key] = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise click.ClickException(f"Invalid JSON for --{key}: {exc}") from exc
    if duration is not None:
        body["duration"] = duration

    resp = state.client.put("/events", json=body)
    output(resp.json(), state.output)


@events.command("get")
@click.argument("session_id")
@pass_state
def get_by_session(state: State, session_id: str) -> None:
    """Get nested events for a session."""
    resp = state.client.get(f"/v1/events/{session_id}")
    output(resp.json(), state.output)


@events.command()
@click.argument("event_id")
@click.confirmation_option(prompt="Are you sure you want to delete this event?")
@pass_state
def delete(state: State, event_id: str) -> None:
    """Delete an event by ID."""
    resp = state.client.delete(f"/v1/events/{event_id}")
    output(resp.json(), state.output)


@events.command()
@click.option("--project", required=True, help="Project name.")
@click.option("--filters", required=True, help="JSON-encoded filter array.")
@click.option("--date-range", default=None, help="JSON-encoded date range {$gte, $lte}.")
@click.option("--projections", default=None, help="Comma-separated fields.")
@click.option("--limit", type=int, default=None, help="Max results.")
@click.option("--page", type=int, default=None, help="Page number.")
@pass_state
def export(
    state: State,
    project: str,
    filters: str,
    date_range: Optional[str],
    projections: Optional[str],
    limit: Optional[int],
    page: Optional[int],
) -> None:
    """Export events based on filters (legacy)."""
    try:
        filters_parsed = json.loads(filters)
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"Invalid JSON for --filters: {exc}") from exc

    body: dict = {"project": project, "filters": filters_parsed}
    if date_range:
        try:
            body["dateRange"] = json.loads(date_range)
        except json.JSONDecodeError as exc:
            raise click.ClickException(f"Invalid JSON for --date-range: {exc}") from exc
    if projections:
        body["projections"] = [p.strip() for p in projections.split(",")]
    if limit is not None:
        body["limit"] = limit
    if page is not None:
        body["page"] = page

    resp = state.client.post("/v1/events/export", json=body)
    output(resp.json(), state.output)


@events.command()
@click.option("--date-range", default=None, help="JSON-encoded date range.")
@click.option("--filters", default=None, help="JSON-encoded filter array.")
@click.option("--metric", default=None, help="Metric to aggregate (default: duration).")
@click.option("--group-by", default=None, help="Field to group by.")
@click.option(
    "--bucket",
    type=click.Choice(["minute", "hour", "day", "week", "month", "1m", "1h", "1d", "1w", "1M"]),
    default=None,
    help="Time bucket.",
)
@click.option(
    "--aggregation",
    type=click.Choice(
        [
            "avg",
            "average",
            "mean",
            "p50",
            "p75",
            "p90",
            "p95",
            "p99",
            "count",
            "sum",
            "min",
            "max",
            "median",
        ]
    ),
    default=None,
    help="Aggregation function.",
)
@click.option("--evaluation-id", default=None, help="Filter by evaluation ID.")
@click.option("--only-experiments", is_flag=True, default=False, help="Only experiment events.")
@pass_state
def chart(
    state: State,
    date_range: Optional[str],
    filters: Optional[str],
    metric: Optional[str],
    group_by: Optional[str],
    bucket: Optional[str],
    aggregation: Optional[str],
    evaluation_id: Optional[str],
    only_experiments: bool,
) -> None:
    """Get charting data for events."""
    params: dict = {}
    if date_range:
        params["dateRange"] = date_range
    if filters:
        params["filters"] = filters
    if metric:
        params["metric"] = metric
    if group_by:
        params["groupBy"] = group_by
    if bucket:
        params["bucket"] = bucket
    if aggregation:
        params["aggregation"] = aggregation
    if evaluation_id:
        params["evaluation_id"] = evaluation_id
    if only_experiments:
        params["only_experiments"] = "true"

    resp = state.client.get("/v1/events/chart", params=params)
    output(resp.json(), state.output)

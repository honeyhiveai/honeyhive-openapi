"""Project commands."""

from typing import Optional

import click

from honeyhive_cli.cli import State, pass_state
from honeyhive_cli.output import output


@click.group()
def projects() -> None:
    """Manage projects."""


@projects.command("list")
@click.option("--name", default=None, help="Filter by project name.")
@pass_state
def list_projects(state: State, name: Optional[str]) -> None:
    """List all projects."""
    params: dict = {}
    if name:
        params["name"] = name

    resp = state.client.get("/v1/projects", params=params)
    data = resp.json()
    if state.output == "table" and isinstance(data, list):
        output(data, state.output, columns=["id", "name", "type", "created_at"])
    else:
        output(data, state.output)


@projects.command()
@click.option("--name", required=True, help="Project name.")
@click.option("--description", default=None, help="Project description.")
@click.option(
    "--type",
    "project_type",
    type=click.Choice(["evaluation", "completion"]),
    default=None,
    help="Project type.",
)
@pass_state
def create(
    state: State, name: str, description: Optional[str], project_type: Optional[str]
) -> None:
    """Create a new project."""
    body: dict = {"name": name}
    if description:
        body["description"] = description
    if project_type:
        body["type"] = project_type

    resp = state.client.post("/v1/projects", json=body)
    output(resp.json(), state.output)


@projects.command()
@click.option("--name", required=True, help="Current project name (identifier).")
@click.option("--new-name", default=None, help="New project name.")
@click.option("--description", default=None, help="New description.")
@click.option(
    "--type",
    "project_type",
    type=click.Choice(["evaluation", "completion"]),
    default=None,
    help="New project type.",
)
@pass_state
def update(
    state: State,
    name: str,
    new_name: Optional[str],
    description: Optional[str],
    project_type: Optional[str],
) -> None:
    """Update a project."""
    body: dict = {"name": name}
    if new_name:
        body["new_name"] = new_name
    if description is not None:
        body["description"] = description
    if project_type:
        body["type"] = project_type

    resp = state.client.put("/v1/projects", json=body)
    output(resp.json(), state.output)


@projects.command()
@click.option("--name", required=True, help="Project name to delete.")
@click.confirmation_option(prompt="Are you sure you want to delete this project?")
@pass_state
def delete(state: State, name: str) -> None:
    """Delete a project."""
    resp = state.client.delete("/v1/projects", params={"name": name})
    output(resp.json(), state.output)

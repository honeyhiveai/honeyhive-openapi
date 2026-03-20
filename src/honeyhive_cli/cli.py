"""HoneyHive CLI entry point."""

import click

from honeyhive_cli import __version__
from honeyhive_cli.client import HoneyHiveClient
from honeyhive_cli.config import get_api_key, get_base_url


class State:
    """Shared CLI state passed via Click context."""

    def __init__(self, api_key: str, base_url: str, output: str, verbose: bool) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.output = output
        self.verbose = verbose
        self._client: HoneyHiveClient | None = None

    @property
    def client(self) -> HoneyHiveClient:
        if self._client is None:
            if not self.api_key:
                raise click.ClickException(
                    "No API key configured. Run `hh auth login` or set HH_API_KEY."
                )
            self._client = HoneyHiveClient(
                api_key=self.api_key,
                base_url=self.base_url,
                verbose=self.verbose,
            )
        return self._client


pass_state = click.make_pass_decorator(State)


@click.group()
@click.version_option(__version__, prog_name="honeyhive-cli")
@click.option("--api-key", envvar="HH_API_KEY", default=None, help="API key override.")
@click.option("--base-url", default=None, help="API base URL override.")
@click.option(
    "--output",
    "output_fmt",
    type=click.Choice(["json", "table"]),
    default="json",
    help="Output format.",
)
@click.option("--verbose", is_flag=True, default=False, help="Enable verbose output.")
@click.pass_context
def cli(ctx: click.Context, api_key: str, base_url: str, output_fmt: str, verbose: bool) -> None:
    """HoneyHive CLI - manage sessions, events, datasets, experiments and more."""
    ctx.ensure_object(dict)
    ctx.obj = State(
        api_key=get_api_key(api_key),
        base_url=get_base_url(base_url),
        output=output_fmt,
        verbose=verbose,
    )


# Register sub-command groups
from honeyhive_cli.commands.auth import auth  # noqa: E402
from honeyhive_cli.commands.configurations import configurations  # noqa: E402
from honeyhive_cli.commands.datapoints import datapoints  # noqa: E402
from honeyhive_cli.commands.datasets import datasets  # noqa: E402
from honeyhive_cli.commands.events import events  # noqa: E402
from honeyhive_cli.commands.metrics import metrics  # noqa: E402
from honeyhive_cli.commands.projects import projects  # noqa: E402
from honeyhive_cli.commands.runs import runs  # noqa: E402
from honeyhive_cli.commands.sessions import sessions  # noqa: E402

cli.add_command(auth)
cli.add_command(sessions)
cli.add_command(events)
cli.add_command(metrics)
cli.add_command(datapoints)
cli.add_command(datasets)
cli.add_command(projects)
cli.add_command(runs)
cli.add_command(configurations)

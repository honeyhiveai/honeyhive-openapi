"""Auth commands for configuring API credentials."""

import click

from honeyhive_cli.config import DEFAULT_BASE_URL, load_config, save_config


@click.group()
def auth() -> None:
    """Manage authentication and configuration."""


@auth.command()
@click.option("--api-key", prompt="API Key", hide_input=True, help="Your HoneyHive API key.")
@click.option(
    "--base-url",
    prompt="Base URL",
    default=DEFAULT_BASE_URL,
    show_default=True,
    help="HoneyHive API base URL.",
)
def login(api_key: str, base_url: str) -> None:
    """Save API credentials to ~/.honeyhive/config.json."""
    config = load_config()
    config["api_key"] = api_key
    config["base_url"] = base_url.rstrip("/")
    save_config(config)
    click.secho("Credentials saved.", fg="green")


@auth.command()
def status() -> None:
    """Show current authentication status."""
    config = load_config()
    api_key = config.get("api_key")
    base_url = config.get("base_url", DEFAULT_BASE_URL)

    if api_key:
        masked = api_key[:4] + "..." + api_key[-4:] if len(api_key) > 8 else "****"
        click.echo(f"API Key: {masked}")
    else:
        click.echo("API Key: not configured")
    click.echo(f"Base URL: {base_url}")


@auth.command()
def logout() -> None:
    """Remove saved credentials."""
    config = load_config()
    config.pop("api_key", None)
    save_config(config)
    click.secho("Credentials removed.", fg="yellow")

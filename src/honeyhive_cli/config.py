"""Configuration management for HoneyHive CLI."""

import json
import os
from pathlib import Path
from typing import Optional

CONFIG_DIR = Path.home() / ".honeyhive"
CONFIG_FILE = CONFIG_DIR / "config.json"

DEFAULT_BASE_URL = "https://api.honeyhive.ai"


def _ensure_config_dir() -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_config() -> dict:
    """Load configuration from disk."""
    if not CONFIG_FILE.exists():
        return {}
    try:
        return json.loads(CONFIG_FILE.read_text())
    except (json.JSONDecodeError, OSError):
        return {}


def save_config(config: dict) -> None:
    """Persist configuration to disk."""
    _ensure_config_dir()
    CONFIG_FILE.write_text(json.dumps(config, indent=2) + "\n")
    CONFIG_FILE.chmod(0o600)


def get_api_key(override: Optional[str] = None) -> Optional[str]:
    """Resolve API key from override > env > config file."""
    if override:
        return override
    env_key = os.environ.get("HH_API_KEY") or os.environ.get("HONEYHIVE_API_KEY")
    if env_key:
        return env_key
    return load_config().get("api_key")


def get_base_url(override: Optional[str] = None) -> str:
    """Resolve base URL from override > env > config file > default."""
    if override:
        return override.rstrip("/")
    env_url = os.environ.get("HH_API_URL") or os.environ.get("HONEYHIVE_API_URL")
    if env_url:
        return env_url.rstrip("/")
    return load_config().get("base_url", DEFAULT_BASE_URL).rstrip("/")

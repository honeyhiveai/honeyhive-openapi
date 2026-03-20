"""HTTP client for the HoneyHive API."""

from typing import Any, Optional

import click
import httpx


class HoneyHiveClient:
    """Thin wrapper around httpx for HoneyHive API calls."""

    def __init__(self, api_key: str, base_url: str, verbose: bool = False) -> None:
        self.base_url = base_url
        self.verbose = verbose
        self._client = httpx.Client(
            base_url=base_url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            timeout=30.0,
        )

    def _log(self, method: str, path: str, **kwargs: Any) -> None:
        if self.verbose:
            click.secho(f"  {method} {self.base_url}{path}", fg="cyan", err=True)
            if "json" in kwargs and kwargs["json"]:
                click.secho(f"  Body: {kwargs['json']}", fg="cyan", err=True)
            if "params" in kwargs and kwargs["params"]:
                click.secho(f"  Params: {kwargs['params']}", fg="cyan", err=True)

    def request(
        self,
        method: str,
        path: str,
        *,
        json: Optional[dict] = None,
        params: Optional[dict] = None,
    ) -> httpx.Response:
        """Make an HTTP request and return the response.

        Raises click.ClickException on HTTP errors.
        """
        self._log(method, path, json=json, params=params)
        # Strip None values from params
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        try:
            resp = self._client.request(method, path, json=json, params=params)
        except httpx.RequestError as exc:
            raise click.ClickException(f"Request failed: {exc}") from exc

        if self.verbose:
            click.secho(f"  Status: {resp.status_code}", fg="cyan", err=True)

        if resp.status_code >= 400:
            try:
                detail = resp.json()
            except Exception:
                detail = resp.text
            raise click.ClickException(f"API error {resp.status_code}: {detail}")
        return resp

    def get(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("DELETE", path, **kwargs)

    def close(self) -> None:
        self._client.close()

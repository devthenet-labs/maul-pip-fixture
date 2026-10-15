"""A tiny package for patchy's egress-proxy tunnel gate (pip through a CONNECT tunnel)."""

import requests


def build_url(base: str, params: dict[str, str]) -> str:
    """Return base with params encoded as its query string, as requests would send it."""
    return requests.Request("GET", base, params=params).prepare().url

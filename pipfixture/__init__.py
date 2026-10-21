"""A tiny package for maul's egress-proxy tunnel gate (pip through a CONNECT tunnel)."""

import requests
from slugify import slugify


def build_url(base: str, params: dict[str, str]) -> str:
    """Return base with params encoded as its query string, as requests would send it."""
    return requests.Request("GET", base, params=params).prepare().url


def slugify_title(title: str) -> str:
    """Return title as a URL slug."""
    return slugify(title)

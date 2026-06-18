"""Main entry point for mlcheck inspections."""

from typing import Any


def inspect(obj: Any) -> dict:
    """Placeholder inspect function returning a simple report dict."""
    return {"type": type(obj).__name__, "ok": True}

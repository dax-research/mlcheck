"""General helper functions."""


def ensure_list(x):
    """Convert a value to a list, preserving an empty list for None."""
    if x is None:
        return []
    return list(x)

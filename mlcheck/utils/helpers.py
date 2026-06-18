"""General helper functions."""


def ensure_list(x):
    if x is None:
        return []
    return list(x)

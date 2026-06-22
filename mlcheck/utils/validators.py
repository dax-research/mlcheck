"""Validation helpers."""


def is_dataframe(obj):
    """Return True if the object is a pandas DataFrame."""
    try:
        import pandas as pd
    except ImportError:
        return False

    return isinstance(obj, pd.DataFrame)

"""Leakage detection utilities."""
import pandas as pd
from mlcheck.models.issue import Issue


def check_leakage(df: pd.DataFrame, target=None):
    """
    Detect features that are identical to the target column.
    """

    if target is None or target not in df.columns:
        return None

    leaked_columns = []

    target_series = df[target]

    for column in df.columns:
        if column == target:
            continue

        if df[column].equals(target_series):
            leaked_columns.append(column)

    if not leaked_columns:
        return None

    return Issue(
        name="target_leakage",
        severity="high",
        details={
            "target": target,
            "columns": leaked_columns,
        },
    )
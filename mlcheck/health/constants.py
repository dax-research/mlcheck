import pandas as pd
from mlcheck.models.issue import Issue


def check_constants(df: pd.DataFrame, target=None):
    """
    Detect constant columns (same value everywhere).
    """

    constant_cols = []

    for col in df.columns:
        if df[col].nunique(dropna=False) == 1:
            constant_cols.append(col)

    if not constant_cols:
        return None

    return Issue(
        name="constant_columns",
        severity="medium",
        details={
            "columns": constant_cols
        }
    )

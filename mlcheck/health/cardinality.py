import pandas as pd
from mlcheck.models.issue import Issue
from pandas.api.types import (
    is_object_dtype,
    is_string_dtype,
)
from mlcheck.config import (
    MEDIUM_CARDINALITY_THRESHOLD,
    HIGH_CARDINALITY_THRESHOLD,
)

def check_cardinality(df: pd.DataFrame, target=None):
    """
    Detect categorical features with high cardinality.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.
    target : str, optional
        Target column name. It is excluded from the analysis.

    Returns
    -------
    Issue or None
        An Issue object if high-cardinality columns are found,
        otherwise None.
    """

    columns_info = []
    overall_severity = "medium"

    for column in df.columns:
        # Skip target column
        if target is not None and column == target:
            continue

        # Analyze only object/string columns
        if not (
            is_object_dtype(df[column])
            or is_string_dtype(df[column])
        ):
            continue

        unique_count = df[column].nunique(dropna=True)

        if unique_count >= HIGH_CARDINALITY_THRESHOLD:
            severity = "high"
            overall_severity = "high"
        elif unique_count >= MEDIUM_CARDINALITY_THRESHOLD:
            severity = "medium"
        else:
            continue

        columns_info.append(
            {
                "column": column,
                "unique_values": int(unique_count),
                "severity": severity,
            }
        )

    if not columns_info:
        return None
    

    return Issue(
        name="high_cardinality",
        severity=overall_severity,
        details={
            "columns": columns_info,
        },
    )
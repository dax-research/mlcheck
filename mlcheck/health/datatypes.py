"""Data types checks and inference."""

import pandas as pd
from pandas.api.types import is_object_dtype, is_string_dtype
from mlcheck.models.issue import Issue

def check_datatypes(df: pd.DataFrame, target=None):
    """
    Detect suspicious data type issues.

    Checks:
    - Mixed Python types in a column (high severity)
    - Numeric values stored as strings (medium severity)

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.
    target : str, optional
        Unused. Included for API consistency.

    Returns
    -------
    Issue or None
        An Issue object if datatype problems are found,
        otherwise None.
    """

    detected = []
    overall_severity = "medium"

    for column in df.columns:
        series = df[column].dropna()

        # Skip empty columns
        if series.empty:
            continue

        # -------------------------
        # Check for mixed types
        # -------------------------
        python_types = series.map(type).unique()

        if len(python_types) > 1:
            detected.append(
                {
                    "column": column,
                    "issue": "mixed_types",
                    "severity": "high",
                }
            )
            overall_severity = "high"
            continue

        # -------------------------
        # Check for numeric strings
        # -------------------------
        if is_object_dtype(series) or is_string_dtype(series):
            converted = pd.to_numeric(series, errors="coerce")

            # If every non-null value can be converted,
            # it's likely numeric data stored as strings.
            if converted.notna().all():
                detected.append(
                    {
                        "column": column,
                        "issue": "numeric_stored_as_string",
                        "severity": "medium",
                    }
                )

    if not detected:
        return None

    return Issue(
        name="datatype_issues",
        severity=overall_severity,
        details={
            "columns": detected,
        },
    )
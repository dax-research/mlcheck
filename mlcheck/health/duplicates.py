import pandas as pd
from mlcheck.models.issue import Issue


def check_duplicates(df: pd.DataFrame, target=None):
    """
    Detect duplicate rows in dataset.
    """

    dup_count = df.duplicated().sum()

    if dup_count == 0:
        return None

    severity = "low"
    if dup_count > len(df) * 0.1:
        severity = "high"
    elif dup_count > len(df) * 0.05:
        severity = "medium"

    return Issue(
        name="duplicates",
        severity=severity,
        details={
            "duplicate_rows": int(dup_count),
            "percentage": round((dup_count / len(df)) * 100, 2)
        }
    )

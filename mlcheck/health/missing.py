import pandas as pd
from mlcheck.models.issue import Issue


def check_missing(df: pd.DataFrame, target=None):
    """
    Detect missing values in the dataset.

    Returns:
        Issue object if missing values exist, else None
    """

    # count missing values per column
    missing_counts = df.isnull().sum()

    # keep only columns with missing values
    missing_counts = missing_counts[missing_counts > 0]

    # if no missing values → return None
    if missing_counts.empty:
        return None

    total_rows = len(df)

    details = {}

    for col, count in missing_counts.items():
        details[col] = {
            "missing_count": int(count),
            "percentage": round((count / total_rows) * 100, 2)
        }

    # severity logic (simple but useful)
    max_percentage = max(v["percentage"] for v in details.values())

    if max_percentage < 5:
        severity = "low"
    elif max_percentage < 20:
        severity = "medium"
    else:
        severity = "high"

    return Issue(
        name="missing_values",
        severity=severity,
        details=details
    )
import pandas as pd
from mlcheck.models.issue import Issue
from mlcheck.config import MEDIUM_MISSING_THRESHOLD
from mlcheck.config import LOW_MISSING_THRESHOLD


def check_missing(df: pd.DataFrame, target=None):
    """
    Detect missing values in the dataset.

    Returns:
        Issue object if missing values exist, else None
    """

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        return None

    details = {}
    total = len(df)

    for col, count in missing.items():
        details[col] = {
            "missing_count": int(count),
            "percentage": round((count / total) * 100, 2)
        }

    max_pct = max(v["percentage"] for v in details.values())

    if max_pct < LOW_MISSING_THRESHOLD:
        severity = "low"
    elif max_pct < MEDIUM_MISSING_THRESHOLD:
        severity = "medium"
    else:
        severity = "high"

    return Issue(
        name="missing_values",
        severity=severity,
        details=details
    )

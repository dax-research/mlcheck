import pandas as pd

from mlcheck.models.issue import Issue
from mlcheck.config import CORRELATION_THRESHOLD

def check_correlations(df: pd.DataFrame, target=None):
    """
    Detect highly correlated numeric feature pairs.

    Correlation severity:
        - Medium: 0.80 <= |r| < 0.90
        - High:   |r| >= 0.90

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.
    target : str, optional
        Name of the target column. If provided, it is excluded from
        correlation analysis.

    Returns
    -------
    Issue or None
        An Issue object containing correlated feature pairs if any are
        detected, otherwise None.
    """

    # Select only numeric columns
    numeric_df = df.select_dtypes(include="number")

    # Exclude target column
    if target is not None and target in numeric_df.columns:
        numeric_df = numeric_df.drop(columns=[target])

    # Need at least two numeric columns
    if numeric_df.shape[1] < 2:
        return None

    # Compute absolute correlation matrix
    corr_matrix = numeric_df.corr().abs()

    pairs = []
    overall_severity = "medium"

    columns = corr_matrix.columns

    # Iterate over upper triangle only
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            corr_value = float(corr_matrix.iloc[i, j])

            # Ignore weak correlations
            if corr_value < 0.80:
                continue

            # Determine severity
            if corr_value >= CORRELATION_THRESHOLD:
                severity = "high"
                overall_severity = "high"
            else:
                severity = "medium"

            pairs.append(
                {
                    "feature_1": columns[i],
                    "feature_2": columns[j],
                    "correlation": round(corr_value, 4),
                    "severity": severity,
                }
            )

    if not pairs:
        return None

    return Issue(
        name="high_correlation",
        severity=overall_severity,
        details={
            "pairs": pairs,
        },
    )
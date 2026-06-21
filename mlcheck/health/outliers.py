"""Outlier detection utilities."""

import pandas as pd
from mlcheck.models.issue import Issue
from mlcheck.config import DEFAULT_IQR_MULTIPLIER

def check_outliers(df: pd.DataFrame, target=None):
    """
    Detect outliers in numeric features using the IQR method.

    Severity:
        - Medium: 5% to <10% outliers
        - High: >=10% outliers

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.
    target : str, optional
        Target column name. It is excluded from analysis.

    Returns
    -------
    Issue or None
        An Issue object if outliers are detected, otherwise None.
    """

    columns_info = []
    overall_severity = "medium"

    numeric_df = df.select_dtypes(include="number")

    if target is not None and target in numeric_df.columns:
        numeric_df = numeric_df.drop(columns=[target])

    for column in numeric_df.columns:
        q1 = numeric_df[column].quantile(0.25)
        q3 = numeric_df[column].quantile(0.75)
        iqr = q3 - q1

        # Skip constant columns
        if iqr == 0:
            continue

        lower_bound = q1 - DEFAULT_IQR_MULTIPLIER * iqr
        upper_bound = q3 + DEFAULT_IQR_MULTIPLIER * iqr

        outlier_count = (
            (numeric_df[column] < lower_bound)
            | (numeric_df[column] > upper_bound)
        ).sum()

        outlier_percentage = (outlier_count / len(numeric_df)) * 100

        if outlier_percentage >= 10:
            severity = "high"
            overall_severity = "high"
        elif outlier_percentage >= 5:
            severity = "medium"
        else:
            continue

        columns_info.append(
            {
                "column": column,
                "outlier_count": int(outlier_count),
                "outlier_percentage": round(outlier_percentage, 2),
                "severity": severity,
            }
        )

    if not columns_info:
        return None

    return Issue(
        name="outliers",
        severity=overall_severity,
        details={
            "columns": columns_info,
        },
    )
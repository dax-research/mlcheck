import pandas as pd
from mlcheck.models.issue import Issue
from mlcheck.config import HIGH_IMBALANCE_THRESHOLD
from mlcheck.config import MEDIUM_IMBALANCE_THRESHOLD


def check_imbalance(df: pd.DataFrame, target=None):
    """
        Detect class imbalance in the target column.

        This function analyzes the distribution of classes in the specified
        target column and reports an issue if one class dominates the dataset.

        Severity levels:
            - Medium: Majority class is between 70% and 80%.
            - High: Majority class is 80% or greater.

        Parameters
        ----------
        df : pandas.DataFrame
            The input dataset.
        target : str, optional
            Name of the target column. If not provided or not found,
            the imbalance check is skipped.

        Returns
        -------
        Issue or None
            An Issue object describing the detected class imbalance if one
            exists. Returns None if the dataset is balanced or if no valid
            target column is specified.
    """
        
    if target is None or target not in df.columns:
        return None

    distribution = df[target].value_counts(normalize=True)
    majority_class = distribution.idxmax()
    majority_ratio = float(distribution.max())  # e.g. 0.75

    # Determine severity
    if majority_ratio >= HIGH_IMBALANCE_THRESHOLD:
        severity = "high"
    elif majority_ratio >= MEDIUM_IMBALANCE_THRESHOLD:
        severity = "medium"
    else:
        return None  # Considered balanced

    return Issue(
        name="class_imbalance",
        severity=severity,
        details={
            "target": target,
            "majority_class": majority_class,
            "majority_percentage": round(majority_ratio * 100, 2),
            "class_distribution": {
                str(label): round(ratio * 100, 2)
                for label, ratio in distribution.items()
            },
        },
    )
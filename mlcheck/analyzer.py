from mlcheck.health import HEALTH_CHECKS
from mlcheck.report import MLReport


def inspect(df, target=None):
    """
    Run the MLCheck pipeline on a dataset and return an MLReport.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataset to inspect.
    target : str, optional
        The name of the target column in the dataset. If specified, the target
        column is excluded from the feature count and some checks are performed
        with the target in mind.

    Returns
    -------
    mlcheck.report.MLReport
        A report object containing detected issues, recommendations, and export helpers.

    Notes
    -----
    This function executes every check registered in `mlcheck.health.HEALTH_CHECKS`.
    If a check raises an exception, the pipeline continues and logs a warning.
    """

    issues = []

    for check in HEALTH_CHECKS:
        try:
            issue = check(df, target)
            if issue is not None:
                issues.append(issue)

        except Exception as e:
            print(f"[MLCheck Warning] {check.__name__} failed: {e}")
    
    return MLReport(df=df, target=target, issues=issues)
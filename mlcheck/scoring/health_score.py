"""Compute a simple health score for a report."""

SEVERITY_PENALTY = {
    "high": 20,
    "medium": 10,
}

def calculate_health_score(issues):
    """
    Calculate a health score for a dataset.

    Parameters
    ----------
    issues : list
        List of Issue objects.

    Returns
    -------
    int
        Health score between 0 and 100.
    """
    score = 100

    for issue in issues:
        score -= SEVERITY_PENALTY.get(issue.severity.lower(), 0)

    return max(score, 0)
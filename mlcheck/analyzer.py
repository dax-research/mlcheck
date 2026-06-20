from mlcheck.health import HEALTH_CHECKS
from mlcheck.report import MLReport


def inspect(df, target=None):
    """
    Main MLCheck pipeline entry point.
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
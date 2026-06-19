from .health import HEALTH_CHECKS
from .report import MLReport


def inspect(df, target=None):
    """
    Main entry point of MLCheck.

    Steps:
    1. Run all health checks
    2. Collect issues
    3. Build MLReport
    4. Return report object
    """

    issues = []

    # Run each health check
    for check in HEALTH_CHECKS:
        try:
            result = check(df, target)

            if result is not None:
                issues.append(result)

        except Exception as e:
            # Optional: don't crash full pipeline if one check fails
            print(f"[MLCheck Warning] {check.__name__} failed: {e}")

    # Create report object
    report = MLReport(
        df=df,
        target=target,
        issues=issues
    )

    return report
import pandas as pd
from mlcheck.health.missing import check_missing


def test_missing_detected():
    df = pd.DataFrame({
        "a": [1, None, 3],
        "b": [4, 5, None]
    })

    issue = check_missing(df)

    assert issue is not None
    assert issue.name == "missing_values"
    assert "a" in issue.details
    assert "b" in issue.details


def test_no_missing():
    df = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    })

    issue = check_missing(df)

    assert issue is None
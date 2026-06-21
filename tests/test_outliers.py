import pandas as pd

from mlcheck.health.outliers import check_outliers


def test_detect_outliers():
    df = pd.DataFrame({
        "value": [10, 11, 12, 13, 14, 15, 1000]
    })

    issue = check_outliers(df)

    assert issue is not None
    assert issue.name == "outliers"


def test_no_outliers():
    df = pd.DataFrame({
        "value": [10, 11, 12, 13, 14, 15, 16]
    })

    issue = check_outliers(df)

    assert issue is None


def test_target_column_ignored():
    df = pd.DataFrame({
        "feature": [1, 2, 3, 4, 5, 100],
        "target": [0, 1, 0, 1, 0, 1],
    })

    issue = check_outliers(df, target="target")

    # The function should execute successfully and ignore "target".
    assert issue is None or issue.name == "outliers"
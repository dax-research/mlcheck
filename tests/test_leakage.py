import pandas as pd

from mlcheck.health.leakage import check_leakage


def test_detect_target_leakage():
    df = pd.DataFrame({
        "feature": [1, 2, 3, 4],
        "target": [0, 1, 0, 1],
        "target_copy": [0, 1, 0, 1],
    })

    issue = check_leakage(df, target="target")

    assert issue is not None
    assert issue.name == "target_leakage"
    assert issue.severity == "high"
    assert "target_copy" in issue.details["columns"]


def test_no_target_leakage():
    df = pd.DataFrame({
        "feature": [1, 2, 3, 4],
        "target": [0, 1, 0, 1],
    })

    issue = check_leakage(df, target="target")

    assert issue is None


def test_no_target_provided():
    df = pd.DataFrame({
        "feature": [1, 2, 3, 4],
    })

    issue = check_leakage(df)

    assert issue is None
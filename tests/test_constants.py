import pandas as pd
from mlcheck.health.constants import check_constants


def test_constant_column_detected():
    df = pd.DataFrame({
        "age": [25, 30, 35],
        "country": ["India", "India", "India"],  # Constant column
    })

    issue = check_constants(df)

    assert issue is not None
    assert issue.name == "constant_columns"
    assert "country" in issue.details["columns"]


def test_no_constant_columns():
    df = pd.DataFrame({
        "age": [25, 30, 35],
        "country": ["India", "USA", "Canada"],
    })

    issue = check_constants(df)

    assert issue is None


def test_multiple_constant_columns():
    df = pd.DataFrame({
        "a": [1, 1, 1],
        "b": ["x", "x", "x"],
        "c": [10, 20, 30],
    })

    issue = check_constants(df)

    assert issue is not None
    assert set(issue.details["columns"]) == {"a", "b"}

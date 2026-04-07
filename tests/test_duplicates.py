import pandas as pd
from mlcheck.health.duplicates import check_duplicates


def test_duplicates_found():
    df = pd.DataFrame({
        "a": [1, 1, 2],
        "b": [3, 3, 4]
    })

    issue = check_duplicates(df)

    assert issue is not None
    assert issue.name == "duplicates"
    assert "duplicate_rows" in issue.details


def test_no_duplicates():
    df = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    })

    issue = check_duplicates(df)

    assert issue is None

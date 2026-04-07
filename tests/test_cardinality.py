import pandas as pd

from mlcheck.health.cardinality import check_cardinality


def test_high_cardinality():
    df = pd.DataFrame({
        "user_id": [f"user_{i}" for i in range(150)]
    })



    issue = check_cardinality(df)

    assert issue is not None
    assert issue.name == "high_cardinality"
    assert issue.severity == "high"


def test_medium_cardinality():
    df = pd.DataFrame({
        "city": [f"city_{i}" for i in range(60)]
    })

    issue = check_cardinality(df)

    assert issue is not None
    assert issue.severity == "medium"


def test_no_cardinality_issue():
    df = pd.DataFrame({
        "color": ["red", "blue", "green", "red", "blue"]
    })

    issue = check_cardinality(df)

    assert issue is None

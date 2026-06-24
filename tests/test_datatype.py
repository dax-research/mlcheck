import pandas as pd

from mlcheck.health.datatypes import check_datatypes


def test_numeric_strings():
    df = pd.DataFrame({
        "age": ["10", "20", "30", "40"]
    })

    issue = check_datatypes(df)

    assert issue is not None
    assert issue.name == "datatype_issues"
    assert issue.severity == "medium"


def test_mixed_types():
    df = pd.DataFrame({
        "age": [10, "20", 30, "40"]
    })

    issue = check_datatypes(df)

    assert issue is not None
    assert issue.name == "datatype_issues"
    assert issue.severity == "high"


def test_normal_numeric_column():
    df = pd.DataFrame({
        "age": [10, 20, 30, 40]
    })

    issue = check_datatypes(df)

    assert issue is None


def test_normal_string_column():
    df = pd.DataFrame({
        "city": ["Ahmedabad", "Surat", "Vadodara"]
    })

    issue = check_datatypes(df)

    assert issue is None

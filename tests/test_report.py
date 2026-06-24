import pandas as pd

from mlcheck.models.issue import Issue
from mlcheck.report import MLReport


def test_to_dict():
    df = pd.DataFrame({
        "a": [1, 2, 3],
        "target": [0, 1, 0],
    })

    issues = [
        Issue(
            name="missing_values",
            severity="medium",
            details={"count": 2},
        )
    ]

    report = MLReport(df, target="target", issues=issues)

    result = report.to_dict()

    assert result["rows"] == 3
    assert result["features"] == 1
    assert result["target"] == "target"
    assert result["issue_count"] == 1
    assert result["issues"][0]["name"] == "missing_values"


def test_summary_runs(capsys):
    df = pd.DataFrame({
        "a": [1, 2, 3],
    })

    report = MLReport(df)

    report.summary()

    captured = capsys.readouterr()

    assert "MLCheck Report" in captured.out
    assert "Rows" in captured.out


def test_empty_report():
    df = pd.DataFrame({
        "x": [1, 2],
    })

    report = MLReport(df)

    result = report.to_dict()

    assert result["issue_count"] == 0
    assert result["issues"] == []

import json

import pandas as pd

from mlcheck import inspect


def make_report():
    df = pd.DataFrame({
        "a": [1, 2, 3],
        "target": [0, 1, 0],
    })

    return inspect(df, target="target")


def test_to_json_valid():
    report = make_report()
    s = report.to_json()
    parsed = json.loads(s)

    assert parsed["rows"] == 3
    assert "issues" in parsed


def test_to_markdown_contains_header():
    report = make_report()
    md = report.to_markdown()

    assert "# MLCheck Report" in md
    assert "Dataset Information" in md


def test_to_html_contains_elements():
    report = make_report()
    html = report.to_html()

    assert "<h1>MLCheck Report</h1>" in html
    # older renderer used <ul>, newer styled renderer uses tables — accept either
    assert ("<ul>" in html) or ("<table>" in html)


def test_console_renders(capsys):
    report = make_report()
    from mlcheck.reporting import console

    console.render(report.to_dict())
    captured = capsys.readouterr()

    # JSON keys should be present in output
    assert '"rows"' in captured.out or "Rows" in captured.out

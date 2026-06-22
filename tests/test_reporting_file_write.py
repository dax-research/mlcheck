import json
from pathlib import Path

import pandas as pd

from mlcheck import inspect


def make_report():
    df = pd.DataFrame({"a": [1, 2, 3], "target": [0, 1, 0]})
    return inspect(df, target="target")


def test_to_file_json(tmp_path):
    report = make_report()
    p = tmp_path / "report.json"
    report.to_file(str(p))

    assert p.exists()
    parsed = json.loads(p.read_text(encoding="utf-8"))
    assert parsed["rows"] == 3


def test_to_file_markdown(tmp_path):
    report = make_report()
    p = tmp_path / "report.md"
    report.to_file(str(p))

    assert p.exists()
    content = p.read_text(encoding="utf-8")
    assert "# MLCheck Report" in content


def test_to_file_html(tmp_path):
    report = make_report()
    p = tmp_path / "report.html"
    report.to_file(str(p))

    assert p.exists()
    content = p.read_text(encoding="utf-8")
    assert "<h1>MLCheck Report</h1>" in content

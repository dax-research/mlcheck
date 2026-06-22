# mlcheck

`mlcheck` is a lightweight Python library for quickly auditing datasets and getting actionable insights
before training machine learning models. It detects common data problems (missing values, class imbalance,
high cardinality, potential leakage, etc.), scores dataset health, and produces human-friendly reports and
recommendations.

## Features

- Run a suite of data health checks over a pandas DataFrame
- Produce a concise human-readable summary and structured report
- Compute a dataset health score
- Generate recommendations mapping issues to remediation steps
- Export reports as JSON, Markdown, or HTML and write them to disk

## Installation

Install from source (development):

```bash
python -m pip install -r requirements-dev.txt
python -m pip install -e .
```

## Quickstart

Basic usage with a pandas DataFrame:

```python
import pandas as pd
from mlcheck import inspect

df = pd.DataFrame({
	"age": [20, 21, 22, 23, 24],
	"label": [0, 0, 0, 0, 1]
})

report = inspect(df, target="label")

report.summary()                # print a human readable summary
print(report.health_score())     # numeric health score
print(report.to_markdown())      # markdown formatted report
print(report.to_html())          # HTML formatted report
report.to_file("reports/report.md")
```

## API (high level)

- `inspect(df, target=None)` — run health checks and return an `MLReport` instance
- `MLReport.summary()` — print a short human-readable summary
- `MLReport.to_dict()` — get a Python dict representation
- `MLReport.to_json()` / `to_markdown()` / `to_html()` — renderers for different formats
- `MLReport.to_file(path, format=None)` — write report to disk (infers format from extension)
- `MLReport.download_summary(path="mlcheck_summary.txt")` — save the textual summary to disk
- `MLReport.health_score()` — compute numeric health score (0–100)
- `MLReport.show_issues()` / `MLReport.issues()` — inspect detected issues
- `MLReport.recommendations()` — get remediation suggestions

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository and create a feature branch.
2. Run tests and linters locally.
3. Open a pull request describing your change.

See `CONTRIBUTING.md` for more details.

## License

This project is licensed under the terms in the `LICENSE` file.

---

If you'd like, I can help prepare `pyproject.toml` packaging metadata and a short release checklist for PyPI.

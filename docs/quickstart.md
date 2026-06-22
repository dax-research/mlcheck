# Quickstart

This quickstart shows how to use `mlcheck` with a pandas DataFrame.

```python
import pandas as pd
from mlcheck import inspect

# Create a sample dataset

df = pd.DataFrame({
    "age": [20, 21, 22, 23, 24],
    "label": [0, 0, 0, 0, 1],
})

report = inspect(df, target="label")
```

## Print a summary

```python
report.summary()
```

## Get the health score

```python
score = report.health_score()
print(f"Health score: {score}")
```

## Export report formats

```python
json_text = report.to_json()
markdown_text = report.to_markdown()
html_text = report.to_html()
```

## Save reports to disk

```python
report.to_file("reports/report.json")
report.to_file("reports/report.md")
report.to_file("reports/report.html")
report.download_summary("reports/summary.txt")
```

## Inspect issues and recommendations

```python
report.show_issues()
print(report.recommendations())
```

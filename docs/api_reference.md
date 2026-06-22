# API Reference

The public API for `mlcheck` is centered around the `inspect()` entrypoint and the returned `MLReport` object.

## `mlcheck.inspect(df, target=None)`

Run the full ML health check pipeline on a pandas DataFrame.

- `df` — pandas `DataFrame` to analyze.
- `target` — optional target column name.

Returns an `MLReport` object.

## `MLReport`

The `MLReport` object exposes the following methods.

### `summary()`

Print a human-readable summary of the dataset and detected issues.

### `get_summary_text()`

Return the same summary text as a string without printing it.

### `health_score()`

Return a numeric health score between 0 and 100.

### `to_dict()`

Return the report as a standard Python dictionary.

### `to_json()`

Return the report as a JSON-formatted string.

### `to_markdown()`

Return the report rendered as Markdown.

### `to_html()`

Return the report rendered as HTML.

### `to_file(path, format=None)`

Write the report to disk. If `format` is omitted, the file extension is used to infer the output format.

Supported formats:

- `json`
- `markdown`
- `html`

### `download_summary(path="mlcheck_summary.txt")`

Write the textual summary to a file and return the written path.

### `issues()`

Return the raw list of detected issue objects.

### `show_issues()`

Print the detected issues to the console.

### `recommendations()`

Return a list of remediation recommendations derived from detected issues.

## Reporting helpers

`mlcheck.reporting` provides renderer modules for each supported output format.

- `mlcheck.reporting.json.render(report)`
- `mlcheck.reporting.markdown.render(report)`
- `mlcheck.reporting.html.render(report)`
- `mlcheck.reporting.console.render(report)`

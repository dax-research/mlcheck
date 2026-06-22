"""Console reporter that pretty-prints the report to stdout."""

from mlcheck.reporting import json as reporting_json


def render(report):
    """Render the report to stdout using the JSON reporter."""
    print(reporting_json.render(report))

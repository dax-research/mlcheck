"""HTML reporter for MLCheck reports."""

from html import escape


def render(report):
    """Render a report as an HTML document string."""
    parts = [
        "<!doctype html>",
        "<html>",
        "<head>",
        "<meta charset='utf-8' />",
        "<title>MLCheck Report</title>",
        "<style>",
        "body{font-family:Arial,Helvetica,sans-serif;margin:20px;color:#333}",
        "h1{color:#2b6cb0}",
        "table{border-collapse:collapse;width:100%;margin-bottom:16px}",
        "th,td{border:1px solid #ddd;padding:8px;text-align:left}",
        "th{background:#f5f7fa}",
        "tr:nth-child(even){background:#fbfbfb}",
        "</style>",
        "</head>",
        "<body>",
        "<h1>MLCheck Report</h1>",
    ]

    parts.append("<h2>Dataset Information</h2>")
    parts.append("<table>")
    parts.append("<tr><th>Property</th><th>Value</th></tr>")
    parts.append(f"<tr><td>Rows</td><td>{escape(str(report.get('rows')))}</td></tr>")
    parts.append(f"<tr><td>Features</td><td>{escape(str(report.get('features')))}</td></tr>")
    parts.append(f"<tr><td>Target</td><td>{escape(str(report.get('target')))}</td></tr>")
    parts.append(f"<tr><td>Issues Found</td><td>{escape(str(report.get('issue_count')))}</td></tr>")
    parts.append("</table>")

    if report.get('issue_count'):
        parts.append("<h2>Issues</h2>")
        parts.append("<table>")
        parts.append("<tr><th>Name</th><th>Severity</th><th>Details</th></tr>")

        for issue in report.get('issues', []):
            name = escape(str(issue.get('name')))
            sev = escape(str(issue.get('severity')))
            details = issue.get('details') or {}
            parts.append(f"<tr><td>{name}</td><td>{sev}</td><td>{escape(str(details))}</td></tr>")

        parts.append("</table>")
    else:
        parts.append("<p>No issues detected.</p>")

    parts.append("</body>")
    parts.append("</html>")

    return "\n".join(parts)

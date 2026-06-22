"""Markdown reporter for MLCheck reports."""


def render(report):
    """Render a report as a Markdown text string."""
    def _fmt_val(v):
        """Format a value for Markdown output."""
        try:
            import json as _json

            return _json.dumps(v)
        except Exception:
            return str(v)

    parts = ["# MLCheck Report", ""]

    # Dataset info as a small table
    parts.append("## Dataset Information")
    parts.append("")
    parts.append("| Property | Value |")
    parts.append("|---|---|")
    parts.append(f"| Rows | {report.get('rows')} |")
    parts.append(f"| Features | {report.get('features')} |")
    parts.append(f"| Target | {report.get('target')} |")
    parts.append(f"| Issues Found | {report.get('issue_count')} |")
    parts.append("")

    if report.get('issue_count'):
        parts.append("## Issues")
        parts.append("")
        parts.append("| Name | Severity | Details |")
        parts.append("|---|---:|---|")

        for issue in report.get('issues', []):
            name = issue.get('name')
            sev = issue.get('severity')
            details = issue.get('details') or {}
            parts.append(f"| {name} | {sev} | {_fmt_val(details)} |")

        parts.append("")
    else:
        parts.append("No issues detected.")

    return "\n".join(parts)

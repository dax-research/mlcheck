from mlcheck.scoring.health_score import calculate_health_score
from mlcheck.recommendations import generate_recommendations

class MLReport:
    def __init__(self, df, target=None, issues=None):
        """Create a new MLReport for the given DataFrame, target, and detected issues."""
        self.df = df
        self.target = target
        self._issues = issues or []

    def to_dict(self):
        """
        Return the report as a Python dictionary.
        """

        num_features = self.df.shape[1]

        if self.target is not None and self.target in self.df.columns:
            num_features -= 1

        return {
            "rows": self.df.shape[0],
            "features": num_features,
            "target": self.target,
            "issue_count": len(self.issues()),
            "issues": [
                {
                    "name": issue.name,
                    "severity": issue.severity,
                    "details": issue.details,
                }
                for issue in self.issues()
            ],
        }

    # 1. SUMMARY
    def summary(self):
        """
        Print a human-readable summary of the dataset and detected issues.
        """

        num_features = self.df.shape[1]

        if self.target is not None and self.target in self.df.columns:
            num_features -= 1

        print("=" * 60)
        print("                     MLCheck Report")
        print("=" * 60)

        # Dataset information
        print("\n📊 Dataset Information")
        print("-" * 60)
        print(f"Rows          : {self.df.shape[0]}")
        print(f"Features      : {num_features}")
        print(f"Target        : {self.target}")
        print(f"Issues Found  : {len(self.issues())}")

        # No issues
        if not self.issues():
            print("\n✅ No issues detected. Dataset looks healthy.")
            print("=" * 60)
            return

        # Issue overview
        print("\n🚨 Detected Issues")
        print("-" * 60)

        for issue in self.issues():
            print(f"[{issue.severity.upper():6}] {issue.name}")

        # Detailed information
        print("\n📋 Details")
        print("-" * 60)

        for issue in self.issues():
            print(f"\n▶ {issue.name} ({issue.severity.upper()})")

            if not issue.details:
                print("  No additional details available.")
                continue

            for key, value in issue.details.items():

                # If the value is a list of dictionaries
                if (
                    isinstance(value, list)
                    and value
                    and isinstance(value[0], dict)
                ):
                    for item in value:
                        text = ", ".join(
                            f"{k}={v}" for k, v in item.items()
                        )
                        print(f"  - {text}")

                # If the value is a list
                elif isinstance(value, list):
                    for item in value:
                        print(f"  - {item}")

                # Otherwise print normally
                else:
                    print(f"  {key}: {value}")

        print("\n" + "=" * 60)

    # 2. ISSUES
    def show_issues(self):
        """Print the detected issues in a compact list format."""
        if not self.issues():
            print("\nNo issues found. Dataset looks clean.")
            return

        print("\n=== Issues ===\n")

        for i, issue in enumerate(self.issues(), 1):
            print(f"[{i}] {issue.name}")
            print(f"    Severity: {issue.severity}")
            print(f"    Details: {issue.details}")

    # 3. RAW ACCESS
    def issues(self):
        """Return the list of detected issues for this report."""
        return self._issues

    def get_summary_text(self):
        """Return the report summary as plain text."""
        num_features = self.df.shape[1]

        if self.target is not None and self.target in self.df.columns:
            num_features -= 1

        lines = ["=" * 60, "                     MLCheck Report", "=" * 60, ""]
        lines.append("📊 Dataset Information")
        lines.append("-" * 60)
        lines.append(f"Rows          : {self.df.shape[0]}")
        lines.append(f"Features      : {num_features}")
        lines.append(f"Target        : {self.target}")
        lines.append(f"Issues Found  : {len(self.issues())}")
        lines.append("")

        if not self.issues():
            lines.append("✅ No issues detected. Dataset looks healthy.")
            lines.append("=" * 60)
            return "\n".join(lines)

        lines.append("🚨 Detected Issues")
        lines.append("-" * 60)

        for issue in self.issues():
            lines.append(f"[{issue.severity.upper():6}] {issue.name}")

        lines.append("")
        lines.append("📋 Details")
        lines.append("-" * 60)

        for issue in self.issues():
            lines.append("")
            lines.append(f"▶ {issue.name} ({issue.severity.upper()})")

            if not issue.details:
                lines.append("  No additional details available.")
                continue

            for key, value in issue.details.items():
                if (
                    isinstance(value, list)
                    and value
                    and isinstance(value[0], dict)
                ):
                    for item in value:
                        text = ", ".join(
                            f"{k}={v}" for k, v in item.items()
                        )
                        lines.append(f"  - {text}")
                elif isinstance(value, list):
                    for item in value:
                        lines.append(f"  - {item}")
                else:
                    lines.append(f"  {key}: {value}")

        lines.append("")
        lines.append("=" * 60)

        return "\n".join(lines)

    # 4. HEALTH SCORE
    def health_score(self):
        """
        Return the dataset health score.
        """
        return calculate_health_score(self.issues())

    # 5. REPORT EXPORTS
    def to_json(self):
        """
        Return the report as a JSON string.
        """
        from mlcheck.reporting import json as reporting_json

        return reporting_json.render(self.to_dict())

    def to_markdown(self):
        """
        Return the report rendered as Markdown.
        """
        from mlcheck.reporting import markdown as reporting_md

        return reporting_md.render(self.to_dict())

    def to_html(self):
        """
        Return the report rendered as HTML.
        """
        from mlcheck.reporting import html as reporting_html

        return reporting_html.render(self.to_dict())

    def to_file(self, path, format=None):
        """
        Write the report to `path`. If `format` is not provided, infer from file extension.

        Supported formats: 'json', 'markdown', 'html'. Returns the path written.
        """
        import os

        if format is None:
            ext = os.path.splitext(path)[1].lower()
            if ext in (".json",):
                format = "json"
            elif ext in (".md", ".markdown"):
                format = "markdown"
            elif ext in (".html", ".htm"):
                format = "html"
            else:
                format = "json"

        if format == "json":
            content = self.to_json()
        elif format == "markdown":
            content = self.to_markdown()
        elif format == "html":
            content = self.to_html()
        else:
            raise ValueError(f"Unsupported format: {format}")

        # Ensure parent dir exists
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return path

    def download_summary(self, path="mlcheck_summary.txt"):
        """
        Write the summary text to a file and return the written path.
        """
        import os

        content = self.get_summary_text()
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return path

    # 6. RECOMMENDATIONS
    def recommendations(self):
        """
        Return recommendations for detected issues.
        """
        return generate_recommendations(self.issues())

class MLReport:
    def __init__(self, df, target=None, issues=None):
        self.df = df
        self.target = target
        self._issues = issues or []

    # 1. SUMMARY
    def summary(self):
        num_features = self.df.shape[1]

        if self.target and self.target in self.df.columns:
            num_features -= 1

        print("\n=== MLCheck Report ===")
        print(f"Rows     : {self.df.shape[0]}")
        print(f"Features : {num_features}")
        print(f"Target   : {self.target}")

    # 2. ISSUES
    def show_issues(self):
        if not self._issues:
            print("\nNo issues found. Dataset looks clean.")
            return

        print("\n=== Issues ===\n")

        for i, issue in enumerate(self._issues, 1):
            print(f"[{i}] {issue.name}")
            print(f"    Severity: {issue.severity}")
            print(f"    Details: {issue.details}")

    # 3. RAW ACCESS
    def issues(self):
        return self._issues

    # 4. PLACEHOLDER
    def recommendations(self):
        print("\nNo recommendations implemented yet.")
class MLReport:
    def __init__(self, df, target=None, issues=None):
        self.df = df
        self.target = target
        self._issues = issues if issues is not None else []

    def summary(self):
        num_features = self.df.shape[1]
        if self.target and self.target in self.df.columns:
            num_features -= 1

        print("=== MLCheck Report ===")
        print(f"Rows    : {self.df.shape[0]}")
        print(f"Features: {num_features}")
        print(f"Target  : {self.target}")

    def show_issues(self):
        if not self.issues:
            print("No issues found.")
            return

        print("\n=== Issues ===\n")

        for i, issue in enumerate(self.issues, 1):
            print(f"[{i}] {issue.name}")
            print(f"    Severity: {issue.severity}")
            print(f"    Details: {issue.details}\n")
        

    def recommendations(self):
        print("No recommendations yet.")
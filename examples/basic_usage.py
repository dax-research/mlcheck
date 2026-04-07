import pandas as pd
from mlcheck import inspect

df = pd.DataFrame({
    "age": [20, 21, 22, 23, 24],
    "label": [0, 0, 0, 0, 1]
})

report = inspect(df, target="label")

report.summary()
report.to_dict()
print()
print(f"Health Score: {report.health_score()}")
report.show_issues()   # or report.issues(), depending on your API
for rec in report.recommendations():
    print(
        f"[{rec['severity'].upper()}] "
        f"{rec['issue']}: {rec['recommendation']}"
    )

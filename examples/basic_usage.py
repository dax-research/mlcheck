import pandas as pd
from mlcheck import inspect

df = pd.DataFrame({
    "age": [20, 21, None, 23],
    "salary": [50000, 52000, 51000, 1000000],
    "target": [0, 0, 0, 1],
})

report = inspect(df, target="target")

report.summary()

print("Health Score:", report.health_score())

print("\nRecommendations:")
for rec in report.recommendations():
    print("-", rec)

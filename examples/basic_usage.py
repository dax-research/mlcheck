import pandas as pd
from mlcheck.health.missing import check_missing

df = pd.DataFrame({
    "age": [10, None, 30, None],
    "salary": [1000, 2000, None, 4000],
    "name": ["A", "B", "C", "D"]
})

issue = check_missing(df)

print(issue)
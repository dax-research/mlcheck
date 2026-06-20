import pandas as pd
from mlcheck import inspect

df = pd.DataFrame({
    "age": [10, None, 30, None],
    "salary": [1000, 2000, None, 4000],
    "name": ["A", "B", "C", "D"]
})

report = inspect(df, target=None)

report.summary()
report.show_issues()
report.recommendations()
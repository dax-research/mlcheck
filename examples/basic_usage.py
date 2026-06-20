import pandas as pd
from mlcheck import inspect

df = pd.DataFrame({
    "age": [20, 21, 22, 23, 24],
    "label": [0, 0, 0, 0, 1]
})

report = inspect(df, target="label")

report.summary()
report.show_issues()   # or report.issues(), depending on your API
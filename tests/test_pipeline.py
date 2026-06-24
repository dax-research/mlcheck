import pandas as pd

from mlcheck import inspect


def test_pipeline_runs():
    df = pd.DataFrame({
        "a": [1, 2, None, 4],
        "b": [1, 2, None, 4],
    })

    report = inspect(df)

    assert report is not None
    assert hasattr(report, "summary")
    assert hasattr(report, "to_dict")

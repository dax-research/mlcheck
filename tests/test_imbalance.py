import pandas as pd
from mlcheck.health.imbalance import check_imbalance


def test_high_imbalance():
    df = pd.DataFrame({
        "feature": [1, 2, 3, 4, 5],
        "label": [0, 0, 0, 0, 1]  # 80% vs 20%
    })

    issue = check_imbalance(df, target="label")

    assert issue is not None
    assert issue.name == "class_imbalance"
    assert issue.severity == "high"


def test_medium_imbalance():
    df = pd.DataFrame({
        "feature": range(10),
        "label": [0] * 7 + [1] * 3  # 70% vs 30%
    })

    issue = check_imbalance(df, target="label")

    assert issue is not None
    assert issue.severity == "medium"


def test_balanced_dataset():
    df = pd.DataFrame({
        "feature": range(10),
        "label": [0] * 5 + [1] * 5  # 50% vs 50%
    })

    issue = check_imbalance(df, target="label")

    assert issue is None

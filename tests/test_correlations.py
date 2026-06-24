import pandas as pd
import numpy as np
from mlcheck.health.correlations import check_correlations

def test_high_correlation_detected():
    df = pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "y": [2, 4, 6, 8, 10],  # Perfect correlation (1.0)
        "z": [5, 3, 1, 4, 2],
    })

    issue = check_correlations(df)

    assert issue is not None
    assert issue.name == "high_correlation"
    assert issue.severity == "high"


def test_medium_correlation_detected():
    # Correlation ≈ 0.866 (between 0.80 and 0.90)
    df = pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 2, 4, 3],
    })

    issue = check_correlations(df)

    assert issue is not None
    assert issue.name == "high_correlation"
    assert issue.severity == "medium"


def test_no_high_correlation():
    np.random.seed(42)

    df = pd.DataFrame({
        "a": np.random.rand(100),
        "b": np.random.rand(100),
        "c": np.random.rand(100),
    })

    issue = check_correlations(df)

    assert issue is None


def test_target_column_is_ignored():
    df = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [2, 4, 6, 8, 10],
        "target": [0, 1, 0, 1, 0],
    })

    issue = check_correlations(df, target="target")

    assert issue is not None
    assert issue.name == "high_correlation"


def test_single_numeric_column():
    df = pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "city": ["A", "B", "C", "D", "E"],
    })

    issue = check_correlations(df)

    assert issue is None

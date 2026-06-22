"""Rules for mapping findings to recommendations."""

RULES = {
    "missing_values":
        "Fill missing values using an appropriate imputation strategy.",

    "duplicate_rows":
        "Remove duplicate rows before training.",

    "constant_columns":
        "Drop constant columns since they carry no information.",

    "class_imbalance":
        "Consider class weighting, oversampling, or undersampling.",

    "high_correlation":
        "Remove redundant features or apply dimensionality reduction.",

    "high_cardinality":
        "Consider target encoding, frequency encoding, or grouping rare categories.",

    "outliers":
        "Inspect extreme values and consider clipping or robust preprocessing.",

    "target_leakage":
        "Remove features that reveal the target variable.",

    "datatype_issues":
        "Convert columns to appropriate data types before training.",
}

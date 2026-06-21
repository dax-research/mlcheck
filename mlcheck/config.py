"""Default configuration for mlcheck."""

DEFAULT_CONFIG = {
    "health_checks": True,
    "recommendations": True,
}

# config.py

# Missing values
LOW_MISSING_THRESHOLD = 5  # percentage
MEDIUM_MISSING_THRESHOLD = 20

# Class imbalance
HIGH_IMBALANCE_THRESHOLD = 0.80
MEDIUM_IMBALANCE_THRESHOLD = 0.70

# Correlation
CORRELATION_THRESHOLD = 0.90

# Outliers
DEFAULT_IQR_MULTIPLIER = 1.5

# Cardinality
MEDIUM_CARDINALITY_THRESHOLD = 50
HIGH_CARDINALITY_THRESHOLD = 100
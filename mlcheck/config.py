"""Default configuration for mlcheck."""

DEFAULT_CONFIG = {
    "health_checks": True,
    "recommendations": True,
}

# config.py

# Missing values
HIGH_MISSING_THRESHOLD = 50.0  # percent
MEDIUM_MISSING_THRESHOLD = 20.0

# Class imbalance
HIGH_IMBALANCE_THRESHOLD = 0.80
MEDIUM_IMBALANCE_THRESHOLD = 0.70

# Correlation
CORRELATION_THRESHOLD = 0.90

# Outliers
DEFAULT_IQR_MULTIPLIER = 1.5
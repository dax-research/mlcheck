"""Health checks subpackage."""

from .missing import check_missing
from .duplicates import check_duplicates
from .constants import check_constants
from .imbalance import check_imbalance
from .datatypes import check_datatypes
from .leakage import check_leakage
from .cardinality import check_cardinality
from .outliers import check_outliers
from .correlations import check_correlations

HEALTH_CHECKS = [
    check_missing,
    check_duplicates,
    check_constants,
    check_imbalance,
    check_datatypes,
    check_leakage,
    check_cardinality,
    check_outliers,
    check_correlations,
]

__all__ = [
    "check_missing",
    "check_duplicates",
    "check_constants",
    "check_imbalance",
    "check_datatypes",
    "check_leakage",
    "check_cardinality",
    "check_outliers",
    "check_correlations",
    "HEALTH_CHECKS",
]

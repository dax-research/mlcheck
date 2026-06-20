"""Custom exceptions for mlcheck."""

class MLCheckError(Exception):
    """Base exception for mlcheck."""
    pass


class ConfigurationError(MLCheckError):
    """Raised when configuration is invalid."""


class HealthCheckError(MLCheckError):
    """Raised when a health check fails unexpectedly."""
"""JSON reporter with safe serialization for numpy types and objects."""

import json


def _default(o):
    """Return a JSON-serializable value for unsupported objects."""
    try:
        return o.item()
    except Exception:
        try:
            import numpy as _np

            if isinstance(o, _np.ndarray):
                return o.tolist()
        except Exception:
            pass
    return str(o)


def render(report):
    """Render a report as a pretty-printed JSON string."""
    return json.dumps(report, default=_default, indent=2)

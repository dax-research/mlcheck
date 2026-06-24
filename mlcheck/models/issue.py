from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Issue:
    """
    Standard representation of a dataset problem detected by MLCheck.
    """

    name: str
    severity: str
    details: Dict[str, Any] = field(default_factory=dict)

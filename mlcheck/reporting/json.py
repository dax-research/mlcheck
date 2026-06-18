"""JSON reporter."""

import json


def render(report):
    return json.dumps(report)

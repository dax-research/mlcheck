"""Recommendation engine entrypoints."""

from .rules import RULES


def generate_recommendations(issues):
    """
    Generate recommendations from detected issues.
    """

    recommendations = []

    for issue in issues:
        recommendation = RULES.get(issue.name)

        if recommendation:
            recommendations.append({
                "issue": issue.name,
                "severity": issue.severity,
                "recommendation": recommendation,
            })

    return recommendations

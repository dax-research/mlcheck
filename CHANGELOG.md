# Changelog

All notable changes to this project are recorded in this file. This project follows a simple unreleased-first changelog format.

## [Unreleased]

### Added
- Core dataset health checks for missing values, duplicates, high cardinality, outliers, class imbalance, correlations, and target leakage.
- `MLReport` summary and issue reporting.
- Health score computation via `MLReport.health_score()`.
- Recommendations engine that maps detected issues to remediation guidance.
- Exporters for `to_json()`, `to_markdown()`, and `to_html()`.
- `MLReport.to_file()` helper to persist reports to disk.
- `MLReport.download_summary()` helper to save a plain-text summary.
- Improved Markdown and HTML report styling.
- Added developer documentation and contribution workflow.

### Changed
- Added `pandas` as a runtime dependency.
- Added `requirements.txt` and expanded `requirements-dev.txt` with testing and formatting tools.
- Updated `README.md` with usage, installation, and API examples.

### Fixed
- Fixed report export path inference and improved serialization of numpy-compatible values.

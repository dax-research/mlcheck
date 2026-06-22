# Contributing to mlcheck

Thank you for contributing to `mlcheck`! We welcome improvements, bug fixes, and feature requests.

## Getting Started

1. Fork the repository and create a branch from `main`.
2. Install the development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

3. Run the existing test suite before making changes:

```bash
python -m pytest
```

## Coding Guidelines

- Keep changes small and focused.
- Follow the existing code style and formatting.
- Add tests for new behavior and fix regressions when possible.
- Write or update documentation when you add features or change public APIs.

## Committing Changes

- Use clear commit messages that describe the intent of the change.
- Prefer one logical change per commit.
- If you use GitHub, open a pull request with a summary and testing notes.

## Pull Request Checklist

- [ ] The code follows the project style.
- [ ] New or changed behavior is covered by tests.
- [ ] Documentation and examples are updated if needed.
- [ ] The PR description explains the reason for the change.

## Reporting Issues

If you find a bug or want to request a feature, please open an issue with:

- A clear title and description.
- Reproduction steps or sample code.
- Expected versus actual behavior.
- Any relevant error messages or tracebacks.

## Notes for Maintainers

- Review contributions for correctness and consistency.
- Encourage test coverage for functional changes.
- Keep the changelog updated with notable changes.

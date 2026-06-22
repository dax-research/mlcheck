# Installation

Install `mlcheck` and its runtime dependencies.

## Option 1: Install from source

Use the runtime and development dependency files in this repository:

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

Then install the package in editable mode for development:

```bash
python -m pip install -e .
```

## Option 2: Runtime-only install

If you only want to use `mlcheck` without the development tools:

```bash
python -m pip install -r requirements.txt
```

## Requirements

- Python 3.8+
- `pandas`

`requirements.txt` currently includes the runtime requirements for the package.
`requirements-dev.txt` includes test and formatting tools such as `pytest`, `black`, `flake8`, and `mypy`.

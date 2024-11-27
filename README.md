### Demonstrating `__all__` with Tools

This repository showcases how defining `__all__` impacts tools like `mypy` and `flake8`.

#### Example Workflow

```bash
# Create and activate a virtual environment
python -m virtualenv .venv
. .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows

# Install tools
pip install mypy flake8

# Run mypy to check for missing or incorrectly defined exports
mypy --strict .
# Example output:
# main.py:3: error: Module "dummy_package" does not explicitly export attribute "bar"  [attr-defined]

# Run flake8 to catch unused imports related to __all__
flake8 dummy_package
# Example output:
# dummy_package\__init__.py:2:1: F401 '._package_impl.bar' imported but unused
```

#### Key Points
- `mypy` checks for attributes not explicitly defined in `__all__`.
- `flake8` detects unused imports, ensuring alignment with `__all__`. 

This demonstrates how `__all__` helps enforce clarity and maintainability in your code.

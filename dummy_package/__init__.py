from ._package_impl import foo
from ._package_impl import bar
# $ flake8.exe .\dummy_package\__init__.py
# .\dummy_package\__init__.py:2:1: F401 '._package_impl.bar' imported but unused

__all__ = ["foo"]

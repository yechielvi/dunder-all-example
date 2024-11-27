from dummy_package import foo  
# mypy will not complain about this import
from dummy_package import bar  
# $ mypy --strict main.py
# main.py:2: error: Module "dummy_package" does not explicitly export attribute "bar"  [attr-defined]

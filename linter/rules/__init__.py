# linter/rules/__init__.py

from .print_rule import PrintRule
from .short_var_rule import ShortVarRule

__all__ = [
    "PrintRule",
    "ShortVarRule",
]

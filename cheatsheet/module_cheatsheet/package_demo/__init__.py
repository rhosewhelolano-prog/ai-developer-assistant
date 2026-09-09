"""Package demo package for Python imports.

A package is a folder containing __init__.py and other modules.
This lets us organize related code into one namespace.
"""

from .utils import format_label
from .operations import double_value, calculate_total

__all__ = ["format_label", "double_value", "calculate_total"]

"""Module cheat sheet package.

This package demonstrates how Python modules work, including:
- importing modules
- using the standard library
- module search paths
- packages and subpackages
- running a module as a script
"""

from .basic_module import add, greet
from .standard_lib_demo import get_standard_library_examples

__all__ = ["add", "greet", "get_standard_library_examples"]

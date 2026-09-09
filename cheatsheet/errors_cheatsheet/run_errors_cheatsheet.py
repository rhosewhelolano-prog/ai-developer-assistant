"""Main runner for the errors and exceptions cheat sheet.

This file runs the examples from the errors_cheatsheet package so you can see
all the concepts in one place.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from errors_cheatsheet.exceptions_examples import (
    syntax_error_example,
    exception_examples,
    safe_divide,
    raise_value_error,
    exception_chaining_demo,
    custom_exception_demo,
    cleanup_demo,
    multiple_exception_demo,
    add_exception_note_demo,
)

# -------------------------------------------------------------------
# 8.1 Syntax Errors
# -------------------------------------------------------------------
# Syntax errors happen before the code can run.
# They often mean the grammar of the file is wrong, such as a missing colon.
syntax_error_example()

# -------------------------------------------------------------------
# 8.2 Exceptions
# -------------------------------------------------------------------
# Python raises exceptions at runtime when something unexpected happens.
# This is similar to throwing an error in JavaScript.
exception_examples()

# -------------------------------------------------------------------
# 8.3 Handling Exceptions
# -------------------------------------------------------------------
# try/except catches errors so the program can continue.
print("Result of safe_divide(10, 2):", safe_divide(10, 2))
print("Result of safe_divide(10, 0):", safe_divide(10, 0))
print()

# -------------------------------------------------------------------
# 8.4 Raising Exceptions
# -------------------------------------------------------------------
# We can deliberately raise errors to enforce validation rules.
try:
    print("Result of raise_value_error(5):", raise_value_error(5))
    print("Result of raise_value_error(-2):", raise_value_error(-2))
except ValueError as exc:
    print(f"Caught ValueError: {exc}")
print()

# -------------------------------------------------------------------
# 8.5 Exception Chaining
# -------------------------------------------------------------------
# When one error causes another, Python preserves the original cause.
exception_chaining_demo()

# -------------------------------------------------------------------
# 8.6 User-defined Exceptions
# -------------------------------------------------------------------
# Custom classes allow domain-specific message handling.
custom_exception_demo()

# -------------------------------------------------------------------
# 8.7 and 8.8 Cleaning up resources
# -------------------------------------------------------------------
# finally and with are used for cleanup no matter what happens.
cleanup_demo()

# -------------------------------------------------------------------
# 8.9 Multiple Unrelated Exceptions
# -------------------------------------------------------------------
# ExceptionGroup allows multiple exceptions to be handled together.
multiple_exception_demo()

# -------------------------------------------------------------------
# 8.10 Enriching Exceptions with Notes
# -------------------------------------------------------------------
# add_note() adds extra debugging details to an exception.
add_exception_note_demo()

print("Errors and exceptions cheat sheet complete.")

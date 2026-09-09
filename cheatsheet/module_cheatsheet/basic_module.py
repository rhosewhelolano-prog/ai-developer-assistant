"""Basic module examples for learning Python modules.

A module is just a Python file that can be imported into another file.
This module shows the basics of importing functions from one file into another.
"""

# The import below is used later in the package demonstration.
import sys


def greet(name):
    """Return a simple greeting.

    This is similar to a function in JavaScript, except the syntax is simpler.
    """
    return f"Hello, {name}!"


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def show_sys_path():
    """Display the module search path.

    Python checks these locations when you import a module.
    This is why modules must be in the current project or a recognized path.
    """
    print("=== Module Search Path ===")
    for path in sys.path:
        print(path)


if __name__ == "__main__":
    # This block only runs when the file is executed directly:
    # python basic_module.py
    print("This file is running as a script.")
    print(greet("Python learner"))
    print(add(5, 7))

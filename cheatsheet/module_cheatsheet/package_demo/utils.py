"""Utility helpers for the package demo."""


def format_label(name, value):
    """Format a simple label like a JS object summary.

    Example output: 'Name: Ada | Value: 42'
    """
    return f"Name: {name} | Value: {value}"


def show_package_example():
    """Demonstrate package usage with a helper function."""
    print("=== Packages ===")
    print(format_label("score", 99))

"""Operations used in the package example."""


def double_value(value):
    """Double a number and return the result."""
    return value * 2


def calculate_total(*numbers):
    """Add many numbers together."""
    total = 0
    for number in numbers:
        total += number
    return total

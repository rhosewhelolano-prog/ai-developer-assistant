"""Python errors and exceptions cheat sheet.

This file shows common Python exception patterns and explains how they compare to
JavaScript error handling. It is intended as a review/learning file.
"""

# -------------------------------------------------------------------
# 8.1 Syntax Errors
# -------------------------------------------------------------------
# A syntax error happens when the code is not valid Python grammar.
# Example: missing a colon or using incorrect indentation.
# These errors are usually caught before the script runs.

def syntax_error_example():
    print("=== Syntax Errors ===")
    print("Example: forgetting a colon after an if statement causes a SyntaxError.")
    print("Example code: if True\n    print('oops')")
    print("This would fail before execution begins.")
    print()


# -------------------------------------------------------------------
# 8.2 Exceptions
# -------------------------------------------------------------------
# Exceptions are runtime errors that happen while the program is running.
# Examples include ZeroDivisionError, ValueError, TypeError, FileNotFoundError.

def exception_examples():
    print("=== Exceptions ===")
    examples = [
        ("ZeroDivisionError", lambda: 10 / 0),
        ("ValueError", lambda: int("abc")),
        ("TypeError", lambda: "a" + 5),
    ]

    for name, action in examples:
        try:
            action()
        except Exception as exc:
            print(f"{name}: {type(exc).__name__} -> {exc}")
    print()


# -------------------------------------------------------------------
# 8.3 Handling Exceptions
# -------------------------------------------------------------------
# try/except lets us catch errors and continue executing the program.
# In JavaScript this is similar to try/catch.

def safe_divide(a, b):
    """Divide a by b and safely handle invalid input."""
    print("=== Handling Exceptions ===")
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    except TypeError:
        print("Inputs must be numbers.")
        return None
    finally:
        print("This finally block always runs.")


# -------------------------------------------------------------------
# 8.4 Raising Exceptions
# -------------------------------------------------------------------
# raise allows us to create our own runtime errors when a condition is invalid.
# This is often useful for input validation.

def raise_value_error(value):
    """Raise a ValueError when the value is invalid."""
    print("=== Raising Exceptions ===")
    if value < 0:
        raise ValueError("Value must be non-negative.")
    return value


# -------------------------------------------------------------------
# 8.5 Exception Chaining
# -------------------------------------------------------------------
# When one exception is raised while handling another, Python can chain them.
# This helps preserve the original cause in the traceback.

def exception_chaining_demo():
    print("=== Exception Chaining ===")
    try:
        try:
            1 / 0
        except ZeroDivisionError as exc:
            raise ValueError("Bad value during calculation") from exc
    except Exception as exc:
        print(f"Caught: {type(exc).__name__} -> {exc}")
    print()


# -------------------------------------------------------------------
# 8.6 User-defined Exceptions
# -------------------------------------------------------------------
# Custom exceptions make domain-specific error handling easier and clearer.

class PaymentError(Exception):
    """Raised when a payment operation fails."""


class InsufficientFundsError(PaymentError):
    """Raised when the account balance is too low."""


def custom_exception_demo():
    print("=== User-defined Exceptions ===")
    balance = 20
    amount = 100

    try:
        if amount > balance:
            raise InsufficientFundsError("Not enough funds for this payment.")
    except PaymentError as exc:
        print(f"Caught custom error: {exc}")
    print()


# -------------------------------------------------------------------
# 8.7 and 8.8 Defining Clean-up Actions / Predefined Clean-up Actions
# -------------------------------------------------------------------
# finally blocks run whether or not an exception occurs.
# The with statement also provides cleanup for resources like files.

def cleanup_demo():
    print("=== Defining Clean-up Actions ===")
    try:
        print("Opening a file-like resource...")
        raise RuntimeError("Simulated failure")
    except RuntimeError:
        print("Handled the runtime error.")
    finally:
        print("Cleanup runs in finally, even after the exception.")

    print("\n=== Predefined Clean-up Actions ===")
    try:
        with open("sample_temp.txt", "w", encoding="utf-8") as file:
            file.write("hello from Python")
        with open("sample_temp.txt", "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    finally:
        # This demonstrates cleanup and resource management as a best practice.
        print("The with statement automatically closes the file after use.")

    print()


# -------------------------------------------------------------------
# 8.9 Raising and Handling Multiple Unrelated Exceptions
# -------------------------------------------------------------------
# Python 3.11+ supports raising multiple unrelated exceptions with ExceptionGroup.
# This is useful when several errors happen at once.

def multiple_exception_demo():
    print("=== Multiple Unrelated Exceptions ===")
    try:
        raise ExceptionGroup(
            "Multiple failures",
            [
                ValueError("bad value"),
                TypeError("wrong type"),
            ],
        )
    except* ValueError as exc:
        print("Handled ValueError subgroup:", exc)
    except* TypeError as exc:
        print("Handled TypeError subgroup:", exc)
    print()


# -------------------------------------------------------------------
# 8.10 Enriching Exceptions with Notes
# -------------------------------------------------------------------
# Python allows attaching notes to exceptions with the add_note() method.
# This is useful for extra debugging context.

def add_exception_note_demo():
    print("=== Enriching Exceptions with Notes ===")
    try:
        raise RuntimeError("Something went wrong.")
    except RuntimeError as exc:
        exc.add_note("This happened while processing user input.")
        exc.add_note("Review the request payload before retrying.")
        print(f"Caught: {exc}")
        for note in exc.__notes__:
            print("Note:", note)
    print()


if __name__ == "__main__":
    syntax_error_example()
    exception_examples()
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(raise_value_error(5))
    try:
        print(raise_value_error(-2))
    except ValueError as exc:
        print(f"Caught raised error: {exc}")
    exception_chaining_demo()
    custom_exception_demo()
    cleanup_demo()
    multiple_exception_demo()
    add_exception_note_demo()

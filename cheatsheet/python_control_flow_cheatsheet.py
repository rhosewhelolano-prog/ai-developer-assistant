"""Python Control Flow Cheat Sheet for a JavaScript Developer

This file focuses on Python's control flow and function behavior.
It is designed to help someone coming from JavaScript understand the
core concepts from the Python tutorial section on control flow.
"""

# -------------------------------------------------------------------
# 1) if statements
# -------------------------------------------------------------------
# Python uses indentation instead of braces to define blocks.
# The condition is written without parentheses, which is common in Python.
print("=== if Statements ===")

age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

score = 85
if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs improvement")
print()

# -------------------------------------------------------------------
# 2) for statements
# -------------------------------------------------------------------
# A for loop in Python iterates over items in a collection.
# This is similar to for...of in JavaScript, but the syntax is more direct.
print("=== for Statements ===")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")
print()

# -------------------------------------------------------------------
# 3) range() function
# -------------------------------------------------------------------
# range() creates a sequence of numbers.
# range(5) means 0 through 4.
# range(start, stop, step) is very handy for loops.
print("=== range() Function ===")

for i in range(5):
    print(i)

print("range(2, 8, 2):")
for i in range(2, 8, 2):
    print(i)
print()

# -------------------------------------------------------------------
# 4) break and continue
# -------------------------------------------------------------------
# continue skips the rest of the current loop iteration.
# break exits the loop immediately.
# This is similar to JavaScript's continue and break statements.
print("=== break and continue ===")

for number in range(1, 10):
    if number == 3:
        continue
    if number == 7:
        break
    print(number)
print()

# -------------------------------------------------------------------
# 5) else clauses on loops
# -------------------------------------------------------------------
# In Python, a loop can have an else block that runs when the loop ends
# without being stopped by break.
print("=== else Clauses on Loops ===")

for n in range(2, 10):
    if n % 2 == 0:
        print(f"Found an even number: {n}")
        break
else:
    print("No even numbers found.")
print()

# -------------------------------------------------------------------
# 6) pass statements
# -------------------------------------------------------------------
# pass is a placeholder used when Python requires a block but you want
# to do nothing. It is similar to an empty statement in other languages.
print("=== pass Statement ===")

for item in [1, 2, 3]:
    if item == 2:
        pass  # placeholder; does nothing
    print(item)
print()

# -------------------------------------------------------------------
# 7) match statements (Python 3.10+)
# -------------------------------------------------------------------
# match is Python's structural pattern matching feature.
# It is similar to switch/case in JavaScript, but more expressive.
print("=== match Statements ===")

day = "Monday"
match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("Almost the weekend.")
    case _:
        print("Some other day.")
print()

# -------------------------------------------------------------------
# 8) Defining functions
# -------------------------------------------------------------------
# Python functions are defined with the def keyword.
# They can return values and take parameters just like JavaScript functions.
print("=== Defining Functions ===")


def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}!"

print(greet("Jordan"))
print()

# -------------------------------------------------------------------
# 9) Default argument values
# -------------------------------------------------------------------
# A parameter can have a default value so the caller does not always need
# to pass it. This is similar to a default parameter in JavaScript.
print("=== Default Argument Values ===")


def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(3, 3))
print()

# -------------------------------------------------------------------
# 10) Keyword arguments
# -------------------------------------------------------------------
# Keyword arguments let you pass arguments by name instead of position.
# This makes functions easier to read and less error-prone.
print("=== Keyword Arguments ===")


def introduce(name, age, city):
    return f"{name} is {age} years old and lives in {city}."

print(introduce(name="Sam", age=25, city="Boston"))
print(introduce(city="Austin", name="Priya", age=30))
print()

# -------------------------------------------------------------------
# 11) Special parameters
# -------------------------------------------------------------------
# Python supports a few special parameter rules:
# - positional-only arguments before /
# - keyword-only arguments after *
# This is a more advanced concept that helps control function APIs.
print("=== Special Parameters ===")


def display_info(a, b, /, c, *, d):
    # a and b are positional-only
    # c can be positional or keyword
    # d must be keyword-only
    return (a, b, c, d)

print(display_info(1, 2, 3, d=4))
print()

# -------------------------------------------------------------------
# 12) Arbitrary argument lists
# -------------------------------------------------------------------
# *numbers collects any number of positional arguments into a tuple.
# This is useful when the number of items is not known ahead of time.
print("=== Arbitrary Argument Lists ===")


def sum_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_all(1, 2, 3, 4, 5))
print()

# -------------------------------------------------------------------
# 13) Unpacking argument lists
# -------------------------------------------------------------------
# The * operator can unpack a list into separate arguments.
# This is similar to spreading values into a function call in JavaScript.
print("=== Unpacking Argument Lists ===")

values = [10, 20, 30]
print(sum(values))
print()

# -------------------------------------------------------------------
# 14) Lambda expressions
# -------------------------------------------------------------------
# Lambda functions are small anonymous functions.
# They are often used for short operations, like map/filter callbacks.
print("=== Lambda Expressions ===")

square = lambda x: x * x
print(square(6))

numbers = [1, 2, 3, 4]
print(list(map(lambda n: n * 2, numbers)))
print()

# -------------------------------------------------------------------
# 15) Documentation strings
# -------------------------------------------------------------------
# A docstring is a triple-quoted string placed right under a function or class.
# It documents the purpose and behavior of the code.
print("=== Documentation Strings ===")


def calculate_total(price, tax):
    """Return total with tax included.

    Args:
        price: item price before tax
        tax: tax rate as a decimal
    """
    return price + (price * tax)

print(calculate_total(100, 0.10))
print()

# -------------------------------------------------------------------
# 16) Function annotations
# -------------------------------------------------------------------
# Function annotations add type information in a readable way.
# They are optional, but they help with documentation and tooling.
print("=== Function Annotations ===")


def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(4, 5))
print()

# -------------------------------------------------------------------
# 17) Coding style note
# -------------------------------------------------------------------
# Python has a strong style convention called PEP 8.
# These rules help code stay readable and consistent across projects.
print("=== Coding Style ===")
print("- Use 4 spaces for indentation.")
print("- Keep functions small and readable.")
print("- Use descriptive names.")
print("- Add docstrings to explain what functions do.")
print()

# -------------------------------------------------------------------
# 18) Quick JavaScript-to-Python comparison
# -------------------------------------------------------------------
# This section helps you map JavaScript patterns to Python patterns.
# It is especially useful when you are learning Python from a JS background.
print("=== JS to Python Comparison ===")
print("JavaScript: if (x > 0) { ... }")
print("Python:     if x > 0:\n             ...")
print("JavaScript: for (let i = 0; i < 5; i++) { ... }")
print("Python:     for i in range(5): ...")
print("JavaScript: function greet(name) { ... }")
print("Python:     def greet(name): ...")
print()

print("Control flow cheat sheet complete.")

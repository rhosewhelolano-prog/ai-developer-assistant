"""Python Cheat Sheet for a JavaScript Developer

This file is meant to help someone coming from JavaScript understand the
basic syntax and patterns in Python.

Key differences to remember:
- Python uses indentation instead of curly braces {}.
- Variables are assigned with =, not const/let/var.
- There is no semicolon required at the end of each line.
- Python is dynamically typed, but values still have types.
- Lists, dictionaries, loops, and functions are all very readable in Python.
"""

# -----------------------------
# 1) Variables and simple values
# -----------------------------

# Python variable assignment is simple and flexible.
name = "Ada"
age = 31
price = 19.99
is_student = False
nothing = None

print("=== Variables ===")
print(name)
print(age)
print(price)
print(is_student)
print(nothing)
print()

# -----------------------------
# 2) Numbers and arithmetic
# -----------------------------

print("=== Numbers and Arithmetic ===")
num1 = 10
num2 = 3

print(num1 + num2)   # addition
print(num1 - num2)   # subtraction
print(num1 * num2)   # multiplication
print(num1 / num2)   # division -> float
print(num1 // num2)  # floor division
print(num1 % num2)   # modulo
print(num1 ** num2)  # exponent
print()

# -----------------------------
# 3) Strings and text
# -----------------------------

print("=== Strings ===")
message = "Hello, Python!"
print(message)
print(message.upper())
print(message.lower())
print(message.replace("Python", "JavaScript"))
print(len(message))
print(message[0])  # first character
print(message[7:13])  # slice from index 7 to 12
print()

# -----------------------------
# 4) Lists
# -----------------------------

print("=== Lists ===")
# A list is like a JavaScript array.
items = ["apple", "banana", "cherry"]
print(items)
print(items[0])
print(items[-1])
items.append("date")
print(items)
items.pop()
print(items)
print(len(items))
print()

# -----------------------------
# 5) Tuples
# -----------------------------

print("=== Tuples ===")
# Tuples are immutable (cannot be changed after creation).
point = (10, 20)
print(point)
print(point[0])
print()

# -----------------------------
# 6) Dictionaries
# -----------------------------

print("=== Dictionaries ===")
# A dictionary is like a JavaScript object.
student = {
    "name": "Sam",
    "age": 22,
    "course": "Python"
}
print(student)
print(student["name"])
student["age"] = 23
print(student)
print(student.get("course"))
print()

# -----------------------------
# 7) Booleans and comparisons
# -----------------------------

print("=== Booleans and Comparisons ===")
print(5 > 3)
print(5 == 3)
print(5 != 3)
print(True and False)
print(True or False)
print(not True)
print()

# -----------------------------
# 8) Conditionals
# -----------------------------

print("=== Conditionals ===")
score = 85

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs improvement")
print()

# -----------------------------
# 9) Loops
# -----------------------------

print("=== For Loop ===")
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

print("=== While Loop ===")
count = 0
while count < 3:
    print("Count is", count)
    count += 1
print()

# -----------------------------
# 10) Functions
# -----------------------------

print("=== Functions ===")

def greet(name):
    return f"Hello, {name}!"

print(greet("Jordan"))


def add(a, b=0):
    return a + b

print(add(5))
print(add(5, 10))
print()

# -----------------------------
# 11) List comprehensions
# -----------------------------

print("=== List Comprehension ===")
squares = [x * x for x in range(1, 6)]
print(squares)
print()

# -----------------------------
# 12) Dictionaries and loops together
# -----------------------------

print("=== Looping Through a Dictionary ===")
for key, value in student.items():
    print(key, "->", value)
print()

# -----------------------------
# 13) Exception handling
# -----------------------------

print("=== Try / Except ===")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("This runs no matter what.")
print()

# -----------------------------
# 14) Classes (very basic)
# -----------------------------

print("=== Classes ===")

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

    def dogName(self):
        return f"My dog's name is {self.name}."

my_dog = Dog("Buddy")
print(my_dog.bark())
print(my_dog.dogName())
print()

# -----------------------------
# 15) Python notes for JavaScript developers
# -----------------------------

print("=== Python vs JavaScript ===")
print("- Python uses indentation instead of curly braces.")
print("- Lists use [] and dictionaries use {}.")
print("- print() is the equivalent of console.log().")
print("- Python has no 'let'/'const' keywords; variables are just assigned.")
print("- In Python, whitespace matters a lot.")
print("- Python does not require semicolons at the end of lines.")
print("- Indexing starts at 0, just like JavaScript.")
print()

# The script prints all of the above when run directly.
print("Python cheat sheet complete.")

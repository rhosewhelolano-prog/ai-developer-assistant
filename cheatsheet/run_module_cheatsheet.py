"""Main runner for the Python modules cheat sheet.

This file imports all of the examples from the module_cheatsheet package and
runs them in one place so you can see the output from a single command.
"""

# Import from the local package we created.
from module_cheatsheet.basic_module import add, greet, show_sys_path
from module_cheatsheet.standard_lib_demo import get_standard_library_examples
from module_cheatsheet.package_demo import format_label, double_value, calculate_total

# -------------------------------------------------------------------
# 6) Modules
# -------------------------------------------------------------------
# A module is a Python file that contains functions, classes, or variables.
# You can import it into another file to reuse code.
print("=== Modules ===")
print(greet("Ada"))
print(add(10, 5))
print()

# -------------------------------------------------------------------
# 6.1) More on Modules
# -------------------------------------------------------------------
# The import system allows Python to share code across files.
# This makes large projects easier to organize.
print("=== More on Modules ===")
print("Imported greet() and add() from basic_module.py")
print()

# -------------------------------------------------------------------
# 6.1.1) Executing modules as scripts
# -------------------------------------------------------------------
# If you run a file directly, the __name__ == '__main__' block executes.
# That is useful for testing and demo code in a single file.
print("=== Executing Modules as Scripts ===")
print("When you run a module directly, Python executes its main block.")
print("Example: python basic_module.py")
print()

# -------------------------------------------------------------------
# 6.1.2) Module Search Path
# -------------------------------------------------------------------
# Python checks paths in sys.path to find modules.
# This is why local project folders and installed libraries can be imported.
show_sys_path()
print()

# -------------------------------------------------------------------
# 6.1.3) Compiled Python files
# -------------------------------------------------------------------
# Python may create .pyc files to speed up imports after code is compiled.
# These are cached bytecode files and usually do not need manual attention.
print("=== Compiled Python Files ===")
print("Python can create .pyc cache files to speed up future imports.")
print()

# -------------------------------------------------------------------
# 6.2) Standard Modules
# -------------------------------------------------------------------
# Python includes built-in modules like math, random, and datetime.
# These are available without needing package installation.
get_standard_library_examples()
print()

# -------------------------------------------------------------------
# 6.3) The dir() function
# -------------------------------------------------------------------
# dir() prints all names inside an object or module.
# This helps you explore what is available for import and use.
print("=== dir() Function ===")
print(dir())
print()

# -------------------------------------------------------------------
# 6.4) Packages
# -------------------------------------------------------------------
# A package is a directory that contains modules and an __init__.py file.
# Packages help organize larger Python projects into namespaces.
print("=== Packages ===")
print(format_label("level", 7))
print(double_value(10))
print(calculate_total(1, 2, 3, 4))
print()

# -------------------------------------------------------------------
# 6.4.1) Importing * from a package
# -------------------------------------------------------------------
# Importing * brings in all names that are listed in __all__.
# This is convenient but less explicit than importing specific items.
print("=== Importing * From a Package ===")
from module_cheatsheet import *
print(greet("Package user"))
print(add(2, 3))
print()

# -------------------------------------------------------------------
# 6.4.2) Intra-package references
# -------------------------------------------------------------------
# If modules inside a package need to reference one another, they can use
# relative imports such as from .utils import format_label.
print("=== Intra-package References ===")
from module_cheatsheet.package_demo.utils import format_label
print(format_label("team", "Python"))
print()

print("Module cheat sheet complete.")

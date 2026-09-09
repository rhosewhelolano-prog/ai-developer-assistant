"""Examples of using Python's standard library modules.

Standard modules are built into Python, so they are available without installing
anything extra. This is a big advantage over JavaScript, where many features
require package installs.
"""

import math
import random
import datetime


def get_standard_library_examples():
    """Show common modules and what they are used for."""
    print("=== Standard Modules ===")
    print("math.sqrt(25) ->", math.sqrt(25))
    print("random.randint(1, 10) ->", random.randint(1, 10))
    print("datetime.datetime.now() ->", datetime.datetime.now())

    print("\n=== dir() Function ===")
    # dir() shows the names available in an object or module.
    print(dir(math)[:10])
    print(dir(datetime)[:10])


if __name__ == "__main__":
    # This is how a module can also be run directly as a script.
    get_standard_library_examples()

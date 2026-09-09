"""Master Python cheat sheet runner.

This file intentionally does not change the current scripts or their run process.
It simply provides one additional way to run all of the existing cheat sheet files
from a single entry point.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CHEATSHEET_DIR = Path(__file__).resolve().parent

for path in (PROJECT_ROOT, CHEATSHEET_DIR):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

print("\n=== MASTER PYTHON CHEATSHEET ===")
print("Running all review files from a single entry point.\n")

# Import the existing review scripts.
# These scripts are intentionally left untouched so your current workflow still works.
import python_cheatsheet
import python_control_flow_cheatsheet
import run_module_cheatsheet
import errors_cheatsheet.run_errors_cheatsheet

print("\n=== ALL CHEAT SHEETS COMPLETED ===")

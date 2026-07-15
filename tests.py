"""
Simple tests for calculator.py

Run with:
    python3 tests.py

If nothing prints except "All tests passed!", everything works.
An AssertionError means one of the checks failed.
"""

from calculator import (
    add, subtract, multiply, divide,
    power, square_root, percentage,
    memory_add, memory_subtract, memory_recall, memory_clear,
)

# ---- Basic operations ----
assert add(2, 3) == 5
assert subtract(10, 4) == 6
assert multiply(3, 4) == 12
assert divide(10, 2) == 5

# Dividing by zero should raise an error, not crash silently
try:
    divide(5, 0)
    raise AssertionError("divide(5, 0) should have raised a ValueError")
except ValueError:
    pass  # this is expected

# ---- Scientific operations ----
assert power(2, 3) == 8
assert square_root(16) == 4
assert percentage(50, 20) == 10

# Square root of a negative number should raise an error
try:
    square_root(-1)
    raise AssertionError("square_root(-1) should have raised a ValueError")
except ValueError:
    pass  # this is expected

# ---- Memory functions ----
memory_clear()
memory_add(5)
assert memory_recall() == 5
memory_subtract(2)
assert memory_recall() == 3
memory_clear()
assert memory_recall() == 0

print("All tests passed!")
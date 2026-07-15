# Advanced Calculator

A command-line calculator built in Python. Supports basic arithmetic,
scientific operations, a memory function, and a running history of
past calculations.

## Features

- **Basic operations:** add, subtract, multiply, divide
- **Scientific operations:** power (x^y), square root, percentage
- **Memory functions:** M+ (add to memory), M- (subtract from memory),
  MR (recall memory), MC (clear memory)
- **Calculation history:** view a log of every calculation you've run
  this session
- **Error handling:** won't crash on invalid input or division by zero

## How to run

Make sure you have Python 3 installed, then run:

```bash
python calculator.py
```

Follow the on-screen menu and enter the number of the operation you want.

## Example

```text
=== Advanced Calculator ===

Add
Subtract
Multiply
Divide
Power
Sqrt
Percentage
M+
M-
MR
MC
History
Quit

Pick an option (1-13): 1
Enter first number: 4
Enter second number: 5

Result: 9.0
```

## Project Structure

```text
advanced-calculator/
├── calculator.py   # main calculator program
├── tests.py        # unit tests for calculator functions
└── README.md       # project documentation
```

Building this project helped me practice:

- Writing and organizing functions in Python
- Handling errors gracefully with `try`/`except`
- Working with global state (the memory feature)
- Using lists to track data over time (the history feature)
- Using Git and GitHub to track project history and publish code

## Future improvements

- Add unit tests
- Add support for more advanced operations (trigonometry, logarithms)
- Build a simple graphical interface (GUI) version

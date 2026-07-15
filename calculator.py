import math

# ---- Basic operations ----

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# ---- Scientific operations ----

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(x)

def percentage(x, y):
    return (x * y) / 100

# ---- Memory functions ----

memory = 0.0

def memory_add(value):
    global memory
    memory += value

def memory_subtract(value):
    global memory
    memory -= value

def memory_recall():
    return memory

def memory_clear():
    global memory
    memory = 0.0

# ---- History ----

history = []

def log_calculation(description, result):
    history.append(f"{description} = {result}")

def show_history():
    if not history:
        print("No calculations yet.")
    else:
        print("--- Calculation History ---")
        for entry in history:
            print(entry)

# ---- Input helper ----

def get_number(prompt):
    """Keep asking until the user types a real number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")

# ---- Main program ----

def main():
    print("=== Advanced Calculator ===")

    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square Root (of one number)")
        print("7. Percentage (x% of y)")
        print("8. Memory Add (M+)")
        print("9. Memory Subtract (M-)")
        print("10. Memory Recall (MR)")
        print("11. Memory Clear (MC)")
        print("12. View History")
        print("13. Quit")

        choice = input("Pick an option (1-13): ")

        if choice == "13":
            print("Goodbye!")
            break

        try:
            if choice == "6":
                num1 = get_number("Enter a number: ")
                result = square_root(num1)
                print("Result:", result)
                log_calculation(f"sqrt({num1})", result)

            elif choice == "10":
                print("Memory value:", memory_recall())

            elif choice == "11":
                memory_clear()
                print("Memory cleared.")

            elif choice == "8":
                num1 = get_number("Enter a number to add to memory: ")
                memory_add(num1)
                print("Memory is now:", memory_recall())

            elif choice == "9":
                num1 = get_number("Enter a number to subtract from memory: ")
                memory_subtract(num1)
                print("Memory is now:", memory_recall())

            elif choice == "12":
                show_history()

            elif choice in ("1", "2", "3", "4", "5", "7"):
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")

                if choice == "1":
                    result = add(num1, num2)
                    print("Result:", result)
                    log_calculation(f"{num1} + {num2}", result)
                elif choice == "2":
                    result = subtract(num1, num2)
                    print("Result:", result)
                    log_calculation(f"{num1} - {num2}", result)
                elif choice == "3":
                    result = multiply(num1, num2)
                    print("Result:", result)
                    log_calculation(f"{num1} * {num2}", result)
                elif choice == "4":
                    result = divide(num1, num2)
                    print("Result:", result)
                    log_calculation(f"{num1} / {num2}", result)
                elif choice == "5":
                    result = power(num1, num2)
                    print("Result:", result)
                    log_calculation(f"{num1} ^ {num2}", result)
                elif choice == "7":
                    result = percentage(num1, num2)
                    print("Result:", result)
                    log_calculation(f"{num1}% of {num2}", result)

            else:
                print("Invalid choice, try again.")

        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
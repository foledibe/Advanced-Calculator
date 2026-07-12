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

def get_number(prompt):
    """Keep asking until the user types a real number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")

def main():
    print("=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Pick an option (1-4): ")
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    try:
        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
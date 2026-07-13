# CALCULATOR PROGRAM.
# ------------------ #
def read_number(prompt):
    return float(input(prompt))


# 1. First part. Logic Math.
def calculate(n1, op, n2):
    match op:
        case '+': return n1 + n2
        case '-': return n1 - n2
        case '*': return n1 * n2
        case '/': return n1 / n2 if n2 != 0 else "Can NOT be divided by zero."
        case _: return "Invalid Operator."

# 2. Calculate Logic.
def run_calculator():
    print("--- Calculator Program ---")
    try:
        num1 = read_number("First number: ")
        oper = input("Operation: (+, -, /, *) ").strip()
        num2 = read_number("Second number: ")

        # Call the logic.
        result = calculate(num1, oper, num2)
        print(f"The result is: {result}")

    except ValueError:
        print("Invalid number. Please enter a numeric value.")
    except (EOFError, KeyboardInterrupt):
        print("\nEnd of the program.")
        raise SystemExit

#3. Loop Function.
if __name__ == "__main__":
    while True:
        run_calculator()
        try:
            user_choice = input("\nDo you want another calculation? (y/n) ").lower()
        except (EOFError, KeyboardInterrupt):
            user_choice = 'n'
        if user_choice != 'y':
            print("End of the program.")
            break

# CALCULATOR PROGRAM.
# ------------------ #
# 1. First part. Logic Math.
def calculate(n1, op, n2):
    match op:
        case '+': return n1 + n2
        case '-': return n1 - n2
        case '*': return n1 * n2
        case '/':
            if n2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return n1 / n2
        case _:
            raise ValueError(f"Invalid operator: {op!r}")

# 2. Calculate Logic.
def run_calculator():
    print("--- Calculator Program ---")
    try:
        num1 = float(input("First number: "))
        oper = input("Operation: (+, -, /, *) ").strip()
        num2 = float(input("Second number: "))

        # Call the logic.
        result = calculate(num1, oper, num2)
    except ValueError as err:
        print(f"Invalid input: {err}")
    except ZeroDivisionError as err:
        print(f"Math error: {err}")
    except (EOFError, KeyboardInterrupt):
        print("\nEnd of the program.")
        raise SystemExit
    else:
        print(f"The result is: {result}")

#3. Loop Function.
if __name__ == "__main__":
    while True:
        run_calculator()
        try:
            user_choice = input("\nDo you want another calculation? (y/n) ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            user_choice = 'n'
        if user_choice != 'y':
            print("End of the program.")
            break

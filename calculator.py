def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            print("Invalid operation selected.")
            return

        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

def is_even(number: int) -> bool:
    return number % 2 == 0


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def main():
    try:
        number = int(input("Enter a number: "))

        print(f"Even: {is_even(number)}")
        print(f"Prime: {is_prime(number)}")
        print(f"Positive: {number > 0}")

        if number >= 0:
            print(f"Factorial: {factorial(number)}")

    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()

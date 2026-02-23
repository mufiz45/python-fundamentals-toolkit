import datetime


def collect_user_data():
    """Collect user personal information."""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height (in meters): "))
    weight = float(input("Enter your weight (in kg): "))
    fav_number = int(input("Enter your favorite number: "))
    return name, age, height, weight, fav_number


def calculate_birth_year(age: int) -> int:
    current_year = datetime.datetime.now().year
    return current_year - age


def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)


def display_summary(name, age, height, weight, fav_number, birth_year, bmi):
    print("\n=== User Summary ===")
    print(f"Name: {name}")
    print(f"Age: {age} (Born approx. {birth_year})")
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"BMI: {bmi:.2f}")
    print(f"Favorite Number: {fav_number}")


def main():
    try:
        name, age, height, weight, fav_number = collect_user_data()
        birth_year = calculate_birth_year(age)
        bmi = calculate_bmi(weight, height)
        display_summary(name, age, height, weight, fav_number, birth_year, bmi)
    except ValueError:
        print("Invalid input. Please enter correct numeric values.")


if __name__ == "__main__":
    main()

import re


def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


def main():
    password = input("Enter your password: ")

    if is_strong_password(password):
        print("Strong password.")
    else:
        print("Weak password. Ensure it has at least 8 characters, one uppercase letter, one number, and one special character.")


if __name__ == "__main__":
    main()

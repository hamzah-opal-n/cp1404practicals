"""Password Stars"""

MINIMUM_LENGTH = 8
PASSWORD_PROMPT = "Enter password: "


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    password = input(PASSWORD_PROMPT)
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long")
        password = input(PASSWORD_PROMPT)
    return password


def print_asterisks(password):
    print("*" * len(password))


main()

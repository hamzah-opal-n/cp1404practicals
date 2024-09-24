"""Password Stars"""

MINIMUM_LENGTH = 8
PASSWORD_PROMPT = "Enter a password: "

password = input(PASSWORD_PROMPT)
while len(password) < MINIMUM_LENGTH:
    print(f"Password must be at least {MINIMUM_LENGTH} characters long")
    password = input(PASSWORD_PROMPT)
password_length = len(password)
print("*" * password_length)

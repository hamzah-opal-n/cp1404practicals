"""
Emails
Estimate: 20 minutes
Actual:   ?? minutes
"""


def main():
    """Create a database of emails and names based on user input"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = email
        choice = input(f"Is your name {name}? (Y/n)").upper()
        if choice not in ("Y", ""):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print(email_to_name)


main()

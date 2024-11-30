"""
Emails
Estimate: 20 minutes
Actual:   12 minutes
"""


def main():
    """Create a database of emails and names based on user input"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        choice = input(f"Is your name {name}? (Y/n) ").upper()
        if choice not in ("Y", ""):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email"""
    name = " ".join(email.split("@")[0].split(".")).title()
    return name


main()

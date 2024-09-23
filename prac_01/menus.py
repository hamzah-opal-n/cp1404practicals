"""
James Cook University
CP1404 - Practical 01 - Menus
By: Hamzah (Opal) Nutt (14693231, hamzah.nutt@my.jcu.edu.au)
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()

print("Finished.")

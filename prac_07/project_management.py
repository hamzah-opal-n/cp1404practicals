"""
Project Management Program
Estimate:   90 minutes
Start Time: 1242
End Time:   xxxx
Time Taken: xx minutes (with breaks)
"""

DEFAULT_FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects)\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit")
INPUT_PROMPT = ">>> "


def main():
    """Project management program"""
    print("Welcome to Pythonic Project Management")
    # Load projects from DEFAULT_FILENAME
    print(MENU)
    menu_choice = input(INPUT_PROMPT).upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            print("load from different file")
        elif menu_choice == "S":
            print("save to filename")
        elif menu_choice == "D":
            print("display projects")
        elif menu_choice == "F":
            print("filter projects")
        elif menu_choice == "A":
            print("add new project")
        elif menu_choice == "U":
            print("update project")
        else:
            print("Invalid choice")
        print(MENU)
        menu_choice = input(INPUT_PROMPT).upper()
    # ask if they want to save to default file
    print("Thank you for using custom-built project management software.")


main()

"""
Project Management Program
Estimate:   90 minutes
Start Time: 1242
End Time:   xxxx
Time Taken: 30 minutes (with breaks)
"""

from prac_07.project import Project

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
    projects = load_projects(DEFAULT_FILENAME)
    print(MENU)
    menu_choice = input(INPUT_PROMPT).upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            print("load from different file")
        elif menu_choice == "S":
            print("save to filename")
        elif menu_choice == "D":
            display_projects(projects)
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


def load_projects(filename):
    """Load projects from filename, values separated by tabs"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def display_projects(projects):
    """Display projects, sorted by priority and separated based on completion status"""
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    complete_projects = sorted([project for project in projects if project.is_complete()])
    print("Incomplete projects:")
    for incomplete_project in incomplete_projects:
        print(f"  {incomplete_project}")
    print("Completed projects:")
    for complete_project in complete_projects:
        print(f"  {complete_project}")


main()

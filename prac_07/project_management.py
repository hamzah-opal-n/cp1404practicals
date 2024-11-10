"""
Project Management Program
Estimate:   90 minutes
Start Time: 1242
End Time:   xxxx
Time Taken: 30 minutes (with breaks)
"""

import datetime
from prac_07.project import Project

DEFAULT_FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n"
        "- (S)ave projects\n"
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
            filter_projects_by_date(projects)
        elif menu_choice == "A":
            print("Let's add a new project")
            new_project = create_project()
            projects.append(new_project)
        elif menu_choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_number_choice = int(input("Project choice: "))
            print(projects[project_number_choice])
            projects[project_number_choice] = update_project(projects[project_number_choice])
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
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y")
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
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


def filter_projects_by_date(projects):
    """Display all projects that start on or after a given date"""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
    filtered_projects = [project for project in projects if project.starts_after_date(filter_date)]
    for project in sorted(filtered_projects, key=lambda project: project.start_date):
        print(project)


def update_project(project):
    """Update a project's percentage completion and priority"""
    new_percentage_text = input("New Percentage: ")
    if new_percentage_text != "":
        try:
            new_percentage = int(new_percentage_text)
            project.percent_complete = new_percentage
        except ValueError:
            print("Invalid input!")
    new_priority_text = input("New Priority: ")
    if new_priority_text != "":
        try:
            new_priority = int(new_priority_text)
            project.priority = new_priority
        except ValueError:
            print("Invalid input!")
    return project


def create_project():
    """Create a new project based on user input"""
    name = input("Name: ")
    start_date_string = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, percent_complete)


main()

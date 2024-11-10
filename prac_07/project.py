"""
Word Occurrences
Estimate: 120 minutes
Actual:   180 minutes

This time is also counting the time it taken to complete the other project file
"""
import datetime
from operator import attrgetter

from prac_07.project_management import ProjectManagement

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    filename = "projects.txt"
    projects = process_file(filename)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter a file name: ")
            projects = process_file(filename)
        elif choice == "S":
            save_to_file(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_string = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            display_projects_after_date(date, projects)
        elif choice == "A":
            print("Let's add a new project")
            name = get_valid_variable_type("Name: ", str)
            start_date = get_valid_date("Start date (dd/mm/yy): ")
            priority = get_valid_variable_type("Priority: ", int)
            cost_estimate = get_valid_variable_type("Cost estimate: ", float)
            completion_percentage = get_valid_percentage("Percent complete: ")
            projects.append(ProjectManagement(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            for i, project in enumerate(sorted(projects)):
                print(i, project)
            project_index = get_valid_variable_type("Project choice: ", int)
            project = projects[project_index]
            print(project)
            completion_percentage = get_valid_percentage("New Percentage: ")
            completion_percentage = get_default_if_string_empty(completion_percentage, project.completion_percentage)
            priority = get_valid_variable_type("New Priority: ", int)
            priority = get_default_if_string_empty(priority, project.priority)
            projects[project_index] = ProjectManagement(project.name, project.start_date, priority, project.cost_estimate, completion_percentage)
        else:
            print("Error invalid input")
        print(MENU)
        choice = input(">>> ").upper()


def get_valid_percentage(question):
    is_valid_input = False
    while not is_valid_input:
        try:
            percentage = float(input(question))
            if 0 <= percentage <= 100:
                is_valid_input = True
            else:
                print("Must be between 0 and 100")
        except ValueError:
            print("Invalid input")
    return percentage


def get_valid_variable_type(question, variable_type):
    is_valid_input = False
    while not is_valid_input:
        try:
            variable = variable_type(input(question))
            if isinstance(variable, (int, float)) and variable <= 0:
                print("Invalid must be more then 0")
            elif variable:
                is_valid_input = True
            else:
                print("Enter a value")
        except ValueError:
            print("Please invalid input value")
    return variable


def get_valid_date(question):
    is_valid_input = False
    while not is_valid_input:
        try:
            date = input(question)
            if datetime.datetime.strptime(date, "%d/%m/%Y").date():
                is_valid_input = True
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid date")
    return date


def get_default_if_string_empty(string, default):
    if not string:
        string = default
    return string


def display_projects_after_date(date, projects):
    for project in sorted(projects, key=attrgetter("converted_date")):
        if project.converted_date >= date:
            print(project)


def process_file(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            part = line.strip().split("\t")
            project = ProjectManagement(part[0], part[1], part[2], part[3], part[4])
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_to_file(projects, filename):
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    print("Incomplete projects:")
    for project in sorted(projects):
        if not project.is_complete():
            print(f"  {project}")

    print("Complete projects:")
    for project in sorted(projects):
        if project.is_complete():
            print(f"  {project}")


main()

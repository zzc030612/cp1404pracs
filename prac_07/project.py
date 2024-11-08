"""
Word Occurrences
Estimate: 120 minutes
Actual:   ?? minutes 90 + ??

This time is also counting the time it taken to complete the other project file
"""
import datetime
from operator import attrgetter

from pylint.pyreverse.inspector import Project

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
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            display_projects_after_date(date, projects)
        elif choice == "A":
            print("Let's add a new project")
            name = input("Name: ")
            start_date = input("Start date (dd/mm/yy): ")
            priority = input("Priority: ")
            cost_estimate = input("Cost estimate: ")
            completion_percentage = input("Percent complete: ")
            projects.append(ProjectManagement(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            pass
        else:
            print("Error invalid input")

        print(MENU)
        choice = input(">>> ").upper()


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
        for project in projects:
            print(f"{project.name}  {project.start_date}    {project.priority}    {project.cost_estimate}   "
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

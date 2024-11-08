"""
Word Occurrences
Estimate: 120 minutes
Actual:   ?? minutes

This time is also counting the time it taken to complete the other project file
"""
from prac_07.project_management import ProjectManagement

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    filename = "project.py"
    process_file(filename)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter a file name: ")
            projects = process_file(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Error invalid input")

        print(MENU)
        choice = input(">>> ").upper()


def process_file(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            part = line.split(" ")
            project = ProjectManagement(part[0], part[1], part[2], part[3], part[4])
            projects.append(project)
    return projects


main()

"""
Word Occurrences
Estimate: 90 minutes
Actual:   ?? minutes

This time is also counting the time it taken to complete the other project file
"""

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "L":
        pass
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

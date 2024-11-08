"""Prac 7, task 'More Guitars!'"""
from prac_07.guitar import Guitar


def main():
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)

    print("Owned Guitars:")
    for guitar in sorted(guitars):
        print(guitar)

    print()
    print("Enter new guitar details:")
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"New guitar added: {guitar}\n")
        print("Enter new guitar details:")
        name = input("Name: ")


main()

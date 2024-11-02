from operator import attrgetter

from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = input("Name: ")
while name:
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:,.2f} added.")
    name = input("Name: ")

max_name_length = max((len(guitar.name)) for guitar in guitars)
max_cost_length = max((len(str(guitar.cost))) for guitar in guitars)
max_cost_length += max_cost_length // 3  # The commas add extra characters to string. (a comma each 3 characters)

guitars.sort(key=attrgetter('cost'))

for i, guitar in enumerate(guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(
        f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth $ {guitar.cost:>{max_cost_length},.2f} {vintage_string}")

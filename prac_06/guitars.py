"""Guitar client code"""

from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost:.2f} added.\n")
    name = input("Name: ")

name_length = max(len(guitar.name) for guitar in guitars)
cost_length = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{name_length}} ({guitar.year}), "
          f"worth $ {guitar.cost:{cost_length},.2f}{vintage_string}")

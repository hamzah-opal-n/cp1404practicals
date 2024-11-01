"""Guitar client code"""

from prac_06.guitar import Guitar

guitars = []
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

name_length = max(len(guitar.name) for guitar in guitars)
cost_length = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>{name_length}} ({guitar.year}), "
          f"worth $ {guitar.cost:{cost_length},.2f}{vintage_string}")

"""More Guitars!"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Program to view and add guitar data"""
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)

    print("\nAdd new guitars (leave name blank to finish)")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    guitars.sort()
    display_guitars(guitars)
    save_guitars(guitars, FILENAME)
    print(f"Guitars saved to {FILENAME}")


def load_guitars(filename):
    """Load guitars from csv file"""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def save_guitars(guitars, filename):
    """Save guitars to csv file"""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            fields = (guitar.name, str(guitar.year), str(guitar.cost))
            out_file.write(",".join(fields) + "\n")


def display_guitars(guitars):
    """Display all guitars sorted by year"""
    name_length = max(len(guitar.name) for guitar in guitars)
    cost_length = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
    print("\nMy guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{name_length}} ({guitar.year}), "
              f"worth $ {guitar.cost:{cost_length},.2f}{vintage_string}")


main()

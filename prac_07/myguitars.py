"""More Guitars!"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Program to view guitar data"""
    guitars = load_guitars(FILENAME)
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

    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from filename"""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars sorted by year"""
    print("My guitars:")
    for guitar in sorted(guitars):
        print(guitar)


main()

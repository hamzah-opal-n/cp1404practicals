"""More Guitars!"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Program to view guitar data"""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from filename"""
    guitars = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars"""
    for guitar in guitars:
        print(guitar)


main()

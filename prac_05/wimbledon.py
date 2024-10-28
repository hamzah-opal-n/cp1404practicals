"""
Wimbledon
Estimate: 30 minutes
Actual:   18 minutes
"""

FILE_NAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Program to display the Wimbledon champions and their countries"""
    records = read_file(FILE_NAME)
    champion_to_count, winning_countries = process_records(records)
    display_winners(champion_to_count, winning_countries)


def read_file(file_name):
    """Read input csv file"""
    records = []
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Advance past header
        for line in in_file:
            records.append(line.strip().split(","))
    return records


def process_records(records):
    """Extract champion win counts and countries from records"""
    winning_countries = set()
    champion_to_count = {}
    for record in records:
        country = record[COUNTRY_INDEX]
        champion = record[CHAMPION_INDEX]
        winning_countries.add(country)
        try:
            champion_to_count[champion] += 1
        except KeyError:
            champion_to_count[champion] = 1
    return champion_to_count, winning_countries


def display_winners(champion_to_count, winning_countries):
    """Display champions and winning countries"""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winning_countries)))


main()

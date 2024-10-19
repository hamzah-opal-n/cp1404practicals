"""
Wimbledon
Estimate: 30 minutes
Actual:   ?? minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Program to display the Wimbledon champions and their countries"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            records.append(line.strip().split(","))
    champion_to_count, winning_countries = process_records(records)
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(winning_countries)))


def process_records(records):
    """Extract champion win counts and countries from records"""
    champion_to_count = {}
    winning_countries = set()
    for record in records:
        country = record[COUNTRY_INDEX]
        champion = record[CHAMPION_INDEX]
        winning_countries.add(country)
        try:
            champion_to_count[champion] += 1
        except KeyError:
            champion_to_count[champion] = 1
    return champion_to_count, winning_countries


main()

FILENAME = "wimbledon.csv"


def read_wimbledon_data(filename):
    """Read data from the Wimbledon CSV file and return a list of [champion, country] rows."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        data = []
        for line in in_file:
            parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            data.append([champion, country])
    return data


def count_champions(data):
    """Return a dictionary mapping champions to the number of times they won."""
    champion_to_count = {}

    for champion, _ in data:
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count


def get_countries(data):
    """Return a sorted set of unique countries from the data."""
    countries = {country for _, country in data}
    return sorted(countries)


def main():
    data = read_wimbledon_data(FILENAME)
    champion_to_count = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_count.items()):
        print(f"{champion:20} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()

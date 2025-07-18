from guitar import Guitar


def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted by year:")
    display_guitars(guitars)

    print("\nAdd new guitars:")
    guitars.extend(add_new_guitars())

    save_guitars(filename, guitars)
    print(f"\nAll guitars saved to {filename}.")


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    try:
        with open(filename, 'r') as in_file:
            for line in in_file:
                parts = line.strip().split(',')
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars


def display_guitars(guitars):
    """Display a list of guitars with formatting."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")


def add_new_guitars():
    """Ask the user for new guitars and return them as a list."""
    new_guitars = []
    while True:
        name = input("Name: ")
        if name == "":
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            new_guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Please enter a valid year and cost.")
    return new_guitars


def save_guitars(filename, guitars):
    """Write the list of guitars to a CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()

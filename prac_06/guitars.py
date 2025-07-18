from guitar import Guitar

def main():
    """Let user enter guitar details and display formatted list."""

    print("My guitars!")

    guitars = []

    # Uncomment to allow manual input
    # while True:
    #     name = input("Name: ")
    #     if not name:
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     print(f"{guitar} added.\n")

    # Comment these out when using real input
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()

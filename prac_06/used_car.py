from prac_06.car import Car

def main():
    """Demo test code to show how to use the Car class with multiple car objects."""

    # Create a Car object called "my_car" with 180 units of fuel
    my_car = Car("MyCar", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new Car object called "limo" with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 units of fuel to the limo
    limo.add_fuel(20)

    # Print the amount of fuel in the limo
    print(f"Limo has fuel: {limo.fuel}")

    # Attempt to drive the limo 115 km
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven} km")

    # Print the limo's state using __str__
    print(limo)


if __name__ == "__main__":
    main()


from unreliable_car import UnreliableCar

def main():
    # Create a car with 50% reliability and lots of fuel
    test_car = UnreliableCar("Unreliable", 1000, 50.0)

    attempts = 100
    successful_drives = 0

    for i in range(attempts):
        distance = test_car.drive(1)  # Try to drive 1km each time
        if distance > 0:
            successful_drives += 1

    print(f"Attempted to drive {attempts} times.")
    print(f"Successful drives: {successful_drives}")
    print(f"Expected success range (around 50%): ~{attempts * 0.5:.0f}")

main()

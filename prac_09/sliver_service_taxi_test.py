from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 2)  # fanciness of 2
    taxi.drive(18)  # drive 18 km
    fare = taxi.get_fare()

    print(taxi)
    print(f"Fare: ${fare:.2f}")

    # Assertion to confirm correct fare (18 km * 1.23 * 2 + 4.50 = 48.78 -> rounded to 48.80)
    assert round(fare, 2) == 48.80, f"Expected $48.80 but got ${fare:.2f}"

main()

class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0.0):
        """
        Initialize a Car instance.

        :param fuel: float, amount of fuel in the tank (1 unit = 1 km of driving)
        """
        self.fuel = fuel
        self._odometer = 0.0


    def add_fuel(self, amount):
        """
        Add the specified amount of fuel to the car.

        :param amount: float, amount of fuel to add
        """
        if amount < 0:
            raise ValueError("Fuel amount must be non-negative.")
        self.fuel += amount

    def drive(self, distance):
        """
        Drive the car for the given distance if enough fuel is available.

        If not enough fuel, drive only as far as possible.

        :param distance: float, requested distance to drive
        :return: float, actual distance driven
        """
        if distance < 0:
            raise ValueError("Distance must be non-negative.")

        actual_distance = min(distance, self.fuel)
        self.fuel -= actual_distance
        self._odometer += actual_distance
        return actual_distance

    def get_odometer(self):
        """
        Return the total distance the car has driven.

        :return: float, odometer reading
        """
        return self._odometer

    def __str__(self):
        """
        Return a string representation of the Car.

        :return: str
        """
        return f"Fuel: {self.fuel:.1f}, Odometer: {self._odometer:.1f}"

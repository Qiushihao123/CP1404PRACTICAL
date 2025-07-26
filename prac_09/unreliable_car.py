import random
from car import Car  # Make sure car.py is in the same directory or accessible

class UnreliableCar(Car):
    """A Car that may not always drive when asked, depending on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on its reliability."""
        if random.uniform(0, 100) < self.reliability:
            # If it's reliable this time, drive normally
            return super().drive(distance)
        else:
            # Car doesn't drive at all
            return 0

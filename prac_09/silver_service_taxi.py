from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi with higher price and flagfall charge."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with fanciness scaling."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # override instance's price_per_km

    def get_fare(self):
        """Return the fare for the trip including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation with flagfall."""
        return f"{super().__str__()}, ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}"

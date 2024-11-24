"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with a different price per km, and includes fanciness and flagfall costs."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi.

        fanciness: float, multiples/scales price_per_km
        """
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall cost."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f})"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

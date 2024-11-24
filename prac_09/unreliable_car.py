"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from prac_09.car import Car
import random

MINIMUM_RELIABILITY = 0
MAXIMUM_RELIABILITY = 100


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car.

        reliability: float, range 0 to 100, percentage chance of actually driving
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but based on reliability."""
        if random.randint(MINIMUM_RELIABILITY, MAXIMUM_RELIABILITY) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven

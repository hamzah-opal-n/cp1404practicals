"""
Guitar
Estimate:   30 minutes
Start Time: 2305
End Time:   2337
Time Taken: 32 minutes
"""

CURRENT_YEAR = 2024
VINTAGE_AGE_THRESHOLD = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Car instance.

        name: string
        year = integer
        cost: float
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """String to represent a Guitar instance."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Calculate the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE_THRESHOLD

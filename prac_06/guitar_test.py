"""Guitar class test"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 0)
vintage_guitar = Guitar("Vintage Guitar", 1974, 0)

print(f"Gibson L-5 CES get_age() - Expected 102. Got {gibson.get_age()}")
print(f"Another Guitar get_age() - Expected 11. Got {another_guitar.get_age()}")
print(f"Vintage Guitar get_age() - Expected 50. Got {vintage_guitar.get_age()}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
print(f"Vintage Guitar is_vintage() - Expected True. Got {vintage_guitar.is_vintage()}")

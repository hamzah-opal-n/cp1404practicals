"""SilverServiceTaxi class test"""

from prac_09.silver_service_taxi import SilverServiceTaxi

hummer = SilverServiceTaxi("Hummer", 200, 4.0)
print(hummer)

fancy_taxi = SilverServiceTaxi("Fancy Taxi", 1000, 2.0)
fancy_taxi.drive(18)
assert fancy_taxi.get_fare() == 48.78

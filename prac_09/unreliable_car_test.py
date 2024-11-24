"""UnreliableCar class test"""

from prac_09.unreliable_car import UnreliableCar

my_broken_car = UnreliableCar("Death Trap", 1000, 50)
for i in range(10):
    my_broken_car.drive(60)
    print(my_broken_car)

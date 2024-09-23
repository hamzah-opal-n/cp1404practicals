"""
James Cook University
CP1404 - Practical 01 - Loops
By: Hamzah (Opal) Nutt (14693231, hamzah.nutt@my.jcu.edu.au)
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end='')
print()

# d.
for i in range(number_of_stars):
    print("*" * (i + 1))
print()

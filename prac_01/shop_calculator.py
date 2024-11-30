"""
James Cook University
CP1404 - Practical 01 - Shop Calculator
By: Hamzah (Opal) Nutt (14693231, hamzah.nutt@my.jcu.edu.au)
"""

DISCOUNT_RATE = 0.1
MINIMUM_ITEMS = 0
DISCOUNT_THRESHOLD = 100

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < MINIMUM_ITEMS:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD:
    total_price -= (total_price * DISCOUNT_RATE)

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

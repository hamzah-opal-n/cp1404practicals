"""Quick Pick Lottery Ticket Generator"""

import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6

number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    pick = []
    for j in range(NUMBERS_PER_PICK):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in pick:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        pick.append(number)
    pick.sort()
    print(" ".join(f"{number:>{len(str(MAXIMUM_NUMBER))}}" for number in pick))

"""Quick Pick Lottery Ticket Generator"""

import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6

pick = []
for i in range(NUMBERS_PER_PICK):
    number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    while number in pick:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    pick.append(number)
print(sorted(pick))

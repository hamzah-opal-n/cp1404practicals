"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MINIMUM_SALES = 0
MAXIMUM_SALES = 1000
MINIMUM_BONUS = 0.1
MAXIMUM_BONUS = 0.15

sales = float(input("Enter sales: $"))

while sales >= MINIMUM_SALES:
    if sales < MAXIMUM_SALES:
        bonus_rate = MINIMUM_BONUS
    else:
        bonus_rate = MAXIMUM_BONUS
    final_bonus = sales * bonus_rate
    print(f"Bonus: ${final_bonus:.2f}")
    sales = float(input("Enter sales: $"))

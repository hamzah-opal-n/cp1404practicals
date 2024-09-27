"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randint

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Score status program with random score generator"""
    score = float(input("Enter score: "))
    message = determine_score_status(score)
    print(message)
    random_score = randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(f"Random score: {random_score}\nStatus: {determine_score_status(random_score)}")


def determine_score_status(score: float) -> str:
    """Determine status from score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    return "Bad"


main()

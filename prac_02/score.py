"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Score status program"""
    score = float(input("Enter score: "))
    message = determine_score_status(score)
    print(message)


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

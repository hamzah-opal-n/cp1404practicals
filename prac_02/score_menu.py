"""Score menu program."""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
CHOICE_PROMPT = ">>> "
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50


def main():
    """Menu-based program to get score and determine status."""
    score = get_valid_score(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(f"Current score: {score}")
    print(MENU)
    choice = input(CHOICE_PROMPT).upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            result = determine_score_status(score)
            print(f"Result: {result}")
        elif choice == "S":
            pass
        else:
            print("Invalid choice!")
        print(f"Current score: {score}")
        print(MENU)
        choice = input(CHOICE_PROMPT).upper()


def determine_score_status(score: float) -> str:
    """Determine status from score."""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    return "Bad"


def get_valid_score(minimum: int, maximum: int) -> float:
    """Get a score within a specified range."""
    score = float(input("Enter a score: "))
    while score < minimum or score > maximum:
        print(f"Score must be {MINIMUM_SCORE} to {MAXIMUM_SCORE} inclusive!")
        score = float(input("Enter a score: "))
    return score


main()

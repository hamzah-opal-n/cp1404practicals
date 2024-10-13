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
    score = get_valid_number(MINIMUM_SCORE, MAXIMUM_SCORE, "Enter score: ")
    print(f"\nCurrent score: {score}\n{MENU}")
    choice = input(CHOICE_PROMPT).upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number(MINIMUM_SCORE, MAXIMUM_SCORE, "Enter new score: ")
        elif choice == "P":
            result = determine_score_status(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_character("*", score)
        else:
            print("Invalid choice!")
        print(f"\nCurrent score: {score}\n{MENU}")
        choice = input(CHOICE_PROMPT).upper()
    print("Thank you, goodbye!")


def determine_score_status(score: float) -> str:
    """Determine status from score."""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        return "Passable"
    return "Bad"


def get_valid_number(minimum: int, maximum: int, prompt: str) -> float:
    """Get a number within a specified range."""
    number = float(input(prompt))
    while number < minimum or number > maximum:
        print(f"Input must be {minimum} to {maximum} inclusive!")
        number = float(input(prompt))
    return number


def print_character(character: str, length: float):
    print(character * int(length))


main()

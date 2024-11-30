"""Wikipedia Page Search"""

import wikipedia
from wikipedia import DisambiguationError

INPUT_PROMPT = "Enter page title: "


def main():
    """Program to search for Wikipedia pages based on user input."""
    search_term = input(INPUT_PROMPT)
    while search_term != "":  # while input is not blank
        try:
            page = wikipedia.page(search_term, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except DisambiguationError:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(wikipedia.search(search_term))
        print()
        search_term = input(INPUT_PROMPT)
    print("Thank you.")


main()

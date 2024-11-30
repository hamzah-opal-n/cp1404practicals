"""Wikipedia Page Search"""

import wikipedia

INPUT_PROMPT = "Enter page title: "


def main():
    """Program to search for Wikipedia pages based on user input."""
    search_term = input(INPUT_PROMPT)
    while search_term != "":  # while input is not blank
        page = wikipedia.page(search_term)
        print(page.title)
        print(page.summary)
        print(page.url)
        search_term = input(INPUT_PROMPT)
    print("Thank you.")


main()

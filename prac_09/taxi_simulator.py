"""Taxi Simulator"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Simulator program."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()

    while menu_choice != "q":

        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")
            try:
                taxi_choice = int(taxi_choice)
                if taxi_choice >= 0:
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except (IndexError, ValueError):
                print("Invalid taxi choice")

        elif menu_choice == "d":
            print("Drive")
            print(current_taxi)

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()

"""Taxi Simulator"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi Simulator program"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Choose Taxi")
        elif menu_choice == "d":
            print("Drive")
        else:
            print("Invalid option")
        print("Bill to date: xxxxx")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Total trip cost: $xxx.xx")
    print("Taxis are now:")


main()

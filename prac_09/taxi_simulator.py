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
            if current_taxi:
                distance_to_drive = input("Drive how far? ")
                try:
                    distance_to_drive = float(distance_to_drive)
                    if distance_to_drive > 0:
                        current_taxi.start_fare()
                        current_taxi.drive(distance_to_drive)
                        trip_cost = current_taxi.get_fare()
                        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                        total_bill += trip_cost
                    else:
                        print("Distance must be > 0")
                except ValueError:
                    print("Invalid distance")

            else:
                print("You need to choose a taxi before you can drive")

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

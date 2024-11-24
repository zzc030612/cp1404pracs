from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Menu-driven taxi simulator."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = get_taxi(taxis, current_taxi)
        elif choice == "d":
            if current_taxi:
                if current_taxi.fuel != 0:
                    try:
                        current_taxi.start_fare()
                        distance_driven = int(input("Drive how far? "))
                        current_taxi.drive(distance_driven)
                        total_cost += current_taxi.get_fare()
                        print(f"{current_taxi.name} trip cost you ${total_cost}")
                    except ValueError:
                        print("Invalid input")
                else:
                    print(f"The {current_taxi.name} has no fuel.")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: {total_cost}")
        print(MENU)
        choice = input(">>> ").lower()
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all the taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_taxi(taxis, current_taxi):
    """Get a new taxi or return previous taxi."""
    display_taxis(taxis)
    try:
        taxi_index = int(input(">>> "))
        if  0 <= taxi_index < len(taxis):
            current_taxi = taxis[taxi_index]
            return current_taxi
    except ValueError:
        pass
    print("Invalid taxi choice")
    return current_taxi




main()
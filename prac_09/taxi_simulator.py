from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    choice = input(">>> ")
    while choice != "q":
        if choice == "c":
            current_taxi = get_taxi(taxis)
        elif choice == "d":
            pass
        else:
            print("Invalid option")
        print("Bill to date: ")
        print(MENU)
        choice = input(">>> ")


def get_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_index = int(input(">>> "))
        if  0 <= taxi_index < len(taxis):
            current_taxi = taxis[taxi_index]
            return current_taxi
        print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")



main()
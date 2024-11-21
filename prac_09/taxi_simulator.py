
MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    choice = input(MENU)
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            pass
        else:
            print("Invalid option")
        print("Bill to date: ")
        choice = input(MENU)

main()
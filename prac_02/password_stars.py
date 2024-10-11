"""Password error checking program."""
MIN_LENGTH = 5


def main():
    """Prints a valid password as asterisks."""
    password = get_valid_password()
    print_asterisk(password)


def print_asterisk(password):
    """Prints asterisks to replace given password."""
    for i in password:
        print("*", end="")


def get_valid_password():
    """Get a password above the MIN_LENGTH."""
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password


main()

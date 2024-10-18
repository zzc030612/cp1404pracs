name_to_email = {}
email = input("Email: ")
while email:
    # Expected result:
    # corey.camilleri@my.jcu.edu.au
    names = email.split("@")[0].split(".")
    name = " ".join([name.title() for name in names])
    choice = input(f"Is your name {name}? (Y/n) ")
    if choice.upper() == "N" or choice.upper() == "NO":
        name = input("Name: ")
    name_to_email[name] = email
    email = input("Email: ")

print()
for name, email in name_to_email.items():
    print(f"{name} ({email})")

name_to_email = {}
email = input("Email: ")
while email:
    names = email.split("@")[0].split(".")
    name = " ".join([item.title() for item in names])
    choice = input(f"Is your name {name}? (Y/n) ")
    if choice.upper() == "N" or choice.upper() == "NO":
        name = input("Name: ")
    name_to_email[name] = email
    email = input("Email: ")

print()
for name, email in name_to_email.items():
    print(f"{name} ({email})")

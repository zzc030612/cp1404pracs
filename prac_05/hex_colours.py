
CODE_TO_NAME = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff",
                "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "ffbf00",
                "Amethyst": "#9966cc", "Antique White": "#faebd7", "Apricot": "#fbceb1",
                "Aqua": "#00ffff"}

max_name_length = max([len(name) for name in CODE_TO_NAME.values()])
max_code_length = max([len(code) for code in CODE_TO_NAME.keys()])

print("Available colours:")

for code, name in CODE_TO_NAME.items():
    print(f"{code:{max_code_length}}")

state_code = input("Enter colour name: ").title()
while state_code != "":
    try:
        if state_code in CODE_TO_NAME:
            print(state_code, "is", CODE_TO_NAME[state_code])
        else:
            raise ValueError
    except ValueError:
        print(f"Invalid colour name: {state_code}")
    state_code = input("Enter colour name: ").title()

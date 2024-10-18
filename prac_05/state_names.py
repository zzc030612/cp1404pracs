"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

max_name_length = max([len(name) for name in CODE_TO_NAME.values()])
max_code_length = max([len(code) for code in CODE_TO_NAME.keys()])

for code, name in CODE_TO_NAME.items():
    print(f"{code:{max_code_length}} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print(f"Invalid state: {state_code}")
    state_code = input("Enter short state: ").upper()

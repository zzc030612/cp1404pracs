"""
CP1404/CP5632 - Practical
Test multiple file reading functions
"""

name = input("What is your name? ")
out_file = open(f"{name}.txt", "w")
print(name, file=out_file)
out_file.close()

in_file = open(f"{name}.txt", "r")
print(f"Hi {in_file.readline().strip()}!")
in_file.close()

with open(f"numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    total = first_number + second_number
    print(total)

total = 0
with open('numbers.txt', 'r') as numbers:
    for line in numbers:
        total += int(line)
print(total)

"""
CP1404/CP5632 Practical
Generate 6 random numbers for each a number of lines based on user input
"""
import random

MIN = 1
MAX = 45
NUMBER_OF_COLUMNS = 6
number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    random_numbers = []
    while len(random_numbers) < NUMBER_OF_COLUMNS:
        random_number = random.randint(MIN, MAX)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    print(("{:2} " * NUMBER_OF_COLUMNS).format(*sorted(random_numbers)))

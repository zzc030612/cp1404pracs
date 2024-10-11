import random
NUMBER_OF_COLUMNS = 6
number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    random_numbers = []
    while len(random_numbers) < NUMBER_OF_COLUMNS:
        random_number = random.randint(1, 45)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    print(("{:2} "*NUMBER_OF_COLUMNS).format(*sorted(random_numbers)))

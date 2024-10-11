"""
CP1404/CP5632 Practical
List manipulation
"""
numbers = [3, 1, 4, 1, 5, 9, 2]
# these values are integers

print(numbers[1] + numbers[2])
numbers[0] = '10'
numbers[-1] = 1
print(numbers[2:])
if 9 in numbers:
    print("9 is in the list")

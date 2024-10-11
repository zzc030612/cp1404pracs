"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- When a value entered is not the expected value, in this code typing letters or float values will raise a ValueError as an integer is expected.
2. When will a ZeroDivisionError occur?
- When you divide a number by zero will raise a ZeroDivisionError.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- You could write a function to get valid numbers, following the error checking pattern or do a simple if statement to check if 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("The denominator cannot be 0.")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

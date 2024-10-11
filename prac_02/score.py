"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    """Print the grade of the user."""
    score = float(input("Enter score: "))
    print(determine_grade(score))
    print(determine_grade(random.randint(0, 100)))


def determine_grade(score):
    """Determine the grade based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"


main()

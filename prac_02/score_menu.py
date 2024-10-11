"""
CP1404/CP5632 - Practical
Menu-driven program that prints grade or stars.
"""

MENU = """(G)et a valid score
(P)rint grade
(S)how stars
(Q)uit"""


def main():
    """Menu-driven program that prints grade or stars based on score."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(determine_grade(score))
        elif choice == 'S':
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()


def determine_grade(score):
    """Determine the grade based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"


def get_valid_score():
    """Get a score between 0 and 100."""
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter your score: "))
    return score


main()

"""
Purpose: Dice rolling game that gives the user options to roll different types of dices.
Author: Treon Washington
Course: CSC6301
Date: September 4, 2026
"""

import random

def RollDice(desiredNumberOfSides):
    """
    Rolls a dice with the specified number of sides and returns the result.
    Argument: desiredNumberOfSides (int): The number of sides on the dice to roll.
    Returns: int: A random integer between 1 and desiredNumberOfSides, inclusive.
    """
    return random.randint(1, desiredNumberOfSides)

def main():
    validDice = [4, 6, 8, 10, 12, 20]

    while True:
        try:
            desiredNumberOfSides = int(input("What size dice would you like to roll? "))

        except ValueError:
            print("Please enter a valid integer.")
            continue

        if desiredNumberOfSides in validDice:
            roll = RollDice(desiredNumberOfSides)
            print(f"You rolled: {roll}")
        else:
            print("Invalid dice size. Please choose from the following options: 4, 6, 8, 10, 12, or 20.")
            continue

        rollAgain = input("Would you like to roll again? (yes/no): ").lower()
        if rollAgain == "no":
            print("Thank you for playing!")
            break

        while rollAgain != "yes":
            print("Please enter yes or no.")
            rollAgain = input("Would you like to roll again? (yes/no): ").lower()

            if rollAgain == "no":
                print("Thank you for playing!")
                break

if __name__ == "__main__":
    main()




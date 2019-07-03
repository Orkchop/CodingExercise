# Author Ian Rosenfield
# P1) Guessing Game
# Write a number guessing game. Keep asking the user to guess a number between 1 and 100 until they guess correctly.
# If the number the user guesses is too high, tell them so. Same with if the number is too low. Congratulate them when
# they’ve guessed the correct number and tell them how many guesses they used to get to the correct number.

import random

# You could put the whole game in a while loop here and ask them if they want to play again after they guess

secretNumber = random.randint(1, 101)
tries = 0

# Introduction to the game and getting their first guess
print("Can you guess what number I am thinking of?")
guess = int(input("Please guess a number: "))
tries += 1

# Keep looping until they guess the correct number
while guess != secretNumber:
    if guess < secretNumber:
        print("That was too low.")
        guess = int(input("lease guess a higher number: "))
        tries += 1
    else:
        print("That was too high.")
        guess = int(input("lease guess a lower number: "))
        tries += 1

# A Winner Is You!
print("Congratulations! You guessed it!\nThe number was %s. you guess it in %s tries!" % (secretNumber, tries))

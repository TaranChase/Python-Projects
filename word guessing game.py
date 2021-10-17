# Title: Python program for word guessing game
#  Author: ngrover241
#  Date: 08 Sep, 2020
#  Code version: Python3
#  Availability: https://www.geeksforgeeks.org
# ----------------------------------------------
# (Version Python3)[Source code].https://www.geeksforgeeks.org
#--------------------------------------------------------------

import random  # used to choose random words from list of words.

name = input("Enter Name:")
print("Let's Play!", name)

words = ['dove', 'passion', 'lime', 'rose', 'horse', 'purple', 'jade', 'python', 'program', 'colloseum']

# Choosing one random word from list of words
w = random.choice(words)

print("Guess the letters")

guesses = ''

#Number of turns
turns = 20

while turns > 0:
    fail = 0

    for let in w:
        if let in guesses:
            print(let)
        else:
            print("-")
            fail = fail + 1

    if fail == 0:
        print("Congratulations!, You Won.")
        print("Word:", w)
        break

    guess = input("guess a letter")
    guesses = guesses + guess

    if guess not in w:
        turns = turns - 1

        print("Incorrect!")

        print("You have", + turns, "more guesses")

        if turns == 0:
            print("You lose!")

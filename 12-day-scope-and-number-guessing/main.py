#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

number = random.randint(1,100)
attemps = 0
guessed = False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input('Choose a difficulty. Type "easy" or "hard": ')
if difficulty == 'easy':
    attemps = 10
else:
    attemps = 5

while attemps > 0 and not guessed:
    print(f"You have {attemps} remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > number:
        print("Too high.")
        attemps -= 1
        print("Guess Again.")
    elif guess < number:
        print("Too low.")
        attemps -= 1
        print("Guess Again.")
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        guessed = True

    if attemps == 0:
        print("You've run out of guesses, you lose.")

#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter: ")
guess = guess.lower()

#TCheck if the letter the user guessed (guess) is one of the letters in the chosen_word.
for c in chosen_word:
    if c == guess:
        print("Right")
    else:
        print("Wrong")
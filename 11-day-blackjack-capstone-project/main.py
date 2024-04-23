############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


#I choose expert difficulty
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
computer_hand = []

def calculate_score(hand):
    score = 0
    for card in hand:
        score += card

    return score

def first_hand():
    user_hand.clear()
    computer_hand.clear()
    user_hand.append(random.choice(cards))
    user_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))

def append_card(hand):
    current_score = calculate_score(hand)
    choice = random.choice(cards)
    if choice == 11 and current_score > 10:
        choice = 1
    hand.append(choice)

def final_scores(user_hand, computer_hand):
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"\tYour final hand: {user_hand}, final score: {user_score}")
    print(f"\tComputer's final hand: {computer_hand}, final score: {computer_score}")
    if computer_score == 21:
        print("\tYou lose. Computer has blackjack 😱")
    elif user_score > computer_score and user_score <= 21:
        print("\tYou win 😃")
    elif user_score < computer_score and user_score <= 21 and computer_score <= 21:
        print("\tYou lose 😤")
    elif user_score == computer_score and user_score <= 21 and computer_score <= 21:
        print("\tYou Draw 🙃")
    elif user_score > 21:
        print("\tYou went over. You Lose 😭")
    elif computer_score > 21:
        print("\tComputer's went over. You win 😁")

print(logo)
def blackjack_game():
    more_game = input("Do you want to play a game of Blacjack? Type 'y' or 'n':")
    if more_game != 'y':
        return
    else:
        clear()
        print(logo)
        first_hand()
        another_card = True
        computer_score = calculate_score(computer_hand)
        if computer_score == 21:
            final_scores(user_hand, computer_hand)
            another_card = False
            blackjack_game()
        while another_card:
            print(f"\tYour cards: {user_hand}, current score: {calculate_score(user_hand)}")
            print(f"\tComputer's first card: {computer_hand[0]}")
            more_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if more_card != 'y':
                another_card = False
                computer_score = calculate_score(computer_hand)
                while computer_score < 17:
                    append_card(computer_hand)
                    computer_score = calculate_score(computer_hand)
                final_scores(user_hand, computer_hand)
                blackjack_game()
            else:
                append_card(user_hand)
                user_score = calculate_score(user_hand)
                if user_score > 21:
                    final_scores(user_hand, computer_hand)
                    another_card = False
                    blackjack_game()

blackjack_game()




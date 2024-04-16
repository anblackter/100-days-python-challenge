rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
options = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
print(f"You chose:\n{options[input]}")
print(f"Computer chose:\n{options[computer_choice]}")
if input == computer_choice:
    print("It's a draw.")
elif input == 0 and computer_choice == 2:
    print("You win.")
elif input == 1 and computer_choice == 0:
    print("You win.")
elif input == 2 and computer_choice == 1:
    print("You win.")
elif input > 2:
    print("Invalid number. You lose.")
else:
    print("You lose.")

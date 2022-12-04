import random

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

images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number and you lost automatically.")
else:
    print(f"You chose {images[user_choice]}")
    computer_choice = random.randint(0, 2)
    print(f"The computer chose {images[computer_choice]}")

# The logic behind "Who wins". (Rock beats scissors. Scissors beat paper. Paper beats rock.)
if user_choice >= 3 or user_choice < 0:
    print("Restart the game to play again.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose.")
elif computer_choice > user_choice:
    print("You lose.")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw.")

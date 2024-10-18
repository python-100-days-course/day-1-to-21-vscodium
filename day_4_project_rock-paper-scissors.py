# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 4 Project - Rock Paper Scissors Game

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

#Write your code below this line 👇

rock_paper_scissors_list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

print(rock_paper_scissors_list[user_choice])

computer_choice = random.randint(0, 2)

print(f"Computer chose:\n\n {rock_paper_scissors_list[computer_choice]}")

# rules:
# 0 beats 2
# 1 beats 0
# 2 beats 1

if user_choice == computer_choice:
    print("It's a draw!\n")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!\n")
elif (user_choice == 2 and computer_choice == 0) or (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2):
    print("You lose!\n")
else:
    print("Oops, something went wrong!")
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

my_choice = int(input("What do you choose?  Type 0 for Rock, 1 for Paper, or 2 for Scissors"))

computer_choice = random.randint(0, 2)

if my_choice == 0:
    print(rock)
elif my_choice == 1:
    print(paper)
elif my_choice == 2:
    print(scissors)

print("Computer chooses:  ")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if (my_choice == 0 and computer_choice == 0) or (my_choice == 1 and computer_choice == 1) or (
        my_choice == 2 and computer_choice == 2):
    print("Tie!  ")
elif (my_choice == 0 and computer_choice == 2) or (my_choice == 1 and computer_choice == 0) or (
        my_choice == 2 and computer_choice == 1):
    print("You win!  ")
elif (my_choice == 0 and computer_choice == 1) or (my_choice == 1 and computer_choice == 2) or (
        my_choice == 2 and computer_choice == 0):
    print("You lose!  ")
else:
    print("Invalid input!  ")

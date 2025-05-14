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

player = int(input("What do you chose?\n"
      "Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

if player == 0:
    print(rock);
    if computer == 0:
        print("Computer chose: \n" + rock)
        print("Tie!")
    elif computer == 1:
        print("Computer chose: \n" + paper)
        print("You lose!")
    elif computer == 2:
        print("Computer chose: \n" + scissors)
        print("You win!")
elif player == 1:
    print(paper)
    if computer == 0:
        print("Computer chose: \n" + rock)
        print("You win!")
    elif computer == 1:
        print("Computer chose: \n" + paper)
        print("Tie!")
    elif computer == 2:
        print("Computer chose: \n" + scissors)
        print("You lose!")
elif player == 2:
    print(scissors)
    if computer == 0:
        print("Computer chose: \n" + rock)
        print("You lose!")
    elif computer == 1:
        print("Computer chose: \n" + paper)
        print("You win!")
    elif computer == 2:
        print("Computer chose: \n" + scissors)
        print("Tie!")
else:
    print("Invalid.")





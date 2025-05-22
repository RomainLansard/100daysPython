from imghdr import tests

import art
import random

def game_loop(chances):
    while chances + 1 != 0:
        print(f"You have {chances + 1} attempts remaining to guess the number.")
        while True:
            try:
                guess = int(input("Make a guess:    "))
                break
            except ValueError:
                print("That's not a valid number. Try again.")
        if guess < number:
            print("Too low.")
            chances -= 1
        elif guess > number:
            print("Too high")
            chances -= 1
        elif guess == number:
            print(f"You got it! The answer was {number}")
            return True

    print(f"You lose. The answer was {number}")
    return True

def guessing_game():
    game_over = False
    global number #Makes global a global variabl
    number = random.randint(1, 100) #randomises a number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. "
          "Type 'easy' or 'hard':   ").lower()
    while not game_over:
        if difficulty == 'hard':
            chances = 4
            game_over = game_loop(chances)

        elif difficulty == 'easy':
            chances = 9
            game_over = game_loop(chances)

        else:
            print("Wrong input, please write 'easy' or 'hard' "
                  "Refresh to play again.")
            game_over = True
            print("\n" * 20)
            guessing_game()

print(art.logo)
guessing_game()
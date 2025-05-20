import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# print(art.logo)
def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
        game_state = False
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

    # score_user = sum(user_cards)
    # score_computer = sum(computer_cards)
def black_jack():
    game_state = True

    while game_state == True:
        game_over = False
        user_cards = []
        computer_cards = []
        score_user = 0
        score_computer = 0
        for card in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
        score_user = calculate_score(user_cards)
        score_computer = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, "
              f"current score: {score_user}\n"
              f"Computer's first card: {computer_cards[0]}")

        while game_over == False:
            more_card = input("Type 'y' to get another card, "
                              "type 'n' to pass.\n")
            if more_card == 'y':
                user_cards.append(deal_card())
                score_user = calculate_score(user_cards)

                computer_cards.append(deal_card())
                score_computer = calculate_score(computer_cards)

                print(f"Your cards: {user_cards}, "
                      f"current score: {score_user}\n"
                      f"Computer's first card: {computer_cards[0]}\n")
                game_over = False

                if score_user > 21:
                    print(f"Your final hand: {user_cards}, "
                          f"final score: {score_user}\n"
                          f"Computer's final hand: {computer_cards} "
                          f"Computer's final score: {score_computer}\n")
                    if score_user > 21:
                        print("You lose.\n")
                    elif score_computer == 0:
                        print("You lose.\n")
                    elif score_user > score_computer or score_user == 0:
                        print("You win!\n")
                    else:
                        print("You lose\n")
                    game_over = True

            elif more_card == 'n':
                print(f"Your final hand: {user_cards}, "
                      f"final score: {score_user}\n"
                      f"Computer's final hand: {computer_cards} "
                      f"Computer's final score: {score_computer}\n")
                if score_user > score_computer or score_user == 0:
                    print("You win!\n")
                else:
                    print("You lose\n")
                game_over = True


        game_continue = input("Do you want to play "
                                  "another game of blackjack?"
                                  " 'y' or 'n' ?\n")
        if game_continue == 'n':
            game_state = False
        elif game_continue == 'y':
            game_state = True

black_jack()




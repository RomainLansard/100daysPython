# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
price = {}
game_state = True
print(art.logo)

while game_state == True:
    name = input("What is your name?: ").lower()
    bids = int(input("What is your bid: $"))
    price[name] = bids
    game_continue = input("Are there any other bidders? " 
                          "type 'yes' or 'no'\n").lower()
    if game_continue == 'no':
        game_state = False
    elif game_continue == 'yes':
        game_state = True
        print("\n"*100)

price[name] = bids

highest_bid = 0
winner = ""

for bid in price:
    if price[name] > highest_bid:
        highest_bid = price[bid]
        winner = bid
print(f"The winner is {winner.title()}"
    f"with a bid of {bids} !")




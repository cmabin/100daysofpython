import os 
def clear_console() :
    os.system('cls')

from auction_art import logo
print(logo)

auction = {}

def find_highest_bidder(bid_record)    :
    # bid_record = {"Cee-Jay": 123, "Robin": 321}
    highest_bid = 0
    winner = ""
    for bidder in bid_record :
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while True   :
    name = input("What is your name?: ")
    offer = int(input("What's your bid? $"))
    auction[name] = offer
    if input("Are there other bidders? Type 'Y' or 'N': ").lower() == "y"   :
        clear_console()
    else   :
        False
        clear_console()
        find_highest_bidder(auction)
        break

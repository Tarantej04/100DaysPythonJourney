import art
print(art.logo)

bids = {}
continue_game = True

def high_bid(bidding_record):
    bid_high = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_high < bid_amount:
            bid_high = bid_amount
            winner = bidder
    print(f"The winner of the bid is {winner} with a bid of ${bid_high}.")

while(continue_game):
    name = input("What is your name ? : ")
    amount = int(input("What is your bid ? : $"))
    bids[name] = amount
    players_avail = input("Are there more bidders ? - type 'yes' or 'no':\n").lower()
    if players_avail == "no":
        continue_game = False
        high_bid(bids)
    elif players_avail == "yes":
        print("\n" * 30)
    else:
        print("Enter the correct choice. Begin again")
        quit
    
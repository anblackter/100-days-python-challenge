from replit import clear
#HINT: You can call clear() to clear the output in the console.

other_bidders = True

while other_bidders:
    bidders = {}
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == 'yes':
        clear()
    else:
        other_bidders = False
        highest_bid = 0
        winner = ""
        for bidder in bidders:
            if bidders[bidder] > highest_bid:
                highest_bid = bidders[bidder]
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")

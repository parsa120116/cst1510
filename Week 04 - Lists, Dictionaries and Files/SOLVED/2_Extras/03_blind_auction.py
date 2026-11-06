bids = {}

more_bidders = True
while more_bidders:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bids[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if answer == "no":
        more_bidders = False

highest_bid = 0
winner = ""
for bidder, amount in bids.items():
    if amount > highest_bid:
        highest_bid = amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid:.2f}")

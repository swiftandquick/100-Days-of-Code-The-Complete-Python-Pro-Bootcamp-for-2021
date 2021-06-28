# from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

# Create an empty dictionary.
bidders = {}

# Initially, there is at least one bidder, so new_bidder is initially set to true.
new_bidder = True

# Highest bidder is not found yet and bidding starts off as $0.
highest_bidder = ""
highest_bidding = 0

while new_bidder:
    name = input("What is your name?:  ")
    bid = int(input("What's your bid?:  $"))

    bidders[name] = bid
    # If the bidder bids higher than current highest bidder, they will become the new highest_bidder.
    if bidders[name] > highest_bidding:
        highest_bidder = name
        highest_bidding = bidders[name]

    new_bidder = input("Are there any other bidders?  Type 'yes' or 'no'.  ").lower()

    # Ends the loop if there's no new bidder.
    if new_bidder != "yes":
        new_bidder = False


print(f"The winner is {highest_bidder} with a bid of ${highest_bidding}.  ")

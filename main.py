from replit import clear
from art import logo

print(logo)
print("Welcome to Greed Island auction!")

bids = {}

def bid_winner(bidding_records):
  highest_bid = 0
  winner = ""
  for bidder in bidding_records:
    bid_amount = bidding_records[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the bid amount of {highest_bid}.")

bidding_finished = False
while not bidding_finished:
  name = input("Type your name here: ")
  price = int(input("Type your bid price: $"))
  bids[name] = price
  should_continue = input("Are there any bidders? Type 'yes' or 'no'.\n")
  if should_continue == "yes":
    clear()
  elif should_continue == "no":
    bidding_finished = True
    bid_winner(bids)
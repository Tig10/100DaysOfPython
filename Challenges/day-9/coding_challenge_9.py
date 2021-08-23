import os
from art import logo


print(logo)
print('Welcome to the Blind Auction!!\n')

bids = {}


def bid_entry(bidder_name, bid_amount):
    bids[name] = amount


def highest_bidder(all_bids):
    highest_bid = 0
    highest_bid_owner = ''
    for key, value in bids.items():
        if value > highest_bid:
            highest_bid = value
            highest_bid_owner = key
    print(f'The highest bidder is {highest_bid_owner} at ${highest_bid}')


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'): # If machine is running Windows, use cls
        command = 'cls'
    os.system(command)


bidding = True
while bidding:
    name = input('What is your name?: ')
    amount = int(input('What is your bid?: $'))
    bid_entry(name, amount)
    more_bids = input('Any more bidders?: yes or no: ')
    if more_bids == 'no':
        bidding = False
    else:
        clear()

highest_bidder(bids)


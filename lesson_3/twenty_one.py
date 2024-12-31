import random

SUITS = ['H', 'D', 'C', 'S']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] 

# Initializes entire deck
def initialize_deck(): 
	deck = [[suit, value] for suit in SUITS
						  for value in VALUES]
	return deck

def shuffle(deck):
	random.shuffle(deck)


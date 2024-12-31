import random

SUITS = ['H', 'D', 'C', 'S']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] 

"""
High-level pseudocode:
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.
"""

# Initializes entire deck
def initialize_deck(): 
	deck = [[suit, value] for suit in SUITS
						  for value in VALUES]
	return deck

def shuffle(deck):
	random.shuffle(deck)

def deal_card(current_deck):
	if deck:
		return current_deck.pop()

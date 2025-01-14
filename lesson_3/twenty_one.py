import random

SUITS = ['H', 'D', 'C', 'S']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] 

PLAYER = 'player'
DEALER = 'dealer'

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

def prompt(message):
	print(f'==> {message}')

# Initializes entire deck
def initialize_deck(): 
	new_deck = [[suit, value] for suit in SUITS
						  for value in VALUES]
	return new_deck

def shuffle(full_deck):
	random.shuffle(full_deck)

def deal_card(current_deck):
	if current_deck:
		return current_deck.pop()


# def player_turn()

def play_twenty_one():
    prompt("Let's play a game of Twenty-One!")
        
    deck = initialize_deck()
    shuffle(deck)
    
    player_hand = []
    dealer_hand = []

play_twenty_one()

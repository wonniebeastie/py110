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


def initialize_deck(): 
	"""Creates a card deck that will be used throughout the game.

	Returns:
		list: A nested list representing a deck of cards. 
  		      Example: [['H', '3'], ['S', 'Q'], ... ]
	"""
	new_deck = [[suit, value] for suit in SUITS
						  for value in VALUES]
	return new_deck

def shuffle(deck):
	random.shuffle(deck)

def deal_card(deck):
	if deck:
		return deck.pop()

def deal_two_cards(deck):
	"""Deals two cards to each player.
	
	Returns:
		list: A hand composed of 2 returning cards from `deal_card` function.
	"""
	return [deal_card(deck), deal_card(deck)]

# def player_turn()

def play_twenty_one():
    prompt("Let's play a game of Twenty-One!")
        
    deck = initialize_deck()
    shuffle(deck)
    
    player_hand = deal_two_cards(deck)
    dealer_hand = deal_two_cards(deck) 
    
    print(player_hand)
    print(dealer_hand)    

play_twenty_one()

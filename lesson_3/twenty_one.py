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

def replace_face_cards(lst_of_card_values):
	face_card_names = {
		'A': 'Ace',
		'J': 'Jack',
		'Q': 'Queen',
		'K': 'King',
	}

	for i in range(len(lst_of_card_values)):
		if lst_of_card_values[i] in face_card_names:
			# Using the value in arg list as the key for face_card_names
			lst_of_card_values[i] = face_card_names[lst_of_card_values[i]]
	
	return lst_of_card_values

def display_hand(hand):
    """
	PROBLEM
	Display the card in human-readable form.

	I: A player's "hand" (nested lst)
	O: "...[card value], [card value] and [card_value]"

	ALGO (-, +, -, +)
	[x] - SET "delimiter" to ', '
	[x] - Extract just the values of the cards in the hand. 
 		 i.e. (['1', 'J', 'K'...])
		 Capture in "values"
	[NOTE: Extract step to another function - to change letters to long form]
	[] - IF the length of "values" is less than 3:
		 + display them joined together with 'and'
	   - ELSE join them together with "delimiter" (except for the last element)
		 (Capture in "joined_first_part")
	[] - Combine the "joined_first_part" string with 'and' & the last element
		 (Capture in "final_string")
	[] - Return "final_string"
	"""
    delimiter = ', '
    values = [card[1] for card in cards]

def deal_card(deck):
	if deck:
		return deck.pop()

def deal_two_cards(deck):
	"""Deals two cards to each player.
	
	Returns:
		list: A hand composed of 2 returning cards from `deal_card` function.
	"""
	return [deal_card(deck), deal_card(deck)]

def player_turn(initial_player_hand):
	"""
	Rename `initial_player_hand` to `current_hand`
	- Display `current_hand` & "Your hand: ... Total points: [#]."

	- WHILE True:
		- Ask (`input()`) player to hit or stay (capture in `answer`)
		- IF `answer` is `'hit'`:
			- call: `deal_card(deck)` to deal player a new card.
			- display new card.
			- update `current_hand` to include new card. 
			- capture `total(current_hand)` in `player_total`
			- display: "Dealer has: [ex: 7 and unknown card]"
			- display:  "You have: [ex: Jack, 10 and 6] | Total points: [`player_total`]. 
			- check if busted - call: `busted(player_points)`
				- if True, END LOOP.
		- ELSE IF : `answer` is `'stay'`: END LOOP 
		- ELSE: display "invalid input. Please enter 'hit' or 'stay'"
	- IF `busted(current_hand)` is truthy:
		- print "You busted! Dealer wins!"
		- call  `ask_play_again()`
	- ELSE:
		- print "You chose to stay." (`prompt()`)
		- return `player_total`
	"""
    current_hand = initial_player_hand
    
    

def play_twenty_one():
    prompt("Let's play a game of Twenty-One!")
        
    deck = initialize_deck()
    shuffle(deck)
    
    player_hand = deal_two_cards(deck)
    dealer_hand = deal_two_cards(deck) 
    
    player_turn(player_hand)

play_twenty_one()

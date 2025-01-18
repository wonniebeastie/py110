import random
import os

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

def generate_just_card_values(hand):
    cards = hand
    lst_of_card_values = [card[1] for card in cards] 
    return lst_of_card_values

def replace_face_cards(lst_of_card_values):
    """Replaces face card abbreviations to full names for displaying to player.

    Args:
        lst_of_card_values (lst): A list of just the values of cards in a hand.

    Returns:
        lst: A new list with the abrreviations replaced with their long names.
    """
    face_card_names = {
        'A': 'Ace',
        'J': 'Jack',
        'Q': 'Queen',
        'K': 'King',
    }
    # NOTE TO SELF: Add the value of the key-value pair using the card value
    # as the key ('A') to the new list - if it cannot be found, then just add
    # the card value.
    return [face_card_names.get(card_value, card_value)
            for card_value in lst_of_card_values]

def display_card(drawn_card):
    """
    PROBLEM
    Find a way to display the suit & value in human readable form.

    I: the drawn/dealt card (`lst`)
    O: "[value] of [suit]" i.e. -> "10 of Diamonds" (`str`)

    DS:
    - 

    ALGO (-, +, -, +)
    [] - 
    [] - 
    [] - 

    """

def display_hand(hand, hide_second_card=False):
    """Formats a hand of cards into a human-readable string.

    Args:
        hand (list): A list of cards where each card is represented as a list
                     (e.g., [['H', 'A'], ['D', 'J'], ['C', '10']]).

    Returns:
        str: A string representation of the hand, with face card values 
             replaced by their full names and proper grammar (e.g., "Ace, Jack 
             and 10").
    """
    delimiter = ', '
    # Extracting just the values of the cards in hand.
    card_values = generate_just_card_values(hand)

    if hide_second_card:
        return f'{card_values[0]} and unknown card'
    elif len(card_values) < 3:
        return f'{card_values[0]} and {card_values[1]}'
    else:
        first_str = delimiter.join(card_value 
                                   for card_value in card_values[:-1])
        final_str = f'{first_str} and {card_values[-1]}'
        return final_str

def total(hand):
    """Calculates the total value of a hand of cards, with Aces dynamically 
    valued as 1 or 11 to avoid exceeding 21.

    Args:
        cards (list): A list of cards, where each card is represented as 
                      a list or tuple (e.g., [['H', 'A'], ['D', 'J'], ['C', 
                      '10']]).

    Returns:
        int: The total value of the hand.

    NOTE:
        - Number cards (2–10) are worth their face values.
        - Face cards (J, Q, K) are worth 10.
        - Aces are worth 1 but may be upgraded to 11 if it doesn't cause a 
          bust.
    """
    card_values = generate_just_card_values(hand)

    sum_val = 0
    for card_value in card_values:
        if card_value == "A":
            sum_val += 1
        elif card_value in ['J', 'Q', 'K']:
            sum_val += 10
        else:
            sum_val += int(card_value)
    
    aces = card_values.count("A")
    for _ in range(aces):
        if sum_val + 10 <= 21: # Upgrade an ace to 11 if it won't cause a bust.
            sum_val += 10
    
    return sum_val

def player_turn(initial_player_hand, initial_dealer_hand, deck):
    """Player's turn to play. 
    Player must decide to draw a card & risk busting or choose to stay.
    """

    """
    [x] - Rename `initial_player_hand` to `current_hand`
    [x] - Display "Dealer has: [card value] and unknown card."
    [x] - Display `current_hand` & "Your hand: ... Total points: [#]."

    [] - WHILE True:
        [x] - Ask (`input()`) player to hit or stay (capture in `answer`)
        [] - IF `answer` is `'hit'`:
              - call: `deal_card(deck)` to deal player a new card (capture in
                `new_card`).
              - display the new card - "You drew: [value] of [suit]" -
                call `display_card(new_card)`.
              - update `current_hand` to include `new_card`. 
              - capture `total(current_hand)` in `player_total`
              - display: "Dealer has: [ex: 7 and unknown card]"
              - display:  "You have: [ex: Jack, 10 and 6] | 
                Total points: [`player_total`]."
              - check if busted - call: `busted(player_points)`
                  - if True, END LOOP.
        - ELSE IF : `answer` is `'stay'`: END LOOP 
        - ELSE: display "invalid input. Please enter 'hit' or 'stay'"
    [] - IF `busted(current_hand)` is truthy:
        - print "You busted! Dealer wins!"
        - call  `ask_play_again()`
    [] - ELSE:
        - print "You chose to stay." (`prompt()`)
        - return `player_total`
    """
    current_hand = initial_player_hand
    prompt(f"Dealer has: {display_hand(initial_dealer_hand, True)}")
    prompt(f"You have: {display_hand(current_hand)} | Total Points: {total(current_hand)}")

    while True:
        answer = input("Hit or Stay? Enter 'h' for Hit & 's' for Stay. ").strip().lower()
        if answer == 'h':
            new_card = deal_card(deck)
            prompt(f"You drew: {new_card}")

def play_twenty_one():
    prompt("Let's play a game of Twenty-One!")
    
    terminal_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80

    deck = initialize_deck()
    shuffle(deck)

    print(''.center(terminal_width, '-'))
    print("PLAYER TURN".center(terminal_width))
    print(''.center(terminal_width, '-'))
    
    player_hand = deal_two_cards(deck)
    dealer_hand = deal_two_cards(deck)
    
    humbug = player_turn(player_hand, dealer_hand, deck)
    print(humbug)

play_twenty_one()

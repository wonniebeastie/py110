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

def replace_suit_name(suit_abbreviation):
    match suit_abbreviation:
        case 'H':
            return 'Hearts'
        case 'D':
            return 'Diamonds'
        case 'C':
            return 'Clubs'
        case 'S':
            return 'Spades'

def display_card(drawn_card):
    value_abbr = replace_face_cards(drawn_card[1])
    value = value_abbr[0]

    suit_abbr = drawn_card[0]
    suit = replace_suit_name(suit_abbr)

    return f'{value} of {suit}'

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
    # Extracting just the values of the cards in hand.\
    card_values = generate_just_card_values(hand)
    # Replacing the face card abbreviations with their long names.
    card_values = replace_face_cards(card_values)

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

def busted(hand):
    if total(hand) > 21:
        return True
    else:
        return False

def ask_play_again():
    while True:
        answer = input("==> Play again? Enter 'y' for yes, 'n' for no. \n").strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            prompt("Invalid input, please type 'y' or 'n'.")


def player_turn(initial_player_hand, initial_dealer_hand, deck):
    terminal_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 60
    current_hand = initial_player_hand

    print(f"Dealer has: {display_hand(initial_dealer_hand, True)}")
    print(f"You have: {display_hand(current_hand)} | Total Points: {total(current_hand)}")
    print(''.center(terminal_width, '-'))

    while True:
        answer = input("==> Hit or Stay? Enter 'h' for Hit & 's' for Stay. \n").strip().lower()
        if answer == 'h':
            new_card = deal_card(deck)
            new_card_for_display = display_card(new_card)

            prompt(f"You drew: {new_card_for_display}")
            print(''.center(terminal_width, '-'))

            current_hand.append(new_card)
            print(f"Dealer has: {display_hand(initial_dealer_hand, True)}")
            print(f"You have: {display_hand(current_hand)} | Total Points: {total(current_hand)}")
            print(''.center(terminal_width, '-'))

            if busted(current_hand):
                break
        
        elif answer == 's':
            break
        
        else:
            prompt("Invalid input. Please enter 'h' or 's'.")
    
    if busted(current_hand):
        return total(current_hand), True
    else:
        return total(current_hand), False

def play_twenty_one():
    while True:
        prompt("Let's play a game of Twenty-One!")
        prompt("Whoever gets the highest points without going over 21 wins the game!")
        terminal_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 60

        # Initialize & shuffle deck.
        deck = initialize_deck()
        shuffle(deck)

        # Deal initial cards to the player & dealer.
        player_hand = deal_two_cards(deck)
        dealer_hand = deal_two_cards(deck)

        # Player's turn
        print(''.center(terminal_width, '-'))
        print("PLAYER TURN".center(terminal_width))
        print(''.center(terminal_width, '-'))
        player_total, player_busted = player_turn(player_hand, dealer_hand, deck)
        
        if player_busted:
            prompt(f"You busted with a total of {player_total} points. Dealer wins!")
            if ask_play_again():
                continue
            else:
                prompt("Thanks for playing Twenty-One, see you next time!")
                break
        else:
            prompt(f"You chose to stay with a total of {player_total} points.")
            break

play_twenty_one()

import random
import os

SUITS = ['H', 'D', 'C', 'S']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

FACE_CARD_NAMES = {
    'A': 'Ace',
    'J': 'Jack',
    'Q': 'Queen',
    'K': 'King',
}


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
    """Removes and returns the top card from the deck.

    Args:
        deck (list): The deck of cards.

    Returns:
        list: The top card of the deck as a list [suit, value].

    Raises:
        ValueError: If the deck is empty.
    """
    if not deck:
        raise ValueError("Cannot deal from an empty deck.")
    return deck.pop()

def deal_two_cards(deck):
    return [deal_card(deck), deal_card(deck)]

def generate_just_card_values(hand):
    """Extracts and returns the values of cards in a given hand.

    Args:
        hand (list): A list of cards, where each card is represented as [suit, 
        value].

    Returns:
        list: A list of card values from the given hand.
    """
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
    """Converts a suit abbreviation ('H', 'D', 'C', 'S') to its full name.

    Args:
        suit_abbreviation (str): The suit abbreviation.

    Returns:
        str: The full name of the suit (e.g., 'Hearts', 'Diamonds').
    """
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
    """Formats a single card into a human-readable string.

    Args:
        drawn_card (list): A card represented as a list [suit, value],
                           e.g., ['H', 'A'].

    Returns:
        str: A string representation of the card, with the suit and value
             converted to full names (e.g., "Ace of Hearts").
    """
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
    # Extracting just the values of the cards in hand.
    card_values = generate_just_card_values(hand)
    # Replacing the face card abbreviations with their long names.
    card_values = replace_face_cards(card_values)

    if hide_second_card:
        return f'{card_values[0]} and unknown card'

    if len(card_values) < 3:
        return f'{card_values[0]} and {card_values[1]}'

    first_str = delimiter.join(card_value
                                for card_value in card_values[:-1])
    final_str = f'{first_str} and {card_values[-1]}'
    return final_str

def total(hand):
    """Calculates the total value of a hand of cards, with Aces dynamically 
    valued as 1 or 11 to avoid exceeding 21.

    Args:
        cards (list): A list of cards, where each card is represented as 
                      a list (e.g., [['H', 'A'], ['D', 'J'], ['C', '10']]).

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
    """Determines if a given hand exceeds 21 points.

    Args:
        hand (list): A list of cards, where each card is represented as [suit, 
        value].

    Returns:
        bool: True if the hand's total exceeds 21, False otherwise.
    """
    return total(hand) > 21

def ask_play_again():
    while True:
        answer = input("==> Play again? Enter 'y' for yes, 'n' for no. \n").strip().lower()

        if answer == 'y':
            return True

        if answer == 'n':
            return False

        prompt("Invalid input, please type 'y' or 'n'.")


def player_turn(initial_player_hand, initial_dealer_hand, deck):
    """Handles the player's turn, allowing them to hit or stay.

    Args:
        initial_player_hand (list): The player's starting hand.
        initial_dealer_hand (list): The dealer's starting hand for display.
        deck (list): The current deck of cards.

    Returns:
        tuple: (total_points, busted_status)
               - total_points (int): The player's final total points.
               - busted_status (bool): True if the player busted, False 
                 otherwise.
    """
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

    return total(current_hand), False

def dealer_turn(initial_dealer_hand, deck):
    """Handles the dealer's turn, drawing cards until the total reaches at 
    least 17 or the dealer busts.

    Args:
        initial_dealer_hand (list): The dealer's starting hand.
        deck (list): The current deck of cards.

    Returns:
        tuple: (total_points, busted_status)
               - total_points (int): The dealer's final total points.
               - busted_status (bool): True if the dealer busted, False 
                 otherwise.
    """
    terminal_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 60
    current_hand = initial_dealer_hand

    while total(current_hand) < 17:
        new_card = deal_card(deck)
        new_card_for_display = display_card(new_card)

        prompt(f"Dealer drew: {new_card_for_display}")
        current_hand.append(new_card)

        print(f"Dealer has: {display_hand(current_hand)} | Total Points: {total(current_hand)}")
        print(''.center(terminal_width, '-'))

        if busted(current_hand):
            break

    if busted(current_hand):
        return total(current_hand), True

    return total(current_hand), False

def determine_winner(player_hand_total, dealer_hand_total):
    if player_hand_total > dealer_hand_total:
        return 'player'

    if player_hand_total < dealer_hand_total:
        return 'dealer'

    return 'tie'

def announce_winner(player_hand_total, dealer_hand_total):
    victor = determine_winner(player_hand_total, dealer_hand_total)
    if victor == 'player':
        prompt(
            f"And the winner is... You! Congratulations, you won the game "
            f"with {player_hand_total} points!"
        )
    elif victor == 'dealer':
        prompt(
            f"And the winner is... The dealer! The dealer won the game with "
            f"{dealer_hand_total} points. Better luck next time!"
        )
    else:
        prompt(f"It's a tie! Both you and the dealer had {player_hand_total} points.")

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

            prompt("Thanks for playing Twenty-One, see you next time!")
            break

        prompt(f"You chose to stay with a total of {player_total} points.")

        # Dealer's turn
        print(''.center(terminal_width, '-'))
        print("DEALER TURN".center(terminal_width))
        print(''.center(terminal_width, '-'))
        dealer_total, dealer_busted = dealer_turn(dealer_hand, deck)

        if dealer_busted:
            prompt(f"Dealer busted with a total of {dealer_total} points. You win!")
            if ask_play_again():
                continue

            prompt("Thanks for playing Twenty-One, see you next time!")
            break

        prompt(f"Dealer chose to stay with a total of {dealer_total} points.")

        # Determine & announce who won if both stayed.
        prompt("Both you and the dealer chose to stay.")
        announce_winner(player_total, dealer_total)

        # Ask if player wants to play again.
        if ask_play_again():
            continue

        break

play_twenty_one()
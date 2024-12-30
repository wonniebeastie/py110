import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_SCORE = 5
WINNING_LINES = [
	[1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
	[1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
	[1, 5, 9], [3, 5, 7]              # diagonals
]

PLAYER = 'player'
COMPUTER = 'computer'
CHOOSE = 'choose'


def prompt(message):
	print(f'==> {message}')

def join_or(num_list, delimiter=', ', join_word='or'):
	"""
	Format a list of numbers into a human-readable string with custom 
	delimiters.

    Parameters:
    + num_list (list): A list of numbers to format.
    + delimiter (str): A string used to separate elements in the list 
	  (default: ', ').
    + join_word (str): A word to use before the last element (default: 'or').

    Returns:
    str: 
        - An empty string if the input list is empty.
        - The first element as a string if the input list has one element.
        - Two elements joined by the join_word if the input list has two 
		  elements.
        - Elements separated by the delimiter, with the join_word before the 
		  last element for lists with three or more elements.
	"""
	match len(num_list):
		case 0:
			return ''
		case 1:
			return str(num_list[0])
		case 2:
			return f'{num_list[0]} {join_word} {num_list[1]}'
	
	joined_first_part = delimiter.join([str(num) for num 
										in num_list[:-1]])
	final_string = f'{joined_first_part}{delimiter}{join_word} {num_list[-1]}'
	return final_string

def display_board(board):
	"""
    Display the current state of the Tic-Tac-Toe board.
	
	Parameters:
    + board (dict): A dictionary representing the game board where keys
                    are square numbers (1-9) and values are markers.
    """
	prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")

	print('')
	print('     |     |')
	print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
	print('     |     |')
	print('-----+-----+-----')
	print('     |     |')
	print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
	print('     |     |')
	print('-----+-----+-----')
	print('     |     |')
	print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
	print('     |     |')
	print('')

def initialize_board():
	"""
    Create a new empty Tic-Tac-Toe board.

    Returns:
    dict: A dictionary where keys are square numbers (1-9) and values
          are the initial marker (space).
    """
	return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
	"""
    Get a list of unoccupied squares on the board.

    Parameters:
    board (dict): A dictionary representing the game board.

    Returns:
    list: A list of square numbers (keys) that are still unoccupied.
    """
	return [key 
			for key, value in board.items() 
			if value == INITIAL_MARKER]

def player_chooses_square(board):
	"""
    Allow the player to choose a square on the board.

    Parameters:
    board (dict): A dictionary representing the game board.
    """
	while True:
		valid_choices = [str(num) for num in empty_squares(board)]
		# input trimmed to allow spaces in input
		prompt(f"Choose a square: {join_or(valid_choices)}")
		square = input().strip()
		
		if square in valid_choices:
			break

		prompt("Sorry, that's not a valid choice.")

	board[int(square)] = HUMAN_MARKER

# Function changed to allow for both defense & offense.
# Now the computer will only pick a random square if there are no two
# Xs or Os in the winning line sublist.
def find_at_risk_square(line, board, marker):
	markers_in_line = [board[square] for square in line]
	
	if markers_in_line.count(marker) == 2:
		for square in line:
			if board[square] == ' ':
				return square
	return None

def computer_chooses_square(board):
	"""
    Allow the computer to choose a square on the board.

    Parameters:
    board (dict): A dictionary representing the game board.
    """
	square = None

	# Offense first
	for line in WINNING_LINES:
		square = find_at_risk_square(line, board, COMPUTER_MARKER)
		if square:
			break
	
	# Defense
	if not square:
		for line in WINNING_LINES:
			square = find_at_risk_square(line, board, HUMAN_MARKER)
			if square:
				break
	
	# Pick square 5 if available
	if not square and board[5] == INITIAL_MARKER:
		square = 5
	
	# Pick a random square if no immediate threat nor win
	if not square:
		square = random.choice(empty_squares(board))
	
	board[square] = COMPUTER_MARKER

def board_full(board):
	"""
    Check if the board is full (no empty squares remain).

    Parameters:
    board (dict): A dictionary representing the game board.

    Returns:
    bool: True if no empty squares remain, False otherwise.
    """
	return len(empty_squares(board)) == 0

def someone_won(board):
	"""
    Check if either player has won the game.

    Parameters:
    board (dict): A dictionary representing the game board.

    Returns:
    bool: True if either player has won, False otherwise.
    """
	return bool(detect_winner(board))

def detect_winner(board):
	"""
    Determine the winner of the game, if any.

    Parameters:
    board (dict): A dictionary representing the game board.

    Returns:
    str: 'Player' if the player wins, 'Computer' if the computer wins,
          or None if there is no winner.
    """
	for line in WINNING_LINES:
		sq1, sq2, sq3 = line
		if (board[sq1] == HUMAN_MARKER
			   and board[sq2] == HUMAN_MARKER
			   and board[sq3] == HUMAN_MARKER):
			return 'Player'
		elif (board[sq1] == COMPUTER_MARKER
				  and board[sq2] == COMPUTER_MARKER
				  and board[sq3] == COMPUTER_MARKER):
			return 'Computer'

	return None

def increment_scores(score_dictionary, winner):
	"""
    Update the scores based on the winner of the round.

    Parameters:
    score_dictionary (dict): A dictionary containing current scores for
                              the 'Player' and 'Computer'.
    winner (str): The winner of the round ('Player' or 'Computer').
    """
	if winner == 'Player':
		score_dictionary['Player'] += 1
	elif winner == 'Computer':
		score_dictionary['Computer'] += 1

def display_scores(score_board):
	"""
    Display the current scores for the player and computer.

    Parameters:
    score_board (dict): A dictionary containing the scores for 'Player' and
                   'Computer'.
	"""
	player_score = score_board['Player']
	computer_score = score_board['Computer']
	print(f" < Player: {player_score} | Computer: {computer_score} >")

def choose_square(game_board, player):
	"""
	PROBLEM
	Function that will call `computer_chooses_square` or `player_chooses_square`
	depending on the value of `current_player`.

	INPUT & OUTPUT
	I: the game board,
	I: current player
	O: 

	RULES (EXPLICIT/IMPLICIT)
	EXP:
	- 

	IMP:
	- 


	EXAMPLES / TEST CASES
	- 


	ALGO (-, +, -, +)
	[] - 
	[] - 
	[] - 

	"""



def play_round(player):
	"""
	Play a single round of Tic-Tac-Toe.

    Returns:
    str: 'Player' if the player wins, 'Computer' if the computer wins,
         or None if the round ends in a tie.
	"""

	board = initialize_board()

	while True:
		display_board(board)
		choose_square(board, current_player)
		current_player = alternate_player(current_player)
		
		if someone_won(board) or board_full(board):
			break

	# while True:
	# 	if player == PLAYER: # Player goes first
	# 		display_board(board)
	# 		player_chooses_square(board)
	# 		if someone_won(board) or board_full(board):
	# 			break
	# 		computer_chooses_square(board)
	# 		if someone_won(board) or board_full(board):
	# 			break

	# 	else: # Computer goes first
	# 		computer_chooses_square(board)
	# 		display_board(board)
	# 		if someone_won(board) or board_full(board):
	# 			break
	# 		player_chooses_square(board)
	# 		if someone_won(board) or board_full(board):
	# 			break

	display_board(board)

	if someone_won(board):
		winner = detect_winner(board)
		prompt(f"{winner} wins this round.")
		return winner

	prompt("It's a tie!")
	return None

def play_match(starting_option):
	while True:
		scores = { 'Player': 0, 'Computer': 0 }

		prompt("Let's play a match of Tic-Tac-Toe!")
		prompt("The first player to win 5 games wins the overall match!")

		if starting_option == CHOOSE:
			valid_choices = {'p': PLAYER, 'c': COMPUTER}
			while True:
				player_input = input("==> Pick who will make the first move: Enter 'p' Player or 'c' for Computer \n").lower()
				if player_input in valid_choices:
					player =  valid_choices[player_input]
					break
				print("Invalid choice. Please try again.")
		else:
			player = starting_option
			input("Press Enter to start...")
		# Pause before entering a round, which clears the terminal.
		os.system('clear')

		round = 1

		while (scores['Player'] < WINNING_SCORE and scores['Computer'] < WINNING_SCORE): 
			terminal_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80

			print(''.center(terminal_width, '-'))
			print(f'ROUND {round}'.center(terminal_width))
			print(''.center(terminal_width, '-'))

			display_scores(scores)

			if player == PLAYER:
				winner = play_round(PLAYER)
			else:
				winner = play_round(COMPUTER)

			if winner:
				increment_scores(scores, winner)
			
			display_scores(scores)
			
			round += 1

			if scores['Player'] < WINNING_SCORE and scores['Computer'] < WINNING_SCORE:
				input(f"Press Enter to continue onto round {round}...")
				os.system('clear')
		
		if scores['Player'] == WINNING_SCORE:
			prompt("You win the overall match!")
		else:
			prompt("Computer wins the overall match!")
		
		while True:
			# Ask user if they want to play again.
			prompt("Play another match? (y or n)")
			valid_responses = ['y', 'n']
			answer = input().strip().lower()

			if answer not in valid_responses:
				print("Invalid response. Please enter 'y' or 'n'.")
			else:
				break
		
		if answer == 'n':
			prompt('Thanks for playing Tic Tac Toe!')
			break

play_match(CHOOSE)
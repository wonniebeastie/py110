import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_SCORE = 5

def prompt(message):
	print(f'==> {message}')

"""
PROBLEM 
Improved "join".

INPUT & OUTPUT
I: a list (empty or integers)
I (Optional): a string (delimiter of choice)
I (Optional): a string (a word before last digit)

O: a string that represents the final string


QUESTIONS
Q:


RULES (EXPLICIT/IMPLICIT) / SEQ
EXP:
- Lets you specify different delimiters & different words for last item.

IMP:
- Empty list as an input produces an empty string as output.
- The delimiters & different words are optional.
	- Default is a comma followed by a space & 'or' for the join word.
- Just two integers on the list does not display a comma, just 'or'.


EXAMPLES / TEST CASES
print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"


ALGO [PROGRAMMATIC]
[x] 1. If "input list" is empty, return an empty string.
	   [NOTE] Function should have default values of:
			  - ', ' ("delimiter")
			  - 'or' ("join word")
[x] 2. If "input list" only has one value, return that value as a string
[x] 3. If "input list" has exactly two values, return those values 
	  separated by "join word"; don't use "delimiter".
[x] 4. If "input list" has 3 or more values, return the concatenation of
	  all the values as follows:
		4A) "For each number in 'input list', join each with 'delimiter' 
		  until the last number; Join the last number with the 'join 
		  word' to the rest of the numbers.
			- [TODO] Two lists for each? Try slicing syntax.
				a) from index 0 to index before the last - "first part"
					a.1. Join each num of "first part" with 'delimiter'
				b) last index - "second part"
				c) Join "first part" & "second part" with "join word"
				   as "final string".
		4B) Return "final string".

"""

def join_or(num_list, delimiter=', ', join_word='or'):
	'''
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

	'''
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
	os.system('clear')
	
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

def computer_chooses_square(board):
	"""
    Allow the computer to choose a square on the board.

    Parameters:
    board (dict): A dictionary representing the game board.
    """
	if len(empty_squares(board)) == 0:
		return
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
	winning_lines = [
		[1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
		[1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
		[1, 5, 9], [3, 5, 7]              # diagonals
	]

	for line in winning_lines:
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

"""
PROBLEM
Keep track of how many times the player & computer each win, and report
scores after each game. First player to win 5 games wins the overall
match (a series of 2 or more games). The score should reset to `0` for 
each player when beginning a new match. Don't use any global variables. 
However, you may want to use a global constant to represent the number 
of games needed to win the match.


INPUT & OUTPUT
I: play_tic_tac_toe()
O: "You win the overall match!" (if player wins)
O: "Computer wins the overall match!" (if computer wins)


RULES (EXPLICIT/IMPLICIT)
EXP:
- Keep track of "player score" 
- Keep track of "computer score"
- Each time player or computer wins, increment their score by 1.
- Keep looping tic tac toe game until either the player or the computer
  score is 5.
- A "match" is "a series of 2 or more games".
- The score should reset to `0` when beginning a new "match". 
- Use a global constant to represent the # of games needed to win the
  match.
- A "match" ends if either the player or computer has a total score of
  5. 
  [NOTE] Ask to play again when beginning a new "match".

IMP:
- Do not increment either score if result of a game is a tie.


EXAMPLES / TEST CASES
- input: 


**[TODO] Make global constant "WINNING_SCORE" = 5


`play_match` ALGO
[x] + Create outer loop:
	[NOTE] Break Condition: If player doesn't say "yes" to playing 
	again.
    [x] ++ Create "scores":
	   [TODO] Use a dictionary
	   - Make "player score" == 0
	   - Make "computer score" == 0

    [x] ++ "Let's play a match of Tic Tac Toe! The first player to win 5
	    games wins the overall match!"

	[x] ++ CREATE INNER LOOP: 
		[NOTE] Break Condition: Either the player or the computer has a 
		score of 5. 
			++ Call `play_round`, assign returning value to "winner".
			++ Call `increment_scores` with "scores" & "winner" as 
			   arguments. (This should update the dictionary.)

[] + "Play another match?"
	++ If yes:
	  +++ reset "player score" & "computer score" to 0
	  +++ restart from step 1.
	++ Otherwise,
	  +++ "Thanks for playing Tic Tac Toe!"
"""

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

def display_scores(scores):
	"""
	I: a dictionary, "scores" from main function
	O: a string, "Player: {player_score} | Computer: {computer_score}"

	ALGO
	[] + "player score" is "scores['Player']"
	[] + "computer score" is "scores['Computer']
	[] + Print "Player: {player_score} | Computer: {computer_score}"

    Display the current scores for the player and computer.

    Parameters:
    scores (dict): A dictionary containing the scores for 'Player' and
                   'Computer'.
	"""
	player_score = scores['Player']
	computer_score = scores['Computer']
	print(f"Player: {player_score} | Computer: {computer_score}")

def play_round():
	"""
	I: 
	O: `'Player'` or `'Computer'` or `None`

	ALGO
	[TODO] 
	[] + Create loop:
		++ Initalize empty board.
		  +++ Create inner loop: 
			 ++++ Display current state of board (`display_board`)
			 ++++ Player chooses a square (`player_chooses_square`)
			 ++++ If `someone_won` or `board_full` - break out of loop.
			 ++++ Computer chooses a square (`computer_chooses_square`)
			 ++++ If `someone_won` or `board_full` - break out of loop.
		++ Display board.
		++ If "someone won": 
		  +++ "'detect winner' wins this round."
		  +++ Call `increment_scores` with "detect winner".
		  +++ Return "detect_winner"
		++ Else, "It's a tie, try again."

	"""
	"""
	Play a single round of Tic-Tac-Toe.

    Returns:
    str: 'Player' if the player wins, 'Computer' if the computer wins,
         or None if the round ends in a tie.
	"""
	board = initialize_board()

	while True:
		display_board(board)

		player_chooses_square(board)
		if someone_won(board) or board_full(board):
			break

		computer_chooses_square(board)
		if someone_won(board) or board_full(board):
			break
	
	display_board(board)
	
	if someone_won(board):
		winner = detect_winner(board)
		prompt(f"{winner} wins this round.")
		return winner
	prompt("It's a tie!")
	return None

def play_match():
	"""
    Play a single round of Tic-Tac-Toe.

    Returns:
    str: 'Player' if the player wins, 'Computer' if the computer wins,
          or None if the round ends in a tie.
    """
	while True:
		scores = { 'Player': 0, 'Computer': 0 }

		prompt(
            "Let's play a match of Tic-Tac-Toe! "
            "The first player to win 5 games wins the overall match!"
        )
		
		while (scores['Player'] < WINNING_SCORE and scores['Computer'] < WINNING_SCORE): 
			winner = play_round()

			if winner:
				increment_scores(scores, winner)
				display_scores(scores)
		
		if scores['Player'] == WINNING_SCORE:
			prompt("You win the overall match!")
		else:
			prompt("Computer wins the overall match!")
		
		# Ask user if they want to play again.
		prompt("Play another match? (y or n)")
		answer = input().strip().lower()

		if answer[0] != 'y':
			break

	prompt('Thanks for playing Tic Tac Toe!')

play_match()
import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def prompt(message):
    print(f'==> {message}')

"""
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
[] 4. If "input list" has 3 or more values, return the concatenation of
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
	match len(num_list):
		case 0:
			return ''
		case 1:
			return str(num_list[0])
		case 2:
			return f'{num_list[0]} {join_word} {num_list[1]}'
	
	first_part = num_list[:-1]
	second_part = num_list[-1:]
	
	joined_first_part = delimiter.join([str(num) for num 
										in first_part])
	last_element = str(second_part[0])
	final_string = f'{joined_first_part}{delimiter}{join_word} {last_element}'
	return final_string

def display_board(board):
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
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    # create a list of only the valid choices
    return [key 
        	for key, value in board.items() 
            if value == INITIAL_MARKER]

def player_chooses_square(board):
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
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def board_full(board):
	'''
	`==` was used to return a truthy value, since `[]` is a falsy value
	and we need this function to return a truthy value in order for
	our loop to work correctly.
	'''
	return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
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

def play_tic_tac_toe():
    while True:
        '''
		Board intialized in outer loop bc each game needs a separate
		board.
		'''
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
            prompt(f"{detect_winner(board)} won!")
        else:
            prompt("It's a tie!")
		
		# Ask user if they want to play again.
        prompt("Play again? (y or n)")
        answer = input().lower()

        if answer[0] != 'y':
            break

    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()
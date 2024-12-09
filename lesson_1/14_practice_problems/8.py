"""
INPUT & OUTPUT
I: a string
O: dictionary that shows the count of occurrence for each character in
input string.

QUESTIONS
- 

RULES (EXPLICIT/IMPLICIT) / SEQ
EXP:
- The pairs can be outputted in a different order.
- Frequency count is case-sensitive.

IMP:
- Whitespaces do not count as a character.
- Uppercase chars are separate from lowercase chars of the same letter


EXAMPLES / TEST CASES
- "The Flintstones Rock" =>
{
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}


ALGO [HI-LVL]
1. Split the string into a list of characters (no repeats).
2. Loop through the string and count each time a character occurs.
3. Return it as pairs of character-number of occurences.

ALGO [PROGRAMMATIC]
[x] 1. Split "input string" into a list of unique characters. 
	[TODO] 
	- Use set constructor (for unique members)
	- Rename it to "letters".
[x] 2. Create "letter count pairs" dictionary of paired values of "letters"-0.
	[TODO] Try a dictionary comprehension?
[x] 3. Loop through "input string" and increment the value of each
"letter" every time the value occurs in the string. 
	[TODO]
	- Use a `for` loop.
	- Use "letter" as key to target the value.
[x] 4. Return "letter count pairs" dictionary.

"""

def character_counter(text):
	# Remove repeat letters
	letters = set(list(text))
	# To get a dictionary without whitespaces
	letter_count_pairs = {letter: 0 for letter in letters if letter != ' '}
	
	for letter in text:
		if letter in letter_count_pairs.keys():
			letter_count_pairs[letter] += 1
	
	return letter_count_pairs

statement = "The Flintstones Rock"

print(character_counter(statement))
# {'t': 2, 'i': 1, 'R': 1, 'T': 1, 'e': 2, 's': 2, 'n': 2, 'k': 1, 
# 'l': 1, 'o': 2, 'c': 1, 'F': 1, 'h': 1}
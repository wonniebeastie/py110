"""
INPUT & OUTPUT
I: No argument 
O: a string that contains a UUID


QUESTIONS 


RULES (EXPLICIT/IMPLICIT) / SEQ
EXP:
- Each UUID consists of 32 hexadecimal characters represented as a 
string.
	- each character: digits `0`-`9` & letters `a`-`f`
- Each UUID is typically broken into 5 sections in an 8-4-4-4-12
pattern

IMP:
- 


EXAMPLES
- input: (no input)
=> output: 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'


DS / VIS
- strings
	- f-strings for returning string

VIS:

BRAINSTORM
- How to generate mix of numbers and letters that are 8-chars, 4 chars,
and so on for f-string?
- Maybe try having separate so-and-so characters long strings and put
each to use: i.e. 8 char string generator, 4 char string generator (to
be reused 3 times), then 12 char string generator
- Or create a helper function that takes an integer as an argument that
will be the whatever length of a string we need.
- 


ALGO [HI-LVL]
1. Create something that will return a mix of hexademical characters
for however long of a string we need.
2. Put together a string in 8-4-4-4-12 pattern.
3. Return said string.

ALGO [PROGRAMMATIC]
[] 1. Create "return hex string" function that will return a string of 
any given length from the 32 hexadecimal characters.
	[NOTE] Use random.choice module to achieve this.
			- a string with numbers 0-9 & letters a-f in it.
	[NOTE: SUBSTEPS]
			1A) Use list comprehension to create a list of chars that
			will be x number of characters long.
			1B) Combine this list into a string.
			1C) Return said string.
[] 2. Return string of 8-4-4-4-12 pattern created from step 1.

"""
import random 

def return_hex_string(length):
	valid_chars = '0123456789abcdef'
	hex_list = [ random.choice(valid_chars) for _ in range(length) ]
	return ''.join(hex_list)

print(return_hex_string(8))
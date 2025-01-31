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


ALGO [HI-LVL]
1. Create something that will return a mix of hexademical characters
for however long of a string we need.
2. Put together a string in 8-4-4-4-12 pattern.
3. Return said string.

ALGO [PROGRAMMATIC]
[x] 1. Create "return hex string" function that will return a string of 
any given length from the 32 hexadecimal characters.
	[NOTE] Use random.choice module to achieve this.
			- a string with numbers 0-9 & letters a-f in it.
	[NOTE: SUBSTEPS]
			1A) Use list comprehension to create a list of chars that
			will be x number of characters long.
			1B) Combine this list into a string.
			1C) Return said string.
[x] 2. Return string of 8-4-4-4-12 pattern created from step 1.

"""
import random 

def return_hex_string(length):
	hex_chars = '0123456789abcdef'
	hex_list = [ random.choice(hex_chars) for _ in range(length) ]
	return ''.join(hex_list)

print((
		f'{return_hex_string(8)}-'
		f'{return_hex_string(4)}-' 
		f'{return_hex_string(4)}-'
		f'{return_hex_string(4)}-' 
		f'{return_hex_string(12)}'
		))

'''
This code imports the `random` module to implement the `random.choice`
function to create a list of random hexadecimal characters to a 
specified length and return it joined into a string. 

Then f-strings are used to return a string that represents a UUID by
calling the function to the desired length for each section of the 
UUID.
'''

# SOLUTION
import random

def generate_uuid():
    hex_chars = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)

# Outputs shown below are samples - you output will vary
print(generate_uuid())  # '02e51c2f-dacd-c319-53b5-e40e6e8c1f78'
print(generate_uuid())  # '39038ab9-3b95-43d8-6959-5d785ccb9b69'
print(generate_uuid())  # 'f7d56480-c5b2-8d4d-465f-01a4ea605729'

'''
It seems that the solution is of a function that also makes use of a
string of hexadecimal character & a list comprehension;

But instead of using f-strings, a list is created that holds the 
integer values of the lengths of the strings for each section of the
UUID that is used for the `for` loop as a way to generate the a list
that holds strings of the correct length.

And each of those strings are joined by `-` and appended to the
initially empty `uuid` variable.

Then all you need to do is call the function without any arguments to
generate UUID strings.

'''
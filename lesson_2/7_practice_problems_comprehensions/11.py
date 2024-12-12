"""
INPUT & OUTPUT
I: a dictionary with nested lists of strings
O: a list of every vowel that appears in the strings of the nested
lists

QUESTIONS
Q. Can vowels be repeated in the output list? 
	A. Yes, according to the example, it's literally every single one.


RULES (EXPLICIT/IMPLICIT)
EXP:
- Start by writing this using nested loops.
- Extra challenge: after a working nested loop, try to refactor the
code so that it uses a single list comprension.

IMP:
- Repeats do not matter, just include whatever is a vowel.


EXAMPLES / TEST CASES
- input: 
{
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}
=> output: ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

ALGO 
[x] 1. Create an empty "final list" list.
[x] 2. Create a "string of vowels" (aeiou).
[x] 3. Use a loop to target the values of the "input dictionary" (by
using the key);
[] 4. Use a nested loop to target each element (strings) of the nested 
lists:
	[TODO: SUBSTEPS]
	4A) If any of the strings include the characters from "string of
	vowels" then add the char to "final list".
[] 5. Return "final list"

"""

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

def list_of_vowels(dictionary):
	all_vowels = []
	vowels = 'aeiou'

	for list_of_strings in dictionary.values():
		for string in list_of_strings:
			print(string)

print(list_of_vowels(dict1))
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
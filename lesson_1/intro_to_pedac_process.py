'''
P - Understand the Problem

3 Steps:
1. Read the problem description.
2. Check the test cases, if any.
3. If any part of the problem is unclear, ask the interviewer or problem
requester to clarify the matter.

Input, output.
Explicit requirements, Implicit requirements.
'''

"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection should be case-sensitive.
"""

# Test cases:

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

'''
My own workthrough of "understand the problem":

INPUT/OUTPUT
I: a string
O: a list of 0 or more strings

RULES
Explicit
- Return all palindromic substrings of given string;
- Substrings should be 2 or more characters long.
- Palindrome detection should be case-sensitive.

Implicit
- Returning strings must be in a list.
- If no paliandrome substrings, return empty list.
- If input string is emoty, return empty list.
- Multiple palindromes can be detected from the same given string (overlaps allowed).
'''

"""
LS Solution:
Some questions you might have?
1. What is a substring?
2. What is a palindrome?
3. Will inputs always be strings?
4. What does it mean to treat palindrome words case-sensitively?

input: string
output: a list of substrings
rules:
- Explicit requirements:
    - Return only substrings which are palindromes.
    - Palindrome words should be case sensitive; "abBA" is not a
	palindrome.

- Implicit requirements:
    - If the string is an empty string, the result should be an
	empty list.
"""

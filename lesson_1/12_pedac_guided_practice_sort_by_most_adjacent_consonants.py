"""
P: INPUT & OUTPUT, RULES (EXP/IMP), QUESTIONS, MENTAL MODEL

INPUT & OUTPUT
I: a list (of strings)
O: a list (of strings sorted according to the highest number of adjacent
consonants)

QUESTIONS
- What are "consonants"? (English is my second language)
	-> They're all the letters besides the vowels 
		-> vowels are a, e, i, o, u, y (only if no vowel in word)
(LS's
- Do strings always contain multiple words?
	-> [No.]
	- Can strings contain a single word?
		-> [Yes]
	- Can strings be empty?
		-> [Not answered by test cases, ask interviewer. But for this
			exercise, we'll go with "No".]
- Is it possible for a string to contain no adjacent consonants?
	-> [Yes]
- What is meant by "a space between two consonants in adjacent words"?
	-> [The space between doesn't matter.]
- Should the strings be sorted in ascending or descending order?
	-> [Descending (highest adjacent consonant strings appear first)]
- Is case important?
	-> [Not answered by the test cases, ask interviewer for clarification.])


RULES (EXPLICIT/IMPLICIT) / SEQ
EXP:
- List must be sorted from highest to lowest number of adjacent
consonants & returned.
	- Consonants are adjacent if:
		- they're next to each other in the same
		word, or
		- if there is a space between 2 consonants in adjacent words.
	- If two strings have the same highest # of adjacent consonants,
	they should be ordered the same way they original were.

(LS'S EXP:
- If two strings contain the same highest number of adjacent
consonants, they should maintain their original relative order.
- Adjacent consonants:
    - are next to each other in the same string.
    - can have a space between them in adjacent
    words. ???)

LS's IMP:
- Strings may contain more than one words (hinted by "adjacent words")

UPDATED IMP:
- Strings may contain single or multiple words.
- Strings may not be empty.
- Strings may have no adjacent consonants.
- Strings should be sorted in descending order.
- Case is not relevant.
- Single consonants in a string do not affect sort order in comparison
to strings with no consonants. Only adjacent consonants affect sort order.


EXAMPLES / TEST CASES
- ['aa', 'baa', 'ccaa', 'dddaa'] -> ['dddaa', 'ccaa', 'aa', 'baa']
- ['can can', 'toucan', 'batman', 'salt pan'] -> ['salt pan', 'can can', 'batman', 'toucan']
	- 'salt pan`: 3
	- 'can can': 2
	- 'batman': 2
	- 'toucan': 0
- ['bar', 'car', 'far', 'jar'] -> ['bar', 'car', 'far', 'jar']
- ['day', 'week', 'month', 'year'] -> ['month', 'day', 'week', 'year']
- ['xxxa', 'xxxx', 'xxxb'] -> ['xxxx', 'xxxb', 'xxxa']

Note: Yes, they do confirm what I thought about the rules:
- What consonants are,
- Space between them not mattering,
- Maintaining the same order if same # of consonants.
(See QUESTIONS section)


DS / VIS
- Lists
- MIGHT need an intermediate structure, like a dictionary to track the
number of adjacent consonants in each word, like:

VIS:
{
    'aa': 0,
    'baa': 0,
    'ccaa': 2,
    'dddaa': 3,
    'rstafgdjecc': 4,
}

ALGO (High-level)
1. Count how many number of adjacent consonants there are for each word.
[EXTRACTED]

2. Repeat step 1 with each word in the list.

3. Sort the list by highest number of adjacent consonants, in descending order.

4. Return the list.

----------- STEP 1 EXTRACTED -----------
	Input: a string
	Output: an integer representing a count of the highest number of
			adjacent consonants in the string

	1. Determine whether the first letter is a consonant or a vowel ('a', 'e', 
	'i', 'o', 'u') for each word.

	2. If it's a consonant, check if the letter that comes after it is also
	a consonant. 

	3. If it is, count it as 1; If not, go on to the next letter.

	4. Repeat until the last letter in the word.
-------------------------------------------

(LS's ALGO [High-level]
[x] 1. For each string in the input list, determine the highest number
    of adjacent consonants within that string. [EXTRACTED]
    
[] 2. Sort the input list based on the calculated highest number of
    consonants from step 1.
	[NOTE] Ensure correct order of arguments in the callback to `sort` to
	produce a descending order.

[] 3. Return the sorted list.


------------ STEP 1 EXTRACTED -------------
	Problem: Count consonants 

	Input: a string
	Output: an integer representing a count of the highest number of
			adjacent consonants in the string

	Test Cases:
	print(count_max_adjacent_consonants('dddaa'))       # 3
	print(count_max_adjacent_consonants('ccaa'))        # 2
	print(count_max_adjacent_consonants('baa'))         # 0
	print(count_max_adjacent_consonants('aa'))          # 0
	print(count_max_adjacent_consonants('rstafgdjecc')) # 4


	COUNT CONSONANTS ALGO 
	1. Remove the spaces from the "input string". 
	[TODO] Try using `string.split` combined with `string.join` to remove the
	spaces from the input string.

	2. Initialize a "maximum consonants count" to zero.

	3. Initialize an "adjacent consonants string" to an empty string.

	4. For each "letter" in the "input string":
	[TODO] Perhaps use a `for` loop to iterate through the string?
	[TODO] Use the `in` keyword to check whether a string of consonants
	includes the letter for that iteration.

		4A. If the "letter" is a consonant:
			a) Concatenate it to the "adjacent consonants string".
		4B. If the "letter" is a vowel:
			a) If the "adjacent consonants string" has a length
			greater than the current "maximum consonants count":
				a.1) If the "adjacent consonants string" has a length
				greater than 1:
					a.1.1) Set the "maximum consonants count" to the length 
					of the "adjacent consonants string".
			
			b) Reset the "adjacent consonants string" to an empty string.

	5. Return the "maximum consonants count".
-----------------------------
)
"""

"""
MAIN ALGO
[x] 1. For each string in the input list, determine the highest number
    of adjacent consonants within that string. [EXTRACTED]
    
[] 2. Sort the input list based on the calculated highest number of
    consonants from step 1.
	[NOTE] Ensure correct order of arguments in the callback to `sort` to
	produce a descending order.

[] 3. Return the sorted list.
"""

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings

def count_max_adjacent_consonants(word):
    word = ''.join(word.split(' '))
    max_consonant_count = 0
    adjacent_consonants = ''

    for letter in word:
        if letter not in 'aeiou':
            adjacent_consonants += letter
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)
        else:
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_consonants) > 1:
                    max_consonant_count = len(adjacent_consonants)
            adjacent_consonants = ''
        
        # print(f"adjacent_consonants: '{adjacent_consonants}', "
        #         f"max_consonant_count: {max_consonant_count}")
    return max_consonant_count

# count_max_adjacent_consonants('month')

# print(count_max_adjacent_consonants('dddaa'))       # 3
# print(count_max_adjacent_consonants('ccaa'))        # 2
# print(count_max_adjacent_consonants('baa'))         # 0
# print(count_max_adjacent_consonants('aa'))          # 0
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
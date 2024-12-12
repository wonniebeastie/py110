"""
PROBLEM
Write code that returns a list that contains only the dictionaries
where all the numbers are even.

Keep data structure the same as the given.

INPUT & OUTPUT
I: a list with nested dictionaries that has nested lists containing
integers
O: a list with the dictionaries from the input list where all the 
numbers are even


RULES (EXPLICIT/IMPLICIT)
EXP:
- 

IMP:
- Don't include the other dictionaries if any of their lists have odd
numbers in them.


EXAMPLES / TEST CASES
- input: [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
=> output[{e: [8], f: [6, 10]}]

ALGO 
[] 1. Create "all nums even" function that will return True if all the 
numbers in the "sub_list" given to it are all even, False otherwise.
[] 2. Create "all even" function that will return True - if calling
"all nums even" function returns True - if EVERY "sub_list"s in
the "dictionary" given to it contain only even numbers, False 
otherwise.
[] 3. Create "result" list that selects for only the dictionaries that
do not contain odd numbers.
[] 4. Print the "result" list.

"""
# LS's solution with the first function's name changed
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def all_nums_even(lst):
    return all([num % 2 == 0 for num in lst])

def all_even(dictionary):
    lists_are_even = [all_nums_even(list_value)
                    	for list_value in dictionary.values()]
    return all(lists_are_even)

result = [dictionary for dictionary in lst
                    	if all_even(dictionary)]

print(result) # [{'e': [8], 'f': [6, 10]}]
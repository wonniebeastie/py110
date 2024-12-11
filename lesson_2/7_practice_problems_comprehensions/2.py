"""
PROBLEM
Given the following data structure, return a new list with the same 
structure, but with the values in each sublist ordered in ascending 
order. Use a comprehension if you can. (Try using a `for` loop first.)

The string values should be sorted as strings, while the numeric values
should be sorted as numbers.

INPUT & OUTPUT
I: a list with nested lists inside
O: a new list with nested lists inside, but each sublist in ascending
order

RULES 
- string values must be sorted as strings
- numeric values must be sorted as numbers
- returned list must be a different object from the original list.


EXAMPLES / TEST CASES
>Input: [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
Output: [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]


ALGO (high-level)
[] 1. Target each sublist in given list, sort them in ascending order.
[] 2. Return it as a new list. 
[NOTE]: Use the `sorted()` function since it's non-mutating.

"""
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Regular `for` loop
sorted_sublists = []

for sublist in lst:
	sorted_list = sorted(sublist)
	sorted_sublists.append(sorted_list)

print(sorted_sublists) 
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
print(lst is sorted_sublists) # False


# Using comprehension
sorted_sublists = [sorted(sublist) for sublist in lst]

print(sorted_sublists)
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
print(lst is sorted_sublists) # False

# NOTE: The `sorted` function knows how to differentiate between strings
# and numbers by itself.

'''
=============================================================
If the `sort` list method is used with the list comprehension:
'''
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

sorted_sublists = [sublist.sort() for sublist in lst]
'''
NOTE: Using the `sort` method here still mutates the original `lst`
because that is what it is called on, even though we are creating a
new list with the list comprehension.
'''

print(sorted_sublists) # [None, None, None]
print(lst is sorted_sublists) # False
'''
NOTE: The `sort` list method mutates the list it is called on, and
returns the default return value, `None`. That is what is added to 
the new list, `sorted_sublists`.
'''
print(lst) # [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
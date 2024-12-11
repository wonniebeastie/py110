"""
INPUT & OUTPUT
I: a list with nested lists
O: a new list but values in each sublist in ascending order *as strings*

EXAMPLES / TEST CASES
Input: [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
Output: [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

"""

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Using a `for` loop.
sorted_lst = []

for sublist in lst:
	sorted_sublst = sorted(sublist, key=str)
	sorted_lst.append(sorted_sublst)

print(sorted_lst)
# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]


# Using a list comprehension.
sorted_lst = [sorted(sublist, key=str) for sublist in lst]

print(sorted_lst)
[['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]
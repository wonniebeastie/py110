"""
INPUT & OUTPUT
I: a list with nested dictionaries
O: a new list identical in structure to input list, but with each
number incremented by `1`.
"""

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def increment_ints(dictionary):
	incremented_dict = { key: value + 1 for key, value in dictionary.items() }
	return incremented_dict

new_lst = [increment_ints(sub_dict) for sub_dict in lst]

print(new_lst)
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
print(lst)
# {'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# COMBINED SOLUTION
new_list = [{key: value + 1 for key, value in dictionary.items()}
                            for dictionary in lst]

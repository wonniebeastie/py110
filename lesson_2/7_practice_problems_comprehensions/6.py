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



# SECOND PASS
"""
I: a list with nested dictionaries
O: a new list with nested dictionaries, with numbers incremented by 1

✱ EXAMPLES ✱
- Ex 1
- I: [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
- O: [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

✱ QUESTIONS ✱
- Can the nested dictionaries be new objects or do they have to be mutated og
  objects?

✱ SUB-PROBLEMS ✱
- og list must be unmutated 
    - create new list (order of elements stays the same)

- find a way to increment all numbers by 1
    - helper function job: take a dictionary, iterate through it, add 1 to each
     value, return dictionary


✱ A - ALGORITHM ✱
(-, +, -, +)
I: subdict
[] - define function "increment_by_1"
    [] + create a dictionary with dict comprehension
	    - from: subdict
	    - filter for: n/a
	    - do what: +1 to each value
    [] + return dictionary

I: lst_of_dict_nums
[] - make a new empty list "new_list"
[] - for each element of lst_of_dict_nums,
    [] - call increment_by_1() - "new_dict"
    [] - append new_dict to new_list
[] - return new_list
or
[] + create a list
    - from: lst_of_dict_nums
    - filter for: n/a
    - do what: call increment_by_1
[] + return list 

"""
def increment_by_1(subdict):
    return {letter: num + 1 for letter, num in subdict.items()}

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_list = [increment_by_1(subdict) for subdict in lst]

print(new_list)
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

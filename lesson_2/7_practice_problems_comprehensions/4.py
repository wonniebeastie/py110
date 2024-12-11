"""
I: a list with sublists
O: a dictionary in which key == first item in each sublist, 
value == second

Expected result:
Pretty printed for clarity
{
    'a': 1,
    'b': 'two',
    'sea': {c: 3},
    'D': ['a', 'b', 'c']
}
"""

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

cool_dictionary = {key: value for key, value in lst}

print(cool_dictionary)
# {'a': 1, 'b': 'two', 'sea': {'c': 3}, 'D': ['a', 'b', 'c']}


# SOLUTION
dict1 = {item[0]: item[1] for item in lst}

print(dict1)
# {'a': 1, 'b': 'two', 'sea': {'c': 3}, 'D': ['a', 'b', 'c']}
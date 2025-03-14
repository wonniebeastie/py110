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


# SECOND PASS
"""
✱ P - PROBLEM ✱
I: a nested list
O: a dictionary (key = first item in each sublist, value = second item)
"""
def create_dict(nested_list):
    new_dict = {}

    for sublist in nested_list:
        key, value = sublist
        new_dict[key] = value

    return new_dict

def create_dict2(nested_list):
    return {key: value for key, value in nested_list}

def create_dict3(nested_list):
    return dict([*sublist] for sublist in nested_list)


lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

print(create_dict(lst))
# {'a': 1, 'b': 'two', 'sea': {'c': 3}, 'D': ['a', 'b', 'c']}
print(create_dict2(lst))
# {'a': 1, 'b': 'two', 'sea': {'c': 3}, 'D': ['a', 'b', 'c']}
print(create_dict3(lst))
# {'a': 1, 'b': 'two', 'sea': {'c': 3}, 'D': ['a', 'b', 'c']}

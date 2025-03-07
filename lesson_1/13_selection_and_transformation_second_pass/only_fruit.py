produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(produce_list):
    only_fruit = {}

    for produce_name, produce_type in produce_list.items():
        if produce_type == 'Fruit':
            only_fruit[produce_name] = produce_type
    
    return only_fruit


print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

# The `items()` dicitonary method returns a dictionary view object, which is
# an iterable containing the key-value pairs of the dictionary passed to the 
# `produce` function as an argument.

# And from that view object, if the value (`produce_type`) was equal in value
# to the string `'Fruit'`, then it is added, along with its key 
# (`produce_name`), to the dictionary via direct key assignment.

# Finally, the resulting dictionary is returned.

# Solution 2
def select_fruit2(produce_list):
    only_fruit = { 
        produce_name: produce_type 
        for produce_name, produce_type
        in produce_list.items()
        if produce_type == 'Fruit'
    }

    return only_fruit

print(select_fruit2(produce)) # {'apple': 'Fruit', 'pear': 'Fruit'}

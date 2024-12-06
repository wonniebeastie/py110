"""
Problem: 
Create a function that selects only the key-value pairs where the value
is 'Fruit'.

I: dictionary
O: dictionary with key-value pairs where the value is 'Fruit'

Algo
1. Create "new dictionary".
2. Iterate through "input dictionary", selecting the keys whose values
are 'Fruit'. 
3. If the value is 'Fruit', add key-value pair to "new dictionary".
4. Repeat until the end of "input dictionary".
5. Return "new dictionary".
"""

# This problem demonstrates selection only.

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_only_fruit(dictionary):
    new_dict = {}

    for key, value in dictionary.items():
        if dictionary[key] == 'Fruit':
            new_dict[key] = value

    return new_dict

print(select_only_fruit(produce))


# Solution
def select_fruit(produce_list):
    selected_fruits = {}

    for current_key, current_value in produce_list.items():
        if current_value == 'Fruit':
            selected_fruits[current_key] = current_value

    return selected_fruits

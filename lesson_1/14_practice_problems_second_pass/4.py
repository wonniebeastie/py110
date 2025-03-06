# Given the following code, what would the output be? 
# Try to answer without running the code.

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}

for index, name in enumerate(names):
    name_positions[name] = index

print(name_positions)

# I believe the output will be:
# {'Fred': 0, 'Barney': 1, 'Wilma': 2, 'Betty': 3, 'Pebbles': 4, 'Bambam': 5}

# The `for` loop on line 7 is used with tuple unpacking & the `enumerate` 
# function to "unpack" the values returned by the function to populate the
# empty dictionary initialized on line 5 (`name_positions`).

# The `enumerate` function is useful for keeping track of both the element and
# its position in the given sequence. In this code, the values assigned to 
# `name` is used as the key and the value assigned to `index` is used as its
# value to be added to the `name_positions` dictionary.


# AFTER LSBot's Feedback:

# I believe the output will be:
# {'Fred': 0, 'Barney': 1, 'Wilma': 2, 'Betty': 3, 'Pebbles': 4, 'Bambam': 5}

# The `for` loop on line 7 is used with tuple unpacking and the `enumerate` 
# function to "unpack" the values returned by the function to populate the
# empty dictionary initialized on line 5 (`name_positions`).

# The `enumerate` function yields pairs of (index, element) for each element in
# the `names` list. It starts the index count at 0 by default, which is why
# `'Fred'` gets assigned index 0, `'Barney'` to index 1, and so on.

# In each iteration of the `for` loop, the values assigned to `name` is 
# used as the key and the values assigned to `index` is used as its value to 
# form key-value pairs - these pairs are added to the `name_positions`
# dictionary via direct key assignment. 


# Condensed version by LSBot:

# I believe the output will be:
# {'Fred': 0, 'Barney': 1, 'Wilma': 2, 'Betty': 3, 'Pebbles': 4, 'Bambam': 5}

# Line 3 initializes an empty dictionary `name_positions`.
# The `for` loop on line 5 uses `enumerate()` with tuple unpacking to iterate 
# through the `names` list. For each iteration, `index` is assigned the position
# (starting at 0) and `name` is assigned the element at that position.
# Line 6 adds each name as a key in the dictionary with its index as the value.

# Finally, line 8 prints the resulting dictionary.

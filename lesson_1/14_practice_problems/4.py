# Given the following code, what would the output be? Try to answer 
# without running the code.

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}

for index, name in enumerate(names):
    name_positions[name] = index

print(name_positions)

# Output:
# Pretty printed for clarity
# {
#     'Fred': 0,
#     'Barney': 1,
#     'Wilma': 2,
#     'Betty': 3,
#     'Pebbles': 4,
#     'Bambam': 5
# }

""""
I think it will print `{"Fred": 0, "Barney": 1, "Wilma": 2 ... } and so
on. 

The `name_positions` variable on line 5 is initialized with an empty 
dictionary.

Then on line 7, the `for` loop temporarily assigns `index` & `name` to
the returning value of the `enumerate` function with `names` passed as
the argument.

The `enumerate` function takes an iterable object as an argument and 
returns an enumerate object, which can be directly used for loops. The
enumerate object is a tuple that contains pairs of the index number & 
the value that index number refers to.

Inside the `for` loop, the dictionary `name_positions` is assigned to is
updated with the value of the pair, `name`, used as the key and the index
number, `index`, as the value for that key. This is repeated for each pair
returned by the `enumerate` function.
"""

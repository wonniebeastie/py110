# Calculate the total age given the following dictionary:
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

print(sum(ages.values())) # 6174

# On line 11, the `values` method returns a dictionary view object, which 
# displays all the values in the dictionary it was called on. Dictionary view
# objects provide a window to the current state of the dictionary.

# This view object is then used by the `sum` function to add the values up, 
# returning `6174`, which is then printed to the console. 

# AFTER LSBOT FEEDBACK:

# One line 11, the `values()` method returns a dictionary view object, which is
# an iterable containing all the values from the `ages` dictionary. Dictionary
# view objects provide a dynamic view of the dictionary's values that would 
# reflect any changes made to the original dictionary.abs

# The `sum()` function then iterates through this view object, adding up all
# the numeric values, which results in `6174`. This result is then printed to
# the console.

# Determine the minimum age from the above ages dictionary.
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

print(min(ages.values())) # 10

# The `values()` dictionary method on line 11 returns a dictionary view object,
# which is an iterable containing all the values of the `ages` dictionary.
# Dictionary view objects provide a dynamic view of the current state of the
# dictionary, meaning it will reflect any changes made to it in real time.

# The `min()` function then iterates through this view object, looking for the
# smallest value it can find, then returns it. This value, which is `10` in
# this code, is then printed to the console.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# How would you obtain a set that contains all the unique values from both sets?

print(a.union(b)) # {1, 2, 3, 4, 5, 6}
print(a | b) # {1, 2, 3, 4, 5, 6}

# You can use the `union` set method or the union operator `|` to return a 
# set that combines all unique elements from both sets.

# How would you obtain a set that contains all the unique values from
# both sets?
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b)) # {1, 2, 3, 4, 5, 6}
print(a | b)      # {1, 2, 3, 4, 5, 6}
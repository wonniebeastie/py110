# Sort in ascending numeric order, then descending order. Do not mutate
# the list.
lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst))               # [-16, -6, 7, 8, 9, 10, 11, 50]
print(sorted(lst, reverse=True)) # [50, 11, 10, 9, 8, 7, -6, -16]

print(lst) # [10, 9, -6, 11, 7, -16, 50, 8]

# SECOND PASS
lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst))
print(sorted(lst, reverse=True))

# The `sorted` function takes an iterable and sorts it in ascending order by
# default, returning it as a list. It is non-mutating and can be used with 
# any iterable.

# You can use the optional `reverse` parameter to sort the list in descending
# order. The default is `False`. 

# Repeat exercise 1, but mutate the list.
lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort()
print(lst) # [-16, -6, 7, 8, 9, 10, 11, 50]

lst.sort(reverse=True)
print(lst) # [50, 11, 10, 9, 8, 7, -6, -16]


# SECOND PASS
lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

# The `sort` list method is a method that sorts the list it was called
# on in ascending order by default. It mutates the list in place so it doesn't
# return a useful return value. Which is why you must print the list it was
# called on using the `print` function instead of printing its return value
# directly.

# You can use the optional `reverse` parameter to sort the list in descending
# order by settings its value to `True`. 

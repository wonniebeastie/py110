# Repeat Problem 2 but sort the list as string values.
# Both lists (passed to the function & returned) should contain numbers,
# not strings.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort(key=str)
print(lst) # [-16, -6, 10, 11, 50, 7, 8, 9]

lst.sort(key=str, reverse=True)
print(lst) # [9, 8, 7, 50, 11, 10, -6, -16]


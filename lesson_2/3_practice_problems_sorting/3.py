# Repeat Problem 2 but sort the list as string values.
# Both lists (passed to the function & returned) should contain numbers,
# not strings.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort(key=str)
print(lst) # [-16, -6, 10, 11, 50, 7, 8, 9]

lst.sort(key=str, reverse=True)
print(lst) # [9, 8, 7, 50, 11, 10, -6, -16]


# SECOND PASS
lst = [10, 9, -6, 11, 7, -16, 50, 8]

def sort_as_strings(numbers, order='ascending'):
    if order == 'ascending':
        numbers.sort(key=str)
        return numbers
    else:
        numbers.sort(key=str, reverse=True)
        return numbers

print(sort_as_strings(lst)) # [-16, -6, 10, 11, 50, 7, 8, 9]
print(sort_as_strings(lst, 'descending')) # [9, 8, 7, 50, 11, 10, -6, -16]




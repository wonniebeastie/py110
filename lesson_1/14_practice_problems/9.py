# What is the return value of the list comprehension below? Try to 
# answer without running the code.
[num for num in [1, 2, 3] if num > 1]

"""
I believe this will output:
```
[2, 3]
```
This is a list comprehension that uses `[1, 2, 3]` as the source to 
create a new list, using only selection.

It selects for the elements in the source list if they are greater than
1.
"""

yo = [num for num in [1, 2, 3] if num > 1]
print(yo) # [2, 3]
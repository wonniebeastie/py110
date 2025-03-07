"""
PROBLEM
Create a function that doubles each element of a list and returns it, with
mutation.

INPUT & OUTPUT
I: a list
O: the same input list, numbers doubled

RULES (EXPLICIT/IMPLICIT) / SEQ
EXP:
- each element must be doubled
- returned list must be the same list (mutated)

ALGO [HI-LVL]
- For each number in input-list, multiply it by two
    - reassign it in that index position
- Return the input-list
"""

def double_numbers(numbers):
    for num in range(len(numbers)):
        numbers[num] *= 2

    return numbers

my_numbers = [1, 4, 3, 7, 2, 6]

print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers) # [2, 8, 6, 14, 4, 12]

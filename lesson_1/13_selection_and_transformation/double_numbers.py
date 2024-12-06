"""
PROBLEM
Create a function that doubles the integers of a list that mutates the
function argument.

INPUT & OUTPUT
I: a list of integers
O: the same list object but with the integers doubled

ALGO 
[x] 1. Loop through the list of integers and multiply each integer by
    [TODO] Use a `for` loop.
[x] 2. Return the list.
"""

# This problem demonstrates transformation only.

'''
This function works by mutating the elements at each index of the list
passed as the argument.
'''
def double_numbers(numbers):
    for current_num in range(len(numbers)):
        numbers[current_num] *= 2

    return numbers


my_numbers = [1, 4, 3, 7, 2, 6]

print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers) # [2, 8, 6, 14, 4, 12]
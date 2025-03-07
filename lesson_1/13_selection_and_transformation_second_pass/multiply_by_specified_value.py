"""
PROBLEM
Create a function that lets you multiply every list element by a specified
value. Don't mutate the list.

INPUT & OUTPUT
I: a list of numbers
I: an integer, the multiplier
O: a new list, with all elements from input list multipled by multiplier

ALGO [HI-LVL]
- initialize empty list "transformed_nums"
- for each number in input list:
    - multiply number by "multiplier"
    - add multiplied number to "transformed nums" list
- return "transformed nums" list
"""
# Solution 1: Using traditional loop
def multiply(numbers, multiplier):
    transformed_nums = []

    for num in numbers:
        transformed_nums.append(num * multiplier)

    return transformed_nums

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]

# Solution 2: Using a list comprehension
def multiply2(numbers, multiplier):
    return [ num * multiplier for num in numbers ]

print(multiply2(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]

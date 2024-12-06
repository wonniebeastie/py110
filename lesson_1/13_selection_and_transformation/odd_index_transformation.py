"""
PROBLEM
Given a list, multiply the integers at odd indexes by 2.

INPUT & OUTPUT
I: a list of integers
O: the input list with the integers at odd indexes multiplied by 2

TEST CASE
- [1, 4, 3, 7, 2, 6] => [1, 8, 3, 14, 2, 12]

ALGO
[] 1. Create an empty list to hold new values. 
[] 2. Go through the list of numbers and multiply the integers at odd
indexes by 2.
    [NOTE] Iterate over integers using a `for` loop 
    2A) Check if the index is odd 
        a) Set "index" to 0.
    2B) If "index" is odd, multiply the integer with 2
        a) Add the transformed integer to empty list.
        b) Increment "index" by 1.
    2C) Else add the integer to empty list.
        a) Incerement "index" by 1.
[] 3. Return it as a new list.
"""

def double_odd_index(numbers):
    transformed_list = []

    for num in range(len(numbers)):
        current_num = numbers[num]

        if num % 2 != 0:
            transformed_list.append(current_num * 2)
        else:
            transformed_list.append(current_num)

    return transformed_list

my_numbers = [1, 4, 3, 7, 2, 6]

print(double_odd_index(my_numbers)) # [1, 8, 3, 14, 2, 12]
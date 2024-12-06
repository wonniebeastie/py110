def double_numbers(numbers):
    for current_num in range(len(numbers)):
        numbers[current_num] *= 2

    return numbers


my_numbers = [1, 4, 3, 7, 2, 6]

# print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
# print(my_numbers) # [2, 8, 6, 14, 4, 12]

"""
PROBLEM
Change the `double_numbers` function to let the integers in the input
list to be multiplied by an arbitrary number.

INPUT & OUTPUT
I: a list with integers 
I: integer (number to be multiplied by)
O: a new list with the integers transformed

RULES 
- Do not mutate the list - return a new list.

TEST CASE:
- [1, 4, 3, 7, 2, 6] => [3, 12, 9, 21, 6, 18]

ALGO [High-Lvl]
1. Create new list to hold new values.
    [NOTE] To avoid mutation.
2. For each number, multiply it by the input number.
3. Reapeat until end of the list.
4. Return the new list.

ALGO [PROGRAMMATIC]
[x] 1. Create "(to be) transformed list" to hold new values. [NOTE] 
        - To avoid mutation.
[] 2. Loop through each "number" of "input list", and multiply it by
    "input number". [NOTE]
        - Use a `for` loop.
        - With a `range` object same length as "input list" (remember
        that stop value is exclusive).
        [TODO: SUBSTEPS]
        - Add transformed "number" to "transformed list".
[] 3. Repeat until end of "input list".
[] 4. Return "transformed list".
"""

def multiply(num_list, multiplier):
    transformed_list = []

    for current_num in num_list:
        new_num = current_num * multiplier
        transformed_list.append(new_num)
    
    return transformed_list


my_numbers = [1, 4, 3, 7, 2, 6]

print(multiply(my_numbers, 3)) # [3, 12, 9, 21, 6, 18]
print(my_numbers) # [1, 4, 3, 7, 2, 6]

"""
This function is different from `double_numbers` in that:
- The `double_numbers` directly alters the element at each index of
the input list using a `range` object because it's meant to mutate
the input list.
- The `multiply`function just uses the values of the input list to
multiply with & adds the values to the new list, avoiding mutation.
"""

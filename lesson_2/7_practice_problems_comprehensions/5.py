"""
INPUT & OUTPUT
I: a list with sublists
O: a new list that contains the same sublists as the input list but 
sorted based on the sum of the odd numbers in ascending order.


EXAMPLES / TEST CASES
input: [[1, 6, 7], [1, 5, 3], [1, 8, 3]] 
=>
output: [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

ALGO
[x] 1. Create empty "sorted_lst" list.
[] 2. For each sublist, sum the numbers that are odd.
	- If sum of odd numbers 
[] 3. Add them to "sorted_lst" in ascending order.
[] 4. Return "sorted_lst".
"""

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sort_by_odd_sum(int_list):
	odd_nums = [num for num in int_list if num % 2 != 0]
	return sum(odd_nums)

sorted_list = sorted(lst, key=sort_by_odd_sum)
print(sorted_list)

# NOTE: You can create a function just to use it to decide the order of
# elements.



# SECOND PASS
"""
I: a list with nested lists of numbers
O: a new list with nested lists of numbers, sorted by the sum of the 
   odd numbers they contain

✱ EXAMPLES ✱
- Ex 1
- I: [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
- O: [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

✱ QUESTIONS ✱
- 

✱ SUB-PROBLEMS ✱
- og list can't be mutated
    - come up with a way to make a new list
        - op1: use sorted() function - returns a new list
        - op2: use a comprehension

- need a custom function to use as the key to sort
    - custom function should be able to:
        - if number is odd, add them up
            - need a way to identify odd numbers
            - need a way to sum them
        - return the sum

- new list must be sorted in ascending order

✱ A - ALGORITHM ✱ (-, +, -, +)

I: sublist
[] - define custom function "odd_sum"
    [] + initialize "result" - set to 0
    [] + for each "number" in "sublist":
        [] - if number is odd, (number % 2 != 0)
            [] + add number to result
    [] - return result

I: nested_list
[] -  define main function "sorted_by_odd_sum"
    [] + sort nested_list by ascending order using odd_sum as key
    [] + return sorted list

"""
# Solution: traditional loop
def odd_sum(sublist):
    result = 0

    for num in sublist:
        if num % 2 != 0:
            result += num

    return result

def sorted_by_odd_sum(nested_list):
    return sorted(nested_list, key=odd_sum)

# Solution: Using comprehension
def odd_sum2(sublist):
    return sum([num for num in sublist if num % 2 != 0])

def sorted_by_odd_sum2(numbers):
    return sorted(numbers, key=odd_sum2)

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

print(sorted_by_odd_sum(lst))  # [[1, 8, 3], [1, 6, 7], [1, 5, 3]]
print(sorted_by_odd_sum2(lst)) # [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

# The list comprehension in `odd_sum2()` returns a list of just the odd numbers
# which is then added and returned by the function.
# The `sorted_by_odd_sum2()` function takes a nested list as its input, and
# uses the `sorted()` built-in function with the `odd_sum2()` function as the
# key to sort the nested list in ascending order and returns it as a new list. 


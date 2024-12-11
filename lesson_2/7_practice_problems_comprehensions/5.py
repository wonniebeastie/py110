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
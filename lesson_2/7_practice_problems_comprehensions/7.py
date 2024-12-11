'''
I: a list with sublists
O: a new list identical in structure to input list but only containing
numbers that are multiples of `3`

Expected result:
[[], [3, 12], [9], [15, 18]]
'''
# Using nested `for` loops:
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = []

for sublist in lst:
	new_sublst = []
	for num in sublist:
		if num % 3 == 0:
			new_sublst.append(num)
	
	new_lst.append(new_sublst)

print(new_lst)
# [[], [3, 12], [9], [15, 18]]
print(lst)
# [[2], [3, 5, 7, 12], [9], [11, 15, 18]]


# Using a list comprehension:
def only_multiples_of_3(sublist):
	return [ num for num in sublist if num % 3 == 0 ]

# print(only_multiples_of_3([3, 5, 7, 12]))
new_lst = [ only_multiples_of_3(sublist) for sublist in lst ]

print(new_lst) # [[], [3, 12], [9], [15, 18]]
print(lst) # [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

'''
SOLUTION
'''
# Solution 1
new_list = []

for sublist in lst:
    new_sublist = []
    for num in sublist:
        if num % 3 == 0:
            new_sublist.append(num)

    new_list.append(new_sublist)

print(new_list)


# Solution 2 - refactoring the inner loop from Solution 1 into a
# comprehension
new_list = []

for sublist in lst:
    new_sublist = [num for num in sublist if num % 3 == 0]
    new_list.append(new_sublist)

print(new_list)

# Solution 3 - refactoring by extracting the comprehension from
# Solution 2 into a function, and creating another comprehension
# that uses that function as its outer_expression. 
def divisible_by_3(sublist):
    return [num for num in sublist if num % 3 == 0]

new_list = [divisible_by_3(sublist) for sublist in lst]
print(new_list)

'''
Solution 4 - refactoring by using the comprehension inside the function
from Solution 3 as its outer_expression rather than a function call.

Very concise, but hard to understand.

Nested comprehensions in the output_expression like this are usually a 
sign that you've refactored TOO MUCH.
'''
new_list = [[num for num in sublist if num % 3 == 0] for sublist in lst]
print(new_list)
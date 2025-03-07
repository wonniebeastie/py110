"""
PROBLEM
Create a function that returns a new list, with the elements doubled, but only
the numbers at odd indexes.

QUESTIONS
Q:

I: a list of numbers
O: a new list, elements at odd indexes in the original list, doubled

DS:
- 

ALGO (-, +, -, +)
[x] - initialize empty list "doubled nums"
[x] - for each number in input list,
    [x] + if the index is odd, 
        [x] - multiply number by 2
        [x] - add it to "doubled nums"
[x] - return "doubled nums" list

"""
# Solution 1
def double_odd_numbers(numbers):
    doubled_nums = []

    for indx in range(len(numbers)):
        if indx % 2 != 0:
            doubled_nums.append(numbers[indx] * 2)
        else:
            doubled_nums.append(numbers[indx])

    return doubled_nums

my_numbers = [1, 4, 3, 7, 2, 6]

print(double_odd_numbers(my_numbers))  # [1, 8, 3, 14, 2, 12]

# not mutated
print(my_numbers) # [1, 4, 3, 7, 2, 6]


# LS SOLUTION
def double_nums_with_odd_indexes(numbers):
    doubled_nums = []

    for idx in range(len(numbers)):
        current_number = numbers[idx]

        if idx % 2 == 1:
            doubled_nums.append(current_number * 2)
        else:
            doubled_nums.append(current_number)

    return doubled_nums

print(double_nums_with_odd_indexes(my_numbers)) # [1, 8, 3, 14, 2, 12]
print(my_numbers)


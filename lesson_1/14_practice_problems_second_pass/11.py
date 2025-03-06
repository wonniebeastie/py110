# What does the following code return? Try to answer without running the code.
lst = [1, 2, 3, 4, 5]
lst[:2]

# This will return:
# [1, 2]

# It uses slicing notation with the optional stop value, which is exclusive.abs
# So even though it stops at index 2, which is element `3`, it is not included
# in the returned slice because it's excluded by default.

# Given the following code, what will the final values of `a` and `b` 
# be? Try to answer without running the code.

a = 2
b = [5, 8]
lst = [a, b]   # Essentially, [2, [5, 8]]

lst[0] += 2    
# 4 - We're adding 2 to the integer referred to at lst's index 0
# Now it looks like `lst = [4, [5, 8]]`
lst[1][0] -= a 
# 3 - We're using the integer referred to by `a`, which is 2, to
# subtract that from the integer referred to by `lst[1][0]`, which is
# 5, and reassigning the element at that index 0.

print(lst)  # [4, [3, 8]]
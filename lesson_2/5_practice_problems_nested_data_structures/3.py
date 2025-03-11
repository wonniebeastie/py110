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




# SECOND PASS
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

# The final value of `a` will be `2`. The value assigned to `a` on line 1 is
# `2`. This is what is referred to by `lst[0]` on line 5. This value (`2`) is
# used to add another `2` to, creating a new object (`4`), which is then 
# reassigned to index 0` of `lst`. 
# And although `2` was used to do this, since integers are immutable values in 
# Python, it cannot be changed after creation. So the `a` will remain `2`, as 
# `a` itself has never been reassigned. 

# The final value of `b` will be `[3, 8]`. The `lst[1][0]` on line 6 references 
# the value at index 0 of the list referred to by `b`, which is `5`. What is 
# assigned to `a` at this point (`2`), is subtracted from this `5`, leaving `3`
# . This is possible because the object referred to by `b` is a list, which is
# a mutable value, meaning it can be changed after creation.

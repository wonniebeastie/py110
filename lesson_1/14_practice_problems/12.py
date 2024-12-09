# What would be the output of the below code? Try to answer without 
# running the code.
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)

print(frozen)

"""
I think this will result in an error because frozensets are immutable,
so the `add` method, which is mutating, cannot be used with them.
"""
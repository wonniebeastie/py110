# What would be the output of the below code? 
# Try to answer without running the code.
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)

print(frozen) # AttributeError: 'frozenset' object has no attribute 'add'

# This will result in an error because frozensets are immutable, which means
# they can't be changed after creation. So attempting to add an element will
# not work.

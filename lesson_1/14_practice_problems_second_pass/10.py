# What does the following code print and why?
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

# This returns:
# ('b': 'bear')
# because the `popitem` dictionary method returns the last key-value pair 
# from the dictionary and returns it as a tuple.

# What does the following code print and why?
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

"""
This will print:
```
('b', 'bear')
```
The `popitem()` method "pops off" the last key-value pair in a
dictionary and returns it as a tuple.
"""

# Count the number of occurences of "banana" in the tuple.
fruits = ("apple", "banana", "cherry", "date", "banana")

print(fruits.count("banana")) # 2

"""
I: tuple
O: integer (# of "banana"s)

A:
[x] 1. Set "banana count" to 0.
[x] 2. Iterate through tuple, check if input is "banana".
    [TODO: Use a for loop]
[x] 3. If it is, then increment "banana count" by 1.
[x] 4. Return "banana count".
"""

banana_count = 0

for fruit in fruits:
    if fruit == "banana":
        banana_count += 1

print(banana_count) # 2
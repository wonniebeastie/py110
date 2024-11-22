numbers = [1, 2, 3, 4]
numbers[0] = numbers[0] + 1

print(numbers) # [2, 2, 3, 4]

# Increment values of the remaining numbers in the `numbers` list by 
# `1`. Also try this with an element that does not exist, such as 
# `numbers[4]`.

# Method 1
numbers[1] += 1
numbers[2] += 1
numbers[3] += 1

print(numbers) # [2, 3, 4, 5]


# Method 2
numbers = [1, 2, 3, 4]

numbers[0] += 1

index = 1

while index < len(numbers):
    numbers[index] += 1
    index += 1

print(numbers) # [2, 3, 4, 5]


# Method 3
numbers = [1, 2, 3, 4]
numbers[0] += 1

for num in range(1, len(numbers)):
    numbers[num] += 1

print(numbers) # [2, 3, 4, 5]

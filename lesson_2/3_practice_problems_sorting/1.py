# Sort in ascending numeric order, then descending order. Do not mutate
# the list.
lst = [10, 9, -6, 11, 7, -16, 50, 8]

print(sorted(lst))               # [-16, -6, 7, 8, 9, 10, 11, 50]
print(sorted(lst, reverse=True)) # [50, 11, 10, 9, 8, 7, -6, -16]

print(lst) # [10, 9, -6, 11, 7, -16, 50, 8]

"""
PROBLEM
Calculate the total age in input dictionary

INPUT & OUTPUT
I: dictionary of people's names (strings) & their ages (integers)
O: integer (sum of their ages)
"""
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

ages_only = ages.values()

print(sum(ages_only)) # 6174


# SOLUTION
total_age = sum(ages.values())
print(total_age) # 6174
"""
PROBLEM
Determine the minimum age from the given `ages` dictionary

INPUT & OUTPUT
I: dictionary of people's names (strings) & their ages (integers)
O: integer (minimum age)
"""

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

print(min(ages.values())) # 10

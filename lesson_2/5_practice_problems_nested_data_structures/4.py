"""
PROBLEM
Given the object shown below, print the name, age, and gender of each
family member (the `munsters` dictionary)

INPUT & OUTPUT
I: a dictionary of family names and their age & gender
O: strings that follow the pattern: (name) is a (age)-year-old (male or
female).
"""

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

def print_family_info(family_info):
	for name, other_info in family_info.items():
		print(f"{name} is a {other_info['age']}-year-old {other_info['gender']}.")

print_family_info(munsters)
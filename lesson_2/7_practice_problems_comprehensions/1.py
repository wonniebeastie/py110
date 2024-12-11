"""
PROBLEM
Compute and display the total age of the family's male members. Try 
working out the answer two ways: first with an ordinary loop, then with
a comprehension.


INPUT & OUTPUT
I: a dictionary with nested dictionaries
O: an integer (the sum of male family members' ages)

ALGO 
[x] 1. Create empty "ages to be summed" list.
[] 2. Loop through each key-value pair of "given dictionary" -
		[x] 2A. Loop through "nested dictionary"
			a) If the value of "gender" is "male" - [NOTE: EXTRACTED]
				Add "age" to "ages to be summed" list.
			b) Else, go onto next pair.
[x] 3. Repeat until end of dictionary.
[x] 4. Sum the values in "ages to be summed" list.
[x] 5. Return the sum.

<------ STEP a EXTRACTED ------> 

Problem: Figure out how to check if the value of 'age' is 'male.

I: a dictionary of age & gender
O: a string - 'male'

Rules:
- The values of the outer dictionary are nested dictionaries.

Can do either:
- if 'male' is a value to any of the keys in this sub-dictionary using
`in`.
- if `'gender' == 'male'` [TODO]
- go by name - but don't think this is a good idea for future use.

Algorithm (xA, xB...)
A) if "input dictionary"['gender'] is 'male',
B) append it to "ages" list.

<------------------------------>

"""

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Using a regular `for` loop.
def sum_male_ages(family_info):
	ages = []

	for age_n_gender in family_info.values():
		if age_n_gender['gender'] == 'male':
			ages.append(age_n_gender['age'])
	
	summed_ages = sum(ages)

	return summed_ages

print(sum_male_ages(munsters)) # 444

# Using a comprehension.
def sum_male_ages_comprehension(family_info):
	age_list = [person_info['age'] for person_info in family_info.values()
								if person_info['gender'] == 'male']
	return sum(age_list)

print(sum_male_ages_comprehension(munsters)) # 444


# SOLUTIONS
total_male_age = 0
for member in munsters.values():
    if member['gender'] == 'male':
        total_male_age += member['age']

print(total_male_age)         # 444

all_male_ages = [member['age'] for member in munsters.values()
                            	if member['gender'] == 'male']

print(sum(all_male_ages))     # 444
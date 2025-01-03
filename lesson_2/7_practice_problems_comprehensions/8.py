"""
INPUT & OUTPUT
I: a dictionary with nested dictionaries
O: a list that contains the COLORS of FRUITS,
and SIZES of VEGETABLES.


RULES (EXPLICIT/IMPLICIT)
EXP:
- Sizes should be uppercase.
- Colors should be capitalized.

IMP:
- 

EXPECTED RESULT
[["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]


ALGO 
[] 1. Create an empty "resulting_list".
[] 2. Loop through each item in "input dictionary"
	- if the "type" is a "fruit", 
		append the value of "colors" to "resulting_list"
	- if the "type" is a "vegetable",
		append the value of "size" to "resulting list"
[] 3. Repeat until end of "input dictionary"
[] 4. Return "resulting_list".

"""

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def color_n_size(fruits_n_veggies):
	resulting_list = []
	
	for item in fruits_n_veggies.values():
		if item['type'] == 'fruit':
			uppercase_colors = []
			for color in item['colors']:
				uppercase_colors.append(color.capitalize())
			resulting_list.append(uppercase_colors)
		else:
			resulting_list.append(item['size'].upper())
	
	return resulting_list

# print(color_n_size(dict1)) 
# [['Red', 'Green'], 'MEDIUM', ['Orange'], 'LARGE']

'''
NOW DO ONE WITH COMPREHENSION!
'''


def color_or_size(subdict):
	if subdict['type'] == 'fruit':
		return [color.capitalize() for color in subdict['colors']]
	else:
		return subdict['size'].upper()

def colors_n_sizes(dictionary):
	return [color_or_size(subdict) for subdict in dict1.values()]

print(colors_n_sizes(dict1))
# [['Red', 'Green'], 'MEDIUM', ['Orange'], 'LARGE']

'''
The `color_or_size` function defined on line 77 works by returning
either a list with strings that describe a color or colors (first
character capitalized) if the value for the `'type'` key is `'fruit'`,
or just a string describing size otherwise (if it's `'vegetable'`), 
all in uppercase.

This returning value is used in the function defined after it, called
`colors_n_sizes`. This function returns the final list called for by
the problem description - a list of colors in sublists and sizes as 
strings.
'''
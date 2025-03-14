# """
# INPUT & OUTPUT
# I: a dictionary with nested dictionaries
# O: a list that contains the COLORS of FRUITS,
# and SIZES of VEGETABLES.


# RULES (EXPLICIT/IMPLICIT)
# EXP:
# - Sizes should be uppercase.
# - Colors should be capitalized.

# IMP:
# - 

# EXPECTED RESULT
# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]


# ALGO 
# [] 1. Create an empty "resulting_list".
# [] 2. Loop through each item in "input dictionary"
# 	- if the "type" is a "fruit", 
# 		append the value of "colors" to "resulting_list"
# 	- if the "type" is a "vegetable",
# 		append the value of "size" to "resulting list"
# [] 3. Repeat until end of "input dictionary"
# [] 4. Return "resulting_list".

# """

# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }

# def color_n_size(fruits_n_veggies):
# 	resulting_list = []
	
# 	for item in fruits_n_veggies.values():
# 		if item['type'] == 'fruit':
# 			uppercase_colors = []
# 			for color in item['colors']:
# 				uppercase_colors.append(color.capitalize())
# 			resulting_list.append(uppercase_colors)
# 		else:
# 			resulting_list.append(item['size'].upper())
	
# 	return resulting_list

# # print(color_n_size(dict1)) 
# # [['Red', 'Green'], 'MEDIUM', ['Orange'], 'LARGE']

# '''
# NOW DO ONE WITH COMPREHENSION!
# '''


# def color_or_size(subdict):
# 	if subdict['type'] == 'fruit':
# 		return [color.capitalize() for color in subdict['colors']]
# 	else:
# 		return subdict['size'].upper()

# def colors_n_sizes(dictionary):
# 	return [color_or_size(subdict) for subdict in dict1.values()]

# print(colors_n_sizes(dict1))
# # [['Red', 'Green'], 'MEDIUM', ['Orange'], 'LARGE']

# '''
# The `color_or_size` function defined on line 77 works by returning
# either a list with strings that describe a color or colors (first
# character capitalized) if the value for the `'type'` key is `'fruit'`,
# or just a string describing size otherwise (if it's `'vegetable'`), 
# all in uppercase.

# This returning value is used in the function defined after it, called
# `colors_n_sizes`. This function returns the final list called for by
# the problem description - a list of colors in sublists and sizes as 
# strings.
# '''


# SECOND PASS
"""
I: a dictionary 
O: a list - containing specific values based on type

✱ EXAMPLES ✱
- Ex 1
- I: 
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
- O: [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

✱ REQUIREMENTS ✱
- return list must contain colors of the fruits & sizes of the vegetables
- sizes = uppercase
- colors = capitalized

- so of each item of input dict:
    - the key `'type'` in each sub-dict value must be `'fruit'` or `'vegetable'`
      of these:
        - if the type is `'fruit'`:
            + the value of key `'colors'` must be added to returning list
            + the elements of the value must be added as is, as a list, instead
              of as individual items.
            + each string of the value must be capitalized
        - if the type is `'vegetable'`:
            + the value of key `'size'` must be added to returning list
            + the value must be in all uppercase

✱ QUESTIONS ✱
- Does order matter for the result?
    - assume yes, bc example output.
- Can the list of colors be mutated?
    - if yes, reassign element at list?
    - if no, create new list

✱ A - ALGORITHM ✱
I: `produce_items`
[x] - initialize empty container list - `size_color_list`
[] - for each key-value pair in `produce_items` dictionary:
    + if the `value['type']` is `'fruit'`:
        - get the list of color(s) (direct key access)
        - for each color in list of color(s):
            + capitalize first letter of each string
            + add transformed list of colors to `size_color_list`
    + if the `value['type']` is `'vegetable'`, 
        - get the size
        - transform the whole string to uppercase
        - add the transformed size to `size_color_list`
[] - Return `size_color_list`

""" 
def get_colors_n_sizes(produce_items):
    size_color_list = []

    for produce in produce_items:
        if produce_items[produce]['type'] == 'fruit':
            color_list = produce_items[produce]['colors']
            new_color_list = []
            for color in color_list:
                transformed_color = color.capitalize()
                new_color_list.append(transformed_color)
            size_color_list.append(new_color_list)
    return size_color_list

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

print(get_colors_n_sizes(dict1))

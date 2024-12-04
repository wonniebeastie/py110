"""
P: INPUT & OUTPUT, RULES (EXP/IMP), QUESTIONS, MENTAL MODEL

INPUT & OUTPUT
I: integer - number of available blocks
O: integer - number of blocks left over after building the tallest
possible valid structure. 	

QUESTIONS
- What is a "valid" structure?
- What to do if given input is 0?
- Is a lower layer valid if it has more blocks than it needs?
- Will there always be left-over blocks?


RULES (EXPLICIT/IMPLICIT) 
EXP:
- Structures:
	- Built with blocks.
		- Blocks are cubes.
		- Cubes: 6 sided, square faces, equal lengths on all sides.
- Top layer is a single block.
- One upper block - must be supported by 4 lower blocks
- One lower block - can support more than 1 upper block
- No gaps between blocks.

IMP:
- Layer number correlates with blocks in a layer (layer 1: 1x1, layer 2: 
2x2, 3x3...)
- The number of blocks in a layer is: layer number * layer number 
(rule of 1 lower block being able to support more than 1 upper block 
suggests overlapping arrangement - so lower blocks can be counted more
than once when counting how many blocks are there to support an upper 
block.)

SEQ:
- Layer 1: 1 block  (1x1)
- Layer 2: 4 blocks (2x2)
- Layer 3: 9 blocks (3x3)


EXAMPLES / TEST CASES
- Available blocks: 0 -> Leftover blocks: 0
- Available blocks: 1 -> Leftover blocks: 0
- Available blocks: 2 -> Leftover blocks: 1
- Available blocks: 4 -> Leftover blocks: 3
- Available blocks: 5 -> Leftover blocks: 0
- Available blocks: 6 -> Leftover blocks: 1
("Is a lower layer valid if it has more blocks than it needs?" No.)
- Available blocks: 14 -> Leftover blocks: 0
("Will there always be left-over-blocks" No.)


DS / VISUALIZATION
- Maybe we can use a nested list to represent the structure?
	- Each sublist could represent a layer.

VS: 
[
    ['x'],
    ['x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ...
]

ALGO (HIGH-LEVEL)
1. Build structure one layer at a time until you no longer have enough
blocks left to build a "valid" layer.
2. Count how many blocks you have left.

ALGO
1. Start with:
    - The "number of blocks remaining" is equal to the input.
    - The "current layer number" is layer 1.
    - The "number of blocks required in this layer" is 1.

2. Subtract the "number of blocks required in this layer" from
the "number of blocks remaining".

3. Calculate the "current layer number" for the next layer by
adding 1 to the "current layer number".

4. Using the new "current layer number", calculate the "number of
blocks required in this layer" by multiplying the "current
layer number" by itself.

5. Determine whether the "number of blocks remaining" is greater
than or equal to the "number of blocks required in this layer".
    - If there are enough blocks:
        - Subtract the "number of blocks required in this layer"
        from the "number of blocks remaining".
        - Go to step 3.
    - If there aren't enough blocks:
        - Return the "number of blocks remaining".

ALGO (CORRECTED):
1. Start with:
    - The "number of blocks remaining" is equal to the input.
    - The "current layer number" is layer 0.

2. Calculate the "current layer number" for the next layer by
adding 1 to the "current layer number".

3. Using the new "current layer number", calculate the "number of
blocks required in this layer" by multiplying the "current
layer number" by itself.

4. Determine whether the "number of blocks remaining" is greater
than or equal to the "number of blocks required in this layer".
    - If there are enough blocks:
        - Subtract the "number of blocks required in this layer"
        from the "number of blocks remaining".
        - Go to step 2.
    - If there aren't enough blocks:
        - Return the "number of blocks remaining".

Notes:
- Use a `while` loop?
    - For the condition, check whether "number of blocks
    remaining" is greater than or equal to the "number of
    blocks required".
- Calculating the blocks for the next layer, use `**` operator?
    - For example: `(current_layer + 1)**2`.
"""

def calculate_leftover_blocks(available_blocks):
	current_layer = 0
	remaining_blocks = available_blocks

	required_blocks = (current_layer + 1) ** 2

	while remaining_blocks >= required_blocks:
		remaining_blocks -= required_blocks
		current_layer += 1
		required_blocks = (current_layer + 1) ** 2
	
	return remaining_blocks


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True







































"""
P: INPUT & OUTPUT, RULES (EXP/IMP), QUESTIONS, MENTAL MODEL

INPUT & OUTPUT
I: integer (number of available blocks)
O: integer (left over after building the tallest possible valid 
structure)

QUESTIONS
- What is a "valid structure"?
- What makes a layer "valid"?
- Is a lower layer still valid if it has more blocks than it needs?
	A: After looking at the test cases, no.
- Will there always be left-over blocks?
	A: After looking at the test cases, no.
- Do we have to represent the structure as specific data?

RULES (EXPLICIT/IMPLICIT)
E:
- Number of available blocks will be given.
- Building blocks == cubes (cubes are 6-sided, square faces, equal
	length on all sides)
- Top layer is always a single block.
- 1 block in upper layer - must be supported by 4 blocks in lower
	layer.
- 1 block in lower layer - can support 1+ blocks in an upper layer.
- No gaps between blocks.

I:
- Layer # correlates with blocks in a layer.
- The # of blocks in a layer is layer number * layer number.


EXAMPLES / TEST CASES
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

DS
- Maybe we can use a nested list to represent the structure (if needed)?
---> Each sublist could represent a layer. 
[
    ['x'],
    ['x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ...
]


ALGO
High-level, abstract:
1. Build the structure one layer at a time until you no longer
    have enough blocks left to build a "valid" layer.
2. Count how many blocks you have left.

- Create a function `calculate_leftover_blocks`, with 1 parameter - 
	`available_blocks` 
- Given an integer, multiply it with itself, assign to variable `valid_layer`.
- Subtract `valid_layer` from `available_blocks`, assign to variable 
	`left_over_blocks`.
- Return `left_over_blocks`.

"""


"""
P: INPUT & OUTPUT, RULES (EXP/IMP), QUESTIONS, MENTAL MODEL

INPUT & OUTPUT
I: Integer representing the number of a particular row
O: Integer representing the sum of all integers in that row

QUESTIONS


RULES (EXPLICIT/IMPLICIT) 
E:
- Sequence of integers
- Sequence begins with 2
- Integers are consecutive
- Integers are even
- Sequence is grouped into rows
- Each row is incrementally larger than the last: 1, 2, 3, ...

I:
- Row 1 has 1 element, row 2 has 2 elements, etc.

Sequence:
- 2 --> 2
- 4, 6 --> 10
- 8, 10, 12
- 14, 16, 18, 20 --> 68


EXAMPLES / TEST CASES
- Row number: 1 → Sum of integers in row: 2
- Row number: 2 → Sum of integers in row: 10
- Row number: 4 → Sum of integers in row: 68


DS / VIS
((We know we have a structure that consists of:
- Sequence of rows
- Order of rows is important
- Rows contain integers
- Order of integers is important))
- Nested list

[
    [2],
    [4, 6],
    [8, 10, 12],
    [14, 16, 18, 20],
    ...
]


ALGO
1. Create an empty 'rows' array/list to hold all of our rows.
2. Create a 'row' array/list and add it to the overall 'rows' 
	array/list. [EXTRACTED]
3. Repeat step 2 until all the necessary rows have been created. [NOTE]
	All the rows have been created when the length of the 'rows' array/list is equal to the input. 
4. Sum the final row.
5. Return the sum.



<------ FOR STEP 2 OF MAIN ALGO (HELPER FUNCTION) ------>

Problem: Create a Row

Rules: 
- Row is an array/list
- Array/list contains integers
- Integers are consecutive even numbers
- Integers in each row form part of a larger overall sequence
- Rows are of different lengths.

I:
- Length of the row
- The starting integer

O: The row itself ---> [8, 10, 12]

Examples:
- starting int: 2, row length: 1 --> [2]
- starting int: 4, row length: 2 --> [4, 6]
- starting int: 8, row length: 3 --> [8, 10, 12] 

Data Structure: array/list 

Algorithm:
2A. Create an empty 'row' array/list to contain the integers.

2B. Add the starting integer (which would be one of the inputs we receive)

2C. Increment the starting integer by 2 to get the next integer in the sequence.

2D. Repeat steps 2 & 3 until array/list has reached the correct length 
	(second input we receive). [SUBSTEPS]
		a) Start the loop
			a.1 Add start_integer to row [EXTRACTED]
			a.2 Increment start_integer by 2.
			a.3 Break out of loop if length of row equals row_length

2E. Return the 'row' array/list.

<------ END OF STEP 2 OF MAIN ALGO (HELPER FUNCTION) ------>


<------ STEP a.1 EXTRACTED ------> 

Problem: Calculating the start integer

Rules: First integer of row == last integer of preceding row + 2

Algorithm (x.1, x.2,...)
a.1.1 Get the last row of the rows list
a.1.2 Get the last integer from that row
a.1.3 Add 2 to that integer

<------- END OF STEP a.1 EXTRACTED ------>

"""

def sum_even_number_row(row_number): # main function
    rows = []
    start_integer = 2
    
    for row_length in range(1, row_number + 1):
        row = create_row(start_integer, row_length)
        rows.append(row)
        start_integer = row[-1] + 2
        
    return sum(rows[-1])

def create_row(start_integer, row_length): # helper function
    row = []
    current_integer = start_integer
    while len(row) < row_length:
        row.append(current_integer)
        current_integer += 2
    return row

print(sum_even_number_row(1) == 2)
print(sum_even_number_row(2) == 10)
print(sum_even_number_row(4) == 68)

print(create_row(2, 1) == [2])
print(create_row(4, 2) == [4, 6])
print(create_row(8, 3) == [8, 10, 12])
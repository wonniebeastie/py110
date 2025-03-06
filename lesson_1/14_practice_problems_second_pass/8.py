"""
PROBLEM
Create a dictionary that represents the frequency with which each letter occurs.

I: a string - "The Flintstones Rock"
O: a dictionary - with each letter as keys & the values how many times they
   occur

QUESTIONS
- What process needs to happen?
  + Character counting
- Are there special cases to consider?
  + white space characters
  + case-sensitivity

RULES
EXP
- Frequency count needs to be case-sensitive.

IMP
- The whitespaces are not counted.

EXAMPLE
{
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}

TEST CASES
- What happens with empty strings?
- What about a string with only spaces?
- What about strings of numbers or special characters?

DS
- Dictionary (key/value association)


ALGO (-, +, -, +)
How will I go from an input string to a dictionary of character frequencies?
What steps need to happen in between?
~ How will I acesss each character in the string?
~ How will I handle the requirement to ignore whitespace?
~ How will I count and store the frequency of each character?

[x] - Initialize empty dictionary
[x] - For each character in the input string:
    [x] + If the character is not a space:
        [x] - If the character is already in the dictionary:
            [x] + Increment its count
        [x] - Else:
            [x] + Add the character to the dictionary with a count of 1
[x] - Return the dictionary

"""
statement = "The Flintstones Rock"

# Solution 1: traditional loop
def char_count(txt):
    count = {}

    for char in txt:
        if char != ' ':
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    return count

print(char_count("")) # {}
print(char_count(" ")) # {}
print(char_count("aaa")) # {'a': 3}

print(char_count(statement))
# {'T': 1, 'h': 1, 'e': 2, 'F': 1, 'l': 1, 'i': 1, 'n': 2, 't': 2, 's': 2, 'o': 2, 'R': 1, 'c': 1, 'k': 1}

# LS Solution:
# Initialize empty dictionary
char_freq = {}
# The `replace` method replaces the spaces in the og string with empty strings.
statement = statement.replace(' ', '')

# Iterates through "TheFlintstonesRock"
for char in statement:
    # Assigns key-value pairs of:
    # Key: the character in "TheFlintstonesRock"
    # Value: The `get` dictionary method fetches whatever value is associated
    # with the character, if there is none, returns 0, which 1 is then added.
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)

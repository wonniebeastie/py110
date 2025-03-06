# What would the following code output? Try to answer without running the code.
words = ['ant', 'bear', 'cat']
selected_words = []

for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)

# This code would output:
# ['bear']

# The `for` loop on line 5 iterates through each string in the `words` list;
# The `len()` function on line 6 returns the number of characters in the 
# string of the current iteration. The greater than operator, `>`, is then used
# to determine whether the value returned by the function is greater than 3. 
# And if it is, the string is appended to the `selected_words` list, defined on
# line 3, using the `append()` list method, which adds a specified element to 
# the end of the list it was called on.

# Finally, the `print()` function prints this mutated list onto the console.



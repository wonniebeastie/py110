# What would the following code output?
words = ['ant', 'bear', 'cat']

selected_words = []

for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)

"""
This code iterates through the list assigned to the `words` variable
and adds the strings that are more than 3 characters long to a new list
called `selected_words` and returns it. 

Therefore, I believe this code will output:
```
['bear']
```
"""
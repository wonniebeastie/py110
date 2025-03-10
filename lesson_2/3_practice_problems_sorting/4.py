# How would you sort the following list of dictionaries based on the 
# year of publication of each book, from the earliest to the most 
# recent?

def transform_year(book):
	year = int(book['published'])
	return year

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

print(sorted(books, key=transform_year))
# [
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800'
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869'
#     },
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967'
#     }
# ]

# SECOND PASS
"""
✱ P - PROBLEM ✱

INPUT & OUTPUT
I: a list of nested dictionaries
O: a list of nested dictionaries, sorted by publication year, ascending


✱ E - EXAMPLES/TEST CASES ✱

- Example 1
- I: 
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
- O:
# Pretty printed for clarity
[
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800'
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869'
    },
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967'
    }
]


✱ A - ALGORITHM ✱
SUB-PROBLEMS
- find a way to target the value to the nested `'published'` key
- then sort the values as numbers instead of strings, in ascending order.
  (the `sorted()` function allows for custom sorting - use `int`)

(-, +, -, +)
[x] - initialize a custom function to return each value of `'published'` key as
     an integer - "get published year"
     [NOTE: extracted step 1]
     [NOTE: this integer is what will be used by `sorted()` to sort the input
      list.]
[x] - use `sorted()` function with custom function to sort the list 
[x] - print list

<-------- EXTRACTED STEP 1 -------->

✱ P - PROBLEM ✱
I: a dictionary
O: an integer (the value of `'published'` key)

✱ D - DATA STRUCTURE ✱
- 

✱ A - ALGORITHM ✱
SUB-PROBLEMS
- target the nested value of a key-value pair
- convert it to an integer from a string

(-, +, -, +)
[x] - target the value of "published" key
[x] - convert it to an integer
[x] - return the integer
<---------------------------------->

"""
def get_published_year(book):
    return int(book['published'])

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

sorted_book_list = sorted(books, key=get_published_year)

print(sorted_book_list)
# [
#     {
#         'title': 'The Book of Kells',
#         'author': 'Multiple Authors',
#         'published': '800'
#     },
#     {
#         'title': 'War and Peace',
#         'author': 'Leo Tolstoy',
#         'published': '1869'
#     },
#     {
#         'title': 'One Hundred Years of Solitude',
#         'author': 'Gabriel Garcia Marquez',
#         'published': '1967'
#     }
# ]

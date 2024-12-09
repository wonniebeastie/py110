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
# Desired Output: {book1: 1925, book2: 1960, book3: 1979}
library_catalog = {
    "book1": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genres": ["Fiction", "Classics"]
    },
    "book2": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genres": ["Fiction", "Classics"]
    },
    "book3": {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "year": 1979,
        "genres": ["Science Fiction", "Comedy"]
    }
}

def print_desired_dictionary(catalog):
    result = {}
    for book, details in catalog.items():
        result[book] = details["year"]
    return result

# Call the function and print the result
desired_output = print_desired_dictionary(library_catalog)
print(desired_output)
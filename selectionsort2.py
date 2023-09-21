def selection_sort_books(books, key):
    n = len(books)

    for i in range(n):
        # Find the index of the minimum element based on the specified key
        min_index = i
        for j in range(i + 1, n):
            if books[j][key] < books[min_index][key]:
                min_index = j

        # Swap the found minimum element with the current element
        books[i], books[min_index] = books[min_index], books[i]

# Example usage
if __name__ == "__main__":
    books = [
        {"title": "Book1", "author": "Author1", "year": 2005},
        {"title": "Book2", "author": "Author2", "year": 1998},
        {"title": "Book3", "author": "Author3", "year": 2010},
        {"title": "Book4", "author": "Author4", "year": 1995},
    ]

    print("Original list of books:")
    for book in books:
        print(book)

    selection_sort_books(books, key="year")

    print("\nSorted list of books by publication year:")
    for book in books:
        print(book)


def merge_sort_books(books, key='publication_year'):
    if len(books) > 1:
        mid = len(books) // 2
        left_half = books[:mid]
        right_half = books[mid:]

        merge_sort_books(left_half, key)
        merge_sort_books(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                books[k] = left_half[i]
                i += 1
            else:
                books[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            books[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            books[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
if __name__ == "__main__":
    books = [
        {"title": "Book A", "publication_year": 2005},
        {"title": "Book B", "publication_year": 1998},
        {"title": "Book C", "publication_year": 2015},
        {"title": "Book D", "publication_year": 1985},
        {"title": "Book E", "publication_year": 2020},
    ]

    print("Unsorted list of books:")
    for book in books:
        print(book)

    merge_sort_books(books, key='publication_year')

    print("\nSorted list of books by publication year:")
    for book in books:
        print(book)


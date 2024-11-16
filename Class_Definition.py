# Book class definition
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

# Creating Book objects
book1 = Book("Programming Book 1", "Owomuka Jailack", 2021)
book2 = Book("Programming Book  2", "Jane Smith", 2019)

# Displaying book descriptions
print(book1.description())
print(book2.description())


# Function to sort books by year
def sort_books_by_year(books):
    if not books:
        return "No books to sort"
    return sorted(books, key=lambda book: book.year)

# Creating a list of books and sorting
books = [book1, book2]
sorted_books = sort_books_by_year(books)

for book in sorted_books:
    print(book.description())




    # Search for a book by title
while True:
    search_title = input("Enter a book title to search (or type 'exit' to quit): ")
    if search_title.lower() == "exit":
        break
    found = False
    for book in books:
        if book.title.lower() == search_title.lower():
            print(book.description())
            found = True
            break
    if not found:
        print("Book not found!")



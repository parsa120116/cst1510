class Book:
    """A library book that can be borrowed and returned."""

    def __init__(self, title, author, is_available=True):
        """Store the book details; a new book is available by default."""
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrow(self):
        """Borrow the book if it is on the shelf."""
        if self.is_available:
            self.is_available = False
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        """Put the book back on the shelf."""
        if self.is_available:
            print(f"'{self.title}' was not borrowed.")
        else:
            self.is_available = True
            print(f"Thank you for returning '{self.title}'.")

    def __str__(self):
        """Return the book as 'title by author'."""
        return f"{self.title} by {self.author}"


books = [
    Book("1984", "George Orwell"),
    Book("Animal Farm", "George Orwell"),
    Book("The Little Prince", "Antoine de Saint-Exupery"),
    Book("The Blind Owl", "Sadegh Hedayat"),
]

# 1. Borrow a book, then try again
print("--- Borrowing ---")
books[0].borrow()
books[0].borrow()

# 2. Show the books that are on the shelf
print("--- Available books ---")
for book in books:
    if book.is_available:
        print(book)

# 3. Search by author (not case-sensitive)
print("--- Search by author ---")
wanted = input("Enter an author: ").strip()
found = 0
for book in books:
    if book.author.lower() == wanted.lower():
        if book.is_available:
            status = "available"
        else:
            status = "borrowed"
        print(f"{book} ({status})")
        found += 1

if found == 0:
    print(f"No books by {wanted} in the library.")

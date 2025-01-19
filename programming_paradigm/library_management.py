class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            return False  # Book is already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned."""
        if not self._is_checked_out:
            return False  # Book is already available
        self._is_checked_out = False
        return True

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library."""
    
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}'")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned '{title}'")
                return
        print(f"'{title}' is not checked out or does not exist.")

    def list_available_books(self):
        """List all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")

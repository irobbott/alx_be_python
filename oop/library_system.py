class Book:
    """A base class to represent a book."""

    def __init__(self, title, author):
        """Initialize the book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """A class to represent an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize the ebook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """A class to represent a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize the print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the printed book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A class to represent a library."""

    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        """Print details of all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

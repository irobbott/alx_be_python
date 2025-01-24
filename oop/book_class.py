class Book:
    """A class to represent a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Initialize the book with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor method to handle object deletion."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a human-readable string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

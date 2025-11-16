"""Book class for Library Management System"""

class Book:
    """Represents a book in the library"""
    
    book_counter = 1000  # Class variable for unique book IDs
    
    def __init__(self, title, author, isbn):
        """
        Initialize a Book object
        
        Args:
            title (str): Title of the book
            author (str): Author of the book
            isbn (str): ISBN of the book
        """
        self.book_id = Book.book_counter
        Book.book_counter += 1
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_by = None  # Member ID who borrowed this book
    
    def __repr__(self):
        """String representation of Book"""
        status = "Available" if self.is_available else f"Borrowed by Member #{self.borrowed_by}"
        return f"Book(ID: {self.book_id}, Title: '{self.title}', Author: '{self.author}', Status: {status})"
    
    def to_dict(self):
        """Convert book to dictionary for JSON storage"""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "is_available": self.is_available,
            "borrowed_by": self.borrowed_by
        }
    
    @staticmethod
    def from_dict(data):
        """Create Book object from dictionary"""
        book = Book(data["title"], data["author"], data["isbn"])
        book.book_id = data["book_id"]
        book.is_available = data["is_available"]
        book.borrowed_by = data["borrowed_by"]
        # Update counter to avoid ID conflicts
        if data["book_id"] >= Book.book_counter:
            Book.book_counter = data["book_id"] + 1
        return book

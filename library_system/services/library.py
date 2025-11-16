"""Library service class for Library Management System"""

import json
import os
from library_system.models.book import Book
from library_system.models.member import Member
from library_system.models.admin import Admin

class Library:
    """Manages all library operations"""
    
    DATA_DIR = "library_system/data"
    BOOKS_FILE = os.path.join(DATA_DIR, "books.json")
    MEMBERS_FILE = os.path.join(DATA_DIR, "members.json")
    
    def __init__(self):
        """Initialize the Library"""
        self.books = {}  # Dictionary: book_id -> Book object
        self.members = {}  # Dictionary: user_id -> Member/Admin object
        self.current_user = None
        self._ensure_data_dir()
        self.load_data()
    
    def _ensure_data_dir(self):
        """Ensure data directory exists"""
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)
    
    # ==================== BOOK OPERATIONS ====================
    
    def add_book(self, title, author, isbn):
        """
        Add a new book to the library
        
        Args:
            title (str): Title of the book
            author (str): Author of the book
            isbn (str): ISBN of the book
        
        Returns:
            Book object if successful, None otherwise
        """
        try:
            book = Book(title, author, isbn)
            self.books[book.book_id] = book
            self.save_data()
            return book
        except Exception as e:
            print(f"Error adding book: {e}")
            return None
    
    def remove_book(self, book_id):
        """
        Remove a book from the library
        
        Args:
            book_id (int): ID of the book to remove
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if book_id in self.books:
                book = self.books.pop(book_id)
                self.save_data()
                return True
            return False
        except Exception as e:
            print(f"Error removing book: {e}")
            return False
    
    def get_book(self, book_id):
        """
        Get a book by ID
        
        Args:
            book_id (int): ID of the book
        
        Returns:
            Book object or None
        """
        return self.books.get(book_id)
    
    def search_books(self, keyword, search_type="title"):
        """
        Search books by title or author
        
        Args:
            keyword (str): Search keyword
            search_type (str): "title" or "author"
        
        Returns:
            List of matching Book objects
        """
        results = []
        keyword_lower = keyword.lower()
        
        for book in self.books.values():
            if search_type == "title" and keyword_lower in book.title.lower():
                results.append(book)
            elif search_type == "author" and keyword_lower in book.author.lower():
                results.append(book)
        
        return results
    
    def list_all_books(self):
        """
        Get list of all books
        
        Returns:
            List of Book objects
        """
        return list(self.books.values())
    
    def get_available_books(self):
        """
        Get list of available books
        
        Returns:
            List of available Book objects
        """
        return [book for book in self.books.values() if book.is_available]
    
    # ==================== MEMBER OPERATIONS ====================
    
    def add_member(self, name, email, is_admin=False):
        """
        Add a new member to the library
        
        Args:
            name (str): Name of the member
            email (str): Email of the member
            is_admin (bool): Whether this member is an admin
        
        Returns:
            Member/Admin object if successful, None otherwise
        """
        try:
            if is_admin:
                member = Admin(name, email)
            else:
                member = Member(name, email)
            
            self.members[member.user_id] = member
            self.save_data()
            return member
        except Exception as e:
            print(f"Error adding member: {e}")
            return None
    
    def get_member(self, user_id):
        """
        Get a member by ID
        
        Args:
            user_id (int): ID of the member
        
        Returns:
            Member/Admin object or None
        """
        return self.members.get(user_id)
    
    def list_all_members(self):
        """
        Get list of all members
        
        Returns:
            List of Member/Admin objects
        """
        return list(self.members.values())
    
    def authenticate_member(self, user_id):
        """
        Authenticate a member by ID
        
        Args:
            user_id (int): ID of the member
        
        Returns:
            Member/Admin object if found, None otherwise
        """
        if user_id in self.members:
            self.current_user = self.members[user_id]
            return self.current_user
        return None
    
    # ==================== BORROW/RETURN OPERATIONS ====================
    
    def borrow_book(self, member_id, book_id):
        """
        Borrow a book for a member
        
        Args:
            member_id (int): ID of the member
            book_id (int): ID of the book
        
        Returns:
            True if successful, False otherwise
        """
        try:
            member = self.get_member(member_id)
            book = self.get_book(book_id)
            
            if not member:
                print(f"Member {member_id} not found.")
                return False
            
            if not book:
                print(f"Book {book_id} not found.")
                return False
            
            if not book.is_available:
                print(f"Book '{book.title}' is not available.")
                return False
            
            # Update book and member
            book.is_available = False
            book.borrowed_by = member_id
            member.borrow_book(book_id)
            
            self.save_data()
            print(f"✓ {member.name} successfully borrowed '{book.title}'")
            return True
        except Exception as e:
            print(f"Error borrowing book: {e}")
            return False
    
    def return_book(self, member_id, book_id):
        """
        Return a book from a member
        
        Args:
            member_id (int): ID of the member
            book_id (int): ID of the book
        
        Returns:
            True if successful, False otherwise
        """
        try:
            member = self.get_member(member_id)
            book = self.get_book(book_id)
            
            if not member:
                print(f"Member {member_id} not found.")
                return False
            
            if not book:
                print(f"Book {book_id} not found.")
                return False
            
            if book_id not in member.borrowed_books:
                print(f"{member.name} has not borrowed this book.")
                return False
            
            # Update book and member
            book.is_available = True
            book.borrowed_by = None
            member.return_book(book_id)
            
            self.save_data()
            print(f"✓ {member.name} successfully returned '{book.title}'")
            return True
        except Exception as e:
            print(f"Error returning book: {e}")
            return False
    
    # ==================== FILE OPERATIONS ====================
    
    def save_data(self):
        """Save books and members to JSON files"""
        try:
            # Save books
            books_data = {str(book_id): book.to_dict() for book_id, book in self.books.items()}
            with open(self.BOOKS_FILE, 'w') as f:
                json.dump(books_data, f, indent=2)
            
            # Save members
            members_data = {str(user_id): member.to_dict() for user_id, member in self.members.items()}
            with open(self.MEMBERS_FILE, 'w') as f:
                json.dump(members_data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_data(self):
        """Load books and members from JSON files"""
        try:
            # Load books
            if os.path.exists(self.BOOKS_FILE):
                with open(self.BOOKS_FILE, 'r') as f:
                    books_data = json.load(f)
                    for book_id, book_dict in books_data.items():
                        book = Book.from_dict(book_dict)
                        self.books[book.book_id] = book
            
            # Load members
            if os.path.exists(self.MEMBERS_FILE):
                with open(self.MEMBERS_FILE, 'r') as f:
                    members_data = json.load(f)
                    for user_id, member_dict in members_data.items():
                        if member_dict.get("role") == "Admin":
                            member = Admin.from_dict(member_dict)
                        else:
                            member = Member.from_dict(member_dict)
                        self.members[member.user_id] = member
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def clear_all_data(self):
        """Clear all data and reset files"""
        self.books.clear()
        self.members.clear()
        # Reset counters
        Book.book_counter = 1000
        from library_system.models.user import User
        User.user_counter = 1000
        self.save_data()

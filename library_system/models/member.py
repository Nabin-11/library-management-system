"""Member class for Library Management System"""

from library_system.models.user import User

class Member(User):
    """Represents a library member/user"""
    
    def __init__(self, name, email):
        """
        Initialize a Member object
        
        Args:
            name (str): Name of the member
            email (str): Email of the member
        """
        super().__init__(name, email)
        self.borrowed_books = []  # List of book IDs
    
    def get_role(self):
        """Return the role of the user"""
        return "Member"
    
    def borrow_book(self, book_id):
        """
        Add a book to borrowed books list
        
        Args:
            book_id (int): ID of the book to borrow
        """
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            return True
        return False
    
    def return_book(self, book_id):
        """
        Remove a book from borrowed books list
        
        Args:
            book_id (int): ID of the book to return
        """
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False
    
    def view_borrowed_books(self):
        """Return list of borrowed book IDs"""
        return self.borrowed_books.copy()
    
    def display_menu(self):
        """Display member menu options"""
        print("\n" + "="*50)
        print(f"MEMBER MENU - Welcome {self.name}!")
        print("="*50)
        print("1. Search Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View My Borrowed Books")
        print("5. Logout")
        print("="*50)
    
    def __repr__(self):
        """String representation of Member"""
        return f"Member(ID: {self.user_id}, Name: '{self.name}', Borrowed Books: {len(self.borrowed_books)})"
    
    def to_dict(self):
        """Convert member to dictionary for JSON storage"""
        data = super().to_dict()
        data["borrowed_books"] = self.borrowed_books
        return data
    
    @staticmethod
    def from_dict(data):
        """Create Member object from dictionary"""
        member = Member(data["name"], data["email"])
        member.user_id = data["user_id"]
        member.borrowed_books = data.get("borrowed_books", [])
        # Update counter to avoid ID conflicts
        if data["user_id"] >= User.user_counter:
            User.user_counter = data["user_id"] + 1
        return member

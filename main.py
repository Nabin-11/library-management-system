"""Main application for Library Management System"""

from library_system.services.library import Library

class LibraryApp:
    """Main application class for Library Management System"""
    
    def __init__(self):
        """Initialize the application"""
        self.library = Library()
        self.running = True
    
    def clear_screen(self):
        """Clear the terminal screen"""
        import os
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def display_main_menu(self):
        """Display main login menu"""
        print("\n" + "="*50)
        print("LIBRARY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Login as Admin")
        print("2. Login as Member")
        print("3. Create New Member Account")
        print("4. Exit")
        print("="*50)
    
    def create_member_account(self):
        """Handle new member registration"""
        print("\n--- Create New Member Account ---")
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        
        if not name or not email:
            print("❌ Name and email cannot be empty.")
            return
        
        member = self.library.add_member(name, email, is_admin=False)
        if member:
            print(f"\n✓ Account created successfully!")
            print(f"Your Member ID: {member.user_id}")
        else:
            print("❌ Error creating account.")
    
    def login_admin(self):
        """Handle admin login"""
        print("\n--- Admin Login ---")
        try:
            admin_id = int(input("Enter Admin ID: "))
            admin = self.library.authenticate_member(admin_id)
            
            if admin and admin.get_role() == "Admin":
                self.admin_menu(admin)
            else:
                print("❌ Invalid Admin ID or user is not an admin.")
        except ValueError:
            print("❌ Please enter a valid ID.")
    
    def login_member(self):
        """Handle member login"""
        print("\n--- Member Login ---")
        try:
            member_id = int(input("Enter Member ID: "))
            member = self.library.authenticate_member(member_id)
            
            if member and member.get_role() in ["Member", "Admin"]:
                if member.get_role() == "Admin":
                    self.admin_menu(member)
                else:
                    self.member_menu(member)
            else:
                print("❌ Invalid Member ID.")
        except ValueError:
            print("❌ Please enter a valid ID.")
    
    def admin_menu(self, admin):
        """Display and handle admin menu"""
        while True:
            admin.display_menu()
            choice = input("Select an option: ").strip()
            
            if choice == "1":
                self.add_book_admin(admin)
            elif choice == "2":
                self.remove_book_admin(admin)
            elif choice == "3":
                self.view_all_books()
            elif choice == "4":
                self.search_book()
            elif choice == "5":
                self.view_all_members()
            elif choice == "6":
                print(f"\n✓ Goodbye, {admin.name}!")
                break
            else:
                print("❌ Invalid option. Please try again.")
    
    def member_menu(self, member):
        """Display and handle member menu"""
        while True:
            member.display_menu()
            choice = input("Select an option: ").strip()
            
            if choice == "1":
                self.search_book()
            elif choice == "2":
                self.borrow_book_member(member)
            elif choice == "3":
                self.return_book_member(member)
            elif choice == "4":
                self.view_borrowed_books(member)
            elif choice == "5":
                print(f"\n✓ Goodbye, {member.name}!")
                break
            else:
                print("❌ Invalid option. Please try again.")
    
    def add_book_admin(self, admin):
        """Add a new book - Admin only"""
        print("\n--- Add New Book ---")
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        isbn = input("Enter ISBN: ").strip()
        
        if not title or not author or not isbn:
            print("❌ All fields are required.")
            return
        
        book = self.library.add_book(title, author, isbn)
        if book:
            print(f"\n✓ Book added successfully!")
            print(f"Book ID: {book.book_id}")
        else:
            print("❌ Error adding book.")
    
    def remove_book_admin(self, admin):
        """Remove a book - Admin only"""
        print("\n--- Remove Book ---")
        try:
            book_id = int(input("Enter Book ID to remove: "))
            book = self.library.get_book(book_id)
            
            if not book:
                print("❌ Book not found.")
                return
            
            if self.library.remove_book(book_id):
                print(f"✓ Book '{book.title}' removed successfully.")
            else:
                print("❌ Error removing book.")
        except ValueError:
            print("❌ Please enter a valid book ID.")
    
    def search_book(self):
        """Search for books"""
        print("\n--- Search Books ---")
        print("1. Search by Title")
        print("2. Search by Author")
        choice = input("Select search type: ").strip()
        
        keyword = input("Enter search keyword: ").strip()
        
        if choice == "1":
            results = self.library.search_books(keyword, "title")
        elif choice == "2":
            results = self.library.search_books(keyword, "author")
        else:
            print("❌ Invalid option.")
            return
        
        if results:
            print(f"\n✓ Found {len(results)} result(s):\n")
            for book in results:
                print(book)
        else:
            print("❌ No books found.")
    
    def view_all_books(self):
        """View all books in the library"""
        books = self.library.list_all_books()
        
        if not books:
            print("❌ No books in the library.")
            return
        
        print(f"\n--- All Books ({len(books)} total) ---\n")
        for book in books:
            print(book)
    
    def view_all_members(self):
        """View all members - Admin only"""
        members = self.library.list_all_members()
        
        if not members:
            print("❌ No members in the system.")
            return
        
        print(f"\n--- All Members ({len(members)} total) ---\n")
        for member in members:
            print(member)
    
    def borrow_book_member(self, member):
        """Borrow a book - Member only"""
        print("\n--- Borrow Book ---")
        
        # Show available books
        available = self.library.get_available_books()
        if not available:
            print("❌ No books available to borrow.")
            return
        
        print("Available books:")
        for book in available:
            print(f"ID: {book.book_id} - {book.title} by {book.author}")
        
        try:
            book_id = int(input("\nEnter Book ID to borrow: "))
            self.library.borrow_book(member.user_id, book_id)
        except ValueError:
            print("❌ Please enter a valid book ID.")
    
    def return_book_member(self, member):
        """Return a book - Member only"""
        print("\n--- Return Book ---")
        
        borrowed = member.view_borrowed_books()
        if not borrowed:
            print("❌ You have no borrowed books.")
            return
        
        print("Your borrowed books:")
        for book_id in borrowed:
            book = self.library.get_book(book_id)
            if book:
                print(f"ID: {book.book_id} - {book.title}")
        
        try:
            book_id = int(input("\nEnter Book ID to return: "))
            self.library.return_book(member.user_id, book_id)
        except ValueError:
            print("❌ Please enter a valid book ID.")
    
    def view_borrowed_books(self, member):
        """View member's borrowed books"""
        borrowed = member.view_borrowed_books()
        
        if not borrowed:
            print("\n❌ You have not borrowed any books.")
            return
        
        print(f"\n--- Your Borrowed Books ({len(borrowed)} total) ---\n")
        for book_id in borrowed:
            book = self.library.get_book(book_id)
            if book:
                print(f"ID: {book.book_id} - '{book.title}' by {book.author}")
    
    def setup_demo_data(self):
        """Setup demo data for testing"""
        print("Setting up demo data...")
        
        # Add some books
        self.library.add_book("Python Programming", "Guido van Rossum", "978-0134685991")
        self.library.add_book("Clean Code", "Robert C. Martin", "978-0132350884")
        self.library.add_book("Design Patterns", "Gang of Four", "978-0201633610")
        
        # Add admin and members
        admin = self.library.add_member("Admin User", "admin@library.com", is_admin=True)
        member1 = self.library.add_member("John Doe", "john@example.com", is_admin=False)
        member2 = self.library.add_member("Jane Smith", "jane@example.com", is_admin=False)
        
        print(f"✓ Demo data created!")
        print(f"Admin ID: {admin.user_id}")
        print(f"Member 1 ID: {member1.user_id}")
        print(f"Member 2 ID: {member2.user_id}")
    
    def run(self):
        """Run the main application loop"""
        print("\n" + "="*50)
        print("Welcome to Library Management System!")
        print("="*50)
        
        # Check if this is first run
        if not self.library.list_all_members():
            print("\nThis appears to be your first run.")
            print("Setting up demo data for testing...\n")
            self.setup_demo_data()
        
        while self.running:
            self.display_main_menu()
            choice = input("Select an option: ").strip()
            
            if choice == "1":
                self.login_admin()
            elif choice == "2":
                self.login_member()
            elif choice == "3":
                self.create_member_account()
            elif choice == "4":
                print("\n✓ Thank you for using Library Management System!")
                self.running = False
            else:
                print("❌ Invalid option. Please try again.")

def main():
    """Main entry point"""
    app = LibraryApp()
    app.run()

if __name__ == "__main__":
    main()

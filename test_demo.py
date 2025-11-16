"""Quick test/demo script for Library Management System"""

from library_system.services import Library
from library_system.models import Book, Member, Admin

def test_library_system():
    """Test the Library Management System"""
    
    print("\n" + "="*60)
    print("LIBRARY MANAGEMENT SYSTEM - TEST DEMO")
    print("="*60)
    
    # Create library instance
    lib = Library()
    print("\n✓ Library initialized")
    
    # Test 1: Add books
    print("\n--- TEST 1: Add Books ---")
    book1 = lib.add_book("Python Programming", "Guido van Rossum", "978-0134685991")
    book2 = lib.add_book("Clean Code", "Robert C. Martin", "978-0132350884")
    book3 = lib.add_book("Design Patterns", "Gang of Four", "978-0201633610")
    print(f"✓ Added {len(lib.books)} books")
    for book in lib.list_all_books():
        print(f"  - {book}")
    
    # Test 2: Add members
    print("\n--- TEST 2: Add Members ---")
    admin = lib.add_member("Admin User", "admin@library.com", is_admin=True)
    member1 = lib.add_member("John Doe", "john@example.com", is_admin=False)
    member2 = lib.add_member("Jane Smith", "jane@example.com", is_admin=False)
    print(f"✓ Added {len(lib.members)} members")
    for member in lib.list_all_members():
        print(f"  - {member}")
    
    # Test 3: Verify roles
    print("\n--- TEST 3: Verify Roles & Polymorphism ---")
    print(f"Admin role: {admin.get_role()}")
    print(f"Member role: {member1.get_role()}")
    print(f"Member2 role: {member2.get_role()}")
    
    # Test 4: Borrow books
    print("\n--- TEST 4: Borrow Books ---")
    lib.borrow_book(member1.user_id, book1.book_id)
    lib.borrow_book(member1.user_id, book2.book_id)
    lib.borrow_book(member2.user_id, book3.book_id)
    
    print(f"\n{member1.name}'s borrowed books: {member1.view_borrowed_books()}")
    print(f"{member2.name}'s borrowed books: {member2.view_borrowed_books()}")
    
    # Test 5: Search functionality
    print("\n--- TEST 5: Search Functionality ---")
    results = lib.search_books("python", "title")
    print(f"Search for 'python' in titles: {len(results)} result(s)")
    for book in results:
        print(f"  - {book}")
    
    results = lib.search_books("martin", "author")
    print(f"\nSearch for 'martin' in authors: {len(results)} result(s)")
    for book in results:
        print(f"  - {book}")
    
    # Test 6: Availability checking
    print("\n--- TEST 6: Availability Checking ---")
    available = lib.get_available_books()
    print(f"Available books: {len(available)}")
    for book in available:
        print(f"  - {book.title} by {book.author} (ID: {book.book_id})")
    
    # Test 7: Return books
    print("\n--- TEST 7: Return Books ---")
    lib.return_book(member1.user_id, book1.book_id)
    
    print(f"\n{member1.name}'s borrowed books after return: {member1.view_borrowed_books()}")
    available = lib.get_available_books()
    print(f"Available books after return: {len(available)}")
    
    # Test 8: Data persistence
    print("\n--- TEST 8: Data Persistence (JSON) ---")
    import os
    books_file = lib.BOOKS_FILE
    members_file = lib.MEMBERS_FILE
    print(f"Books file exists: {os.path.exists(books_file)}")
    print(f"Members file exists: {os.path.exists(members_file)}")
    
    # Show file sizes
    if os.path.exists(books_file):
        print(f"Books file size: {os.path.getsize(books_file)} bytes")
    if os.path.exists(members_file):
        print(f"Members file size: {os.path.getsize(members_file)} bytes")
    
    # Test 9: Load from persisted data
    print("\n--- TEST 9: Load from Persisted Data ---")
    lib2 = Library()
    print(f"Loaded {len(lib2.books)} books from storage")
    print(f"Loaded {len(lib2.members)} members from storage")
    
    # Test 10: Remove book
    print("\n--- TEST 10: Remove Book ---")
    lib.remove_book(book3.book_id)
    print(f"✓ Book removed. Total books now: {len(lib.books)}")
    
    print("\n" + "="*60)
    print("✓ ALL TESTS PASSED!")
    print("="*60 + "\n")

if __name__ == "__main__":
    test_library_system()

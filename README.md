# Library Management System - OOP Python Project

## 📚 Overview

A comprehensive Library Management System built in Python to demonstrate Object-Oriented Programming (OOP) concepts from basic to advanced levels. This project implements a complete library system where users can borrow/return books and admins can manage books and members.

## 🎯 Project Phases

### Phase 1: Basic OOP ✓
- Book class with attributes (title, author, ISBN, availability)
- User class hierarchy (User → Member → Admin)
- Basic add/list operations
- Static book and user ID generation

### Phase 2: Intermediate OOP ✓
- Borrow & return system with availability checking
- Search and filter functionality (by title/author)
- Exception handling throughout
- File-based storage using JSON (books.json, members.json)
- Polymorphic methods in class hierarchy

### Phase 3: Advanced OOP ✓
- Abstract Base Classes (ABC) for User
- Admin inherits from Member (inheritance chain)
- Polymorphic display_menu() and get_role() methods
- Modular package structure (models, services)
- Role-based access control
- Comprehensive menu system

## 🏗️ Project Structure

```
library-management-system/
├── library_system/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── book.py          # Book class
│   │   ├── user.py          # Abstract User class (ABC)
│   │   ├── member.py        # Member class (inherits from User)
│   │   └── admin.py         # Admin class (inherits from Member)
│   ├── services/
│   │   ├── __init__.py
│   │   └── library.py       # Library service class (all operations)
│   └── data/
│       ├── books.json       # Persisted book data
│       └── members.json     # Persisted member data
├── main.py                  # Main application entry point
├── README.md                # This file
└── fow_map.txt              # Project roadmap
```

## 📚 OOP Concepts Demonstrated

### 1. **Classes & Objects**
- `Book` class for library items
- `Member` and `Admin` for users
- `Library` service class for operations

### 2. **Constructor & Initialization**
```python
def __init__(self, name, email):
    self.user_id = User.user_counter
    User.user_counter += 1
```

### 3. **Encapsulation**
- Private data (`_ensure_data_dir()`)
- Controlled access through methods
- Data hiding with properties

### 4. **Inheritance**
```
User (ABC - Abstract Base Class)
├── Member
│   └── Admin
```

### 5. **Polymorphism**
- Abstract methods: `get_role()`, `display_menu()`
- Subclasses implement their own versions
- Different behavior for Admin vs Member

### 6. **Abstraction (ABC)**
```python
from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def display_menu(self):
        pass
```

### 7. **Static Methods & Class Variables**
```python
class Book:
    book_counter = 1000  # Class variable
    
    @staticmethod
    def from_dict(data):  # Static method
        return Book(...)
```

### 8. **Exception Handling**
```python
try:
    book = self.get_book(book_id)
    if not book:
        raise ValueError("Book not found")
except Exception as e:
    print(f"Error: {e}")
```

### 9. **File Handling (JSON)**
- Loading data: `load_data()` → Deserialize JSON → Create objects
- Saving data: `save_data()` → Serialize objects → Store JSON
- Persistence across sessions

### 10. **Modular Programming**
- Packages: `models/`, `services/`
- Separation of concerns
- Reusable components
- `__init__.py` for package exports

## 🚀 Features

### Admin Features
✓ Add new books to the library  
✓ Remove books from the library  
✓ View all books  
✓ Search books by title/author  
✓ View all registered members  

### Member Features
✓ Search books by title or author  
✓ Borrow available books  
✓ Return borrowed books  
✓ View personal borrowed books list  
✓ Create new account (self-registration)  

### System Features
✓ Role-based access control (Admin vs Member)  
✓ Unique ID generation for books and users  
✓ Automatic data persistence (JSON)  
✓ Availability checking  
✓ Exception handling & error messages  

## 🎮 How to Run

### 1. Navigate to project directory
```bash
cd /Users/nabinpandey/Desktop/git_project/library-management-system
```

### 2. Run the application
```bash
python3 main.py
```

### 3. First Run
The system automatically creates demo data:
- **Admin ID**: 1000 (Admin User)
- **Member 1 ID**: 1001 (John Doe)
- **Member 2 ID**: 1002 (Jane Smith)
- **Books**: 3 sample books

### 4. Login Options
- **Admin**: Enter ID 1000 (or create new)
- **Member**: Enter ID 1001, 1002 (or create new)

## 📝 Demo Workflow

### As Admin:
1. Login with Admin ID (1000)
2. View all books
3. Add a new book
4. View all members
5. Logout

### As Member:
1. Login with Member ID (1001)
2. Search for books
3. Borrow a book
4. View borrowed books
5. Return a book
6. Logout

## 💾 Data Persistence

### books.json
```json
{
  "1000": {
    "book_id": 1000,
    "title": "Python Programming",
    "author": "Guido van Rossum",
    "isbn": "978-0134685991",
    "is_available": true,
    "borrowed_by": null
  }
}
```

### members.json
```json
{
  "1000": {
    "user_id": 1000,
    "name": "Admin User",
    "email": "admin@library.com",
    "role": "Admin",
    "borrowed_books": []
  }
}
```

## 🔄 System Flowchart

```
START
  ↓
Load Data (JSON)
  ↓
Display Main Menu
  ↓
┌─────────────────┬──────────────────┐
│                 │                  │
v                 v                  v
Admin Login    Member Login      Create Account
  │               │                  │
  v               v                  v
Admin Menu    Member Menu        Save New Member
  │               │
  v               v
Perform Op    Perform Op
  │               │
  v               v
Save Data     Save Data
  │               │
  └─────────┬─────┘
            │
            v
        Exit / Repeat
            ↓
          END
```

## 🧪 Testing

### Test Scenarios

1. **Create New Member**
   - Create account with name and email
   - Verify unique ID assignment

2. **Borrow Book**
   - Check availability
   - Update member's borrowed list
   - Verify data persists

3. **Return Book**
   - Verify member borrowed the book
   - Update availability
   - Verify data persists

4. **Search Functionality**
   - Search by title (case-insensitive)
   - Search by author (case-insensitive)
   - Return correct results

## 📦 Dependencies

- Python 3.7+
- No external packages required (uses only standard library)
- Uses: `abc`, `json`, `os`

## 🎓 Learning Outcomes

After completing this project, you will understand:

1. ✅ How to design classes and objects
2. ✅ Inheritance chains and polymorphism
3. ✅ Abstract Base Classes (ABC)
4. ✅ Encapsulation and data hiding
5. ✅ Exception handling and validation
6. ✅ File I/O and data persistence
7. ✅ JSON serialization/deserialization
8. ✅ Modular programming and packages
9. ✅ Building CLI applications
10. ✅ Testing and debugging OOP code

## 🔧 Future Enhancements

- [ ] Database integration (SQLite/MySQL)
- [ ] User authentication (password hashing)
- [ ] Overdue book tracking
- [ ] Book ratings and reviews
- [ ] Fine/penalty system
- [ ] Web UI (Flask/Django)
- [ ] REST API
- [ ] Unit tests
- [ ] Logging system
- [ ] Configuration file support

## 📄 License

This project is for educational purposes.

## 👨‍💻 Author

**Nabin Pandey**

---

**Happy Learning! 🎉**
library

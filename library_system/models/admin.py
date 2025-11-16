"""Admin class for Library Management System"""

from library_system.models.member import Member

class Admin(Member):
    """Represents an admin user with special privileges"""
    
    def __init__(self, name, email):
        """
        Initialize an Admin object
        
        Args:
            name (str): Name of the admin
            email (str): Email of the admin
        """
        super().__init__(name, email)
    
    def get_role(self):
        """Return the role of the user"""
        return "Admin"
    
    def display_menu(self):
        """Display admin menu options"""
        print("\n" + "="*50)
        print(f"ADMIN MENU - Welcome {self.name}!")
        print("="*50)
        print("1. Add Book")
        print("2. Remove Book")
        print("3. View All Books")
        print("4. Search Book")
        print("5. View All Members")
        print("6. Logout")
        print("="*50)
    
    def __repr__(self):
        """String representation of Admin"""
        return f"Admin(ID: {self.user_id}, Name: '{self.name}')"
    
    def to_dict(self):
        """Convert admin to dictionary for JSON storage"""
        data = super().to_dict()
        return data
    
    @staticmethod
    def from_dict(data):
        """Create Admin object from dictionary"""
        admin = Admin(data["name"], data["email"])
        admin.user_id = data["user_id"]
        admin.borrowed_books = data.get("borrowed_books", [])
        # Update counter to avoid ID conflicts
        from library_system.models.user import User
        if data["user_id"] >= User.user_counter:
            User.user_counter = data["user_id"] + 1
        return admin

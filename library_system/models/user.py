"""Abstract User class for Library Management System"""

from abc import ABC, abstractmethod

class User(ABC):
    """Abstract base class for all users in the system"""
    
    user_counter = 1000  # Class variable for unique user IDs
    
    def __init__(self, name, email):
        """
        Initialize a User object
        
        Args:
            name (str): Name of the user
            email (str): Email of the user
        """
        self.user_id = User.user_counter
        User.user_counter += 1
        self.name = name
        self.email = email
    
    @abstractmethod
    def get_role(self):
        """Return the role of the user - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def display_menu(self):
        """Display menu options - must be implemented by subclasses"""
        pass
    
    def __repr__(self):
        """String representation of User"""
        return f"{self.__class__.__name__}(ID: {self.user_id}, Name: '{self.name}', Email: '{self.email}')"
    
    def to_dict(self):
        """Convert user to dictionary for JSON storage"""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "role": self.get_role()
        }

class admin_menu():
    def __init__(self):
        self.title = []
        self.id = []
    def add_book(self, book_title, book_id):
        self.title.append(book_title)
        self.id.append(book_id)
    def remove_book(self, book_id):
        if book_id in self.id:
            index = self.id.index(book_id)
            print(f"{self.id.pop(index)} {self.title[index]} removed successfully.")
        else:
            print("Book ID not found.")
    def list_books(self):
        for i in range(len(self.id)):
            print(f"Book ID: {self.id[i]}, Title: {self.title[i]}")

        
       
        
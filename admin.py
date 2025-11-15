class admin_menu():
    def add_book(self, book_title, book_id):
        self.title = []
        self.id = []
        self.title.append(book_title)
        self.id.append(book_id)
    def remove_book(self, book_id):
        if book_id in self.id:
            index = self.id.index(book_id)
            print(f"{self.id.pop(index)} {self.title[index]} removed successfully.")
        else:
            print("Book ID not found.")

        
       
        
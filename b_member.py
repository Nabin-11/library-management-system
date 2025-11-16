import admin as amn
class member_menu():
    def __init__(self):
        self.admin = amn.admin_menu()
    def search_book(self, book_title="none", book_id=0):
        if book_id in self.admin.id or book_title in self.admin.title:
            print(f"Book Found: {book_id} - {book_title}")
        else:
            print("Book not found.")
    def book_borrow(self, book_id,member_name, member_id):
        if book_id in self.admin.id:
            index = self.admin.id.index(book_id)
            print(f"""Book-details 
                   ID: {book_id} 
                   Name : {self.admin.title[index]}
                   Borrowed by 
                   Name : {member_name} 
                   ID: {member_id}""")
            self.admin.id.remove(book_id)
            self.admin.title.remove(self.admin.title[index])
        else:
            print("Book ID not found, cannot borrow.")
    
book = amn.admin_menu()
book.add_book("Python Programming", 101)
nabin = member_menu()
nabin.admin = book
nabin.book_borrow(101, "Nabin Pandey", 1)
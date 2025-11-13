class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False
        
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies}/{self.total_copies} available)"
    
    
class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrow_books = []

    def borrow_book(self, book):
        self.borrow_books.append(book)

    def return_book(self, book):
        if book in self.borrow_books:
            self.borrow_books.remove(book)

    def __str__(self):
        return f"{self.name} ({self.email})"



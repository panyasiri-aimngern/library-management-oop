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
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book_id, title, author, total_copies):
        book = Book(book_id, title, author, total_copies)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def add_member(self, member_id, name, email):
        member = Member(member_id, name, email)
        self.members.append(member)
        print(f"Member '{name}' registered successfully!")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print(f"Error: Member {member_id} not found!")
            return False
        if not book:
            print(f"Error: Book {book_id} not found!")
            return False

        if len(member.borrow_books) >= 3:
            print(f"Error: {member.name} has reached the borrowing limit!")
            return False

        if not book.borrow():
            print(f"Error: '{book.title}' is not available!")
            return False

        member.borrow_book(book)
        print(f"{member.name} borrowed '{book.title}'")
        return True

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member or not book:
            print("Error: Member or Book not found!")
            return False

        if book not in member.borrow_books:
            print(f"Error: {member.name} did not borrow '{book.title}'!")
            return False

        member.return_book(book)
        book.return_book()
        print(f"{member.name} returned '{book.title}'")
        return True

    def display_available_books(self):
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(book)

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if not member:
            print(f"Error: Member {member_id} not found!")
            return

        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrow_books:
            print("No books currently borrowed.")
        else:
            for book in member.borrow_books:
                print(f"- {book.title} by {book.author}")

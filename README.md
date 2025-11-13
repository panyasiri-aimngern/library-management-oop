# Library Management System (OOP)


## Project Overview

This is a Python project that demonstrates how to implement a Library Management System using object-oriented programming (OOP). The user will be able to process book and member management, borrow and return books, and deal with edge cases, such as the borrowing of books that were not available or the limit of borrowed books. The key features include:

- Adding books and members
- Borrowing and returning books
- Displaying available books and member information
- Handling edge cases for invalid operations


## Project Structure

The project contains
- 'README.md' : This file which is project overview.
- procedural_version/
    - 'library_procedural.py' : Original procedural library system
    - 'test_procedural.py' : Tests for procedural version
- oop_solution/
    - 'library_oop.py' : Object-oriented implementation
    - 'test_oop.py' : Comprehensive tests for OOP version


## Design Overview

### 'Book' Class
Purpose: Represents a book in the library.

Attributes
- 'book_id' : Unique book identifier
- 'title' : Title of the book
- 'author' : Author of the book
- 'total_copies' : Total number of copies in the library
- 'available_copies' : Currently available copies

Methods
- '__init__(self, book_id, title, author, total_copies)': Initializes the attributes.  
- 'borrow()' : Decreases available copies by 1 if possible.
- 'return_book()' : Increases available copies by 1.
- '__str__()' : Returns a readable string representation of the book.

### 'Member' Class
Purpose: Represents a library member.

Attributes
- 'Member_id' : Unique member identifier
- 'name' : Member’s name
- 'email' : Member’s email address
- 'borrow_books' : List of Book objects currently borrowed

Methods
- '__init__(self, member_id, name, email)': Initializes the attributes.
- 'borrow_book(book)' : Adds a book to borrowed list if under limit.
- 'return_book(book)' : Removes a book from borrowed list.
- '__str__()' : Returns a readable string representation of the member.

### 'Library' Class
Purpose: Manages collections of books and members and handles library operations.

Attributes
- 'books' : List of all 'Book' objects
- 'members' : List of all 'Member' objects

Methods
- '__init__(self)': Initializes the attributes.
- 'add_book(id, title, author, copies)' : Adds a new book.
- 'add_member(member_id, name, email)' : Registers a new member.
- 'borrow_book(member_id, book_id)' : Allows a member to borrow a book.
- 'return_book(member_id, book_id)' : Allows a member to return a book.
- 'find_book(book_id)' : Finds a book by ID.
- 'find_member(member_id)' : Finds a member by ID.
- 'display_available_books()' : Shows all books with available copies.
- 'display_member_books(member_id)' : Shows books borrowed by a member.


## Testing

The project includes a comprehensive test suite (test_oop.py) covering:

Basic Operations
- Adding books and members
- Borrowing and returning books
- Displaying books and member information

Edge Cases
- Borrowing unavailable books
- Exceeding borrowing limit
- Returning books not borrowed
- Handling non-existent books or members


## How to test and run the code

1. Prepare the project folder and ensure all required files are included.
2. Open 'test_oop.py' and run the file.
3. Verify the output matches expected results for all operations and edge cases.
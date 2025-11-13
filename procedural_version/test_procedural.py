from library_procedural import *

# Test adding books
def test_books():
    print("\n--- Test Books ---")
    add_book(1, "History of Kasetsart", "Eric", 10)
    add_book(2, "Com-Eng and Com-Sci", "Nancy", 3)
    display_available_books()

# Test adding members
def test_members():
    print("\n--- Test Members ---")
    add_member(1, "Alice", "alice@mail.com")
    add_member(2, "Bob", "bob@mail.com")
    display_member_books(1)
    display_member_books(2)

# Test borrowing and returning books
def test_borrow_return():
    print("\n--- Test Borrowing and Returning ---")

    #Borrowing
    borrow_book(1, 2)
    borrow_book(2, 1)
    display_available_books()
    display_member_books(1)
    display_member_books(2)

    # Returning
    return_book(1, 2)
    display_available_books()
    display_member_books(1)
    display_member_books(2)

# Test edge cases
def test_edge_cases():
    print("\n--- Test Edge Cases ---")
    # Non-existent book/member
    borrow_book(1, 999)
    borrow_book(999, 1)

    # Returning a book not borrowed
    return_book(2, 2)

    # Borrowing a book until 0 copies left
    print("\nBorrowing Book ID 2 until no copies left:")
    add_book(3, "Python Programming", "John", 2)
    borrow_book(1, 3)
    borrow_book(2, 3)
    borrow_book(1, 3)
    display_available_books()


if __name__ == "__main__":
    test_books()
    test_members()
    test_borrow_return()
    test_edge_cases()

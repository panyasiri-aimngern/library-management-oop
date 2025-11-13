from library_oop import Book

# test cases for class Book
def test_book_class():
    print("=" * 60)
    print("TESTING BOOK CLASS")
    print("=" * 60)

    book = Book(1, "Python Crash Course", "Eric Matthes", 3)
    print(f"Created book: {book}")

    # Test borrow
    print("\n--- TEST 1: Borrowing Books ---")
    result1 = book.borrow()
    result2 = book.borrow()
    result3 = book.borrow()
    result4 = book.borrow()
    print(f"Borrow results: {result1}, {result2}, {result3}, {result4}")
    print(f"After borrowing: {book.available_copies} copies left")

    # Test return_book
    print("\n--- TEST 2: Returning Books ---")
    result5 = book.return_book()
    print(f"Return result: {result5}")
    print(f"After returning: {book.available_copies} copies left")

    # Test returning book when it's full)
    print("\n--- TEST 3: Returning More Than Total ---")
    book.return_book()
    book.return_book()
    result6 = book.return_book()
    print(f"Return result (over limit): {result6}")
    print(f"Final book state: {book}")

    print("\n" + "=" * 60)
    print("TEST BOOK CLASS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_book_class()

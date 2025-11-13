from library_oop import Book, Member

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

# test cases for class Member
def test_member_class():
    print("\n" + "=" * 60)
    print("TESTING MEMBER CLASS")
    print("=" * 60)

    book1 = Book(1, "Python Crash Course", "Eric Matthes", 2)
    book2 = Book(2, "Clean Code", "Robert Martin", 1)
    book3 = Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)

    member = Member(101, "Alice Smith", "alice@email.com")
    print(f"Created member: {member}")

    #test borrow books
    print("\n--- TEST 1: Borrowing Books ---")
    member.borrow_book(book1)
    member.borrow_book(book2)
    member.borrow_book(book3)
    extra_book = Book(4, "Design Patterns", "Gang of Four", 1)
    member.borrow_book(extra_book)
    print(f"{member.name} has borrowed {len(member.borrow_books)} books:")
    for b in member.borrow_books:
        print(f"- {b}")

    #test return books
    print("\n--- TEST 2: Returning Books ---")
    member.return_book(book2)
    print(f"{member.name} has borrowed {len(member.borrow_books)} books after returning one:")
    for b in member.borrow_books:
        print(f"- {b}")

    # test return a book that is not borrowed
    print("\n--- TEST 3: Returning a Book Not Borrowed ---")
    member.return_book(Book(5, "Nonexistent Book", "Unknown", 1))
    print("\nFinal borrowed books:")
    for b in member.borrow_books:
        print(f"- {b}")

    print("\n" + "=" * 60)
    print("TEST MEMBER CLASS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_book_class()
    test_member_class()
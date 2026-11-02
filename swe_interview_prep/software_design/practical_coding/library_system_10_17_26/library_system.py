"""
Library System Practical Implementation
By: Nayeel Imtiaz
Date: 10-17-26
Time Limit: 30 minutes

Task:
    Library Book Lending System
    Difficulty: Medium · Python or Java · Implementation-focused
    Design and implement an in-memory library system that manages physical book copies, members, and borrowing operations.

    Functional requirements
    1. Add books: Register books with a unique ISBN, title, and author. A book may have multiple physical copies.
    2. Register members: Each member has a unique ID and name.
    3. Borrow a book: A member can borrow an available copy by ISBN.
    4. Return a book: A member can return a copy they previously borrowed.
    5. Check availability: Query how many copies of a particular book are currently available.
    6. Borrowing limit: Each member can have at most 3 active loans.

    Business rules
    - A physical copy cannot be borrowed by multiple members simultaneously.
    - A member cannot return a copy they did not borrow.
    - Borrowing fails if no copies are available.
    - Invalid operations should fail gracefully.
    - The system should preserve a consistent state after failed operations.

    Expected API
    ```
    library = Library()

    library.add_book("978-123", "Clean Code", "Robert Martin", 2)
    library.register_member("M1", "Alice")
    library.register_member("M2", "Bob")

    copy1 = library.borrow_book("M1", "978-123")
    copy2 = library.borrow_book("M2", "978-123")

    assert library.available_copies("978-123") == 0

    library.return_book("M1", copy1)
    assert library.available_copies("978-123") == 1
    ```

    You decide what borrow_book() returns and how failures are represented.

    Scope
    No database, UI, network calls, authentication, or concurrency handling required. Focus on a clean, working implementation with basic tests.

Reflection:
"""

from dataclasses import dataclass
from enum import Enum, auto


class LibrarySystemCodes(Enum):
    NEW_BOOK_ADDED = auto()
    MORE_COPIES_ADDED = auto()
    NEW_MEMBER_ADDED = auto()
    MEMBER_ALREADY_EXISTS = auto()
    BORROW_SUCCESSFUL = auto()
    BORROW_UNSUCCESSFUL = auto()
    RETURN_SUCCESSFUL = auto()
    RETURN_UNSUCCESSFUL = auto()


@dataclass
class Book:
    isbn: str
    title: str
    author: str


@dataclass
class BookCopy:
    copy_id: int
    isbn: str
    borrower_id: str | None = None


@dataclass
class Member:
    member_id: str
    name: str


class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
        self.copies: dict[int, BookCopy] = {}
        self.next_copy_id = 1

    def add_book(self, isbn: str, title: str, author: str, number_of_copies: int) -> bool:
        if number_of_copies <= 0:
            return False

        if isbn not in self.books:
            self.books[isbn] = Book(isbn, title, author)

        for _ in range(number_of_copies):
            self.copies[self.next_copy_id] = BookCopy(self.next_copy_id, isbn)
            self.next_copy_id += 1

        return True

    def register_member(self, member_id: str, name) -> bool:
        if member_id in self.members:
            return False

        else:
            self.members[member_id] = Member(member_id, name)
            return True

    def borrow_book(self, member_id: str, isbn: str) -> int | None:
        if (
            member_id in self.members
            and self.active_loans(member_id) < 3
        ):
            for copy_id, book_copy in self.copies.items():
                if book_copy.isbn == isbn and book_copy.borrower_id is None:
                    book_copy.borrower_id = member_id
                    return copy_id

        return None

    def return_book(self, member_id: str, copy_id: int) -> bool:
        if (
            member_id in self.members
            and copy_id in self.copies
            and self.copies[copy_id].borrower_id == member_id
        ):
            self.copies[copy_id].borrower_id = None
            return True

        return False

    def available_copies(self, isbn: str) -> int:
        number_of_available_copies = 0
        for _, book_copy in self.copies.items():
            if book_copy.isbn == isbn and book_copy.borrower_id is None:
                number_of_available_copies += 1
        return number_of_available_copies

    def active_loans(self, member_id: str) -> int:
        number_of_loans = 0
        for _, book_copy in self.copies.items():
            if book_copy.borrower_id and book_copy.borrower_id == member_id:
                number_of_loans += 1
        return number_of_loans


def main():
    library = Library()

    print("Add 2 copies of Clean Code by Robert Martin.")
    print(library.add_book("978-123", "Clean Code", "Robert Martin", 2))
    print()

    print("Add 1 more copy of Clean Code by Robert Martin.")
    print(library.add_book("978-123", "Clean Code", "Robert Martin", 1))
    print()
    assert library.available_copies("978-123") == 3

    print("Add 2 Members: Alice and Bob.")
    print(library.register_member("M1", "Alice"))
    print(library.register_member("M2", "Bob"))
    print()

    print("M1 and M2 borrows separate copies of same book:")
    copy1 = library.borrow_book("M1", "978-123")
    copy2 = library.borrow_book("M2", "978-123")
    print(copy1)
    print(copy2)
    print()

    assert copy1 is not None
    assert copy2 is not None
    assert copy1 != copy2

    assert library.active_loans("M1") == 1
    assert library.active_loans("M2") == 1

    assert library.available_copies("978-123") == 1

    print("M1 returns \"Clean Code\"")
    return_copy1 = library.return_book("M1", copy1)
    print()

    assert return_copy1
    assert library.available_copies("978-123") == 2
    assert library.active_loans("M1") == 0
    assert library.active_loans("M2") == 1


if __name__ == '__main__':
    main()

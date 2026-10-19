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
class Member:
    member_id: str
    name: str


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, isbn: str, title: str, author: str, number_of_copies: int) -> LibrarySystemCodes:
        if isbn in self.books:
            self.books[isbn][number_of_copies] += number_of_copies
            return LibrarySystemCodes.MORE_COPIES_ADDED
        else:
            self.books[isbn] = {
                "book": Book(isbn, title, author),
                "number_of_copies": number_of_copies
            }
            return LibrarySystemCodes.NEW_BOOK_ADDED

    def register_member(self, member_id: str, name) -> LibrarySystemCodes:
        if member_id not in self.members:
            self.members[member_id] = {
                "member": Member(member_id, name),
                "has_books": set()
            }
            return LibrarySystemCodes.NEW_MEMBER_ADDED
        else:
            return LibrarySystemCodes.MEMBER_ALREADY_EXISTS

    def borrow_book(self, member_id: str, isbn: str) -> LibrarySystemCodes:
        if (
            isbn in self.books and self.books[isbn]["number_of_copies"] > 0
            and member_id in self.members
            and len(self.members[member_id]["has_books"]) <= 3
        ):
            self.books[isbn]["number_of_copies"] -= 1
            self.members[member_id]["has_books"].add(isbn)
            return LibrarySystemCodes.BORROW_SUCCESSFUL
        else:
            return LibrarySystemCodes.BORROW_UNSUCCESSFUL

    def return_book(self, member_id: str, isbn: str) -> LibrarySystemCodes:
        if (
            member_id in self.members
            and isbn in self.books
        ):
            self.members[member_id]["has_books"].discard(isbn)
            self.books[isbn]["number_of_copies"] += 1
            return LibrarySystemCodes.RETURN_SUCCESSFUL
        else:
            return LibrarySystemCodes.RETURN_UNSUCCESSFUL


    def available_copies(self, isbn: str) -> LibrarySystemCodes:
        if isbn in self.books:
            return self.books[isbn]["number_of_copies"]
        else:
            return 0


def main():
    library = Library()

    print("Add 2 copies of Clean Code by Robert Martin.")
    print(library.add_book("978-123", "Clean Code", "Robert Martin", 2))
    print()

    print("Add 2 Members: Alice and Bob.")
    print(library.register_member("M1", "Alice"))
    print(library.register_member("M2", "Bob"))
    print()

    print("M1 and M2 borrows separate copies of same book:")
    print(library.borrow_book("M1", "978-123"))
    print(library.borrow_book("M2", "978-123"))
    print()

    assert library.available_copies("978-123") == 0

    print("M1 returns \"Clean Code\"")
    print(library.return_book("M1", "978-123"))
    print()

    assert library.available_copies("978-123") == 1


if __name__ == '__main__':
    main()

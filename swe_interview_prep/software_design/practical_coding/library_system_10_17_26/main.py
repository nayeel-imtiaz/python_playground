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


@dataclass
class Book:
    isbn: int
    title: str
    author: str


@dataclass
class Member:
    id: int
    name: str
    books: set[int]


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book: Book, number_of_copies: int):
        if book in self.books:
            self.books[book] += number_of_copies
        else:
            self.books[book] = number_of_copies

    def register_member(self, member: Member):
        if member not in self.members:
            self.members[member] = 0

    def borrow_book(self, member: Member, book: Book) -> bool:
        if not self.check_book_availability(book):
            return False
        member.books.add(book.isbn)
        self.books[book] -= 1
        return True

    def return_book(self, member: Member, book: Book):
        if book.isbn not in member.books:
            return False
        member.books.discard(book.isbn)
        self.books[book] += 1
        return True


    def check_book_availability(self, book: Book) -> bool:
        if book in self.books and self.books[book] > 0:
            return True
        return False


def main():
    pass


if __name__ == '__main__':
    main()

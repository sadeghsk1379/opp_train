import datetime
from book import Book
from library import Library


class Member:
    """
    Represents a library member who can borrow books and return them.

    Attributes:
        name (str): The member's name.
        barrowed_books (list[Book]): A list of books the member has borrowed.
        return_due_dates (list[datetime.date]): A list of due dates for the borrowed books.
        balance (float): The member's current balance.
        getbook (dict[Book, int]): A dictionary where keys are the books and values are their return due dates.
    """

    def __init__(self, name, barrowed_books, balance):
        """
        Initializes a member object.

        Args:
            name (str): The member's name.
            barrowed_books (list[Book]): A list of books the member has borrowed initially.
            balance (float): The member's current balance initially.
        """
        self.name = name
        self.barrowed_books = barrowed_books
        self.return_due_dates = []
        self.balance = balance
        self.getbook = {}

    def request_book(self, book, library):
        """
        Checks if the specified book is available and requests it for borrowing.

        Args:
            book (Book): The book to be requested.
            library (Library): The library where the book resides.

        Returns:
            bool: True if the book is available for borrowing, False otherwise.
        """
        if book in library.books:
            if len(self.barrowed_books) < 2:
                return True
        return False

    def barrow_book(self, book, library):
        """
        Borrows the specified book, updating the member's balance and book's availability.

        Args:
            book (Book): The book to be borrowed.
            library (Library): The library where the book resides.
        """
        for b in library.books:
            for e in b.editions.keys():
                if e in book.editions.keys():
                    if b.editions[e] >= 1:
                        b.editions[e] -= 1  # Update book's availability
                        self.balance -= (
                            b.rental_fee
                        )  # Deduct rental fee from member's balance
                        self.barrowed_books.append(book)  # Add book to borrowered_books
                        x = datetime.datetime.now()  # Get current date
                        self.getbook[b] = (
                            int(x.strftime("%j")) + 7
                        )  # Set return due date
                        return
        return

    def return_book(self, book, library):
        """
        Returns the specified book, updating the library's books list and member's borrowed_books list.

        Args:
            book (Book): The book to be returned.
            library (Library): The library where the book is being returned.
        """
        for b in library.books:  # Add book back to library
            for e in b.editions.keys():
                if e in book.editions.keys():
                    b.editions[e] += 1

        self.barrowed_books.remove(book)  # Remove book from borrowed_books
        days_late = Member.remaining_due_days(self, book)
        days_late *= -1
        while days_late > 0:
            self.balance -= book.rental_fee * library.late_fee_percentage
            days_late -= 1

    def display_borrowed_books(self):
        """
        Displays all the books currently borrowed by the member.
        """
        for i in self.barrowed_books:
            print("Title:", i.title)
            print("Authors:", i.authors)
            print("Publisher:", i.published_year)
            print("Edition:", i.editions)
            print("rental_fee:", i.rental_fee)

    def charge_balance(self, amount):
        """
        Charges the specified amount to the member's balance.

        Args:
            amount (float): The amount to be charged.
        """
        self.balance += amount

    def remaining_due_days(self, book):
        """
        Calculates the number of remaining due days for the specified book.

        Args:
            book (Book): The book to check the remaining due days for.

        Returns:
            int: The number of remaining due days.
        """
        if book in self.getbook:
            x = datetime.datetime.now()
            return int(self.getbook[book]) - int(x.strftime("%j"))

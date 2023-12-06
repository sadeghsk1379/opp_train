from member import Member

import datetime


class Special_member(Member):
    """
    Represents a special member who gets a discount on rental fees.

    Attributes:
        discount_rate (float): The member's discount rate.
    """

    def __init__(self, discount_rate, *args, **kwargs):
        """
        Initializes a special member object.

        Args:
            discount_rate (float): The member's discount rate.
            *args: Additional positional arguments to be passed to the base class constructor.
            **kwargs: Additional keyword arguments to be passed to the base class constructor.
        """
        self.discount_rate = discount_rate
        super().__init__(*args, **kwargs)

    def apply_discount(self, discount):
        """
        Applies a discount to the member's rental fees.

        Args:
            discount (float): The discount to be applied.
        """
        self.discount_rate = discount

    def barrow_book(self, book, library):
        for b in library.books:
            for e in b.editions.keys():
                if e in book.editions.keys():
                    if b.editions[e] >= 1:
                        b.editions[e] -= 1  # Update book's availability
                        self.balance -= (
                            b.rental_fee * self.discount_rate
                        ) / 100  # Deduct rental fee from member's balance
                        self.barrowed_books.append(book)  # Add book to borrowered_books
                        x = datetime.datetime.now()  # Get current date
                        self.getbook[b] = (
                            int(x.strftime("%j")) + 7
                        )  # Set return due date

        return super().barrow_book(book, library)

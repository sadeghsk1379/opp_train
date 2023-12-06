from book import Book


class Library:
    """
    Represents a library.

    Attributes:
        late_fee_percentage (float): The percentage of the book's price charged for late returns.
        books (list[Book]): A list of books in the library.
    """

    def __init__(self, late_fee_percentage):
        """
        Initializes a library object.

        Args:
            late_fee_percentage (float): The percentage of the book's price charged for late returns.
        """
        self.late_fee_percentage = late_fee_percentage
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book to the library.

        Args:
            book (Book): The book to be added to the library.
        """
        self.books.append(book)

    def remove_book(self, book: Book):
        """
        Removes a book from the library.

        Args:
            book (Book): The book to be removed from the library.
        """
        self.books.remove(book)

    def get_all_books(self):
        """
        Displays all the books in the library.
        """
        for book in self.books:
            print("Title:", book.title)
            print("Authors:", book.authors)
            print("Publisher:", book.published_year)
            print("Edition:", book.editions)
            print("rental_fee:", book.rental_fee)

    def get_book_by_author(self, author):
        """
        Gets the book written by a specific author.

        Args:
            author (str): The name of the author.

        Returns:
            Book: The book written by the specified author, if found.
        """
        for book in self.books:
            for a in book.authors:
                if a == author:
                    return book

from library import Library
from book import Book
from librarysystem import Librarysystem
from member import Member
from special_member import Special_member


def test_book():
    """Test the Book class."""
    edition = {"1": 2, "2": 4}
    newedition = {"3": 3}
    test1 = Book("travel around the world", "micheal", 1930, edition, 30)
    test1.display_info()  # Displays the book's information
    test1.add_edit_edition(newedition)  # Adds new editions to the book
    test1.display_info()  # Displays the updated book information
    test1.save_to_csv()  # Saves the book information to a CSV file
    test1.load_from_csv("book.csv")  # Loads the book information from a CSV file


def test_library():
    """Test the Library class."""
    lib1 = Library(20)  # Creates a new library with a late fee percentage of 20%

    book1 = Book("a", ["111", "222"], 1220, {"1": 1}, 1000)
    book2 = Book("b", ["333", "444"], 1500, {"2": 2}, 1500)

    lib1.add_book(book1)  # Adds books to the library
    lib1.add_book(book2)

    lib1.get_all_books()  # Retrieves all books from the library

    book = lib1.get_book_by_author(
        "222"
    )  # Retrieves the book written by the specified author
    if book:
        print("Book found:")  # Prints the book information if found
        print(book)
    else:
        print("Book not found.")  # Prints an error message if the book is not found


def test_member():
    """Test the Member class."""
    book1 = Book("a", ["111", "222"], 1220, {"1": 1}, 1000)
    book2 = Book("b", ["333", "444"], 1500, {"2": 2}, 1500)
    lib1 = Library(20)

    lib1.add_book(book1)  # Adds books to the library
    lib1.add_book(book2)

    memb1 = Member("sadegh", [], 1000)  # Creates a new member

    memb1.request_book(book1, lib1)  # Requests a book
    memb1.barrow_book(book1, lib1)  # Borrows the book
    memb1.return_book(book1, lib1)  # Returns the book

    memb1.barrow_book(book1, lib1)  # Borrows the same book again
    memb1.display_borrowed_books()  # Displays the list of borrowed books
    memb1.charge_balance(1500)  # Charges the balance


def test_librarysystem():
    """Test the Librarysystem class."""
    lib1 = Library(20)  # Creates a new library with a late fee percentage of 20%

    book1 = Book("a", ["111", "222"], 1220, {"1": 1}, 1000)
    book2 = Book("b", ["333", "444"], 1500, {"2": 2}, 1500)

    lib1.add_book(book1)  # Adds books to the library
    lib1.add_book(book2)

    memb1 = Member("sadegh", [book1, book2], 1000)  # Creates a new member
    sys1 = Librarysystem(lib1)

    sys1.add_member(memb1)  # Adds the member to the library system
    sys1.display_member_all()  # Displays information about all members
    sys1.display_library

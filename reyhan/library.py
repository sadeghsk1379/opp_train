from book import Book


class Library:
    def __init__(self, late_fee_percentage):
        self.late_fee_percentage = late_fee_percentage
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_all_books(self):
        for books in self.books:
            print(books)

    def get_book_by_author(self, author):
        for book in self.books:
            for a in book.authors:
                if a == author:
                    return book


lib1 = Library(20)
book1 = Book("a", ["111", "222"], 1220, {"1": 1}, 1000)
book2 = Book("b", ["333", "444"], 1500, {"2": 2}, 1500)

lib1.add_book(book1)
lib1.add_book(book2)
lib1.get_all_books()
lib1.get_book_by_author("222")

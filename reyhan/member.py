import datetime
from book import Book
from library import Library


class Member:
    def __init__(self, name, barrowed_books, balance):
        self.name = name
        self.barrowed_books = barrowed_books
        self.return_due_dates = []
        self.balance = balance
        self.getbook = {}

    def request_book(self, book, library):
        if book in library.books:
            return True

    def barrow_book(self, book, library):
        for b in library.books:
            for e in b.editions.keys():
                if e in book.editions.keys():
                    b.editions[e] -= 1
                    self.balance -= b.rental_fee
                    self.barrowed_books.append(book)
                    x = datetime.datetime.now()
                    self.getbook[b] = int(x.strftime("%j")) + 7

    def return_book(self, book, library):  # soti
        library.books.append(book)
        self.barrowed_books.remove(book)

    def display_borrowed_books(self):
        for i in self.barrowed_books:
            print("Title:", i.title)
            print("Authors:", i.authors)
            print("Publisher:", i.published_year)
            print("Edition:", i.editions)
            print("rental_fee:", i.rental_fee)

    def charge_balance(self, amount):
        self.balance += amount

    def remaining_due_days(self, book):
        if book in self.getbook:
            x = datetime.datetime.now()
            sum = int(self.getbook[book]) - int(x.strftime("%j"))
            return sum


book1 = Book("a", ["111", "222"], 1220, {"1": 1}, 1000)
book2 = Book("b", ["333", "444"], 1500, {"2": 2}, 1500)
lib1 = Library(20)
lib1.add_book(book1)
lib1.add_book(book2)
memb1 = Member("sadegh", [book1, book2], 1000)
memb1.request_book(book1, lib1)
memb1.barrow_book(book2, lib1)
memb1.return_book(book1, lib1)
memb1.remaining_due_days(book2)

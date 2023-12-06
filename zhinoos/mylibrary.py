import csv
import datetime


class Book:
    def __init__(
        self,
        title,
        authors,
        published_year,
        editions,
        rental_fee=None,
    ):
        self.title = title
        self.authors = authors
        self.published_year = published_year
        self.editions = editions
        self.rental_fee = rental_fee

    def display_info(self):
        print("Title:", self.title)
        print("Authors:", self.authors)
        print("Publisher:", self.published_year)
        print("Edition:", self.editions)
        print("rental_fee:", self.rental_fee)

    def add_edition(self, newedition):
        self.editions.update(newedition)

    def edit_edition(self, newedition):
        self.editions.update(newedition)

    def calculate_rental_fee(self, days):
        rental_fee = days * self.rental_fee
        return rental_fee

    def save_to_csv(self):
        with open("mybook.csv", "w") as file:
            line = csv.writer(file)
            line.writerow(
                ["Title", "Authors ", "published_year", "editions", "rental_fee"]
            )
            line.writerow(
                [
                    self.title,
                    self.authors,
                    self.published_year,
                    self.editions,
                    self.rental_fee,
                ]
            )

    def load_from_csv(self, path):
        with open(path, "r") as file:
            while True:
                line = file.readline()
                if line == "":
                    break

                print(line)


class Library:
    def __init__(self, late_fee_percentage):
        self.books = list

        self.late_fee_percentage = late_fee_percentage

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_all_books(self):
        for books in self.books:
            print(books)

    def findbook(self, author):
        for book in self.books:
            for _ in book.authors:
                if _ == author:
                    return book


class Member:
    def __init__(self, name, barrowed_books, balance):
        self.name = name
        self.barrowed_books = barrowed_books
        self.return_due_dates = []
        self.balance = balance

    def request_book(self, book, library):
        if book in library.books:
            return True

    def barrow_book(self, book, library):
        for B in library.books:
            for E in B.editions.keys():
                if E in book.editions.keys():
                    B.editions[E] -= 1
                    self.balance -= B.rental_fee
                    self.barrowed_books.append(book)
                    x = datetime.datetime.now()
                    y = int(x.strftime("%j")) + 7

                    self.return_due_dates.append(self.remaining_due_days(book, y))

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

    def remaining_due_days(self, book, time):
        x = datetime.datetime.now()
        sum = time - int(x.strftime("%j"))
        return sum


class Special_member(Member):
    def __init__(self, discount_rate, *args, **kwargs):
        self.discount_rate = discount_rate
        super().__init__(*args, **kwargs)

    def apply_discount(self, discount):
        self.discount_rate = discount


class Librarysystem:
    def __init__(self, library) -> None:
        self.library = library
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def display_member_info(self, member):
        if member in self.members:
            print(f"Member Name: {member.name}")
            print(f"Borrowed Books: {member.barrowed_books}")
            print(f"Return Due Dates: {member.return_due_dates}")
            print(f"Balance: {member.balance}")
            print(f"Getbook: {member.getbook}")

    def display_member_all(self):
        for member in self.members:
            print(f"Member Name: {member.name}")
            print(f"Borrowed Books: {member.barrowed_books}")
            print(f"Return Due Dates: {member.return_due_dates}")
            print(f"Balance: {member.balance}")
            print(f"Getbook: {member.getbook}")

    def display_library_books(self):
        for i in self.library.books:
            print(f"Title: {i.title}")
            print(f"Authors: {', '.join(i.authors)}")
            print(f"Published Year: {i.published_year}")
            print(f"Editions: {i.editions}")


edition = {
    "1": 2,
    "2": 4,
}
newedition = {"2": 3}
test1 = Book("b", "micheal", 1930, edition, 1500)
test1.display_info()
test1.add_edition(newedition)
test1.edit_edition(newedition)

test1.display_info()
test1.save_to_csv()
test1.load_from_csv("mybook.csv")

from library import Library
from member import Member
from book import Book


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


lib1 = Library(20)

book1 = Book("a", ["111", "222"], 1220, {"1": 1}, 1000)
book2 = Book("b", ["333", "444"], 1500, {"2": 2}, 1500)

lib1.add_book(book1)
lib1.add_book(book2)
sys1 = Librarysystem(lib1)
memb1 = Member("sadegh", [book1, book2], 1000)
sys1.add_member(memb1)
sys1.remove_member(memb1)
sys1.add_member(memb1)
sys1.display_member_info(memb1)
sys1.display_member_all()
sys1.display_library_books()

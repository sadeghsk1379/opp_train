from library import Library
from member import Member
from book import Book


class Librarysystem:
    """
    Represents a library system that manages members, books, and their interactions.

    Attributes:
        library (Library): The library associated with the system.
        members (list[Member]): A list of members registered in the system.
    """

    def __init__(self, library: Library) -> None:
        """
        Initializes a library system object.

        Args:
            library (Library): The library associated with the system.
        """
        self.library = library
        self.members = []

    def add_member(self, member: Member) -> None:
        """
        Adds a member to the system.

        Args:
            member (Member): The member to be added to the system.
        """
        self.members.append(member)

    def remove_member(self, member: Member) -> None:
        """
        Removes a member from the system.

        Args:
            member (Member): The member to be removed from the system.
        """
        self.members.remove(member)

    def display_member_info(self, member: Member) -> None:
        """
        Displays the information of a specific member.

        Args:
            member (Member): The member whose information to display.
        """
        if member in self.members:
            print(f"Member Name: {member.name}")
            print(f"Borrowed Books: {member.barrowed_books}")
            print(f"Return Due Dates: {member.return_due_dates}")
            print(f"Balance: {member.balance}")
            print(f"Getbook: {member.getbook}")
        else:
            print(f"Member {member.name} not found.")

    def display_member_all(self) -> None:
        """
        Displays the information of all registered members.
        """
        for member in self.members:
            self.display_member_info(member)

    def display_library_books(self) -> None:
        """
        Displays all the books in the library system.
        """
        for book in self.library.books:
            print(f"Title: {book.title}")
            print(f"Authors: {', '.join(book.authors)}")
            print(f"Published Year: {book.published_year}")
            print(f"Editions: {book.editions}")

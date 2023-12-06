import csv


class Book:
    """Represents a book."""

    def __init__(
        self,
        title: str,
        authors: list[str],
        published_year: int,
        editions: dict,
        rental_fee: float = None,
    ):
        """
        Initializes a book object.

        Args:
            title (str): The title of the book.
            authors (list[str]): A list of the authors of the book.
            published_year (int): The year the book was published.
            editions (dict): A dictionary of editions and their respective quantities.
            rental_fee (float): The rental fee for the book.
        """
        self.title = title
        self.authors = authors
        self.published_year = published_year
        self.editions = editions
        self.rental_fee = rental_fee

    def display_info(self):
        """
        Displays information about the book.

        Prints the title, authors, published year, editions, and rental fee of the book.
        """
        print("Title:", self.title)
        print("Authors:", self.authors)
        print("Publisher:", self.published_year)
        print("Edition:", self.editions)
        print("rental_fee:", self.rental_fee)

    def add_edit_edition(self, new_edition: dict):
        """
        Adds or edits an edition of the book.

        Args:
            newedition (dict): A dictionary representing the new or updated edition.
        """
        self.editions.update(new_edition)

    def calculate_rental_fee(self, days: int):
        """
        Calculates the rental fee for the book based on the number of days it is rented.

        Args:
            days (int): The number of days the book is rented.

        Returns:
            float: The rental fee for the book.
        """
        rental_fee = days * self.rental_fee
        return rental_fee

    def save_to_csv(self):
        """
        Saves the book information to a CSV file.

        Creates a CSV file named `book.csv` and writes the book information to it.
        """
        with open("book.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["Title", "Authors ", "published_year", "editions", "rental_fee"]
            )
            writer.writerow(
                [
                    self.title,
                    self.authors,
                    self.published_year,
                    self.editions,
                    self.rental_fee,
                ]
            )
        f.close()

    def load_from_csv(self, path):
        """
        Loads the book information from a CSV file.

        Reads the `book.csv` file and updates the book object with the information from the file.

        Args:
            path (str): The path to the CSV file.
        """
        with open(path, "r", newline="") as f:
            while True:
                line = f.readline()
                line = line.strip()
                if line == "":
                    break

                # Extract the book information from the CSV line
                title, authors, published_year, editions, rental_fee = line.split(",")

                # Update the book object with the extracted information
                self.title = title
                self.authors = authors
                self.published_year = published_year
                self.editions = {
                    int(key): int(value) for key, value in editions.split(":")
                }
                self.rental_fee = float(rental_fee)
        f.close

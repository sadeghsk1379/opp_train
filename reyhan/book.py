import csv


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
        self.rental_fee = rental_fee  # all editions have same price

    def display_info(self):
        print("Title:", self.title)
        print("Authors:", self.authors)
        print("Publisher:", self.published_year)
        print("Edition:", self.editions)
        print("rental_fee:", self.rental_fee)

    def add_edit_edition(self, newedition):
        self.editions.update(newedition)

    def calculate_rental_fee(self, days):
        rental_fee = days * self.rental_fee
        return rental_fee

    def save_to_csv(self):
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

    def load_from_csv(self, path):
        with open(path, "r", newline="") as f:
            while True:
                line = f.readline()
                line = line.strip()
                if line == "":
                    break

                print(line)


edition = {
    "1": 2,
    "2": 4,
}
newedition = {"2": 3}
test1 = Book("a", "micheal", 1930, edition, 1500)
test1.display_info()
test1.add_edit_edition(newedition)
test1.display_info()
test1.save_to_csv()
test1.load_from_csv("book.csv")

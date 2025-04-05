class Library:
    # no_of_books = 0
    # books = []
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_books(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1
        # print(f"{book_name} has been added to the library.")

    def get_all_books(self):
        for book in self.books:
            print(book)


# create a new library
library1 = Library()
library1.add_books("Harry Potter and the Philosopher's Stone")
library1.add_books("Harry Potter and the Chamber of Secrets")
library1.add_books("Harry Potter and the Prisoner of Azkaban")
library1.add_books("Harry Potter and the Goblet of Fire")
library1.add_books("Harry Potter and the Order of the Phoenix")
library1.add_books("Harry Potter and the Half-Blood Prince")
library1.add_books("Harry Potter and the Deathly Hallows")
library1.add_books("Harry Potter and the Cursed Child")

library1.no_of_books = len(library1.books)
print(f"Total number of books in the library: {library1.no_of_books}")

library1.get_all_books()
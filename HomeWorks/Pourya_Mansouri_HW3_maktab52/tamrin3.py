class Book:
    title: str
    price: float
    book_count: int
    count_all_of_books: int

    count_all_of_books = 0

    def __init__(self, title: str, price: float, book_count):
        self.title = title
        self.price = price
        self.book_count = book_count
        self.__class__.add_book(book_count)

    @classmethod
    def add_book(cls, book_count):
        cls.count_all_of_books += book_count

    def __repr__(self):
        return f"book with title= \"{self.title}\" has {self.price}$ price and we have {self.book_count} of it " \
               f"\n** and we have {self.__class__.count_all_of_books} books in our store "


b1 = Book("Harry Potter", 13.1, 10)
b2 = Book("The Great Gatsby", 17.6, 5)
print(b1)
print()
print(b2)

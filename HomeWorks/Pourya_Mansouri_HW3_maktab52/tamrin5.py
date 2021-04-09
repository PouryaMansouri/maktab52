# TODO: __repr__ for all classes
# TODO: How many author
# TODO: check valid input for author

class User:
    name: str
    email: str
    sex: str

    def __init__(self, name: str, email: str = None, sex: str = None):
        self.name = name
        self.email = email
        self.sex = sex


class Asar:
    title: str
    authors: list

    def __init__(self, title: str, authors: list or User = None):
        self.title = title
        if issubclass(authors, User):
            self.authors = [authors]
        elif isinstance(authors, list):
            self.authors = authors


# TODO: How many author
# TODO: check valid input for author
class Article(Asar):
    magazine: str
    year_of_publication: int
    __count: int

    def __init__(self, title: str, authors: list or User = None, magazine: str = None, year_of_publication: int = None):
        super().__init__(title, authors)
        self.magazine = magazine
        self.year_of_publication = year_of_publication

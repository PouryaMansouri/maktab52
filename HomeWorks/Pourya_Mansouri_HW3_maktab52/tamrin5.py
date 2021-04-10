# TODO: __repr__ for all classes
# TODO: How many author
# TODO: check valid input for author

class User:
    name: str
    email: str
    sex: str

    def __init__(self, name: str, email: str = None, sex: str = None):
        self.name = name.capitalize()
        self.email = email
        self.sex = sex

    # TODO: need to improve
    def __repr__(self):
        _ = ''
        for key in self.__dict__:
            if self.__dict__[key]:
                _ += f"{key}= {self.__dict__[key]}  "
        return _


class Poet(User):
    style: str

    def __init__(self, name: str, email: str = None, sex: str = None, style=None):
        super().__init__(name, email, sex)
        self.style = style


class Researcher(User):
    field: str
    university: str

    def __init__(self, name: str, field: str, email: str = None, sex: str = None, university: str = None):
        super().__init__(name, email, sex)
        self.field = field
        self.university = university


class Writer(User):
    writer_code: int
    genre: str

    def __init__(self, name: str, writer_code: int, email: str = None, sex: str = None, genre: str = None):
        super().__init__(name, email, sex)
        self.writer_code = writer_code
        self.genre = genre


# TODO: How many author
# TODO: check valid input for author
class Asar:
    title: str
    authors: list

    def __init__(self, title: str, authors: list or User = None):
        self.title = title
        self._set_author(authors)

    def __repr__(self):
        _ = ''
        for key in self.__dict__:
            if self.__dict__[key]:
                _ += f"{key}= {self.__dict__[key]}  "
        return _

    def _set_author(self, authors):
        if not self.__is_valid_owner(authors):
            raise Exception(f"Invalid input for author(s) ")
        if isinstance(authors, list):
            self.authors = authors
        else:
            self.authors = [authors]

    def __is_valid_owner(self, authors) -> bool:

        if isinstance(self, Article):
            if isinstance(self, Researcher):
                return True

            elif isinstance(authors, list):
                for _ in authors:
                    if not isinstance(_, Researcher):
                        return False
                else:
                    return True

        elif isinstance(self, Poem):
            if isinstance(authors, Poet):
                return True

        elif isinstance(self, Book):
            if isinstance(authors, Writer):
                return True

            elif isinstance(authors, list):
                for _ in authors:
                    if not isinstance(_, Writer):
                        return False
                else:
                    return True
        elif isinstance(self, Asar):
            if isinstance(authors, list):
                for _ in authors:
                    if not isinstance(_, (Researcher, Poet, Writer, User)):
                        return False
                else:
                    return True
            elif isinstance(authors, (Researcher, Poet, Writer, User)):
                return True

        return False


class Article(Asar):
    magazine: str
    year_of_publication: int

    def __init__(self, title: str, authors: list or Researcher = None, magazine: str = None,
                 year_of_publication: int = None):
        super().__init__(title, authors)
        self.magazine = magazine
        self.year_of_publication = year_of_publication

    @property
    def count_authors(self):
        return f"This article has {len(self.authors)} researcher(s)"


class Poem(Asar):
    literary_format: str

    def __init__(self, title: str, author: Poet = None, literary_format: str = None):
        super().__init__(title, author)
        self.literary_format = literary_format


class Book(Asar):
    isbn: str
    publisher: str

    def __init__(self, title: str, authors: list or Writer = None, isbn: str = None,
                 publisher: str = None):
        super().__init__(title, authors)
        self.isbn = isbn
        self.publisher = publisher

    @property
    def count_authors(self):
        return f"This article has {len(self.authors)} writer(s)"


u = User("Ali", sex='M')
print(u)
r1 = Researcher("Reza", "Math", email="RezA@gmail.com", sex='M')
r2 = Researcher("Pourya", "chemistry", email="pourya@gmail.com")
print(r1)
print(r2)
a1 = Asar("title1", r1)
a2 = Article("python", [r1, r2])
print(a1)
print(a2)
print(a2.count_authors)
# error for author
# p = Poem("sher no", r1)

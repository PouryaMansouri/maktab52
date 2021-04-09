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
            if self.__dict__[key] :
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
        if not self.__class__.__is_valid_owner(authors):
            raise Exception("In valid input -  author(s) should be researcher")
        super().__init__(title, authors)
        self.magazine = magazine
        self.year_of_publication = year_of_publication

    @staticmethod
    def __is_valid_owner(owner) -> bool:
        """
            Use staticmethod because it's pycharm recommendation
        """
        if isinstance(owner, Researcher):
            return True

        elif isinstance(owner, list):
            for _ in owner:
                if not isinstance(_, Researcher):
                    return False
            else:
                return True

        return False


u = User("Ali", sex='M')
print(u)
r1 = Researcher("Reza", "Math", email="RezA@gmail.com", sex='M')
print(r1)
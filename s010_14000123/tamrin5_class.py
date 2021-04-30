from abc import ABC


class Person(ABC):
    name: str
    email: str
    gender: str


class Relic(ABC):
    __COUNTER = 0
    title: str
    owner: Person or list

    def __init__(self, title: str, owner: Person or list = None):
        self.title = title
        self.owner = owner

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        assert isinstance(title, str)
        self.__title = title

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        if isinstance(owner, list):
            self.__owner = owner
        else:
            self.__owner = [owner]

    @classmethod
    def get_count(cls):
        return cls.__COUNTER


class Poem(Relic):
    style: str

    def __init__(self,title:str , owner : list = None):
        ...
"""
    Birthday class
    tamrin 2
"""

from datetime import datetime


class Birthday:
    age: int
    now: datetime
    birthday_date: tuple

    def __init__(self, date: tuple):
        self.__birthday_tuple = date
        self.__birthday_date = datetime(*date)

    @staticmethod
    def calculate_delta_time(date):
        __delta = datetime.now() - date
        return __delta

    @property
    def years(self) -> int:
        return int(Birthday.calculate_delta_time(self.__birthday_date).days // 365)

    @property
    def hours(self) -> int:
        return int(Birthday.calculate_delta_time(self.__birthday_date).total_seconds() // 3600)

    def days_to_birthday(self):
        __birthday = self.__birthday_tuple[1:]
        if __birthday[0] < datetime.now().month:
            __year = datetime.now().year + 1
        else:
            __year = datetime.now().year
        __next_birthday = datetime(__year, *__birthday)
        return f"{abs(Birthday.calculate_delta_time(__next_birthday).days)} days to your next birthday"

    def __repr__(self) -> str:
        return f'you are {self.years} years old or {self.hours} hours old'


my_birthday_date = 1991, 3, 21, 11

b1 = Birthday(my_birthday_date)
print(b1)
print(b1.days_to_birthday())

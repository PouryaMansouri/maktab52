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
        self.birthday_date = date

    @property
    def birthday_date(self):
        return self.__birthday_date

    @birthday_date.setter
    def birthday_date(self, date):
        assert isinstance(date, tuple) and 1910 <= date[0] < 2022 and 1 <= date[1] <= 12 and 1 <= date[2] < 31
        self.__birthday_date = datetime(*date)

    @staticmethod
    def calculate_delta_time(date):
        __delta = datetime.now() - date
        return __delta

    @property
    def years(self) -> int:
        return int(Birthday.calculate_delta_time(self.birthday_date).days // 365)

    @property
    def hours(self) -> int:
        return int(Birthday.calculate_delta_time(self.birthday_date).total_seconds() // 3600)

    def days_to_birthday(self):
        __birthday = self.__birthday_tuple[1:]
        if __birthday[0] < datetime.now().month:
            __year = datetime.now().year + 1
        else:
            __year = datetime.now().year
        __next_birthday = datetime(__year, *__birthday)
        return f"{abs(Birthday.calculate_delta_time(__next_birthday).days)} days to your next birthday"

    def __repr__(self) -> str:
        return f'you are {self.years} years old or {self.hours} hours old\n' \
               f"your birthday is {self.birthday_date}"


my_birthday_date = 1991, 3, 21, 11

b1 = Birthday(my_birthday_date)
print(b1)
print(b1.days_to_birthday())
print()
b1.birthday_date = 1991, 22, 21, 11

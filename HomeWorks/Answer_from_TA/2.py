from datetime import datetime, timedelta


class BirthDay:
    def __init__(self, year, month, day, hour):
        self.__hour = hour
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def birthdate(self):
        return datetime(year=self.__year, month=self.__month, day=self.__day, hour=self.__hour)

    @property
    def age_in_year(self):
        birthdate = self.birthdate
        today = datetime.now()
        return today.year - birthdate.year - (
                (today.month, today.day, today.hour) < (birthdate.month, birthdate.day, birthdate.hour)
        )

    @property
    def age_in_hour(self):
        birthdate = self.birthdate
        today = datetime.now()
        age = today - birthdate
        return (age.days * 24) + (age.seconds / 3600)

    @property
    def to_birthday(self):
        today = datetime.now()
        birthdate = self.birthdate
        has_passed = (today.month, today.day, today.hour) > (birthdate.month, birthdate.day, birthdate.day)
        birthdate = birthdate.replace(year=today.year + has_passed)
        return birthdate - today


my_birthdate = BirthDay(1995, 10, 19, 10)
print(my_birthdate.age_in_year)
print(my_birthdate.age_in_hour)
print(my_birthdate.to_birthday)

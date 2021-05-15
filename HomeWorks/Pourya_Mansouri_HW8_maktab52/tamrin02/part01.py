from datetime import datetime, timedelta
import jdatetime
from tamrin03.weekday_gen_function import weekdays_gen

class MyTime:

    def __init__(self):
        print("Welcome to my class time")
        self.pattern = "%Y-%m-%d %H:%M"

    @property
    def date_from(self) -> datetime:
        return self.__date_from

    @date_from.setter
    def date_from(self, date: datetime or str):
        self.__date_from = self.__set_time(date)

    @property
    def date_to(self) -> datetime:
        return self.__date_to

    @date_to.setter
    def date_to(self, date: datetime or str):
        self.__date_to = self.__set_time(date)

    def __set_time(self, date):
        if isinstance(date, datetime):
            return date
        else:
            return datetime.strptime(date, self.pattern)

    def get_time(self) -> datetime:
        date_string = input(f'Enter date(yyyy-mm-dd hh:mm): ')
        date = datetime.strptime(date_string, self.pattern)
        return date

    def delta_time(self) -> int:
        delta = self.date_to - self.date_from
        return delta.seconds

    @property
    def date_to_jdatetime(self):
        return jdatetime.datetime.fromgregorian(datetime=self.date_to)

    @property
    def date_from_jdatetime(self):
        return jdatetime.datetime.fromgregorian(datetime=self.date_from)

    def check_leap_year(self):
        res = 0
        from_year = self.date_from_jdatetime.year

        if self.date_to_jdatetime.month > self.date_from_jdatetime.month:
            to_year = self.date_to_jdatetime.year + 1
        else:
            to_year = self.date_to_jdatetime.year
        date = self.date_from_jdatetime
        years = list()
        for _ in range(from_year, to_year):
            date = date.replace(year=_)
            if date.isleap():
                res += 1
                years.append(_)
        return res, years

    def time_change(self):
        from_year = self.date_from_jdatetime.year
        to_year = self.date_to_jdatetime.year
        from_month = self.date_to_jdatetime.month
        to_month = self.date_to_jdatetime.month
        times = list()
        if from_month <= 6:
            times.append((from_year, 6))
            res = 1
        else:
            res = 0
        for _ in range(from_year + 1, to_year):
            times.append((_, 1))
            times.append((_, 6))
            res += 2
        times.append((to_year, 1))
        res += 1
        if to_month > 6:
            times.append((to_year, 6))
            res += 1

        return res, times

    # @staticmethod
    # def weekdays_gen(s_day: datetime, e_day: datetime, w_day: int):
    #     assert 0 <= w_day <= 6
    #     w_day -= 2
    #     if w_day < 0:
    #         w_day += 7
    #     step = timedelta(days=1)
    #     # print(s_day)
    #     # print(s_day.weekday())
    #     while s_day.weekday() != w_day:
    #         s_day += step
    #         # print(s_day)
    #     step = timedelta(weeks=1)
    #     while s_day <= e_day:
    #         yield s_day
    #         s_day += step


if __name__ == '__main__':
    t = MyTime()
    t.date_from = '2010-02-10 11:30'
    t.date_to = datetime.now()
    print(t.date_from)
    print(t.date_to)
    print("\ndelta time:")
    print(f"{t.delta_time()} seconds")
    print("\nthose times in persian calender")
    print(t.date_to_jdatetime)
    print(t.date_from_jdatetime)
    print("\nHow many times,we have leap year:")
    print(t.check_leap_year())
    print("\nHow many times,we have time change:")
    print(t.time_change())
    s = t.date_from
    e = t.date_to
    # gen = MyTime.weekdays_gen(s, e, 3)
    gen = weekdays_gen(s, e, 3)
    for _ in gen:
        print(_.date(), _.strftime("%A"))

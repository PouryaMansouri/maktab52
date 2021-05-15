from datetime import datetime, timedelta


def weekdays_gen(s_day: datetime, e_day: datetime, w_day: int):
    assert 0 <= w_day <= 6
    w_day -= 2
    if w_day < 0:
        w_day += 7
    step = timedelta(days=1)
    # print(s_day)
    # print(s_day.weekday())
    while s_day.weekday() != w_day:
        s_day += step
        # print(s_day)
    step = timedelta(weeks=1)
    while s_day <= e_day:
        yield s_day
        s_day += step

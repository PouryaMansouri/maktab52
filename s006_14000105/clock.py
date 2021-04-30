class Clock:
    def __init__(self, hour, minute):
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            raise Exception("Invalid input for hour")
        if 0 <= minute <= 24:
            self.minute = minute
        else:
            raise Exception("Invalid input for minute")

    def __repr__(self):
        return f"{self.hour:0>2d}:{self.minute:0>2d}"

    def __eq__(self, other):
        return all([self.hour == other.hour, self.minute == other.minute])

    def __add__(self, minutes):
        m = self.minute + minutes
        self.minute = m % 60
        self.hour = (self.hour + (m // 60)) % 24
        return f"{self.hour:0>2d}:{self.minute:0>2d}"

    def __sub__(self, minutes):
        m = self.minute - minutes
        self.minute = m % 60
        self.hour = (self.hour - abs((m // 60))) % 24
        return f"{self.hour:0>2d}:{self.minute:0>2d}"


clock1 = Clock(13, 4)
clock2 = Clock(13, 4)
clock3 = Clock(6, 4)

print(clock1)
print(clock2 == clock1)
print(clock2 == clock3)
print(clock1 + 60 * 2)
print(clock1 + 20)
print(clock1 - 15)
print(clock1 - 60 * 2)
print(clock1 - 65)


class Base:
    def method(self):
        return " base "


class Father(Base):
    def method(self):
        return " father " + super().method()


class Mother(Base):
    def method(self):
        return " mother " + super().method()


class Child(Father, Mother):
    pass


print(Child().method())

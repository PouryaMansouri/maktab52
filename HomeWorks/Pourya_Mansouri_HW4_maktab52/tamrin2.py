import abc


# TODO: ask question : class shape(metaclass = abs.ABCMeta) vs (abc.ABC)
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    x: int

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        assert isinstance(x, int)
        self.__x = x

    @property
    def area(self):
        return self.__x ** 2

    @property
    def perimeter(self):
        return self.__x * 4


class Rectangle(Shape):
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        assert isinstance(x, int)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert isinstance(y, int)
        self.__y = y

    @property
    def area(self):
        return self.__x * self.__y

    @property
    def perimeter(self):
        return (self.__x + self.__y) * 2

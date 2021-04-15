import abc


# TODO: ask question : class shape(metaclass = abs.ABCMeta) vs (abc.ABC)
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    @staticmethod  # because it's tools and  it dont call cls
    def concat_area(rectangle_list: list) -> int:
        sum_area = 0
        for _ in rectangle_list:
            assert isinstance(_, Rectangle)
            sum_area += _.area
        return sum_area


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

    @staticmethod
    def draw_concat(square_side_list: list) -> None:
        for _ in square_side_list:
            assert isinstance(_, int) and _ > 0
        copy_list = square_side_list.copy()
        while not all(map(lambda x: x <= 0, copy_list)):
            for _ in range(len(square_side_list)):
                if copy_list[_] <= 0:
                    print(' ' * square_side_list[_], end="")
                else:
                    print('*' * square_side_list[_], end="")
            copy_list = list(map(lambda x: x - 1, copy_list))
            print()

    def __repr__(self):
        return f"this is a square with area: {self.area} and perimeter: {self.perimeter}"


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

    def __repr__(self):
        return f"this is a rectangle with area: {self.area} and perimeter: {self.perimeter}"


rect1 = Rectangle(3, 5)
print(rect1)
# rect1.x = 2.5
print()
rect2 = Rectangle(4, 6)
print(rect2)

print()
rect_list = [rect2, rect1]
print(Shape.concat_area(rect_list))
print()
Square.draw_concat([2, 5, 3])

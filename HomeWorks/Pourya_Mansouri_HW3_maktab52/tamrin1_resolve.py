"""
   Tamrin 1: Triangle class
"""


# TODO: use private attr , property,  @A.setter  --> Done
# TODO check input validation for set attr --> Done
class Triangle:
    p1: tuple
    p2: tuple
    p3: tuple

    # TODO: what should I do for shadow?!!
    def __init__(self, point1: tuple, point2: tuple, point3: tuple):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3

    @property
    def p1(self):
        return self.__p1

    @p1.setter
    def p1(self, point):
        assert isinstance(point, tuple) and isinstance(point[0], int) and isinstance(point[1], int)
        self.__p1 = point

    @property
    def p2(self):
        return self.__p2

    @p2.setter
    def p2(self, point):
        assert isinstance(point, tuple) and isinstance(point[0], int) and isinstance(point[1], int)
        self.__p2 = point

    @property
    def p3(self):
        return self.__p3

    @p3.setter
    def p3(self, point):
        assert isinstance(point, tuple) and isinstance(point[0], int) and isinstance(point[1], int)
        self.__p3 = point

    def area(self) -> float:
        """
            calculation the area of triangle with formula
        :return: float
        """
        return abs(
            0.5 * (self.__p1[0] * (self.__p2[1] - self.__p3[1]) + self.__p2[0] * (self.__p3[1] - self.__p1[1]) +
                   self.__p3[0] * (
                           self.__p1[1] - self.__p2[1])))

    @staticmethod
    def distance_between_two_point(point1: tuple, point2: tuple):
        """
        calculate the distance between to point
        the function is static because it is tools
        :param point1:
        :param point2:
        :return: float
        """
        return round(((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5, 3)

    def sides(self):
        """
        calculate the sides of triangle with distance tools
        :return: tuple
        """
        __p1_p2 = Triangle.distance_between_two_point(self.__p1, self.__p2)
        __p1_p3 = Triangle.distance_between_two_point(self.__p1, self.__p3)
        __p2_p3 = Triangle.distance_between_two_point(self.__p2, self.__p3)
        return __p1_p2, __p1_p3, __p2_p3

    def perimeter(self) -> float:
        __p1_p2, __p1_p3, __p2_p3 = self.sides()
        return __p1_p2 + __p1_p3 + __p2_p3

    def centroid(self) -> tuple:
        return round((self.__p1[0] + self.__p2[0] + self.__p3[0]) / 3, 3), round(
            (self.__p1[1] + self.__p2[1] + self.__p3[1]) / 3,
            3)

    def type(self):
        __p1_p2, __p1_p3, __p2_p3 = self.sides()

        if all([__p2_p3 == __p1_p2, __p1_p3 == __p2_p3, __p1_p3 == __p1_p2]):
            return "Equilateral triangle"
        elif any([__p2_p3 == __p1_p2, __p1_p3 == __p2_p3, __p1_p3 == __p1_p2]):
            return "Isosceles triangle"

        elif any([
            round((__p1_p2 ** 2 + __p1_p3 ** 2) ** 0.5, 3) == __p2_p3,
            round((__p1_p2 ** 2 + __p2_p3 ** 2) ** 0.5, 3) == __p1_p3,
            round((__p2_p3 ** 2 + __p1_p3 ** 2) ** 0.5, 3) == __p1_p2
        ]):
            return "Right-angle triangle"
        else:
            return "Scalene Triangle"

    def __repr__(self):
        return f"Type= {self.type()} \nArea= {self.area()} \nperimeter= {self.perimeter()} \nsides{self.sides()}\n" \
               f"centroid{self.centroid()} "


p1 = (1, 5)
p2 = (4, 10)
p3 = (7, 5)

p4 = (1, 5)
p5 = (1, 10)
p6 = (7, 5)

t1 = Triangle(p1, p2, p3)
t2 = Triangle(p4, p5, p6)

print("Triangle 1")
print(t1)


print()
print("Triangle 2")
print(t2)

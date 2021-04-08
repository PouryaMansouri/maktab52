'''
   Triangle class
'''


class Triangle:
    p1: tuple
    p2: tuple
    p3: tuple

    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        return abs(
            0.5 * (self.p1[0] * (self.p2[1] - self.p3[1]) + self.p2[0] * (self.p3[1] - self.p1[1]) + self.p3[0] * (
                    self.p1[1] - self.p2[1])))

    @staticmethod
    def distance_between_two_point(point1: tuple, point2: tuple):
        return round(((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5, 3)

    def sides(self):
        __p1_p2 = Triangle.distance_between_two_point(self.p1, self.p2)
        __p1_p3 = Triangle.distance_between_two_point(self.p1, self.p3)
        __p2_p3 = Triangle.distance_between_two_point(self.p2, self.p3)
        return __p1_p2, __p1_p3, __p2_p3

    def perimeter(self):
        __p1_p2, __p1_p3, __p2_p3 = self.sides()
        return __p1_p2 + __p1_p3 + __p2_p3

    def centroid(self):
        return round((self.p1[0] + self.p2[0] + self.p3[0]) / 3, 3), round((self.p1[1] + self.p2[1] + self.p3[1]) / 3,
                                                                           3)

    def type(self):
        __p1_p2 = Triangle.distance_between_two_point(self.p1, self.p2)
        __p1_p3 = Triangle.distance_between_two_point(self.p1, self.p3)
        __p2_p3 = Triangle.distance_between_two_point(self.p2, self.p3)

        if all([__p2_p3 == __p1_p2, __p1_p3 == __p2_p3, __p1_p3 == __p1_p2]):
            return "Equilateral triangle"
        elif any([__p2_p3 == __p1_p2, __p1_p3 == __p2_p3, __p1_p3 == __p1_p2]):
            return "Isosceles triangle"

        elif any([
            round((__p1_p2 ** 2 + __p1_p3 ** 2) ** 0.5, 3)
        ]):
            return "Right-angle triangle"


p1 = (1, 5)
p2 = (4, 10)
p3 = (7, 5)

p4 = (1, 5)
p5 = (1, 10)
p6 = (7, 5)

t1 = Triangle(p1, p2, p3)
t2 = Triangle(p4, p5, p6)

print("Triangle 1")
print("area: ", t1.area())
print("sides:", t1.sides())
print("perimeter:", t1.perimeter())
print("centroid:", t1.centroid())

print()
print("Triangle 2")
print("area: ", t2.area())
print("sides:", t2.sides())
print("perimeter:", t2.perimeter())
print("centroid:", t2.centroid())
print(round((5 ** 2 + 6 ** 2) ** 0.5, 3))

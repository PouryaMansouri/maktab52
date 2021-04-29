from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def sides(self):
        a = self.__a
        b = self.__b
        c = self.__c
        ab = sqrt((a[0] - b[0]) ** 2 + ((a[1] - b[1]) ** 2))
        ac = sqrt((a[0] - c[0]) ** 2 + ((a[1] - c[1]) ** 2))
        bc = sqrt((b[0] - c[0]) ** 2 + ((b[1] - c[1]) ** 2))
        return ab, ac, bc

    @property
    def perimeter(self):
        return sum(self.sides)

    @property
    def area(self):
        ab, ac, bc = self.sides
        p = self.perimeter / 2
        return sqrt(p * (p - ab) * (p - ac) * (p - bc))

    @property
    def centroid(self):
        a = self.__a
        b = self.__b
        c = self.__c
        return (a[0] + b[0] + c[0]) / 3, (a[1] + b[1] + c[1]) / 3

    @property
    def type(self):
        ab, ac, bc = self.sides
        if ab == ac == bc:
            return 'equilateral'
        elif ab == ac or \
                ab == bc or \
                ac == bc:
            return 'Isosceles'
        elif sqrt(ab ** 2 + ac ** 2) == bc or \
                sqrt(ab ** 2 + bc ** 2) == ac or \
                sqrt(ac ** 2 + bc ** 2) == ab:
            return 'right'
        else:
            return 'Unknown'


t1 = Triangle((0, 0), (5, 0), (0, 5))
print(t1.sides)
print(t1.perimeter)
print(t1.area)
print(t1.type)
print(t1.centroid)

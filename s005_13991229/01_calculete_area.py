#  S = 1/2  |XA ( YB - YC ) + XB ( YC - YA ) + XC ( YA - YB ) |

class Triangle:
    def __init__(self, a, b, c):
        self.vertex1_x = a[0]
        self.vertex1_y = a[1]
        self.vertex2_x = b[0]
        self.vertex2_y = b[1]
        self.vertex3_x = c[0]
        self.vertex3_y = c[1]

    def area(self):
        return 0.5 * (self.vertex1_x * (self.vertex2_y - self.vertex3_y) + \
                      self.vertex2_x * (self.vertex3_y - self.vertex1_y) + \
                      self.vertex3_x * (self.vertex1_y - self.vertex2_y))


if __name__ == '__main__':
    a = [0, 0]
    b = [3, 0]
    c = [2, 2]

    triangle1 = Triangle(a, b, c)
    print(triangle1.area())

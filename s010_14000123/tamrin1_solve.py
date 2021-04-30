class Triangle:

    def __init__(self, a, b, c):
        self.A, self.B, self.C = a, b, c
        self.set_A(*a)

    @property
    def A(self):
        return self.__A

    @property
    def B(self):
        return self.__B

    @property
    def C(self):
        return self.__C

    @A.setter
    def A(self, _):
        self.__A = _

    @B.setter
    def B(self, _):
        self.__B = _

    @C.setter
    def C(self, _):
        self.__C = _

    @staticmethod
    def prepare_vertex(x, y):
        ...
        return int(x), int(y)

    def set(self, name, x, y):
        setattr(self, '__' + name, self.prepare_vertex(x, y))

    def set_A(self, x, y):
        ...

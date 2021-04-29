# class Class1:
#
#     def __iter__(self):
#         self.n = -1
#         return self
#
#     def __next__(self):
#         self.n += 1
#         if self.n < 10:
#             return self.n ** 2
#         raise StopIteration("N < 10")
#
#
#
# x = iter(Class1())
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print('For:')
# for i in x:
#     print(i)
py_range = range


class range:
    def __init__(self, start: int, end: int = None, step: int = 1):
        self.start = start
        self.end = end
        self.step = step
        if self.end is None and self.step > 0:
            self.i = 0
            self.end = self.start
            self.start = 0
        elif self.step > 0:
            self.i = self.start
        else:
            self.end, self.start = self.start, self.end

    def __iter__(self):

        return self

    def __next__(self):
        if self.step > 0:
            if self.start <= self.i < self.end:
                i = self.i
                self.i += self.step
                return i
            raise StopIteration("Finish")
        elif self.step < 0:
            if self.start <= self.i < self.end:
                i = self.i
                self.i -= self.step
                return i
            raise StopIteration("Finish")
        else:
            raise StopIteration("Step == 0")


# for j in iter(range(10)):
# print(j)
def tester(start, end=None, step=1):
    if end:
        print(list(py_range(start, end, step)))
        print(list(range(start, end, step)))
        return list(range(start, end, step)) == list(py_range(start, end, step))
    else:
        print(list(range(start)))
        print(list(py_range(start)))
        return list(range(start)) == list(py_range(start))


print("test1")
print(tester(10))
print("test2")
print(tester(10, 1))
print("test3")
print(tester(1, 10))
print("test4")
print(tester(1, 10, 3))
print("test5")
print(tester(10, 20))
print("test6")
print(tester(10, 1, -1))
# print("test7")
# print(tester(10, 1, -2))
# print("test8")
# print(tester(10, 20, 2))

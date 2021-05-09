from functools import lru_cache
from num2words import num2words
from num2fawords import words


def remainder(n: int):
    def inner_function(func):
        def wrapper_function(*args, **kwargs):
            res = func(*args, **kwargs)
            return res % n

        return wrapper_function

    return inner_function


def sting_p(lang):
    def inner_function(func):
        def wrapper_function(*args, **kwargs):
            res = func(*args, **kwargs)
            to_string = num2words(res, lang=lang)
            return to_string

        return wrapper_function

    return inner_function


def farsi(func):
    def inner_function(*args, **kwargs):
        res = func(*args, **kwargs)
        to_string = words(res)
        return to_string

    return inner_function


def cache_decorator(func):
    memory = {}

    def inner_function(*args):
        self = args[0]
        alt2 = self.num1, self.num2
        alt1 = self.num2, self.num1
        if alt1 in memory:
            print(">>>find in cache: ")
            return memory[alt1]
        elif alt2 in memory:
            print(">>>find in cache: ")
            return memory[alt2]
        else:
            res = func(*args)
            memory[alt1] = res
            memory[alt2] = res
        return res

    return inner_function


class Multi:
    number1: int
    number2: int

    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    @property
    def num1(self):
        return self.__num1

    @num1.setter
    def num1(self, num: int):
        self.__num1 = int(num)

    @property
    def num2(self):
        return self.__num2

    @num2.setter
    def num2(self, num: int):
        self.__num2 = int(num)

    # @sting_p('en')
    # @farsi
    # @remainder(4)
    @cache_decorator
    def multi(self):
        return self.num1 * self.num2


m = Multi(3, 5)
print(m.multi())

m.num1 = 23
m.num2 = 613
print(m.multi())
print(m.multi())
m.num1 = 5
m.num2 = 3
print(m.multi())

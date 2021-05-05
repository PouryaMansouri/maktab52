import logging

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s —%(name)s: — %(levelname)s"
                           " - %(msecs)s —  %(message)s")


def process_timer(func):
    def inner_function(*args, **kwargs):
        logging.info(f"Function start - function:{func.__name__}")
        res = func(*args, **kwargs)
        logging.info(f"Function finish - function:{func.__name__}")
        return res

    return inner_function


def hsg(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            yield int(n)
        else:
            n = 3 * n + 1
            yield int(n)


class his:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        while self.n > 1:
            if self.n % 2 == 0:
                self.n = self.n / 2
                return int(self.n)
            else:
                self.n = 3 * self.n + 1
                return int(self.n)
        raise StopIteration("Finish")


@process_timer
def hailstone_g(n):
    for _ in hsg(n):
        print(_, end=',')
    print()


hailstone_g(10 ** 300)


@process_timer
def hailstone_iter(n):
    for _ in iter(his(n)):
        print(_, end=',')
    print()


hailstone_iter(10 ** 300)

import logging
from time import sleep

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


def is_primal(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


@process_timer
def primals_func(n: int):
    res = []
    for i in range(2, n + 1):
        if is_primal(i):
            res.append(i)
    return res


@process_timer
def test(a, b, c):
    sleep(2)
    print("finish")


# print(primals_func(9000))
test(1, 2, 3)

# def process_timer(func, *args):
#     f = func
#     number = args[0]
#     logging.info("Function start")
#     res = f(number)
#     logging.info("Function finish")
#     return res

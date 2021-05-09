# import logging
import timeit


#
# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s —%(name)s: — %(levelname)s"
#                            " - %(msecs)s —  %(message)s")
#
#
# def process_timer(func):
#     def inner_function(*args, **kwargs):
#         logging.info(f"Function start - function:{func.__name__}")
#         res = func(*args, **kwargs)
#         logging.info(f"Function finish - function:{func.__name__}")
#         return res
#
#     return inner_function


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


# @process_timer
def hailstone_g(n):
    num = [str(n)]
    for _ in hsg(n):
        num.append(str(_))
    return num




# @process_timer
def hailstone_iter(n):
    num = [str(n)]
    for _ in iter(his(n)):
        num.append(str(_))
    return num




def hailstone_g_time():
    SETUP_CODE = '''
from __main__ import hailstone_g
'''

    TEST_CODE = '''
nums = hailstone_g(100000)
    '''
    # timeit.repeat statement
    times = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=10000
                          )

    # printing minimum exec. time
    # print('hailstone_g time: {}'.format(min(times)))
    print('hailstone_g time: {}'.format(times))


def hailstone_iter_time():
    SETUP_CODE = '''
from __main__ import hailstone_iter
'''

    TEST_CODE = '''
nums = hailstone_iter(100000)
    '''
    # timeit.repeat statement
    times = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=10000
                          )

    # printing minimum exec. time
    # print('hailstone_iter time: {}'.format(min(times)))
    print('hailstone_iter time: {}'.format(times))


if __name__ == "__main__":
    nums = hailstone_iter(100000)
    print(", ".join(nums))
    print("-------------")
    nums2 = hailstone_g(100000)
    print(", ".join(nums2))
    hailstone_g_time()
    hailstone_iter_time()

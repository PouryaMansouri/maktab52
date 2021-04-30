from typing import Callable


def make_upper(func: Callable[[], str]) -> Callable:
    def inner_function():
        res = func()
        return res.upper()

    return inner_function


@make_upper  # Decorating...
def hello_world():
    return "Hello World!"


print(hello_world())

from typing import Literal, Tuple
import os


def files_generator(directory) -> Tuple[str, str, str]:
    for (root, dirs, files) in os.walk(directory):
        yield root, dirs, files


def convert_unit(unit: Literal['B', 'KB', 'MB', 'GB']):
    "Decorator: Returns converted result from byte"

    # TODO: Complete here
    def inner_function(func):
        res = func()
        return res

    return inner_function


#
# @convert_unit('KB')
def get_directory_size(directory: str) -> int:
    """Returns the `directory` size in bytes."""
    # TODO: Complete here
    size = 0
    for _ in files_generator(directory):
        root, dirs, files = _
        if dirs != None:
            for d in dirs:
                size += get_directory_size(directory + "/" + d)
        if not root.endswith("__") :
            print(root)
        size += os.path.getsize(root)
    return size


if __name__ == '__main__':
    # TODO: Complete hereos.getcwd()
    print(os.getcwd())
    a = get_directory_size(os.getcwd())
    print(a/1024)

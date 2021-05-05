import os
from typing import Tuple


def files_generator(directory) -> Tuple[str, str, str]:
    for (root, dirs, files) in os.walk(directory):
        yield root, dirs, files


def find_files(directory: str, file_format: str):
    for _ in files_generator(directory):
        res = [i for i in _[2] if i.endswith(file_format)]
        if res:
            path = _[0]
            print(f"in {path} address the is {len(res)} file with path {format}")
            print(res)
            print("--------------------------------------------------------")


path_directory = "/home/pourya/Documents/classes/maktab52/HomeWorks/"

find_files(path_directory, "py")

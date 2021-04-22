import os
import re


def file_size_in_folder(file_path):
    items_list = os.listdir(file_path)
    files_size = 0
    file_extension = re.compile('\..*')
    for _ in items_list:
        if os.path.isfile(_):
            if len(file_extension.findall(_)[0][1:]) >= 3:
                files_size += os.path.getsize(_)

    return files_size


path = "./"
print(file_size_in_folder(path))

import os
import re


def file_size_in_folder(file_path):
    items_list = os.listdir(file_path)
    files_size = 0
    file_extension = re.compile('\..*')
    file_list = []
    for _ in items_list:
        if os.path.isfile(_):
            if len(file_extension.findall(_)[0][1:]) >= 5:
                files_size += os.path.getsize(_)
                file_list.append(_)
    return files_size, file_list


path = "./"

files_size, file_list = file_size_in_folder(path)
print("file list:\n", file_list)
print("\nfile size: \n", files_size)

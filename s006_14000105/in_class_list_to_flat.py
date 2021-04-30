arr = [1, 2, 3, 4, [5, 6, [3, 5], [3, [3]]]]


# def open_list(array, list_out):
#     for i in array:
#         if str(i).isnumeric():
#             list_out.append(i)
#         else:
#             open_list(i, list_out)

def open_list(array):
    list_out = []
    for i in array:
        if isinstance(i, list):
            list_out.extend(open_list(i))
        else:
            list_out.append(i)

    return list_out



print(open_list(arr))

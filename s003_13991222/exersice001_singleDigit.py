# 1
def get_input():
    return input("Enter your number: ")


# 2
def string_to_int_list(string):
    return list(map(int, list(string)))


# 3
def sum_list_items(List):
    return sum(List)


# 4
def int_to_string(n):
    return str(n)


# main
n = get_input()

while (len(n) > 1):
    list_number = string_to_int_list(n)
    sum_list = sum_list_items(list_number)
    n = int_to_string(sum_list)

print(n)

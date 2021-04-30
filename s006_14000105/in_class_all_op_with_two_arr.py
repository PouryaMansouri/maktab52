arr1 = [-1, 7, 9, 2, 1]
arr2 = [-1, -1, 2, 5, 4]


def find_bigger(arr1, arr2):
    for i in range(len(arr1)):
        if arr1[i] > arr2[i]:
            return arr1, arr2
        elif arr1[i] < arr2[i]:
            return arr2, arr1


def sum_arr(arr1, arr2):
    arr3 = [0 for i in range(len(arr1) + 1)]
    for i in range(1, len(arr1) + 1):
        if arr1[-i] != -1:
            num1 = arr1[-i]
        else:
            num1 = 0

        if arr2[-i] != -1:
            num2 = arr2[-i]
        else:
            num2 = 0

        num3 = num1 + num2

        if num3 >= 10:
            sarbare = num3 // 10
            remain = num3 % 10
        else:
            sarbare = 0
            remain = num3

        arr3[-i] += remain
        arr3[-i - 1] += sarbare
    return arr3


def sub_arr(array1, array2):
    arr3 = [0 for i in range(len(arr1) + 1)]
    for i in range(1, len(array1) + 1):
        if array1[-i] != -1:
            num1 = array1[-i]
        else:
            num1 = 0

        if array2[-i] != -1:
            num2 = array2[-i]
        else:
            num2 = 0

        num3 = num1 - num2
        if num3 < 0:
            sarbare = -1
            remain = num3 + 10
        else:
            sarbare = 0
            remain = num3

        arr3[-i] += remain
        arr3[-i - 1] += sarbare
    return arr3


def multi(array1, array2):
    arr3 = [-1 for i in array2]
    arr3[-1] = 1


operators = {
    '+': lambda x, y: sum_arr(x, y),
    '*': lambda x, y: x * y,
    '-': lambda x, y: sub_arr(x, y),
}
op = input('op: ')

big, small = find_bigger(arr1, arr2)

print(operators[op](big, small))

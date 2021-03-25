arr1 = [-1, 7, 9, 2, 1]
arr2 = [-1, -1, 2, 5, 4]

# arr1 = [-1, 9, 2, 5, 4]
# arr2 = [1, 7, 9, 2, 1]
arr3 = [0 for i in range(len(arr1) + 1)]

operators = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
}
op = input('op: ')
for i in range(1, len(arr1) + 1):
    if arr1[-i] != -1:
        arr1_num = arr1[-i]
    else:
        arr1_num = 0

    if arr2[-i] != -1:
        arr2_num = arr2[-i]
    else:
        arr2_num = 0
    if op == '+':
        arr3_num = operators[op](arr1_num, arr2_num)
        if arr3_num >= 10:
            sarbare = arr3_num // 10
            remain = arr3_num % 10
        else:
            sarbare = 0
            remain = arr3_num

        arr3[-i] += remain
        arr3[-i - 1] += sarbare


    elif op == '-':
        arr3_num = operators[op](arr1_num, arr2_num)
        if arr3_num < 0:
            sarbare = -1
            remain = arr3_num + 10
        else:
            sarbare = 0
            remain = arr3_num

        arr3[-i] += remain
        arr3[-i - 1] += sarbare

print(arr3)

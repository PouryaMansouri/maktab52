# 1
def get_input():
    return int(input("Enter your number: "))


def fib(number) -> list:
    fib_list = [1, 1]
    for i in range(2, number):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list


n = get_input()
fib_list = fib(n)
print(*fib_list, sep=', ')

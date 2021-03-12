def is_primal(num):
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


n = int(input("enter number: "))

for i in range(2, n):
    if is_primal(i):
        print(i, end=" , ")


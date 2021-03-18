n = int(input("Enter a number: "))
print(">> Start (num=" + str(n) + ") <<")
while n:
    print(n * '*')
    n -= 1
print(">> End (num=" + str(n) + ") <<")

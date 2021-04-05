n = int(input("Enter a number: "))
print(">> Start (_=" + str(n) + ") <<")
while n:
    print(n * '*')
    n -= 1
print(">> End (_=" + str(n) + ") <<")

n = int(input("Enter a number: "))
print(">> Start (n="+ str(n) +") <<")
while n:
    print(n * '*')
    n -= 1
print(">> End (n="+ str(n) +") <<")
def fibo(n):
    if n<=2:
        return 1;
    else:
        return fibo(n-1)+fibo(n-2)

number = int(input())

for i in range(1,number+1):
    print(fibo(i),end='\t')
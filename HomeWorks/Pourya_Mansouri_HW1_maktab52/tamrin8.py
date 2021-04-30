n = int(input())
i = 1
while (n!=0):
    if i<n:
        print(i*'*')
        i+=1
    else:
        print(n*'*')
        n-=1

n = int(input())
k = 1
for i in range(0, n, 2):
    print((k * '*').center(n))
    k += 2
k-=2
for i in range(n):
    k -= 2
    print((k * '*').center(n))

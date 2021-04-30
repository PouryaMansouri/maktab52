n, m = map(int, input().split())


def GCM(n, m):
    minimun = min(m, n)
    maximun = max(m, n)
    gcm = 1
    for i in range(minimun, 1, -1):
        if minimun % i == 0 and maximun % i == 0:
            return i

    return gcm


def LCM(n, m):
    minimun = min(m, n)
    maximun = max(m, n)
    return (n / GCM(n, m)) * m


print(GCM(n, m))
print(int(LCM(n, m)))

def func(a, b=3, c=0, d=10):
    return a, b, c, d


res = func(1, c=12)
print(res)

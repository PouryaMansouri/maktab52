def range(start: int, end: int = None, step: int = 1):
    if end is None and step > 0:
        i = 0
        end = start
        start = 0
    elif step < 0:
        start, end = end, start
        i = end

    else:
        i = start

    while start <= i < end:
        yield i
        i += step


for i in range(10, -20, -4):
    print(i)

# args = ("===", 'Hello', 'World', '!')
# kwargs_dict = {'end': '===', 'sep': ' - '}
# print(*args, **kwargs_dict)

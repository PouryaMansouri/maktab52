n = input()
n_in_loop=0

while(len(n)>1):
    for i in n:
        n_in_loop += int(i)
    n = str(n_in_loop)
    n_in_loop = 0

print(int(n))
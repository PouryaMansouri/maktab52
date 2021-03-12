n = input()

#1

# n_in_loop=0
# while(len(n)>1):
#     for i in n:
#         n_in_loop += int(i)
#     n = str(n_in_loop)
#     n_in_loop = 0

# print(int(n))

#2

while(len(n)>1):
    # list_number = list(map(int,list(n)))
    # sum_llist = sum(list_number)
    # n= str(sum_llist)
    n = str(sum(map(int,n)))

print(n)



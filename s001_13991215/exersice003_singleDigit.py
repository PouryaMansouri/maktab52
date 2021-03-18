n = input()

#1

# n_in_loop=0
# while(len(num)>1):
#     for i in num:
#         n_in_loop += int(i)
#     num = str(n_in_loop)
#     n_in_loop = 0

# print(int(num))

#2

while(len(n)>1):
    # list_number = list(map(int,list(num)))
    # sum_llist = sum(list_number)
    # num= str(sum_llist)
    n = str(sum(map(int,n)))

print(n)



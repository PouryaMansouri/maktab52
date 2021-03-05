i = 0
while i < 30:
    i+=1
    print(i)

    if i %3 ==0:
        i+=1
        continue
    if i//11:
        break

print("The end")
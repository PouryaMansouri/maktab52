n= int(input())
seen=[[0 for i in range(n)] for j in range(n)] 
value=[[0 for i in range(n)] for j in range(n)] 
def paskal(row,col):
    if seen[row][col]==1:
        return value[row][col]
    
    seen[row][col]=1
    if col==0  or row==col:
        value[row][col]=1
    else:
        value[row][col]=paskal(row-1,col)+paskal(row-1,col-1)
    return value[row][col]
        
for i in range(n):
    for j in range(i+1):
        print(paskal(i,j),end=' ')  
    print()     
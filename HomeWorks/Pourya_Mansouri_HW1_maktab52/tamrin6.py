num1,op,num2 = input().split()
if op == '+':
    result= float(num1)+float(num2)
elif op== '-':
    result= float(num1)-float(num2)
elif op== '*':
    result= float(num1)*float(num2)
elif op== '/':
    if float(num2)==0:
        result = "Error(num2 = 0 in divition)"
    else:
        result= float(num1)/float(num2)
        
print("Result:",result)
num1 = float(input("number1 :"))
num2 = float(input("number2 :"))
op = input('operator: ')

if op == '+':
    print(num1+num2)
elif op== '-':
    print(num1-num2)
elif op== '*':
    print(num1*num2)
elif op== '/':
    if num2==0:
        print("Error")
    else:
        print(num1/num2)

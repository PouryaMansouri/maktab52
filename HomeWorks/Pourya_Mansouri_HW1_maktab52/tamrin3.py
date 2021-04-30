listOfNumbers = list(map(float,input().split()))

maximum = listOfNumbers[0]
minimum = listOfNumbers[0]
sumOfList=0
avarage = 0

for i in listOfNumbers:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
    sumOfList += i
    
avarage=sumOfList/len(listOfNumbers)

print("Maximum:",maximum)
print("Minimum", minimum)
print("Avarage",avarage)
    
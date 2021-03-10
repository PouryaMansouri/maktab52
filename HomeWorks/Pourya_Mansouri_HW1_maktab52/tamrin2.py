sentence = input()
sumOfDigit = 0
vowels = 0
digits = 0
allCharacter = {}
for ch in sentence.lower():
    allCharacter[ch]=allCharacter.get(ch,0)+1
    if ch in "0123456789":
        digits+=1
        sumOfDigit+=float(ch)
    elif ch in "aioue":
        vowels+=1

print("Vowels:",vowels)
print("Digits:",digits)
print("Sum of digits:",sumOfDigit)
for key in allCharacter.keys():
    if allCharacter[key]>1:
        print(str(key),allCharacter[key],sep=':',end=" , ")
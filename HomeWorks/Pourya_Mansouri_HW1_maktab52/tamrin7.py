listCharacters = list(input())
dictOfCharacter = dict()
for ch in listCharacters:
    dictOfCharacter[ch]=dictOfCharacter.get(ch,0)+1
    
for key in dictOfCharacter.keys():
    print(key,dictOfCharacter[key],sep=':')
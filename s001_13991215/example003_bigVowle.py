s= input()

for ch in s:
    if ch.lower() in 'aoeiu':
        print(ch.upper(),end='')
    else:
        print(ch,end='')
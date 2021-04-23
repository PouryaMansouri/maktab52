import translators

print(translators.google("hello", to_language='fa'))

with open('./tra.txt') as f:
    s = f.read()
print(translators.google(s, to_language='fa'))

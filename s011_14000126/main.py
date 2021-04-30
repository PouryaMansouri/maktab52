# f = open('example.txt', 'w')
# text = """Test test:
# > Hello world!
# > Date: 4/14/2021
# > Time: 1:18 pm
# """
# f.write(text)
# f.close()


f = open('example.txt')
print(f.readlines(5))
print(f.readlines())


# lines = f.readlines(15)
# lines = list(map(lambda x: x.strip(),lines))
# print(lines)
# print(f.readlines())
# print(f.readline(7))
# print(f.readline())
# print(f.readline())
# print(f.readline())
